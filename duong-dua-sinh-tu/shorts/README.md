# Đường Đua Sinh Tử: 10 Giây Tự Do — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **12 khoảnh khắc hay nhất** của phim 40 phút, không phải cả phim: đột kích xa lộ, đua 1/4 dặm, rượt đuổi, đối đầu, cú lật thân phận và cái kết. Mỗi phần là một mạch liền 50–60 giây (5–6 clip liên tiếp), mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger, đăng nối tiếp theo thứ tự truyện.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn cam “ĐƯỜNG ĐUA SINH TỬ • PHẦN N” và câu hook ở trên khung phim (cụm nhấn màu xanh neon); phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau, phần cuối đổi thành “XEM FULL PHIM”. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chính tả và tên người nói sửa theo kịch bản `PHAN_CANH_V3.json`. Câu Omni nói khác kịch bản thì phụ đề theo tiếng thật.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm); clip có đuôi nói lặp thì cắt trước đoạn lặp.
- **Đầu ra:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; lịch đăng và caption TikTok / YouTube / Facebook của mọi phần nằm trong `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py duong-dua-sinh-tu            # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py duong-dua-sinh-tu --only 3   # một phần
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py duong-dua-sinh-tu --captions # chỉ ghi lại README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-du-cap-thep-130-kmh.mp4`](01-du-cap-thep-130-kmh.mp4) | Đu cáp thép sang cabin xe tải đang chạy 130 km/h | 02.1, 02.2, 02.3, 02.4, 02.5 | 39s | Thứ Bảy 14/11 – 11:00 |  |
| 2 | [`02-toi-hau-thu-cua-micdo.mp4`](02-toi-hau-thu-cua-micdo.mp4) | Thủ lĩnh Micdo ra tối hậu thư, Tom thách lại | 09.1, 09.2, 09.3, 09.4, 09.5, 09.6 | 50s | Thứ Bảy 14/11 – 19:00 |  |
| 3 | [`03-xa-nos-bung-san-xe.mp4`](03-xa-nos-bung-san-xe.mp4) | Xả bình NOS thứ hai, bung sàn xe, thua một thân xe | 15.1, 15.2, 15.3, 15.4, 15.5, 15.6 | 51s | Chủ Nhật 15/11 – 11:00 | ⭐ |
| 4 | [`04-drift-180-do-giai-vay.mp4`](04-drift-180-do-giai-vay.mp4) | Xe bốc khói vẫn quay đầu drift 180 độ cứu Micdo | 17.1, 17.2, 17.3, 17.5, 17.6 | 41s | Chủ Nhật 15/11 – 19:00 |  |
| 5 | [`05-muoi-giay-tu-do.mp4`](05-muoi-giay-tu-do.mp4) | Chiếc xe 900 mã lực của cha và 10 giây tự do | 24.1, 24.2, 24.3, 24.4, 24.5, 24.6 | 52s | Thứ Hai 16/11 – 11:00 |  |
| 6 | [`06-nhan-mat-qua-kinh-xe.mp4`](06-nhan-mat-qua-kinh-xe.mp4) | Trùm Ny Tran nhận ra mặt Tom sau kính xe chỉ huy | 26.2, 26.3, 26.4, 26.5, 26.6 | 45s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-nos-giau-duoi-ghe.mp4`](07-nos-giau-duoi-ghe.mp4) | Dẫn trước cả đường đua, thua vì NOS giấu dưới ghế | 29.1, 29.2, 29.3, 29.4, 29.5, 29.6 | 50s | Thứ Ba 17/11 – 11:00 |  |
| 8 | [`08-thu-nhan-voi-ami.mp4`](08-thu-nhan-voi-ami.mp4) | Người yêu hỏi “anh là ai?”, anh thú nhận là cảnh sát chìm | 31.2, 31.3, 31.4, 31.5, 31.6 | 44s | Thứ Ba 17/11 – 19:00 |  |
| 9 | [`09-cat-cap-cuu-cevin.mp4`](09-cat-cap-cuu-cevin.mp4) | Giao vô lăng cho người yêu, nhoài người cắt cáp cứu bạn | 33.5, 33.6, 34.1, 34.2, 34.3, 34.4 | 50s | Thứ Tư 18/11 – 11:00 |  |
| 10 | [`10-ma-hieu-437.mp4`](10-ma-hieu-437.mp4) | Đọc mã 437 gọi cứu viện, lộ thân phận trước mặt Micdo | 35.2, 35.3, 35.4, 35.5, 35.6 | 42s | Thứ Tư 18/11 – 19:00 | ⭐ |
| 11 | [`11-cat-dau-tau-hoa.mp4`](11-cat-dau-tau-hoa.mp4) | Mười giây tự do: đua cắt đầu tàu hỏa | 39.1, 39.2, 39.3, 39.4, 39.5, 39.6 | 49s | Thứ Năm 19/11 – 11:00 | ⭐ |
| 12 | [`12-chia-khoa-con-xe-10-giay.mp4`](12-chia-khoa-con-xe-10-giay.mp4) | Cảnh sát chìm trao chìa khóa cho người mình phải bắt | 40.2, 40.3, 40.4, 40.5, 40.6 | 41s | Thứ Năm 19/11 – 19:00 |  |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Đường Đua Sinh Tử”. Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả ở dưới; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption; tắt phụ đề tự động vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00), 3 nền tảng cùng giờ, bắt đầu 14/11. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Cần kiểm tra trước khi đăng

- **Chưa duyệt bản Whisper:** `subtitle_replace` và `fixes` đang để trống. Sau lần dựng đầu, xem phụ đề và khung hình từng phần rồi bổ sung (tên riêng như Micdo, Ny Tran, Cevin, Seja, Verni dễ bị nghe sai; logo hay chữ Omni tự vẽ thì xoá bằng `fixes`).
- **Thoại có thể khác kịch bản:** lần sửa cuối của kịch bản V3 (03/11) đổi lời 19 clip; trong short có 02.3, 02.5 (phần 1) và 26.3 (phần 6). Phụ đề theo tiếng thật nên không sai; caption chỉ trích các câu không đổi.
- **Clip 9,5 giây:** 24.5 (phần 5), 33.5 (phần 9), 35.3 (phần 10), 40.2, 40.3, 40.6 (phần 12) ngắn hơn các clip 10 giây còn lại; xem lại có cụt thoại không.
- Hook, tiêu đề và caption không nhắc tên hãng xe thật; xe gọi theo màu (xe đỏ, xe xanh, xe cam, xe trắng) hoặc “xe cơ bắp 900 mã lực”.

## Caption từng phần (copy dán)

### Phần 1/12 — Đu cáp thép sang cabin xe tải đang chạy 130 km/h

`01-du-cap-thep-130-kmh.mp4` · 39s · cảnh 02.1, 02.2, 02.3, 02.4, 02.5 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
Giữa đêm trên xa lộ mười, Cevin phóng mũi cáp thép từ chiếc xe đen sang cabin xe đầu kéo đang chạy: “Giữ cứng một trăm ba mươi cây số, để tao khóa mũi cáp vô cabin nó!” Anh ta đu người qua khung cửa, leo vào tận buồng lái và giành tay lái của tài xế Verni.
Ở tốc độ đó, bạn có dám đu qua không?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #xalo #phimduaxe
```

