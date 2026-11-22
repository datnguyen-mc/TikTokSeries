# Dự án phim: CHỊ ƠI, ĐẾN RỒI — bản 2

*Phim tình cảm hư cấu cho đêm Noel 2026 · 20 cảnh · 260 shot · ~21 phút 42 giây bản thô (cắt đuôi khi dựng còn khoảng 19–20 phút) · 100% thoại trên hình, giọng Bắc, không lời dẫn.*

> Hai năm nay, đêm nào tài xế chuyến xe buýt cuối cũng đọc "bản tin đêm" cho cô y tá ngủ gật ở ghế cuối nghe. Cô chưa ngủ đêm nào. Đêm Noel này tuyến xe bị cắt, sáng hôm sau cô bay đi năm năm, và một ông cụ gục trên ghế đá cổng viện buộc cả hai phải mở mắt.

## Đọc theo thứ tự này

| File | Nội dung |
|---|---|
| `CAU_CHUYEN.md` | Câu chuyện bản 2: bản 1 yếu ở đâu và sửa thế nào, logline, đồng hồ, dàn ý 20 cảnh, gài – trả |
| `KICH_BAN_CHI_TIET.md` | **Kịch bản phân cảnh**: từng shot có cỡ cảnh, hành động, thoại, sắc thái; mỗi cảnh có mục đích, cảm xúc, nhạc, chuyển cảnh |
| `NHAN_VAT_GOC.md` | Hồ sơ nhân vật: tiểu sử, muốn – cần – sợ – bí mật, cử chỉ, cách nói, tủ đồ, hành trình, quy tắc quay, bảng xưng hô, giọng lồng tiếng |
| `DAO_DIEN.md` | Sổ tay đạo diễn & quay phim: ba quy tắc vàng, ống kính, trục nhìn, màu theo cảnh, âm thanh, lịch nhạc, motif, khớp hình, dựng, mẹo Flow, prompt ảnh bối cảnh mẫu |
| `TRAILER_SHORTS.md` | Teaser 15s, trailer 75s theo mã shot, 20 short + short một câu, lịch đăng, caption, hashtag, ảnh bìa, mô tả YouTube |
| `NHAN_VAT_FLOW.md` | 19 nhân vật theo bộ đồ cần tạo trên Flow, prompt đầy đủ / prompt sửa |
| `SHOTS.md` | Bảng shot cho người render: số giây, nhân vật cần đính, thoại |
| `kich-ban/canh-XX.md` | Kịch bản chi tiết + bảng shot từng cảnh |
| `film/cNN/NN-SS.txt` | Prompt dán nguyên văn vào Flow |
| `film/shots.json` | Danh sách shot cho công cụ |
| `_tools/data.py` | **Nguồn duy nhất** của mọi file sinh tự động. Sửa ở đây |
| `_tools/build.py` | `python3 _tools/build.py` sinh lại toàn bộ (tự kiểm lỗi: mã bộ đồ, người nói không có trong khung, thiếu mô tả tiếng Việt, thoại quá 15 giây) |
| `_tools/collect.sh` | Gom clip `CODR_<shot>_*.mp4` từ Downloads vào `film/clips/<shot>.mp4`, so thời lượng |
| `revisions/ban1/` | Bản 1 (câu chuyện, dữ liệu, kịch bản và prompt cũ) |

## Cách làm trên Flow

1. Tạo 4 ảnh bối cảnh mẫu theo `DAO_DIEN.md` mục 10 (xe buýt, cổng viện, bến xe, đầu ngõ), lưu vào `character_refs/`.
2. Tạo 7 nhân vật gốc (★ trong `NHAN_VAT_FLOW.md`): Hưng, An, Ông Thư, Bà Nguyệt trẻ, Anh Tú, Bà Lụa, Thảo.
3. Tạo 12 bộ còn lại bằng *Prompt sửa* từ ảnh ở cột *Gốc từ*. Ông Thư trẻ và Bà Nguyệt già tạo từ ảnh gốc của chính người đó.
4. Render từng shot: Omni 1.2 Flash, 16:9, 720p (nháp 360p), đúng số giây, đính đúng nhân vật (+ ảnh bối cảnh nếu cần), dán nguyên file prompt. Tên video `<shot> · <tên>`.
5. Tải về đặt tên `CODR_<shot>_....mp4`, chạy `_tools/collect.sh`. Kiểm từng shot theo danh sách cuối `DAO_DIEN.md`.
6. Ưu tiên render cảnh 01, 02, 03, 05, 10, 14 trước để kịp teaser (09/12) và trailer (12/12).

**Ước tính:** 1.302 giây cần tạo ≈ 5.200 credit ở mức 4 credit/giây (15 giây = 60 credit như dự án trước). Giá credit Google đổi thường xuyên, kiểm tra trong Settings của Flow.
