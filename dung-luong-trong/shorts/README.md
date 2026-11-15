# Dung Lượng Trống — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Phim 20 phút (20 cảnh × 4 clip × 15 s) được cắt thành **12 phần dọc 9:16 từ những cảnh hay nhất**, theo đúng thứ tự truyện: dòng chữ lạ lúc 3 giờ 17, app thuê não, ký ức của người khác, vụ án, livestream và mười giây đếm ngược. Phần cuối dừng trước đoạn kết (cảnh 19–20) để người xem tìm phim full.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 ở giữa, nền là chính cảnh đó làm mờ.
- **Chữ trên video:** nhãn tím “DUNG LƯỢNG TRỐNG • PHẦN N”, câu hook phía trên khung phim, phụ đề khớp tiếng phía dưới. 2,5 giây cuối hook đổi thành “CÒN TIẾP » PHẦN N+1”.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chính tả sửa theo `PHAN_CANH_OMNI.json`.
- **Âm thanh:** chuẩn hoá −14 LUFS.
- **File:** video `NN-<slug>.mp4` nằm ngay trong `shorts/`; caption của mọi phần ở cuối README này.

Dựng lại:

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py dung-luong-trong
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py dung-luong-trong --only 4
```

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-3-gio-17-sang-chu-tren-tuong.mp4`](01-3-gio-17-sang-chu-tren-tuong.mp4) | 3 giờ 17 sáng, trên tường có chữ ai đó viết | 01.1, 01.2, 01.3 | 43s | Thứ Hai 16/11 – 12:00 | ⭐ |
| 2 | [`02-ba-tu-cho-thue-nao-10-nam.mp4`](02-ba-tu-cho-thue-nao-10-nam.mp4) | Cho thuê não 10 năm, bà Tư quên dần mọi thứ | 04.2, 04.3, 04.4 | 44s | Thứ Hai 16/11 – 20:00 |  |
| 3 | [`03-bam-dong-y-khoi-doc.mp4`](03-bam-dong-y-khoi-doc.mp4) | Ngủ 8 tiếng được 480 nghìn, chỉ cần bấm đồng ý | 05.1, 05.2, 05.4 | 42s | Thứ Ba 17/11 – 12:00 |  |
| 4 | [`04-bai-hat-tieng-nhat-la.mp4`](04-bai-hat-tieng-nhat-la.mp4) | Tự nhiên thuộc lòng một bài hát tiếng Nhật | 07.1, 07.2, 07.3 | 41s | Thứ Ba 17/11 – 20:00 | ⭐ |
| 5 | [`05-tay-tu-bam-ma-cua.mp4`](05-tay-tu-bam-ma-cua.mp4) | Tay tự bấm mã cửa tòa nhà chưa từng đến | 08.1, 08.2, 08.3 | 43s | Thứ Tư 18/11 – 12:00 |  |
| 6 | [`06-noi-mo-goi-ten-vy.mp4`](06-noi-mo-goi-ten-vy.mp4) | Đêm nào cũng nói mớ gọi tên một cô gái lạ | 09.2, 09.3, 09.4 | 42s | Thứ Tư 18/11 – 20:00 |  |
| 7 | [`07-ky-uc-vu-an.mp4`](07-ky-uc-vu-an.mp4) | Trong giấc mơ là ký ức về một vụ án | 10.2, 10.3, 10.4 | 43s | Thứ Năm 19/11 – 12:00 | ⭐ |
| 8 | [`08-can-phong-y-het-giac-mo.mp4`](08-can-phong-y-het-giac-mo.mp4) | Căn phòng y hệt giấc mơ và cô gái tên Vy | 11.2, 11.3, 11.4 | 45s | Thứ Năm 19/11 – 20:00 | ⭐ |
| 9 | [`09-su-that-ve-neurorent.mp4`](09-su-that-ve-neurorent.mp4) | Sự thật: họ gửi ký ức tội ác vào đầu người nghèo | 12.2, 12.3, 12.4 | 43s | Thứ Sáu 20/11 – 12:00 |  |
| 10 | [`10-ba-quen-con-gai.mp4`](10-ba-quen-con-gai.mp4) | Bà không nhận ra con gái mình trong tấm ảnh | 15.1, 15.2, 15.3 | 43s | Thứ Sáu 20/11 – 20:00 | ⭐ |
| 11 | [`11-livestream-chip-nhay-do.mp4`](11-livestream-chip-nhay-do.mp4) | Livestream kể ký ức, chip sau gáy nháy đỏ | 17.2, 17.3, 17.4 | 42s | Thứ Bảy 21/11 – 12:00 |  |
| 12 | [`12-muoi-giay-truoc-khi-bi-xoa.mp4`](12-muoi-giay-truoc-khi-bi-xoa.mp4) | Mười giây trước khi bị xóa ký ức | 18.2, 18.3, 18.4 | 44s | Thứ Bảy 21/11 – 20:00 | ⭐ |