**YouTube Shorts — tiêu đề** (71/100 ký tự)

```text
Đu cáp thép sang cabin xe tải đang chạy 130 km/h | Đường Đua Sinh Tử P1
```

**YouTube Shorts — mô tả**

```text
Giữa đêm trên xa lộ mười, Cevin phóng mũi cáp thép từ chiếc xe đen sang cabin xe đầu kéo đang chạy: “Giữ cứng một trăm ba mươi cây số, để tao khóa mũi cáp vô cabin nó!” Anh ta đu người qua khung cửa, leo vào tận buồng lái và giành tay lái của tài xế Verni.

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 2: Thủ lĩnh Micdo ra tối hậu thư, Tom thách lại

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Giữa đêm trên xa lộ mười, Cevin phóng mũi cáp thép từ chiếc xe đen sang cabin xe đầu kéo đang chạy: “Giữ cứng một trăm ba mươi cây số, để tao khóa mũi cáp vô cabin nó!” Anh ta đu người qua khung cửa, leo vào tận buồng lái và giành tay lái của tài xế Verni.

Ở tốc độ đó, bạn có dám đu qua không? 👇
👉 Xem tiếp Phần 2: Thủ lĩnh Micdo ra tối hậu thư, Tom thách lại
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #xalo #phimduaxe
```

