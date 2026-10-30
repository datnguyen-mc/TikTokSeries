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
    'W': '35mm wide shot at human eye level, subject already moving at 0.0s. Preserve readable geography and screen direction.',
    'M': '50mm medium shot at eye level. Gesture, reaction and dialogue play in the same composition without dead air.',
    'C': '85mm close-up at eye level, natural shallow depth of field. Readable facial micro-expressions and natural lip sync, no orbit.',
    'I': '85mm detail shot. Hands and the relevant object move decisively from 0.0s and stay spatially readable.',
    'T': '35mm lateral tracking shot moving with the subject in the established direction. No whip pan, drone move or reverse-axis cut.',
    'H': '35mm controlled handheld medium-wide with kinetic energy. Keep the entire defensive action readable from one side of the axis.',
    'O': '50mm over-shoulder or point-of-view composition from the observer specified in the opening frame. Keep eyelines matched.',
    'P': '50mm steady, purposeful straight push-in, no lens change, no orbit. Tension builds while the final expression stays readable.',
}
SHUTTER = {'H': 'Crisp 150-degree shutter for sharp action'}
CLEAN_FRAME = ('Clean cinematic frame, never TV footage: no TV channel or broadcaster logo in any corner, no watermark, '
               'news ticker, lower-third, LIVE/REC badge, timestamp or other on-screen graphics. Screens and phones in the '
               'story never show a TV channel, news programme or broadcaster branding; story emblems stay simple unreadable shapes.')
# Words that invite the model to frame a shot as television news.
BROADCAST_WORDS = re.compile(r'\b(TV|television|broadcast\w*|newscast|news|tivi|truyền hình|thời sự|bản tin|phóng viên|báo đài)\b', re.I)
MAX_CLIP_SYLLABLES = 30  # FLOW_GUIDE: Omni rushes or truncates more speech than this in 10 s
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
    'BROKER': 'Unknown caller: filtered Southern Vietnamese male voice, identity concealed. Voice only, never add a caller body to this shot.',
    'RADIO': 'Radio operator: concise Southern Vietnamese voice through radio compression, off screen.',
    'EXTRA': 'The unnamed background person specified by the action: natural Southern Vietnamese voice, no new named lead character.',
    'OFFICER': 'Unnamed assisting officer: composed Southern Vietnamese voice, no new named lead character.',
}
DETAIL_FIELDS = ('intent','composition','blocking','performance','focus','texture','sound_detail','rhythm')
DRAMA_FIELDS = ('dramatic_question_vi','turn_vi','hook_vi','payoff_or_setup_vi','tension')


def edition(plan: dict) -> str:
    return '3.1' if plan.get('editorial_revision')=='3.1' else '3'


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
            beats=BEATS.match(c['action'])
            if not beats or not 0<float(beats[1])<float(beats[2])<10:
                errors.append(f"{c['id']}: action needs three timed beats chaining 0.0s to 10.0s")
            blocking=detail.get('blocking','').strip().rstrip('.')
            if blocking and blocking in c['action']:
                errors.append(f"{c['id']}: blocking note replayed inside the action")
        if any(k in frame for frame in (c['start_frame'],c['end_frame']) for k in ('Final physical lock','Framing:')):
            errors.append(f"{c['id']}: start/end frame must be a state, not an action or camera note")
        written=[c['start_frame'],c['action'],c['end_frame'],c['lighting'],c.get('wardrobe_note',''),
                 *c.get('cinematic',{}).values(),*(d['text'] for d in c['dialogue'])]
        if any(BROADCAST_WORDS.search(t) for t in written):
            errors.append(f"{c['id']}: TV/news wording invites a broadcaster logo or news graphics")
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
            errors.append(f"{c['id']}: expected 1 or 2 dialogue turns in every take")
        if sum(syllables(d['text']) for d in c['dialogue']) > MAX_CLIP_SYLLABLES:
            errors.append(f"{c['id']}: over {MAX_CLIP_SYLLABLES} spoken syllables in one 10 s take")
        for d in c['dialogue']:
            if '@' in d['text'] or '"' in d['text']:
                errors.append(f"{c['id']}: spoken text contains injected tag/quote")
            if d['mode'] not in ('on','off','vo','device'):
                errors.append(f"{c['id']}: unknown voice mode")
            if syllables(d['text']) < 3:
                errors.append(f"{c['id']}: line too short to carry a beat")
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
    if key == 'MAY' and (24,6) <= (c['scene'],c['number']) < (35,1):
        outfit = outfit.replace(', steel handcuffs at belt','')
        notes.append('no handcuffs on her belt: both city pairs were used at 23.5 and 24.5, fresh pairs arrive at 35.1')
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
    if base == 'THANH' and c['scene'] == 29:
        notes.append('one glasses temple arm bent in the struggle, not yet taped')
    if base == 'THANH' and (30,1) <= (c['scene'],c['number']) < (56,5):
        notes.append('one glasses temple arm bent, held by tape after rescue; new glasses only at 56.5')
    extra = ' ' + '; '.join(notes) + '.' if notes else ''
    return f"{identity['tag']} = {identity['name']}: same approved identity, age {age}; {face}. {outfit}.{extra} Voice: {identity['voice']}."


