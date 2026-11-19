"""Thẻ chữ kiểu trailer điện ảnh Việt: chữ vàng ánh kim, nền tàn lửa bay, khung 2.39:1."""
import numpy as np, cv2, subprocess, os, unicodedata
from PIL import Image, ImageDraw, ImageFont
W, H, FPS = 1280, 720, 24
BAR = 92                                   # viền đen trên/dưới → 1280×536 (2.39:1)
LORA = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
def font(size, weight="SemiBold"):
    f = ImageFont.truetype(LORA, size)
    try: f.set_variation_by_name(weight)
    except Exception: pass
    return f
def text_mask(lines):
    """lines: [(text, size, tracking, weight)] → mask (H×W float 0..1), căn giữa khung."""
    im = Image.new("L", (W, H), 0); dr = ImageDraw.Draw(im)
    hs = [s * 1.35 for _, s, _, _ in lines]; y = H / 2 - sum(hs) / 2
    for (t, s, tr, wt), h in zip(lines, hs):
        t = unicodedata.normalize("NFC", t)
        f = font(s, wt); ws = [dr.textlength(c, font=f) for c in t]; tw = sum(ws) + s * tr * (len(t) - 1); x = (W - tw) / 2
        for c, w in zip(t, ws): dr.text((x, y), c, font=f, fill=255); x += w + s * tr
        y += h
    return np.asarray(im, np.float32) / 255
def gold(mask):
    """Tô vàng ánh kim: dải sáng ngang giữa chữ, viền tối nhẹ, ánh hào quang cam."""
    ys = np.where(mask.max(1) > 0.1)[0]; y0, y1 = (ys.min(), ys.max()) if len(ys) else (0, H)
    yy = np.clip((np.arange(H) - y0) / max(1, y1 - y0), 0, 1)[:, None]
    hi = np.exp(-((yy - 0.42) / 0.16) ** 2)                       # vệt sáng
    base = np.stack([60 + 120 * yy * 0 + 0 * yy, 0 * yy, 0 * yy], -1)  # placeholder
    r = 176 + 70 * hi + 0 * yy; g = 128 + 92 * hi - 18 * yy; b = 52 + 90 * hi - 20 * yy
    col = np.stack([b + 0 * mask, g + 0 * mask, r + 0 * mask], -1)    # BGR
    edge = cv2.GaussianBlur(mask, (0, 0), 1.2) - mask                # viền
    col = col * (1 - np.clip(edge, 0, 1)[..., None] * 0.6)
    return np.clip(col, 0, 255)
class Embers:
    def __init__(self, n=170, seed=7):
        r = np.random.default_rng(seed); self.r = r
        self.x = r.uniform(0, W, n); self.y = r.uniform(BAR, H - BAR, n); self.vx = r.normal(18, 10, n); self.vy = -r.uniform(14, 55, n)
        self.s = r.uniform(0.6, 3.2, n) ** 1.6; self.b = r.uniform(0.35, 1.0, n); self.ph = r.uniform(0, 6.3, n)
    def frame(self, t, dt=1 / FPS):
        img = np.zeros((H, W, 3), np.float32)
        self.x += self.vx * dt + 6 * np.sin(t * 1.7 + self.ph) * dt; self.y += self.vy * dt
        out = self.y < BAR - 10; self.y[out] = H - BAR + 10; self.x[out] = self.r.uniform(0, W, out.sum())
        flick = 0.65 + 0.35 * np.sin(t * 9 + self.ph * 3)
        for x, y, s, b, f in zip(self.x, self.y, self.s, self.b, flick):
            c = (40 * b * f, 120 * b * f, 255 * b * f)
            cv2.circle(img, (int(x), int(y)), max(1, int(s)), c, -1, lineType=cv2.LINE_AA)
        glow = cv2.GaussianBlur(img, (0, 0), 6) * 1.8
        # khói/ánh lửa mờ góc dưới phải
        yy, xx = np.mgrid[0:H, 0:W]
        return img + glow
def render_card(lines, dur, out, title=False, seed=7):
    em = Embers(220 if title else 170, seed); m = text_mask(lines); g = gold(m)
    halo = cv2.GaussianBlur(m, (0, 0), 14 if title else 9)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    warm = np.exp(-(((xx - W * 0.82) / 520) ** 2 + ((yy - H * 0.9) / 260) ** 2)) * 70     # ánh lửa góc
    p = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-f", "lavfi", "-t", f"{dur:.3f}", "-i", "anullsrc=r=48000:cl=stereo", "-shortest",
                          "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", out], stdin=subprocess.PIPE)
    n = round(dur * FPS)
    for i in range(n):
        t = i / FPS
        a = min(1, t / 0.6) * min(1, (dur - t) / 0.5)                                    # mờ vào/ra
        sc = 1 + 0.025 * t / dur
        M = cv2.getRotationMatrix2D((W / 2, H / 2), 0, sc)
        mi = cv2.warpAffine(m, M, (W, H)); gi = cv2.warpAffine(g, M, (W, H)); hi = cv2.warpAffine(halo, M, (W, H))
        f = em.frame(t)
        f[..., 2] += warm; f[..., 1] += warm * 0.35
        f += np.stack([hi * 20, hi * 70, hi * 150], -1) * a
        f = f * (1 - mi[..., None] * a) + gi * mi[..., None] * a
        f[:BAR] = 0; f[H - BAR:] = 0
        p.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()
if __name__ == "__main__":
    import sys
    render_card([("VỢ TÔI MẤT TRÍ NHỚ", 78, 0.08, "Bold"), ("CÓ CHỌN LỌC", 50, 0.3, "SemiBold")], 3.0, "/tmp/test_title.mov", title=True)
    cap = cv2.VideoCapture("/tmp/test_title.mov"); cap.set(1, 40); ok, im = cap.read(); cv2.imwrite(sys.argv[1], im)