### Phần 2/12 — Thủ lĩnh Micdo ra tối hậu thư, Tom thách lại

`02-toi-hau-thu-cua-micdo.mp4` · 50s · cảnh 09.1, 09.2, 09.3, 09.4, 09.5, 09.6 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Micdo bước xuống chiếc xe đỏ, chỉ một câu là Cevin lùi ngay về sau lưng. Anh cấm Tom, anh thợ máy của lão Ryh, bén mảng tới quán nhà Toto thêm lần nào nữa, nhưng Tom đáp lại: “Quán ăn là của anh, nhưng đường đua một phần tư dặm đêm nay không của riêng ai.”
Tom liều thật hay đã tính trước?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #micdo #doidau
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
Thủ lĩnh Micdo ra tối hậu thư, anh thợ máy thách lại một câu | Đường Đua Sinh Tử P2
```

**YouTube Shorts — mô tả**

```text
Micdo bước xuống chiếc xe đỏ, chỉ một câu là Cevin lùi ngay về sau lưng. Anh cấm Tom, anh thợ máy của lão Ryh, bén mảng tới quán nhà Toto thêm lần nào nữa, nhưng Tom đáp lại: “Quán ăn là của anh, nhưng đường đua một phần tư dặm đêm nay không của riêng ai.”

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 3: Xả bình NOS thứ hai, bung sàn xe, thua một thân xe

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Micdo bước xuống chiếc xe đỏ, chỉ một câu là Cevin lùi ngay về sau lưng. Anh cấm Tom, anh thợ máy của lão Ryh, bén mảng tới quán nhà Toto thêm lần nào nữa, nhưng Tom đáp lại: “Quán ăn là của anh, nhưng đường đua một phần tư dặm đêm nay không của riêng ai.”

Tom liều thật hay đã tính trước? 👇
👉 Xem tiếp Phần 3: Xả bình NOS thứ hai, bung sàn xe, thua một thân xe
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #micdo #doidau
```

### Phần 3/12 — Xả bình NOS thứ hai, bung sàn xe, thua một thân xe

`03-xa-nos-bung-san-xe.mp4` · 51s · cảnh 15.1, 15.2, 15.3, 15.4, 15.5, 15.6 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Trăm thước cuối, Tom xả nốt bình NOS thứ hai: sàn phụ bung chốt tóe lửa, chiếc xe đỏ của Micdo về trước đúng một thân xe. Micdo đòi chìa khóa theo luật chơi, nhưng Tom chỉ tay ra đầu đường: “Xe thuộc về anh theo đúng luật chơi, nhưng nghe tiếng còi hú khóa bốn ngả đường kìa!”
Bấm NOS sớm như Tom là liều hay dại?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #nos #duaxeduongpho
```

**YouTube Shorts — tiêu đề** (78/100 ký tự)

```text
Xả bình NOS thứ hai, bung sàn xe, thua đúng một thân xe | Đường Đua Sinh Tử P3
```

**YouTube Shorts — mô tả**

```text
Trăm thước cuối, Tom xả nốt bình NOS thứ hai: sàn phụ bung chốt tóe lửa, chiếc xe đỏ của Micdo về trước đúng một thân xe. Micdo đòi chìa khóa theo luật chơi, nhưng Tom chỉ tay ra đầu đường: “Xe thuộc về anh theo đúng luật chơi, nhưng nghe tiếng còi hú khóa bốn ngả đường kìa!”

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 4: Xe bốc khói vẫn quay đầu drift 180 độ cứu Micdo

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Trăm thước cuối, Tom xả nốt bình NOS thứ hai: sàn phụ bung chốt tóe lửa, chiếc xe đỏ của Micdo về trước đúng một thân xe. Micdo đòi chìa khóa theo luật chơi, nhưng Tom chỉ tay ra đầu đường: “Xe thuộc về anh theo đúng luật chơi, nhưng nghe tiếng còi hú khóa bốn ngả đường kìa!”

Bấm NOS sớm như Tom là liều hay dại? 👇
👉 Xem tiếp Phần 4: Xe bốc khói vẫn quay đầu drift 180 độ cứu Micdo
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #nos #duaxeduongpho
```

