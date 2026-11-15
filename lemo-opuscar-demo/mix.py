"""Score + foley for «Một câu lệnh» (Lemo-Opuscar demo, Stick-figure Explainer). No voice.

The score runs on the film clock: F major, 100 bpm, beat .6 s, bar 2.4 s, 13 bars (31.2 s).
  A  0–4.8    one figure, one sentence: sparse marimba + pizz bass, typing ticks
  B  4.8–9.6  the pulse: harp flick on send, walking pizz bass, glockenspiel on each crew pop (rising)
  C  9.6–14.4 the chain: kalimba per clasp (rising), glockenspiel as the accent reaches each, vibraphone chord + strings
  D  14.4–19.2 pull back: string pad grows, marimba tally per new chain, harp sweep up — cut to silence at 19.2
  E  19.2–21.6 silence: room tone only
  F  21.6–31.2 everyone turns: soft low hit + vibraphone + strings, harp on the title, Bb – C – F cadence ringing out
Run:  LIB=<library> <library>/.venv/bin/python mix.py   → out/mix.wav
"""
import json, os, sys
import numpy as np, soundfile as sf
LIB = os.environ['LIB']; sys.path.insert(0, LIB)
from core.audio import sampler as S
from core.audio.sfx import SR, bp, lp, hp, add, compress, limit, click, whoosh, pop, thump, brown

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'events.json')))
DUR = float(D['dur']); N = int(round(DUR * SR)); EV = D['ev']
first = lambda typ: [e for e in EV if e['type'] == typ]
one = lambda typ: first(typ)[0]['t']
B = .6; BAR = 2.4
rng = np.random.default_rng(7)

# ================= score =================
ev = []
F_, Dm, Bb, C_ = (41, [65, 69, 72]), (38, [62, 65, 69]), (46, [62, 65, 70]), (48, [64, 67, 72])
def bass(t0, root, walk=False, vel=.5):
    ev.append((t0, 'contrabass_pizz', root, .9, vel, -.05, .6))
    if walk:
        for i, st in enumerate([4, 7, 9]): ev.append((t0 + B * (i + 1), 'contrabass_pizz', root + st, .5, vel - .08, -.05, .5))
    else: ev.append((t0 + 2 * B, 'contrabass_pizz', root + 7, .8, vel - .06, -.05, .52))
def marim(t0, tri, vel=.18, eighths=True):
    pat = [0, 1, 2, 1, 0, 2, 1, 2] if eighths else [0, 2, 1, 2]
    st = B / 2 if eighths else B
    for i, k in enumerate(pat): ev.append((t0 + i * st, 'marimba', tri[k] + (12 if i % 4 == 2 else 0), .3, vel + .04 * (i % 2 == 0), .25, .5))

# A — sparse
bass(0.0, *F_[:1]); marim(0.0, F_[1], .16, eighths=False)
bass(BAR, *Dm[:1]); marim(BAR, Dm[1], .16, eighths=False)
ev.append((one('pop'), 'glockenspiel', 89, .8, .28, -.3, .3))
# B — the sentence leaves
T = one('send')
for i, p in enumerate([65, 69, 72, 77, 81]): ev.append((T - .1 + i * .025, 'harp', p, 1.0, .45, -.4 + .2 * i, .6))
for b, ch in enumerate([Bb, C_]): bass(T + b * BAR, ch[0], walk=True); marim(T + b * BAR, ch[1], .17)
POPN = [84, 86, 89, 93]
for e in first('pop'):
    if e['i'] >= 1: ev.append((e['t'], 'glockenspiel', POPN[e['i'] - 1], .7, .32, e['pan'] * .6, .32))
