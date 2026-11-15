import json
import math
import random
from pathlib import Path
import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

OUT = Path("/Users/iseul-a/Documents/TikTokSeries/ww2-ghost-army-b2/art")
OUT.mkdir(parents=True, exist_ok=True)
FONT_PATH = "/Users/iseul-a/Documents/TikTokSeries/ww2-ghost-army-b2/fonts/Nunito.ttf"

INK = (38, 35, 31, 255)
INK_MID = (72, 66, 58, 255)
HEAD_WHITE = (253, 251, 245, 255)
CREAM_CARD = (250, 246, 235, 255)
OLIVE = (118, 136, 92, 255)
OLIVE_DARK = (86, 102, 66, 255)
OLIVE_LIGHT = (150, 168, 118, 255)
KHAKI = (212, 195, 160, 255)
KHAKI_DARK = (176, 156, 120, 255)
TERRACOTTA = (198, 100, 76, 255)
OCHRE = (226, 172, 78, 255)
SLATE = (96, 126, 148, 255)
SLATE_LIGHT = (142, 172, 190, 255)
WOOD = (148, 106, 70, 255)
CHARCOAL = (62, 65, 70, 255)


def load_font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size=size)


def draw_centered_text(draw: ImageDraw.ImageDraw, box, text: str, font: ImageFont.FreeTypeFont, fill=INK, stroke_width=0, stroke_fill=INK):
    x0, y0, x1, y1 = box
    bb = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    tx = (x0 + x1 - tw) / 2.0 - bb[0]
    ty = (y0 + y1 - th) / 2.0 - bb[1]
    draw.text((tx, ty), text, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)


def make_paper_bg(w: int, h: int, base_rgb: tuple, seed: int = 1, grain: float = 5.5) -> Image.Image:
    rng = np.random.default_rng(seed)
    arr = np.ones((h, w, 3), dtype=np.float32)
    arr[:, :, 0] = base_rgb[0]
    arr[:, :, 1] = base_rgb[1]
    arr[:, :, 2] = base_rgb[2]

    yy, xx = np.mgrid[0:h, 0:w]
    nx = (xx / w - 0.5) * 2.0
    ny = (yy / h - 0.5) * 2.0
    vig = 1.0 - 0.045 * (nx * nx + ny * ny)
    arr *= vig[:, :, None]

    coarse = rng.normal(0, grain * 0.85, (max(4, h // 24), max(4, w // 24))).astype(np.float32)
    coarse_img = Image.fromarray(np.clip(coarse + 128, 0, 255).astype(np.uint8)).resize((w, h), Image.Resampling.BICUBIC)
    coarse_arr = (np.asarray(coarse_img, dtype=np.float32) - 128.0)[:, :, None]
    fine = rng.normal(0, grain * 0.45, (h, w, 1)).astype(np.float32)
    arr = np.clip(arr + coarse_arr * 0.55 + fine, 0, 255).astype(np.uint8)
    return Image.fromarray(arr, mode="RGB").convert("RGBA")


def wobble_points(pts, amp=2.2, seed=7, closed=False):
    rng = random.Random(seed)
    pts = [tuple(map(float, p)) for p in pts]
    if closed and pts[0] != pts[-1]:
        pts.append(pts[0])
    out = []
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        dist = math.hypot(x2 - x1, y2 - y1)
        steps = max(3, int(dist / 18))
        dx, dy = x2 - x1, y2 - y1
        nx, ny = (-dy / (dist + 1e-6), dx / (dist + 1e-6))
        p_a = rng.uniform(0, math.tau)
        p_b = rng.uniform(0, math.tau)
        for s in range(steps):
            t = s / steps
            taper = math.sin(t * math.pi) if not closed else 1.0
            wob = (math.sin(t * math.pi * 2.0 + p_a) * 0.65 + math.sin(t * math.pi * 5.0 + p_b) * 0.35) * amp * taper
            out.append((x1 + dx * t + nx * wob, y1 + dy * t + ny * wob))
    out.append(pts[-1])
    return out


def stroke_line(draw: ImageDraw.ImageDraw, pts, width=8, color=INK, amp=2.0, seed=11):
    wpts = wobble_points(pts, amp=amp, seed=seed, closed=False)
    draw.line(wpts, fill=color, width=width, joint="curve")
    r = width / 2.0 - 0.5
    if r > 1.2:
        for px, py in (wpts[0], wpts[-1]):
            draw.ellipse((px - r, py - r, px + r, py + r), fill=color)


def gouache_poly(canvas: Image.Image, pts, fill=None, outline=INK, width=8, amp=2.2, seed=19, shade=True):
    wpts = wobble_points(pts, amp=amp, seed=seed, closed=True)
    if fill is not None:
        layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        ld.polygon(wpts, fill=fill)

        if shade and fill[3] > 180:
            xs = [p[0] for p in wpts]
            ys = [p[1] for p in wpts]
            x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys)
            h_span = max(8.0, y1 - y0)
            mask = layer.split()[3]
            wash = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
            wd = ImageDraw.Draw(wash)
            hi = (min(255, fill[0] + 24), min(255, fill[1] + 22), min(255, fill[2] + 18), 75)
            lo = (max(0, fill[0] - 28), max(0, fill[1] - 26), max(0, fill[2] - 22), 85)
            wd.ellipse((x0 - 20, y0 - h_span * 0.35, x1 + 20, y0 + h_span * 0.45), fill=hi)
            wd.ellipse((x0 - 20, y1 - h_span * 0.38, x1 + 20, y1 + h_span * 0.45), fill=lo)
            wash = wash.filter(ImageFilter.GaussianBlur(radius=max(4, int(h_span * 0.12))))
            wash.putalpha(ImageChops.multiply(wash.split()[3], mask))
            layer = Image.alpha_composite(layer, wash)

        canvas.alpha_composite(layer)

    if outline is not None and width > 0:
        d = ImageDraw.Draw(canvas)
        d.line(wpts, fill=outline, width=width, joint="curve")


def gouache_ellipse(canvas: Image.Image, box, fill=None, outline=INK, width=8, amp=1.8, seed=23, steps=44, shade=True):
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    rx, ry = (x1 - x0) / 2.0, (y1 - y0) / 2.0
    pts = [(cx + math.cos(i / steps * math.tau) * rx, cy + math.sin(i / steps * math.tau) * ry) for i in range(steps)]
    gouache_poly(canvas, pts, fill=fill, outline=outline, width=width, amp=amp, seed=seed, shade=shade)


def stroke_arc(draw: ImageDraw.ImageDraw, cx, cy, rx, ry, a0_deg, a1_deg, width=8, color=INK, amp=1.5, seed=41):
    steps = max(12, int(abs(a1_deg - a0_deg) / 4))
    pts = []
    for i in range(steps + 1):
        a = math.radians(a0_deg + (a1_deg - a0_deg) * (i / steps))
        pts.append((cx + math.cos(a) * rx, cy + math.sin(a) * ry))
    stroke_line(draw, pts, width=width, color=color, amp=amp, seed=seed)


def draw_star(canvas: Image.Image, cx, cy, r_outer, r_inner, fill=HEAD_WHITE, outline=INK, width=5, seed=77):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r))
    gouache_poly(canvas, pts, fill=fill, outline=outline, width=width, amp=0.9, seed=seed, shade=False)


