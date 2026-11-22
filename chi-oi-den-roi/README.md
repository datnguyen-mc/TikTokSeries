# Dự án phim: CHỊ ƠI, ĐẾN RỒI — bản 3

*Phim tình cảm hư cấu cho đêm Noel 2026 · 20 cảnh · 254 shot · ~21 phút 47 giây bản thô (dựng xong khoảng 18–20 phút) · 100% thoại trên hình, giọng Bắc, không lời dẫn.*

**Tagline:** *Mai rét, nhớ mặc thêm áo.*

> Hai năm nay, đêm nào tài xế chuyến xe buýt cuối cũng đọc "bản tin đêm" cho cô y tá ngủ gật ở ghế cuối nghe, và dặn cô mặc thêm áo. Cô chưa ngủ đêm nào. Đêm Noel này tuyến xe của bố anh bị cắt, sáng hôm sau cô bay đi năm năm, và một câu dặn đã chờ hai mươi năm cuối cùng có người trả lời.

## Đọc theo thứ tự này

| File | Nội dung |
|---|---|
| `CAU_CHUYEN.md` | Câu chuyện bản 3: bản 2 còn thiếu gì, vì sao phim sẽ lan, một con đường ba thế hệ, dàn ý 20 cảnh, gài – trả |
| `KICH_BAN_CHI_TIET.md` | **Kịch bản phân cảnh**: từng shot có cỡ cảnh, hành động, thoại, sắc thái; mỗi cảnh có mục đích, cảm xúc, nhạc, chuyển cảnh |
| `NHAN_VAT_GOC.md` | Hồ sơ nhân vật (thêm bố Đông): tiểu sử, muốn – cần – sợ – bí mật, cử chỉ, cách nói, tủ đồ, hành trình, quy tắc quay, xưng hô, giọng lồng tiếng |
| `DAO_DIEN.md` | Sổ tay đạo diễn & quay phim: bốn quy tắc vàng, ống kính, màu theo cảnh, âm thanh, lịch nhạc, motif, khớp hình, dựng, mẹo Flow, prompt 5 ảnh bối cảnh mẫu |
| `TRAILER_SHORTS.md` | Teaser, trailer 80s, chiến dịch "Mai rét, nhớ mặc thêm áo", 20 short + short một câu, lịch đăng, caption, ảnh bìa, YouTube |
| `NHAN_VAT_FLOW.md` | 20 nhân vật theo bộ đồ cần tạo trên Flow, prompt đầy đủ / prompt sửa |
| `SHOTS.md` | Bảng shot cho người render |
| `kich-ban/canh-XX.md` | Kịch bản chi tiết + bảng shot từng cảnh |
| `film/cNN/NN-SS.txt` | Prompt dán nguyên văn vào Flow |
| `film/shots.json` | Danh sách shot cho công cụ |
| `_tools/data.py` | **Nguồn duy nhất** của mọi file sinh tự động. Sửa ở đây |
| `_tools/build.py` | `python3 _tools/build.py` sinh lại toàn bộ và tự kiểm lỗi |
| `_tools/collect.sh` | Gom clip `CODR_<shot>_*.mp4` từ Downloads vào `film/clips/`, so thời lượng |
| `revisions/ban1/`, `revisions/ban2/` | Các bản trước |

## Cách làm trên Flow

1. Tạo 5 ảnh bối cảnh mẫu theo `DAO_DIEN.md` mục 10, lưu vào `character_refs/`.
2. Tạo 7 nhân vật gốc (★ trong `NHAN_VAT_FLOW.md`): Đông, Hạ, Ông Khánh, Bà Hằng trẻ, Anh Toàn, Bà Huệ, Linh.
3. Tạo 13 bộ còn lại bằng *Prompt sửa* từ ảnh ở cột *Gốc từ*. Bố Đông tạo từ ảnh Đông; Ông Khánh trẻ và Bà Hằng già tạo từ ảnh gốc của chính người đó.
4. Render từng shot: Omni 1.2 Flash, 16:9, 720p (nháp 360p), đúng số giây, đính đúng nhân vật (+ ảnh bối cảnh), dán nguyên file prompt. Tên video `<shot> · <tên>`.
5. Tải về đặt tên `CODR_<shot>_....mp4`, chạy `_tools/collect.sh`. Kiểm từng shot theo danh sách cuối `DAO_DIEN.md`.
6. Ưu tiên cảnh 01, 02, 03, 04, 05, 10, 14, 15, 16 để kịp teaser (09/12) và trailer (12/12).

**Ước tính:** 1.307 giây cần tạo ≈ 5.200 credit ở mức 4 credit/giây. Giá credit Google đổi thường xuyên, kiểm tra trong Settings của Flow.