# C — the chain
for b, ch in enumerate([F_, Dm]): bass(9.6 + b * BAR, ch[0]); marim(9.6 + b * BAR, ch[1], .15)
KAL = [65, 67, 69, 72]
for e in first('clasp'): ev.append((e['t'], 'kalimba', KAL[e['k'] - 1], 1.0, .62, e['pan'] * .6, .8))
for e in first('node'): ev.append((e['t'], 'glockenspiel', [84, 86, 89, 93][e['k'] - 1], .6, .3 + .03 * e['k'], e['pan'] * .6, .3))
T = one('run') + .85
for i, p in enumerate([65, 69, 72, 77]): ev.append((T + i * .03, 'vibraphone', p, 1.8, .4, -.2 + .13 * i, .45))
ev.append(dict(t=T, inst='violins', pitch=72, dur=1.6, vel=.28, pan=.25, gain=.25, attack=.5))
# D — pull back: the pad grows, a tally per chain, a harp sweep up into the cut
T0 = one('pull'); T1 = 19.2
for b, ch in enumerate([Bb, C_]): bass(T0 + b * BAR, ch[0], walk=True, vel=.45)
pads = [(T0, T0 + BAR, [46, 58, 65, 70]), (T0 + BAR, T1, [48, 60, 67, 72, 76])]
for t0, t1, notes in pads:
    for i, p in enumerate(notes):
        inst = 'cellos' if p < 55 else ('violas' if p < 64 else 'violins')
        ev.append(dict(t=t0, inst=inst, pitch=p, dur=t1 - t0 + .05, vel=.3, pan=-.3 + .15 * i, gain=.22, attack=.45, release=.25))
SCALE = [65, 67, 69, 70, 72, 74, 76, 77, 79, 81, 84]
for e in first('cpop'): ev.append((e['t'], 'marimba', SCALE[e['j']], .4, .42, -.4 + .08 * e['j'], .5))
for i in range(9): ev.append((18.0 + i * .1, 'harp', [60, 64, 67, 72, 76, 79, 84, 88, 91][i], .8, .38 + .02 * i, -.5 + .12 * i, .45))
# E — silence (nothing scored 19.2–21.6)
# F — everyone turns to you
T = one('turn')
for i, p in enumerate([53, 65, 69, 72, 79]): ev.append((T + i * .03, 'vibraphone', p, 2.6, .42, -.25 + .12 * i, .48))
for i, p in enumerate([41, 53, 60, 65, 69, 72]):
    inst = 'cellos' if p < 55 else ('violas' if p < 64 else 'violins')
    ev.append(dict(t=T, inst=inst, pitch=p, dur=2.4, vel=.32, pan=-.3 + .12 * i, gain=.26, attack=.3, release=.6))
bass(T, 41)
for e in first('wave'):
    for i, p in enumerate([77, 81, 84]): ev.append((e['t'] + i * .3, 'kalimba', p - 12, .8, .45, .2, .5))
# title + cadence Bb – C – F (on the bar grid: 24.0, 26.4, 28.8)
for i, p in enumerate([58, 62, 65, 70, 74, 77, 82]): ev.append((24.0 + i * .035, 'harp', p, 1.6, .45, -.4 + .12 * i, .55))
for t0, (root, tri), dur in [(24.0, Bb, 2.4), (26.4, C_, 2.4), (28.8, F_, 2.4)]:
    ev.append((t0, 'contrabass_pizz', root, 1.2, .5, 0, .55))
    for i, p in enumerate(tri):
        ev.append(dict(t=t0, inst='violas' if p < 64 else 'violins', pitch=p, dur=dur, vel=.3, pan=-.2 + .2 * i, gain=.2, attack=.35, release=.8))
    if t0 < 28: marim(t0, tri, .13, eighths=False)