def draw_b2_stickman_head(canvas: Image.Image, cx, cy, r=76, expr="smile", hat="helmet", facing=1, seed=10):
    gouache_ellipse(canvas, (cx - r, cy - r, cx + r, cy + r), fill=HEAD_WHITE, outline=INK, width=9, amp=1.8, seed=seed, shade=False)
    d = ImageDraw.Draw(canvas)
    cheek = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    cd = ImageDraw.Draw(cheek)
    cd.ellipse((cx + facing * 10 - 38, cy + 8, cx + facing * 10 - 14, cy + 24), fill=(228, 148, 128, 70))
    cd.ellipse((cx + facing * 10 + 14, cy + 8, cx + facing * 10 + 38, cy + 24), fill=(228, 148, 128, 70))
    canvas.alpha_composite(cheek)

    ex1 = cx + facing * 12 - 20
    ex2 = cx + facing * 12 + 20
    ey = cy - 6
    d.ellipse((ex1 - 7, ey - 9, ex1 + 7, ey + 9), fill=INK)
    d.ellipse((ex2 - 7, ey - 9, ex2 + 7, ey + 9), fill=INK)
    stroke_line(d, [(ex1 - 12, ey - 22), (ex1 + 10, ey - 26)], width=6, amp=0.8, seed=seed + 1)
    stroke_line(d, [(ex2 - 10, ey - 26), (ex2 + 12, ey - 22)], width=6, amp=0.8, seed=seed + 2)

    if expr == "smile":
        stroke_arc(d, cx + facing * 10, cy + 12, 22, 16, 18, 162, width=7, seed=seed + 3)
    elif expr == "grin":
        gouache_poly(canvas, [
            (cx + facing * 10 - 24, cy + 14),
            (cx + facing * 10 + 24, cy + 14),
            (cx + facing * 10 + 16, cy + 34),
            (cx + facing * 10 - 16, cy + 34),
        ], fill=TERRACOTTA, outline=INK, width=6, amp=0.8, seed=seed + 3, shade=False)
    elif expr == "open":
        gouache_ellipse(canvas, (cx + facing * 10 - 14, cy + 14, cx + facing * 10 + 14, cy + 38),
                        fill=TERRACOTTA, outline=INK, width=6, amp=0.8, seed=seed + 4, shade=False)

    if hat == "helmet":
        pts = [
            (cx - r - 16, cy - 14),
            (cx - r + 4, cy - r - 22),
            (cx, cy - r - 34),
            (cx + r - 4, cy - r - 22),
            (cx + r + 16, cy - 14),
            (cx, cy - 24),
        ]
        gouache_poly(canvas, pts, fill=OLIVE, outline=INK, width=9, amp=1.8, seed=seed + 5)
        stroke_line(ImageDraw.Draw(canvas), [(cx - r + 10, cy - 26), (cx + r - 10, cy - 26)], width=5, color=OLIVE_DARK, seed=seed + 6)
    elif hat == "beret":
        pts = [
            (cx - r - 8, cy - 24),
            (cx - r + 16, cy - r - 32),
            (cx + r + 32, cy - r - 8),
            (cx + r + 10, cy - 16),
        ]
        gouache_poly(canvas, pts, fill=TERRACOTTA, outline=INK, width=9, amp=1.8, seed=seed + 6)
        stroke_line(ImageDraw.Draw(canvas), [(cx + 6, cy - r - 28), (cx + 18, cy - r - 44)], width=7, seed=seed + 7)
    elif hat == "headphones":
        stroke_arc(ImageDraw.Draw(canvas), cx, cy - 8, r + 14, r + 18, 195, 345, width=12, color=CHARCOAL, amp=1.2, seed=seed + 8)
        gouache_ellipse(canvas, (cx - r - 26, cy - 28, cx - r + 6, cy + 26), fill=OCHRE, outline=INK, width=8, amp=1.0, seed=seed + 9)
        gouache_ellipse(canvas, (cx + r - 6, cy - 28, cx + r + 26, cy + 26), fill=OCHRE, outline=INK, width=8, amp=1.0, seed=seed + 10)
    elif hat == "cap":
        pts = [
            (cx - r - 4, cy - 24),
            (cx - r + 10, cy - r - 28),
            (cx + r - 6, cy - r - 24),
            (cx + r + 30 * facing, cy - 16),
        ]
        gouache_poly(canvas, pts, fill=KHAKI_DARK, outline=INK, width=9, amp=1.6, seed=seed + 11)


def save_2x_sprite(img_2x: Image.Image, name: str, meta: dict, pad_1x: int = 8):
    w1, h1 = img_2x.width // 2, img_2x.height // 2
    img = img_2x.resize((w1, h1), Image.Resampling.LANCZOS)
    bbox = img.getbbox()
    if bbox is None:
        raise RuntimeError(f"Empty sprite {name}")
    x0 = max(0, bbox[0] - pad_1x)
    y0 = max(0, bbox[1] - pad_1x)
    x1 = min(img.width, bbox[2] + pad_1x)
    y1 = min(img.height, bbox[3] + pad_1x)
    cropped = img.crop((x0, y0, x1, y1))
    cropped.save(OUT / name, "PNG")
    meta[name] = {"w": cropped.width, "h": cropped.height}


