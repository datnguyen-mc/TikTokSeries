# Hổ Phách: Ngược Dòng Tiền Sử — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Phim 22 phút (22 cảnh × 4 clip × 15 s) được cắt thành **12 phần dọc 9:16 từ những cảnh hay nhất**, theo đúng thứ tự truyện: la bàn hóa đá, cổng thời gian, kỷ băng hà, rừng than đá, thời khủng long. Phần cuối dừng trước đoạn kết để người xem tìm phim full.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 ở giữa, nền là chính cảnh đó làm mờ.
- **Chữ trên video:** nhãn hổ phách “HỔ PHÁCH NGƯỢC DÒNG TIỀN SỬ • PHẦN N”, câu hook phía trên khung phim, phụ đề khớp tiếng phía dưới. 2,5 giây cuối hook đổi thành “CÒN TIẾP » PHẦN N+1”.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chữ nghe nhầm sửa bằng `subtitle_replace`.
- **Âm thanh:** chuẩn hoá −14 LUFS.
- **Nguồn clip:** `clips/HoPhach_CanhNN_ClipN.mp4`, liên kết sang `output_videos/canh-NN/` để script đọc được (liên kết không vào git).
- **File:** video `NN-<slug>.mp4` nằm ngay trong `shorts/`; caption của mọi phần ở cuối README này.

Dựng lại:

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ho-phach-nguoc-dong-tien-su
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ho-phach-nguoc-dong-tien-su --only 4
```

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-la-ban-hoa-da-66-trieu-nam.mp4`](01-la-ban-hoa-da-66-trieu-nam.mp4) | La bàn hóa đá 66 triệu năm khắc tên cô ấy | 01.1, 01.2, 01.3, 01.4 | 57s | Chủ Nhật 15/11 – 12:00 | ⭐ |
| 2 | [`02-hoa-thach-that-tu-thoi-khung-long.mp4`](02-hoa-thach-that-tu-thoi-khung-long.mp4) | Kết quả chụp chiếu: la bàn là hóa thạch thật | 03.1, 03.2, 03.3 | 44s | Chủ Nhật 15/11 – 20:00 |  |
| 3 | [`03-ho-phach-mo-cong-thoi-gian.mp4`](03-ho-phach-mo-cong-thoi-gian.mp4) | Hổ phách tự sáng lên, mở cổng ra kỷ băng hà | 04.1, 04.2, 04.3 | 43s | Thứ Hai 16/11 – 12:00 | ⭐ |
| 4 | [`04-bao-tuyet-va-dan-voi-ma-mut.mp4`](04-bao-tuyet-va-dan-voi-ma-mut.mp4) | Bão tuyết và cả đàn voi ma mút lao tới | 06.2, 06.3, 06.4 | 41s | Thứ Hai 16/11 – 20:00 | ⭐ |
| 5 | [`05-sap-chet-cong-va-bo-ba-thuy.mp4`](05-sap-chet-cong-va-bo-ba-thuy.mp4) | Sắp chết cóng, cứu mạng bằng một con bọ ba thùy | 07.2, 07.3, 07.4 | 41s | Thứ Ba 17/11 – 12:00 |  |
| 6 | [`06-chuon-chuon-khong-lo-ky-than-da.mp4`](06-chuon-chuon-khong-lo-ky-than-da.mp4) | Chuồn chuồn to bằng cái diều đậu lên mũ anh | 11.2, 11.3, 11.4 | 42s | Thứ Ba 17/11 – 20:00 |  |
| 7 | [`07-con-ret-dai-bang-xe-may.mp4`](07-con-ret-dai-bang-xe-may.mp4) | Con rết dài bằng xe máy bò qua chân anh | 12.2, 12.3, 12.4 | 44s | Thứ Tư 18/11 – 12:00 | ⭐ |
| 8 | [`08-chay-rung-vet-nut-thu-tam.mp4`](08-chay-rung-vet-nut-thu-tam.mp4) | Rừng cháy rực, viên hổ phách chỉ còn một lần | 14.1, 14.2, 14.3, 14.4 | 56s | Thứ Tư 18/11 – 20:00 |  |
| 9 | [`09-dung-giua-dan-khung-long.mp4`](09-dung-giua-dan-khung-long.mp4) | Đứng giữa đàn khủng long, ngay bãi khai quật | 15.1, 15.2, 15.3 | 43s | Thứ Năm 19/11 – 12:00 |  |
| 10 | [`10-hoa-thach-nam-2026.mp4`](10-hoa-thach-nam-2026.mp4) | Kẹt ở thời khủng long, cần một hóa thạch năm 2026 | 16.3, 16.4, 17.1, 17.2 | 56s | Thứ Năm 19/11 – 20:00 |  |
| 11 | [`11-tarbosaurus-danh-hoi.mp4`](11-tarbosaurus-danh-hoi.mp4) | Tarbosaurus đánh hơi ngay trên đầu hai người | 18.2, 18.3, 18.4 | 44s | Thứ Sáu 20/11 – 12:00 | ⭐ |
| 12 | [`12-tha-drone-mat-ca-kenh.mp4`](12-tha-drone-mat-ca-kenh.mp4) | Thả drone dụ khủng long, mất 3 năm video | 19.1, 19.2, 19.3 | 42s | Thứ Sáu 20/11 – 20:00 | ⭐ |

