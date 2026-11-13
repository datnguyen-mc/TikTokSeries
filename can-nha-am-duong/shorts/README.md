# Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **các cảnh hay nhất** của phim ma 15 phút, không phải cả phim: **11 phần dọc 9:16**, mỗi phần là một khoảnh khắc trọn vẹn dài 30–60 giây (bí ẩn, hù dọa, cú lật), mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger, đăng nối tiếp theo thứ tự truyện như một series.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn đỏ máu “CĂN NHÀ ÂM DƯƠNG • PHẦN N” và câu hook ở trên khung phim (cụm nhấn màu vàng chanh); phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau, phần cuối đổi thành “XEM FULL PHIM”. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chính tả và tên riêng sửa theo kịch bản `PHAN_CANH_OMNI.json`. Câu Omni nói khác kịch bản thì phụ đề theo tiếng thật.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** mỗi đoạn dùng nguyên clip; khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm), câu Omni đọc lặp ở đuôi clip được cắt bỏ.
- **File:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; lịch đăng và caption TikTok, tiêu đề + mô tả YouTube, caption Facebook của mọi phần nằm trong `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py can-nha-am-duong            # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py can-nha-am-duong --only 4   # một phần
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py can-nha-am-duong --captions # chỉ caption + README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-tron-no-ve-nha-hoang.mp4`](01-tron-no-ve-nha-hoang.mp4) | Ôm nợ 400 triệu, trốn về căn nhà hoang của ông nội | 01.1, 01.2, 01.3, 01.4 | 38s | Thứ Bảy 14/11 – 11:00 |  |
| 2 | [`02-hoi-duong-ca-xom-bien-sac.mp4`](02-hoi-duong-ca-xom-bien-sac.mp4) | Hỏi đường về nhà ông nội, ai nghe cũng biến sắc | 02.3, 02.4, 02.5, 02.6 | 36s | Thứ Bảy 14/11 – 19:00 |  |
| 3 | [`03-xe-ruoc-dau-luc-ba-gio-sang.mp4`](03-xe-ruoc-dau-luc-ba-gio-sang.mp4) | Xe rước dâu lật trước cổng lúc 3 giờ sáng | 03.4, 03.5, 03.6 | 30s | Chủ Nhật 15/11 – 11:00 |  |
| 4 | [`04-vet-bam-nam-ngon-tay.mp4`](04-vet-bam-nam-ngon-tay.mp4) | Đêm đầu ngủ nhà hoang, sáng ra cổ tay hằn 5 ngón | 05.2, 05.3, 05.4, 05.5, 05.6 | 45s | Chủ Nhật 15/11 – 19:00 | ⭐ |
| 5 | [`05-bong-ma-xin-thuoc-la.mp4`](05-bong-ma-xin-thuoc-la.mp4) | Mời thuốc dưới gốc mít, gặp mặt không có con ngươi | 06.3, 06.4, 06.5, 06.6 | 32s | Thứ Hai 16/11 – 11:00 |  |
| 6 | [`06-hoi-tho-lanh-sau-gay.mp4`](06-hoi-tho-lanh-sau-gay.mp4) | Đèn tắt phụt, hơi thở lạnh buốt phả vào sau gáy | 07.2, 07.3, 07.4, 07.5, 07.6 | 40s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-ban-tay-xam-thoc-qua-man.mp4`](07-ban-tay-xam-thoc-qua-man.mp4) | 2 giờ 45 sáng, bàn tay xám ngoét thò qua màn | 08.2, 08.3, 08.4, 08.5, 08.6 | 41s | Thứ Ba 17/11 – 11:00 | ⭐ |
| 8 | [`08-vong-ong-noi-hien-ve.mp4`](08-vong-ong-noi-hien-ve.mp4) | Bóng ma trong góc nhà hóa ra là ông nội | 10.2, 10.3, 10.4, 10.5, 10.6 | 45s | Thứ Ba 17/11 – 19:00 | ⭐ |
| 9 | [`09-xin-bo-ngu-nha-ma.mp4`](09-xin-bo-ngu-nha-ma.mp4) | Con xin bố về ngủ nhà ma, bố giơ tay định đánh | 11.2, 11.3, 11.4, 11.5, 11.6 | 42s | Thứ Tư 18/11 – 11:00 |  |
| 10 | [`10-nguoi-cha-khoc-trong-mo.mp4`](10-nguoi-cha-khoc-trong-mo.mp4) | Ngủ một đêm ở nhà ma, người cha bật khóc trong mơ | 12.2, 12.3, 12.4, 12.5 | 35s | Thứ Tư 18/11 – 19:00 |  |
| 11 | [`11-loi-nhan-coi-am.mp4`](11-loi-nhan-coi-am.mp4) | Đêm trăng cuối, vong ông nội mỉm cười tan vào trăng | 15.2, 15.3, 15.4, 15.5, 15.6 | 42s | Thứ Năm 19/11 – 11:00 |  |

⭐ = 3 phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Căn Nhà Âm Dương”. Chọn ảnh bìa bằng khung hình có hook (giây đầu). Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả trong README này; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption; tắt “Tạo phụ đề tự động” vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00) từ 14/11, 3 nền tảng cùng giờ. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Ghi chú dựng

- Các đoạn đang dùng nguyên clip, chưa có `from`/`to`: xem bản dựng rồi tinh chỉnh điểm cắt trong plan nếu cần.
- `subtitle_replace` và `fixes` đang trống: điền sau khi xem bản Whisper (tên riêng nghe sai, chữ hay logo Omni tự vẽ vào khung).
- Đã đối chiếu bản Whisper (`shorts/_whisper/`) của mọi clip trong plan với kịch bản: thoại khớp. Nhiều clip VO đọc lặp cụm cuối câu (05.5, 06.4–06.6, 07.5, 08.2, 08.6, 10.2, 10.6, 11.4, 12.2); script tự cắt đoạn lặp ở đuôi clip.
- **02.5** (8,7 s): tiếng bị cắt, ông Bảy dừng ở “nhà ấy nặng âm khí”, mất cụm “có ma đấy!” của kịch bản (phần 2). **12.2**: nghe như Omni nói vấp “người đái người đàn ông” (phần 10). Cần nghe lại trước khi đăng.

## Caption từng phần (copy dán)

### Phần 1/11 — Ôm nợ 400 triệu, trốn về căn nhà hoang của ông nội

`01-tron-no-ve-nha-hoang.mp4` · 38s · cảnh 01.1, 01.2, 01.3, 01.4 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
Ôm món nợ hơn bốn trăm triệu, Bình bỏ trốn trong đêm về căn nhà hoang của ông nội. Mẹ gọi điện, giọng run run: “Bố mày vẫn chưa biết chuyện đâu, nhưng đám chủ nợ sắp tìm tới nhà rồi, mày về quê nội phải thật cẩn thận nhé!” Cậu đâu biết sau vụ tai nạn cướp đi sáu mạng người, căn nhà ấy đã thành nơi trú ngụ của ma quỷ.
Nợ ngập đầu, bạn có dám về ở căn nhà ấy không?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #tronno #nhahoang
```