def draw_sherman_tank_2x(canvas: Image.Image, x, y, scale=1.0, rubber_marks=True, label="40 TẤN", seed=100):
    s = scale * 2.0
    turret = [
        (x - 95 * s, y - 76 * s),
        (x - 68 * s, y - 138 * s),
        (x + 54 * s, y - 138 * s),
        (x + 88 * s, y - 76 * s),
    ]
    gouache_poly(canvas, turret, fill=OLIVE, outline=INK, width=10, amp=2.6, seed=seed + 1)
    gouache_poly(canvas, [
        (x - 36 * s, y - 138 * s), (x - 28 * s, y - 156 * s),
        (x + 18 * s, y - 156 * s), (x + 25 * s, y - 138 * s)
    ], fill=OLIVE_DARK, outline=INK, width=9, amp=1.5, seed=seed + 2)
    droop = 14 * s if rubber_marks else 0
    barrel = [
        (x + 76 * s, y - 118 * s),
        (x + 170 * s, y - 120 * s + droop * 0.4),
        (x + 252 * s, y - 118 * s + droop),
        (x + 252 * s, y - 94 * s + droop),
        (x + 170 * s, y - 96 * s + droop * 0.4),
        (x + 78 * s, y - 94 * s),
    ]
    gouache_poly(canvas, barrel, fill=OLIVE_LIGHT, outline=INK, width=10, amp=2.0, seed=seed + 3)

    hull = [
        (x - 216 * s, y - 20 * s),
        (x - 182 * s, y - 82 * s),
        (x + 176 * s, y - 82 * s),
        (x + 216 * s, y - 20 * s),
    ]
    gouache_poly(canvas, hull, fill=OLIVE_LIGHT, outline=INK, width=10, amp=2.6, seed=seed + 4)

    gouache_ellipse(canvas, (x - 152 * s, y - 74 * s, x - 98 * s, y - 22 * s), fill=HEAD_WHITE, outline=INK, width=7, amp=1.2, seed=seed + 5, shade=False)
    draw_star(canvas, x - 125 * s, y - 48 * s, 18 * s, 8 * s, fill=OLIVE_DARK, outline=None, width=0, seed=seed + 6)

    gouache_ellipse(canvas, (x - 226 * s, y - 28 * s, x + 226 * s, y + 66 * s), fill=CHARCOAL, outline=INK, width=10, amp=2.8, seed=seed + 7)
    gouache_ellipse(canvas, (x - 198 * s, y - 12 * s, x + 198 * s, y + 48 * s), fill=KHAKI_DARK, outline=INK, width=8, amp=2.0, seed=seed + 8)
    for wx in [-144, -72, 0, 72, 144]:
        gouache_ellipse(canvas, (x + (wx - 25) * s, y - 6 * s, x + (wx + 25) * s, y + 44 * s), fill=OLIVE_DARK, outline=INK, width=8, amp=1.4, seed=seed + 10 + wx)
        gouache_ellipse(canvas, (x + (wx - 8) * s, y + 11 * s, x + (wx + 8) * s, y + 27 * s), fill=KHAKI, outline=INK, width=5, amp=0.8, seed=seed + 20 + wx, shade=False)

    if rubber_marks:
        patch = [
            (x + 98 * s, y - 70 * s), (x + 148 * s, y - 68 * s),
            (x + 145 * s, y - 30 * s), (x + 95 * s, y - 32 * s)
        ]
        gouache_poly(canvas, patch, fill=KHAKI, outline=INK, width=6, amp=1.2, seed=seed + 30, shade=False)
        d = ImageDraw.Draw(canvas)
        for sx_off in [108, 122, 136]:
            stroke_line(d, [(x + sx_off * s, y - 74 * s), (x + sx_off * s, y - 63 * s)], width=4, seed=sx_off)
            stroke_line(d, [(x + sx_off * s, y - 36 * s), (x + sx_off * s, y - 26 * s)], width=4, seed=sx_off + 1)
        gouache_poly(canvas, [
            (x - 244 * s, y + 2 * s), (x - 216 * s, y + 2 * s),
            (x - 216 * s, y + 26 * s), (x - 244 * s, y + 26 * s)
        ], fill=TERRACOTTA, outline=INK, width=7, amp=1.0, seed=seed + 31, shade=False)

    if label:
        d = ImageDraw.Draw(canvas)
        fnt = load_font(int(34 * s))
        draw_centered_text(d, (x - 75 * s, y - 78 * s, x + 85 * s, y - 22 * s), label, fnt, fill=HEAD_WHITE, stroke_width=int(4 * scale * 2), stroke_fill=INK)


