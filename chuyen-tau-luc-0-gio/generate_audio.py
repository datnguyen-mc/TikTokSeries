#!/usr/bin/env python3
"""
Generate multi-voice Vietnamese TTS with word-level timestamps + procedural
dark thriller soundtrack & Foley SFX for 'Chuyến Tàu Lúc 0 Giờ' (30.0s exact).
"""

import asyncio
import json
import math
import subprocess
from pathlib import Path
from typing import Any

import edge_tts
import numpy as np
from scipy import signal
from scipy.io import wavfile

BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "assets" / "audio"
SFX_DIR = BASE_DIR / "assets" / "sfx"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
SFX_DIR.mkdir(parents=True, exist_ok=True)

SR = 44100
TARGET_TOTAL_SEC = 30.0

SCENES_SPEC: list[dict[str, Any]] = [
    {
        "id": "scene_01",
        "speaker": "Hoàng",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+12%",
        "pitch": "-4Hz",
        "text": "Đừng bao giờ bước lên toa số bốn của chuyến tàu điện lúc không giờ.",
        "highlight_words": {"đừng", "toa", "bốn", "không", "giờ"},
        "fx": "narrator",
        "pre_pad": 0.30,
        "post_pad": 0.35,
    },
    {
        "id": "scene_02",
        "speaker": "Hoàng",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+14%",
        "pitch": "-2Hz",
        "text": "Tăng ca về muộn, tôi ngủ gật rồi bước nhầm vào toa tàu vắng tanh.",
        "highlight_words": {"ngủ", "nhầm", "vắng", "tanh"},
        "fx": "narrator",
        "pre_pad": 0.20,
        "post_pad": 0.30,
    },
    {
        "id": "scene_03",
        "speaker": "Hoàng",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+15%",
        "pitch": "+0Hz",
        "text": "Đúng không giờ một phút, điện thoại rung bần bật dù mất sạch sóng.",
        "highlight_words": {"không", "một", "rung", "mất", "sạch"},
        "fx": "narrator",
        "pre_pad": 0.35,
        "post_pad": 0.30,
    },
    {
        "id": "scene_04",
        "speaker": "Số Lạ",
        "voice": "vi-VN-HoaiMyNeural",
        "rate": "+10%",
        "pitch": "-6Hz",
        "text": "Tuyệt đối đừng nhìn vào tấm kính đối diện. Họ đang đứng ngay sau lưng anh.",
        "highlight_words": {"đừng", "kính", "sau", "lưng"},
        "fx": "haunted_phone",
        "pre_pad": 0.25,
        "post_pad": 0.35,
    },
    {
        "id": "scene_05",
        "speaker": "Hoàng",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+12%",
        "pitch": "+2Hz",
        "text": "Theo phản xạ, tôi lỡ ngước mắt nhìn thẳng vào tấm kính đen trước mặt.",
        "highlight_words": {"lỡ", "nhìn", "thẳng", "kính", "đen"},
        "fx": "tense",
        "pre_pad": 0.20,
        "post_pad": 0.30,
    },
    {
        "id": "scene_06",
        "speaker": "Hoàng",
        "voice": "vi-VN-NamMinhNeural",
        "rate": "+6%",
        "pitch": "-5Hz",
        "text": "Sau lưng tôi trống rỗng... Thứ đang mỉm cười trong kính, chính là tôi.",
        "highlight_words": {"trống", "rỗng", "mỉm", "cười", "chính", "tôi"},
        "fx": "twist",
        "pre_pad": 0.25,
        "post_pad": 1.15,
    },
]