**YouTube Shorts — tiêu đề** (78/100 ký tự)

```text
Ôm nợ 400 triệu, trốn về căn nhà hoang có ma của ông nội | Căn Nhà Âm Dương P1
```

**YouTube Shorts — mô tả**

```text
Ôm món nợ hơn bốn trăm triệu, Bình bỏ trốn trong đêm về căn nhà hoang của ông nội. Mẹ gọi điện, giọng run run: “Bố mày vẫn chưa biết chuyện đâu, nhưng đám chủ nợ sắp tìm tới nhà rồi, mày về quê nội phải thật cẩn thận nhé!” Cậu đâu biết sau vụ tai nạn cướp đi sáu mạng người, căn nhà ấy đã thành nơi trú ngụ của ma quỷ.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 2: Hỏi đường về nhà ông nội, ai nghe cũng biến sắc

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Ôm món nợ hơn bốn trăm triệu, Bình bỏ trốn trong đêm về căn nhà hoang của ông nội. Mẹ gọi điện, giọng run run: “Bố mày vẫn chưa biết chuyện đâu, nhưng đám chủ nợ sắp tìm tới nhà rồi, mày về quê nội phải thật cẩn thận nhé!” Cậu đâu biết sau vụ tai nạn cướp đi sáu mạng người, căn nhà ấy đã thành nơi trú ngụ của ma quỷ.

Nợ ngập đầu, bạn có dám về ở căn nhà ấy không? 👇
👉 Xem tiếp Phần 2: Hỏi đường về nhà ông nội, ai nghe cũng biến sắc
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #tronno #nhahoang
```