⭐ = phần có hook mạnh nhất, nên dồn tương tác trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Hổ Phách”. Mỗi caption có đúng 5 hashtag.
- **YouTube Shorts:** dán tiêu đề + mô tả; khi phim full đã lên kênh, điền link vào `full_movie_url` rồi chạy lại với `--captions`.
- **Facebook Reels:** dán caption, bật phụ đề tự động tắt (phụ đề đã in sẵn trên video).

## Ghi chú biên tập

- Không dùng 7 clip có tiếng thoại không rõ chữ (Whisper chỉ ra chữ vô nghĩa): 04.4, 08.4, 09.1, 09.3, 11.1, 13.1, 18.1.
- Không dùng cảnh 20–22 (trở về hiện tại, drone hóa đá) để không lộ kết phim.

## Caption từng phần (copy dán)

### Phần 1/12 — La bàn hóa đá 66 triệu năm khắc tên cô ấy

`01-la-ban-hoa-da-66-trieu-nam.mp4` · 57s · cảnh 01.1, 01.2, 01.3, 01.4 · đăng Chủ Nhật 15/11 – 12:00

**TikTok**

```text
Trong lớp tro núi lửa 66 triệu năm, đội khai quật đào được một chiếc la bàn bằng đồng đã hóa đá hoàn toàn. Trên nắp khắc “Gửi Linh, bố”… trong khi chiếc la bàn của bố vẫn đang đeo trên cổ Linh.
Nếu là Linh, bạn sẽ giải thích chuyện này thế nào?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #khaoco #bian
```

**YouTube Shorts — tiêu đề** (73/100 ký tự)

```text
Đào được la bàn hóa đá 66 triệu năm, trên nắp khắc tên mình | Hổ Phách P1
```

**YouTube Shorts — mô tả**

```text
Trong lớp tro núi lửa 66 triệu năm, đội khai quật đào được một chiếc la bàn bằng đồng đã hóa đá hoàn toàn. Trên nắp khắc “Gửi Linh, bố”… trong khi chiếc la bàn của bố vẫn đang đeo trên cổ Linh.

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 2: Kết quả chụp chiếu: la bàn là hóa thạch thật

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Trong lớp tro núi lửa 66 triệu năm, đội khai quật đào được một chiếc la bàn bằng đồng đã hóa đá hoàn toàn. Trên nắp khắc “Gửi Linh, bố”… trong khi chiếc la bàn của bố vẫn đang đeo trên cổ Linh.

Nếu là Linh, bạn sẽ giải thích chuyện này thế nào? 👇
👉 Xem tiếp Phần 2: Kết quả chụp chiếu: la bàn là hóa thạch thật
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #khaoco #bian
```

### Phần 2/12 — Kết quả chụp chiếu: la bàn là hóa thạch thật

`02-hoa-thach-that-tu-thoi-khung-long.mp4` · 44s · cảnh 03.1, 03.2, 03.3 · đăng Chủ Nhật 15/11 – 20:00

**TikTok**

