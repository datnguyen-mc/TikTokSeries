import json,glob,os,shutil,sys
P=os.path.expanduser('~/mnt/TikTokSeries/hop-dong-lam-chau/film/v3'); D=os.path.expanduser('~/mnt/Downloads')
m={}
for f in sorted(glob.glob(P+'/map_*.json')): m.update(json.load(open(f)))
ok=miss=0
for code,h in sorted(m.items()):
    dst=f'{P}/clips/{code}.mp4'
    if os.path.exists(dst): ok+=1; continue
    c=[f for f in glob.glob(f'{D}/*_{h}*.mp4')]
    if c: shutil.copy2(sorted(c)[0],dst); ok+=1
    else: miss+=1; print('missing',code,h)
print('ok',ok,'missing',miss)