### Phần 2/11 — Hỏi đường về nhà ông nội, ai nghe cũng biến sắc

`02-hoi-duong-ca-xom-bien-sac.mp4` · 36s · cảnh 02.3, 02.4, 02.5, 02.6 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Bình định ẩn náu ở quê nội ít ngày, nhưng hỏi đường về nhà cụ Xá thì ai cũng biến sắc. Ông Bảy hàng xóm chỉ tay về cuối xóm: “Căn nhà cuối xóm có gốc mít cổ thụ ấy bỏ hoang hai mươi năm nay rồi cậu ơi, nhà ấy nặng âm khí…” Đứng trước cánh cổng sắt rỉ sét, một luồng khí lạnh thổi ra làm Bình rùng mình.
Hàng xóm cảnh báo thế, bạn còn dám bước qua cổng không?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #nhama #gocmit
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
Hỏi đường về nhà ông nội, cả xóm biến sắc: nhà ấy có ma | Căn Nhà Âm Dương P2
```

**YouTube Shorts — mô tả**

```text
Bình định ẩn náu ở quê nội ít ngày, nhưng hỏi đường về nhà cụ Xá thì ai cũng biến sắc. Ông Bảy hàng xóm chỉ tay về cuối xóm: “Căn nhà cuối xóm có gốc mít cổ thụ ấy bỏ hoang hai mươi năm nay rồi cậu ơi, nhà ấy nặng âm khí…” Đứng trước cánh cổng sắt rỉ sét, một luồng khí lạnh thổi ra làm Bình rùng mình.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 3: Xe rước dâu lật trước cổng lúc 3 giờ sáng

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Bình định ẩn náu ở quê nội ít ngày, nhưng hỏi đường về nhà cụ Xá thì ai cũng biến sắc. Ông Bảy hàng xóm chỉ tay về cuối xóm: “Căn nhà cuối xóm có gốc mít cổ thụ ấy bỏ hoang hai mươi năm nay rồi cậu ơi, nhà ấy nặng âm khí…” Đứng trước cánh cổng sắt rỉ sét, một luồng khí lạnh thổi ra làm Bình rùng mình.

Hàng xóm cảnh báo thế, bạn còn dám bước qua cổng không? 👇
👉 Xem tiếp Phần 3: Xe rước dâu lật trước cổng lúc 3 giờ sáng
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #nhama #gocmit
```

### Phần 3/11 — Xe rước dâu lật trước cổng lúc 3 giờ sáng

`03-xe-ruoc-dau-luc-ba-gio-sang.mp4` · 30s · cảnh 03.4, 03.5, 03.6 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Nghe chồng bảo mai cho Bình sang nhà hoang ở, vợ ông Bảy tái mặt kéo chồng ra góc hiên. Mười ba năm trước, đúng ba giờ sáng, chiếc xe rước dâu lật nhào trước cổng làm sáu người chết thảm. “Những oan hồn chết oan khuất không tìm được đường về đã kéo cả vào căn nhà bỏ không ấy trú ngụ suốt bao năm.”
Bạn có tin người chết oan sẽ ở lại nơi mình mất không?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #chuyenma #oanhon
```

**YouTube Shorts — tiêu đề** (87/100 ký tự)

```text
13 năm trước, xe rước dâu lật trước cổng nhà hoang lúc 3 giờ sáng | Căn Nhà Âm Dương P3
```

**YouTube Shorts — mô tả**

