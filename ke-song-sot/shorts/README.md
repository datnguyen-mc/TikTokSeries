# Kẻ Sống Sót: Bóng Ma — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Phim 60 phút được cắt thành các phần dọc 9:16, mỗi phần gần như trọn một cảnh (~1 phút): mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt, đăng nối tiếp như một series.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn xanh “KẺ SỐNG SÓT: BÓNG MA • PHẦN N” và câu hook ở trên khung phim; phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper). Bản render dùng thoại khác kịch bản V3 nên không so kịch bản; tên riêng và chữ Whisper nghe nhầm sửa bằng `subtitle_replace`.
- **Âm thanh:** chuẩn hoá −14 LUFS.
- **Nguồn clip:** 360 clip tải từ R2 về `output_videos/` (bản render 03–04/11, kịch bản V3).
- **Thư mục mỗi phần** (`phan-XX-.../`): video `.mp4`, ảnh bìa `cover.jpg`, phụ đề rời `phu-de.srt`, và `caption.md` có sẵn caption TikTok, tiêu đề + mô tả YouTube, caption Facebook để copy.

Dựng lại:

```bash
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ke-song-sot            # tất cả
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ke-song-sot --only 3   # một phần
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ke-song-sot --captions # chỉ caption + README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Nội dung (mở caption) | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|
| 1 | [Bóng Ma chỉ còn 7 ngày để cứu người yêu](phan-01-bay-ngay-de-cuu-ha/caption.md) | 01.1, 01.2, 01.3, 01.4, 01.5, 01.6 | 53s | Thứ Sáu 13/11 – 09:00 | ⭐ |
| 2 | [Sát thủ xin giải nghệ, bà trùm giao việc cuối](phan-02-hop-dong-cuoi/caption.md) | 02.1, 02.2, 02.3, 02.4, 02.5, 02.6 | 55s | Thứ Sáu 13/11 – 17:00 |  |
| 3 | [Sát thủ ghé tiệm hoa ba lần chỉ vì một tiếng cười](phan-03-ba-lan-ghe-tiem-hoa/caption.md) | 04.1, 04.2, 04.3, 04.4, 04.5, 04.6 | 53s | Thứ Bảy 14/11 – 09:00 |  |
| 4 | [Chiếc đồng hồ quả quýt và lời hẹn về biển](phan-04-chiec-dong-ho-qua-quyt/caption.md) | 06.1, 06.2, 06.3, 06.4, 06.5, 06.6 | 46s | Thứ Bảy 14/11 – 17:00 |  |
| 5 | [Hợp đồng cuối là cái bẫy](phan-05-dem-bi-gai/caption.md) | 08.1, 08.2, 08.3, 08.4, 08.5, 08.6 | 52s | Chủ Nhật 15/11 – 09:00 | ⭐ |
| 6 | [Bóng Ma tay không hạ hai kẻ đánh úp](phan-06-rung-duong/caption.md) | 12.1, 12.2, 12.3, 12.4, 12.5, 12.6 | 48s | Chủ Nhật 15/11 – 17:00 | ⭐ |
| 7 | [Cô gái trong ảnh là bạn thân của nữ công an](phan-07-co-gai-trong-anh/caption.md) | 14.2, 14.3, 14.4, 14.5, 14.6 | 48s | Thứ Hai 16/11 – 09:00 |  |
| 8 | [Đàn em bà trùm xuống quậy thị trấn](phan-08-dung-toi-bien/caption.md) | 18.1, 18.2, 18.3, 18.4, 18.5, 18.6 | 52s | Thứ Hai 16/11 – 17:00 |  |
| 9 | [Cuộc gọi giấu mặt: cô ấy còn sống](phan-09-cuoc-goi-giau-mat/caption.md) | 20.1, 20.2, 20.3, 20.4, 20.5 | 41s | Thứ Ba 17/11 – 09:00 |  |
| 10 | [Bà trùm thú nhận bán cô gái trước mặt công an](phan-10-ba-trum-thu-nhan/caption.md) | 22.4, 22.5, 22.6, 23.2, 23.3, 23.4 | 52s | Thứ Ba 17/11 – 17:00 | ⭐ |
| 11 | [Nữ công an còng gã giang hồ giữa hầm xe](phan-11-bai-xe-chiec-cong-thu-hai/caption.md) | 24.1, 24.2, 24.3, 24.4, 24.5, 24.6 | 43s | Thứ Tư 18/11 – 09:00 |  |
| 12 | [Video con tin: cô gái gửi mật mã qua kẹp tóc](phan-12-ha-trong-khung-hinh/caption.md) | 27.1, 27.2, 27.3, 27.4, 27.5, 27.6 | 50s | Thứ Tư 18/11 – 17:00 |  |
| 13 | [Đêm cuối trước khi cô ấy bị bắt đi](phan-13-dem-cuoi-o-tiem-hoa/caption.md) | 33.1, 33.2, 33.3, 33.4, 33.5, 33.6 | 42s | Thứ Năm 19/11 – 09:00 |  |
| 14 | [Trùm thật lộ mặt, ép Bóng Ma ký nhận tội](phan-14-khach-hang-ao-trang/caption.md) | 36.1, 36.2, 36.3, 36.4, 36.5, 36.6 | 51s | Thứ Năm 19/11 – 17:00 |  |
| 15 | [25 năm trước, bà trùm trao đôi găng đen](phan-15-doi-gang-den-dau-tien/caption.md) | 38.2, 38.3, 38.4, 38.5, 38.6 | 46s | Thứ Sáu 20/11 – 09:00 |  |
| 16 | [Cuộc trao đổi con tin bị đổi luật](phan-16-cuoc-trao-doi-doi-luat/caption.md) | 41.1, 41.2, 41.3, 41.4, 41.6 | 39s | Thứ Sáu 20/11 – 17:00 |  |
| 17 | [Bóng Ma trúng thuốc Tê giữa bãi cảng](phan-17-bong-ma-nga-xuong/caption.md) | 42.1, 42.2, 42.3, 42.4, 42.5, 42.6 | 46s | Thứ Bảy 21/11 – 09:00 | ⭐ |
| 18 | [Bà trùm giành lại con nuôi, bị kẻ thù vạch mặt](phan-18-khong-ai-la-mon-hang/caption.md) | 43.1, 43.2, 43.4, 43.6 | 35s | Thứ Bảy 21/11 – 17:00 |  |
| 19 | [Bà trùm Rắn Đen tự tay tháo vòng ngọc](phan-19-chiec-vong-ngoc/caption.md) | 49.1, 49.3, 49.5, 49.6 | 27s | Chủ Nhật 22/11 – 09:00 |  |
| 20 | [Đỉnh hải đăng: kẻ bắt cóc khống chế con tin](phan-20-dinh-hai-dang/caption.md) | 50.1, 50.2, 50.3, 50.4, 50.5, 50.6 | 49s | Chủ Nhật 22/11 – 17:00 |  |
| 21 | [Bóng Ma cứu cả kẻ thù trên đỉnh hải đăng](phan-21-cuu-ca-ke-thu/caption.md) | 51.1, 51.2, 51.3, 51.4, 51.6 | 35s | Thứ Hai 23/11 – 09:00 | ⭐ |
| 22 | [Lần đầu mở nắp chiếc đồng hồ](phan-22-lan-dau-mo-dong-ho/caption.md) | 52.1, 52.2, 52.3, 52.4, 52.5, 52.6 | 41s | Thứ Hai 23/11 – 17:00 | ⭐ |
| 23 | [Cứu được người yêu, Bóng Ma tự nhận còng](phan-23-nguoi-khong-chay-nua/caption.md) | 53.1, 53.2, 53.4, 53.5, 53.6 | 33s | Thứ Ba 24/11 – 09:00 | ⭐ |
| 24 | [Chia tay qua ô cửa xe chuyển trại](phan-24-qua-o-cua-xe/caption.md) | 58.1, 58.2, 58.3, 58.4, 58.5, 58.6 | 38s | Thứ Ba 24/11 – 17:00 |  |
| 25 | [20 năm sau, người ấy đã về](phan-25-hai-muoi-nam-sau/caption.md) | 60.1, 60.2, 60.3, 60.4, 60.5, 60.6 | 35s | Thứ Tư 25/11 – 09:00 |  |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Kẻ Sống Sót: Bóng Ma”. Ghim phần 1 và 2 phần ⭐ hành động lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả trong `caption.md`; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions`.
- **Facebook Reels:** dán caption; tắt phụ đề tự động vì phụ đề đã in sẵn.
- Mỗi ngày 2 phần lúc 09:00 và 17:00, xen kẽ với Chính Thất Cao Tay (12:00 và 20:00). Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Đã xử lý trong bản short

- **Video lấy từ R2:** 360 clip tải về `output_videos/` từ Cloudflare R2 (thư mục trên máy trước đó trống). Bản render này làm từ một phiên bản thoại cũ hơn kịch bản V3 hiện tại, nên caption và phụ đề bám theo tiếng thật trong clip.
- **Whisper ảo giác:** 28 clip có nhạc/tiếng động khiến Whisper bịa câu “Hãy subscribe cho kênh…”; đã nghe lại bằng faster-whisper large-v3 có lọc VAD.
- **Thoại lạc đề:** Omni tự nói câu chung chung không thuộc phim ở 14.1, 38.1, 41.5, 43.3, 43.5, 49.2, 49.4, 51.5, 53.3 (vd “Chúng ta cần kiểm tra lại toàn bộ tàu cá…”). Short bỏ các clip này; **bản FULL vẫn chứa chúng**, nên render lại trước khi đăng phim dài.
- **Nói lặp:** 04.6, 41.6, 52.1 cắt bỏ lần nói lặp; 20.6 bỏ.
- Tên riêng Whisper nghe sai (May → Mây, hòng sóng → Hòn Sóng, ngắm tê → Ngấm Tê…) sửa bằng `subtitle_replace` trong plan.