### Phần 4/12 — Xe bốc khói vẫn quay đầu drift 180 độ cứu Micdo

`04-drift-180-do-giai-vay.mp4` · 41s · cảnh 17.1, 17.2, 17.3, 17.5, 17.6 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Cảnh sát khóa kín con hẻm, Tom lái chiếc xe xanh còn bốc khói quay ngược vào, drift 180 độ mở cửa đón Micdo: “Nhảy lên ghế phụ ngay đi Micdo, trừ khi anh muốn bị giữ lại đồn đêm nay!” Lách qua khe thùng gỗ, vọt qua dốc sắt, cắt đuôi tuần tra… thì mười ánh đèn mô tô hiện ra phía trước.
Tom cứu Micdo vì nhiệm vụ hay vì thật lòng?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #drift #ruotduoi
```

**YouTube Shorts — tiêu đề** (86/100 ký tự)

```text
Xe bốc khói vẫn quay đầu drift 180 độ cứu đối thủ khỏi vòng vây | Đường Đua Sinh Tử P4
```

**YouTube Shorts — mô tả**

```text
Cảnh sát khóa kín con hẻm, Tom lái chiếc xe xanh còn bốc khói quay ngược vào, drift 180 độ mở cửa đón Micdo: “Nhảy lên ghế phụ ngay đi Micdo, trừ khi anh muốn bị giữ lại đồn đêm nay!” Lách qua khe thùng gỗ, vọt qua dốc sắt, cắt đuôi tuần tra… thì mười ánh đèn mô tô hiện ra phía trước.

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 5: Chiếc xe 900 mã lực của cha và 10 giây tự do

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Cảnh sát khóa kín con hẻm, Tom lái chiếc xe xanh còn bốc khói quay ngược vào, drift 180 độ mở cửa đón Micdo: “Nhảy lên ghế phụ ngay đi Micdo, trừ khi anh muốn bị giữ lại đồn đêm nay!” Lách qua khe thùng gỗ, vọt qua dốc sắt, cắt đuôi tuần tra… thì mười ánh đèn mô tô hiện ra phía trước.

Tom cứu Micdo vì nhiệm vụ hay vì thật lòng? 👇
👉 Xem tiếp Phần 5: Chiếc xe 900 mã lực của cha và 10 giây tự do
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #drift #ruotduoi
```

### Phần 5/12 — Chiếc xe 900 mã lực của cha và 10 giây tự do

`05-muoi-giay-tu-do.mp4` · 52s · cảnh 24.1, 24.2, 24.3, 24.4, 24.5, 24.6 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
Micdo dẫn Tom vào góc sâu gara, kéo tấm bạt phủ chiếc xe cơ bắp đời 1970 mà cha anh cùng anh dựng nên. Chín trăm mã lực, mạnh tới mức anh chưa từng dám cầm lái: “Bởi trong mười giây trên đường một phần tư dặm đó, con người ta mới thực sự tự do.”
Với bạn, 10 giây tự do là gì?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #xecobap #muoigiaytudo
```

**YouTube Shorts — tiêu đề** (80/100 ký tự)

```text
Chiếc xe 900 mã lực của cha, đến giờ anh vẫn chưa dám lái | Đường Đua Sinh Tử P5
```

**YouTube Shorts — mô tả**

```text
Micdo dẫn Tom vào góc sâu gara, kéo tấm bạt phủ chiếc xe cơ bắp đời 1970 mà cha anh cùng anh dựng nên. Chín trăm mã lực, mạnh tới mức anh chưa từng dám cầm lái: “Bởi trong mười giây trên đường một phần tư dặm đó, con người ta mới thực sự tự do.”

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 6: Trùm Ny Tran nhận ra mặt Tom sau kính xe chỉ huy

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Micdo dẫn Tom vào góc sâu gara, kéo tấm bạt phủ chiếc xe cơ bắp đời 1970 mà cha anh cùng anh dựng nên. Chín trăm mã lực, mạnh tới mức anh chưa từng dám cầm lái: “Bởi trong mười giây trên đường một phần tư dặm đó, con người ta mới thực sự tự do.”

Với bạn, 10 giây tự do là gì? 👇
👉 Xem tiếp Phần 6: Trùm Ny Tran nhận ra mặt Tom sau kính xe chỉ huy
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #xecobap #muoigiaytudo
```