⭐ = phần có hook mạnh nhất, nên dồn tương tác trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Dung Lượng Trống”. Mỗi caption có đúng 5 hashtag.
- **YouTube Shorts:** dán tiêu đề + mô tả; khi phim full đã lên kênh, điền link vào `full_movie_url` rồi chạy lại với `--captions`.
- **Facebook Reels:** dán caption (phụ đề đã in sẵn trên video).

## Ghi chú biên tập

- 8 clip chưa render nên không dùng: 02.2, 02.3, 02.4, 03.1, 06.1, 06.3, 14.1, 14.2.
- 6 clip có tiếng thoại không rõ chữ (Whisper không khớp kịch bản), không dùng và nên render lại trong phim full: 02.1, 03.3, 03.4, 05.3, 08.4, 19.2.
- Clip 11.4 có logo “VTVgo” ở góc dưới phải (đã cắt bỏ trong shorts); clip 16.4 có logo VTV màu ở góc trên phải (không dùng). Cả hai vẫn còn trong phim full, nên render lại.

## Caption từng phần (copy dán)

### Phần 1/12 — 3 giờ 17 sáng, trên tường có chữ ai đó viết

`01-3-gio-17-sang-chu-tren-tuong.mp4` · 43s · cảnh 01.1, 01.2, 01.3 · đăng Thứ Hai 16/11 – 12:00

**TikTok**

```text
3 giờ 17 sáng, Khải tỉnh dậy với cây bút trong tay và một địa chỉ lạ trên tường nhà mình: “Khu tập thể Kim Liên, nhà C, phòng 704. Đừng ngủ!” Nét chữ nghiêng nghiêng, không phải của anh. Còn trợ lý ảo Nova chỉ bảo anh đã ngủ rất ngon.
Bạn nghĩ ai đã viết dòng chữ đó lên tường?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #bian #vientuong
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
3 giờ 17 sáng tỉnh dậy, trên tường có chữ không phải của mình | Dung Lượng Trống P1
```

**YouTube Shorts — mô tả**

```text
3 giờ 17 sáng, Khải tỉnh dậy với cây bút trong tay và một địa chỉ lạ trên tường nhà mình: “Khu tập thể Kim Liên, nhà C, phòng 704. Đừng ngủ!” Nét chữ nghiêng nghiêng, không phải của anh. Còn trợ lý ảo Nova chỉ bảo anh đã ngủ rất ngon.

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 2: Cho thuê não 10 năm, bà Tư quên dần mọi thứ

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
3 giờ 17 sáng, Khải tỉnh dậy với cây bút trong tay và một địa chỉ lạ trên tường nhà mình: “Khu tập thể Kim Liên, nhà C, phòng 704. Đừng ngủ!” Nét chữ nghiêng nghiêng, không phải của anh. Còn trợ lý ảo Nova chỉ bảo anh đã ngủ rất ngon.

Bạn nghĩ ai đã viết dòng chữ đó lên tường? 👇
👉 Xem tiếp Phần 2: Cho thuê não 10 năm, bà Tư quên dần mọi thứ
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #bian #vientuong
```

### Phần 2/12 — Cho thuê não 10 năm, bà Tư quên dần mọi thứ