```text
Nghe chồng bảo mai cho Bình sang nhà hoang ở, vợ ông Bảy tái mặt kéo chồng ra góc hiên. Mười ba năm trước, đúng ba giờ sáng, chiếc xe rước dâu lật nhào trước cổng làm sáu người chết thảm. “Những oan hồn chết oan khuất không tìm được đường về đã kéo cả vào căn nhà bỏ không ấy trú ngụ suốt bao năm.”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 4: Đêm đầu ngủ nhà hoang, sáng ra cổ tay hằn 5 ngón

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Nghe chồng bảo mai cho Bình sang nhà hoang ở, vợ ông Bảy tái mặt kéo chồng ra góc hiên. Mười ba năm trước, đúng ba giờ sáng, chiếc xe rước dâu lật nhào trước cổng làm sáu người chết thảm. “Những oan hồn chết oan khuất không tìm được đường về đã kéo cả vào căn nhà bỏ không ấy trú ngụ suốt bao năm.”

Bạn có tin người chết oan sẽ ở lại nơi mình mất không? 👇
👉 Xem tiếp Phần 4: Đêm đầu ngủ nhà hoang, sáng ra cổ tay hằn 5 ngón
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #chuyenma #oanhon
```

### Phần 4/11 — Đêm đầu ngủ nhà hoang, sáng ra cổ tay hằn 5 ngón

`04-vet-bam-nam-ngon-tay.mp4` · 45s · cảnh 05.2, 05.3, 05.4, 05.5, 05.6 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Đêm đầu tiên ngủ một mình, ngay bên ngoài lớp màn mỏng có bóng người cao gầy lặng lẽ đi quanh giường. Bình hét lên: “Ai đó?! Bỏ ngay cái bàn tay lạnh buốt ấy ra khỏi người tôi, cứu tôi với…” Trời hửng sáng, cổ tay cậu hằn vết bầm tím đen năm ngón tay… bước ra nắng thì biến mất sạch trơn, nhưng trong góc tối cái bóng đen vẫn dõi theo.
Bạn đã bao giờ bị bóng đè như Bình chưa?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #bongde #nhama
```

**YouTube Shorts — tiêu đề** (82/100 ký tự)

```text
Đêm đầu ngủ nhà hoang, sáng ra cổ tay hằn vết bầm 5 ngón tay | Căn Nhà Âm Dương P4
```

**YouTube Shorts — mô tả**

```text
Đêm đầu tiên ngủ một mình, ngay bên ngoài lớp màn mỏng có bóng người cao gầy lặng lẽ đi quanh giường. Bình hét lên: “Ai đó?! Bỏ ngay cái bàn tay lạnh buốt ấy ra khỏi người tôi, cứu tôi với…” Trời hửng sáng, cổ tay cậu hằn vết bầm tím đen năm ngón tay… bước ra nắng thì biến mất sạch trơn, nhưng trong góc tối cái bóng đen vẫn dõi theo.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 5: Mời thuốc dưới gốc mít, gặp mặt không có con ngươi

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Đêm đầu tiên ngủ một mình, ngay bên ngoài lớp màn mỏng có bóng người cao gầy lặng lẽ đi quanh giường. Bình hét lên: “Ai đó?! Bỏ ngay cái bàn tay lạnh buốt ấy ra khỏi người tôi, cứu tôi với…” Trời hửng sáng, cổ tay cậu hằn vết bầm tím đen năm ngón tay… bước ra nắng thì biến mất sạch trơn, nhưng trong góc tối cái bóng đen vẫn dõi theo.

Bạn đã bao giờ bị bóng đè như Bình chưa? 👇
👉 Xem tiếp Phần 5: Mời thuốc dưới gốc mít, gặp mặt không có con ngươi
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #bongde #nhama
```

### Phần 5/11 — Mời thuốc dưới gốc mít, gặp mặt không có con ngươi

`05-bong-ma-xin-thuoc-la.mp4` · 32s · cảnh 06.3, 06.4, 06.5, 06.6 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
Bên bàn rượu quê, ông Bảy hạ giọng kể chuyện ông Tư gặp ma dưới gốc mít: “Đêm đó ông Tư đi về khuya bật lửa mời thuốc, hiện ra trước mặt ông là khuôn mặt trắng bệch không có con ngươi!” Thứ tà ma ấy nhoẻn miệng cười rồi tan vào thân cây, để lại bao thuốc lá trên rễ mít. Đêm khuya, Bình phải một mình bước qua đúng gốc mít ấy.
Gặp cảnh này giữa đêm, bạn chạy hay đứng im?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #gocmit #chuyenma
```