### Phần 6/12 — Trùm Ny Tran nhận ra mặt Tom sau kính xe chỉ huy

`06-nhan-mat-qua-kinh-xe.mp4` · 45s · cảnh 26.2, 26.3, 26.4, 26.5, 26.6 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Cảnh sát kiểm tra dinh thự Ny Tran lúc rạng đông. Cửa kính chiếc xe chỉ huy hạ xuống, Ny Tran nhìn thấy Tom ngồi bên trong và thề bắt cả nhóm Toto trả giá: “Nhớ kỹ ánh mắt tao hôm nay đi Tom, món nợ này cả nhóm Toto phải trả gấp mười!”
Vỏ bọc của Tom còn giữ được bao lâu?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #nytran #canhsatchim
```

**YouTube Shorts — tiêu đề** (76/100 ký tự)

```text
Trùm băng mô tô nhận ra mặt cảnh sát chìm qua kính xe | Đường Đua Sinh Tử P6
```

**YouTube Shorts — mô tả**

```text
Cảnh sát kiểm tra dinh thự Ny Tran lúc rạng đông. Cửa kính chiếc xe chỉ huy hạ xuống, Ny Tran nhìn thấy Tom ngồi bên trong và thề bắt cả nhóm Toto trả giá: “Nhớ kỹ ánh mắt tao hôm nay đi Tom, món nợ này cả nhóm Toto phải trả gấp mười!”

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 7: Dẫn trước cả đường đua, thua vì NOS giấu dưới ghế

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Cảnh sát kiểm tra dinh thự Ny Tran lúc rạng đông. Cửa kính chiếc xe chỉ huy hạ xuống, Ny Tran nhìn thấy Tom ngồi bên trong và thề bắt cả nhóm Toto trả giá: “Nhớ kỹ ánh mắt tao hôm nay đi Tom, món nợ này cả nhóm Toto phải trả gấp mười!”

Vỏ bọc của Tom còn giữ được bao lâu? 👇
👉 Xem tiếp Phần 7: Dẫn trước cả đường đua, thua vì NOS giấu dưới ghế
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #nytran #canhsatchim
```

### Phần 7/12 — Dẫn trước cả đường đua, thua vì NOS giấu dưới ghế

`07-nos-giau-duoi-ghe.mp4` · 50s · cảnh 29.1, 29.2, 29.3, 29.4, 29.5, 29.6 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Seja lái chiếc xe trắng, kỷ vật của cha, dẫn trước suốt nửa đường đua giữa sa mạc. Tới những mét cuối, Ny Tran mở van hai bình khí giấu dưới ghế: “Tạm biệt kỷ vật của cha mày đi nhóc, hai bình khí ngầm dưới ghế tao mở van rồi!” Thua mất xe của cha, Seja hoảng loạn đạp ga bỏ chạy khỏi đường băng.
Thua kiểu này, Seja có nên giao xe không?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #seja #gianlan
```

**YouTube Shorts — tiêu đề** (88/100 ký tự)

```text
Dẫn trước cả đường đua, thua ở mét cuối vì bình NOS giấu dưới ghế | Đường Đua Sinh Tử P7
```

**YouTube Shorts — mô tả**

```text
Seja lái chiếc xe trắng, kỷ vật của cha, dẫn trước suốt nửa đường đua giữa sa mạc. Tới những mét cuối, Ny Tran mở van hai bình khí giấu dưới ghế: “Tạm biệt kỷ vật của cha mày đi nhóc, hai bình khí ngầm dưới ghế tao mở van rồi!” Thua mất xe của cha, Seja hoảng loạn đạp ga bỏ chạy khỏi đường băng.

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 8: Người yêu hỏi “anh là ai?”, anh thú nhận là cảnh sát chìm

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Seja lái chiếc xe trắng, kỷ vật của cha, dẫn trước suốt nửa đường đua giữa sa mạc. Tới những mét cuối, Ny Tran mở van hai bình khí giấu dưới ghế: “Tạm biệt kỷ vật của cha mày đi nhóc, hai bình khí ngầm dưới ghế tao mở van rồi!” Thua mất xe của cha, Seja hoảng loạn đạp ga bỏ chạy khỏi đường băng.

Thua kiểu này, Seja có nên giao xe không? 👇
👉 Xem tiếp Phần 8: Người yêu hỏi “anh là ai?”, anh thú nhận là cảnh sát chìm
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #seja #gianlan
```