async def synth_line(spec: dict[str, Any]) -> tuple[np.ndarray, list[dict[str, Any]]]:
    mp3_path = AUDIO_DIR / f"{spec['id']}_raw.mp3"
    wav_path = AUDIO_DIR / f"{spec['id']}_raw.wav"

    words: list[dict[str, Any]] = []
    for attempt in range(3):
        words.clear()
        comm = edge_tts.Communicate(
            spec["text"],
            voice=spec["voice"],
            rate=spec["rate"],
            boundary="WordBoundary",
        )
        try:
            with open(mp3_path, "wb") as f:
                async for chunk in comm.stream():
                    if chunk["type"] == "audio":
                        f.write(chunk["data"])
                    elif chunk["type"] == "WordBoundary":
                        # offset & duration are in 100-nanosecond ticks (1e-7 sec)
                        start_s = chunk["offset"] / 10_000_000.0
                        dur_s = max(chunk["duration"] / 10_000_000.0, 0.08)
                        words.append(
                            {
                                "text": chunk["text"],
                                "start": start_s,
                                "end": start_s + dur_s,
                            }
                        )
            break
        except Exception:
            if attempt == 2:
                raise
            await asyncio.sleep(0.5)

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(mp3_path),
            "-ac",
            "1",
            "-ar",
            str(SR),
            str(wav_path),
        ],
        check=True,
    )
    _, pcm = wavfile.read(wav_path)
    audio = pcm.astype(np.float32) / 32768.0

    # Trim leading & trailing silence cleanly while updating word offsets
    env = np.abs(audio)
    active = np.where(env > 0.008)[0]
    if len(active) > 0:
        lead_idx = max(0, int(active[0]) - int(0.03 * SR))
        tail_idx = min(len(audio), int(active[-1]) + int(0.06 * SR))
        lead_sec = lead_idx / SR
        audio = audio[lead_idx:tail_idx]
        for w in words:
            w["start"] = max(0.0, w["start"] - lead_sec)
            w["end"] = max(w["start"] + 0.06, min(len(audio) / SR, w["end"] - lead_sec))

    return audio, words


def apply_voice_fx(mono: np.ndarray, fx_type: str) -> np.ndarray:
    """Return stereo (N, 2) processed vocal."""
    n = len(mono)
    # Normalize peak first
    peak = np.max(np.abs(mono)) + 1e-6
    x = mono / peak * 0.85

    if fx_type == "haunted_phone":
        # Telephone / eerie PA bandpass (350Hz - 3400Hz) + subtle overdrive + stereo ghost slapback
        sos = signal.butter(4, [360 / (SR / 2), 3400 / (SR / 2)], btype="band", output="sos")
        filtered = signal.sosfilt(sos, x)
        filtered = np.tanh(filtered * 2.1) * 0.72

        # Eerie stereo ghost delay (85ms left, 135ms right) + subtle dark reverb tail
        left = filtered.copy()
        right = filtered.copy()
        d1 = int(0.085 * SR)
        d2 = int(0.145 * SR)
        if n > d1:
            left[d1:] += filtered[:-d1] * 0.28
        if n > d2:
            right[d2:] += filtered[:-d2] * 0.24
        # Blend 25% full-body original so Vietnamese consonants stay super crisp
        left = left * 0.82 + x * 0.28
        right = right * 0.82 + x * 0.28
        return np.stack([left, right], axis=1)

    # Rich narrator EQ: warm low-mid boost + crisp presence + subtle dark subway room reflection
    sos_hp = signal.butter(2, 75 / (SR / 2), btype="high", output="sos")
    clean = signal.sosfilt(sos_hp, x)
    clean = np.tanh(clean * 1.25) * 0.86

    left = clean.copy()
    right = clean.copy()
    d_L = int(0.029 * SR)
    d_R = int(0.043 * SR)
    rev_amt = 0.14 if fx_type == "twist" else 0.08
    if n > d_L:
        left[d_L:] += clean[:-d_L] * rev_amt
    if n > d_R:
        right[d_R:] += clean[:-d_R] * rev_amt
    return np.stack([left, right], axis=1)