```text
Viên hổ phách nằm cạnh la bàn có bốn vết rạn, bên trong như có ánh sáng bị nhốt lại. Kết quả chụp chiếu khiến Linh lạnh người: đồng đã biến thành khoáng chất, chiếc la bàn là hóa thạch thật. “Hóa thạch là lá thư mà quá khứ gửi cho tương lai.”
Theo bạn ai đã mang chiếc la bàn về thời khủng long?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #hoathach #bian
```

**YouTube Shorts — tiêu đề** (71/100 ký tự)

```text
La bàn của bố hóa ra là hóa thạch thật từ thời khủng long | Hổ Phách P2
```

**YouTube Shorts — mô tả**

```text
Viên hổ phách nằm cạnh la bàn có bốn vết rạn, bên trong như có ánh sáng bị nhốt lại. Kết quả chụp chiếu khiến Linh lạnh người: đồng đã biến thành khoáng chất, chiếc la bàn là hóa thạch thật. “Hóa thạch là lá thư mà quá khứ gửi cho tương lai.”

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 3: Hổ phách tự sáng lên, mở cổng ra kỷ băng hà

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Viên hổ phách nằm cạnh la bàn có bốn vết rạn, bên trong như có ánh sáng bị nhốt lại. Kết quả chụp chiếu khiến Linh lạnh người: đồng đã biến thành khoáng chất, chiếc la bàn là hóa thạch thật. “Hóa thạch là lá thư mà quá khứ gửi cho tương lai.”

Theo bạn ai đã mang chiếc la bàn về thời khủng long? 👇
👉 Xem tiếp Phần 3: Hổ phách tự sáng lên, mở cổng ra kỷ băng hà
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #hoathach #bian
```

### Phần 3/12 — Hổ phách tự sáng lên, mở cổng ra kỷ băng hà

`03-ho-phach-mo-cong-thoi-gian.mp4` · 43s · cảnh 04.1, 04.2, 04.3 · đăng Thứ Hai 16/11 – 12:00

**TikTok**

```text
Duy lén bay drone trong phòng thí nghiệm thì viên hổ phách tự sáng lên. Nắng xuyên qua nó thành một vòng tròn vàng trên sàn, rồi vòng sáng to dần… và tuyết bắt đầu bay ra. “Anh hứa không bước vào đâu! Thật đấy!”
Bạn có dám bước vào vòng sáng đó không?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #xuyenkhong #kybangha
```

**YouTube Shorts — tiêu đề** (75/100 ký tự)

```text
Viên hổ phách tự sáng lên, tuyết bay ra từ vòng tròn trên sàn | Hổ Phách P3
```

**YouTube Shorts — mô tả**

```text
Duy lén bay drone trong phòng thí nghiệm thì viên hổ phách tự sáng lên. Nắng xuyên qua nó thành một vòng tròn vàng trên sàn, rồi vòng sáng to dần… và tuyết bắt đầu bay ra. “Anh hứa không bước vào đâu! Thật đấy!”

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 4: Bão tuyết và cả đàn voi ma mút lao tới

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Duy lén bay drone trong phòng thí nghiệm thì viên hổ phách tự sáng lên. Nắng xuyên qua nó thành một vòng tròn vàng trên sàn, rồi vòng sáng to dần… và tuyết bắt đầu bay ra. “Anh hứa không bước vào đâu! Thật đấy!”

Bạn có dám bước vào vòng sáng đó không? 👇
👉 Xem tiếp Phần 4: Bão tuyết và cả đàn voi ma mút lao tới
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #xuyenkhong #kybangha
```

### Phần 4/12 — Bão tuyết và cả đàn voi ma mút lao tới

`04-bao-tuyet-va-dan-voi-ma-mut.mp4` · 41s · cảnh 06.2, 06.3, 06.4 · đăng Thứ Hai 16/11 – 20:00

**TikTok**

```text
Giữa thảo nguyên băng, bão tuyết ập đến nhanh hơn ngựa phi, và đàn voi ma mút đang chạy thẳng về phía hai người. Linh hét: “Ra sau tảng đá kia ngay! Voi chạy theo bầy sẽ tự rẽ vòng quanh vật cản!” Chúng rẽ thật… nhưng mặt trời vừa bị mây nuốt mất.
Bạn sẽ chạy hay nấp sau tảng đá?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #voimamut #sinhton
```

