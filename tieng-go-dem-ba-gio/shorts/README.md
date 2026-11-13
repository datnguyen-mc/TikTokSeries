# Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **các cảnh hay nhất** của phim ma 15 phút, không phải cả phim: **11 phần dọc 9:16**, mỗi phần là một khoảnh khắc trọn vẹn dài 30–60 giây (bí ẩn, hù dọa, cú lật), mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger, đăng nối tiếp theo thứ tự truyện như một series.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn tím than “TIẾNG GÕ ĐÊM BA GIỜ • PHẦN N” và câu hook ở trên khung phim (cụm nhấn màu xanh ngọc); phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau, phần cuối đổi thành “XEM FULL PHIM”. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chính tả và tên riêng sửa theo kịch bản `PHAN_CANH_OMNI.json`. Câu Omni nói khác kịch bản thì phụ đề theo tiếng thật.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** mỗi đoạn dùng nguyên clip; khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm), câu Omni đọc lặp ở đuôi clip được cắt bỏ.
- **File:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; lịch đăng và caption TikTok, tiêu đề + mô tả YouTube, caption Facebook của mọi phần nằm trong `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py tieng-go-dem-ba-gio            # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py tieng-go-dem-ba-gio --only 2   # một phần
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py tieng-go-dem-ba-gio --captions # chỉ caption + README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-ba-dieu-cam-ky.mp4`](01-ba-dieu-cam-ky.mp4) | Trông nhà cổ 3 đêm, bà quản gia dặn 3 điều cấm kỵ | 01.3, 01.4, 01.5, 01.6 | 40s | Thứ Bảy 14/11 – 11:00 |  |
| 2 | [`02-tieng-go-duoi-day-gieng.mp4`](02-tieng-go-duoi-day-gieng.mp4) | 2 giờ 59 sáng, ba tiếng gõ dội lên từ đáy giếng | 02.2, 02.3, 02.4, 02.5, 02.6 | 48s | Thứ Bảy 14/11 – 19:00 | ⭐ |
| 3 | [`03-bong-ma-trong-guong-dong.mp4`](03-bong-ma-trong-guong-dong.mp4) | Lỡ nhìn vào gương đồng, thấy cô gái sát sau gáy | 03.2, 03.3, 03.4, 03.5, 03.6 | 45s | Chủ Nhật 15/11 – 11:00 |  |
| 4 | [`04-bong-ma-trong-anh-chup.mp4`](04-bong-ma-trong-anh-chup.mp4) | Mỗi tấm ảnh, bóng ma lại tiến gần ống kính hơn | 04.2, 04.3, 04.4, 04.5 | 39s | Chủ Nhật 15/11 – 19:00 | ⭐ |
| 5 | [`05-canh-cua-thu-tu.mp4`](05-canh-cua-thu-tu.mp4) | Hành lang chỉ có 3 cửa, nửa đêm hiện cửa thứ tư | 06.3, 06.4, 06.5, 06.6 | 31s | Thứ Hai 16/11 – 11:00 |  |
| 6 | [`06-nguc-ngam-duoi-gieng.mp4`](06-nguc-ngam-duoi-gieng.mp4) | Buồng niêm phong 50 năm và nắp hầm thông xuống giếng | 07.2, 07.3, 07.4, 07.5, 07.6 | 42s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-ba-quan-gia-da-chet.mp4`](07-ba-quan-gia-da-chet.mp4) | Bà lão giao chìa khóa đã chết từ 3 năm trước | 08.2, 08.3, 08.4, 08.5, 08.6 | 41s | Thứ Ba 17/11 – 11:00 | ⭐ |
| 8 | [`08-tien-coc-hoa-vang-ma.mp4`](08-tien-coc-hoa-vang-ma.mp4) | Mở phong bì tiền cọc, toàn là tiền vàng mã | 09.1, 09.2, 09.3, 09.4 | 33s | Thứ Ba 17/11 – 19:00 |  |
| 9 | [`09-ac-linh-co-gay-ngoai-hien.mp4`](09-ac-linh-co-gay-ngoai-hien.mp4) | Tiếng chìa khóa ngoài hiên, ác linh cổ gãy đòi mạng | 09.6, 10.1, 10.2, 10.3, 10.4 | 41s | Thứ Tư 18/11 – 11:00 |  |
| 10 | [`10-nhat-bua-luc-2-gio-59.mp4`](10-nhat-bua-luc-2-gio-59.mp4) | Nhát búa lúc 2 giờ 59, đập vỡ bia trấn yểm | 13.1, 13.2, 13.3, 13.4, 13.5 | 38s | Thứ Tư 18/11 – 19:00 |  |
| 11 | [`11-dau-tay-tren-guong-dong.mp4`](11-dau-tay-tren-guong-dong.mp4) | Quay lưng rời nhà cổ, gương đồng hiện dấu tay vẫy chào | 15.3, 15.4, 15.5, 15.6 | 33s | Thứ Năm 19/11 – 11:00 |  |

⭐ = 3 phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Tiếng Gõ Đêm Ba Giờ”. Chọn ảnh bìa bằng khung hình có hook (giây đầu). Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả trong README này; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption; tắt “Tạo phụ đề tự động” vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00) từ 14/11, 3 nền tảng cùng giờ. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Ghi chú dựng

- Các đoạn đang dùng nguyên clip, chưa có `from`/`to`: xem bản dựng rồi tinh chỉnh điểm cắt trong plan nếu cần.
- `subtitle_replace` và `fixes` đang trống: điền sau khi xem bản Whisper (tên riêng nghe sai, chữ hay logo Omni tự vẽ vào khung).
- Đã đối chiếu bản Whisper (`shorts/_whisper/`) của mọi clip trong plan với kịch bản: thoại khớp. Các clip 06.6, 08.2, 09.1, 09.2, 10.2, 13.5 đọc lặp cụm cuối câu; script tự cắt đoạn lặp ở đuôi clip.
- **03.5** (7,4 s): mất vế đầu “Khoảng không phía sau hoàn toàn trống rỗng”, câu bắt đầu từ “Nhưng mặt sàn gỗ khô…” (phần 3). **06.6**: nói vấp “kéo anh, kéo anh”, phụ đề tự gộp nhưng tiếng vẫn còn (phần 5). **13.5**: mất chữ “Tấm bia” ở đầu câu (phần 10).

## Caption từng phần (copy dán)

### Phần 1/11 — Trông nhà cổ 3 đêm, bà quản gia dặn 3 điều cấm kỵ

`01-ba-dieu-cam-ky.mp4` · 40s · cảnh 01.3, 01.4, 01.5, 01.6 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
Đón Lâm nơi hiên nhà lạnh toát là bà Cầm mù một mắt, tay nắm chặt chùm chìa khóa đồng: “Đúng ba giờ sáng, dù dưới đáy giếng có tiếng khóc gọi tên, cậu tuyệt đối không được mở xích nhìn xuống!” Cấm soi gương đồng phủ lụa đen sau nửa đêm, hành lang hiện cửa thứ tư phải lùi ngay. Lâm điểm chỉ lên giấy… và cánh cổng sắt khép lại sau lưng anh.
Ba điều cấm này, bạn giữ nổi điều nào?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #nhaco #camky
```

