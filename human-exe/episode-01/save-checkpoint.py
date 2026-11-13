import hashlib
import json
from pathlib import Path

p = Path(__file__).resolve().parent
script = json.loads((p / 'script.json').read_text())
(p / 'narration-en.txt').write_text('\n\n'.join(b['narration'] for b in script['beats']) + '\n')
report = json.loads((p / 'output/preview-report.json').read_text())
checkpoint = {
    'stage': 'audible_preview_ready_for_user_review',
    'user_authorization': {
        'topic_and_channel_direction': 'accepted in conversation',
        'macos_voice_for_pace_preview': 'explicitly selected by user',
        'exact_preview_acceptance': 'pending',
        'full_film': 'not rendered; awaiting exact sample approval',
        'publishing': 'not requested',
    },
    'script_words': sum(len(b['narration'].split()) for b in script['beats']),
    'voice': {'provider': 'macOS', 'name': 'Samantha', 'rate': 'native default; unchanged'},
    'preview': {
        'path': str(p / 'output/preview.mp4'),
        'sha256': report['output_sha256'],
        'duration': report['duration'],
        'resolution': '1280x720',
        'shots': report['shot_count'],
        'captions': report['caption_count'],
        'full_decode': report['full_decode'],
    },
    'audio_measurement': {'integrated_lufs': -16.44, 'true_peak_dbtp': -2.10, 'method': 'FFmpeg loudnorm measurement of encoded preview; output was not normalized'},
    'review': {
        'technical': 'passed',
        'still_frames': 'Inspected contact sheet and full-size opening, boss and final frames; fixed title/subtitle overlap, coffee contact and head attachment.',
        'continuous_playback_and_listening': 'not performed by author; user review pending',
        'independent_reference_comparison': 'pending; no sample-equivalence claimed',
        'caption_timing': 'Observed natural phrase boundaries in actual continuous recording, using ffmpeg silencedetect; not word-level forced alignment.',
    },
    'rights': {
        'story_and_scene_art': 'original project-authored fictional script and SVG-derived layered drawings',
        'fonts': 'bundled Caveat and Noto Sans; OFL licenses retained in upstream assets/fonts',
        'effects': 'upstream original procedural accents; no downloaded library audio',
        'bed': 'project-generated filtered pink noise; a designed bed, not a recorded real office',
    },
    'tooling': {
        'upstream': 'https://github.com/kaomei/stickman-video-director',
        'installation': 'workspace-local B1 subset with Git blob hashes verified; not global skill installation',
        'doctor': 'node, ffmpeg, ffprobe, canvas, sharp and fonts passed',
        'word_alignment': 'faster-whisper install failed in Python 3.15 due dependency compatibility; no model downloaded',
    },
    'next_step': 'User watches/listens to this exact preview and requests changes or explicitly approves the sample and remaining film. Keep approved voice/art unchanged; produce and align full narration only after scope approval.'
}
(p / 'checkpoint.json').write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2) + '\n')
sound = []
for beat in script['beats']:
    sound.append({'beat': beat['id'], 'actual_time': 'pending full narration; opening timing is in project.json', 'exact_text': beat['narration'], 'picture': beat['picture'], 'sound_plan': beat['sound'], 'voice': 'Samantha selected for preview only; full-film voice decision pending', 'rights_status': 'planned; only opening procedural effects and designed bed acquired'})
(p / 'sound-script.json').write_text(json.dumps(sound, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'stage': checkpoint['stage'], 'words': checkpoint['script_words'], 'preview_sha256': checkpoint['preview']['sha256']}))
