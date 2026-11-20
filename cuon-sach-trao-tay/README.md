# Dự án phim: CUỐN SÁCH TRAO TAY

- `KICH-BAN-TONG.md` — kịch bản tổng 25 phút: ghi chú, nhân vật, 14 cảnh / 96 clip, bảng trang phục, lời dẫn.
- `canh-XX/README.md` — bảng clip từng cảnh, cột "Cách tạo trên Flow" (Ingredients | Frames | Text).
- `canh-01/clip-1..4.md` — prompt Flow đầy đủ cho cảnh mở đầu (dán nguyên văn vào Flow).
- Google Flow project: https://flow.google.com/project/d279def1-0b48-44bb-ba95-5412f50d42bb
- `character_refs/` — đặt ảnh tham chiếu `KhangMid.png`, `KhangYoung.png`, ... (tạo bằng Flow, xem mô tả trong KICH-BAN-TONG.md mục 2).
- `exported_frames/`, `output_videos/` — skill Google Flow tự dùng.

Cách đã chạy trên Flow: tạo nhân vật trong mục Nhân vật → nhờ tác nhân Flow tạo video bằng generate_video_with_references (Omni 1.2 Flash, 15s, 16:9, 720p, 60 credit/clip). Flow chặn mọi video có trẻ em người thật, nên mọi nhân vật trong phim đều từ 18 tuổi trở lên.