def build_backgrounds():
    # NOTE ON COORDINATES: Background PNGs are 1080x1920; design plane is 1280x2275.56 (factor 1.185185x)!
    # --- SHOT 1 BG: Sunny English Coastal Meadow ---
    bg1 = make_paper_bg(1080, 1920, (243, 237, 222), seed=101)
    sky = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    ImageDraw.Draw(sky).rectangle((0, 0, 1080, 960), fill=(198, 219, 228, 115))
    bg1.alpha_composite(sky)
    # Clouds placed cleanly at y=430..450px (510..535 design units) clear of header AND badge!
    for cx, cy, rw, rh, sd in [(165, 435, 115, 38, 1), (905, 445, 120, 40, 2)]:
        gouache_ellipse(bg1, (cx - rw, cy - rh, cx + rw, cy + rh), fill=HEAD_WHITE, outline=INK_MID, width=4, amp=3.0, seed=sd)
    gouache_poly(bg1, [(-10, 905), (1090, 890), (1090, 995), (-10, 1005)], fill=SLATE_LIGHT, outline=INK_MID, width=4, amp=2.5, seed=4)
    gouache_poly(bg1, [(-10, 985), (350, 935), (760, 955), (1090, 920), (1090, 1930), (-10, 1930)], fill=(182, 196, 142, 255), outline=INK, width=5, amp=3.2, seed=5)
    gouache_poly(bg1, [(-10, 1210), (490, 1180), (1090, 1215), (1090, 1930), (-10, 1930)], fill=(212, 200, 160, 255), outline=INK_MID, width=4, amp=3.0, seed=6)
    for tx, ty, sc in [(175, 980, 0.88), (905, 965, 0.92)]:
        gouache_poly(bg1, [(tx - 95 * sc, ty + 55 * sc), (tx, ty - 48 * sc), (tx + 95 * sc, ty + 55 * sc)], fill=KHAKI_DARK, outline=INK, width=4, amp=1.8, seed=int(tx))
        gouache_poly(bg1, [(tx - 24 * sc, ty + 55 * sc), (tx, ty - 10 * sc), (tx + 24 * sc, ty + 55 * sc)], fill=CHARCOAL, outline=INK, width=3, amp=1.0, seed=int(tx) + 2, shade=False)
    d1 = ImageDraw.Draw(bg1)
    for gx, gy in [(160, 1360), (880, 1390), (540, 1335)]:
        stroke_line(d1, [(gx - 12, gy), (gx - 18, gy - 20)], width=3, color=OLIVE_DARK, seed=gx)
        stroke_line(d1, [(gx, gy), (gx + 2, gy - 24)], width=3, color=OLIVE_DARK, seed=gx + 1)
        stroke_line(d1, [(gx + 12, gy), (gx + 18, gy - 18)], width=3, color=OLIVE_DARK, seed=gx + 2)
    bg1.save(OUT / "s1_bg.png", "PNG")

    # --- SHOT 2 BG: Field Tarp & Air-Pump Workshop (Grounded crate + blueprint poster!) ---
    bg2 = make_paper_bg(1080, 1920, (240, 232, 214), seed=102)
    # Framed rubber-tank inflation schematic on upper workshop tent wall (fills y=380..720px naturally!)
    gouache_poly(bg2, [(240, 390), (840, 385), (845, 715), (235, 720)], fill=CREAM_CARD, outline=INK, width=5, amp=2.0, seed=11)
    d2 = ImageDraw.Draw(bg2)
    gouache_poly(bg2, [(265, 415), (815, 410), (820, 690), (260, 695)], fill=SLATE_LIGHT, outline=INK_MID, width=3, amp=1.5, seed=111)
    stroke_line(d2, [(340, 595), (740, 595)], width=4, color=HEAD_WHITE, seed=112)
    stroke_arc(d2, 535, 595, 135, 80, 180, 360, width=4, color=HEAD_WHITE, seed=113)
    draw_centered_text(d2, (265, 425, 815, 485), "MẪU M4 SHERMAN BƠM HƠI", load_font(28), fill=HEAD_WHITE)
    # Ground plane & khaki tarp
    gouache_poly(bg2, [(-10, 960), (1090, 945), (1090, 1930), (-10, 1930)], fill=(190, 182, 142, 255), outline=INK, width=5, amp=2.8, seed=12)
    gouache_poly(bg2, [(65, 1060), (1015, 1045), (1030, 1520), (55, 1535)], fill=KHAKI, outline=INK, width=5, amp=2.8, seed=13)
    # Grounded wooden supply crate sitting ON the grass horizon (y=790..965px -> grounded on y=950!)
    gouache_poly(bg2, [(790, 785), (990, 782), (994, 968), (786, 970)], fill=(186, 154, 112, 255), outline=INK, width=4, amp=1.8, seed=14)
    stroke_line(d2, [(790, 785), (994, 968)], width=3, color=INK_MID, seed=15)
    stroke_line(d2, [(990, 782), (786, 970)], width=3, color=INK_MID, seed=16)
    bg2.save(OUT / "s2_bg.png", "PNG")

    # --- SHOT 3 BG: Secret Studio & Drafting Tent (Floor raised to y=1040px = 1232 design units!) ---
    bg3 = make_paper_bg(1080, 1920, (244, 237, 223), seed=103)
    # Small corner drapes well clear of header text (y <= 190px at x=120..960)
    gouache_poly(bg3, [(-10, -10), (175, -10), (55, 220), (-10, 280)], fill=KHAKI_DARK, outline=INK, width=5, seed=21)
    gouache_poly(bg3, [(905, -10), (1090, -10), (1090, 280), (1025, 220)], fill=KHAKI_DARK, outline=INK, width=5, seed=22)
    # Blueprint & sketch boards high enough (y=330..565px = 391..670 design units) so boom mic never touches them!
    gouache_poly(bg3, [(135, 335), (505, 328), (510, 560), (130, 568)], fill=SLATE, outline=INK, width=5, seed=23)
    d3 = ImageDraw.Draw(bg3)
    stroke_line(d3, [(185, 485), (455, 485)], width=3, color=HEAD_WHITE, seed=231)
    stroke_arc(d3, 315, 485, 95, 52, 180, 360, width=3, color=HEAD_WHITE, seed=232)
    gouache_poly(bg3, [(575, 332), (945, 340), (940, 565), (570, 558)], fill=CREAM_CARD, outline=INK, width=5, seed=24)
    draw_centered_text(d3, (575, 340, 940, 560), "23rd HQ · TOP SECRET", load_font(27), fill=TERRACOTTA)
    # Warm wooden studio floor starting at y=1040px (= 1232 design units, so cast feet at y=1320..1360 stand firmly ON the planks!)
    gouache_poly(bg3, [(-10, 1040), (1090, 1040), (1090, 1930), (-10, 1930)], fill=(198, 170, 132, 255), outline=INK, width=5, seed=25)
    for fy in [1155, 1280, 1415, 1555]:
        stroke_line(d3, [(0, fy), (1080, fy)], width=3, color=(132, 106, 76, 255), seed=fy)
    bg3.save(OUT / "s3_bg.png", "PNG")

    # --- SHOT 4 BG: Night Acoustic Deception Hillside ---
    bg4 = make_paper_bg(1080, 1920, (44, 56, 76), seed=104, grain=5.0)
    # Crescent moon placed at upper-left-center (x=230, y=215px) completely away from right-side radio mast!
    glow = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((135, 125, 325, 315), fill=(244, 224, 168, 52))
    glow = glow.filter(ImageFilter.GaussianBlur(22))
    bg4.alpha_composite(glow)
    crescent = []
    for i in range(25):
        a = math.radians(45 + 270 * (i / 24))
        crescent.append((230 + math.cos(a) * 48, 220 + math.sin(a) * 48))
    for i in range(25):
        a = math.radians(315 - 270 * (i / 24))
        crescent.append((252 + math.cos(a) * 39, 210 + math.sin(a) * 39))
    gouache_poly(bg4, crescent, fill=(246, 228, 174, 255), outline=INK, width=3, amp=0.9, seed=31, shade=False)
    d4 = ImageDraw.Draw(bg4)
    for sx, sy in [(450, 195), (620, 175), (810, 210), (920, 265), (490, 295)]:
        d4.ellipse((sx - 5, sy - 5, sx + 5, sy + 5), fill=(248, 235, 192, 230))
    # Upper ridge flat plateau at y=715px (= 847 design units) so s4_dummy sits solidly ON the ridge!
    gouache_poly(bg4, [(-10, 715), (1090, 715), (1090, 1930), (-10, 1930)], fill=(64, 82, 92, 255), outline=INK, width=5, amp=2.0, seed=32)
    # Lower foreground flat road ridge at y=1195px (= 1416 design units) so s4_truck rolls horizontally ON the ridge!
    gouache_poly(bg4, [(-10, 1195), (1090, 1195), (1090, 1930), (-10, 1930)], fill=(54, 70, 62, 255), outline=INK, width=5, amp=2.0, seed=33)
    bg4.save(OUT / "s4_bg.png", "PNG")

    # --- SHOT 5 BG: Vintage Tactical Parchment Map (Calais coast raised & Channel label centered!) ---
    bg5 = make_paper_bg(1080, 1920, (236, 225, 199), seed=105, grain=6.0)
    gouache_poly(bg5, [(48, 165), (1032, 165), (1032, 1755), (48, 1755)], fill=SLATE_LIGHT, outline=INK, width=6, amp=1.6, seed=40)
    # Southern England (top, jutting toward Dover at x=620, y=520px)
    england = [(48, 165), (1032, 165), (1032, 435), (840, 465), (650, 525), (410, 515), (180, 565), (48, 550)]
    gouache_poly(bg5, england, fill=KHAKI, outline=INK, width=6, amp=3.0, seed=41)
    # France landmass: rises high at Pas-de-Calais on upper-right (x=640..1032, y=625..720px = 740..853 design units!)
    # and sweeps down to Normandy bay at lower-left (x=48..540, y=1110..1160px = 1315..1375 design units!)
    france = [(48, 1120), (280, 1105), (475, 1145), (585, 955), (665, 685), (835, 625), (1032, 605), (1032, 1755), (48, 1755)]
    gouache_poly(bg5, france, fill=(224, 208, 172, 255), outline=INK, width=6, amp=3.0, seed=42)
    d5 = ImageDraw.Draw(bg5)
    for wx, wy in [(160, 720), (410, 740), (220, 920)]:
        stroke_line(d5, [(wx - 28, wy), (wx - 10, wy - 7), (wx + 10, wy + 5), (wx + 28, wy - 4)], width=3, color=HEAD_WHITE, seed=wx + wy)
    gouache_ellipse(bg5, (835, 1305, 965, 1435), fill=CREAM_CARD, outline=INK, width=4, seed=44, shade=False)
    draw_star(bg5, 900, 1370, 48, 16, fill=SLATE, outline=INK, width=3, seed=45)
    d5.text((265, 305), "ANH QUỐC (1944)", font=load_font(38), fill=INK)
    d5.text((95, 815), "EO BIỂN MANCHE", font=load_font(30), fill=INK_MID)
    d5.text((645, 1215), "PHÁP", font=load_font(38), fill=INK_MID)
    bg5.save(OUT / "s5_bg.png", "PNG")

    # --- SHOT 6 BG: Golden Dawn Normandy Beach Landing ---
    bg6 = make_paper_bg(1080, 1920, (245, 235, 212), seed=106)
    sun = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    ImageDraw.Draw(sun).ellipse((320, 410, 760, 820), fill=(248, 204, 122, 170))
    sun = sun.filter(ImageFilter.GaussianBlur(22))
    bg6.alpha_composite(sun)
    # Sea band y=650..960px (= 770..1138 design units), sloping sandy beach below, green bluff on right y=1120px (= 1327 design units)
    gouache_poly(bg6, [(-10, 650), (1090, 650), (1090, 935), (-10, 1065)], fill=SLATE, outline=INK, width=5, amp=2.5, seed=52)
    gouache_poly(bg6, [(-10, 1040), (540, 965), (1090, 915), (1090, 1930), (-10, 1930)], fill=KHAKI, outline=INK, width=5, amp=2.8, seed=54)
    gouache_poly(bg6, [(480, 1145), (840, 1110), (1090, 1105), (1090, 1930), (480, 1930)], fill=OLIVE_LIGHT, outline=INK, width=5, amp=2.8, seed=55)
    d6 = ImageDraw.Draw(bg6)
    stroke_line(d6, [(30, 1020), (390, 972), (740, 932), (1050, 905)], width=9, color=HEAD_WHITE, amp=3.5, seed=53)
    bg6.save(OUT / "s6_bg.png", "PNG")