### Phần 8/12 — Người yêu hỏi “anh là ai?”, anh thú nhận là cảnh sát chìm

`08-thu-nhan-voi-ami.mp4` · 44s · cảnh 31.2, 31.3, 31.4, 31.5, 31.6 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Ami đòi lao ra cao tốc giúp anh trai, Tom chặn lại và cảnh báo tài xế xe tải đã chuẩn bị chống trả. Nhìn chiếc bộ đàm trong tay anh, Ami chết lặng: “Sao anh biết rõ tên tài xế và cầm bộ đàm kia... rốt cuộc anh là ai hả Tom?” Tom thú nhận mình là cảnh sát chìm, rồi đưa cô lên chiếc xe cam đuổi theo.
Là Ami, bạn có tha thứ cho Tom không?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #thunhan #tinhyeu
```

**YouTube Shorts — tiêu đề** (88/100 ký tự)

```text
Người yêu hỏi “anh là ai?”, anh thợ máy thú nhận là cảnh sát chìm | Đường Đua Sinh Tử P8
```

**YouTube Shorts — mô tả**

```text
Ami đòi lao ra cao tốc giúp anh trai, Tom chặn lại và cảnh báo tài xế xe tải đã chuẩn bị chống trả. Nhìn chiếc bộ đàm trong tay anh, Ami chết lặng: “Sao anh biết rõ tên tài xế và cầm bộ đàm kia... rốt cuộc anh là ai hả Tom?” Tom thú nhận mình là cảnh sát chìm, rồi đưa cô lên chiếc xe cam đuổi theo.

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 9: Giao vô lăng cho người yêu, nhoài người cắt cáp cứu bạn

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Ami đòi lao ra cao tốc giúp anh trai, Tom chặn lại và cảnh báo tài xế xe tải đã chuẩn bị chống trả. Nhìn chiếc bộ đàm trong tay anh, Ami chết lặng: “Sao anh biết rõ tên tài xế và cầm bộ đàm kia... rốt cuộc anh là ai hả Tom?” Tom thú nhận mình là cảnh sát chìm, rồi đưa cô lên chiếc xe cam đuổi theo.

Là Ami, bạn có tha thứ cho Tom không? 👇
👉 Xem tiếp Phần 9: Giao vô lăng cho người yêu, nhoài người cắt cáp cứu bạn
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #thunhan #tinhyeu
```

### Phần 9/12 — Giao vô lăng cho người yêu, nhoài người cắt cáp cứu bạn

`09-cat-cap-cuu-cevin.mp4` · 50s · cảnh 33.5, 33.6, 34.1, 34.2, 34.3, 34.4 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
Cevin bị kẹt trên sợi cáp thép bên hông chiếc xe đầu kéo đang lao trên xa lộ sa mạc. Chiếc xe cam của Tom xé gió lao tới, Ami cầm lái giữ thẳng sát bánh xe tải: “Bánh xe đầu kéo sát ngay cửa kính rồi Tom ơi, em đang gồng hết sức giữ thẳng lái!” Tom nhô người qua nóc xe, bấm đứt sợi cáp và đỡ Cevin về xe.
Ami giữ lái như vậy có đáng nể không?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #ami #cuunguoi
```

**YouTube Shorts — tiêu đề** (94/100 ký tự)

```text
Giao vô lăng cho người yêu, nhoài người cắt cáp thép cứu bạn giữa xa lộ | Đường Đua Sinh Tử P9
```

**YouTube Shorts — mô tả**