**YouTube Shorts — tiêu đề** (66/100 ký tự)

```text
Bão tuyết sau lưng, đàn voi ma mút lao tới trước mặt | Hổ Phách P4
```

**YouTube Shorts — mô tả**

```text
Giữa thảo nguyên băng, bão tuyết ập đến nhanh hơn ngựa phi, và đàn voi ma mút đang chạy thẳng về phía hai người. Linh hét: “Ra sau tảng đá kia ngay! Voi chạy theo bầy sẽ tự rẽ vòng quanh vật cản!” Chúng rẽ thật… nhưng mặt trời vừa bị mây nuốt mất.

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 5: Sắp chết cóng, cứu mạng bằng một con bọ ba thùy

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Giữa thảo nguyên băng, bão tuyết ập đến nhanh hơn ngựa phi, và đàn voi ma mút đang chạy thẳng về phía hai người. Linh hét: “Ra sau tảng đá kia ngay! Voi chạy theo bầy sẽ tự rẽ vòng quanh vật cản!” Chúng rẽ thật… nhưng mặt trời vừa bị mây nuốt mất.

Bạn sẽ chạy hay nấp sau tảng đá? 👇
👉 Xem tiếp Phần 5: Sắp chết cóng, cứu mạng bằng một con bọ ba thùy
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #voimamut #sinhton
```

### Phần 5/12 — Sắp chết cóng, cứu mạng bằng một con bọ ba thùy

`05-sap-chet-cong-va-bo-ba-thuy.mp4` · 41s · cảnh 07.2, 07.3, 07.4 · đăng Thứ Ba 17/11 – 12:00

**TikTok**

```text
Đang tê cóng giữa bão tuyết thì một khe nắng mở ra. Hổ phách phải chạm vào hóa thạch mới mở cổng, và thứ duy nhất trong túi Linh là một con bọ ba thùy 500 triệu năm tuổi. “Duy ơi, nếu bên kia không có không khí để thở thì sao?”
Bạn sẽ nhảy vào cổng khi chưa biết bên kia là gì chứ?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #xuyenkhong #sinhton
```

**YouTube Shorts — tiêu đề** (72/100 ký tự)

```text
Sắp chết cóng, mở cổng thời gian bằng hóa thạch bọ ba thùy | Hổ Phách P5
```

**YouTube Shorts — mô tả**

```text
Đang tê cóng giữa bão tuyết thì một khe nắng mở ra. Hổ phách phải chạm vào hóa thạch mới mở cổng, và thứ duy nhất trong túi Linh là một con bọ ba thùy 500 triệu năm tuổi. “Duy ơi, nếu bên kia không có không khí để thở thì sao?”

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 6: Chuồn chuồn to bằng cái diều đậu lên mũ anh

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Đang tê cóng giữa bão tuyết thì một khe nắng mở ra. Hổ phách phải chạm vào hóa thạch mới mở cổng, và thứ duy nhất trong túi Linh là một con bọ ba thùy 500 triệu năm tuổi. “Duy ơi, nếu bên kia không có không khí để thở thì sao?”

Bạn sẽ nhảy vào cổng khi chưa biết bên kia là gì chứ? 👇
👉 Xem tiếp Phần 6: Chuồn chuồn to bằng cái diều đậu lên mũ anh
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #xuyenkhong #sinhton
```

### Phần 6/12 — Chuồn chuồn to bằng cái diều đậu lên mũ anh

`06-chuon-chuon-khong-lo-ky-than-da.mp4` · 42s · cảnh 11.2, 11.3, 11.4 · đăng Thứ Ba 17/11 – 20:00

**TikTok**

```text
Giữa rừng than đá 300 triệu năm, một con chuồn chuồn Meganeura sải cánh gần một mét nhìn chằm chằm vào Duy rồi đậu lên mũ anh. Và lần đầu tiên từ hôm qua, Linh bật cười.
Bạn có dám đứng yên khi con chuồn chuồn này đậu lên đầu không?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #tiensu #khoahoc
```

**YouTube Shorts — tiêu đề** (64/100 ký tự)

```text
Chuồn chuồn khổng lồ sải cánh 1 mét đậu lên mũ anh | Hổ Phách P6
```

**YouTube Shorts — mô tả**

