#!/usr/bin/env python3
"""Compile the explicitly edited 360-shot film plan; never infer cameras from words.

PHAN_CANH_V3.json is the editable source of truth. --check verifies both the
plan's handoffs and every generated file without changing anything.
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

BASE_DIR = Path(__file__).resolve().parent
CAMERAS = {
    'W': 'Wide Establishing / Master Shot (W) — 24mm/35mm prime lens (24mm for expansive coastal/harbour geography; 35mm for architectural wide masters), 24 fps, deep spatial field (f/5.6), eye-level horizontal axis. Anchor full-body blocking, architectural boundaries and 180-degree screen direction within the fixed scene space.',
    'M': 'Medium Waist-Up Shot (M) — 50mm standard prime lens, 24 fps, natural human perspective (f/4.0), eye-level conversational lock. Keep upper bodies, hand-to-prop interactions and matched eyelines clearly readable in one stable frame.',
    'C': 'Intimate Portrait Close-Up (C) — 85mm prime lens, 24 fps, shallow depth of field (f/2.8) at eye level. Isolate facial micro-expressions, subtle breathing, natural eye movement and Vietnamese lip-sync with soft background separation; no camera orbit.',
    'I': 'Tactile Macro Insert Shot (I) — 85mm close-focus lens, 24 fps (f/4.0), angled directly at the active hands and fixed scene prop. Keep finger mechanics and object texture razor-sharp with zero hesitation or camera shake.',
    'T': 'Steadicam Lateral Tracking Shot (T) — 35mm prime lens, 24 fps (f/4.0), gliding smoothly at pedestrian eye level parallel to the subject along the established movement axis. No whip pan, drone lift or reverse-axis jump.',
    'H': 'Controlled Shoulder-Rig Handheld Action Shot (H) — 35mm prime lens, 24 fps, 150-degree crisp action shutter (f/4.0) with grounded, organic physical energy from one fixed side of the 180-degree axis. Keep defensive parries, posture shifts and spatial geometry clear without chaotic shake.',
    'O': 'Over-The-Shoulder / Point-of-View Shot (O) — 50mm prime lens, 24 fps (f/3.5), framing the foreground observer shoulder/head anchor against the facing speaker. Maintain strict 180-degree eyeline match and depth separation.',
    'P': 'Deliberate Dolly Push-In Shot (P) — 50mm prime lens, 24 fps (f/3.2), advancing smoothly along a straight optical track toward the subject at eye level. Build psychological weight organically without optical zoom, lens change or orbit.',
}
TRANSITIONS = {
    'OPEN': 'Cắt thiết lập thời gian/không gian',
    'CUT': 'Cắt dựng đúng vị trí/ánh nhìn',
    'CONTINUE': 'Nối đúng frame, hành động tiếp diễn',
    'MATCH': 'Match cut hình dạng/tư thế, không morph',
    'J': 'J-cut: âm mới đến trước hình',
    'L': 'L-cut: âm cũ đi qua cú cắt',
}
GENERIC_VOICES = {
    'BROKER': 'Unknown caller: filtered Southern Vietnamese male voice, identity concealed. Voice only, never add a caller body to this shot.',
    'RADIO': 'Radio operator: concise Southern Vietnamese voice through radio compression, off screen.',
    'EXTRA': 'The unnamed background person specified by the action: natural Southern Vietnamese voice, no new named lead character.',
    'OFFICER': 'Unnamed assisting officer: composed Southern Vietnamese voice, no new named lead character.',
}
DETAIL_FIELDS = ('intent','composition','blocking','performance','focus','texture','sound_detail','rhythm')
DRAMA_FIELDS = ('dramatic_question_vi','turn_vi','hook_vi','payoff_or_setup_vi','tension')


def edition(plan: dict) -> str:
    return '3.1' if plan.get('editorial_revision')=='3.1' else '3'


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


def validate(plan: dict, shots: list[dict]) -> None:
    errors = []
    if plan.get('schema_version') != 3 or plan.get('aspect_ratio') != '16:9':
        errors.append('Expected schema 3 and full-frame 16:9')
    if [s['number'] for s in plan['scenes']] != list(range(1, 61)):
        errors.append('Scenes must be exactly 01–60 in order')
    if len(plan['identities']) != 9:
        errors.append('Keep the nine approved lead identities')
    for identity in plan['identities'].values():
        try:
            UUID(identity['media_id'])
        except (ValueError, KeyError):
            errors.append('Invalid reference UUID')
    for s in plan['scenes']:
        if [c['number'] for c in s['clips']] != list(range(1, 7)):
            errors.append(f"Scene {s['number']} needs six ordered clips")
        if edition(plan)=='3.1':
            drama=s.get('dramaturgy',{})
            if any(k not in drama for k in DRAMA_FIELDS):
                errors.append(f"Scene {s['number']}: missing dramatic progression")
            if not isinstance(drama.get('tension'),int) or not 1<=drama.get('tension',0)<=5:
                errors.append(f"Scene {s['number']}: tension must be an editorial level from 1 to 5")
            for req_key in ('spatial_lock_en', 'fixed_objects_en', 'spatial_lock_vi', 'fixed_objects_vi'):
                if not isinstance(s.get(req_key), str) or len(s.get(req_key, '').strip()) < 20:
                    errors.append(f"Scene {s['number']}: missing or incomplete {req_key}")
    seen_actions = {}
    seen_lines = {}
    for i, c in enumerate(shots):
        p = shots[i-1] if i else None
        if edition(plan)=='3.1':
            detail=c.get('cinematic',{})
            if any(not isinstance(detail.get(k),str) or len(detail[k].strip())<12 for k in DETAIL_FIELDS):
                errors.append(f"{c['id']}: incomplete specific directing detail")
            words=sum(len(detail.get(k,'').split()) for k in DETAIL_FIELDS)
            if not 55<=words<=280:
                errors.append(f"{c['id']}: directing detail must be useful and bounded, got {words} words")
        if c['location'] not in plan['locations'] or c['camera'] not in CAMERAS:
            errors.append(f"{c['id']}: unknown location/camera")
        if c['transition'] not in TRANSITIONS:
            errors.append(f"{c['id']}: unknown transition")
        if c['number'] == 1 and c['transition'] == 'CONTINUE':
            errors.append(f"{c['id']}: scene entry must be an explicit editorial cut")
        for k in c['characters']:
            if k not in plan['looks']:
                errors.append(f"{c['id']}: unknown appearance {k}")
        if len({base_key(plan,k) for k in c['characters']}) != len(c['characters']):
            errors.append(f"{c['id']}: duplicate identity with two appearances")
        for k in c['props']:
            if k not in plan['props']:
                errors.append(f"{c['id']}: unknown prop {k}")
        for k in c.get('image_references',[]):
            if k not in plan['identities']:
                errors.append(f"{c['id']}: unknown photograph identity {k}")
        if c['transition'] == 'CONTINUE':
            if not p or any(c[k] != p[k] for k in ('location','camera','story_time')):
                errors.append(f"{c['id']}: continuous shot changes location/camera/time")
            if p and c['start_frame'] != p['end_frame']:
                errors.append(f"{c['id']}: broken exact-frame handoff")
            if p and set(c['characters']) != set(p['characters']):
                errors.append(f"{c['id']}: new appearance needs a fresh reference cut")
        action = re.sub(r'\W+', ' ', c['action'].casefold()).strip()
        if action in seen_actions:
            errors.append(f"{c['id']}: action repeats {seen_actions[action]}")
        seen_actions[action] = c['id']
        if not 1 <= len(c['dialogue']) <= 2:
            errors.append(f"{c['id']}: expected 1 or 2 brisk dialogue turns in every take")
        for d in c['dialogue']:
            if '@' in d['text'] or '"' in d['text']:
                errors.append(f"{c['id']}: spoken text contains injected tag/quote")
            if d['mode'] not in ('on','off','vo','device'):
                errors.append(f"{c['id']}: unknown voice mode")
            if not 6 <= len(d['text'].split()) <= 42:
                errors.append(f"{c['id']}: line length must be 6..42 words for brisk take")
            spoken = re.sub(r'\W+', ' ', d['text'].casefold()).strip()
            if spoken in seen_lines:
                errors.append(f"{c['id']}: exact line repeats {seen_lines[spoken]}")
            seen_lines[spoken] = c['id']
            speaker = d['speaker']
            if speaker not in plan['looks'] and speaker not in GENERIC_VOICES:
                errors.append(f"{c['id']}: missing speaker identity")
            if d['mode'] == 'on' and speaker in plan['looks']:
                visible = {base_key(plan,k) for k in c['characters']}
                if base_key(plan,speaker) not in visible:
                    errors.append(f"{c['id']}: visible speaker missing from cast")
        if 35 <= c['scene'] <= 53 and 'SON' in c['characters']:
            errors.append(f"{c['id']}: olive wardrobe inside black-suit sequence")
        if c['scene'] < 54 and 'HA_N' in c['characters']:
            errors.append(f"{c['id']}: clean clothes before station change")
    if len(shots) != 360 or len(shots)*plan['clip_seconds'] != 3600:
        errors.append('Expected 360 ten-second production clips')
    # Story-specific handoffs whose errors would invalidate the climax.
    index = {c['id']:c for c in shots}
    for key in ['28.4','34.2','45.4','48.5','52.2','52.5']:
        if key not in index:
            errors.append(f'Missing continuity anchor {key}')
    opened = [c['id'] for c in shots if 'WATCH_OPEN' in c['props']]
    if not opened or opened[0] != '52.2':
        errors.append('The first open-watch shot must be 52.2')
    if any('HA_R' in c['characters'] and (c['scene'],c['number']) < (52,6) for c in shots):
        errors.append('Rescued scarf appearance starts only after its documented return')
    if errors:
        raise ValueError('\n'.join(errors))


def person_lock(plan: dict, key: str, c: dict) -> str:
    base, age, outfit = plan['looks'][key]
    identity = plan['identities'][base]
    face = identity['identity']
    if base == 'HAINGOC' and (c['scene'],c['number']) >= (49,4):
        face = face.replace(', jade bracelet on LEFT wrist','')
        outfit += '; bracelet removed at 49.3 and remains in evidence, wrists bare'
    notes = []
    if base == 'SON' and key not in ('SON_Y','SON_Y_S','SON_O'):
        if (25 <= c['scene'] <= 27 or c['scene'] >= 29 or
                c['scene'] == 28 and c['number'] >= 4) and c['scene'] < 60:
            notes.append('LEFT wrist bandage from 25.1 onward; right hand uninjured')
        if 28 <= c['scene'] < 60 and key != 'SON_P':
            notes.append('unarmed: complete handgun case was surrendered at 28.4')
        if c['scene'] == 38:
            notes.append('current-day bare hands in this return from memory')
    if base == 'DUNG' and (29,1) <= (c['scene'],c['number']) < (46,4):
        notes.append('cut original cuff ring remains on RIGHT wrist; no usable loose cuff end')
    if base == 'DUNG' and (c['scene'],c['number']) >= (46,4):
        notes.append('fresh custody cuffs applied at 46.4; the cut old cuff is removed and logged separately, not reused')
    if base == 'THANH' and 29 <= c['scene'] < 56:
        notes.append('one glasses arm bent, held by tape after rescue')
    extra = ' ' + '; '.join(notes) + '.' if notes else ''
    outfit_cap = outfit[:1].upper() + outfit[1:] if outfit else ''
    return (
        f"{identity['tag']} = {identity['name']}: same approved identity, age {age}; {face}. "
        f"Wardrobe & gear: {outfit_cap}.{extra} "
        f"Voice profile [VOICE_LOCK_{base} — Fixed {age}-year-old native Southern Vietnamese (Saigon) voice profile, strictly locked across all 360 clips]: {identity['voice']}."
    )


def dialogue_text(plan: dict, d: dict, t_window: str | None = None) -> str:
    if d['speaker'] in plan['looks']:
        base = base_key(plan, d['speaker'])
        identity = plan['identities'][base]
        speaker = f"{identity['name']} ({identity['tag']})" if d['mode']=='on' else identity['name']
        vlock = f"VOICE_LOCK_{base}"
    else:
        speaker = {'BROKER':'Người gọi giấu tên','RADIO':'Bộ đàm','EXTRA':'Người trong cảnh','OFFICER':'Cán bộ hỗ trợ'}[d['speaker']]
        vlock = f"VOICE_LOCK_{d['speaker']}"
    mode = {'on':'nói trong hình','off':'ngoài khung hình','vo':'lời dẫn ngoài hình','device':'qua thiết bị'}[d['mode']]
    tone = d.get('tone', '').strip()
    meta_parts = [p for p in (t_window, vlock if t_window else None, tone) if p]
    meta_str = f" [{' | '.join(meta_parts)}]" if meta_parts else ""
    return f"{speaker}, {mode}{meta_str}: {d['text']}"


def locked_voice_ids_summary(plan: dict, c: dict) -> str:
    """Summarize pre-defined VOICE_LOCK IDs for all characters speaking in this shot."""
    items = []
    for d in c.get('dialogue', []):
        spk = d['speaker']
        if spk in plan['looks']:
            base = base_key(plan, spk)
            ident = plan['identities'][base]
            items.append(f"VOICE_LOCK_{base} ({ident['name']} {ident['tag']}: {ident['voice']} — fixed native Saigon voice)")
        else:
            items.append(f"VOICE_LOCK_{spk} ({GENERIC_VOICES.get(spk, spk)})")
    return '; '.join(dict.fromkeys(items)) if items else 'No active speaker in this shot'


def second_by_second_action_breakdown(plan: dict, c: dict) -> str:
    """Provide contiguous hand-prop manipulation, body continuity, and lip-sync chain aligned to the exact beat timestamps (0.0s -> t1s -> t2s -> 10.0s)."""
    act = c['action'].strip()
    m = re.match(
        r'^0\.0–(\d+(?:\.\d)?)s:\s*(.+?)\s*\1–(\d+(?:\.\d)?)s:\s*(.+?)\s*\3–10\.0s:\s*(.+)$',
        act,
        flags=re.S,
    )
    if m:
        t1, _b1, t2, _b2, _b3 = m.groups()
    else:
        t1, t2 = '3.0', '6.5'
    spd = c.get('voice_speed', '1.05x')
    turns = c.get('dialogue', [])
    if len(turns) == 1:
        w1 = len(turns[0]['text'].split())
        d1 = min(8.2, max(3.5, round(w1 / 3.8, 1)))
        t_windows = [(0.3, round(0.3 + d1, 1))]
    elif len(turns) > 1:
        w1 = len(turns[0]['text'].split())
        w2 = len(turns[1]['text'].split())
        d1 = min(4.3, max(2.5, round(w1 / 3.9, 1)))
        d2 = min(4.3, max(2.5, round(w2 / 3.9, 1)))
        t1_end = round(0.3 + d1, 1)
        t2_start = round(t1_end + 0.3, 1)
        t2_end = min(9.4, round(t2_start + d2, 1))
        t_windows = [(0.3, t1_end), (t2_start, t2_end)]
    else:
        t_windows = []
    dlg_parts = []
    for d, (a, b) in zip(turns, t_windows):
        if d['speaker'] in plan['looks']:
            base = base_key(plan, d['speaker'])
            ident = plan['identities'][base]
            mode_note = 'on-screen lip-sync' if d['mode'] == 'on' else 'mouth closed (off-screen/VO/device)'
            dlg_parts.append(f"{a:.1f}–{b:.1f}s: {ident['name']} ({ident['tag']}) via VOICE_LOCK_{base} at {spd} ({mode_note})")
        else:
            dlg_parts.append(f"{a:.1f}–{b:.1f}s: VOICE_LOCK_{d['speaker']} at {spd}")
    dlg_summary = '; '.join(dlg_parts) if dlg_parts else 'No spoken dialogue; mouths remain naturally closed'
    return (
        f"\n[CONTIGUOUS SECOND-BY-SECOND CHOREOGRAPHY & MANIPULATION CHAIN (0.0s → {t1}s → {t2}s → 10.0s)]:\n"
        f"- 0.0s–{t1}s (Phase 1 — Start-Frame Continuation & Opening Manipulation): Start immediately at 0.0s from START FRAME ({c['start_frame'].rstrip('.')}; zero portrait flash) and execute the 0.0–{t1}s movement with 5 natural fingers and realistic prop weight, ending at the exact transition posture at {t1}s.\n"
        f"- {t1}s–{t2}s (Phase 2 — Contiguous Core Manipulation & Active Lip-Sync): Continue seamlessly at {t1}s from Phase 1 (zero pause, zero repeated gesture) to execute the {t1}–{t2}s physical manipulation; synchronize vocal delivery and mouth articulation ({dlg_summary}) while listeners keep mouths closed.\n"
        f"- {t2}s–10.0s (Phase 3 — Contiguous Follow-Through & 10.0s End-Frame Lock): Continue seamlessly at {t2}s from Phase 2 to execute the {t2}–10.0s closing movement, locking final posture, prop placement, and 180-degree eyeline at 10.0s to match END FRAME ({c['end_frame'].rstrip('.')})."
    )


VOICE_DIRECTION = (
    'Natural native Southern Vietnamese conversational speech, authentic Saigon cadence, '
    'subtle human vocal imperfections, emotionally motivated phrasing, organic breath control, '
    'natural pitch variation, relaxed articulation and believable live-action film acting. '
    'Never sound like a narrator, text-to-speech engine, audiobook reader or commercial voice-over.'
)

SPEECH_DIRECTION = (
    'Dialogue should flow as spontaneous human speech, with natural breath groups, '
    'subtle hesitation only when emotionally justified, realistic sentence stress, '
    'varied intonation and a believable conversational rhythm. '
    'Never deliver dialogue as a perfectly uniform sequence of words.'
)


def voice_speed_profile(c: dict) -> tuple[str, str, str]:
    """Return (speed_tag, pct_str, description) based on realistic human acting range (0.95x–1.25x)."""
    spd = c.get('voice_speed', '1.05x')
    profiles = {
        '0.95x': ('0.95x', '95%', 'Emotional / Grief / Intimate cadence (0.95x / 95%, range 0.90x–1.00x) — soft, breath-paced, emotionally weighted Southern Vietnamese delivery with natural pauses'),
        '1.00x': ('1.00x', '100%', 'Mystery / Suspense / Investigatory cadence (1.00x / 100%, range 0.95x–1.05x) — hushed, guarded, watchful Southern Vietnamese delivery'),
        '1.05x': ('1.05x', '105%', 'Normal Conversational cadence (1.05x / 105%, range 1.00x–1.10x) — natural everyday Saigon conversational flow with relaxed phrasing'),
        '1.15x': ('1.15x', '115%', 'Argument / Urgency / Confrontation cadence (1.15x / 115%, range 1.10x–1.20x) — firm, pressured, emotionally urgent Southern Vietnamese delivery'),
        '1.20x': ('1.20x', '120%', 'Action / Chase / Tactical cadence (1.20x / 120%, range 1.15x–1.25x) — decisive, breath-driven, high-stakes live-action Southern Vietnamese delivery'),
        '1.25x': ('1.25x', '125%', 'Peak Action / Combat Crisis cadence (1.25x / 125%, range 1.15x–1.25x) — sharp, adrenaline-charged Southern Vietnamese tactical delivery'),
    }
    return profiles.get(spd, profiles['1.05x'])


def emotional_performance_note(c: dict) -> str:
    """Derive shot-specific human emotional vocal performance guidance."""
    scene_cat = c.get('scene_category', 'DIALOGUE')
    spd = c.get('voice_speed', '1.05x')
    tones = [d.get('tone', '').strip() for d in c.get('dialogue', []) if d.get('tone')]
    tone_str = '; '.join(dict.fromkeys(tones)) if tones else ''
    perf = c.get('cinematic', {}).get('performance', '')
    base_map = {
        '0.95x': 'Buồn / Xúc động / Tâm sự (Emotional / Grief): slower tempo, lower intimate volume, genuine breath pauses and quiet emotional weight.',
        '1.00x': 'Bí ẩn / Dè chừng (Mystery / Suspense): low guarded voice, cautious phrasing, watchful breathing, never theatrical.',
        '1.05x': 'Đời thường / Đối thoại tự nhiên (Natural Saigon Conversation): relaxed everyday Southern cadence, natural word linking and genuine human warmth/tension.',
        '1.15x': 'Căng thẳng / Tranh luận / Khẩn cấp (Argument / Urgency): firm grounded voice, deliberate word stress, slightly quicker anxious or confrontational rhythm without nonstop shouting.',
        '1.20x': 'Hành động / Rượt đuổi (Action / Chase): quick, urgent, breath-connected phrases driven by physical movement and real exertion.',
        '1.25x': 'Cao trào / Xung đột trực diện (Peak Action / Combat): short, decisive, adrenaline-charged calls anchored in real physical effort and rapid breathing.',
    }
    note = base_map.get(spd, base_map['1.05x'])
    if tone_str:
        note += f" Line-specific vocal tone: {tone_str}."
    if perf:
        note += f" Physical acting link: {perf.split(' (Acting discipline:')[0]}"
    return note


def voice_block(plan: dict, c: dict) -> str:
    if not c['dialogue']:
        return 'No speech, narration or improvised vocal filler. Play the action and location sound.'
    turns = c['dialogue']
    spd, pct, spd_desc = voice_speed_profile(c)
    scene_cat = c.get('scene_category', 'DIALOGUE')
    wide_exterior_vehicle = c.get('camera') in ('W', 'T') and scene_cat in ('VEHICLE_CHASE', 'VEHICLE_RACE')
    if len(turns) == 1:
        w1 = len(turns[0]['text'].split())
        d1 = min(8.2, max(3.5, round(w1 / 3.8, 1)))
        t_windows = [f"0.3–{round(0.3 + d1, 1):.1f}s"]
        end = round(0.3 + d1, 1)
    else:
        w1 = len(turns[0]['text'].split())
        w2 = len(turns[1]['text'].split())
        d1 = min(4.3, max(2.5, round(w1 / 3.9, 1)))
        d2 = min(4.3, max(2.5, round(w2 / 3.9, 1)))
        t1_end = round(0.3 + d1, 1)
        t2_start = round(t1_end + 0.3, 1)
        t2_end = min(9.4, round(t2_start + d2, 1))
        t_windows = [f"0.3–{t1_end:.1f}s", f"{t2_start:.1f}–{t2_end:.1f}s"]
        end = t2_end
    modes = {d['mode'] for d in turns}
    if modes == {'on'} and wide_exterior_vehicle:
        rendering = f'Speaker inside or aboard the moving vehicle (nói trong hình) delivers the line at single target speed {spd} ({pct}); from this wide exterior vehicle angle prioritize natural driver posture and head sync without forcing a close-up mouth zoom.'
    elif modes == {'on'}:
        rendering = f'ONLY the active speaker (nói trong hình) moves their lips at single target speed {spd} ({pct}) with natural Southern Vietnamese jaw, lip and cheek movement (never over-open the mouth on every syllable; keep acting and moving naturally while speaking); all listeners keep their mouths naturally closed and react through eyes and posture.'
    elif modes == {'vo'}:
        rendering = f'Internal character thought / voice-over only (lời dẫn ngoài hình) at single target speed {spd} ({pct}); all visible mouths remain completely closed at rest while physical action unfolds.'
    elif modes == {'off'}:
        rendering = f'Off-screen speech (ngoài khung hình) at single target speed {spd} ({pct}); do not add the speaker into frame or animate the visible listener speaking.'
    elif modes == {'device'}:
        rendering = f'Speech heard through the established communication device (qua thiết bị) at single target speed {spd} ({pct}); no caller body added to this shot.'
    else:
        rendering = f'Follow each turn mode strictly at single target speed {spd} ({pct}) (nói trong hình = only the active speaker moves their lips with natural Southern Vietnamese articulation when face is in range; lời dẫn ngoài hình / ngoài khung hình / qua thiết bị = visible mouths remain naturally closed).'
    prefixes = [GENERIC_VOICES[d['speaker']] for d in turns if d['speaker'] in GENERIC_VOICES]
    prefix_block = ('\n'.join(dict.fromkeys(prefixes)) + '\n') if prefixes else ''
    lines_block = '\n'.join(dialogue_text(plan, d, t_windows[i]) if isinstance(t_windows, list) else dialogue_text(plan, d, t_win) for i, (d, t_win) in enumerate(zip(turns, t_windows)))
    turn_label = 'two natural back-and-forth conversational turns' if len(turns) > 1 else 'one natural, emotionally grounded spoken line'
    total_w = sum(len(d['text'].split()) for d in turns)
    return (
        f"Delivery & Timing: 0.3–{end:.1f}s, {turn_label} ({total_w} Vietnamese words — calibrated for natural breathing, emotional phrasing and single target speed {spd} ({pct}) [{spd_desc}]).\n"
        f"Lip-Sync & Voice Control: {rendering}\n"
        f"{prefix_block}{lines_block}\n"
        f"Spoken Audio Rule: Only the Vietnamese words after the final colon (:) are spoken aloud. Never read names, @tags, timestamps or bracketed vocal notes. No captions."
    )


def prop_detail(plan: dict, key: str, c: dict) -> str:
    if key=='MARKS':
        changes={'01.5':(0,1),'07.1':(1,2),'12.1':(2,3),'19.2':(3,4),'28.5':(4,6),'34.1':(6,7)}
        if c['id'] in changes:
            before, after = changes[c['id']]
        else:
            sc_num = (c['scene'], c['number'])
            if sc_num < (1, 5):
                before = after = 0
            elif sc_num < (7, 1):
                before = after = 1
            elif sc_num < (12, 1):
                before = after = 2
            elif sc_num < (19, 2):
                before = after = 3
            elif sc_num < (28, 5):
                before = after = 4
            elif sc_num < (34, 1):
                before = after = 6
            else:
                before = after = 7
        return f'Same wooden doorframe. Exactly {before} tally marks at the start and {after} at the end of THIS shot. No other tally row.'
    if key=='WATCH':
        detail='ONE silver pocket watch with engraved flower lid, same chain, lid CLOSED in this shot. No second matching watch.'
        if c['scene'] in (6,33):
            return detail+' Before the escape it is intact and ticking softly. Do not open it.'
        if c['scene']==8 and c['number']<4:
            return detail+' Before the impact it is intact and running inside the closed case. No inside photograph is visible.'
        if c['id']=='08.4':
            return detail+' It starts intact and running; the impact dents the closed case and stops it. Never open the lid to demonstrate the damage.'
        if c['scene']<52:
            return detail+' After the escape it has stopped; do not add ticking or show the inner photo.'
        return detail+' It runs again after 52.3; never open it again as a new reveal.'
    if key=='WATCH_OPEN':
        if c['id']=='52.2':
            return 'The SAME single silver watch. Lid CLOSED in start frame and opened only during this action; cracked glass and small photo of Hạ revealed inside. Hands remain stopped. No second watch.'
        running = 'Starts stopped and resumes only when wound in this shot.' if c['id']=='52.3' else 'Hands already running; do not repeat opening or winding.'
        return 'The SAME single silver watch, lid OPEN, cracked glass, small photo of Hạ inside lid. '+running
    return plan['props'][key]


def transition_text(c: dict, previous: dict|None) -> str:
    if previous is None:
        return 'Film opening hook. Start directly at 0.0s with purposeful physical movement and opening narration at 0.3s to introduce the protagonist, coastal setting and 7-day stakes; no logo, recap, fade-in or dead pause.'
    prefix = f"Previous editorial shot: {previous['id']}, ending with {previous['end_frame']}\n"
    if c['transition']=='CONTINUE':
        return prefix + 'Use that last frame as this start frame. Preserve lens, axis, positions, light and props. Continue the physical action seamlessly from 0.0s; do not replay the preceding gesture or words. No freeze at the seam.'
    cut = {
        'OPEN':'Scene-opening editorial cut to the explicitly stated new time/place. Establish the new composition and dramatic stakes from 0.0s with purposeful action and natural dialogue at 0.3s.',
        'CUT':'Intentional editorial cut, not a continuous take. Start cleanly in the new composition; preserve compatible 180-degree screen direction and matched eyelines. No morph or duplicated gesture.',
        'MATCH':'Intentional match cut using the related shape or pose. Cut cleanly to the new time/place and advance the action naturally from 0.0s; no transformation, morph, dissolve or replay of the old shot.',
        'J':'J-cut in the edit: introduce the incoming location sound about 0.25s before the picture cut, then begin the new shot action and dialogue naturally. This generated clip contains only the new shot, not a two-location montage.',
        'L':'L-cut in the edit: retain the preceding diegetic sound about 0.25s after the picture cut while the new shot action begins at 0.0s. This generated clip contains only the new shot.',
    }[c['transition']]
    return prefix + cut


def render_prompt(plan: dict, c: dict, previous: dict|None, following: dict|None) -> str:
    continuous = c['transition']=='CONTINUE'
    if continuous:
        head = f"Continue the scene seamlessly from the final frame of clip {previous['number']}. Same composition at the seam, natural new action immediately after the seam."
    else:
        head = '[FORMAT]'
    location, sound = plan['locations'][c['location']]
    sound = c.get('sound_override', sound)
    locks = '\n'.join(person_lock(plan,k,c) for k in c['characters']) or 'No named lead visible. Only the unnamed background people explicitly specified below.'
    picture_refs = '\n'.join(f"{plan['identities'][k]['tag']}: approved face for the PRINTED PHOTOGRAPH ONLY. Do not add this person physically to the room or street." for k in c.get('image_references',[]))
    picture_refs = '\n[PICTURE-ONLY REFERENCES]\n'+picture_refs+'\n' if picture_refs else ''
    prop_text = '\n'.join(f'- {prop_detail(plan,p,c)}' for p in c['props']) or 'No new featured prop. Preserve already established carried items; introduce no extra symbolic objects.'
    note = c.get('wardrobe_note','')
    if c.get('time_ellipsis'):
        note += '\nTime ellipsis: ' + c['time_ellipsis'] + '.'
    end = c['end_frame']
    if following:
        out = f"Next shot {following['id']}: {TRANSITIONS[following['transition']]}. Do not perform its action inside this clip."
    else:
        out = 'End the film on this living composition. Any title and final fade are added in the edit, never generated inside the image.'
    scene_obj = plan['scenes'][c['scene']-1]
    spatial_lock_en = scene_obj.get('spatial_lock_en', '')
    fixed_objects_en = scene_obj.get('fixed_objects_en', '')
    spatial_block = (
        f"\n[FIXED SCENE SPATIAL LOCK — Cố định không gian xuyên suốt Cảnh {c['scene']:02d} (Clip 1–6)]\n"
        f"{spatial_lock_en}\n"
        f"Strict spatial rule: Lock this exact spatial geometry, compass axis and architectural boundary across all 6 clips (Clip 1–6) of Scene {c['scene']:02d}.\n"
    ) if spatial_lock_en else ''
    object_inventory_block = (
        f"[FIXED SCENE OBJECT INVENTORY — Chỉ xoay quanh các vật thể cố định từ đầu tới cuối Cảnh {c['scene']:02d} (Clip 1–6)]\n"
        f"{fixed_objects_en}\n"
        f"Strict object rule: Revolve camera framing and character actions strictly around these fixed objects present from Clip 1 to Clip 6 of Scene {c['scene']:02d}; never spawn, morph or introduce any unstated objects or background clutter.\n"
    ) if fixed_objects_en else ''
    audio_bridge = scene_obj['outgoing_audio'] if c['number']==6 else ''
    if c['scene'] == 1 and c['number'] == 1:
        scene_intro = f"\n[FILM OPENING INTRODUCTION — Mở đầu phim: {scene_obj['title']}]\nIntroduce protagonist Sơn (Bóng Ma) arriving at Hòn Sóng coastal town with a 7-day deadline to rescue Hạ after being betrayed by the Rắn Đen syndicate. Start physical movement at 0.0s and opening voice-over at 0.3s.\n"
    elif c['number'] == 1:
        scene_intro = f"\n[SCENE OPENING HOOK — Mở cảnh {c['scene']:02d}: {scene_obj['title']}]\nScene goal: {scene_obj['purpose']} Establish the setting and dramatic stakes from 0.0s with natural movement and dialogue at 0.3s.\n"
    else:
        scene_intro = ''
    detail=c.get('cinematic',{})
    intent=f"\n[DRAMATIC INTENT — show through behaviour, never narrate this note]\n{detail['intent']}\n" if detail else ''
    perf_text = detail.get('performance', '')
    if perf_text and 'No exaggerated sadness' not in perf_text:
        perf_text = f"{perf_text.rstrip('.')} (Acting discipline: Micro-expression, subtle breathing, natural eye movement; three-layer progression from guarded reaction -> controlled breath -> settled resolve. No exaggerated sadness, no theatrical frown, no forced hero pose.)"
    elif perf_text and 'Micro-expression' not in perf_text:
        perf_text = f"{perf_text.rstrip('.')}. Acting discipline: Micro-expression, subtle breathing, natural eye movement."
    staging=f"\n[BLOCKING AND PERFORMANCE]\nBlocking: {detail['blocking']}\nPerformance: {perf_text}\n" if detail else ''
    surface=f"\n[VISIBLE TEXTURE]\n{detail['texture']}\n" if detail else ''
    is_action_shot = (c['camera'] == 'H') or (c['scene'] in (8, 12, 18, 23, 24, 29, 30, 41, 42, 43, 44, 46, 51) and c['camera'] in ('H', 'T'))
    shutter_spec = (
        '150-degree action shutter (24 fps) for crisp, sharp kinetic motion edges during physical action'
        if is_action_shot else
        '180-degree default cinema shutter (24 fps) for natural motion cadence and grounded dramatic pacing'
    )
    camera_contract = (
        'Continuity lock (CONTINUE): Inherit the exact camera position, focal length, horizon line, prop placement, eyeline and 180-degree movement axis from the final frame of the preceding clip; zero framing reset.'
        if continuous else
        'Continuity & Axis Lock: Lock character positions, props, eyelines and 180-degree movement axis across the single 10-second camera setup; never cut, whip-pan or reset framing inside the clip.'
    )
    cam_move_defaults = {
        'W': '0.0–3.0s: slow lateral dolly gliding gently with the subject entry; 3.0–6.5s: dolly slows and settles to hold the wide spatial geography; 6.5–10.0s: very subtle optical push-in to underscore isolation and dramatic weight. No snap zoom, no heavy shake, no axis jump.',
        'M': '0.0–3.0s: subtle lateral re-balance as the interaction begins; 3.0–6.5s: steady eye-level hold on the shared conversational axis; 6.5–10.0s: gentle 5% dolly push-in on the emotional turn. No snap zoom, no heavy shake, no axis jump.',
        'C': '0.0–3.0s: locked portrait framing on eyes and breathing; 3.0–6.5s: imperceptible slow push-in during spoken delivery; 6.5–10.0s: rock-steady hold on the three-layer micro-expression settle. No snap zoom, no heavy shake, no axis jump.',
        'I': '0.0–3.0s: crisp macro track-in with the hand approaching the prop; 3.0–6.5s: locked close-focus hold on tactile finger mechanics; 6.5–10.0s: steady settle on the final object state. No snap zoom, no heavy shake, no axis jump.',
        'T': '0.0–3.0s: smooth Steadicam lateral glide matching the subject stride; 3.0–6.5s: maintain parallel pace and constant distance along the 180-degree line; 6.5–10.0s: decelerate smoothly into the stopping mark. No snap zoom, no heavy shake, no axis jump.',
        'H': '0.0–3.0s: grounded shoulder-rig follow as physical tension initiates; 3.0–6.5s: controlled lateral pivot keeping both figures and prop clear; 6.5–10.0s: steady breathing settle into the end posture. No snap zoom, no heavy shake, no axis jump.',
        'O': '0.0–3.0s: anchor foreground shoulder silhouette and establish eyeline depth; 3.0–6.5s: subtle push past the shoulder anchor during the key exchange; 6.5–10.0s: hold locked over-the-shoulder tension. No snap zoom, no heavy shake, no axis jump.',
        'P': '0.0–3.0s: initiate slow, deliberate dolly push-in along the optical axis; 3.0–6.5s: sustain smooth forward glide as psychological weight builds; 6.5–10.0s: ease gently into the close final framing. No snap zoom, no heavy shake, no axis jump.',
    }
    if c['id'] == '01.1':
        lens_spec = '35mm, 24 fps, 180-degree shutter, eye-level, slow lateral dolly with subtle push-in. Camera glides gently with Sơn, keeping the coach on the left and the empty space toward the coastal town on the right.'
        cam_move = '0.0–3.0s: camera tracks gently laterally as Sơn steps down from the coach. 3.0–6.5s: as the coach pulls out of frame, the camera slows down and settles. 6.5–10.0s: camera pushes in very subtly toward Sơn, emphasizing his solitude against the empty coastal road. No snap zoom, no heavy shake, no axis jump.'
    else:
        lens_spec = f"{CAMERAS[c['camera']]} Shutter: {shutter_spec}."
        cam_move = detail.get('camera_movement', cam_move_defaults[c['camera']])
    framing = (
        f"\n- Framing & Angle Composition: {detail['composition']}\n"
        f"- Camera Movement Plan (0–10s): {cam_move}\n"
        f"- Optical Focus & Depth of Field: {detail['focus']}\n"
        f"- Camera Stability & Continuity Contract: {camera_contract}"
    ) if detail else f"\n- Camera Stability & Continuity Contract: {camera_contract}"
    rhythm=f"\nAction rhythm: {detail['rhythm']}" if detail else ''
    sound_specific=f"\nForeground motivated sound: {detail['sound_detail']}" if detail else ''
    scene_cat = c.get('scene_category', 'DIALOGUE')
    spd, pct, spd_desc = voice_speed_profile(c)
    fight_module = (
        '\n[CINEMATIC MARTIAL ARTS & FIGHT CHOREOGRAPHY — FIGHT_ACTION]\n'
        'Photorealistic live-action cinematic combat with professional stunt choreography. Fast, precise, powerful and physically believable movements with realistic body weight, balance, inertia and momentum. Strictly follow the 5-stage combat chain in ACTION: Attack → Defense → Contact/Reversal → Reaction → Recovery (maximum 2–3 core martial-arts exchanges in 10s, continuous choreography without frozen poses, realistic footwork, pivots, dodges, blocks and counterattacks, grounded cinematic camera movement with readable combat geography). No air-striking, no unmotivated falling, no wire-fu floating, and no repeated identical moves.\n'
        if scene_cat == 'FIGHT_ACTION' else ''
    )
    vehicle_module = (
        f'\n[HIGH-SPEED VEHICLE ACTION — {scene_cat}]\n'
        'Preserve locked vehicle/vessel identity, paint finish, body silhouette, wheels/hull and driver/pilot position. Wheels rotate in the exact forward direction matching travel velocity with realistic road parallax, suspension kinematics, tire friction, inertia, grip and steering angle. Co-directional vehicles keep consistent forward direction along the established axis. Never flip the 180-degree camera axis or slide sideways unmotivated.\n'
        if scene_cat in ('VEHICLE_CHASE', 'VEHICLE_RACE') else ''
    )
    sound_profile_map = {
        'FIGHT_ACTION': 'Scene sound profile (FIGHT_ACTION): Prioritize grounded footstep traction, rapid clothing movement, athletic breathing, simulated stunt contact acoustics and physical body-weight shifts alongside clear dialogue.',
        'VEHICLE_CHASE': 'Scene sound profile (VEHICLE_CHASE): Prioritize engine RPM, gearshifts, tire friction on wet coastal asphalt or boat hull spray, suspension load and wind rush synchronized with vehicle speed.',
        'VEHICLE_RACE': 'Scene sound profile (VEHICLE_RACE): Prioritize engine RPM, gearshifts, tire traction and wind rush synchronized with vehicle speed.',
        'EMOTIONAL_DRAMA': 'Scene sound profile (EMOTIONAL_DRAMA): Prioritize intimate natural breathing, subtle fabric rustle, natural room/coastal stillness and emotionally weighted vocal presence without masking ambience.',
    }
    scene_sound_profile = sound_profile_map.get(
        scene_cat,
        f'Scene sound profile ({scene_cat}): Prioritize clean, forward-mixed Southern Vietnamese dialogue over a balanced, realistic coastal/interior ambience bed that never masks vocal clarity.',
    )
    return f"""{head}
