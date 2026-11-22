#!/usr/bin/env python3
# Dựng phim "Chị Ơi, Đến Rồi" từ film/clips/<id>.mp4 theo shots.json + EDL.
import json, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
ROOT = os.environ.get('ROOT', os.path.expanduser('~/mnt/TikTokSeries/chi-oi-den-roi'))
FILM = ROOT + '/film'; CLIPS = FILM + '/clips'
WORK = os.path.expanduser('~/codr/edit/work'); os.makedirs(WORK, exist_ok=True)
W, H, FPS = 1280, 720, 24
shots = json.load(open(FILM + '/shots.json'))
EDL = json.load(open(os.path.expanduser('~/codr/edit/edl.json')))
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
for f in ['/usr/share/fonts/truetype/noto/NotoSans-Light.ttf','/usr/share/fonts/opentype/noto/NotoSans-Light.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf']:
    if os.path.exists(f): FONT = f; break
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(' '.join(cmd)); print(r.stderr[-1500:]); sys.exit(1)
def dur(p):
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).decode().strip())
def lines_of(sid):
    t = open(ROOT + '/' + next(s for s in shots if s['id']==sid)['prompt'], encoding='utf-8').read()
    out = []
    for m in re.finditer(r'^- (\d+\.\d)s–(\d+\.\d)s, @(\w+) \([^)]*\): (.+)$', t, re.M):
        out.append((float(m.group(1)), float(m.group(2)), m.group(3), m.group(4).strip()))
    return out