**YouTube Shorts — tiêu đề** (90/100 ký tự)

```text
Nhận trông nhà cổ 3 đêm, bà quản gia mù một mắt dặn 3 điều cấm kỵ | Tiếng Gõ Đêm Ba Giờ P1
```

**YouTube Shorts — mô tả**

```text
Đón Lâm nơi hiên nhà lạnh toát là bà Cầm mù một mắt, tay nắm chặt chùm chìa khóa đồng: “Đúng ba giờ sáng, dù dưới đáy giếng có tiếng khóc gọi tên, cậu tuyệt đối không được mở xích nhìn xuống!” Cấm soi gương đồng phủ lụa đen sau nửa đêm, hành lang hiện cửa thứ tư phải lùi ngay. Lâm điểm chỉ lên giấy… và cánh cổng sắt khép lại sau lưng anh.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 2: 2 giờ 59 sáng, ba tiếng gõ dội lên từ đáy giếng

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Đón Lâm nơi hiên nhà lạnh toát là bà Cầm mù một mắt, tay nắm chặt chùm chìa khóa đồng: “Đúng ba giờ sáng, dù dưới đáy giếng có tiếng khóc gọi tên, cậu tuyệt đối không được mở xích nhìn xuống!” Cấm soi gương đồng phủ lụa đen sau nửa đêm, hành lang hiện cửa thứ tư phải lùi ngay. Lâm điểm chỉ lên giấy… và cánh cổng sắt khép lại sau lưng anh.

Ba điều cấm này, bạn giữ nổi điều nào? 👇
👉 Xem tiếp Phần 2: 2 giờ 59 sáng, ba tiếng gõ dội lên từ đáy giếng
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #nhaco #camky
```