def dialogue_text(plan: dict, d: dict) -> str:
    if d['speaker'] in plan['looks']:
        identity = plan['identities'][base_key(plan,d['speaker'])]
        speaker = f"{identity['name']} ({identity['tag']})" if d['mode']=='on' else identity['name']
    else:
        speaker = {'BROKER':'Người gọi giấu tên','RADIO':'Bộ đàm','EXTRA':'Người trong cảnh','OFFICER':'Cán bộ hỗ trợ'}[d['speaker']]
    mode = {'on':'nói trong hình','off':'ngoài khung hình','vo':'lời dẫn ngoài hình','device':'qua thiết bị'}[d['mode']]
    return f"{speaker}, {mode}: {d['text']}"


def voice_block(plan: dict, c: dict) -> str:
    if not c['dialogue']:
        return 'No speech, narration or improvised vocal filler. Play the action and location sound.'
    total = sum(syllables(d['text']) for d in c['dialogue'])
    duration = min(9.2, max(3.2, total / 3.6 + 0.6))
    end = round(0.2 + duration, 1)
    modes = {d['mode'] for d in c['dialogue']}
    if modes == {'on'}:
        rendering = 'Visible speaker talks at a natural pace with accurate lip sync; the listener reacts in the moment without dead air.'
    elif modes == {'vo'}:
        rendering = 'Voice-over only, dry and close, short natural pauses at sentence breaks; visible mouths stay closed while the action continues.'
    elif modes == {'off'}:
        rendering = 'Off-screen speech at a natural pace; do not add a face or animate the listener speaking.'
    elif modes == {'device'}:
        rendering = 'Voice through the established device at a natural pace; no caller body in this shot.'
    else:
        rendering = 'Follow each turn mode strictly (nói trong hình = visible mouth; lời dẫn ngoài hình / ngoài khung hình / qua thiết bị = mouth at rest).'
    prefixes = [GENERIC_VOICES[d['speaker']] for d in c['dialogue'] if d['speaker'] in GENERIC_VOICES]
    prefix_block = ('\n'.join(dict.fromkeys(prefixes)) + '\n') if prefixes else ''
    lines_block = '\n'.join(dialogue_text(plan, d) for d in c['dialogue'])
    turn_label = 'two turns with a natural handover' if len(c['dialogue']) > 1 else 'one line'
    if modes == {'vo'}:
        timing = f"0.2–{end:.1f}s, {turn_label} (natural Southern Vietnamese pace, clear diction, cue at 0.2s)."
    else:  # the beats place each speaker; a fixed window would contradict them
        timing = (f"{turn_label.capitalize()} at a natural Southern Vietnamese conversational pace, clear diction. "
                  "Each line starts inside the ACTION beat that names its speaker (at 0.2s when no beat names it) "
                  "and is complete before 10.0s.")
    return (
        f"{timing} {rendering}\n"
        f"{prefix_block}{lines_block}\n"
        f"Only words after the final colon are spoken. Never read names, tags or directions. No captions."
    )