**YouTube Shorts — tiêu đề** (90/100 ký tự)

```text
Bật lửa mời thuốc dưới gốc mít, hiện ra khuôn mặt không có con ngươi | Căn Nhà Âm Dương P5
```

**YouTube Shorts — mô tả**

```text
Bên bàn rượu quê, ông Bảy hạ giọng kể chuyện ông Tư gặp ma dưới gốc mít: “Đêm đó ông Tư đi về khuya bật lửa mời thuốc, hiện ra trước mặt ông là khuôn mặt trắng bệch không có con ngươi!” Thứ tà ma ấy nhoẻn miệng cười rồi tan vào thân cây, để lại bao thuốc lá trên rễ mít. Đêm khuya, Bình phải một mình bước qua đúng gốc mít ấy.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 6: Đèn tắt phụt, hơi thở lạnh buốt phả vào sau gáy

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Bên bàn rượu quê, ông Bảy hạ giọng kể chuyện ông Tư gặp ma dưới gốc mít: “Đêm đó ông Tư đi về khuya bật lửa mời thuốc, hiện ra trước mặt ông là khuôn mặt trắng bệch không có con ngươi!” Thứ tà ma ấy nhoẻn miệng cười rồi tan vào thân cây, để lại bao thuốc lá trên rễ mít. Đêm khuya, Bình phải một mình bước qua đúng gốc mít ấy.

Gặp cảnh này giữa đêm, bạn chạy hay đứng im? 👇
👉 Xem tiếp Phần 6: Đèn tắt phụt, hơi thở lạnh buốt phả vào sau gáy
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #gocmit #chuyenma
```

### Phần 6/11 — Đèn tắt phụt, hơi thở lạnh buốt phả vào sau gáy

`06-hoi-tho-lanh-sau-gay.mp4` · 40s · cảnh 07.2, 07.3, 07.4, 07.5, 07.6 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Đêm thứ ba, chiếc xoong nhôm rơi loảng xoảng dưới bếp, Bình tự trấn an: “Chắc chỉ là con chuột thôi mà.” Vừa chạm tay vào chiếc đinh, bóng đèn nổ lách tách rồi tắt phụt, một luồng hơi thở lạnh như băng phả thẳng vào sau gáy. Đèn sáng lại, ngoài cửa sổ một bóng trắng lướt vụt qua chấn song…
Đến đây bạn còn tin là con chuột không?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #kinhdi #nhama
```

**YouTube Shorts — tiêu đề** (78/100 ký tự)

```text
Đèn tắt phụt, hơi thở lạnh buốt phả vào sau gáy giữa đêm | Căn Nhà Âm Dương P6
```

**YouTube Shorts — mô tả**

```text
Đêm thứ ba, chiếc xoong nhôm rơi loảng xoảng dưới bếp, Bình tự trấn an: “Chắc chỉ là con chuột thôi mà.” Vừa chạm tay vào chiếc đinh, bóng đèn nổ lách tách rồi tắt phụt, một luồng hơi thở lạnh như băng phả thẳng vào sau gáy. Đèn sáng lại, ngoài cửa sổ một bóng trắng lướt vụt qua chấn song…

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 7: 2 giờ 45 sáng, bàn tay xám ngoét thò qua màn

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Đêm thứ ba, chiếc xoong nhôm rơi loảng xoảng dưới bếp, Bình tự trấn an: “Chắc chỉ là con chuột thôi mà.” Vừa chạm tay vào chiếc đinh, bóng đèn nổ lách tách rồi tắt phụt, một luồng hơi thở lạnh như băng phả thẳng vào sau gáy. Đèn sáng lại, ngoài cửa sổ một bóng trắng lướt vụt qua chấn song…

