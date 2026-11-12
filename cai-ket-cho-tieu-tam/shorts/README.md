# Chính Thất Cao Tay — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Phim 25 phút được cắt thành **25 phần dọc 9:16**, mỗi phần là một mạch truyện trọn vẹn (mở bằng câu thoại gây tò mò, kết bằng câu chốt) dài 30–60 giây, đăng nối tiếp như một series.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn đỏ “CHÍNH THẤT CAO TAY • PHẦN N” và câu hook ở trên khung phim; phụ đề khớp tiếng ở dưới khung phim (lời chị Thu màu vàng, người khác màu trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chính tả sửa theo kịch bản. Câu Omni nói khác kịch bản thì phụ đề theo tiếng thật.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm).
- **Thư mục mỗi phần** (`phan-XX-.../`): video `.mp4`, ảnh bìa `cover.jpg`, phụ đề rời `phu-de.srt` (tải lên YouTube/Facebook làm CC nếu muốn), và `caption.md` có sẵn caption TikTok, tiêu đề + mô tả YouTube, caption Facebook để copy.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam            # tất cả
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam --only 17  # một phần
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam --captions # chỉ caption + README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Nội dung (mở caption) | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|
| 1 | [Tiểu tam đến tận tiệm vợ cả đặt may áo cưới](phan-01-tieu-tam-dat-ao-cuoi/caption.md) | 01.2, 01.3, 01.4 | 44s | Thứ Sáu 13/11 – 12:00 | ⭐ |
| 2 | [Cổ áo chồng thơm đúng mùi nước hoa cô dâu](phan-02-co-ao-thom-nuoc-hoa/caption.md) | 02.2, 02.3, 02.4 | 43s | Thứ Sáu 13/11 – 20:00 |  |
| 3 | [Mẹ chồng giữ cho con dâu một đường lui](phan-03-me-chong-giu-bi-mat/caption.md) | 03.1, 03.2, 03.3, 03.4 | 58s | Thứ Bảy 14/11 – 12:00 |  |
| 4 | [Cô thư ký ngây thơ hoá ra đã có chồng](phan-04-vo-chong-nha-lua/caption.md) | 04.1, 04.2, 04.3, 04.4 | 59s | Thứ Bảy 14/11 – 20:00 | ⭐ |
| 5 | [Chính thất phát hiện vết hằn nhẫn trên tay tiểu tam](phan-05-vet-han-nhan-cuoi/caption.md) | 05.1, 05.2, 05.3, 05.4 | 59s | Chủ Nhật 15/11 – 12:00 |  |
| 6 | [Chồng nhờ vợ ký giấy, vợ đọc trang đầu](phan-06-to-giay-ky-khong-doc/caption.md) | 06.1, 06.2, 06.3, 06.4 | 56s | Chủ Nhật 15/11 – 20:00 |  |
| 7 | [Luật sư cầm cặp ngược](phan-07-luat-su-cam-cap-nguoc/caption.md) | 07.1, 07.2, 07.3, 07.4 | 59s | Thứ Hai 16/11 – 12:00 |  |
| 8 | [Tiểu tam về ra mắt, mẹ chồng bắt lau nhà](phan-08-me-chong-bat-tieu-tam-lau-nha/caption.md) | 08.1, 08.2, 08.3, 08.4 | 60s | Thứ Hai 16/11 – 20:00 | ⭐ |
| 9 | [Về quê tiểu tam, thấy ảnh cưới trên bàn thờ](phan-09-ve-que-tieu-tam/caption.md) | 09.2, 09.3, 09.4 | 45s | Thứ Ba 17/11 – 12:00 |  |
| 10 | [Tiểu tam mua chuộc con gái chính thất](phan-10-be-na-theo-bo/caption.md) | 10.1, 10.2, 10.3, 10.4 | 60s | Thứ Ba 17/11 – 20:00 |  |
| 11 | [Nhà bố có bể bơi nhưng không có mẹ](phan-11-nha-bo-khong-co-me/caption.md) | 11.1, 11.2, 11.3, 11.4 | 54s | Thứ Tư 18/11 – 12:00 |  |
| 12 | [Chuyển 5 tỷ sính lễ, cô dâu hứa làm vợ đúng 1 ngày](phan-12-nam-ty-sinh-le/caption.md) | 12.1, 12.2, 12.3, 12.4 | 59s | Thứ Tư 18/11 – 20:00 |  |
| 13 | [Vợ đồng ý ly hôn với một điều kiện](phan-13-chinh-that-dong-y-ly-hon/caption.md) | 13.1, 13.2, 13.3, 13.4 | 59s | Thứ Năm 19/11 – 12:00 | ⭐ |
| 14 | [Tiểu tam doạ cho chính thất trắng tay](phan-14-buoi-thu-ao-cuoi-cung/caption.md) | 14.1, 14.2, 14.3, 14.4 | 58s | Thứ Năm 19/11 – 20:00 |  |
| 15 | [Đêm trước đám hỏi](phan-15-dem-truoc-dam-hoi/caption.md) | 15.2, 15.3, 15.4 | 45s | Thứ Sáu 20/11 – 12:00 |  |
| 16 | [Vợ cả đeo tạp dề đến đám hỏi của chồng](phan-16-vo-ca-den-dam-hoi/caption.md) | 16.2, 16.3, 16.4 | 44s | Thứ Sáu 20/11 – 20:00 |  |
| 17 | [Quà cưới: ảnh cưới lần trước của tiểu tam](phan-17-mon-qua-cuoi/caption.md) | 17.1, 17.2, 17.3, 17.4 | 57s | Thứ Bảy 21/11 – 12:00 | ⭐ |
| 18 | [Chồng hứa tặng bồ căn nhà đứng tên vợ](phan-18-so-do-dung-ten-ai/caption.md) | 18.1, 18.2, 18.3 | 44s | Thứ Bảy 21/11 – 20:00 | ⭐ |
| 19 | [Tiểu tam bỏ trốn nhưng áo cưới may quá khít](phan-19-loi-thoat-hiem/caption.md) | 19.1, 19.2, 19.3, 19.4 | 52s | Chủ Nhật 22/11 – 12:00 |  |
| 20 | [Mất trắng sau đám hỏi, mẹ nói một câu](phan-20-cay-tung-do/caption.md) | 20.1, 20.2, 20.3, 20.4 | 59s | Chủ Nhật 22/11 – 20:00 |  |
| 21 | [Vợ thành chủ tịch, chồng xuống công trường](phan-21-tu-giam-doc-xuong-be-gach/caption.md) | 21.1, 21.2, 21.3, 21.4 | 60s | Thứ Hai 23/11 – 12:00 | ⭐ |
| 22 | [Chính thất vào trại thăm tiểu tam](phan-22-phong-tham-gap/caption.md) | 22.1, 22.2, 22.3, 22.4 | 59s | Thứ Hai 23/11 – 20:00 | ⭐ |
| 23 | [Cựu giám đốc bê gạch, con gái mang cơm](phan-23-bo-be-gach-con-mang-com/caption.md) | 23.1, 23.2, 23.3, 23.4 | 56s | Thứ Ba 24/11 – 12:00 |  |
| 24 | [Bà nội 71 tuổi đòi đi bước nữa](phan-24-ao-dai-mung-tho/caption.md) | 24.1, 24.2, 24.3, 24.4 | 60s | Thứ Ba 24/11 – 20:00 |  |
| 25 | [Tiểu tam là gì hả mẹ?](phan-25-tieu-tam-la-gi-ha-me/caption.md) | 25.2, 25.3, 25.4 | 44s | Thứ Tư 25/11 – 12:00 | ⭐ |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Chính Thất Cao Tay”. Chọn ảnh bìa bằng khung hình có hook (giây đầu) hoặc tải `cover.jpg`. Ghim 3 phần ⭐ đầu tiên lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả trong `caption.md`; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption, bật “Tạo phụ đề tự động” tắt đi (phụ đề đã in sẵn trên video).
- Mỗi ngày 2 phần (12:00 và 20:00), 3 nền tảng cùng giờ. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Đã xử lý trong bản short

- **Logo VTV** Omni tự vẽ ở góc phải clip 17.2 → xoá bằng delogo (phần 17). Logo này **vẫn còn trong bản FULL YouTube** (khoảng 16:15–16:30).
- **Khung máy quay giả** (chữ “24 fps”, “HÀ NỘI” ở viền) trong clip 02.4 → phóng nhẹ để cắt viền (phần 2). Bản FULL vẫn còn.
- **Nói lặp:** 11.3 lặp nguyên câu “Bố cũng chẳng chịu nghe con nói” → cắt ở 10,05 s; 17.2 chen câu “cũng là đạo cụ à?” trước lượt → bỏ đoạn 8,5–10,13 s.
- **Clip 09.1 hỏng tiếng:** Omni nói ra chuỗi vô nghĩa (“May là một của trong trăm năm môi nghiên…”), không dùng trong short. Bản FULL vẫn chứa clip này ở khoảng 08:00–08:15, nên render lại.
