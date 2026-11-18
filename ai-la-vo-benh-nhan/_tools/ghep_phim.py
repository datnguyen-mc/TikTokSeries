#!/usr/bin/env python3
"""Ghép phim "Ai Là Vợ Bệnh Nhân?" từ film/clips/<shot>.mp4.
Chạy từ gốc repo:  python3 ai-la-vo-benh-nhan/_tools/ghep_phim.py [00 01 ...]
- Không truyền cảnh: ghép toàn bộ thành film/Ai_La_Vo_Benh_Nhan_FULL.mp4
- Có truyền cảnh: ghép riêng các cảnh đó thành film/canh/canh-<đầu>[-<cuối>].mp4
Mỗi shot cắt đúng số giây trong bảng shot, chuẩn hoá 1280x720 24fps; giữa các cảnh có 0,6 giây đen.
Mỗi shot được mã hoá một lần vào film/_seg/ (đổi tên khi ffmpeg xong), rồi nối bằng concat -c copy."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import canh_a
import canh_b
import canh_c

CLIPS = os.path.join(ROOT, "film", "clips")
SEG = os.path.join(ROOT, "film", "_seg")
W, H, FPS = 1280, 720, 24
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]


def plan():
    out = {}
    for m in (canh_a, canh_b, canh_c):
        for sc, S in m.SCENES.items():
            out[sc] = [(s[0], s[2]) for s in S["shots"]]
    return out


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg lỗi:\n" + r.stderr[-1500:])


def norm(src, dst, dur):
    """Chuẩn hoá một shot; bỏ qua nếu bản chuẩn hoá mới hơn clip gốc."""
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return
    tmp = dst[:-4] + ".tmp.mp4"
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,"
          f"fps={FPS},format=yuv420p")
    run(["ffmpeg", "-y", "-i", src, "-t", str(dur), "-vf", vf, "-af", "aresample=48000,apad", "-shortest"] + ENC + [tmp])
    os.replace(tmp, dst)


def black(dst, d=0.6):
    if os.path.exists(dst):
        return
    tmp = dst[:-4] + ".tmp.mp4"
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={d}", "-f", "lavfi", "-i",
         "anullsrc=r=48000:cl=stereo", "-t", str(d)] + ENC + [tmp])
    os.replace(tmp, dst)


def main():
    P = plan()
    scenes = sys.argv[1:] or list(P)
    os.makedirs(SEG, exist_ok=True)
    missing = [c for sc in scenes for c, _ in P[sc] if not os.path.exists(os.path.join(CLIPS, f"{c}.mp4"))]
    if missing:
        print("Thiếu clip (bỏ qua):", ", ".join(missing))
    blk = os.path.join(SEG, "_black.mp4")
    black(blk)
    segs = []
    for i, sc in enumerate(scenes):
        if i:
            segs.append(blk)
        for c, d in P[sc]:
            src = os.path.join(CLIPS, f"{c}.mp4")
            if not os.path.exists(src):
                continue
            dst = os.path.join(SEG, f"{c}.mp4")
            norm(src, dst, d)
            segs.append(dst)
    lst = os.path.join(SEG, "_list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{s}'\n" for s in segs)
    if len(sys.argv) > 1:
        os.makedirs(os.path.join(ROOT, "film", "canh"), exist_ok=True)
        name = f"canh-{scenes[0]}" + (f"-{scenes[-1]}" if len(scenes) > 1 else "")
        out = os.path.join(ROOT, "film", "canh", name + ".mp4")
    else:
        out = os.path.join(ROOT, "film", "Ai_La_Vo_Benh_Nhan_FULL.mp4")
    tmp = out[:-4] + ".tmp.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", tmp])
    os.replace(tmp, out)
    print("Xong:", out, f"({len(segs)} đoạn)")


if __name__ == "__main__":
    main()