def card(text, secs, name):
    import hashlib; name = 'card_' + hashlib.md5((text+str(secs)).encode()).hexdigest()[:8]
    png = f'{WORK}/{name}.png'; mp4 = f'{WORK}/{name}.mp4'
    if os.path.exists(mp4): return mp4, secs
    im = Image.new('RGB', (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FONT, 40)
    bw = d.textbbox((0, 0), text, font=f); x = (W - (bw[2]-bw[0]))//2; y = (H - (bw[3]-bw[1]))//2
    d.text((x, y), text, font=f, fill=(235, 235, 235)); im.save(png)
    run(['ffmpeg','-y','-loop','1','-t',str(secs),'-i',png,'-f','lavfi','-t',str(secs),'-i','anullsrc=r=48000:cl=stereo',
         '-vf',f'fps={FPS},format=yuv420p,fade=t=in:st=0:d=0.6,fade=t=out:st={secs-0.6}:d=0.6',
         '-c:v','libx264','-preset','veryfast','-crf','18','-c:a','aac','-b:a','192k','-shortest',mp4])
    return mp4, secs
def segment(sid, a, b, idx, fade_in=False, fade_out=False, j=0):
    src = f'{CLIPS}/{sid}.mp4'; out = f'{WORK}/seg_{sid}_{j}.mp4'
    key = json.dumps([a, b, fade_in, fade_out, EDL.get('shots', {}).get(sid, {}), os.path.getmtime(src)])
    if os.path.exists(out) and os.path.exists(out + '.key') and open(out + '.key').read() == key: return out, b - a
    e = EDL.get('shots', {}).get(sid, {})
    vf = []
    blur = e.get('blur', [])
    fc = f'[0:v]trim=start={a}:end={b},setpts=PTS-STARTPTS,scale={W}:{H}:flags=lanczos,fps={FPS}'
    if e.get('crop'):  # zoom-crop to hide corner text: fraction e.g. 0.9
        z = e['crop']; fc += f',crop=iw*{z}:ih*{z}:{e.get("cx","(iw-ow)/2")}:{e.get("cy","(ih-oh)/2")},scale={W}:{H}'
    fc += '[v0]'; last = 'v0'
    for i, (x, y, w, h, t0, t1) in enumerate(blur):
        fc += f';[{last}]split[m{i}][n{i}];[n{i}]crop={w}:{h}:{x}:{y},boxblur=12:2[b{i}];[m{i}][b{i}]overlay={x}:{y}:enable=\'between(t,{t0},{t1})\'[v{i+1}]'
        last = f'v{i+1}'
    L = b - a
    fades = []
    if fade_in: fades.append('fade=t=in:st=0:d=0.5')
    if fade_out: fades.append(f'fade=t=out:st={max(0,L-0.5)}:d=0.5')
    fc += f';[{last}]' + (','.join(fades + ['format=yuv420p']) ) + '[vo]'
    af = f'[0:a]atrim=start={a}:end={b},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d={0.4 if fade_in else 0.03},afade=t=out:st={max(0,L-(0.4 if fade_out else 0.04))}:d={0.4 if fade_out else 0.04}[ao]'
    run(['ffmpeg','-y','-i',src,'-filter_complex',fc+';'+af,'-map','[vo]','-map','[ao]','-c:v','libx264','-preset','veryfast','-crf','18','-r',str(FPS),'-c:a','aac','-b:a','192k','-ac','2',out])
    open(out + '.key', 'w').write(key)
    return out, L
def speech_end(src, D):
    r = subprocess.run(['ffmpeg','-i',src,'-af','silencedetect=noise=-30dB:d=0.35','-f','null','-'], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]
    en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    if not st: return D
    if len(en) < len(st): return st[-1]   # trailing silence until end
    return D
def srt_time(t):
    ms = int(round(t*1000)); return f'{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}'
def main():
    only = sys.argv[1:]  # optional scene filter e.g. 01 02
    segs = []; subs = []; T = 0.0; idx = 0; tl = []
    order = [s for s in shots if not only or s['scene'] in only]
    scenes = [s['scene'] for s in order]
    for k, s in enumerate(order):
        sid = s['id']; e = EDL.get('shots', {}).get(sid, {})
        for c in EDL.get('cards_before', {}).get(sid, []):
            p, L = card(c[0], c[1], f'card_{idx:04d}'); segs.append(p); T += L; idx += 1
        src = f'{CLIPS}/{sid}.mp4'
        if not os.path.exists(src): print('MISSING', sid); continue
        D = dur(src); ln = lines_of(sid)
        parts = e.get('parts')
        if not parts:
            a = e.get('in', 0.0)
            if 'out' in e: b = e['out']
            elif ln: b = min(D, max(ln[-1][1] + EDL.get('tail', 1.1), speech_end(src, D) + 0.5, a + 2.0))
            else: b = min(D, e.get('max', D))
            parts = [[a, b]]
        t_start = T
        first = (k == 0 or scenes[k-1] != s['scene']); lastsh = (k == len(order)-1 or scenes[k+1] != s['scene'])
        for j, (a, b) in enumerate(parts):
            b = min(b, D)
            p, L = segment(sid, a, b, idx, fade_in=first and j == 0, fade_out=lastsh and j == len(parts)-1, j=j)
            for (t0, t1, who, txt) in ln:
                if t0 >= a - 0.05 and t0 < b:
                    subs.append((T + t0 - a, T + min(t1, b) - a, txt))
            segs.append(p); T += L; idx += 1
        tl.append([sid, round(t_start, 3), round(T, 3)])
        for c in EDL.get('cards_after', {}).get(sid, []):
            p, L = card(c[0], c[1], f'card_{idx:04d}'); segs.append(p); T += L; idx += 1
        print(sid, round(T, 1), flush=True)
    lst = f'{WORK}/list.txt'
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in segs))
    tag = EDL.get('name', 'Chi-Oi-Den-Roi') + ('_canh' + '-'.join(only) if only else '')
    out = f'{WORK}/{tag}.mp4'
    run(['ffmpeg','-y','-f','concat','-safe','0','-i',lst,'-c','copy','-movflags','+faststart',out])
    with open(f'{WORK}/{tag}.srt', 'w', encoding='utf-8') as f:
        for i, (a, b, t) in enumerate(subs, 1): f.write(f'{i}\n{srt_time(a)} --> {srt_time(b)}\n{t}\n\n')
    json.dump(tl, open(f'{WORK}/{tag}.timeline.json', 'w'))
    print('OUT', out, round(T, 1))
main()