### Phần 2/11 — 2 giờ 59 sáng, ba tiếng gõ dội lên từ đáy giếng

`02-tieng-go-duoi-day-gieng.mp4` · 48s · cảnh 02.2, 02.3, 02.4, 02.5, 02.6 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Hai giờ năm mươi chín phút, đồng hồ quả lắc đứng khựng, nến bàn thờ phụt tắt. Từ đáy giếng đá ong, ba tiếng gõ trầm đục dội lên nắp đá, xích sắt tự giật căng, rồi năm ngón tay trắng bệch rớm máu thò lên bấu chặt thành giếng. Ngay khe cửa, một giọng con gái thì thầm: “Lâm ơi cứu em ra khỏi đáy giếng lạnh lẽo này với, ở dưới này tối tăm và ngột ngạt lắm Lâm ơi!”
Nếu là Lâm, bạn có mở nắp giếng không?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #gieng #kinhdi
```

**YouTube Shorts — tiêu đề** (80/100 ký tự)

```text
2 giờ 59 sáng, ba tiếng gõ dội lên từ đáy giếng bị xích | Tiếng Gõ Đêm Ba Giờ P2
```

**YouTube Shorts — mô tả**

```text
Hai giờ năm mươi chín phút, đồng hồ quả lắc đứng khựng, nến bàn thờ phụt tắt. Từ đáy giếng đá ong, ba tiếng gõ trầm đục dội lên nắp đá, xích sắt tự giật căng, rồi năm ngón tay trắng bệch rớm máu thò lên bấu chặt thành giếng. Ngay khe cửa, một giọng con gái thì thầm: “Lâm ơi cứu em ra khỏi đáy giếng lạnh lẽo này với, ở dưới này tối tăm và ngột ngạt lắm Lâm ơi!”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 3: Lỡ nhìn vào gương đồng, thấy cô gái sát sau gáy

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Hai giờ năm mươi chín phút, đồng hồ quả lắc đứng khựng, nến bàn thờ phụt tắt. Từ đáy giếng đá ong, ba tiếng gõ trầm đục dội lên nắp đá, xích sắt tự giật căng, rồi năm ngón tay trắng bệch rớm máu thò lên bấu chặt thành giếng. Ngay khe cửa, một giọng con gái thì thầm: “Lâm ơi cứu em ra khỏi đáy giếng lạnh lẽo này với, ở dưới này tối tăm và ngột ngạt lắm Lâm ơi!”

Nếu là Lâm, bạn có mở nắp giếng không? 👇
👉 Xem tiếp Phần 3: Lỡ nhìn vào gương đồng, thấy cô gái sát sau gáy
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #gieng #kinhdi
```

### Phần 3/11 — Lỡ nhìn vào gương đồng, thấy cô gái sát sau gáy

`03-bong-ma-trong-guong-dong.mp4` · 45s · cảnh 03.2, 03.3, 03.4, 03.5, 03.6 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Cúi nhặt tấm khăn lụa đen vừa rơi, Lâm vô tình nhìn thẳng vào gương đồng: ngay sát sau gáy anh là bóng cô gái áo dài trắng ướt đẫm bùn đen. Anh quay phắt lại: “Ai đó?! Kẻ nào vừa đứng ngay sát sau lưng tôi ở trong gian nhà thờ tối tăm này thế hả?!” Phía sau trống rỗng, chỉ có hai dấu chân bùn đen trên sàn gỗ khô… và bóng ma trong gương mỉm cười vươn bàn tay rớm máu ra ngoài.
Bạn còn dám soi gương lúc nửa đêm không?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #guongdong #kinhdi
```

**YouTube Shorts — tiêu đề** (89/100 ký tự)

```text
Lỡ nhìn vào gương đồng sau nửa đêm, thấy cô gái đứng sát sau gáy | Tiếng Gõ Đêm Ba Giờ P3
```

**YouTube Shorts — mô tả**