10 seconds, full-frame 16:9, 24 fps, photorealistic live-action Vietnamese neo-noir thriller. Shutter: {shutter_spec}. Scene category: {scene_cat} | Single target voice speed: {spd} ({pct}). Color grade: Cool shadows, restrained warm highlights, natural skin tones. ONE camera setup and ONE location; no internal montage, recap or closing fade.

[CHARACTERS — approved identities, wardrobe, carried gear and voice profiles]
{locks}
{note.strip()}
Character reference images are for identity locking only — NEVER display, flash or insert the static character portrait card or studio backdrop at 0.0s; start directly in the live-action scene.
{picture_refs}

[TIMELINE AND LOCATION]
Scene {c['scene']:02d}/60, clip {c['number']}/6; shot {c['id']}. Story time: {c['story_time']}. Scene classification: {scene_cat}.
{location}
Lighting & Color: {c['lighting']} Motivated directional light source with natural falloff; cool shadows, restrained warm highlights, natural Vietnamese skin tones.{spatial_block}{scene_intro}{intent}

[ACTION — 0–10s, one clear primary action in a continuous take]
{c['action']}{second_by_second_action_breakdown(plan, c)}
Single primary action rule: Execute ONE clear primary physical action from start state to end state with natural real-time weight, subtle breathing and zero repeated gestures.{rhythm}
{fight_module}{vehicle_module}{staging}

