"""Verify and label the encoded review candidate without inventing acceptance."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

base = Path(__file__).resolve().parent
long = base / 'longform'
project = json.loads((long/'project.json').read_text())
report = json.loads((long/'output/film-report.json').read_text())
story = json.loads((base/'story-10min.json').read_text())
words = json.loads((base/'words-10min.json').read_text())['words']
expected = ' '.join(b['text'] for b in story['beats']).split()
actual = ' '.join(c['text'] for c in project['captions']).split()
assert actual == expected, 'Caption/source mismatch'
assert len(project['shots']) == len(json.loads((long/'shot-ledger.json').read_text()))
assert report['full_decode'] == 'pass'
assert abs(report['duration'] - 604) < .04
assert report['frames'] == 18120
for c in project['captions']:
    assert 0 <= c['start'] < c['end'] <= 604
for a,b in zip(project['captions'],project['captions'][1:]):
    assert a['end'] <= b['start'] + .001
film=long/'output/film.mp4'
assert hashlib.sha256(film.read_bytes()).hexdigest()==report['output_sha256']
target=base/'Human-exe-Episode-01-10min.mp4'
shutil.copy2(film,target)
shutil.copy2(long/'output/film.srt',base/'Human-exe-Episode-01-10min.srt')
shutil.copy2(long/'output/film.vtt',base/'Human-exe-Episode-01-10min.vtt')
source_cursor=0
chapters=[]
for beat in story['beats']:
    start=words[source_cursor]['start'];source_cursor+=len(beat['text'].split())
    chapters.append({'start':start,'heading':beat['heading']})
(base/'chapters-10min.txt').write_text('\n'.join(f"{int(x['start'])//60:02d}:{int(x['start'])%60:02d} {x['heading']}" for x in chapters)+'\n')
result={
    'stage':'complete_encoded_review_candidate',
    'user_request':'làm bản 10 phut đi',
    'duration_seconds':report['duration'],
    'voice':'macOS Samantha, native speed unchanged',
    'video':str(target),
    'video_sha256':report['output_sha256'],
    'words':len(expected),
    'shots':report['shot_count'],
    'caption_cues':len(project['captions']),
    'caption_source_coverage':'exact word-for-word source coverage; acoustic timestamps with recorded local token corrections',
    'technical_decode':'pass',
    'independent_still_review':'See independent-still-review.json and independent-still-review-v2.json; fixes recorded separately',
    'continuous_picture_and_listening_review':'not claimed; final user review pending',
    'sample_equivalence':'not claimed',
    'publication':'not performed'
}
(long/'delivery-checkpoint.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