```text
Cúi nhặt tấm khăn lụa đen vừa rơi, Lâm vô tình nhìn thẳng vào gương đồng: ngay sát sau gáy anh là bóng cô gái áo dài trắng ướt đẫm bùn đen. Anh quay phắt lại: “Ai đó?! Kẻ nào vừa đứng ngay sát sau lưng tôi ở trong gian nhà thờ tối tăm này thế hả?!” Phía sau trống rỗng, chỉ có hai dấu chân bùn đen trên sàn gỗ khô… và bóng ma trong gương mỉm cười vươn bàn tay rớm máu ra ngoài.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 4: Mỗi tấm ảnh, bóng ma lại tiến gần ống kính hơn

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Cúi nhặt tấm khăn lụa đen vừa rơi, Lâm vô tình nhìn thẳng vào gương đồng: ngay sát sau gáy anh là bóng cô gái áo dài trắng ướt đẫm bùn đen. Anh quay phắt lại: “Ai đó?! Kẻ nào vừa đứng ngay sát sau lưng tôi ở trong gian nhà thờ tối tăm này thế hả?!” Phía sau trống rỗng, chỉ có hai dấu chân bùn đen trên sàn gỗ khô… và bóng ma trong gương mỉm cười vươn bàn tay rớm máu ra ngoài.

Bạn còn dám soi gương lúc nửa đêm không? 👇
👉 Xem tiếp Phần 4: Mỗi tấm ảnh, bóng ma lại tiến gần ống kính hơn
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #guongdong #kinhdi
```

### Phần 4/11 — Mỗi tấm ảnh, bóng ma lại tiến gần ống kính hơn

`04-bong-ma-trong-anh-chup.mp4` · 39s · cảnh 04.2, 04.3, 04.4, 04.5 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Xem lại ảnh chụp gian nhà trống, Lâm thấy bóng áo trắng thấp thoáng nơi góc cột gỗ lim. Sang tấm thứ hai, thứ ba, sau mỗi lần chớp đèn cái bóng lại tiến gần thêm, đến tấm cuối thì khuôn mặt trắng bệch đã áp sát ống kính. “Đột nhiên đèn flash máy ảnh tự chớp sáng trắng xóa, cô gái áo trắng đang đứng ngay bên kia chiếc bàn gỗ!”
Đến tấm ảnh thứ mấy thì bạn ném máy ảnh đi?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #anhma #kinhdi
```

**YouTube Shorts — tiêu đề** (85/100 ký tự)

```text
Mỗi tấm ảnh chụp, bóng ma áo trắng lại tiến gần ống kính hơn | Tiếng Gõ Đêm Ba Giờ P4
```

**YouTube Shorts — mô tả**

```text
Xem lại ảnh chụp gian nhà trống, Lâm thấy bóng áo trắng thấp thoáng nơi góc cột gỗ lim. Sang tấm thứ hai, thứ ba, sau mỗi lần chớp đèn cái bóng lại tiến gần thêm, đến tấm cuối thì khuôn mặt trắng bệch đã áp sát ống kính. “Đột nhiên đèn flash máy ảnh tự chớp sáng trắng xóa, cô gái áo trắng đang đứng ngay bên kia chiếc bàn gỗ!”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 5: Hành lang chỉ có 3 cửa, nửa đêm hiện cửa thứ tư

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Xem lại ảnh chụp gian nhà trống, Lâm thấy bóng áo trắng thấp thoáng nơi góc cột gỗ lim. Sang tấm thứ hai, thứ ba, sau mỗi lần chớp đèn cái bóng lại tiến gần thêm, đến tấm cuối thì khuôn mặt trắng bệch đã áp sát ống kính. “Đột nhiên đèn flash máy ảnh tự chớp sáng trắng xóa, cô gái áo trắng đang đứng ngay bên kia chiếc bàn gỗ!”