def prop_detail(plan: dict, key: str, c: dict) -> str:
    if key=='MARKS':
        changes={'01.5':(0,1),'07.1':(1,2),'12.1':(2,3),'19.2':(3,4),'28.5':(4,6),'34.1':(6,7)}
        if c['id'] in changes:
            before,after=changes[c['id']]
        else:  # unchanged in this shot: whatever the latest earlier cut left on the frame
            before=after=max((a for k,(_,a) in changes.items()
                              if tuple(map(int,k.split('.')))<(c['scene'],c['number'])),default=0)
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
        return 'Film opening. Start directly at 0.0s with physical movement already under way and the opening voice-over at 0.2s; no logo, recap, fade-in or slow pause.'
    prefix = f"Previous editorial shot: {previous['id']}, ending with {previous['end_frame']}\n"
    if c['transition']=='CONTINUE':
        return prefix + 'Use that last frame as this start frame. Preserve lens, axis, positions, light and props. Advance to the new action immediately at 0.0s; do not replay the preceding gesture or words. No freeze at the seam.'
    cut = {
        'OPEN':'Scene-opening editorial cut to the explicitly stated new time/place. Establish the new composition and dramatic stakes from the first frame, action under way at 0.0s.',
        'CUT':'Intentional editorial cut, not a continuous take. Start in the new composition with momentum; preserve compatible screen direction and eyelines. No morph or duplicated gesture.',
        'MATCH':'Intentional match cut using the related shape or pose. Cut cleanly to the new time/place and advance the action from 0.0s; no transformation, morph, dissolve or replay of the old shot.',
        'J':'J-cut in the edit: introduce the incoming location sound about 0.25s before the picture cut; the action is already under way at 0.0s. This generated clip contains only the new shot, not a two-location montage.',
        'L':'L-cut in the edit: retain the preceding diegetic sound about 0.25s after the picture cut while the new scene action starts at 0.0s. This generated clip contains only the new shot.',
    }[c['transition']]
    return prefix + cut


