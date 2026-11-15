# 🎬 Chuyến Tàu Lúc 0 Giờ — Tập 1 (30s Motion Comic • 0 Đồng)

Dự án mẫu sản xuất tự động 100% trên máy Mac với chi phí **0 đồng**:
- **Hình ảnh:** 6 khung hình dọc `9:16` phong cách Dark Korean Webtoon đồng nhất nhân vật (`assets/images/scene_01.jpg` – `scene_06.jpg`).
- **Lồng tiếng & Âm thanh (`generate_audio.py`):**
  - 2 giọng đọc tiếng Việt tự nhiên (`vi-VN-NamMinhNeural` cho Hoàng & `vi-VN-HoaiMyNeural` qua bộ lọc điện đài ma mị cho tin nhắn lạ).
  - Đồng bộ thời gian từng chữ (`WordBoundary`) để làm phụ đề Karaoke nhảy chữ chuẩn TikTok.
  - Tự động tổng hợp nhạc nền Dark Minor Synth Drone + hiệu ứng Foley/SFX (tiếng phanh tàu, bánh sắt đường ray, rung điện thoại, chuông cảnh báo, tiếng tim đập dồn dập, violin riser, VHS glitch & Sub-bass `BRAAAM`).
- **Dựng phim & Chuyển động (`render_episode.py`):**
  - Chuyển động camera mượt dưới mức điểm ảnh (Zoom-in/out, lia máy, nghiêng góc Dutch-angle, lắc lư theo nhịp tàu, rung chấn bất ngờ).
  - Lớp phủ hiệu ứng (đèn huỳnh quang chớp tắt, hạt bụi/sương trôi, nhịp đèn đỏ cấp cứu, tách kênh màu RGB Chromatic Aberration, nhiễu băng từ VHS Glitch).
  - HUD đồ họa chuyển động (đồng hồ ga ngầm `00:00`, thông báo tin nhắn khẩn mất sóng, thẻ kết tập `CÒN TIẾP`).

## ▶️ Chạy lại toàn bộ quy trình (Re-render)

```bash
cd /Users/iseul-a/Documents/TikTokSeries/chuyen-tau-luc-0-gio
./.venv/bin/python generate_audio.py
./.venv/bin/python render_episode.py
```

File xuất cuối cùng nằm tại: `output/chuyen_tau_luc_0_gio_tap_01.mp4` (`1080x1920`, `30fps`, `30.0s`).