Đến tấm ảnh thứ mấy thì bạn ném máy ảnh đi? 👇
👉 Xem tiếp Phần 5: Hành lang chỉ có 3 cửa, nửa đêm hiện cửa thứ tư
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #anhma #kinhdi
```

### Phần 5/11 — Hành lang chỉ có 3 cửa, nửa đêm hiện cửa thứ tư

`05-canh-cua-thu-tu.mp4` · 31s · cảnh 06.3, 06.4, 06.5, 06.6 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
Nơi bức vách gỗ trống ban ngày, đêm thứ hai bỗng lù lù hiện ra cánh cửa buồng thứ tư đỏ sẫm như máu, sau cửa vang tiếng khung cửi lách cách hòa tiếng con gái khóc. “Lâm nhắm chặt mắt bước lùi, nhưng mới lùi được ba bước thì cánh cửa thứ tư bỗng tự bật chốt mở toang!” Một luồng lực vô hình níu dây máy ảnh, kéo anh vào buồng niêm phong.
Sau cánh cửa thứ tư có gì, bạn đoán thử?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #cuathutu #bian
```

**YouTube Shorts — tiêu đề** (91/100 ký tự)

```text
Hành lang chỉ có 3 cửa, nửa đêm hiện ra cánh cửa thứ tư đỏ như máu | Tiếng Gõ Đêm Ba Giờ P5
```

**YouTube Shorts — mô tả**

```text
Nơi bức vách gỗ trống ban ngày, đêm thứ hai bỗng lù lù hiện ra cánh cửa buồng thứ tư đỏ sẫm như máu, sau cửa vang tiếng khung cửi lách cách hòa tiếng con gái khóc. “Lâm nhắm chặt mắt bước lùi, nhưng mới lùi được ba bước thì cánh cửa thứ tư bỗng tự bật chốt mở toang!” Một luồng lực vô hình níu dây máy ảnh, kéo anh vào buồng niêm phong.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 6: Buồng niêm phong 50 năm và nắp hầm thông xuống giếng

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Nơi bức vách gỗ trống ban ngày, đêm thứ hai bỗng lù lù hiện ra cánh cửa buồng thứ tư đỏ sẫm như máu, sau cửa vang tiếng khung cửi lách cách hòa tiếng con gái khóc. “Lâm nhắm chặt mắt bước lùi, nhưng mới lùi được ba bước thì cánh cửa thứ tư bỗng tự bật chốt mở toang!” Một luồng lực vô hình níu dây máy ảnh, kéo anh vào buồng niêm phong.

Sau cánh cửa thứ tư có gì, bạn đoán thử? 👇
👉 Xem tiếp Phần 6: Buồng niêm phong 50 năm và nắp hầm thông xuống giếng
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #cuathutu #bian
```

### Phần 6/11 — Buồng niêm phong 50 năm và nắp hầm thông xuống giếng

`06-nguc-ngam-duoi-gieng.mp4` · 42s · cảnh 07.2, 07.3, 07.4, 07.5, 07.6 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Trong căn buồng niêm phong, di ảnh cô gái áo trắng bị ai cào nát hai mắt, dưới chiếu cói là nắp hầm chi chít vết móng tay cào thông thẳng xuống đáy giếng: một ngục ngầm dùng chôn sống người. Bóng cô gái trồi lên chỉ tay vào bức ảnh gia tộc, và cụ Từ giữ đền lao vào: “Cậu đừng sợ! Oán hồn cô ấy đang chỉ mặt kẻ thủ ác đã chôn sống mình năm mươi năm trước đấy!”
Theo bạn, kẻ thủ ác trong bức ảnh là ai?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #bian #oanhon
```

**YouTube Shorts — tiêu đề** (90/100 ký tự)

```text
Buồng niêm phong 50 năm, nắp hầm thông xuống đáy giếng chôn người | Tiếng Gõ Đêm Ba Giờ P6
```

**YouTube Shorts — mô tả**

```text
Trong căn buồng niêm phong, di ảnh cô gái áo trắng bị ai cào nát hai mắt, dưới chiếu cói là nắp hầm chi chít vết móng tay cào thông thẳng xuống đáy giếng: một ngục ngầm dùng chôn sống người. Bóng cô gái trồi lên chỉ tay vào bức ảnh gia tộc, và cụ Từ giữ đền lao vào: “Cậu đừng sợ! Oán hồn cô ấy đang chỉ mặt kẻ thủ ác đã chôn sống mình năm mươi năm trước đấy!”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 7: Bà lão giao chìa khóa đã chết từ 3 năm trước

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Trong căn buồng niêm phong, di ảnh cô gái áo trắng bị ai cào nát hai mắt, dưới chiếu cói là nắp hầm chi chít vết móng tay cào thông thẳng xuống đáy giếng: một ngục ngầm dùng chôn sống người. Bóng cô gái trồi lên chỉ tay vào bức ảnh gia tộc, và cụ Từ giữ đền lao vào: “Cậu đừng sợ! Oán hồn cô ấy đang chỉ mặt kẻ thủ ác đã chôn sống mình năm mươi năm trước đấy!”