Đến đây bạn còn tin là con chuột không? 👇
👉 Xem tiếp Phần 7: 2 giờ 45 sáng, bàn tay xám ngoét thò qua màn
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #kinhdi #nhama
```

### Phần 7/11 — 2 giờ 45 sáng, bàn tay xám ngoét thò qua màn

`07-ban-tay-xam-thoc-qua-man.mp4` · 41s · cảnh 08.2, 08.3, 08.4, 08.5, 08.6 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Đúng hai giờ bốn mươi lăm phút sáng, Bình choàng tỉnh vì cảm giác có kẻ đang nhìn sát mặt mình. Đáp lại cậu chỉ là im lặng chết chóc, rồi một bàn tay xám ngoét năm móng đen thò xuyên qua màn: “Đi đi, mày hãy cút khỏi căn nhà này ngay lập tức…” Sáng ra, vết bầm năm ngón trên cổ tay đã tím đen, không tan nữa.
Nếu là Bình, đêm mai bạn còn dám ở lại không?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #bongde #kinhdi
```

**YouTube Shorts — tiêu đề** (81/100 ký tự)

```text
2 giờ 45 sáng, bàn tay xác chết thò qua màn đuổi người sống | Căn Nhà Âm Dương P7
```

**YouTube Shorts — mô tả**

```text
Đúng hai giờ bốn mươi lăm phút sáng, Bình choàng tỉnh vì cảm giác có kẻ đang nhìn sát mặt mình. Đáp lại cậu chỉ là im lặng chết chóc, rồi một bàn tay xám ngoét năm móng đen thò xuyên qua màn: “Đi đi, mày hãy cút khỏi căn nhà này ngay lập tức…” Sáng ra, vết bầm năm ngón trên cổ tay đã tím đen, không tan nữa.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 8: Bóng ma trong góc nhà hóa ra là ông nội

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Đúng hai giờ bốn mươi lăm phút sáng, Bình choàng tỉnh vì cảm giác có kẻ đang nhìn sát mặt mình. Đáp lại cậu chỉ là im lặng chết chóc, rồi một bàn tay xám ngoét năm móng đen thò xuyên qua màn: “Đi đi, mày hãy cút khỏi căn nhà này ngay lập tức…” Sáng ra, vết bầm năm ngón trên cổ tay đã tím đen, không tan nữa.

Nếu là Bình, đêm mai bạn còn dám ở lại không? 👇
👉 Xem tiếp Phần 8: Bóng ma trong góc nhà hóa ra là ông nội
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #bongde #kinhdi
```

### Phần 8/11 — Bóng ma trong góc nhà hóa ra là ông nội

`08-vong-ong-noi-hien-ve.mp4` · 45s · cảnh 10.2, 10.3, 10.4, 10.5, 10.6 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Một giờ sáng đêm thứ năm, hơi thở Bình phả ra khói trắng, từ góc gian thờ cũ một bóng già hiện lên: “Bình đấy ư, đứa cháu nội đích tôn của ông đấy ư, con đừng sợ ông.” Ông kể ngày ông mất, bố Bình quên lễ rước vong, để hồn ông bơ vơ lạnh lẽo… và chính ông đã sai vong gốc mít vào dọa cháu.
Bạn có đoán ra ai sai con ma gốc mít từ đầu không?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #plottwist #ongnoi
```

**YouTube Shorts — tiêu đề** (82/100 ký tự)

```text
Bóng ma hiện trong góc nhà hóa ra là ông nội, cú lật khó tin | Căn Nhà Âm Dương P8
```

**YouTube Shorts — mô tả**

```text
Một giờ sáng đêm thứ năm, hơi thở Bình phả ra khói trắng, từ góc gian thờ cũ một bóng già hiện lên: “Bình đấy ư, đứa cháu nội đích tôn của ông đấy ư, con đừng sợ ông.” Ông kể ngày ông mất, bố Bình quên lễ rước vong, để hồn ông bơ vơ lạnh lẽo… và chính ông đã sai vong gốc mít vào dọa cháu.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 9: Con xin bố về ngủ nhà ma, bố giơ tay định đánh

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Một giờ sáng đêm thứ năm, hơi thở Bình phả ra khói trắng, từ góc gian thờ cũ một bóng già hiện lên: “Bình đấy ư, đứa cháu nội đích tôn của ông đấy ư, con đừng sợ ông.” Ông kể ngày ông mất, bố Bình quên lễ rước vong, để hồn ông bơ vơ lạnh lẽo… và chính ông đã sai vong gốc mít vào dọa cháu.

