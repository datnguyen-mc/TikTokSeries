#!/bin/bash
# Copy CSTT_<id>_*.mp4 from Downloads into film/clips/<id>.mp4 and check duration against shots.json
P=$HOME/mnt/TikTokSeries/cuon-sach-trao-tay
cd "$P"
for f in $HOME/mnt/Downloads/CSTT_*.mp4; do
  [ -e "$f" ] || continue
  b=$(basename "$f"); id=$(echo "$b" | sed -E 's/^CSTT_([0-9]{2}-[0-9]{2})_.*/\1/')
  [ -e "film/clips/$id.mp4" ] || cp -n "$f" "film/clips/$id.mp4"
done
python3 - <<'PY'
import json,subprocess,os
sh=json.load(open('film/shots.json'))
need=[s for s in sh if not s.get('existing')]
have=0;bad=[]
for s in need:
    p=f"film/clips/{s['id']}.mp4"
    if os.path.exists(p):
        have+=1
        d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout.strip() or 0)
        if abs(d-s['secs'])>0.5: bad.append((s['id'],s['secs'],round(d,2)))
print(f"clips: {have}/{len(need)}  duration mismatches: {bad}")
PY