for i, p in enumerate([65, 69, 72, 77, 81]): ev.append((28.8 + i * .04, 'vibraphone', p, 2.4, .38, -.2 + .1 * i, .45))
ev.append((28.8, 'glockenspiel', 89, 1.6, .26, .1, .26))
S.seed(3)
music = S.render(ev, dur=DUR + 3, master=False)[:N]
music = S.room(music, size=.34, mix=.18)
# keep the low end in check: high-pass, then pull 20–120 Hz down a little (low shelf by subtraction)
music = np.stack([hp(music[:, c], 40) for c in range(2)], axis=1)
music = music - .55 * np.stack([lp(music[:, c], 120) for c in range(2)], axis=1)
# silence for the held bar: let tails die quickly into it, then room tone only
t = np.arange(N) / SR
gate = np.ones(N)
m = (t >= 19.2) & (t < 21.6); gate[m] = np.clip(1 - (t[m] - 19.2) / .35, 0, 1) ** 2
music *= gate[:, None]
# the last 1.5 s fade
music *= np.clip((DUR - t) / 1.5, 0, 1)[:, None]

# ================= foley =================
fx = np.zeros((N, 2))
for e in EV:
    T, typ, pan = e['t'], e['type'], e.get('pan', 0) * .7
    if typ == 'pop': add(fx, lp(pop(1.0), 3500) * .11, T, 1.0, pan); add(fx, hp(click(pitch=.75), 1200) * .025, T + .03, 1.0, pan)
    elif typ == 'tick': add(fx, hp(click(pitch=1.6), 2500) * .018, T, 1.0, -.2 + rng.uniform(-.05, .05))
    elif typ == 'send': add(fx, lp(pop(1.0), 4000) * .12, T, 1.0, -.4)
    elif typ == 'reach': add(fx, lp(whoosh(.28), 2200) * .035, T, 1.0, 0)
    elif typ == 'clasp': add(fx, lp(click(pitch=.42), 2600) * .13, T, 1.0, pan)
    elif typ == 'cpop': add(fx, lp(pop(1.0), 3000) * .045, T, 1.0, -.3 + .06 * e['j'])
    elif typ == 'cclasp': add(fx, lp(click(pitch=.45), 2400) * .04, T, 1.0, -.3 + .06 * e['j'])
    elif typ in ('pulse', 'run'):
        d = e['d'] + .15; n = int(d * SR)
        x = bp(rng.standard_normal(n), 1500, 5200) * np.sin(np.pi * np.arange(n) / n) ** 2 * (.03 if typ == 'pulse' else .022)
        k = 8                                       # pan sweeps left → right in steps, crossfaded by the envelope
        for i in range(k):
            a, b = i * n // k, (i + 1) * n // k
            w = x[a:b] * np.hanning(b - a) * 1.6
            add(fx, w, T + a / SR, 1.0, -.7 + 1.4 * i / (k - 1))
    elif typ == 'pull': add(fx, lp(whoosh(1.4), 1600) * .06, T, 1.0, 0)
    elif typ == 'turn': add(fx, thump(.9, f=62) * .2, T, 1.0, 0); add(fx, lp(whoosh(.5), 1400) * .03, T, 1.0, .2)
    elif typ == 'wave': add(fx, lp(whoosh(.4), 1800) * .025, T, 1.0, -.3)
    elif typ == 'line': add(fx, bp(rng.standard_normal(int(.8 * SR)), 800, 3000) * np.hanning(int(.8 * SR)) * .012, T, 1.0, -.3)
# room tone: a very soft, warm bed through the whole film (it is all that is left in the silent bar)
room = bp(brown(DUR), 150, 1200); room = room / (np.abs(room).max() + 1e-9) * .006
fx[:len(room), 0] += room[:N]; fx[:len(room), 1] += room[:N] * .97

out = music * .9 + fx
out = np.stack([limit(compress(out[:, c], thr=.4, ratio=2.5), ceil=.9) for c in range(2)], axis=1)
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
sf.write(os.path.join(HERE, 'out', 'mix.wav'), out.astype(np.float32), SR)
print('mix', out.shape, 'peak', float(np.abs(out).max()))
print(S.credits(sorted({(x['inst'] if isinstance(x, dict) else x[1]) for x in ev})))
