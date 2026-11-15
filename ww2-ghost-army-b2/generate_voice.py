import asyncio
import json
import subprocess
from pathlib import Path
import edge_tts

BASE = Path("/Users/iseul-a/Documents/TikTokSeries/ww2-ghost-army-b2")
SCRIPT_PATH = BASE / "script-vi.txt"
MP3_PATH = BASE / "narration_raw.mp3"
WAV_PATH = BASE / "narration.wav"
WORDS_PATH = BASE / "words.json"

VOICE = "vi-VN-NamMinhNeural"

async def main():
    text = SCRIPT_PATH.read_text(encoding="utf-8").strip()
    communicate = edge_tts.Communicate(text, voice=VOICE, boundary="WordBoundary")
    words = []
    with open(MP3_PATH, "wb") as audio_f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 10_000_000.0
                dur = chunk["duration"] / 10_000_000.0
                words.append({
                    "text": chunk["text"],
                    "start": round(start, 3),
                    "end": round(start + dur, 3),
                })

    # Convert to uncompressed PCM WAV at original native speed (no tempo/pitch filters)
    subprocess.run([
        "/opt/homebrew/bin/ffmpeg", "-y", "-v", "error",
        "-i", str(MP3_PATH),
        "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le",
        str(WAV_PATH)
    ], check=True)

    probe = subprocess.check_output([
        "/opt/homebrew/bin/ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(WAV_PATH)
    ], text=True).strip()

    duration = float(probe)
    WORDS_PATH.write_text(json.dumps({
        "voice": VOICE,
        "rate": "+0% (native original speed)",
        "duration": round(duration, 3),
        "word_count": len(words),
        "words": words
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated narration.wav: duration={duration:.3f}s, words={len(words)}")
    for i, w in enumerate(words):
        print(f"{i:02d}: [{w['start']:6.3f} - {w['end']:6.3f}] {w['text']}")

if __name__ == "__main__":
    asyncio.run(main())