`02-ba-tu-cho-thue-nao-10-nam.mp4` · 44s · cảnh 04.2, 04.3, 04.4 · đăng Thứ Hai 16/11 – 20:00

**TikTok**

```text
Bà Tư dán miếng NeuroRent sau gáy suốt mười năm: “Ngủ một giấc, sáng ra là có tiền rồi, sướng lắm con ạ.” Chỉ có điều dạo này bà hay quên: quên tên người này người kia, có hôm quên cả mình đang nấu cơm cho ai.
Bạn có dám đổi giấc ngủ lấy tiền không?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #neurorent #camdong
```

**YouTube Shorts — tiêu đề** (73/100 ký tự)

```text
Cho công ty thuê não 10 năm, bà cụ quên dần mọi thứ | Dung Lượng Trống P2
```

**YouTube Shorts — mô tả**

```text
Bà Tư dán miếng NeuroRent sau gáy suốt mười năm: “Ngủ một giấc, sáng ra là có tiền rồi, sướng lắm con ạ.” Chỉ có điều dạo này bà hay quên: quên tên người này người kia, có hôm quên cả mình đang nấu cơm cho ai.

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 3: Ngủ 8 tiếng được 480 nghìn, chỉ cần bấm đồng ý

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Bà Tư dán miếng NeuroRent sau gáy suốt mười năm: “Ngủ một giấc, sáng ra là có tiền rồi, sướng lắm con ạ.” Chỉ có điều dạo này bà hay quên: quên tên người này người kia, có hôm quên cả mình đang nấu cơm cho ai.

Bạn có dám đổi giấc ngủ lấy tiền không? 👇
👉 Xem tiếp Phần 3: Ngủ 8 tiếng được 480 nghìn, chỉ cần bấm đồng ý
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #neurorent #camdong
```

### Phần 3/12 — Ngủ 8 tiếng được 480 nghìn, chỉ cần bấm đồng ý

`03-bam-dong-y-khoi-doc.mp4` · 42s · cảnh 05.1, 05.2, 05.4 · đăng Thứ Ba 17/11 – 12:00

**TikTok**

```text
“Dung lượng trống của anh là 87%. 60 nghìn mỗi giờ ngủ.” Điều khoản dài 48 trang, Khải bấm đồng ý luôn, khỏi đọc. Đêm đó em gái hỏi: “Cái gì sau gáy anh mà sáng tím thế?”
Bạn có bao giờ đọc hết điều khoản trước khi bấm đồng ý không?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #neurorent #congnghe
```

**YouTube Shorts — tiêu đề** (68/100 ký tự)

```text
Ngủ 8 tiếng được 480 nghìn, chỉ cần bấm đồng ý | Dung Lượng Trống P3
```

**YouTube Shorts — mô tả**

```text
“Dung lượng trống của anh là 87%. 60 nghìn mỗi giờ ngủ.” Điều khoản dài 48 trang, Khải bấm đồng ý luôn, khỏi đọc. Đêm đó em gái hỏi: “Cái gì sau gáy anh mà sáng tím thế?”

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 4: Tự nhiên thuộc lòng một bài hát tiếng Nhật

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
“Dung lượng trống của anh là 87%. 60 nghìn mỗi giờ ngủ.” Điều khoản dài 48 trang, Khải bấm đồng ý luôn, khỏi đọc. Đêm đó em gái hỏi: “Cái gì sau gáy anh mà sáng tím thế?”

Bạn có bao giờ đọc hết điều khoản trước khi bấm đồng ý không? 👇
👉 Xem tiếp Phần 4: Tự nhiên thuộc lòng một bài hát tiếng Nhật
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #neurorent #congnghe
```

### Phần 4/12 — Tự nhiên thuộc lòng một bài hát tiếng Nhật

`04-bai-hat-tieng-nhat-la.mp4` · 41s · cảnh 07.1, 07.2, 07.3 · đăng Thứ Ba 17/11 – 20:00

**TikTok**