def group_subtitle_chunks(
    words: list[dict[str, Any]],
    offset_sec: float,
    highlight_set: set[str],
    speaker: str,
) -> list[dict[str, Any]]:
    """Group words into punchy 3-5 word TikTok subtitle chunks with exact word timings."""
    shifted = []
    for w in words:
        clean_tok = w["text"].strip(".,!?:;…\"'").lower()
        shifted.append(
            {
                "text": w["text"],
                "start": round(w["start"] + offset_sec, 3),
                "end": round(w["end"] + offset_sec, 3),
                "highlight": clean_tok in highlight_set,
            }
        )

    chunks: list[dict[str, Any]] = []
    cur: list[dict[str, Any]] = []
    for i, w in enumerate(shifted):
        cur.append(w)
        ends_punct = any(p in w["text"] for p in [".", ",", "!", "?", "…"])
        gap_next = (shifted[i + 1]["start"] - w["end"]) if i + 1 < len(shifted) else 0.0
        if len(cur) >= 4 or (len(cur) >= 2 and (ends_punct or gap_next > 0.18)):
            chunks.append(
                {
                    "speaker": speaker,
                    "start": cur[0]["start"],
                    "end": cur[-1]["end"] + 0.08,
                    "words": cur,
                }
            )
            cur = []
    if cur:
        chunks.append(
            {
                "speaker": speaker,
                "start": cur[0]["start"],
                "end": cur[-1]["end"] + 0.12,
                "words": cur,
            }
        )

    # Close tiny gaps within same scene so subtitles don't blink annoyingly
    for i in range(len(chunks) - 1):
        if chunks[i + 1]["start"] - chunks[i]["end"] < 0.22:
            chunks[i]["end"] = chunks[i + 1]["start"]
    return chunks


def add_stereo(mix: np.ndarray, clip: np.ndarray, start_sec: float, gain: float = 1.0) -> None:
    idx = max(0, int(start_sec * SR))
    if idx >= len(mix):
        return
    if clip.ndim == 1:
        clip = np.stack([clip, clip], axis=1)
    end = min(len(mix), idx + len(clip))
    mix[idx:end] += clip[: end - idx] * gain


