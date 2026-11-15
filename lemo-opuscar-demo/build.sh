#!/bin/sh
# One-command rebuild of the film. Needs the Lemo-Opuscar library (setup.sh prints LIB=...) and ffmpeg 7+.
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
LIB=${LIB:-$HOME/lemo-opuscar}
export LIB
[ -f "$LIB/core/render/video.mjs" ] || { echo "set LIB to the library folder"; exit 1; }
cd "$LIB"
"$LIB/.venv/bin/python" core/audio/sampler.py --need "$HERE/mix.py"
node core/render/events.mjs "$HERE"
node core/render/video.mjs "$HERE" --fps 60 --workers 3 --out "$HERE/out/video.mp4"
"$LIB/.venv/bin/python" "$HERE/mix.py"
sh core/render/mux.sh "$HERE/out/video.mp4" "$HERE/out/mix.wav" "$HERE/lemo-opuscar-demo.mp4" 60 0
node core/render/readcheck.mjs "$HERE"