```text
Cevin bị kẹt trên sợi cáp thép bên hông chiếc xe đầu kéo đang lao trên xa lộ sa mạc. Chiếc xe cam của Tom xé gió lao tới, Ami cầm lái giữ thẳng sát bánh xe tải: “Bánh xe đầu kéo sát ngay cửa kính rồi Tom ơi, em đang gồng hết sức giữ thẳng lái!” Tom nhô người qua nóc xe, bấm đứt sợi cáp và đỡ Cevin về xe.

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 10: Đọc mã 437 gọi cứu viện, lộ thân phận trước mặt Micdo

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Cevin bị kẹt trên sợi cáp thép bên hông chiếc xe đầu kéo đang lao trên xa lộ sa mạc. Chiếc xe cam của Tom xé gió lao tới, Ami cầm lái giữ thẳng sát bánh xe tải: “Bánh xe đầu kéo sát ngay cửa kính rồi Tom ơi, em đang gồng hết sức giữ thẳng lái!” Tom nhô người qua nóc xe, bấm đứt sợi cáp và đỡ Cevin về xe.

Ami giữ lái như vậy có đáng nể không? 👇
👉 Xem tiếp Phần 10: Đọc mã 437 gọi cứu viện, lộ thân phận trước mặt Micdo
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #ami #cuunguoi
```

### Phần 10/12 — Đọc mã 437 gọi cứu viện, lộ thân phận trước mặt Micdo

`10-ma-hieu-437.mp4` · 42s · cảnh 35.2, 35.3, 35.4, 35.5, 35.6 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Giữa sa mạc, Cevin kiệt sức, xe cấp cứu đường bộ không thể tới kịp. Tom chọn cách duy nhất: cầm bộ đàm đọc mã sĩ quan gọi trực thăng y tế, ngay trước mặt Micdo. “Sĩ quan bốn ba bảy sao... hóa ra người anh em ngồi chung bàn với tao là cảnh sát chìm?”
Nếu là Micdo, bạn sẽ làm gì với Tom?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #plottwist #canhsatchim
```

**YouTube Shorts — tiêu đề** (85/100 ký tự)

```text
Đọc mã 437 gọi trực thăng cứu bạn, lộ thân phận cảnh sát chìm | Đường Đua Sinh Tử P10
```

**YouTube Shorts — mô tả**

```text
Giữa sa mạc, Cevin kiệt sức, xe cấp cứu đường bộ không thể tới kịp. Tom chọn cách duy nhất: cầm bộ đàm đọc mã sĩ quan gọi trực thăng y tế, ngay trước mặt Micdo. “Sĩ quan bốn ba bảy sao... hóa ra người anh em ngồi chung bàn với tao là cảnh sát chìm?”

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 11: Mười giây tự do: đua cắt đầu tàu hỏa

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Giữa sa mạc, Cevin kiệt sức, xe cấp cứu đường bộ không thể tới kịp. Tom chọn cách duy nhất: cầm bộ đàm đọc mã sĩ quan gọi trực thăng y tế, ngay trước mặt Micdo. “Sĩ quan bốn ba bảy sao... hóa ra người anh em ngồi chung bàn với tao là cảnh sát chìm?”

Nếu là Micdo, bạn sẽ làm gì với Tom? 👇
👉 Xem tiếp Phần 11: Mười giây tự do: đua cắt đầu tàu hỏa
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #plottwist #canhsatchim
```

### Phần 11/12 — Mười giây tự do: đua cắt đầu tàu hỏa

`11-cat-dau-tau-hoa.mp4` · 49s · cảnh 39.1, 39.2, 39.3, 39.4, 39.5, 39.6 · đăng Thứ Năm 19/11 – 11:00

**TikTok**

```text
Một phần tư dặm cuối trước đường ray: chiếc xe cơ bắp 900 mã lực của Micdo bốc đầu, lao song song với chiếc xe cam của Tom, cả hai vọt qua đường ray chỉ một tích tắc trước mũi tàu. “Lướt qua mũi tàu hỏa trong một hơi thở, đây chính là mười giây tự do của đời tao!” Rồi một chiếc xe tải lao ra chắn ngang đường…
Đua kiểu này, bạn đứng về Tom hay Micdo?