Bạn có đoán ra ai sai con ma gốc mít từ đầu không? 👇
👉 Xem tiếp Phần 9: Con xin bố về ngủ nhà ma, bố giơ tay định đánh
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #plottwist #ongnoi
```

### Phần 9/11 — Con xin bố về ngủ nhà ma, bố giơ tay định đánh

`09-xin-bo-ngu-nha-ma.mp4` · 42s · cảnh 11.2, 11.3, 11.4, 11.5, 11.6 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
Bình gọi cho bố, ông Quân gầm lên: “Thằng nghịch tử kia! Mày phá gia chi tử nợ bốn trăm triệu rồi còn dám lôi vong hồn ông nội ra lừa bố hả?!” Ngay chiều ấy ông về tới cổng, giơ tay định đánh, nhưng bàn tay khựng lại khi con trai quỳ xin bố ngủ lại căn nhà ấy một đêm.
Ông Quân có dám ngủ lại căn nhà ấy không?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #chacon #giadinh
```

**YouTube Shorts — tiêu đề** (90/100 ký tự)

```text
Nợ 400 triệu, con xin bố về ngủ nhà ma một đêm, bố giơ tay định đánh | Căn Nhà Âm Dương P9
```

**YouTube Shorts — mô tả**

```text
Bình gọi cho bố, ông Quân gầm lên: “Thằng nghịch tử kia! Mày phá gia chi tử nợ bốn trăm triệu rồi còn dám lôi vong hồn ông nội ra lừa bố hả?!” Ngay chiều ấy ông về tới cổng, giơ tay định đánh, nhưng bàn tay khựng lại khi con trai quỳ xin bố ngủ lại căn nhà ấy một đêm.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 10: Ngủ một đêm ở nhà ma, người cha bật khóc trong mơ

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Bình gọi cho bố, ông Quân gầm lên: “Thằng nghịch tử kia! Mày phá gia chi tử nợ bốn trăm triệu rồi còn dám lôi vong hồn ông nội ra lừa bố hả?!” Ngay chiều ấy ông về tới cổng, giơ tay định đánh, nhưng bàn tay khựng lại khi con trai quỳ xin bố ngủ lại căn nhà ấy một đêm.

Ông Quân có dám ngủ lại căn nhà ấy không? 👇
👉 Xem tiếp Phần 10: Ngủ một đêm ở nhà ma, người cha bật khóc trong mơ
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #chacon #giadinh
```

### Phần 10/11 — Ngủ một đêm ở nhà ma, người cha bật khóc trong mơ

