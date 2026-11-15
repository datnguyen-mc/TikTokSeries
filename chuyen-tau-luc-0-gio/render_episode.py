#!/usr/bin/env python3
"""
100% Local Motion Comic / Animatic Renderer for TikTok (1080x1920 @ 30fps).
Features:
- Sub-pixel smooth OpenCV affine camera rig (push-in, pull-out, Dutch tilt, train sway, shock shake)
- Scene-specific horror VFX (fluorescent flicker, drifting dust/mist, red heartbeat pulse,
  RGB chromatic aberration, VHS scanline glitch tear, whip-flash transitions)
- Motion Graphics HUD (station clock typewriter, no-signal phone alert popup, cliffhanger end card)
- Word-by-word dynamic TikTok subtitles with Vietnamese diacritics & keyword emphasis
- Direct rawvideo pipe to FFmpeg H.264 + AAC 192kbps master output
"""

import json
import math
import subprocess
from pathlib import Path
from typing import Any

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "assets" / "images"
AUDIO_DIR = BASE_DIR / "assets" / "audio"
OUT_DIR = BASE_DIR / "output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1920
FPS = 30

FONT_BOLD_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_HUD_PATH = "/System/Library/Fonts/Supplemental/Tahoma Bold.ttf"


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", size)


FONT_SUB = load_font(FONT_BOLD_PATH, 56)
FONT_SUB_ACTIVE = load_font(FONT_BOLD_PATH, 61)
FONT_SPEAKER = load_font(FONT_HUD_PATH, 28)
FONT_HUD_SM = load_font(FONT_HUD_PATH, 28)
FONT_HUD_LG = load_font(FONT_BOLD_PATH, 46)
FONT_ALERT_TITLE = load_font(FONT_HUD_PATH, 29)
FONT_ALERT_BODY = load_font(FONT_BOLD_PATH, 34)
FONT_END_BIG = load_font(FONT_BOLD_PATH, 70)
FONT_END_SUB = load_font(FONT_HUD_PATH, 34)