```text
Giữa rừng than đá 300 triệu năm, một con chuồn chuồn Meganeura sải cánh gần một mét nhìn chằm chằm vào Duy rồi đậu lên mũ anh. Và lần đầu tiên từ hôm qua, Linh bật cười.

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 7: Con rết dài bằng xe máy bò qua chân anh

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Giữa rừng than đá 300 triệu năm, một con chuồn chuồn Meganeura sải cánh gần một mét nhìn chằm chằm vào Duy rồi đậu lên mũ anh. Và lần đầu tiên từ hôm qua, Linh bật cười.

Bạn có dám đứng yên khi con chuồn chuồn này đậu lên đầu không? 👇
👉 Xem tiếp Phần 7: Con rết dài bằng xe máy bò qua chân anh
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #tiensu #khoahoc
```

### Phần 7/12 — Con rết dài bằng xe máy bò qua chân anh

`07-con-ret-dai-bang-xe-may.mp4` · 44s · cảnh 12.2, 12.3, 12.4 · đăng Thứ Tư 18/11 – 12:00

**TikTok**

```text
Trên thân cây đổ bắc qua đầm, một con rết Arthropleura dài bằng cả chiếc xe máy bò sang. “Chân của nó còn nhiều hơn cả số người xem kênh anh!” Duy nép sát, thở đều… và hàng trăm cái chân bò qua chân anh.
Gặp con rết này bạn đứng yên nổi không?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #tiensu #rungrom
```

**YouTube Shorts — tiêu đề** (62/100 ký tự)

```text
Con rết khổng lồ dài bằng xe máy bò qua chân anh | Hổ Phách P7
```

**YouTube Shorts — mô tả**

```text
Trên thân cây đổ bắc qua đầm, một con rết Arthropleura dài bằng cả chiếc xe máy bò sang. “Chân của nó còn nhiều hơn cả số người xem kênh anh!” Duy nép sát, thở đều… và hàng trăm cái chân bò qua chân anh.

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 8: Rừng cháy rực, viên hổ phách chỉ còn một lần

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Trên thân cây đổ bắc qua đầm, một con rết Arthropleura dài bằng cả chiếc xe máy bò sang. “Chân của nó còn nhiều hơn cả số người xem kênh anh!” Duy nép sát, thở đều… và hàng trăm cái chân bò qua chân anh.

Gặp con rết này bạn đứng yên nổi không? 👇
👉 Xem tiếp Phần 8: Rừng cháy rực, viên hổ phách chỉ còn một lần
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #tiensu #rungrom
```

### Phần 8/12 — Rừng cháy rực, viên hổ phách chỉ còn một lần

`08-chay-rung-vet-nut-thu-tam.mp4` · 56s · cảnh 14.1, 14.2, 14.3, 14.4 · đăng Thứ Tư 18/11 – 20:00

**TikTok**

```text
Sét đánh trúng cây, khí oxy dày đặc khiến lửa chạy nhanh như nước. Hết sạch hóa thạch, Linh chỉ còn chiếc la bàn của bố. Vết nứt thứ tám xuất hiện: viên đá chỉ còn chịu được đúng một lần nữa. “Bố ơi, con đang đến chỗ của bố đây.”
Bạn nghĩ cánh cổng lần này sẽ đưa họ tới đâu?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #chayrung #xuyenkhong
```

**YouTube Shorts — tiêu đề** (68/100 ký tự)

```text
Rừng cháy rực, viên hổ phách chỉ còn dùng được một lần | Hổ Phách P8
```

**YouTube Shorts — mô tả**

```text
Sét đánh trúng cây, khí oxy dày đặc khiến lửa chạy nhanh như nước. Hết sạch hóa thạch, Linh chỉ còn chiếc la bàn của bố. Vết nứt thứ tám xuất hiện: viên đá chỉ còn chịu được đúng một lần nữa. “Bố ơi, con đang đến chỗ của bố đây.”

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 9: Đứng giữa đàn khủng long, ngay bãi khai quật

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Sét đánh trúng cây, khí oxy dày đặc khiến lửa chạy nhanh như nước. Hết sạch hóa thạch, Linh chỉ còn chiếc la bàn của bố. Vết nứt thứ tám xuất hiện: viên đá chỉ còn chịu được đúng một lần nữa. “Bố ơi, con đang đến chỗ của bố đây.”

Bạn nghĩ cánh cổng lần này sẽ đưa họ tới đâu? 👇
👉 Xem tiếp Phần 9: Đứng giữa đàn khủng long, ngay bãi khai quật
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #chayrung #xuyenkhong
```

