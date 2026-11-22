#!/usr/bin/env python3
# mix_music.py <film.mp4> <timeline.json> <music_edl.json> <out.mp4>
import json, subprocess, sys, os
film, tlf, edlf, out = sys.argv[1:5]
TL = {sid: (a, b) for sid, a, b in json.load(open(tlf))}
E = json.load(open(edlf)); MD = os.path.expanduser(E.get('dir', '~/codr/music/files'))
TOTAL = float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',film]).decode())
def cue_dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
def t_of(ref, end=False):
    if isinstance(ref, (int, float)): return float(ref)
    if ref == 'END': return TOTAL
    if ref.endswith('@end'): ref = ref[:-4]; end = True
    sid, _, off = ref.partition('+')
    a, b = TL[sid]; return (b if end else a) + (float(off) if off else 0.0)
inputs = ['-i', film]; fc = []; labels = []
for i, c in enumerate(E['cues']):
    st = t_of(c['start']); en = t_of(c['end'], end=True) + c.get('tail', 0)
    en = min(en, TOTAL)
    L = max(0.5, en - st); fi = c.get('fade_in', 2.0); fo = c.get('fade_out', 3.0)
    ci = c.get('cue_in', 0)
    if c.get('align_end'): ci = max(0.0, cue_dur(f"{MD}/{c['cue']}") - L)
    inputs += ['-stream_loop', '-1', '-ss', str(ci), '-i', f"{MD}/{c['cue']}"]
    k = i + 1
    fc.append(f"[{k}:a]atrim=0:{L:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,"
              f"loudnorm=I=-18:TP=-2:LRA=11,aresample=48000,afade=t=in:st=0:d={fi},afade=t=out:st={max(0, L-fo):.3f}:d={fo},volume={c.get('gain_db', -20) + E.get('gain_offset', 0)}dB,"
              f"adelay={int(st*1000)}|{int(st*1000)}[m{k}]")
    labels.append(f'[m{k}]')
fc.append(''.join(labels) + f"amix=inputs={len(labels)}:normalize=0:dropout_transition=0,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[mus]")
fc.append("[0:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,asplit=2[dlg][sc]")
fc.append(f"[mus][sc]sidechaincompress=threshold={E.get('duck_thr',0.08)}:ratio={E.get('duck_ratio',3)}:attack=40:release=700:makeup=1[duck]")
fc.append(f"[dlg][duck]amix=inputs=2:normalize=0:duration=first,volume={E.get('master_db',0)}dB,alimiter=limit=0.89:level=false[aout]")
if os.environ.get('MUSONLY'):
    fc = fc[:-3]
    cmd = ['ffmpeg','-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[mus]', '-c:a', 'aac', '-b:a', '128k', out]
    r = subprocess.run(cmd, capture_output=True, text=True); print(r.stderr[-800:] if r.returncode else 'OK ' + out); sys.exit()
cmd = ['ffmpeg', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '0:v', '-map', '[aout]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out]
r = subprocess.run(cmd, capture_output=True, text=True)
print(r.stderr[-1200:] if r.returncode else 'OK ' + out)