def draw_stickman_body_2x(canvas: Image.Image, sx, hip_y, shoulder_y, tunic_color=OLIVE, leg_spread=72, foot_y=None, seed=1):
    d = ImageDraw.Draw(canvas)
    if foot_y is None:
        foot_y = hip_y + 250
    sh = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((sx - leg_spread - 45, foot_y - 18, sx + leg_spread + 45, foot_y + 26), fill=(38, 35, 31, 45))
    canvas.alpha_composite(sh)
    stroke_line(d, [(sx - 18, hip_y), (sx - leg_spread * 0.6, (hip_y + foot_y) / 2), (sx - leg_spread, foot_y)], width=11, seed=seed + 1)
    stroke_line(d, [(sx + 18, hip_y), (sx + leg_spread * 0.6, (hip_y + foot_y) / 2), (sx + leg_spread, foot_y)], width=11, seed=seed + 2)
    gouache_ellipse(canvas, (sx - leg_spread - 34, foot_y - 14, sx - leg_spread + 16, foot_y + 16), fill=CHARCOAL, outline=INK, width=7, seed=seed + 3, shade=False)
    gouache_ellipse(canvas, (sx + leg_spread - 16, foot_y - 14, sx + leg_spread + 34, foot_y + 16), fill=CHARCOAL, outline=INK, width=7, seed=seed + 4, shade=False)
    stroke_line(d, [(sx, shoulder_y - 36), (sx, shoulder_y + 4)], width=11, seed=seed + 9)
    gouache_poly(canvas, [
        (sx - 44, shoulder_y),
        (sx + 44, shoulder_y),
        (sx + 52, hip_y),
        (sx - 52, hip_y),
    ], fill=tunic_color, outline=INK, width=9, amp=1.8, seed=seed + 5)