Theo bạn, kẻ thủ ác trong bức ảnh là ai? 👇
👉 Xem tiếp Phần 7: Bà lão giao chìa khóa đã chết từ 3 năm trước
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #bian #oanhon
```

### Phần 7/11 — Bà lão giao chìa khóa đã chết từ 3 năm trước

`07-ba-quan-gia-da-chet.mp4` · 41s · cảnh 08.2, 08.3, 08.4, 08.5, 08.6 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Năm mươi năm trước, mụ quản gia tên Cầm vu oan cho cô Út, trói cô thả xuống giếng rồi khóa chặt bằng bia đá và xích sắt. Lâm sững người: “Khoan đã cụ ơi, vậy bà lão mặc áo đen đưa chìa khóa bắt cháu lăn tay chiều hôm qua là ai?!” Cụ Từ tái mặt: bà Cầm đã ngã gãy cổ chết dưới đáy giếng từ ba năm trước rồi.
Bạn có đoán ra bà Cầm là ai từ phần đầu không?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #plottwist #bacam
```

**YouTube Shorts — tiêu đề** (81/100 ký tự)

```text
Bà quản gia giao chìa khóa hóa ra đã chết từ 3 năm trước | Tiếng Gõ Đêm Ba Giờ P7
```

**YouTube Shorts — mô tả**

```text
Năm mươi năm trước, mụ quản gia tên Cầm vu oan cho cô Út, trói cô thả xuống giếng rồi khóa chặt bằng bia đá và xích sắt. Lâm sững người: “Khoan đã cụ ơi, vậy bà lão mặc áo đen đưa chìa khóa bắt cháu lăn tay chiều hôm qua là ai?!” Cụ Từ tái mặt: bà Cầm đã ngã gãy cổ chết dưới đáy giếng từ ba năm trước rồi.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 8: Mở phong bì tiền cọc, toàn là tiền vàng mã

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Năm mươi năm trước, mụ quản gia tên Cầm vu oan cho cô Út, trói cô thả xuống giếng rồi khóa chặt bằng bia đá và xích sắt. Lâm sững người: “Khoan đã cụ ơi, vậy bà lão mặc áo đen đưa chìa khóa bắt cháu lăn tay chiều hôm qua là ai?!” Cụ Từ tái mặt: bà Cầm đã ngã gãy cổ chết dưới đáy giếng từ ba năm trước rồi.

Bạn có đoán ra bà Cầm là ai từ phần đầu không? 👇
👉 Xem tiếp Phần 8: Mở phong bì tiền cọc, toàn là tiền vàng mã
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #plottwist #bacam
```

### Phần 8/11 — Mở phong bì tiền cọc, toàn là tiền vàng mã

`08-tien-coc-hoa-vang-ma.mp4` · 33s · cảnh 09.1, 09.2, 09.3, 09.4 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Lâm mở phong bì tiền cọc bà Cầm đưa chiều qua: chẳng có tờ tiền thật nào, chỉ toàn tiền vàng mã âm phủ tanh mùi bùn. Tờ giấy anh điểm chỉ hóa ra là Khế Ước Thế Mạng. Cụ Từ nói: “Bà Cầm lừa cậu lăn tay giữ nắp giếng ba đêm, để đúng giờ Dần lấy mạng cậu thế chỗ dưới đáy giếng!”
Bạn đã bao giờ ký giấy mà không đọc kỹ chưa?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #khecuoc #vangma
```

**YouTube Shorts — tiêu đề** (96/100 ký tự)

```text
Mở phong bì tiền cọc toàn vàng mã, tờ giấy điểm chỉ là khế ước thế mạng | Tiếng Gõ Đêm Ba Giờ P8
```

**YouTube Shorts — mô tả**

```text
Lâm mở phong bì tiền cọc bà Cầm đưa chiều qua: chẳng có tờ tiền thật nào, chỉ toàn tiền vàng mã âm phủ tanh mùi bùn. Tờ giấy anh điểm chỉ hóa ra là Khế Ước Thế Mạng. Cụ Từ nói: “Bà Cầm lừa cậu lăn tay giữ nắp giếng ba đêm, để đúng giờ Dần lấy mạng cậu thế chỗ dưới đáy giếng!”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 9: Tiếng chìa khóa ngoài hiên, ác linh cổ gãy đòi mạng

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Lâm mở phong bì tiền cọc bà Cầm đưa chiều qua: chẳng có tờ tiền thật nào, chỉ toàn tiền vàng mã âm phủ tanh mùi bùn. Tờ giấy anh điểm chỉ hóa ra là Khế Ước Thế Mạng. Cụ Từ nói: “Bà Cầm lừa cậu lăn tay giữ nắp giếng ba đêm, để đúng giờ Dần lấy mạng cậu thế chỗ dưới đáy giếng!”