def synth_sfx_and_score(total_samples: int, scenes_meta: list[dict[str, Any]]) -> np.ndarray:
    """Procedural dark thriller synth score + cinematic Foley SFX."""
    rng = np.random.default_rng(42)
    bed = np.zeros((total_samples, 2), dtype=np.float32)
    t = np.arange(total_samples, dtype=np.float32) / SR

    # 1. Dark Thriller Minor Drone (D1=36.7Hz, D2=73.4Hz, A2=110Hz, Eb3=155.6Hz eerie minor-9th)
    lfo1 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.17 * t)
    lfo2 = 0.5 + 0.5 * np.sin(2 * np.pi * 0.11 * t + 1.3)
    sub = np.sin(2 * np.pi * 36.71 * t) * 0.45 + np.sin(2 * np.pi * 73.42 * t) * 0.30
    pad_L = (
        signal.sawtooth(2 * np.pi * 73.42 * t, 0.5) * 0.18
        + np.sin(2 * np.pi * 110.0 * t + 0.3 * np.sin(2 * np.pi * 2.1 * t)) * 0.16 * lfo1
        + np.sin(2 * np.pi * 155.56 * t) * 0.11 * lfo2
    )
    pad_R = (
        signal.sawtooth(2 * np.pi * 73.85 * t, 0.5) * 0.18
        + np.sin(2 * np.pi * 110.4 * t + 0.3 * np.cos(2 * np.pi * 1.9 * t)) * 0.16 * lfo2
        + np.sin(2 * np.pi * 155.9 * t) * 0.11 * lfo1
    )
    sos_lp = signal.butter(3, 420 / (SR / 2), btype="low", output="sos")
    drone_L = signal.sosfilt(sos_lp, sub + pad_L)
    drone_R = signal.sosfilt(sos_lp, sub + pad_R)
    bed[:, 0] += drone_L * 0.28
    bed[:, 1] += drone_R * 0.28

    # 2. Subway Tunnel Ambience + Rhythmic Rail Clacks (especially Scenes 1-3)
    noise = rng.normal(0, 1, total_samples).astype(np.float32)
    sos_rumble = signal.butter(3, [45 / (SR / 2), 180 / (SR / 2)], btype="band", output="sos")
    rumble = signal.sosfilt(sos_rumble, noise) * 0.14
    bed[:, 0] += rumble
    bed[:, 1] += np.roll(rumble, 220)

    # Rail clack-clack every ~1.35s during first 20s
    for beat_t in np.arange(1.2, 24.0, 1.45):
        for offset, amp in [(0.0, 0.12), (0.19, 0.09)]:
            clack_len = int(0.07 * SR)
            ct = np.arange(clack_len, dtype=np.float32) / SR
            clack = rng.normal(0, 1, clack_len).astype(np.float32) * np.exp(-ct * 48.0)
            sos_cl = signal.butter(2, [300 / (SR / 2), 1800 / (SR / 2)], btype="band", output="sos")
            clack = signal.sosfilt(sos_cl, clack)
            add_stereo(bed, clack, float(beat_t + offset), amp)

    # 3. Scene 1 Opening Hit + Subway Brake Screech + HUD Typewriter Beeps
    s1_start = scenes_meta[0]["start"]
    hit_len = int(1.6 * SR)
    ht = np.arange(hit_len, dtype=np.float32) / SR
    sub_drop = np.sin(2 * np.pi * (95.0 * np.exp(-ht * 2.2) + 32.0) * ht) * np.exp(-ht * 2.4)
    screech = (
        np.sin(2 * np.pi * (2480 - 180 * ht) * ht) * 0.35
        + np.sin(2 * np.pi * (3710 - 240 * ht) * ht) * 0.22
    ) * np.exp(-ht * 2.8) * np.clip(ht * 8.0, 0, 1)
    add_stereo(bed, sub_drop * 0.55 + screech * 0.08, s1_start, 1.0)

    # Subtle digital HUD ticks (0.12s - 0.85s)
    for bt in np.linspace(0.12, 0.82, 9):
        bl = int(0.022 * SR)
        bt_arr = np.arange(bl, dtype=np.float32) / SR
        beep = np.sin(2 * np.pi * 1650 * bt_arr) * np.exp(-bt_arr * 140)
        add_stereo(bed, beep, float(bt), 0.09)

    # 4. Scene 3 Phone Vibration Buzz + Eerie Tritone Notification Chime
    s3_start = scenes_meta[2]["start"]
    for vib_off in [0.05, 0.32]:
        vl = int(0.20 * SR)
        vt = np.arange(vl, dtype=np.float32) / SR
        buzz = (
            np.sin(2 * np.pi * 148 * vt) * 0.6
            + signal.square(2 * np.pi * 74 * vt) * 0.25
        ) * (0.6 + 0.4 * np.sin(2 * np.pi * 28 * vt))
        sos_bz = signal.butter(2, 450 / (SR / 2), btype="low", output="sos")
        buzz = signal.sosfilt(sos_bz, buzz) * np.sin(np.pi * vt / 0.20)
        add_stereo(bed, buzz, s3_start + vib_off, 0.28)

    # Tritone chime (C6 -> F#5)
    for note_off, freq in [(0.12, 1046.5), (0.28, 739.99)]:
        nl = int(0.55 * SR)
        nt = np.arange(nl, dtype=np.float32) / SR
        bell = (np.sin(2 * np.pi * freq * nt) + 0.35 * np.sin(2 * np.pi * freq * 2.0 * nt)) * np.exp(-nt * 6.5)
        add_stereo(bed, bell, s3_start + note_off, 0.16)

    # 5. Scene 4 Radio Static Crackle + Accelerating Heartbeat (Scene 4 & Scene 5)
    s4_start = scenes_meta[3]["start"]
    s5_end = scenes_meta[4]["end"]
    # Short static burst entering Scene 4
    st_len = int(0.22 * SR)
    st_noise = rng.normal(0, 1, st_len).astype(np.float32) * np.linspace(1.0, 0.1, st_len)
    sos_st = signal.butter(2, [900 / (SR / 2), 4500 / (SR / 2)], btype="band", output="sos")
    add_stereo(bed, signal.sosfilt(sos_st, st_noise), s4_start, 0.18)

    hb_t = s4_start + 0.15
    interval = 0.78
    while hb_t < s5_end - 0.2:
        for beat_delay, f0, gain in [(0.0, 58.0, 0.42), (0.19, 48.0, 0.32)]:
            hl = int(0.16 * SR)
            ht_arr = np.arange(hl, dtype=np.float32) / SR
            thump = np.sin(2 * np.pi * (f0 * np.exp(-ht_arr * 8.0) + 28.0) * ht_arr) * np.exp(-ht_arr * 16.0)
            add_stereo(bed, thump, hb_t + beat_delay, gain)
        hb_t += interval
        interval = max(0.44, interval * 0.91)

    # 6. Scene 5 High-Tension Horror Riser sweeping up to Scene 6
    s5_start = scenes_meta[4]["start"]
    riser_dur = max(1.5, scenes_meta[4]["end"] - s5_start)
    rl = int(riser_dur * SR)
    rt = np.arange(rl, dtype=np.float32) / SR
    prog = rt / riser_dur
    phase = 2 * np.pi * (220.0 * rt + 420.0 * (rt**2) / riser_dur)
    riser = (np.sin(phase) * 0.5 + np.sin(phase * 1.015) * 0.5) * (prog**2.1)
    riser_noise = rng.normal(0, 1, rl).astype(np.float32) * (prog**2.6) * 0.35
    sos_rs = signal.butter(2, [600 / (SR / 2), 4200 / (SR / 2)], btype="band", output="sos")
    riser_tot = riser * 0.16 + signal.sosfilt(sos_rs, riser_noise) * 0.18
    add_stereo(bed, riser_tot, s5_start, 1.0)

    # 7. Scene 6 Dramatic Silence Drop -> Twist Sting & Final VHS Glitch + BRAAAM!
    s6 = scenes_meta[5]
    # Carve dramatic near-silence during first half of Scene 6 for maximum chills
    drop_a = int(s6["start"] * SR)
    drop_b = min(total_samples, int((s6["start"] + 1.8) * SR))
    bed[drop_a:drop_b] *= 0.22

    # Final BRAAAM + VHS Glitch Tear on the last ~1.15s
    braam_start = max(s6["start"] + 2.2, TARGET_TOTAL_SEC - 1.35)
    bl_len = max(int(0.5 * SR), total_samples - int(braam_start * SR))
    bt_arr = np.arange(bl_len, dtype=np.float32) / SR
    braam = (
        signal.sawtooth(2 * np.pi * 55.0 * bt_arr, 0.5) * 0.42
        + signal.sawtooth(2 * np.pi * 55.4 * bt_arr, 0.5) * 0.42
        + np.sin(2 * np.pi * 36.71 * bt_arr) * 0.65
        + np.sin(2 * np.pi * 116.54 * bt_arr) * 0.25
    ) * np.exp(-bt_arr * 1.65)
    sos_br = signal.butter(3, 680 / (SR / 2), btype="low", output="sos")
    braam = signal.sosfilt(sos_br, braam)
    add_stereo(bed, np.tanh(braam * 1.8), braam_start, 0.52)

    # Short VHS glitch static tear right at ~29.15s
    gl_len = int(0.18 * SR)
    gl_noise = rng.choice([-1.0, 0.0, 1.0], size=gl_len).astype(np.float32) * np.linspace(1.0, 0.2, gl_len)
    sos_gl = signal.butter(2, [500 / (SR / 2), 6000 / (SR / 2)], btype="band", output="sos")
    add_stereo(bed, signal.sosfilt(sos_gl, gl_noise), TARGET_TOTAL_SEC - 0.95, 0.22)

    return bed