`10-nguoi-cha-khoc-trong-mo.mp4` · 35s · cảnh 12.2, 12.3, 12.4, 12.5 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Giữa đêm không ai biết ông Quân mơ thấy gì, chỉ thấy người đàn ông sắt đá ấy bật khóc trong giấc ngủ. Tờ mờ sáng, ông một mình quỳ gục trước mộ cha, rồi cùng Bình khiêng tủ thờ mới về đặt giữa nhà: “Bố ơi con bất hiếu quá, bao năm để hồn bố lạnh lẽo nơi quê nhà, hôm nay con xin rước bố về gian thờ tổ!”
Bạn nghĩ đêm ấy ông Quân đã mơ thấy ai?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#cannhaamduong #phimma #truyenma #chuhieu #xucdong
```

**YouTube Shorts — tiêu đề** (79/100 ký tự)

```text
Ngủ một đêm ở nhà ma, người cha sắt đá bật khóc trong mơ | Căn Nhà Âm Dương P10
```

**YouTube Shorts — mô tả**

```text
Giữa đêm không ai biết ông Quân mơ thấy gì, chỉ thấy người đàn ông sắt đá ấy bật khóc trong giấc ngủ. Tờ mờ sáng, ông một mình quỳ gục trước mộ cha, rồi cùng Bình khiêng tủ thờ mới về đặt giữa nhà: “Bố ơi con bất hiếu quá, bao năm để hồn bố lạnh lẽo nơi quê nhà, hôm nay con xin rước bố về gian thờ tổ!”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
👉 Xem tiếp Phần 11: Đêm trăng cuối, vong ông nội mỉm cười tan vào trăng

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Giữa đêm không ai biết ông Quân mơ thấy gì, chỉ thấy người đàn ông sắt đá ấy bật khóc trong giấc ngủ. Tờ mờ sáng, ông một mình quỳ gục trước mộ cha, rồi cùng Bình khiêng tủ thờ mới về đặt giữa nhà: “Bố ơi con bất hiếu quá, bao năm để hồn bố lạnh lẽo nơi quê nhà, hôm nay con xin rước bố về gian thờ tổ!”

Bạn nghĩ đêm ấy ông Quân đã mơ thấy ai? 👇
👉 Xem tiếp Phần 11: Đêm trăng cuối, vong ông nội mỉm cười tan vào trăng
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #chuhieu #xucdong
```

### Phần 11/11 — Đêm trăng cuối, vong ông nội mỉm cười tan vào trăng

`11-loi-nhan-coi-am.mp4` · 42s · cảnh 15.2, 15.3, 15.4, 15.5, 15.6 · đăng Thứ Năm 19/11 – 11:00

**TikTok**

```text
Dưới ánh trăng rằm, vong hồn cụ Xá mỉm cười thanh thản rồi tan dần vào ánh trăng. “Sợi dây duy nhất có thể hóa giải mọi oán hờn giữa hai cõi âm dương, chính là chữ Hiếu và lòng thành kính từ tâm can.” Căn nhà ma năm nào giờ sáng ấm giữa cánh đồng quê, và đồng hồ đã điểm sang canh ba.
Lần gần nhất bạn thắp nén nhang cho ông bà là khi nào?

🎬 Xem trọn bộ 15 phút trên kênh YouTube.
#cannhaamduong #phimma #truyenma #chuhieu #amduong
```

**YouTube Shorts — tiêu đề** (82/100 ký tự)

```text
Vong ông nội mỉm cười tan vào ánh trăng, lời nhắn từ cõi âm | Căn Nhà Âm Dương P11
```

**YouTube Shorts — mô tả**

```text
Dưới ánh trăng rằm, vong hồn cụ Xá mỉm cười thanh thản rồi tan dần vào ánh trăng. “Sợi dây duy nhất có thể hóa giải mọi oán hờn giữa hai cõi âm dương, chính là chữ Hiếu và lòng thành kính từ tâm can.” Căn nhà ma năm nào giờ sáng ấm giữa cánh đồng quê, và đồng hồ đã điểm sang canh ba.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”
🎬 Xem trọn bộ 15 phút trên kênh YouTube.

#Shorts #cannhaamduong #phimma #truyenma
```

**Facebook Reels**

```text
Dưới ánh trăng rằm, vong hồn cụ Xá mỉm cười thanh thản rồi tan dần vào ánh trăng. “Sợi dây duy nhất có thể hóa giải mọi oán hờn giữa hai cõi âm dương, chính là chữ Hiếu và lòng thành kính từ tâm can.” Căn nhà ma năm nào giờ sáng ấm giữa cánh đồng quê, và đồng hồ đã điểm sang canh ba.

Lần gần nhất bạn thắp nén nhang cho ông bà là khi nào? 👇
🎬 Xem trọn bộ 15 phút trên kênh YouTube.
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít”

#CanNhaAmDuong #PhimMa #TruyenMa #PhimNgan #chuhieu #amduong
```