Bạn đã bao giờ ký giấy mà không đọc kỹ chưa? 👇
👉 Xem tiếp Phần 9: Tiếng chìa khóa ngoài hiên, ác linh cổ gãy đòi mạng
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #khecuoc #vangma
```

### Phần 9/11 — Tiếng chìa khóa ngoài hiên, ác linh cổ gãy đòi mạng

`09-ac-linh-co-gay-ngoai-hien.mp4` · 41s · cảnh 09.6, 10.1, 10.2, 10.3, 10.4 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
Đúng lúc sự thật hé lộ, ngoài hiên vang lên tiếng chùm chìa khóa đồng khua trong mưa. Dưới ánh chớp, bà Cầm từ từ ngẩng lên với cái cổ gãy vẹo và đôi mắt trắng dã: “Mày đã điểm chỉ máu vào khế ước rồi con ạ, đêm mai đúng ba giờ sáng hồn mày phải thế chỗ tao!” Cụ Từ lập tức lao lên dán lá bùa Chu Sa vào cửa gỗ.
Lá bùa của cụ Từ giữ được Lâm đến bao giờ?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #aclinh #bacam
```

**YouTube Shorts — tiêu đề** (88/100 ký tự)

```text
Nửa đêm tiếng chìa khóa ngoài hiên, ác linh cổ gãy đến đòi mạng | Tiếng Gõ Đêm Ba Giờ P9
```

**YouTube Shorts — mô tả**

```text
Đúng lúc sự thật hé lộ, ngoài hiên vang lên tiếng chùm chìa khóa đồng khua trong mưa. Dưới ánh chớp, bà Cầm từ từ ngẩng lên với cái cổ gãy vẹo và đôi mắt trắng dã: “Mày đã điểm chỉ máu vào khế ước rồi con ạ, đêm mai đúng ba giờ sáng hồn mày phải thế chỗ tao!” Cụ Từ lập tức lao lên dán lá bùa Chu Sa vào cửa gỗ.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 10: Nhát búa lúc 2 giờ 59, đập vỡ bia trấn yểm

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Đúng lúc sự thật hé lộ, ngoài hiên vang lên tiếng chùm chìa khóa đồng khua trong mưa. Dưới ánh chớp, bà Cầm từ từ ngẩng lên với cái cổ gãy vẹo và đôi mắt trắng dã: “Mày đã điểm chỉ máu vào khế ước rồi con ạ, đêm mai đúng ba giờ sáng hồn mày phải thế chỗ tao!” Cụ Từ lập tức lao lên dán lá bùa Chu Sa vào cửa gỗ.

Lá bùa của cụ Từ giữ được Lâm đến bao giờ? 👇
👉 Xem tiếp Phần 10: Nhát búa lúc 2 giờ 59, đập vỡ bia trấn yểm
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #aclinh #bacam
```

### Phần 10/11 — Nhát búa lúc 2 giờ 59, đập vỡ bia trấn yểm