### Phần 9/12 — Đứng giữa đàn khủng long, ngay bãi khai quật

`09-dung-giua-dan-khung-long.mp4` · 43s · cảnh 15.1, 15.2, 15.3 · đăng Thứ Năm 19/11 – 12:00

**TikTok**

```text
Mặt đất rung lên, những chiếc cổ dài như cần cẩu vươn qua tán lá. “Ngoài đời chúng còn đẹp hơn trong phim nhiều.” Rồi Linh nhận ra khúc sông bên dưới: họ đang đứng đúng chỗ cô Hạnh ngồi đào hôm qua.
Bạn muốn tận mắt thấy loài khủng long nào nhất?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #khunglong #tiensu
```

**YouTube Shorts — tiêu đề** (69/100 ký tự)

```text
Ngẩng lên thật chậm: cả đàn khủng long cổ dài trước mặt | Hổ Phách P9
```

**YouTube Shorts — mô tả**

```text
Mặt đất rung lên, những chiếc cổ dài như cần cẩu vươn qua tán lá. “Ngoài đời chúng còn đẹp hơn trong phim nhiều.” Rồi Linh nhận ra khúc sông bên dưới: họ đang đứng đúng chỗ cô Hạnh ngồi đào hôm qua.

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 10: Kẹt ở thời khủng long, cần một hóa thạch năm 2026

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Mặt đất rung lên, những chiếc cổ dài như cần cẩu vươn qua tán lá. “Ngoài đời chúng còn đẹp hơn trong phim nhiều.” Rồi Linh nhận ra khúc sông bên dưới: họ đang đứng đúng chỗ cô Hạnh ngồi đào hôm qua.

Bạn muốn tận mắt thấy loài khủng long nào nhất? 👇
👉 Xem tiếp Phần 10: Kẹt ở thời khủng long, cần một hóa thạch năm 2026
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #khunglong #tiensu
```

### Phần 10/12 — Kẹt ở thời khủng long, cần một hóa thạch năm 2026

`10-hoa-thach-nam-2026.mp4` · 56s · cảnh 16.3, 16.4, 17.1, 17.2 · đăng Thứ Năm 19/11 – 20:00

**TikTok**

```text
Muốn về nhà phải có một hóa thạch của năm 2026, mà chẳng có gì kịp hóa đá trong vài ngày. Đúng lúc Linh xin lỗi vì kéo Duy vào chuyện này, anh lôi ra bàn tay in thạch cao. “Nói ra cái câu mà em ghét nhất trên đời đi.”
Bạn có đoán ra lời giải trước khi Duy nói không?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #khunglong #hoathach
```

**YouTube Shorts — tiêu đề** (70/100 ký tự)

```text
Kẹt lại thời khủng long, cần một hóa thạch của năm 2026 | Hổ Phách P10
```

**YouTube Shorts — mô tả**

```text
Muốn về nhà phải có một hóa thạch của năm 2026, mà chẳng có gì kịp hóa đá trong vài ngày. Đúng lúc Linh xin lỗi vì kéo Duy vào chuyện này, anh lôi ra bàn tay in thạch cao. “Nói ra cái câu mà em ghét nhất trên đời đi.”

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 11: Tarbosaurus đánh hơi ngay trên đầu hai người

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Muốn về nhà phải có một hóa thạch của năm 2026, mà chẳng có gì kịp hóa đá trong vài ngày. Đúng lúc Linh xin lỗi vì kéo Duy vào chuyện này, anh lôi ra bàn tay in thạch cao. “Nói ra cái câu mà em ghét nhất trên đời đi.”

Bạn có đoán ra lời giải trước khi Duy nói không? 👇
👉 Xem tiếp Phần 11: Tarbosaurus đánh hơi ngay trên đầu hai người
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #khunglong #hoathach
```

### Phần 11/12 — Tarbosaurus đánh hơi ngay trên đầu hai người