def build_sprites(meta: dict):
    # =========================================================================
    # SHOT 1 SPRITES: Direct unbroken palm-to-tread contact + centered badge!
    # =========================================================================
    im = Image.new("RGBA", (1400, 720), (0, 0, 0, 0))
    draw_sherman_tank_2x(im, 660, 490, scale=1.12, rubber_marks=True, label="40 TẤN", seed=110)
    save_2x_sprite(im, "s1_rubber_tank.png", meta)

    im = Image.new("RGBA", (1360, 980), (0, 0, 0, 0))
    for idx, (sx, facing) in enumerate([(370, 1), (990, -1)]):
        draw_stickman_body_2x(im, sx, hip_y=615, shoulder_y=390, tunic_color=OLIVE, leg_spread=74, foot_y=885, seed=120 + idx * 20)
        d = ImageDraw.Draw(im)
        # Tall raised arms reaching up into cupped hands so tank treads sit solidly IN their palms!
        stroke_line(d, [(sx - 40, 408), (sx - 96, 225), (sx - 68, 46)], width=11, seed=134 + idx)
        stroke_line(d, [(sx + 40, 408), (sx + 96, 225), (sx + 68, 46)], width=11, seed=136 + idx)
        gouache_ellipse(im, (sx - 96, 20, sx - 40, 62), fill=HEAD_WHITE, outline=INK, width=7, seed=138 + idx, shade=False)
        gouache_ellipse(im, (sx + 40, 20, sx + 96, 62), fill=HEAD_WHITE, outline=INK, width=7, seed=140 + idx, shade=False)
        draw_b2_stickman_head(im, sx, 285, r=78, expr="grin", hat="helmet", facing=facing, seed=150 + idx * 10)
    save_2x_sprite(im, "s1_soldiers_lifting.png", meta)

    im = Image.new("RGBA", (860, 260), (0, 0, 0, 0))
    gouache_poly(im, [(36, 36), (824, 32), (828, 216), (32, 220)], fill=CREAM_CARD, outline=INK, width=9, amp=1.8, seed=165, shade=False)
    draw_centered_text(ImageDraw.Draw(im), (40, 36, 820, 216), "NHẸ NHƯ BÔNG?!", load_font(66), fill=TERRACOTTA)
    save_2x_sprite(im, "s1_feather_badge.png", meta)

    # =========================================================================
    # SHOT 2 SPRITES: Grounded soldier+pump base + separate moving plunger + clean puff!
    # =========================================================================
    im = Image.new("RGBA", (1520, 840), (0, 0, 0, 0))
    draw_sherman_tank_2x(im, 760, 560, scale=1.22, rubber_marks=True, label="CAO SU", seed=210)
    save_2x_sprite(im, "s2_floppy_tank.png", meta)

    # Static grounded soldier + red pump cylinder body + hose reaching tank valve
    im = Image.new("RGBA", (960, 1000), (0, 0, 0, 0))
    sx = 270
    draw_stickman_body_2x(im, sx, hip_y=650, shoulder_y=425, tunic_color=OLIVE, leg_spread=74, foot_y=910, seed=220)
    draw_b2_stickman_head(im, sx + 14, 318, r=78, expr="smile", hat="helmet", facing=1, seed=223)
    d = ImageDraw.Draw(im)
    # Red pump cylinder & base planted firmly on floor at y=915
    gouache_poly(im, [(564, 665), (676, 665), (684, 910), (556, 910)], fill=TERRACOTTA, outline=INK, width=9, seed=228)
    stroke_line(d, [(510, 915), (735, 915)], width=14, seed=229)
    # Black air hose feeding right into the tank's red inflation nozzle
    stroke_line(d, [(682, 875), (810, 875), (895, 790)], width=12, color=CHARCOAL, amp=2.0, seed=230)
    save_2x_sprite(im, "s2_pump_soldier.png", meta)

    # Separate moving plunger T-handle + soldier's pumping hands (tucks behind tunic & inside cylinder!)
    im = Image.new("RGBA", (580, 460), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # Forearms reaching from behind olive tunic to T-handle
    stroke_line(d, [(8, 72), (210, 102), (351, 112)], width=11, seed=224)
    stroke_line(d, [(8, 108), (210, 132), (411, 112)], width=11, seed=225)
    # Long steel rod sliding deep inside the red pump cylinder + wooden T-handle + white hands
    stroke_line(d, [(386, 112), (386, 430)], width=11, color=CHARCOAL, seed=227)
    stroke_line(d, [(291, 112), (481, 112)], width=18, color=WOOD, seed=226)
    gouache_ellipse(im, (321, 92, 368, 132), fill=HEAD_WHITE, outline=INK, width=7, seed=2261, shade=False)
    gouache_ellipse(im, (404, 92, 451, 132), fill=HEAD_WHITE, outline=INK, width=7, seed=2262, shade=False)
    save_2x_sprite(im, "s2_pump_plunger.png", meta)

    # Merged outer-contour cloud puff (ZERO internal black arcs crossing text!)
    im = Image.new("RGBA", (680, 340), (0, 0, 0, 0))
    mask = Image.new("L", (680, 340), 0)
    md = ImageDraw.Draw(mask)
    for cx, cy, rx, ry in [(175, 180, 115, 82), (335, 145, 145, 98), (495, 180, 115, 82), (340, 205, 155, 82)]:
        md.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255)
    outer = mask.filter(ImageFilter.MaxFilter(17))
    ring = ImageChops.subtract(outer, mask)
    puff_fill = Image.new("RGBA", (680, 340), HEAD_WHITE)
    puff_fill.putalpha(mask)
    puff_ink = Image.new("RGBA", (680, 340), INK)
    puff_ink.putalpha(ring)
    im.alpha_composite(puff_fill)
    im.alpha_composite(puff_ink)
    draw_centered_text(ImageDraw.Draw(im), (95, 95, 585, 255), "BƠM HƠI!", load_font(62), fill=SLATE)
    save_2x_sprite(im, "s2_air_puffs.png", meta)

    # =========================================================================
    # SHOT 3 SPRITES: Grounded Cast + Shoulder-Articulated Connected Arm+Hand+Prop!
    # =========================================================================
    # 3A: Grounded Painter body (holding palette in left hand; right arm is on s3_brush_prop!)
    im = Image.new("RGBA", (640, 1020), (0, 0, 0, 0))
    sx = 310
    draw_stickman_body_2x(im, sx, hip_y=690, shoulder_y=455, tunic_color=KHAKI, leg_spread=68, foot_y=950, seed=301)
    draw_b2_stickman_head(im, sx, 345, r=78, expr="smile", hat="beret", facing=1, seed=304)
    d = ImageDraw.Draw(im)
    stroke_line(d, [(sx - 42, 490), (156, 570)], width=11, seed=305)
    gouache_ellipse(im, (56, 510, 236, 640), fill=OCHRE, outline=INK, width=8, seed=306)
    gouache_ellipse(im, (92, 544, 128, 580), fill=TERRACOTTA, outline=INK, width=4, seed=3061, shade=False)
    gouache_ellipse(im, (144, 536, 180, 572), fill=OLIVE, outline=INK, width=4, seed=3062, shade=False)
    save_2x_sprite(im, "s3_painter.png", meta)

    # Shoulder-connected right arm + white hand + giant olive paintbrush (tucks behind khaki tunic!)
    im = Image.new("RGBA", (440, 460), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    stroke_line(d, [(12, 390), (215, 295)], width=11, seed=307)
    stroke_line(d, [(165, 365), (320, 115)], width=18, color=WOOD, seed=308)
    gouache_poly(im, [(295, 122), (365, 36), (398, 98), (338, 148)], fill=OLIVE, outline=INK, width=8, seed=309)
    gouache_ellipse(im, (192, 272, 238, 318), fill=HEAD_WHITE, outline=INK, width=7, seed=3091, shade=False)
    save_2x_sprite(im, "s3_brush_prop.png", meta)

    # 3B: Grounded Sound Engineer body (left hand on reel-to-reel deck; right arm is on s3_boom_prop!)
    im = Image.new("RGBA", (560, 1020), (0, 0, 0, 0))
    sx = 280
    draw_stickman_body_2x(im, sx, hip_y=690, shoulder_y=455, tunic_color=SLATE, leg_spread=68, foot_y=950, seed=311)
    draw_b2_stickman_head(im, sx, 345, r=78, expr="open", hat="headphones", facing=1, seed=314)
    d = ImageDraw.Draw(im)
    stroke_line(d, [(sx - 44, 490), (sx - 98, 560)], width=11, seed=3160)
    gouache_poly(im, [(sx - 88, 520), (sx + 88, 520), (sx + 88, 646), (sx - 88, 646)], fill=KHAKI_DARK, outline=INK, width=8, seed=315)
    gouache_ellipse(im, (sx - 64, 546, sx - 12, 598), fill=HEAD_WHITE, outline=INK, width=6, seed=3151, shade=False)
    gouache_ellipse(im, (sx + 12, 546, sx + 64, 598), fill=HEAD_WHITE, outline=INK, width=6, seed=3152, shade=False)
    gouache_ellipse(im, (sx - 112, 546, sx - 72, 586), fill=HEAD_WHITE, outline=INK, width=7, seed=3161, shade=False)
    save_2x_sprite(im, "s3_sound_eng.png", meta)

    # Shoulder-connected right arm + white hand + boom mic (tucks behind slate tunic!)
    im = Image.new("RGBA", (460, 480), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    stroke_line(d, [(14, 410), (215, 315)], width=11, seed=316)
    stroke_line(d, [(170, 380), (335, 115)], width=11, color=CHARCOAL, seed=317)
    gouache_ellipse(im, (302, 56, 396, 140), fill=CHARCOAL, outline=INK, width=8, seed=318)
    gouache_ellipse(im, (192, 292, 238, 338), fill=HEAD_WHITE, outline=INK, width=7, seed=3181, shade=False)
    save_2x_sprite(im, "s3_boom_prop.png", meta)

    # 3C: Grounded Actor body (waving right hand; left arm is on s3_clapper_prop!)
    im = Image.new("RGBA", (560, 1020), (0, 0, 0, 0))
    sx = 290
    draw_stickman_body_2x(im, sx, hip_y=690, shoulder_y=455, tunic_color=OLIVE_LIGHT, leg_spread=68, foot_y=950, seed=321)
    draw_b2_stickman_head(im, sx, 345, r=78, expr="grin", hat="cap", facing=-1, seed=324)
    d = ImageDraw.Draw(im)
    stroke_line(d, [(sx + 42, 490), (430, 395)], width=11, seed=3251)
    gouache_ellipse(im, (414, 374, 454, 414), fill=HEAD_WHITE, outline=INK, width=7, seed=3252, shade=False)
    save_2x_sprite(im, "s3_actor.png", meta)

    # Shoulder-connected left arm + white hand + clapperboard (tucks behind olive tunic!)
    im = Image.new("RGBA", (440, 340), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    stroke_line(d, [(424, 155), (236, 138)], width=11, seed=325)
    gouache_poly(im, [(36, 114), (236, 114), (236, 268), (36, 268)], fill=CHARCOAL, outline=INK, width=8, seed=326)
    gouache_poly(im, [(32, 62), (234, 24), (242, 68), (40, 106)], fill=OCHRE, outline=INK, width=8, seed=327)
    gouache_ellipse(im, (214, 118, 258, 162), fill=HEAD_WHITE, outline=INK, width=7, seed=328, shade=False)
    save_2x_sprite(im, "s3_clapper_prop.png", meta)

    # =========================================================================
    # SHOT 4 SPRITES: Night Battlefield Illusion
    # =========================================================================
    im = Image.new("RGBA", (1720, 640), (0, 0, 0, 0))
    draw_sherman_tank_2x(im, 420, 465, scale=0.68, rubber_marks=True, label="", seed=401)
    draw_sherman_tank_2x(im, 1040, 468, scale=0.64, rubber_marks=True, label="", seed=402)
    d = ImageDraw.Draw(im)
    stroke_line(d, [(1470, 555), (1530, 110), (1590, 555)], width=10, color=KHAKI, seed=403)
    stroke_line(d, [(1490, 390), (1570, 390)], width=8, color=KHAKI, seed=404)
    stroke_line(d, [(1508, 250), (1552, 250)], width=8, color=KHAKI, seed=405)
    gouache_ellipse(im, (1508, 76, 1552, 120), fill=OCHRE, outline=INK, width=6, seed=406, shade=False)
    save_2x_sprite(im, "s4_dummy_row.png", meta)

    im = Image.new("RGBA", (640, 440), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for r in [84, 148, 212]:
        stroke_arc(d, 320, 330, r, r * 0.75, 200, 340, width=11, color=OCHRE, amp=1.8, seed=410 + r)
    gouache_poly(im, [(120, 18), (520, 16), (524, 100), (116, 102)], fill=CREAM_CARD, outline=INK, width=7, seed=415, shade=False)
    draw_centered_text(d, (120, 18, 520, 100), "RADIO GIẢ", load_font(54), fill=INK)
    save_2x_sprite(im, "s4_radio_rings.png", meta)

    im = Image.new("RGBA", (1240, 840), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    gouache_poly(im, [(110, 490), (630, 490), (630, 650), (110, 650)], fill=OLIVE_DARK, outline=INK, width=10, seed=420)
    gouache_poly(im, [(570, 370), (830, 370), (910, 500), (910, 650), (570, 650)], fill=OLIVE, outline=INK, width=10, seed=421)
    gouache_poly(im, [(640, 398), (804, 398), (864, 490), (640, 490)], fill=KHAKI, outline=INK, width=8, seed=422, shade=False)
    gouache_ellipse(im, (136, 596, 490, 750), fill=CHARCOAL, outline=INK, width=10, seed=423)
    gouache_ellipse(im, (176, 624, 450, 722), fill=KHAKI_DARK, outline=INK, width=7, seed=4231)
    gouache_ellipse(im, (710, 596, 870, 750), fill=CHARCOAL, outline=INK, width=10, seed=424)
    gouache_ellipse(im, (744, 630, 836, 716), fill=KHAKI_DARK, outline=INK, width=7, seed=4241)
    stroke_line(d, [(350, 490), (390, 310)], width=18, color=CHARCOAL, seed=425)
    gouache_poly(im, [(330, 336), (770, 84), (864, 376), (370, 390)], fill=KHAKI, outline=INK, width=10, amp=2.4, seed=426)
    gouache_ellipse(im, (744, 76, 884, 384), fill=TERRACOTTA, outline=INK, width=10, seed=427)
    save_2x_sprite(im, "s4_speaker_truck.png", meta)

    im = Image.new("RGBA", (860, 680), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for idx, r in enumerate([130, 240, 350]):
        col = OCHRE if idx % 2 == 0 else TERRACOTTA
        stroke_arc(d, 90, 370, r, r * 0.88, -48, 42, width=15, color=col, amp=2.2, seed=430 + idx)
    gouache_poly(im, [(170, 36), (820, 32), (826, 184), (166, 188)], fill=CREAM_CARD, outline=INK, width=9, seed=435, shade=False)
    draw_centered_text(d, (170, 34, 822, 186), "VANG 20 KM!", load_font(68), fill=TERRACOTTA)
    save_2x_sprite(im, "s4_sound_waves.png", meta)

    # =========================================================================
    # SHOT 5 SPRITES: Tactical Map Icons
    # =========================================================================
    im = Image.new("RGBA", (920, 520), (0, 0, 0, 0))
    gouache_ellipse(im, (300, 174, 620, 454), fill=(198, 100, 76, 95), outline=TERRACOTTA, width=10, seed=501, shade=False)
    for bx, by in [(240, 300), (460, 360), (660, 286)]:
        gouache_poly(im, [(bx - 56, by - 48), (bx + 56, by - 48), (bx + 44, by + 44), (bx, by + 72), (bx - 44, by + 44)],
                     fill=CHARCOAL, outline=HEAD_WHITE, width=7, seed=502 + bx)
    gouache_poly(im, [(40, 28), (880, 24), (886, 174), (36, 178)], fill=CREAM_CARD, outline=INK, width=9, seed=505, shade=False)
    draw_centered_text(ImageDraw.Draw(im), (42, 26, 880, 176), "CALAIS (MỒI NHỬ)", load_font(64), fill=TERRACOTTA)
    save_2x_sprite(im, "s5_calais_decoy.png", meta)

    im = Image.new("RGBA", (880, 460), (0, 0, 0, 0))
    gouache_ellipse(im, (290, 40, 550, 280), fill=OLIVE, outline=INK, width=10, seed=511)
    draw_star(im, 420, 160, 72, 28, fill=HEAD_WHITE, outline=INK, width=6, seed=5111)
    gouache_poly(im, [(40, 264), (840, 260), (846, 412), (36, 416)], fill=CREAM_CARD, outline=INK, width=9, seed=512, shade=False)
    draw_centered_text(ImageDraw.Draw(im), (42, 262, 840, 414), "BÃI BIỂN NORMANDY", load_font(62), fill=OLIVE_DARK)
    save_2x_sprite(im, "s5_normandy_target.png", meta)

    im = Image.new("RGBA", (720, 440), (0, 0, 0, 0))
    gouache_poly(im, [(190, 64), (330, 56), (430, 370), (310, 384)], fill=SLATE, outline=INK, width=9, seed=521)
    gouache_poly(im, [(64, 190), (590, 176), (636, 224), (590, 256), (70, 248)], fill=CHARCOAL, outline=INK, width=9, seed=522)
    gouache_poly(im, [(56, 130), (136, 130), (156, 236), (56, 236)], fill=TERRACOTTA, outline=INK, width=8, seed=523)
    gouache_ellipse(im, (620, 136, 672, 296), fill=(253, 251, 245, 190), outline=INK, width=6, seed=524, shade=False)
    save_2x_sprite(im, "s5_recon_plane.png", meta)

    # =========================================================================
    # SHOT 6 SPRITES: Grounded Soldier+Pole + Separate Fluttering Flag + Centered Stamp
    # =========================================================================
    im = Image.new("RGBA", (1080, 640), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for ox, oy, sc in [(70, 110, 0.82), (330, 270, 1.0)]:
        s = sc * 2.0
        for hx in [85, 145, 205]:
            gouache_ellipse(im, (ox + (hx - 20) * s, oy + 4 * s, ox + (hx + 20) * s, oy + 42 * s),
                            fill=OLIVE, outline=INK, width=8, seed=610 + hx + ox)
        hull = [
            (ox, oy + 45 * s),
            (ox + 265 * s, oy + 32 * s),
            (ox + 310 * s, oy + 12 * s),
            (ox + 295 * s, oy + 98 * s),
            (ox + 28 * s, oy + 104 * s),
        ]
        gouache_poly(im, hull, fill=SLATE, outline=INK, width=10, seed=601 + ox)
        gouache_poly(im, [(ox + 286 * s, oy + 14 * s), (ox + 324 * s, oy + 4 * s), (ox + 314 * s, oy + 88 * s), (ox + 284 * s, oy + 94 * s)],
                     fill=KHAKI, outline=INK, width=9, seed=605 + ox)
        stroke_line(d, [(ox - 18, oy + 108 * s), (ox + 160 * s, oy + 114 * s), (ox + 318 * s, oy + 98 * s)],
                    width=13, color=HEAD_WHITE, amp=3.0, seed=620 + ox)
    save_2x_sprite(im, "s6_landing_craft.png", meta)

    # Static grounded soldier + wooden flagpole planted firmly on the Normandy bluff!
    im = Image.new("RGBA", (620, 1120), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    stroke_line(d, [(500, 1025), (470, 96)], width=15, color=WOOD, seed=631)
    sx = 300
    draw_stickman_body_2x(im, sx, hip_y=770, shoulder_y=535, tunic_color=OLIVE, leg_spread=72, foot_y=1025, seed=633)
    stroke_line(d, [(sx + 42, 565), (484, 476)], width=11, seed=636)
    stroke_line(d, [(sx - 42, 565), (174, 410)], width=11, seed=637)
    draw_b2_stickman_head(im, sx, 424, r=78, expr="grin", hat="helmet", facing=1, seed=638)
    save_2x_sprite(im, "s6_victory_soldiers.png", meta)

    # Separate animated Allied Invasion Star flag cloth waving from behind the pole!
    im = Image.new("RGBA", (520, 360), (0, 0, 0, 0))
    gouache_poly(im, [(12, 44), (460, 82), (428, 308), (20, 282)], fill=SLATE, outline=INK, width=10, amp=3.0, seed=632)
    gouache_ellipse(im, (152, 92, 326, 264), fill=HEAD_WHITE, outline=INK, width=6, seed=6320, shade=False)
    draw_star(im, 239, 178, 66, 26, fill=OLIVE_DARK, outline=INK, width=5, seed=6321)
    save_2x_sprite(im, "s6_allied_flag.png", meta)

    # Mathematically centered D-Day historical stamp!
    im = Image.new("RGBA", (1240, 340), (0, 0, 0, 0))
    gouache_poly(im, [(36, 40), (1204, 34), (1208, 298), (32, 304)], fill=CREAM_CARD, outline=INK, width=10, amp=2.2, seed=645, shade=False)
    gouache_poly(im, [(60, 64), (1180, 58), (1184, 274), (56, 280)], fill=None, outline=TERRACOTTA, width=5, amp=1.4, seed=646, shade=False)
    draw_centered_text(ImageDraw.Draw(im), (60, 60, 1180, 276), "D-DAY · 06/06/1944", load_font(80), fill=INK)
    save_2x_sprite(im, "s6_dday_stamp.png", meta)


def main():
    meta = {}
    build_backgrounds()
    build_sprites(meta)
    (OUT / "sprites-meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print("Generated grounded B2 assets successfully:")
    for k, v in meta.items():
        print(f"  {k:28s} -> {v['w']}x{v['h']}")


if __name__ == "__main__":
    main()