```text
Khải ngân nga một bài hát ru tiếng Nhật mà anh chưa từng học, đúng từng giai điệu. Mẹ anh không biết tiếng Nhật, anh cũng chưa nghe bài này bao giờ. “Thế mà sao mình lại thuộc lòng từng chữ một thế này?”
Bạn nghĩ bài hát đó từ đâu ra?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #bian #kyuc
```

**YouTube Shorts — tiêu đề** (79/100 ký tự)

```text
Tự nhiên thuộc lòng một bài hát tiếng Nhật chưa từng nghe | Dung Lượng Trống P4
```

**YouTube Shorts — mô tả**

```text
Khải ngân nga một bài hát ru tiếng Nhật mà anh chưa từng học, đúng từng giai điệu. Mẹ anh không biết tiếng Nhật, anh cũng chưa nghe bài này bao giờ. “Thế mà sao mình lại thuộc lòng từng chữ một thế này?”

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 5: Tay tự bấm mã cửa tòa nhà chưa từng đến

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Khải ngân nga một bài hát ru tiếng Nhật mà anh chưa từng học, đúng từng giai điệu. Mẹ anh không biết tiếng Nhật, anh cũng chưa nghe bài này bao giờ. “Thế mà sao mình lại thuộc lòng từng chữ một thế này?”

Bạn nghĩ bài hát đó từ đâu ra? 👇
👉 Xem tiếp Phần 5: Tay tự bấm mã cửa tòa nhà chưa từng đến
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #bian #kyuc
```

### Phần 5/12 — Tay tự bấm mã cửa tòa nhà chưa từng đến

`05-tay-tu-bam-ma-cua.mp4` · 43s · cảnh 08.1, 08.2, 08.3 · đăng Thứ Tư 18/11 – 12:00

**TikTok**

```text
Giao hàng tới một tòa nhà lạ, tay Khải tự bấm đúng mã cửa. Trong đầu anh hiện lên bàn tay một người con gái, móng cắt ngắn, run run. Rồi gương mặt ông chủ NeuroRent trên biển quảng cáo… hình như anh đã thấy ở đâu rồi.
Nếu tay bạn tự làm một việc bạn chưa từng học, bạn sẽ làm gì?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #bian #kyuc
```

**YouTube Shorts — tiêu đề** (70/100 ký tự)

```text
Tay tự bấm đúng mã cửa của tòa nhà chưa từng đến | Dung Lượng Trống P5
```

**YouTube Shorts — mô tả**

```text
Giao hàng tới một tòa nhà lạ, tay Khải tự bấm đúng mã cửa. Trong đầu anh hiện lên bàn tay một người con gái, móng cắt ngắn, run run. Rồi gương mặt ông chủ NeuroRent trên biển quảng cáo… hình như anh đã thấy ở đâu rồi.

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 6: Đêm nào cũng nói mớ gọi tên một cô gái lạ

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Giao hàng tới một tòa nhà lạ, tay Khải tự bấm đúng mã cửa. Trong đầu anh hiện lên bàn tay một người con gái, móng cắt ngắn, run run. Rồi gương mặt ông chủ NeuroRent trên biển quảng cáo… hình như anh đã thấy ở đâu rồi.

Nếu tay bạn tự làm một việc bạn chưa từng học, bạn sẽ làm gì? 👇
👉 Xem tiếp Phần 6: Đêm nào cũng nói mớ gọi tên một cô gái lạ
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #bian #kyuc
```

### Phần 6/12 — Đêm nào cũng nói mớ gọi tên một cô gái lạ

`06-noi-mo-goi-ten-vy.mp4` · 42s · cảnh 09.2, 09.3, 09.4 · đăng Thứ Tư 18/11 – 20:00

**TikTok**

```text
Khải không dám ngủ nữa. Em gái kể đêm nào anh cũng nói mớ bằng thứ tiếng nó không hiểu, và gọi mãi một cái tên: “Vy, Vy ơi.” Ba giờ sáng, anh cố mở mắt… “Chỉ nhắm mắt một chút thôi.”
Bạn có từng nói mớ một cái tên lạ không?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #bian #kyuc
```

**YouTube Shorts — tiêu đề** (71/100 ký tự)

```text
Đêm nào cũng nói mớ gọi tên một cô gái không quen | Dung Lượng Trống P6
```