async def main() -> None:
    raw_vocals: list[np.ndarray] = []
    raw_words: list[list[dict[str, Any]]] = []

    for spec in SCENES_SPEC:
        audio, words = await synth_line(spec)
        raw_vocals.append(audio)
        raw_words.append(words)

    speech_sum = sum(len(v) / SR for v in raw_vocals)
    pad_sum = sum(s["pre_pad"] + s["post_pad"] for s in SCENES_SPEC)
    print(f"Raw speech total: {speech_sum:.2f}s | Default pads: {pad_sum:.2f}s | Sum: {speech_sum + pad_sum:.2f}s")

    # Scale pads smoothly so total episode duration is EXACTLY 30.00s!
    remaining = TARGET_TOTAL_SEC - speech_sum
    if remaining < 1.8:
        raise RuntimeError(f"Speech too long ({speech_sum:.2f}s) for {TARGET_TOTAL_SEC}s target!")

    pad_scale = remaining / pad_sum
    total_samples = int(round(TARGET_TOTAL_SEC * SR))
    voice_stem = np.zeros((total_samples, 2), dtype=np.float32)

    scenes_meta: list[dict[str, Any]] = []
    all_subtitles: list[dict[str, Any]] = []
    cursor = 0.0

    for idx, (spec, mono, words) in enumerate(zip(SCENES_SPEC, raw_vocals, raw_words)):
        pre = spec["pre_pad"] * pad_scale
        post = spec["post_pad"] * pad_scale
        vocal_dur = len(mono) / SR
        scene_start = cursor
        vocal_start = scene_start + pre
        scene_end = TARGET_TOTAL_SEC if idx == len(SCENES_SPEC) - 1 else (vocal_start + vocal_dur + post)

        stereo_vox = apply_voice_fx(mono, spec["fx"])
        add_stereo(voice_stem, stereo_vox, vocal_start, 1.0)

        chunks = group_subtitle_chunks(
            words,
            offset_sec=vocal_start,
            highlight_set=spec["highlight_words"],
            speaker=spec["speaker"],
        )
        all_subtitles.extend(chunks)

        scenes_meta.append(
            {
                "id": spec["id"],
                "index": idx + 1,
                "speaker": spec["speaker"],
                "text": spec["text"],
                "start": round(scene_start, 3),
                "vocal_start": round(vocal_start, 3),
                "vocal_end": round(vocal_start + vocal_dur, 3),
                "end": round(scene_end, 3),
                "duration": round(scene_end - scene_start, 3),
            }
        )
        cursor = scene_end

    bed_stem = synth_sfx_and_score(total_samples, scenes_meta)

    # Smooth sidechain ducking: lower background bed by ~45% whenever voice is speaking
    vox_env = np.max(np.abs(voice_stem), axis=1)
    win = int(0.08 * SR)
    smooth_env = np.convolve(vox_env, np.ones(win, dtype=np.float32) / win, mode="same")
    duck_gain = 1.0 - 0.48 * np.clip(smooth_env * 4.5, 0.0, 1.0)
    master = voice_stem * 0.96 + bed_stem * duck_gain[:, None]

    # Gentle fade-in (80ms) and fade-out (350ms at the very end)
    fi = int(0.08 * SR)
    fo = int(0.35 * SR)
    master[:fi] *= np.linspace(0.0, 1.0, fi)[:, None]
    master[-fo:] *= np.linspace(1.0, 0.0, fo)[:, None]

    # Soft mastering limiter to -1.0 dBFS
    master = np.tanh(master * 1.18)
    peak = np.max(np.abs(master)) + 1e-6
    master = master / peak * 0.89

    out_wav = AUDIO_DIR / "master_mix.wav"
    wavfile.write(out_wav, SR, (master * 32767.0).astype(np.int16))

    timeline = {
        "title": "CHUYẾN TÀU LÚC 0 GIỜ — Tập 1: Quy Tắc Toa Số 4",
        "fps": 30,
        "width": 1080,
        "height": 1920,
        "duration": TARGET_TOTAL_SEC,
        "scenes": scenes_meta,
        "subtitles": all_subtitles,
    }
    timeline_path = AUDIO_DIR / "timeline.json"
    timeline_path.write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Saved master audio: {out_wav} ({TARGET_TOTAL_SEC:.2f}s)")
    for s in scenes_meta:
        print(f"  {s['id']}: {s['start']:5.2f}s -> {s['end']:5.2f}s ({s['duration']:.2f}s) | {s['speaker']}: {s['text']}")


if __name__ == "__main__":
    asyncio.run(main())
