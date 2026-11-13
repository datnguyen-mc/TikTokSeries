"""Fetch only upstream B1 tooling, docs and reference assets; never execute downloads."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent.parent / '.production-skills' / 'directing-stickman-videos'
TREE = json.loads(Path('/private/tmp/human-exe-upstream-tree.json').read_text())
PREFIX = 'skills/directing-stickman-videos/'
selected = []
for item in TREE['tree']:
    name = item['path']
    if item['type'] != 'blob' or not name.startswith(PREFIX):
        continue
    rel = name[len(PREFIX):]
    if rel in ('SKILL.md', 'package.json', 'package-lock.json') or rel.startswith(('scripts/', 'references/', 'assets/fonts/', 'assets/b1/')):
        selected.append((item, rel))

def fetch(pair):
    item, rel = pair
    dest = ROOT / rel
    if dest.exists() and dest.stat().st_size == item['size']:
        return rel
    url = 'https://raw.githubusercontent.com/kaomei/stickman-video-director/main/' + item['path']
    with urllib.request.urlopen(url, timeout=40) as response:
        data = response.read()
    if len(data) != item['size']:
        raise ValueError('Unexpected size: ' + rel)
    blob = b'blob ' + str(len(data)).encode() + b'\0' + data
    if hashlib.sha1(blob).hexdigest() != item['sha']:
        raise ValueError('Unexpected Git blob hash: ' + rel)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return rel

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch, selected))
    print(json.dumps({'root': str(ROOT), 'files': len(results), 'bytes': sum(x[0]['size'] for x in selected), 'scope': 'B1 subset, upstream hashes verified'}))