[CAMERA — Shot Size, Lens (24/35/50/85mm), Shutter, Movement & Continuity]
- Lens & Shot Type: {lens_spec}{framing}

[PROPS]
{object_inventory_block}Reference only; enact only the current ACTION, not a future handover.
{prop_text}
{surface}

[BODY, MOUTH AND FACE CONSISTENCY]
Lock character facial identity, hair, age, body proportions and wardrobe strictly to the approved references throughout the 10-second shot. No facial morphing during head turns or rapid movement. Eyes track the stated target with natural blinking. Every hand keeps five natural fingers and grips carried props with realistic weight, inertia and momentum; no teleportation, no sudden position resets, and no extra unscripted characters.

[VOICE ACTING & ADAPTIVE SPEECH DIRECTION]
Locked Character Voice ID(s) for this shot: {locked_voice_ids_summary(plan, c)}. Keep each character's pre-defined voice identity, pitch register, timbre and native Saigon accent 100% consistent across all 360 clips.
Single Target Voice Speed ({scene_cat}): {spd} ({pct}) — {spd_desc}.
Voice direction: "{VOICE_DIRECTION}"
Speech direction: "{SPEECH_DIRECTION}"
Emotional performance purpose: {emotional_performance_note(c)}
Cinematic lip-sync & breathing discipline: Complete dialogue within its assigned time window with organic breath control, natural jaw/lip/cheek articulation and realistic micro-expressions; continue natural breathing and physical action after the line finishes.