👉 Phần 12 ở trang cá nhân, Follow để xem tiếp!
#duongduasinhtu #phimhanhdong #duaxe #tauhoa #muoigiaytudo
```

**YouTube Shorts — tiêu đề** (76/100 ký tự)

```text
Đua 1/4 dặm cuối, cắt đầu tàu hỏa trong một tích tắc | Đường Đua Sinh Tử P11
```

**YouTube Shorts — mô tả**

```text
Một phần tư dặm cuối trước đường ray: chiếc xe cơ bắp 900 mã lực của Micdo bốc đầu, lao song song với chiếc xe cam của Tom, cả hai vọt qua đường ray chỉ một tích tắc trước mũi tàu. “Lướt qua mũi tàu hỏa trong một hơi thở, đây chính là mười giây tự do của đời tao!” Rồi một chiếc xe tải lao ra chắn ngang đường…

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
👉 Xem tiếp Phần 12: Cảnh sát chìm trao chìa khóa cho người mình phải bắt

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Một phần tư dặm cuối trước đường ray: chiếc xe cơ bắp 900 mã lực của Micdo bốc đầu, lao song song với chiếc xe cam của Tom, cả hai vọt qua đường ray chỉ một tích tắc trước mũi tàu. “Lướt qua mũi tàu hỏa trong một hơi thở, đây chính là mười giây tự do của đời tao!” Rồi một chiếc xe tải lao ra chắn ngang đường…

Đua kiểu này, bạn đứng về Tom hay Micdo? 👇
👉 Xem tiếp Phần 12: Cảnh sát chìm trao chìa khóa cho người mình phải bắt
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #tauhoa #muoigiaytudo
```

### Phần 12/12 — Cảnh sát chìm trao chìa khóa cho người mình phải bắt

`12-chia-khoa-con-xe-10-giay.mp4` · 41s · cảnh 40.2, 40.3, 40.4, 40.5, 40.6 · đăng Thứ Năm 19/11 – 19:00

**TikTok**

```text
Tom dìu Micdo khỏi chiếc xe cơ bắp vừa xoay vòng bên lề, xe của trung sĩ Nese sắp tới đầu đường. Micdo chìa tay chờ bị đưa về đồn: “Cuộc đua khép lại rồi Sĩ quan Tom, đưa tôi về đồn hoàn thành nhiệm vụ của cậu đi.” Tom lại đặt vào tay anh chìa khóa chiếc xe cam để trả món nợ con xe mười giây, rồi một mình đứng lại.
Cái kết này làm bạn thỏa mãn chưa?

🎬 Xem trọn bộ 40 phút trên kênh YouTube.
#duongduasinhtu #phimhanhdong #duaxe #ketphim #anhem
```

**YouTube Shorts — tiêu đề** (79/100 ký tự)

```text
Cảnh sát chìm trao chìa khóa xe cho người mình phải bắt | Đường Đua Sinh Tử P12
```

**YouTube Shorts — mô tả**

```text
Tom dìu Micdo khỏi chiếc xe cơ bắp vừa xoay vòng bên lề, xe của trung sĩ Nese sắp tới đầu đường. Micdo chìa tay chờ bị đưa về đồn: “Cuộc đua khép lại rồi Sĩ quan Tom, đưa tôi về đồn hoàn thành nhiệm vụ của cậu đi.” Tom lại đặt vào tay anh chìa khóa chiếc xe cam để trả món nợ con xe mười giây, rồi một mình đứng lại.

🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”
🎬 Xem trọn bộ 40 phút trên kênh YouTube.

#Shorts #duongduasinhtu #phimhanhdong #duaxe
```

**Facebook Reels**

```text
Tom dìu Micdo khỏi chiếc xe cơ bắp vừa xoay vòng bên lề, xe của trung sĩ Nese sắp tới đầu đường. Micdo chìa tay chờ bị đưa về đồn: “Cuộc đua khép lại rồi Sĩ quan Tom, đưa tôi về đồn hoàn thành nhiệm vụ của cậu đi.” Tom lại đặt vào tay anh chìa khóa chiếc xe cam để trả món nợ con xe mười giây, rồi một mình đứng lại.

Cái kết này làm bạn thỏa mãn chưa? 👇
🎬 Xem trọn bộ 40 phút trên kênh YouTube.
🎬 Full phim 40 phút có trên kênh YouTube, tìm “Đường Đua Sinh Tử: 10 Giây Tự Do”

#DuongDuaSinhTu #PhimHanhDong #DuaXe #PhimNgan #ketphim #anhem
```