`10-nhat-bua-luc-2-gio-59.mp4` · 38s · cảnh 13.1, 13.2, 13.3, 13.4, 13.5 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Lâm vung búa chặt đứt vòng xích thứ nhất, ác linh bà Cầm rú lên lao tới, nhưng bóng trắng cô Út đã kịp hiện ra chắn trước mặt. “Tấm bia trấn yểm này hãy vỡ toạc ra đi!! Trả lại ánh sáng tự do cho người bị chôn dưới đáy giếng sâu!!” Bia đá vỡ đôi, tờ khế ước tự bốc lửa xanh, và bà Cầm tan thành vũng bùn đen.
Khoảnh khắc nào làm bạn nổi da gà nhất?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#tienggodembagio #phimma #truyenma #tranyem #giaioan
```

**YouTube Shorts — tiêu đề** (90/100 ký tự)

```text
Nhát búa lúc 2 giờ 59 đập vỡ bia trấn yểm, ác linh tan thành bùn | Tiếng Gõ Đêm Ba Giờ P10
```

**YouTube Shorts — mô tả**

```text
Lâm vung búa chặt đứt vòng xích thứ nhất, ác linh bà Cầm rú lên lao tới, nhưng bóng trắng cô Út đã kịp hiện ra chắn trước mặt. “Tấm bia trấn yểm này hãy vỡ toạc ra đi!! Trả lại ánh sáng tự do cho người bị chôn dưới đáy giếng sâu!!” Bia đá vỡ đôi, tờ khế ước tự bốc lửa xanh, và bà Cầm tan thành vũng bùn đen.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
👉 Xem tiếp Phần 11: Quay lưng rời nhà cổ, gương đồng hiện dấu tay vẫy chào

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Lâm vung búa chặt đứt vòng xích thứ nhất, ác linh bà Cầm rú lên lao tới, nhưng bóng trắng cô Út đã kịp hiện ra chắn trước mặt. “Tấm bia trấn yểm này hãy vỡ toạc ra đi!! Trả lại ánh sáng tự do cho người bị chôn dưới đáy giếng sâu!!” Bia đá vỡ đôi, tờ khế ước tự bốc lửa xanh, và bà Cầm tan thành vũng bùn đen.

Khoảnh khắc nào làm bạn nổi da gà nhất? 👇
👉 Xem tiếp Phần 11: Quay lưng rời nhà cổ, gương đồng hiện dấu tay vẫy chào
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #tranyem #giaioan
```

### Phần 11/11 — Quay lưng rời nhà cổ, gương đồng hiện dấu tay vẫy chào

`11-dau-tay-tren-guong-dong.mp4` · 33s · cảnh 15.3, 15.4, 15.5, 15.6 · đăng Thứ Năm 19/11 – 11:00

**TikTok**

```text
Trước khi về phố, Lâm quay lại gian chính thu dọn hành lý bên chiếc gương đồng nay đã sáng bóng nắng mai. Đúng lúc anh quay lưng, trên mặt gương phía sau hiện lên dấu bàn tay vẫy chào. “Hãy yên nghỉ thanh thản nơi chín suối nhé cô Út, tạm biệt cô, tôi trở về thành phố đây.”
Cái kết này làm bạn sợ hay ấm lòng?

🎬 Xem trọn bộ 15 phút trên kênh YouTube.
#tienggodembagio #phimma #truyenma #ketphim #guongdong
```

**YouTube Shorts — tiêu đề** (84/100 ký tự)

```text
Quay lưng rời nhà cổ, gương đồng hiện dấu bàn tay vẫy chào | Tiếng Gõ Đêm Ba Giờ P11
```

**YouTube Shorts — mô tả**

```text
Trước khi về phố, Lâm quay lại gian chính thu dọn hành lý bên chiếc gương đồng nay đã sáng bóng nắng mai. Đúng lúc anh quay lưng, trên mặt gương phía sau hiện lên dấu bàn tay vẫy chào. “Hãy yên nghỉ thanh thản nơi chín suối nhé cô Út, tạm biệt cô, tôi trở về thành phố đây.”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”
🎬 Xem trọn bộ 15 phút trên kênh YouTube.

#Shorts #tienggodembagio #phimma #truyenma
```

**Facebook Reels**

```text
Trước khi về phố, Lâm quay lại gian chính thu dọn hành lý bên chiếc gương đồng nay đã sáng bóng nắng mai. Đúng lúc anh quay lưng, trên mặt gương phía sau hiện lên dấu bàn tay vẫy chào. “Hãy yên nghỉ thanh thản nơi chín suối nhé cô Út, tạm biệt cô, tôi trở về thành phố đây.”

Cái kết này làm bạn sợ hay ấm lòng? 👇
🎬 Xem trọn bộ 15 phút trên kênh YouTube.
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong”

#TiengGoDemBaGio #PhimMa #TruyenMa #PhimNgan #ketphim #guongdong
```