[DIALOGUE — Voice Profile, Timing (15–30 words/10s), Vocal Tone & Lip-Sync]
{voice_block(plan,c)}

[SOUND]
Continuous ambience bed: {sound}.{sound_specific}
{scene_sound_profile}
Audio & Vocal Mix Discipline: Keep spoken Southern Vietnamese dialogue clear, close and naturally grounded in the real acoustic space; never let rain, wind, boat engines, vehicles or room ambience drown out the voice; no artificial reverb, no robotic radio/narrator tone, and no unrequested background music score. Edit bridge: {audio_bridge or 'Follow the stated incoming/outgoing edit without restarting the ambience.'}

[EDIT IN — do not render the previous shot again]
{transition_text(c,previous)}

[START FRAME — state only, not an action to repeat]
{c['start_frame']}

[END FRAME — lock position, props, eyeline & movement axis]
{end}
Continuity lock: Hold final character position, prop placement, eyeline direction and 180-degree movement axis naturally into the cut.
{out}

[AVOID]
No identity drift, facial morphing or costume changes; no impossible body mechanics, floating objects or extra/fused fingers; no frozen movement, dead air pauses or repeated actions/lines from adjacent clips; no incorrect vehicle direction or wheel rotation; no camera-axis reversal, shifting room/street geometry or unintended cuts; no inaccurate lip-sync, rushed/clipped speech, robotic TTS/narrator delivery or extra dialogue; no subtitles, watermarks, logos or readable text overlays; no reference portrait flashes or studio backdrops at 0.0s or anywhere in the clip; no unnecessary slow motion, speed ramps, extra watches/scarves, wrong prop owner, real actor likeness, graphic injury, blood, gunfire or instructional drug-use detail.
"""


def render_scene_readme(plan: dict, scene: dict, items: list[dict]) -> str:
    n=scene['number']; start=(n-1)*60
    lines=[f"# {plan['title']} — Cảnh {n:02d}: {scene['title']}", '',
           f'**Bản {edition(plan)} · 6 clip × 10 giây · 16:9 đầy khung · nguồn PHAN_CANH_V3.json**', '',
           f"Phút {clock(start)}–{clock(start+60)} · Thời gian truyện: {scene['story_time']}", '',
           scene['purpose'], '',
           'Một clip là một cú máy. Chỉ dùng frame cuối làm đầu vào khi bảng ghi **CONTINUE**; các hàng khác là cú cắt có chủ đích và đính lại reference. Shot chỉ có người nền, không có reference được chỉ định, dùng text-to-video. Không dùng frame cũ để kéo qua địa điểm mới.', '',
           '| Clip | Cách nối vào | Đầu clip | Hành động mới | Cuối clip | Thoại |',
           '|---|---|---|---|---|---|']
    extra_header = []
    if scene.get('spatial_lock_vi') and scene.get('fixed_objects_vi'):
        extra_header += [
            '## Khóa Không Gian & Hệ Vật Thể Cố Định Xuyên Suốt Cảnh (Clip 1–6)',
            f"- **Không gian cố định toàn cảnh (Fixed Scene Space):** {scene['spatial_lock_vi']}",
            f"- **Hệ vật thể cố định từ đầu tới cuối cảnh (Fixed Scene Objects):** {scene['fixed_objects_vi']}",
            "- **Quy tắc bất biến:** Cả 6 clip (Clip 1–6) trong cảnh này chỉ xoay quanh đúng không gian và hệ vật thể cố định nêu trên; tuyệt đối không tự sinh thêm đồ vật lạ hay thay đổi bố cục không gian giữa chừng.",
            ''
        ]
    if scene.get('dramaturgy'):
        d=scene['dramaturgy']
        extra_header += [
            f"**Câu hỏi đang mở:** {d['dramatic_question_vi']}",
            f"**Móc vào cảnh:** {d['hook_vi']}",
            f"**Điểm bẻ:** {d['turn_vi']}",
            f"**Gieo / trả:** {d['payoff_or_setup_vi']}",
            ''
        ]
    if extra_header:
        lines[8:8] = extra_header
    for c in items:
        d=' / '.join(dialogue_text(plan,x) for x in c['dialogue']) or '—'
        lines.append(f"| [{c['number']}](clip-{c['number']}.md) | {c['transition']} · {TRANSITIONS[c['transition']]} | {c['start_frame']} | {c['action']} | {c['end_frame']} | {d} |")
    if edition(plan)=='3.1':
        lines+=['','## Phân cảnh chi tiết & Vật dụng mang theo (Chuẩn biên kịch 30 năm)','']
        for c in items:
            sp=c.get('screenplay_vi',{})
            gear_vi=sp.get('gear_vi','')
            beats_vi=sp.get('beats_vi','')
            lines += [
                f"### Clip {c['number']} ({c['id']}) · {c['location']} · Góc máy {c['camera']}",
                f"- **Không gian cố định của cảnh:** {scene.get('spatial_lock_vi','')}",
                f"- **Hệ vật thể cố định xoay quanh từ đầu tới cuối cảnh:** {scene.get('fixed_objects_vi','')}",
                f"- **Trang phục & Vật dụng mang theo:** {gear_vi}",
                f"- **Diễn biến 3 nhịp (0–10s):** {beats_vi}",
                f"- **Chỉ đạo diễn xuất:** {c['cinematic']['intent']} **Diễn xuất:** {c['cinematic']['performance']}",
                ""
            ]
    lines += ['', '**Âm nối sang cảnh sau:** '+scene['outgoing_audio'], '',
              '[Bảng nối toàn phim](../BANG_NOI_CLIP.md) · [Kịch bản](../KICH_BAN_60_PHUT.md) · [Khóa và đạo cụ](../FLOW_PROMPTS.md)', '',
              'Kiểm tra video render: mặt/đồ/đạo cụ, ánh nhìn, hướng đi, âm nền, không lặp động tác ở mối nối. Prompt quy định ý đồ; video vẫn cần xem nối đôi trước khi chốt dựng.', '']
    return '\n'.join(lines)


def render_script(plan: dict, shots: list[dict]) -> str:
    lines=[f"# {plan['title']}", f'## Kịch bản phân cảnh chi tiết bản {edition(plan)} — Chuẩn biên kịch điện ảnh 30 năm', '',
           '**60 đơn vị sản xuất × 6 clip × 10 giây = 60 phút hình nguồn.** Mỗi cảnh khóa chặt một không gian cố định và một hệ vật thể cố định xuyên suốt từ Clip 1 đến Clip 6; quản lý chặt chẽ trang phục, ba lô, túi xách, đồng hồ, sổ sách và đạo cụ cầm tay xuyên suốt 360 phân cảnh.', '',
           'Nguồn duy nhất: `PHAN_CANH_V3.json`. Hành động/camera viết tiếng Anh cho prompt kèm bản phân cảnh tiếng Việt 3 nhịp chi tiết. Tái sinh bằng `python3 build_full_60_scenes.py`; kiểm tra bằng `python3 build_full_60_scenes.py --check`.', '',
           'Sơn có bảy ngày trước chuyến tàu chuyển Hạ đi. Anh hợp tác với Mây, giao bằng chứng cho điều tra và chấp nhận trả giá. Kiên muốn Sơn im lặng, Bà Hai muốn lấy lại quyền kiểm soát. Cuộc trao đổi ở cảng bị phản bội; Dũng dùng chất Tê hư cấu giữ Sơn sống, cả hai phe đều nhận biết thuốc. Hạ để lại dấu và mở đường, Mây dẫn việc cứu người. Sơn cứu cả Kiên khỏi ngã rồi tự nhận còng.', '',
           '| Cảnh | Phút phim | Tên | Biến chuyển mới |', '|---|---|---|---|']
    for s in plan['scenes']:
        n=s['number']; lines.append(f"| {n:02d} | {clock((n-1)*60)}–{clock(n*60)} | {s['title']} | {s['purpose']} |")
    for s in plan['scenes']:
        n=s['number']; lines += ['',f"### CẢNH {n:02d}: {s['title']}",f"*Thời gian truyện: {s['story_time']}*",s['purpose'],'']
        if s.get('spatial_lock_vi') and s.get('fixed_objects_vi'):
            lines += [
                f"**Khóa không gian cố định toàn cảnh (Clip 1–6):** {s['spatial_lock_vi']}",
                f"**Hệ vật thể cố định từ đầu tới cuối cảnh (Clip 1–6):** {s['fixed_objects_vi']}",
                ''
            ]
        if s.get('dramaturgy'):
            d=s['dramaturgy']
            lines += [f"**Câu hỏi:** {d['dramatic_question_vi']}",f"**Móc vào:** {d['hook_vi']}",
                      f"**Điểm bẻ:** {d['turn_vi']}",f"**Gieo / trả:** {d['payoff_or_setup_vi']}",'']
        for c in (x for x in shots if x['scene']==n):
            d=' / '.join(dialogue_text(plan,x) for x in c['dialogue']) or '—'
            sp=c.get('screenplay_vi',{})
            props_str=', '.join(c['props']) if c['props'] else 'Không phát sinh đạo cụ mới'
            lines += [f"**Clip {c['number']} ({c['id']}) · {c['transition']} · {c['location']} · {c['camera']}**",
                      f"- **Trang phục & Vật dụng mang theo:** {sp.get('gear_vi', c.get('wardrobe_note',''))}",
                      f"- **Mã đạo cụ khóa xuyên cảnh (Fixed Scene Props):** `{props_str}`",
                      f"- **Diễn biến phân cảnh 3 nhịp (Tiếng Việt):** {sp.get('beats_vi','')}",
                      f"- **Đầu (Start Frame):** {c['start_frame']}",
                      f"- **Hành động 3 nhịp (Action Prompt):** {c['action']}",
                      f"- **Thoại (0.2s–9.4s):** {d}",
                      f"- **Cuối (End Frame):** {c['end_frame']}", '']
            if c.get('cinematic'):
                detail=c['cinematic']
                labels={'intent':'Ý đồ','composition':'Bố cục','blocking':'Vị trí / chuyển động',
                        'performance':'Diễn xuất','focus':'Điểm nét','texture':'Chất liệu',
                        'sound_detail':'Âm nổi','rhythm':'Nhịp diễn'}
                lines += [f'- {labels[k]}: {detail[k]}' for k in DETAIL_FIELDS]+['']
        lines.append('Âm nối sang cảnh sau: '+s['outgoing_audio'])
    return '\n'.join(lines)+'\n'


def render_handoffs(plan: dict, shots: list[dict]) -> str:
    lines=[f'# Bảng nối 359 mối ghép — bản {edition(plan)}', '',
           'Mỗi hàng là một điểm cắt thực sự giữa hai clip, kể cả qua ranh giới cảnh. CONTINUE mới dùng khung cuối làm start frame; các hàng CUT/OPEN/MATCH/J/L dùng reference của shot mới. Không chèn lại nửa giây cuối clip trước và không phát lại thoại.', '',
           '| Từ → tới | Loại nối | Cuối clip trước | Đầu clip sau | Âm thanh / lưu ý dựng |',
           '|---|---|---|---|---|']
    for a,b in zip(shots,shots[1:]):
        bridge=plan['scenes'][a['scene']-1]['outgoing_audio'] if a['number']==6 else ''
        if b['transition']=='J':bridge+=' Cho âm địa điểm mới vào trước hình khoảng 0,25 giây.'
        elif b['transition']=='L':bridge+=' Giữ đuôi âm cũ qua hình mới khoảng 0,25 giây rồi hạ tự nhiên.'
        elif b['transition']=='CONTINUE':bridge+=' Giữ cùng ống kính/trục/vị trí. Tiếp động tác, không lặp đoạn kết.'
        else:bridge+=' Cắt theo tư thế/ánh nhìn được ghi, không morph, không thêm cảnh đệm.'
        lines.append(f"| [{a['id']}]({ref(a)}) → [{b['id']}]({ref(b)}) | {b['transition']} | {a['end_frame']} | {b['start_frame']} | {bridge.strip()} |")
    return '\n'.join(lines)+'\n'


def render_beatmap(plan: dict) -> str:
    lines=['# Nhịp phim và câu hỏi giữ người xem — bản 3.1','',
           'Mức áp lực 1–5 dưới đây là chỉ dẫn biên tập, không phải điểm chất lượng hay dự đoán khán giả. Cảnh lặng vẫn cần một lựa chọn hoặc thông tin mới; không tạo cú lật giả ở mọi clip.', '',
           'Chặng đầu gắn đồng hồ bảy ngày với một người vắng mặt; chặng giữa khiến mỗi bằng chứng có cái giá; cao trào phá giao dịch và buộc Sơn chọn cứu người. Hậu truyện đi từ lời khai sang cuộc sống riêng của Hạ, một lần chia tay rồi một lần trở về.', '',
           '| Cảnh | Áp lực | Móc vào | Câu hỏi đang mở | Điểm bẻ | Gieo / trả |',
           '|---|---|---|---|---|---|']
    for s in plan['scenes']:
        d=s['dramaturgy']
        lines.append(f"| {s['number']:02d} · {s['title']} | {d['tension']}/5 | {d['hook_vi']} | {d['dramatic_question_vi']} | {d['turn_vi']} | {d['payoff_or_setup_vi']} |")
    if plan.get('reviewed_changes'):
        lines += ['', '## Các điểm đã rà và sửa thêm', '',
                  '| Vị trí | Vấn đề | Điều chỉnh |','|---|---|---|']
        for change in plan['reviewed_changes']:
            lines.append(f"| {change['id']} | {change['problem_vi']} | {change['fix_vi']} |")
    lines += ['', '## Cách đọc phần chỉ đạo chi tiết', '',
              '- **Intent:** tác động lên người xem, thể hiện bằng hành vi; không đọc thành lời dẫn.',
              '- **Composition / focus:** chủ thể và thứ tự nhận thông tin trong một setup; không thêm góc quay bên trong clip.',
              '- **Blocking:** tay đang giữ vật gì, khoảng cách và đường đi; giữ start/end đã khóa.',
              '- **Performance:** điều nhân vật muốn giấu hoặc muốn người đối diện làm, thể hiện bằng một phản ứng vừa đủ.',
              '- **Texture / sound:** chất liệu và âm thanh có nguồn trong cảnh; không thêm đạo cụ hay hiệu ứng gây giật mình.',
              '- **Rhythm:** thời gian quan sát, quyết định, hành động và dư âm, biến đổi theo từng shot thay vì chia đều ba nhịp.', '',
              'Xem bản render theo từng chuỗi cảnh để quyết định trim. Điểm im không phải đứng hình; cơ thể, vải, nước và âm phòng vẫn tiếp tục. Không dùng nhạc để thay phần căng thẳng chưa có trong hành động.', '']
    return '\n'.join(lines)


def render_locks(plan: dict) -> str:
    lines=[f'# Khóa hình, đạo cụ và điểm nối — bản {edition(plan)}', '',
           'Master 16:9 đầy khung, 24 fps. Một clip một camera setup; thoại tiếng Việt giọng miền Nam. Không đóng băng cuối clip, không tự tạo nhạc riêng từng đoạn. Nhạc và title làm trên timeline dựng.', '',
           '**Cách tạo:** clip ghi CONTINUE mở bằng `Continue…`, dùng frame cuối clip trước; mọi cú cắt khác mở bằng `[FORMAT]`, đính lại các reference có mặt. Shot chỉ có người nền, không chỉ định reference, dùng text-to-video. Qua ranh giới cảnh luôn là cú cắt biên tập rõ, phù hợp runner hiện tại. Không kéo một start frame qua đổi địa điểm/tuổi/trang phục.', '',
           '**Giọng ngoài hình:** chỉ khai báo giọng, không thêm người vào ảnh. Tag đứng ở trường người nói; không chèn tag hoặc thay tên bên trong câu được đọc.', '',
           '| Nhân vật | Handle | media_id đã có |', '|---|---|---|']
    for x in plan['identities'].values():lines.append(f"| {x['name']} | `{x['tag']}` | `{x['media_id']}` |")
    lines += ['', '## Biến thể dùng cùng danh tính', '',
              'Các UUID trên là reference danh tính đã có, không phải xác nhận rằng mọi ảnh biến thể đã được tạo. Trước khi render, kiểm tra ảnh đúng tuổi/trang phục, đặc biệt Sơn 20 tuổi, Bà Hai 35 tuổi và các giai đoạn nhiều năm sau. Không tạo thêm nhân vật mới cho mỗi bộ đồ.', '']
    for k,(base,age,outfit) in plan['looks'].items():
        lines.append(f"- **{k}** → `{plan['identities'][base]['tag']}`, {age} tuổi: {outfit}.")
    lines += ['', '## Quy tắc liên tục đã chốt', '',
              '- Đồng hồ duy nhất: Hạ tặng ở 06.5, hỏng do va đập ở 08.4; Sơn không mở trước 52.2. Ảnh Mây nhận ra ở 14 là ảnh rời. Mây giữ từ 34.4 tới 45.5, sau đó trả Sơn. Không có chiếc thứ hai ở cảnh cuối.',
              '- Khăn duy nhất bị xé: mảnh ngắn Sơn nhặt ở 10, phần dài Dũng để lại ở 18. Cả hai về Mây ở 34.3; phần dài trả Hạ ở 52.5. Không dùng khăn bất ngờ để trói Kiên.',
              '- Sổ đen/USB gốc giữ ở đồn sau 17.1; sổ đỏ/token theo chuyến thành phố. Bản gốc giao điều tra ở 34.5. Sơn chỉ mang phong bì bản sao tới cảng.',
              '- Sơn áo ô liu ở hiện tại đầu phim, vest tay trần ở 21.5–27 và 35–55. Hồi tưởng vẫn đúng biến thể riêng. Băng cổ tay TRÁI từ 25.1; tay phải không bị thương. Không cài hoa trong cao trào hiện tại.',
              '- Hạ váy xám đến hết 53, nhận lại khăn ở 52.5, thay đồ trắng/jean tại đồn trước 54.1. Trang phục sau cứu không tự đổi ngay khi thoát khỏi Kiên.',
              '- Mây dùng đúng hai còng trong chuyến thành phố: 23.5 và 24.5. Còng Dũng bị cắt xích ở 24.6, không biến thành còng dùng lại được. Mây nhận hai còng mới ở 35.1; một giữ Dũng, một giữ Sơn. Tổ hỗ trợ giữ Kiên bằng còng của họ.',
              '- Vũ khí của Sơn được giao toàn bộ cho Mây ở 28.4. Anh không mang súng ở cảng/hải đăng. Súng Kiên được thu làm vật chứng, không bị ném xuống biển.',
              '- Tê là chất hư cấu, gây bất động còn thở, thời gian hồi phục không cố định. Không dùng làm giả chết, không có mốc 38/40 phút hoặc chỉ dẫn áp dụng thực tế. Phản diện biết đúng thuốc của chúng.',
              '- Bảy vạch: 01→1; 07→2; 12→3; 19→4; 28.5 bù hai ngày đi thành phố→6; 34.1→7. Hạ không bắt đầu một dãy đếm tù mới ở kết phim.',
              '- Hải đăng: cửa chính phía đông; cửa kỹ thuật bắc; lan can biển phía nam. Mây thử đèn ở 16.5, Hạ giữ cửa bằng kẹp ở 45.4, tổ hỗ trợ vào ở 48.5, bật đèn theo lệnh ở 51.1.', '',
              '## Thư viện đạo cụ', '']
    for k,v in plan['props'].items():lines.append(f'- **{k}:** {v}')
    lines += ['', '## Âm thanh và bản dọc', '',
              'Giữ cùng giọng cho mỗi danh tính. J/L-cut thực hiện trên timeline bằng các track ambience tách rời; không yêu cầu model tạo hai địa điểm trong một clip. Dùng một bộ ambience xuyên cảnh, không reset nhạc ở mỗi mười giây. Với 40–43, làm reframe dọc riêng vì crop giữa sẽ mất một phe và con tin.', '',
              'Sau render, xem từng cặp clip và các ranh giới cảnh. Nếu có frame đệm lặp thì trim đúng phần đệm, không cắt mất động tác. Không kéo dài tĩnh để ép bản dựng thành đúng 60:00.', '']
    return '\n'.join(lines)


def render_characters(plan: dict) -> str:
    arcs={
        'SON':'Muốn đưa Hạ về, cần chịu trách nhiệm về việc mình đã làm. Từ nhìn đường để thoát sang lựa chọn ở lại khai. Không cứu người để được xóa tội. Bà Hai nhận anh khi 20 tuổi, cách hiện tại 25 năm.',
        'MAY':'Muốn tìm bạn và giữ thị trấn. Kiểm chứng trước khi hợp tác, bố trí hỗ trợ trước khi đi; trực tiếp dẫn cứu con tin và giữ luật sau cứu người.',
        'HA':'Muốn trở về mở sạp hoa. Để mảnh khăn, gửi dấu qua video, trì hoãn Kiên, giữ cửa bằng kẹp và tự bước ra khỏi tay hắn. Sau vụ án bắt đầu đời sống riêng.',
        'HAINGOC':'Ơn nuôi dưỡng thành quyền sở hữu. Muốn lấy lại Sơn và đường hàng; chọn giữ Sơn khỏi Kiên ở cảng nhưng vẫn phải chịu trách nhiệm về việc bán người.',
        'DUNG':'Muốn được Bà Hai công nhận. Ghen với Sơn, giữ người theo lệnh rồi vượt lệnh dùng Tê. Cuối cùng không còn ai để nhận lệnh giữ nữa.',
        'KIEN':'Mục tiêu xuyên suốt là bịt lời Sơn và nuốt đường hàng của Bà Hai. Bẫy bắt thất bại thì giữ Hạ để ép Sơn quay lại, không đổi động cơ tùy cú lật.',
        'THANH':'Từ người kiểm tra hồ sơ thành người bảo vệ tuyến dân và lần dấu cửa Hạ để lại. Sợ nhưng làm nhiệm vụ, không chỉ là con tin hoặc người gây cười.',
        'LINH':'Giữ người sống bằng theo dõi và hỗ trợ. Không hứa một phút tỉnh chính xác, không có thuốc giải thần kỳ xuất hiện để giải cốt truyện.',
        'BAY':'Bảo vệ người lạ vì từng thấy hành vi tử tế. Giữ lối cho dân, chuẩn bị xe cứu người, rồi trở lại bán cà phê; không cầm sào lao vào họng súng.',
    }
    lines=[f'# Chín nhân vật — hồ sơ thống nhất bản {edition(plan)}', '',
           'Tuổi hiện tại: Sơn 45, Mây 38, Hạ 32, Bà Hai 60. Quá khứ xa cách 25 năm: Sơn 20, Bà Hai 35. Mây và Hạ là bạn thuở nhỏ cùng xóm, không ghi cùng lớp. Hạ bị bắt vài tuần trước ngày Sơn tới thị trấn; không khóa 31 vạch khi lịch không cần số đó.', '']
    for key,x in plan['identities'].items():
        lines += [f"## {x['name']} · {x['tag']}", '',arcs[key],'',f"Nhận diện: {x['identity']}.",f"Giọng xuyên phim: {x['voice']}.",'', 'Biến thể và prompt ảnh tham chiếu:']
        for look,(base,age,outfit) in plan['looks'].items():
            if base==key:
                lines += [f'- **{look}:** Photorealistic reference of the SAME approved Vietnamese identity, age {age}, {outfit}. Plain grey studio background, full body and portrait, no text, no real actor likeness.']
        lines.append('')
    lines += ['Các ảnh biến thể là chỉ dẫn cần kiểm tra trước render, không phải media_id mới đã được cấp. Dùng đúng chín danh tính trong FLOW_PROMPTS.md; không gắn một ảnh tuổi 45 vào shot tuổi 20 rồi trông chờ câu chữ tự giải quyết hoàn toàn.', '']
    return '\n'.join(lines)


def outputs(plan: dict, shots: list[dict]) -> dict[str,str]:
    result={}
    for i,c in enumerate(shots):
        result[ref(c)]=render_prompt(plan,c,shots[i-1] if i else None,shots[i+1] if i+1<len(shots) else None)
    for s in plan['scenes']:
        n=s['number']; folder=f'canh-{n:02d}'
        result[f'{folder}/README.md']=render_scene_readme(plan,s,[c for c in shots if c['scene']==n])
        result[f'{folder}/caption.md']=f"# {plan['title']} · Cảnh {n:02d}: {s['title']}\n\n{s['purpose']}\n\nPhim hư cấu do AI tạo. Xem trọn mạch truyện trên bản phim dài.\n\n#kesongsot #bongma #phimvietai\n"
    result['KICH_BAN_60_PHUT.md']=render_script(plan,shots)
    result['BANG_NOI_CLIP.md']=render_handoffs(plan,shots)
    result['FLOW_PROMPTS.md']=render_locks(plan)
    result['NHAN_VAT.md']=render_characters(plan)
    if edition(plan)=='3.1':
        result['NHIP_PHIM_V3_1.md']=render_beatmap(plan)
    manifest={
        'version':3,
        'editorial_revision':edition(plan),
        'source':'PHAN_CANH_V3.json',
        'source_sha256':hashlib.sha256(json.dumps(plan,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
        'note':'Expected prompt fingerprints only. This manifest does not claim that videos were generated or approved. Existing unversioned renders must be reviewed/rerendered for v3.',
        'clips':[{'id':c['id'],'prompt':ref(c),'sha256':hashlib.sha256(result[ref(c)].encode()).hexdigest(),
                  'mode':'frames' if c['transition']=='CONTINUE' else 'ingredients' if c['characters'] or c.get('image_references') else 'text',
                  'previous':c['previous'],'transition':c['transition']} for c in shots],
    }
    result['RENDER_MANIFEST_V3.json']=json.dumps(manifest,ensure_ascii=False,indent=2)+'\n'
    return result


def main(argv: list[str]|None=None) -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Validate plan and generated files without writing')
    parser.add_argument('--validate-only',action='store_true',help='Validate editable plan without writing')
    parser.add_argument('--out-dir',type=Path,default=BASE_DIR)
    args=parser.parse_args(argv)
    plan=json.loads((BASE_DIR/'PHAN_CANH_V3.json').read_text(encoding='utf-8'))
    shots=normalize(plan)
    validate(plan,shots)
    counts=Counter(c['transition'] for c in shots)
    if args.validate_only:
        print(f'PASS: 60 scenes, 360 unique actions, 359 handoffs; {dict(counts)}')
        return
    files=outputs(plan,shots)
    if args.check:
        stale=[name for name,text in files.items() if not (args.out_dir/name).is_file() or (args.out_dir/name).read_text(encoding='utf-8')!=text]
        if stale:
            raise SystemExit('Missing/out-of-date outputs:\n'+'\n'.join(stale))
        print(f'PASS: {len(files)} generated files match canonical plan; 360 shots / 359 handoffs; {counts["CONTINUE"]} exact-frame continuations.')
        return
    for name,text in files.items():
        path=args.out_dir/name
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(text,encoding='utf-8')
    document_count=len(files)-481
    print(f'Generated {len(files)} files: 360 shot prompts, 60 scene guides, 60 captions, {document_count} film documents and render manifest.')
    print(f'Validated 359 handoffs; {counts["CONTINUE"]} continuous takes, remaining seams are explicit editorial cuts.')


if __name__=='__main__':
    main()