**YouTube Shorts — mô tả**

```text
Khải không dám ngủ nữa. Em gái kể đêm nào anh cũng nói mớ bằng thứ tiếng nó không hiểu, và gọi mãi một cái tên: “Vy, Vy ơi.” Ba giờ sáng, anh cố mở mắt… “Chỉ nhắm mắt một chút thôi.”

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 7: Trong giấc mơ là ký ức về một vụ án

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Khải không dám ngủ nữa. Em gái kể đêm nào anh cũng nói mớ bằng thứ tiếng nó không hiểu, và gọi mãi một cái tên: “Vy, Vy ơi.” Ba giờ sáng, anh cố mở mắt… “Chỉ nhắm mắt một chút thôi.”

Bạn có từng nói mớ một cái tên lạ không? 👇
👉 Xem tiếp Phần 7: Trong giấc mơ là ký ức về một vụ án
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #bian #kyuc
```

### Phần 7/12 — Trong giấc mơ là ký ức về một vụ án

`07-ky-uc-vu-an.mp4` · 43s · cảnh 10.2, 10.3, 10.4 · đăng Thứ Năm 19/11 – 12:00

**TikTok**

```text
Trong giấc mơ là ký ức không phải của Khải: kỹ sư Lâm định công bố toàn bộ dữ liệu của NeuroRent, ông chủ Huy chặn cửa. Rồi ông Lâm ngã xuống. “Vy, nghe anh. Em không thấy gì hết. Em chưa từng ở đây.”
Bạn nghĩ cô gái tên Vy là ai?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #vientuong #hinhsu
```

**YouTube Shorts — tiêu đề** (70/100 ký tự)

```text
Trong giấc mơ là ký ức về một vụ án mạng có thật | Dung Lượng Trống P7
```

**YouTube Shorts — mô tả**

```text
Trong giấc mơ là ký ức không phải của Khải: kỹ sư Lâm định công bố toàn bộ dữ liệu của NeuroRent, ông chủ Huy chặn cửa. Rồi ông Lâm ngã xuống. “Vy, nghe anh. Em không thấy gì hết. Em chưa từng ở đây.”

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 8: Căn phòng y hệt giấc mơ và cô gái tên Vy

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Trong giấc mơ là ký ức không phải của Khải: kỹ sư Lâm định công bố toàn bộ dữ liệu của NeuroRent, ông chủ Huy chặn cửa. Rồi ông Lâm ngã xuống. “Vy, nghe anh. Em không thấy gì hết. Em chưa từng ở đây.”

Bạn nghĩ cô gái tên Vy là ai? 👇
👉 Xem tiếp Phần 8: Căn phòng y hệt giấc mơ và cô gái tên Vy
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #vientuong #hinhsu
```

### Phần 8/12 — Căn phòng y hệt giấc mơ và cô gái tên Vy

`08-can-phong-y-het-giac-mo.mp4` · 45s · cảnh 11.2, 11.3, 11.4 · đăng Thứ Năm 19/11 – 20:00

**TikTok**

```text
Lần theo địa chỉ trên tường, Khải tới căn hộ bỏ hoang 704: rèm vàng rách góc, tranh hoa sen treo lệch, y hệt giấc mơ. Rồi một cô gái xuất hiện: “Đó là bài mẹ tôi hát ru tôi. Ngoài tôi ra, không ai biết bài đó.”
Bạn có đoán ra Vy đã làm gì không?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #bian #vientuong
```

**YouTube Shorts — tiêu đề** (72/100 ký tự)

```text
Căn phòng y hệt giấc mơ, và cô gái biết bài hát ru | Dung Lượng Trống P8
```

**YouTube Shorts — mô tả**