`11-tarbosaurus-danh-hoi.mp4` · 44s · cảnh 18.2, 18.3, 18.4 · đăng Thứ Sáu 20/11 – 12:00

**TikTok**

```text
Tarbosaurus, họ hàng châu Á của khủng long bạo chúa, đứng chắn giữa hai người và bãi trống. “Đừng nhúc nhích gì cả. Mắt nó nhìn vật chuyển động giỏi hơn vật đứng yên.” Duy nghĩ ra một cách, nhưng phải đánh đổi thứ đáng tiền nhất của anh.
Bạn sẽ hy sinh thứ gì để thoát thân?

👉 Phần 12 ở trang cá nhân, Follow để xem tiếp!
#hophach #phimngan #xuyenkhong #khunglong #sinhton
```

**YouTube Shorts — tiêu đề** (67/100 ký tự)

```text
Khủng long bạo chúa đánh hơi ngay trên đầu hai người | Hổ Phách P11
```

**YouTube Shorts — mô tả**

```text
Tarbosaurus, họ hàng châu Á của khủng long bạo chúa, đứng chắn giữa hai người và bãi trống. “Đừng nhúc nhích gì cả. Mắt nó nhìn vật chuyển động giỏi hơn vật đứng yên.” Duy nghĩ ra một cách, nhưng phải đánh đổi thứ đáng tiền nhất của anh.

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
👉 Xem tiếp Phần 12: Thả drone dụ khủng long, mất 3 năm video

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Tarbosaurus, họ hàng châu Á của khủng long bạo chúa, đứng chắn giữa hai người và bãi trống. “Đừng nhúc nhích gì cả. Mắt nó nhìn vật chuyển động giỏi hơn vật đứng yên.” Duy nghĩ ra một cách, nhưng phải đánh đổi thứ đáng tiền nhất của anh.

Bạn sẽ hy sinh thứ gì để thoát thân? 👇
👉 Xem tiếp Phần 12: Thả drone dụ khủng long, mất 3 năm video
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #khunglong #sinhton
```

### Phần 12/12 — Thả drone dụ khủng long, mất 3 năm video

`12-tha-drone-mat-ca-kenh.mp4` · 42s · cảnh 19.1, 19.2, 19.3 · đăng Thứ Sáu 20/11 – 20:00

**TikTok**

```text
Duy cho chiếc drone bay vòng qua đầu Tarbosaurus, kêu thật to để dụ nó vào rừng. Ba năm quay phim của anh nằm hết trong chiếc hộp nhỏ ấy. “Kênh thì làm lại được. Còn em thì không ai làm lại được đâu.”
Nếu là Duy, bạn có thả chiếc drone đi không?

🎬 Họ có về được nhà không? Xem trọn bộ 22 phút trên kênh YouTube.
#hophach #phimngan #xuyenkhong #khunglong #camdong
```

**YouTube Shorts — tiêu đề** (61/100 ký tự)

```text
Thả drone dụ khủng long, mất trắng 3 năm video | Hổ Phách P12
```

**YouTube Shorts — mô tả**

```text
Duy cho chiếc drone bay vòng qua đầu Tarbosaurus, kêu thật to để dụ nó vào rừng. Ba năm quay phim của anh nằm hết trong chiếc hộp nhỏ ấy. “Kênh thì làm lại được. Còn em thì không ai làm lại được đâu.”

🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”
🎬 Họ có về được nhà không? Xem trọn bộ 22 phút trên kênh YouTube.

#Shorts #hophach #khunglong #phimngan
```

**Facebook Reels**

```text
Duy cho chiếc drone bay vòng qua đầu Tarbosaurus, kêu thật to để dụ nó vào rừng. Ba năm quay phim của anh nằm hết trong chiếc hộp nhỏ ấy. “Kênh thì làm lại được. Còn em thì không ai làm lại được đâu.”

Nếu là Duy, bạn có thả chiếc drone đi không? 👇
🎬 Họ có về được nhà không? Xem trọn bộ 22 phút trên kênh YouTube.
🎬 Full phim 22 phút có trên kênh YouTube, tìm “Hổ Phách: Ngược Dòng Tiền Sử”

#HoPhach #NguocDongTienSu #PhimNgan #KhungLong #khunglong #camdong
```