def ease_out_cubic(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return 1.0 - (1.0 - x) ** 3


def ease_in_out_sine(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return -(math.cos(math.pi * x) - 1.0) / 2.0


def prep_scene_image(path: Path) -> np.ndarray:
    """Load RGB image and resize-cover to 1080x1920 cleanly."""
    bgr = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if bgr is None:
        raise FileNotFoundError(f"Missing image: {path}")
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    ih, iw = rgb.shape[:2]
    scale = max(W / iw, H / ih)
    nw, nh = int(round(iw * scale)), int(round(ih * scale))
    resized = cv2.resize(rgb, (nw, nh), interpolation=cv2.INTER_LANCZOS4)
    x0 = (nw - W) // 2
    y0 = (nh - H) // 2
    return resized[y0 : y0 + H, x0 : x0 + W].copy()


def transform_camera(
    img: np.ndarray,
    scale: float,
    tx: float = 0.0,
    ty: float = 0.0,
    angle_deg: float = 0.0,
) -> np.ndarray:
    """Sub-pixel smooth camera zoom/pan/rotation around center + target offset."""
    cx, cy = W / 2.0, H / 2.0
    mat = cv2.getRotationMatrix2D((cx, cy), angle_deg, scale)
    mat[0, 2] += tx
    mat[1, 2] += ty
    return cv2.warpAffine(
        img,
        mat,
        (W, H),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REFLECT_101,
    )


def apply_chromatic_aberration(frame: np.ndarray, shift_px: int) -> np.ndarray:
    if shift_px <= 0:
        return frame
    out = frame.copy()
    out[:, shift_px:, 0] = frame[:, :-shift_px, 0]  # Red right
    out[:, :-shift_px, 2] = frame[:, shift_px:, 2]  # Blue left
    return out


def apply_vhs_glitch(frame: np.ndarray, intensity: float, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    out = apply_chromatic_aberration(frame, int(6 + 16 * intensity))
    num_slices = int(5 + 12 * intensity)
    for _ in range(num_slices):
        y0 = int(rng.integers(0, H - 40))
        bh = int(rng.integers(8, int(28 + 55 * intensity)))
        shift = int(rng.integers(-int(65 * intensity + 10), int(65 * intensity + 11)))
        out[y0 : y0 + bh] = np.roll(out[y0 : y0 + bh], shift, axis=1)
    # Scanlines
    out[::4] = (out[::4].astype(np.float32) * 0.76).astype(np.uint8)
    return out


def build_vignette_mask() -> np.ndarray:
    y = np.linspace(-1.0, 1.0, H, dtype=np.float32)[:, None]
    x = np.linspace(-1.0, 1.0, W, dtype=np.float32)[None, :]
    r2 = (x * 0.92) ** 2 + (y * 0.82) ** 2
    vig = np.clip(1.0 - 0.52 * (r2**1.25), 0.32, 1.0)
    # Darken bottom area slightly so subtitles always pop cleanly
    bottom_grad = np.clip((np.arange(H, dtype=np.float32) - H * 0.62) / (H * 0.38), 0.0, 1.0)[:, None]
    vig = vig * (1.0 - 0.34 * bottom_grad)
    return vig[:, :, None]


VIGNETTE = build_vignette_mask()

# Pre-generate drifting atmospheric particles (x0, y0, speed_x, speed_y, radius, alpha)
RNG_PARTICLES = np.random.default_rng(108)
PARTICLES = [
    (
        float(RNG_PARTICLES.uniform(0, W)),
        float(RNG_PARTICLES.uniform(0, H)),
        float(RNG_PARTICLES.uniform(-22, 22)),
        float(RNG_PARTICLES.uniform(-55, -18)),
        int(RNG_PARTICLES.integers(2, 5)),
        float(RNG_PARTICLES.uniform(0.16, 0.45)),
    )
    for _ in range(55)
]


def draw_particles(frame: np.ndarray, t: float, color: tuple[int, int, int]) -> None:
    overlay = frame.copy()
    for x0, y0, vx, vy, rad, alpha in PARTICLES:
        px = int((x0 + vx * t) % W)
        py = int((y0 + vy * t) % H)
        cv2.circle(overlay, (px, py), rad, color, -1, lineType=cv2.LINE_AA)
    cv2.addWeighted(overlay, 0.28, frame, 0.72, 0, dst=frame)


def render_scene_frame(
    scene_idx: int,
    base_img: np.ndarray,
    t_global: float,
    t_local: float,
    dur: float,
    frame_idx: int,
) -> np.ndarray:
    """Apply scene-specific camera choreography + lighting & atmospheric VFX."""
    u = max(0.0, min(1.0, t_local / max(dur, 0.01)))
    rng = np.random.default_rng(frame_idx * 977 + 13)

    # Handheld micro-breathing
    breath_x = math.sin(t_global * 1.9) * 5.5
    breath_y = math.cos(t_global * 1.4) * 4.5
    chroma = 0

    if scene_idx == 1:
        # Dramatic pull-back from oncoming midnight train + fluorescent flicker
        scale = 1.21 - 0.15 * ease_out_cubic(u)
        tx = -18.0 + 30.0 * ease_in_out_sine(u) + breath_x
        ty = 14.0 - 20.0 * u + breath_y
        angle = -0.8 + 0.8 * u
        if t_local < 0.25:
            amp = (0.25 - t_local) / 0.25
            tx += float(rng.uniform(-18, 18)) * amp
            ty += float(rng.uniform(-18, 18)) * amp
            chroma = int(8 * amp)
        frame = transform_camera(base_img, scale, tx, ty, angle)
        draw_particles(frame, t_global, (165, 240, 255))
        # Fluorescent tube sputter flicker
        if (0.14 < t_local < 0.21) or (0.27 < t_local < 0.31) or (2.05 < t_local < 2.12):
            frame = (frame.astype(np.float32) * 0.52).astype(np.uint8)
            chroma = max(chroma, 5)

    elif scene_idx == 2:
        # Slow creeping push-in down empty subway aisle + gentle rail sway
        scale = 1.04 + 0.15 * ease_in_out_sine(u)
        sway_x = math.sin(t_global * 2.8) * 10.0
        sway_ang = math.sin(t_global * 2.8) * 0.85
        frame = transform_camera(base_img, scale, sway_x + breath_x, -12.0 * u + breath_y, sway_ang)
        draw_particles(frame, t_global * 0.8, (150, 235, 225))

    elif scene_idx == 3:
        # Fast snap-zoom onto shocked face + twin phone-vibration screen shakes
        snap = ease_out_cubic(min(1.0, t_local / 0.45))
        scale = 1.04 + 0.11 * snap + 0.05 * u
        tx, ty = breath_x, 12.0 * snap + breath_y
        if (0.04 <= t_local <= 0.26) or (0.31 <= t_local <= 0.53):
            tx += math.sin(t_local * 170.0) * 11.0
            ty += math.cos(t_local * 145.0) * 6.0
            chroma = 5
        frame = transform_camera(base_img, scale, tx, ty, 0.0)
        # Subtle blue phone screen glow pulse on face
        pulse = 0.5 + 0.5 * math.sin(t_local * 5.5)
        tint = np.zeros_like(frame)
        tint[:, :, 1] = 18
        tint[:, :, 2] = 38
        frame = cv2.addWeighted(frame, 1.0, tint, 0.15 * pulse, 0)

    elif scene_idx == 4:
        # Eerie Dutch-angle tilt on crimson subway + accelerating heartbeat red pulse
        scale = 1.06 + 0.14 * u
        angle = -2.3 + 4.0 * ease_in_out_sine(u)
        tx = 16.0 - 32.0 * u + breath_x
        frame = transform_camera(base_img, scale, tx, breath_y, angle)
        draw_particles(frame, t_global * 1.1, (255, 190, 195))
        # Heartbeat crimson pulse
        hb = max(0.0, math.sin(t_local * 8.2)) ** 4
        red_overlay = np.zeros_like(frame)
        red_overlay[:, :, 0] = 165
        frame = cv2.addWeighted(frame, 1.0, red_overlay, 0.22 * hb, 0)
        chroma = int(3 + 5 * hb)

    elif scene_idx == 5:
        # Claustrophobic push-in toward trembling eyes + rising dread tremor & RGB split
        scale = 1.05 + 0.20 * (u**1.25)
        tremor = (u**2) * 7.5
        tx = -22.0 * u + float(rng.uniform(-tremor, tremor))
        ty = 26.0 * u + float(rng.uniform(-tremor, tremor))
        frame = transform_camera(base_img, scale, tx, ty, 1.4 * u)
        chroma = int(2 + 9 * (u**1.8))

    else:
        # Scene 6: Base scale >= 1.24 crops letterbox bars cleanly & zooms straight into the smiling reflection!
        scale = 1.24 + 0.15 * ease_in_out_sine(u)
        tx = -10.0 * u + breath_x * 0.5
        ty = 18.0 * u + breath_y * 0.5
        # Twist sting around halfway through Scene 6
        if t_local > 1.75:
            sting_u = min(1.0, (t_local - 1.75) / 0.35)
            if t_local < 2.15:
                shk = (1.0 - sting_u) * 16.0
                tx += float(rng.uniform(-shk, shk))
                ty += float(rng.uniform(-shk, shk))
            chroma = int(4 + 6 * math.sin(t_local * 9.0) ** 2)
        frame = transform_camera(base_img, scale, tx, ty, 0.0)
        if t_local > 1.75:
            red_rim = np.zeros_like(frame)
            red_rim[:, :, 0] = 140
            frame = cv2.addWeighted(frame, 1.0, red_rim, 0.14, 0)

    if chroma > 0:
        frame = apply_chromatic_aberration(frame, chroma)

    # Whip-flash / glitch transition on first 4 frames of scenes 2..6
    if scene_idx > 1 and t_local < 0.13:
        tr = 1.0 - (t_local / 0.13)
        frame = apply_chromatic_aberration(frame, int(14 * tr))
        flash = 1.0 + 0.38 * tr
        frame = np.clip(frame.astype(np.float32) * flash, 0, 255).astype(np.uint8)

    # Final 0.95s VHS glitch tear at the end of Scene 6
    if scene_idx == 6 and (dur - t_local) < 0.95:
        gl_amt = 1.0 - max(0.0, (dur - t_local) / 0.95)
        if gl_amt > 0.15:
            frame = apply_vhs_glitch(frame, min(1.0, gl_amt * 0.9), frame_idx)

    # Cinematic vignette + subtle 3-frame stepped film grain (keeps H.264 file size compact & crisp)
    grain_rng = np.random.default_rng((frame_idx // 3) * 131 + 7)
    grain = grain_rng.integers(-3, 4, size=(H, W, 1), dtype=np.int16)
    shaded = frame.astype(np.float32) * VIGNETTE + grain
    return np.clip(shaded, 0, 255).astype(np.uint8)


def draw_warning_triangle(
    draw: ImageDraw.ImageDraw,
    cx: int,
    cy: int,
    size: int,
    color: tuple[int, int, int, int],
) -> None:
    pts = [(cx, cy - size), (cx - size, cy + size - 2), (cx + size, cy + size - 2)]
    draw.polygon(pts, outline=color, width=3)
    draw.line([(cx, cy - size + 8), (cx, cy + 2)], fill=color, width=3)
    draw.ellipse((cx - 2, cy + 6, cx + 2, cy + 10), fill=color)


def draw_rounded_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    radius: int,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int] | None = None,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_hud_overlays(
    pil_img: Image.Image,
    scene_idx: int,
    t_global: float,
    t_local: float,
    dur: float,
) -> None:
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Top-right subtle series watermark badge (TikTok safe zone y=96)
    badge_txt = "CHUYẾN TÀU 00:00"
    bt_box = draw.textbbox((0, 0), badge_txt, font=FONT_HUD_SM)
    bt_w = bt_box[2] - bt_box[0]
    box_r = W - 44
    box_l = box_r - bt_w - 64
    draw_rounded_box(
        draw,
        (box_l, 96, box_r, 150),
        radius=14,
        fill=(8, 12, 18, 168),
        outline=(255, 58, 76, 155),
        width=2,
    )
    rec_on = (int(t_global * 2.5) % 2) == 0
    if rec_on:
        draw.ellipse((box_l + 18, 114, box_l + 36, 132), fill=(255, 45, 65, 245))
    draw.text((box_l + 46, 107), badge_txt, font=FONT_HUD_SM, fill=(235, 242, 250, 235))

    # Scene 1: Typewriter Location & Midnight Digital Clock HUD
    if scene_idx == 1 and t_local > 0.08:
        loc_full = "GA NGẦM SỐ 7 • TUYẾN CUỐI"
        chars = min(len(loc_full), max(1, int((t_local - 0.08) * 28)))
        loc_txt = loc_full[:chars]
        alpha = int(235 * min(1.0, (dur - t_local) / 0.35))
        if alpha > 20:
            draw_rounded_box(
                draw,
                (54, 168, 560, 304),
                radius=18,
                fill=(6, 12, 20, int(alpha * 0.76)),
                outline=(70, 225, 245, int(alpha * 0.7)),
                width=2,
            )
            draw.text((78, 184), loc_txt, font=FONT_HUD_SM, fill=(115, 240, 255, alpha))
            sec_num = min(4, int(t_local))
            draw.text(
                (78, 224),
                f"00 : 00 : 0{sec_num}",
                font=FONT_HUD_LG,
                fill=(255, 62, 78, alpha),
            )

    # Scene 2: Car #4 tag
    elif scene_idx == 2 and t_local < dur - 0.25:
        alpha = int(220 * min(1.0, t_local / 0.3))
        draw_rounded_box(
            draw,
            (54, 96, 290, 148),
            radius=14,
            fill=(8, 18, 22, int(alpha * 0.78)),
            outline=(90, 230, 220, int(alpha * 0.65)),
            width=2,
        )
        draw.text((76, 106), "TOA SỐ 04", font=FONT_HUD_SM, fill=(140, 245, 235, alpha))

    # Scene 3: Pop-in Mysterious Lockscreen Notification Banner
    elif scene_idx == 3 and t_local > 0.14:
        pop = ease_out_cubic(min(1.0, (t_local - 0.14) / 0.32))
        y_top = int(175 + (1.0 - pop) * -60)
        alpha = int(242 * pop * min(1.0, (dur - t_local) / 0.25))
        if alpha > 20:
            draw_rounded_box(
                draw,
                (64, y_top, W - 64, y_top + 154),
                radius=26,
                fill=(12, 16, 28, int(alpha * 0.88)),
                outline=(255, 68, 88, alpha),
                width=3,
            )
            draw_warning_triangle(draw, 108, y_top + 40, 14, (255, 95, 110, alpha))
            draw.text(
                (134, y_top + 22),
                "MẤT SÓNG  •  TIN NHẮN KHẨN (00:01)",
                font=FONT_ALERT_TITLE,
                fill=(255, 95, 110, alpha),
            )
            draw.text(
                (98, y_top + 74),
                "Người gửi: SỐ KHÔNG XÁC ĐỊNH",
                font=FONT_ALERT_BODY,
                fill=(240, 248, 255, alpha),
            )

    # Scene 6 Final 0.90s: Cliffhanger End-Card Stamp
    elif scene_idx == 6 and (dur - t_local) < 0.92:
        ep_u = ease_out_cubic(min(1.0, (0.92 - (dur - t_local)) / 0.28))
        alpha = int(248 * ep_u)
        draw_rounded_box(
            draw,
            (110, 210, W - 110, 405),
            radius=24,
            fill=(8, 6, 12, int(alpha * 0.86)),
            outline=(255, 46, 76, alpha),
            width=4,
        )
        b1 = draw.textbbox((0, 0), "CÒN TIẾP...", font=FONT_END_BIG)
        tw1 = b1[2] - b1[0]
        draw.text(((W - tw1) // 2, 232), "CÒN TIẾP...", font=FONT_END_BIG, fill=(255, 52, 78, alpha))

        sub_ep = "TẬP 2: QUY TẮC KHI ĐÈN TẮT"
        b2 = draw.textbbox((0, 0), sub_ep, font=FONT_END_SUB)
        tw2 = b2[2] - b2[0]
        draw.text(((W - tw2) // 2, 330), sub_ep, font=FONT_END_SUB, fill=(235, 240, 250, alpha))

    pil_img.alpha_composite(overlay)


def draw_subtitle_chunk(
    pil_img: Image.Image,
    sub_chunk: dict[str, Any],
    t_global: float,
) -> None:
    """Render crisp Vietnamese TikTok subtitles with active-word highlight & stroke."""
    words = sub_chunk["words"]
    speaker = sub_chunk["speaker"]
    is_mystery = speaker != "Hoàng"

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Wrap words into at most 2 balanced lines (max width ~ 880px)
    max_line_w = 880
    lines: list[list[dict[str, Any]]] = []
    cur_line: list[dict[str, Any]] = []
    cur_w = 0

    space_w = draw.textlength(" ", font=FONT_SUB)
    for w in words:
        ww = draw.textlength(w["text"], font=FONT_SUB_ACTIVE)
        if cur_line and (cur_w + space_w + ww > max_line_w):
            lines.append(cur_line)
            cur_line = [w]
            cur_w = ww
        else:
            cur_line.append(w)
            cur_w += (space_w + ww) if len(cur_line) > 1 else ww
    if cur_line:
        lines.append(cur_line)

    # Pop-in animation at start of chunk
    chunk_age = max(0.0, t_global - sub_chunk["start"])
    pop = ease_out_cubic(min(1.0, chunk_age / 0.12))

    line_h = 74
    total_h = len(lines) * line_h
    base_y = int(1465 - total_h // 2 + (1.0 - pop) * 14)

    # Measure widest line (including speaker header if shown) so pill never clips header text
    widest = 0.0
    for ln in lines:
        lw = sum(draw.textlength(w["text"], font=FONT_SUB) for w in ln) + space_w * max(0, len(ln) - 1)
        widest = max(widest, lw)
    if is_mystery:
        tag_w = draw.textlength("TIN NHẮN TỪ SỐ LẠ", font=FONT_SPEAKER) + 46
        widest = max(widest, tag_w)

    pad_x, pad_y = 38, 24
    pill_top = base_y - pad_y - (38 if is_mystery else 0)
    pill_bot = base_y + total_h + pad_y - 6
    pill_left = int((W - widest) // 2 - pad_x)
    pill_right = int((W + widest) // 2 + pad_x)

    border_col = (255, 62, 88, 215) if is_mystery else (80, 220, 245, 130)
    draw_rounded_box(
        draw,
        (max(36, pill_left), pill_top, min(W - 36, pill_right), pill_bot),
        radius=24,
        fill=(6, 9, 16, 188),
        outline=border_col,
        width=3 if is_mystery else 2,
    )

    if is_mystery:
        tag = "TIN NHẮN TỪ SỐ LẠ"
        tb = draw.textbbox((0, 0), tag, font=FONT_SPEAKER)
        tw = tb[2] - tb[0]
        tx0 = (W - tw) // 2 + 16
        draw_warning_triangle(draw, tx0 - 24, pill_top + 28, 12, (255, 92, 112, 245))
        draw.text((tx0, pill_top + 13), tag, font=FONT_SPEAKER, fill=(255, 92, 112, 245))

    # Draw each word with thick black stroke + active karaoke color
    for li, ln in enumerate(lines):
        line_str_widths = []
        fonts_used = []
        colors_used = []
        for w in ln:
            is_active = w["start"] - 0.03 <= t_global <= w["end"] + 0.06
            already_spoken = t_global > w["end"] + 0.06
            fnt = FONT_SUB_ACTIVE if is_active else FONT_SUB

            if is_active:
                if w["highlight"] or is_mystery:
                    col = (255, 64, 88, 255) if is_mystery else (255, 218, 36, 255)
                else:
                    col = (105, 242, 255, 255)
            elif w["highlight"] and already_spoken:
                col = (255, 120, 132, 255) if is_mystery else (255, 230, 120, 255)
            elif already_spoken:
                col = (255, 255, 255, 255)
            else:
                col = (212, 220, 232, 238)

            line_str_widths.append(draw.textlength(w["text"], font=fnt))
            fonts_used.append(fnt)
            colors_used.append(col)

        tot_lw = sum(line_str_widths) + space_w * max(0, len(ln) - 1)
        cur_x = (W - tot_lw) / 2.0
        cur_y = base_y + li * line_h

        for w, ww, fnt, col in zip(ln, line_str_widths, fonts_used, colors_used):
            y_adj = -3 if fnt is FONT_SUB_ACTIVE else 0
            # Soft drop shadow + crisp stroke
            draw.text(
                (cur_x + 3, cur_y + y_adj + 4),
                w["text"],
                font=fnt,
                fill=(0, 0, 0, 210),
                stroke_width=6,
                stroke_fill=(0, 0, 0, 210),
            )
            draw.text(
                (cur_x, cur_y + y_adj),
                w["text"],
                font=fnt,
                fill=col,
                stroke_width=6,
                stroke_fill=(8, 10, 15, 255),
            )
            cur_x += ww + space_w

    pil_img.alpha_composite(overlay)


def refine_subtitle_chunks(raw_chunks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Split chunks cleanly on new sentences & merge any 1-word orphan onto the adjacent phrase."""
    split_list: list[dict[str, Any]] = []
    for ch in raw_chunks:
        words = ch["words"]
        sub_group: list[dict[str, Any]] = []
        for idx, w in enumerate(words):
            starts_new_sent = idx > 0 and len(w["text"]) > 0 and w["text"][0].isupper()
            if starts_new_sent and sub_group:
                split_list.append(
                    {
                        "speaker": ch["speaker"],
                        "start": sub_group[0]["start"],
                        "end": w["start"],
                        "words": sub_group,
                    }
                )
                sub_group = [w]
            else:
                sub_group.append(w)
        if sub_group:
            split_list.append(
                {
                    "speaker": ch["speaker"],
                    "start": sub_group[0]["start"],
                    "end": max(ch["end"], sub_group[-1]["end"] + 0.08),
                    "words": sub_group,
                }
            )

    merged: list[dict[str, Any]] = []
    for ch in split_list:
        if (
            len(ch["words"]) == 1
            and merged
            and merged[-1]["speaker"] == ch["speaker"]
            and (ch["start"] - merged[-1]["end"]) < 0.25
            and len(merged[-1]["words"]) <= 4
        ):
            merged[-1]["words"].extend(ch["words"])
            merged[-1]["end"] = ch["end"]
        else:
            merged.append(ch)
    return merged


def main() -> None:
    timeline = json.loads((AUDIO_DIR / "timeline.json").read_text(encoding="utf-8"))
    audio_path = AUDIO_DIR / "master_mix.wav"
    out_mp4 = OUT_DIR / "chuyen_tau_luc_0_gio_tap_01.mp4"

    scenes = timeline["scenes"]
    subtitles = refine_subtitle_chunks(timeline["subtitles"])
    total_dur = float(timeline["duration"])
    total_frames = int(round(total_dur * FPS))

    # Preload & cover-fit all 6 high-res scenes
    scene_imgs: dict[int, np.ndarray] = {}
    for s in scenes:
        idx = s["index"]
        img_file = IMG_DIR / f"scene_{idx:02d}.jpg"
        if not img_file.exists():
            img_file = IMG_DIR / f"scene_{idx:02d}.png"
        scene_imgs[idx] = prep_scene_image(img_file)

    cmd = [
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-f",
        "rawvideo",
        "-vcodec",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "-",
        "-i",
        str(audio_path),
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "20",
        "-maxrate",
        "10M",
        "-bufsize",
        "20M",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
        "-shortest",
        str(out_mp4),
    ]

    print(f"Rendering {total_frames} frames ({total_dur:.2f}s @ {FPS}fps, {W}x{H})...")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None

    for f_idx in range(total_frames):
        t = f_idx / FPS

        # Locate active scene
        active_scene = scenes[-1]
        for s in scenes:
            if s["start"] <= t < s["end"]:
                active_scene = s
                break

        s_idx = active_scene["index"]
        t_local = max(0.0, t - active_scene["start"])
        s_dur = active_scene["duration"]

        rgb_np = render_scene_frame(s_idx, scene_imgs[s_idx], t, t_local, s_dur, f_idx)
        pil_frame = Image.fromarray(rgb_np, mode="RGB").convert("RGBA")

        draw_hud_overlays(pil_frame, s_idx, t, t_local, s_dur)

        # Find active subtitle chunk
        for sub in subtitles:
            if sub["start"] <= t <= sub["end"]:
                draw_subtitle_chunk(pil_frame, sub, t)
                break

        # Fade in first 0.25s and fade to black last 0.20s
        out_rgb = np.asarray(pil_frame.convert("RGB"))
        if t < 0.25:
            out_rgb = (out_rgb.astype(np.float32) * (t / 0.25)).astype(np.uint8)
        elif (total_dur - t) < 0.20:
            out_rgb = (out_rgb.astype(np.float32) * max(0.0, (total_dur - t) / 0.20)).astype(np.uint8)

        proc.stdin.write(out_rgb.tobytes())
        if (f_idx + 1) % 150 == 0 or f_idx == total_frames - 1:
            print(f"  Frame {f_idx + 1}/{total_frames} ({(f_idx + 1) / FPS:.1f}s)")

    proc.stdin.close()
    rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"FFmpeg exited with code {rc}")
    print(f"DONE -> {out_mp4}")


if __name__ == "__main__":
    main()
