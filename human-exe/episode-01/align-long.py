import difflib
import json
from pathlib import Path
import re
import time
from faster_whisper import WhisperModel

base = Path(__file__).resolve().parent
model_dir = Path('/Users/iseul-a/.cache/huggingface/hub/models--Systran--faster-whisper-small/snapshots/536b0662742c02347bc0e980a01041f333bce120')
model = WhisperModel(str(model_dir), device='cpu', compute_type='int8', cpu_threads=6, local_files_only=True)
segments, info = model.transcribe(str(base/'narration-10min.wav'), language='en', beam_size=1, word_timestamps=True, condition_on_previous_text=False, vad_filter=True)
actual = []
segment_data = []
for seg in segments:
    actual.extend({'word': w.word.strip(), 'start': w.start, 'end': w.end, 'probability': w.probability} for w in seg.words)
    segment_data.append({'start': seg.start, 'end': seg.end, 'text': seg.text})
    print(json.dumps({'aligned_through': round(seg.end, 2)}), flush=True)
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
source = (base/'narration-10min.txt').read_text().split()
a = [norm(w) for w in source]
b = [norm(w['word']) for w in actual]
matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
result = [None] * len(source)
issues = []
for tag, i, j, x, y in matcher.get_opcodes():
    if tag == 'equal':
        for n, m in zip(range(i,j), range(x,y)):
            result[n] = {'word': source[n], 'start': actual[m]['start'], 'end': actual[m]['end'], 'timing': 'ASR matched acoustic word'}
    else:
        issues.append({'kind': tag, 'source_range': [i,j], 'recognized_range': [x,y], 'source': ' '.join(source[i:j]), 'recognized': ' '.join(w['word'] for w in actual[x:y])})
        if j > i and y > x:
            # Local replacements preserve actual recognized acoustic intervals.
            for n in range(i,j):
                m = min(y-1, x + int((n-i)*(y-x)/(j-i)))
                result[n] = {'word': source[n], 'start': actual[m]['start'], 'end': actual[m]['end'], 'timing': 'local source correction on recognized acoustic interval'}
for i, word in enumerate(result):
    if word is not None:
        continue
    prior = next((w['end'] for w in reversed(result[:i]) if w is not None),0)
    nxt = next((w['start'] for w in result[i+1:] if w is not None),prior+.2)
    result[i] = {'word':source[i], 'start':prior, 'end':max(prior+.01,nxt), 'timing':'unmatched word bounded by acoustic neighbors; review required'}
out = {'method':'Local faster-whisper small ASR word timestamps matched against original script; not a forced-aligner claim', 'words':result, 'issues':issues, 'segments':segment_data, 'recognized_words':actual}
(base/'words-10min.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'done':True,'source_words':len(source),'recognized_words':len(actual),'corrections':issues}),flush=True)