```text
Lần theo địa chỉ trên tường, Khải tới căn hộ bỏ hoang 704: rèm vàng rách góc, tranh hoa sen treo lệch, y hệt giấc mơ. Rồi một cô gái xuất hiện: “Đó là bài mẹ tôi hát ru tôi. Ngoài tôi ra, không ai biết bài đó.”

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 9: Sự thật: họ gửi ký ức tội ác vào đầu người nghèo

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Lần theo địa chỉ trên tường, Khải tới căn hộ bỏ hoang 704: rèm vàng rách góc, tranh hoa sen treo lệch, y hệt giấc mơ. Rồi một cô gái xuất hiện: “Đó là bài mẹ tôi hát ru tôi. Ngoài tôi ra, không ai biết bài đó.”

Bạn có đoán ra Vy đã làm gì không? 👇
👉 Xem tiếp Phần 9: Sự thật: họ gửi ký ức tội ác vào đầu người nghèo
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #bian #vientuong
```

### Phần 9/12 — Sự thật: họ gửi ký ức tội ác vào đầu người nghèo

`09-su-that-ve-neurorent.mp4` · 43s · cảnh 12.2, 12.3, 12.4 · đăng Thứ Sáu 20/11 – 12:00

**TikTok**

```text
Vy nói ra sự thật: “Ký ức thì không xóa được, chỉ chuyển đi được thôi.” Người giàu muốn quên một vụ tai nạn, một vụ hối lộ, một tội ác, họ trả tiền để gửi nó vào đầu những người nghèo… trong lúc họ đang ngủ say.
Nếu được trả tiền, bạn có chịu giữ hộ ký ức của người khác không?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #neurorent #vientuong
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
Sự thật về app thuê não: gửi ký ức tội ác vào đầu người nghèo | Dung Lượng Trống P9
```

**YouTube Shorts — mô tả**

```text
Vy nói ra sự thật: “Ký ức thì không xóa được, chỉ chuyển đi được thôi.” Người giàu muốn quên một vụ tai nạn, một vụ hối lộ, một tội ác, họ trả tiền để gửi nó vào đầu những người nghèo… trong lúc họ đang ngủ say.

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 10: Bà không nhận ra con gái mình trong tấm ảnh

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Vy nói ra sự thật: “Ký ức thì không xóa được, chỉ chuyển đi được thôi.” Người giàu muốn quên một vụ tai nạn, một vụ hối lộ, một tội ác, họ trả tiền để gửi nó vào đầu những người nghèo… trong lúc họ đang ngủ say.

Nếu được trả tiền, bạn có chịu giữ hộ ký ức của người khác không? 👇
👉 Xem tiếp Phần 10: Bà không nhận ra con gái mình trong tấm ảnh
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #neurorent #vientuong
```

### Phần 10/12 — Bà không nhận ra con gái mình trong tấm ảnh

`10-ba-quen-con-gai.mp4` · 43s · cảnh 15.1, 15.2, 15.3 · đăng Thứ Sáu 20/11 – 20:00

**TikTok**

```text
Bà Tư nhờ Khải xem tấm ảnh cũ ở Hồ Gươm. Mặt sau ghi: “Mẹ và bé Hạnh, năm 2018.” Bà không nhớ nổi con gái mình. “Sao cái tên này nghe đau thế này hả con?”
Điều gì bạn sợ quên nhất?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #camdong #giadinh
```

**YouTube Shorts — tiêu đề** (73/100 ký tự)

```text
Cho thuê não 10 năm, bà không nhận ra con gái mình | Dung Lượng Trống P10
```

**YouTube Shorts — mô tả**

```text
Bà Tư nhờ Khải xem tấm ảnh cũ ở Hồ Gươm. Mặt sau ghi: “Mẹ và bé Hạnh, năm 2018.” Bà không nhớ nổi con gái mình. “Sao cái tên này nghe đau thế này hả con?”

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 11: Livestream kể ký ức, chip sau gáy nháy đỏ

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Bà Tư nhờ Khải xem tấm ảnh cũ ở Hồ Gươm. Mặt sau ghi: “Mẹ và bé Hạnh, năm 2018.” Bà không nhớ nổi con gái mình. “Sao cái tên này nghe đau thế này hả con?”

Điều gì bạn sợ quên nhất? 👇
👉 Xem tiếp Phần 11: Livestream kể ký ức, chip sau gáy nháy đỏ
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #camdong #giadinh
```

### Phần 11/12 — Livestream kể ký ức, chip sau gáy nháy đỏ