def render_prompt(plan: dict, c: dict, previous: dict|None, following: dict|None) -> str:
    continuous = c['transition']=='CONTINUE'
    if continuous:
        head = f"Continue the scene seamlessly from the final frame of clip {previous['number']}. Same composition at the seam, new action immediately after the seam."
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
    audio_bridge = scene_obj['outgoing_audio'] if c['number']==6 else ''
    if c['scene'] == 1 and c['number'] == 1:
        scene_intro = f"\n[FILM OPENING INTRODUCTION — Mở đầu phim: {scene_obj['title']}]\nSơn arrives alone in the fishing town of Hòn Sóng at dawn. The voice-over carries his name, his nickname, Hạ's abduction and the seven-day deadline; the picture shows only this quiet arrival. Movement starts at 0.0s, voice-over at 0.2s.\n"
    elif c['number'] == 1:
        scene_intro = f"\n[SCENE OPENING HOOK — Mở cảnh {c['scene']:02d}: {scene_obj['title']}]\nScene goal: {scene_obj['purpose']} Establish the setting and dramatic stakes from the first frame; movement under way at 0.0s, first line at 0.2s.\n"
    else:
        scene_intro = ''
    detail=c.get('cinematic',{})
    intent=f"\n[DRAMATIC INTENT — show through behaviour, never narrate this note]\n{detail['intent']}\n" if detail else ''
    staging=f"\n[BLOCKING AND PERFORMANCE]\nBlocking: {detail['blocking']}\nPerformance: {detail['performance']}\n" if detail else ''
    surface=f"\n[VISIBLE TEXTURE]\n{detail['texture']}\n" if detail else ''
    framing=f"\nComposition: {detail['composition']}\nFocus: {detail['focus']}" if detail else ''
    rhythm=f"\nAction rhythm: {detail['rhythm']}" if detail else ''
    sound_specific=f"\nForeground sound: {detail['sound_detail']}" if detail else ''
    camera_contract='Keep the exact previous camera, lens and axis; no framing reset.' if continuous else 'One new coverage angle on the established side of the axis; positions, eyelines, prop hands and movement direction stay consistent with the story so far. Never cut internally.'
    shutter=SHUTTER.get(c['camera'],'Natural 180-degree shutter')
    return f"""{head}
10 seconds, full-frame 16:9, 24 fps, photorealistic live-action Vietnamese neo-noir crime thriller, restrained naturalistic acting with micro-expressions, subtle breathing and natural eye movement, natural skin texture, subtle film grain. {shutter}. Grade: cool shadows, restrained warm highlights, natural skin tones; no heavy teal-orange, artificial lens flare or beauty smoothing. In a single continuous shot: ONE camera setup and ONE location; no internal cuts, montage, recap or closing fade.
{CLEAN_FRAME}

[CHARACTERS — approved identities and current appearances]
{locks}
{note.strip()}
{picture_refs}

[TIMELINE AND LOCATION]
Scene {c['scene']:02d}/60, clip {c['number']}/6; shot {c['id']}. Story time: {c['story_time']}.
{location}
{c['lighting']}
{scene_intro}{intent}

[EDIT IN — do not render the previous shot again]
{transition_text(c,previous)}

[START FRAME — state only, not an action to repeat]
{c['start_frame']}

[CAMERA]
{CAMERAS[c['camera']]}
{camera_contract}{framing}

[ACTION — 0–10s, one evolving take]
{c['action']}
Play each beat once, in order, from the start state to the end state; no gesture is repeated and there is no dead air. Breathing and existing environmental motion continue through the seam.{rhythm}
{staging}

[DIALOGUE]
{voice_block(plan,c)}

[PROPS]
Reference only; enact only the current ACTION, not a future handover.
{prop_text}
{surface}

[SOUND]
Location bed: {sound}.{sound_specific}
Keep diegetic continuity, dialogue clean and forward; every sound effect has a visible or established source. No generated score, stock sting or invented weapon effect. Edit bridge: {audio_bridge or 'Follow the stated incoming/outgoing edit without restarting the ambience.'}

[END FRAME — natural motion continues]
{end}
{out}

[AVOID]
repeating any beat or line inside this clip or from adjacent clips, rushed, clipped or dragging speech, dead air pauses, exaggerated or theatrical acting, frozen tail frames, premature scene change, arbitrary slow motion or speed ramps, identity/age/costume drift, extra watches or scarves, wrong prop owner, reversed movement axis, readable text, generated captions, logos, TV station or channel logos, broadcaster watermarks, news tickers, lower-thirds, LIVE/REC badges, timestamps, real actor likeness, graphic injury, blood, gunfire or instructional drug-use detail.
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
    if scene.get('dramaturgy'):
        d=scene['dramaturgy']
        lines[8:8]=[f"**Câu hỏi đang mở:** {d['dramatic_question_vi']}",
                    f"**Móc vào cảnh:** {d['hook_vi']}",
                    f"**Điểm bẻ:** {d['turn_vi']}",
                    f"**Gieo / trả:** {d['payoff_or_setup_vi']}",'']
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
           '**60 đơn vị sản xuất × 6 clip × 10 giây = 60 phút hình nguồn.** Mỗi clip một cú máy, quản lý chặt chẽ trang phục, ba lô, túi xách, đồng hồ, sổ sách và đạo cụ cầm tay xuyên suốt 360 phân cảnh.', '',
           'Nguồn duy nhất: `PHAN_CANH_V3.json`. Hành động/camera viết tiếng Anh cho prompt kèm bản phân cảnh tiếng Việt 3 nhịp chi tiết. Tái sinh bằng `python3 build_full_60_scenes.py`; kiểm tra bằng `python3 build_full_60_scenes.py --check`.', '',
           'Sơn có bảy ngày trước chuyến tàu chuyển Hạ đi. Anh hợp tác với Mây, giao bằng chứng cho điều tra và chấp nhận trả giá. Kiên muốn Sơn im lặng, Bà Hai muốn lấy lại quyền kiểm soát. Cuộc trao đổi ở cảng bị phản bội; Dũng dùng chất Tê hư cấu giữ Sơn sống, cả hai phe đều nhận biết thuốc. Hạ để lại dấu và mở đường, Mây dẫn việc cứu người. Sơn cứu cả Kiên khỏi ngã rồi tự nhận còng.', '',
           '| Cảnh | Phút phim | Tên | Biến chuyển mới |', '|---|---|---|---|']
    for s in plan['scenes']:
        n=s['number']; lines.append(f"| {n:02d} | {clock((n-1)*60)}–{clock(n*60)} | {s['title']} | {s['purpose']} |")
    for s in plan['scenes']:
        n=s['number']; lines += ['',f"### CẢNH {n:02d}: {s['title']}",f"*Thời gian truyện: {s['story_time']}*",s['purpose'],'']
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
                      f"- **Mã đạo cụ khóa (Props):** `{props_str}`",
                      f"- **Diễn biến phân cảnh 3 nhịp (Tiếng Việt):** {sp.get('beats_vi','')}",
                      f"- **Đầu (Start Frame):** {c['start_frame']}",
                      f"- **Hành động 3 nhịp (Action Prompt):** {c['action']}",
                      f"- **Thoại ({sum(syllables(x['text']) for x in c['dialogue'])} âm tiết):** {d}",
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
           '**Khung hình sạch, không logo đài truyền hình:** mọi prompt cấm logo đài hoặc kênh ở góc hình, watermark, chữ chạy tin tức, lower-third (dải tên), biểu tượng LIVE/REC, đồng hồ thời gian và mọi đồ họa trên hình. Màn hình máy tính, điện thoại trong truyện không hiện kênh, bản tin hay thương hiệu đài; biểu tượng hãng tàu chỉ là hình đơn giản không đọc được. Dữ liệu cảnh không dùng chữ TV/tin tức/truyền hình để model không dựng thành bản tin, và validator chặn các chữ này. Khi duyệt render, soi bốn góc khung: thấy logo hoặc chữ thì tạo lại clip đó.', '',
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