`11-livestream-chip-nhay-do.mp4` · 42s · cảnh 17.2, 17.3, 17.4 · đăng Thứ Bảy 21/11 – 12:00

**TikTok**

```text
Khải phát trực tiếp, kể hết những gì anh còn nhớ trước khi bị xóa. Vy công bố danh sách hơn 3 triệu tài khoản. 8.000 người đang xem, đang chia sẻ khắp nơi… thì con chip sau gáy anh bắt đầu nháy đỏ.
Bạn có dám livestream tố cáo một tập đoàn lớn không?

👉 Phần 12 ở trang cá nhân, Follow để xem tiếp!
#dungluongtrong #phimngan #khoahocvientuong #livestream #vientuong
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
Livestream tố cáo ông chủ app thuê não, chip sau gáy nháy đỏ | Dung Lượng Trống P11
```

**YouTube Shorts — mô tả**

```text
Khải phát trực tiếp, kể hết những gì anh còn nhớ trước khi bị xóa. Vy công bố danh sách hơn 3 triệu tài khoản. 8.000 người đang xem, đang chia sẻ khắp nơi… thì con chip sau gáy anh bắt đầu nháy đỏ.

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
👉 Xem tiếp Phần 12: Mười giây trước khi bị xóa ký ức

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
Khải phát trực tiếp, kể hết những gì anh còn nhớ trước khi bị xóa. Vy công bố danh sách hơn 3 triệu tài khoản. 8.000 người đang xem, đang chia sẻ khắp nơi… thì con chip sau gáy anh bắt đầu nháy đỏ.

Bạn có dám livestream tố cáo một tập đoàn lớn không? 👇
👉 Xem tiếp Phần 12: Mười giây trước khi bị xóa ký ức
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #livestream #vientuong
```

### Phần 12/12 — Mười giây trước khi bị xóa ký ức

`12-muoi-giay-truoc-khi-bi-xoa.mp4` · 44s · cảnh 18.2, 18.3, 18.4 · đăng Thứ Bảy 21/11 – 20:00

**TikTok**

```text
“Ông ấy đập đầu vào góc bàn. Còn chiếc kính… văng vào gầm bàn.” Mười giây trước khi bị thu hồi ký ức, Khải chỉ kịp dặn em gái: “Ở nhà học cho tử tế nghe chưa. Anh thương em nhiều lắm, Linh ạ.”
Nếu chỉ còn 10 giây để nói, bạn sẽ nói gì với người thân?

🎬 Khải có quên hết không? Xem trọn bộ 20 phút trên kênh YouTube.
#dungluongtrong #phimngan #khoahocvientuong #camdong #giadinh
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
10 giây trước khi bị xóa ký ức, anh dặn em gái một câu | Dung Lượng Trống P12
```

**YouTube Shorts — mô tả**

```text
“Ông ấy đập đầu vào góc bàn. Còn chiếc kính… văng vào gầm bàn.” Mười giây trước khi bị thu hồi ký ức, Khải chỉ kịp dặn em gái: “Ở nhà học cho tử tế nghe chưa. Anh thương em nhiều lắm, Linh ạ.”

🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”
🎬 Khải có quên hết không? Xem trọn bộ 20 phút trên kênh YouTube.

#Shorts #dungluongtrong #phimngan #vientuong
```

**Facebook Reels**

```text
“Ông ấy đập đầu vào góc bàn. Còn chiếc kính… văng vào gầm bàn.” Mười giây trước khi bị thu hồi ký ức, Khải chỉ kịp dặn em gái: “Ở nhà học cho tử tế nghe chưa. Anh thương em nhiều lắm, Linh ạ.”

Nếu chỉ còn 10 giây để nói, bạn sẽ nói gì với người thân? 👇
🎬 Khải có quên hết không? Xem trọn bộ 20 phút trên kênh YouTube.
🎬 Full phim 20 phút có trên kênh YouTube, tìm “Dung Lượng Trống”

#DungLuongTrong #PhimNgan #KhoaHocVienTuong #PhimViet #camdong #giadinh
```
