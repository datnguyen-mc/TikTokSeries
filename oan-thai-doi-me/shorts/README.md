# Oán Thai Đòi Mẹ: Búp Bê Đất Nung — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **các cảnh hay nhất** của phim 14 phút: **10 phần dọc 9:16**, không phải cả phim. Mỗi phần là một khoảnh khắc rùng rợn, bí ẩn hoặc một cú lật, dài 30–60 giây (mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger), đăng nối tiếp theo thứ tự truyện.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn đỏ máu “OÁN THAI ĐÒI MẸ • PHẦN N” và câu hook ở trên khung phim; phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy nguyên từ tiếng thật trong clip (Whisper), không so kịch bản vì bản render dùng lời thoại cũ; chữ Whisper nghe nhầm sửa bằng `subtitle_replace`.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm); câu Omni nói lặp ở cuối clip bị cắt bỏ.
- **Kết quả:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; lịch đăng và caption TikTok / YouTube / Facebook của mọi phần nằm trong `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py oan-thai-doi-me            # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py oan-thai-doi-me --only 3   # một phần
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py oan-thai-doi-me --captions   # chỉ ghi lại README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-lo-gom-bi-bit-kin.mp4`](01-lo-gom-bi-bit-kin.mp4) | Phá lò gốm bị bít kín, lôi ra tượng hài nhi đất nung | 01.1, 01.2, 01.3, 01.4, 01.5, 01.6 | 56s | Thứ Bảy 14/11 – 11:00 |  |
| 2 | [`02-giot-mau-bi-hut-can.mp4`](02-giot-mau-bi-hut-can.mp4) | Giọt máu mẹ bầu nhỏ xuống, tượng đất hút cạn sạch | 02.2, 02.3, 02.4, 02.5, 02.6 | 49s | Thứ Bảy 14/11 – 19:00 |  |
| 3 | [`03-rach-mieng-tuong-dat.mp4`](03-rach-mieng-tuong-dat.mp4) | Mẹ bầu cầm dao rạch miệng tượng đất giữa đêm | 03.3, 03.4, 03.5, 03.6 | 39s | Chủ Nhật 15/11 – 11:00 |  |
| 4 | [`04-diem-mat-cho-tuong-dat.mp4`](04-diem-mat-cho-tuong-dat.mp4) | 2 giờ sáng, vợ bầu ngồi điểm mắt cho tượng đất | 04.2, 04.3, 04.4, 04.5 | 38s | Chủ Nhật 15/11 – 19:00 | ⭐ |
| 5 | [`05-may-quet-thay-dua-tre.mp4`](05-may-quet-thay-dua-tre.mp4) | Nôi trống trơn, máy quét 3D lại thấy đứa trẻ | 05.3, 05.4, 05.5 | 28s | Thứ Hai 16/11 – 11:00 | ⭐ |
| 6 | [`06-hinh-nhan-trong-guong.mp4`](06-hinh-nhan-trong-guong.mp4) | Soi gương, thấy hình nhân bùn đất bám chặt trước ngực | 06.2, 06.3, 06.4, 06.5 | 38s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-ke-dieu-ho-ly-son.mp4`](07-ke-dieu-ho-ly-son.mp4) | Mở túi ra mới biết tượng thật vẫn ở nhà với vợ | 09.3, 09.4, 09.5 | 29s | Thứ Ba 17/11 – 11:00 | ⭐ |
| 8 | [`08-dap-vo-tuong-mat-ca-hai.mp4`](08-dap-vo-tuong-mat-ca-hai.mp4) | Đập vỡ tượng đất là mất cả hai mẹ con | 11.1, 11.2, 11.3 | 30s | Thứ Ba 17/11 – 19:00 |  |
| 9 | [`09-nguoi-cha-nhan-thay.mp4`](09-nguoi-cha-nhan-thay.mp4) | Người cha xin nhận lời nguyền thay vợ con | 11.5, 11.6, 12.1, 12.2, 12.3 | 50s | Thứ Tư 18/11 – 11:00 |  |
| 10 | [`10-dat-ten-con-la-binh-an.mp4`](10-dat-ten-con-la-binh-an.mp4) | “Sinh con ra nhớ đặt tên con là Bình An” | 13.2, 13.3, 13.4 | 30s | Thứ Tư 18/11 – 19:00 |  |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Oán Thai Đòi Mẹ”. Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả ở phần caption bên dưới; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption; tắt phụ đề tự động vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00), 3 nền tảng cùng giờ, bắt đầu Thứ Bảy 14/11. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Ghi chú bản short

- **Chọn cảnh:** 10 khoảnh khắc mạnh nhất (khoảng 6,7 phút clip thô trên 14 phút phim), chỉ dùng clip đã render và sạch khung hình.
- **Thoại trong clip là bản cũ:** tiếng thật trong 76 clip đã render khác câu chữ của `KICH_BAN_14_PHUT.md` và `canh-XX/clip-N.md` hiện tại (cùng diễn biến, khác lời). Phim không có `PHAN_CANH_OMNI.json` nên `match_script: false`: phụ đề theo tiếng thật (Whisper), caption trích đúng câu nghe được.
- **Chính tả phụ đề:** `subtitle_replace` còn trống; điền sau khi xem bản Whisper. Lỗi nghe nhầm thường gặp: “đất xét” → “đất sét”, “chấn” → “trấn”, “cho” → “tro”, “dạch” → “rạch”, “bà lụa” → “bà Lụa”, “bách” → “Bách”, “oán thai” → “Oán Thai”, “Chúng kế” → “Trúng kế”.
- **Clip chưa render:** 05.2, 05.6, 08.2, 10.6, 12.6, 13.5, 14.3, 14.4. Vì thiếu 14.3–14.4 (vết rạn đất nung trên tay Bách) nên chưa có phần kết phim.
- **Clip có chữ hoặc máy quay lọt khung, short không dùng** (bản FULL vẫn chứa, nên render lại): giờ in trên hình ở 03.2 (“23:45”), 04.6 (“2:00 AM” kèm chữ ở góc), 05.1 (“9:00 PM”), 09.2 (“2:15 AM”), 10.4; chữ “50mm AM” ở 07.4 và 08.5; chữ góc phải ở 07.5; chú thích tên “Thay Phong” ở 11.4; máy quay lọt khung ở 04.1, 10.1, 13.1 (13.1 còn phụ đề cháy vào hình).
- **Clip 01.1** (phần 1) nói lặp câu cuối “…kín cửa thì chẳng ai được đục mở”; script tự cắt đoạn lặp.

## Caption từng phần (copy dán)

### Phần 1/10 — Phá lò gốm bị bít kín, lôi ra tượng hài nhi đất nung

`01-lo-gom-bi-bit-kin.mp4` · 56s · cảnh 01.1, 01.2, 01.3, 01.4, 01.5, 01.6 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
“Lò bầu nào đã xây gạch bít kín cửa thì chẳng ai được đục mở.” Vậy mà vì muốn kiếm tư liệu cho dự án 3D, Bách tự tay rút viên gạch trấn và lôi ra một pho tượng đất nung hình đứa trẻ sơ sinh, chưa kịp có mắt có miệng. Anh không hề biết thứ bị giam dưới đáy lò suốt ba thập kỷ đã lặng lẽ theo anh về tận nhà.
Đồ trong lò bị bít kín, bạn có dám mang về nhà không?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #gomco #tamlinh
```

**YouTube Shorts — tiêu đề** (86/100 ký tự)

```text
Phá lò gốm bị bít kín, lôi ra tượng hài nhi không mắt không miệng | Oán Thai Đòi Mẹ P1
```

**YouTube Shorts — mô tả**

```text
“Lò bầu nào đã xây gạch bít kín cửa thì chẳng ai được đục mở.” Vậy mà vì muốn kiếm tư liệu cho dự án 3D, Bách tự tay rút viên gạch trấn và lôi ra một pho tượng đất nung hình đứa trẻ sơ sinh, chưa kịp có mắt có miệng. Anh không hề biết thứ bị giam dưới đáy lò suốt ba thập kỷ đã lặng lẽ theo anh về tận nhà.

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 2: Giọt máu mẹ bầu nhỏ xuống, tượng đất hút cạn sạch

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
“Lò bầu nào đã xây gạch bít kín cửa thì chẳng ai được đục mở.” Vậy mà vì muốn kiếm tư liệu cho dự án 3D, Bách tự tay rút viên gạch trấn và lôi ra một pho tượng đất nung hình đứa trẻ sơ sinh, chưa kịp có mắt có miệng. Anh không hề biết thứ bị giam dưới đáy lò suốt ba thập kỷ đã lặng lẽ theo anh về tận nhà.

Đồ trong lò bị bít kín, bạn có dám mang về nhà không? 👇
👉 Xem tiếp Phần 2: Giọt máu mẹ bầu nhỏ xuống, tượng đất hút cạn sạch
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #gomco #tamlinh
```

### Phần 2/10 — Giọt máu mẹ bầu nhỏ xuống, tượng đất hút cạn sạch

`02-giot-mau-bi-hut-can.mp4` · 49s · cảnh 02.2, 02.3, 02.4, 02.5, 02.6 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Vừa mở tấm vải nâu, ánh mắt Hà khựng lại như có sợi dây vô hình trói tâm trí cô vào khối đất lạnh. Giọt máu từ đầu ngón tay cô nhỏ xuống pho tượng rồi rút cạn không còn dấu vết, đứa bé trong bụng đạp thốc lên như muốn kêu cứu. Hà ôm ghì lấy pho tượng: “Em nghe rõ mồn một tiếng nó đang khóc vì lạnh và tối lắm Bách ơi.”
Hà đang nghe thấy tiếng khóc của ai?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #mebau #kinhdi
```

**YouTube Shorts — tiêu đề** (91/100 ký tự)

```text
Giọt máu mẹ bầu nhỏ xuống tượng đất nung, bị hút cạn không còn dấu vết | Oán Thai Đòi Mẹ P2
```

**YouTube Shorts — mô tả**

```text
Vừa mở tấm vải nâu, ánh mắt Hà khựng lại như có sợi dây vô hình trói tâm trí cô vào khối đất lạnh. Giọt máu từ đầu ngón tay cô nhỏ xuống pho tượng rồi rút cạn không còn dấu vết, đứa bé trong bụng đạp thốc lên như muốn kêu cứu. Hà ôm ghì lấy pho tượng: “Em nghe rõ mồn một tiếng nó đang khóc vì lạnh và tối lắm Bách ơi.”

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 3: Mẹ bầu cầm dao rạch miệng tượng đất giữa đêm

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
Vừa mở tấm vải nâu, ánh mắt Hà khựng lại như có sợi dây vô hình trói tâm trí cô vào khối đất lạnh. Giọt máu từ đầu ngón tay cô nhỏ xuống pho tượng rồi rút cạn không còn dấu vết, đứa bé trong bụng đạp thốc lên như muốn kêu cứu. Hà ôm ghì lấy pho tượng: “Em nghe rõ mồn một tiếng nó đang khóc vì lạnh và tối lắm Bách ơi.”

Hà đang nghe thấy tiếng khóc của ai? 👇
👉 Xem tiếp Phần 3: Mẹ bầu cầm dao rạch miệng tượng đất giữa đêm
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #mebau #kinhdi
```

### Phần 3/10 — Mẹ bầu cầm dao rạch miệng tượng đất giữa đêm

`03-rach-mieng-tuong-dat.mp4` · 39s · cảnh 03.3, 03.4, 03.5, 03.6 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Vừa miết kín nét chữ cuối cùng, một luồng gió lạnh buốt từ pho tượng sộc thẳng vào ngực Hà. Đôi tay cô như bị ai cầm lái, rút dao rạch mở cái miệng vốn đã bị phong kín của đứa trẻ đất nung: “Sắp xong rồi con ơi. Đêm nay mẹ trả lại mắt mũi cho con.” Ngay góc tối sau kệ gốm, bóng một người đàn bà lặng lẽ hiện ra, chắp đôi bàn tay nứt nẻ đầy tuyệt vọng.
Người đàn bà sau kệ gốm là ai?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #kinhdi #mebau
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
Mẹ bầu như bị nhập, cầm dao rạch miệng tượng đất nung giữa đêm | Oán Thai Đòi Mẹ P3
```

**YouTube Shorts — mô tả**

```text
Vừa miết kín nét chữ cuối cùng, một luồng gió lạnh buốt từ pho tượng sộc thẳng vào ngực Hà. Đôi tay cô như bị ai cầm lái, rút dao rạch mở cái miệng vốn đã bị phong kín của đứa trẻ đất nung: “Sắp xong rồi con ơi. Đêm nay mẹ trả lại mắt mũi cho con.” Ngay góc tối sau kệ gốm, bóng một người đàn bà lặng lẽ hiện ra, chắp đôi bàn tay nứt nẻ đầy tuyệt vọng.

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 4: 2 giờ sáng, vợ bầu ngồi điểm mắt cho tượng đất

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
Vừa miết kín nét chữ cuối cùng, một luồng gió lạnh buốt từ pho tượng sộc thẳng vào ngực Hà. Đôi tay cô như bị ai cầm lái, rút dao rạch mở cái miệng vốn đã bị phong kín của đứa trẻ đất nung: “Sắp xong rồi con ơi. Đêm nay mẹ trả lại mắt mũi cho con.” Ngay góc tối sau kệ gốm, bóng một người đàn bà lặng lẽ hiện ra, chắp đôi bàn tay nứt nẻ đầy tuyệt vọng.

Người đàn bà sau kệ gốm là ai? 👇
👉 Xem tiếp Phần 4: 2 giờ sáng, vợ bầu ngồi điểm mắt cho tượng đất
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #kinhdi #mebau
```

### Phần 4/10 — 2 giờ sáng, vợ bầu ngồi điểm mắt cho tượng đất

`04-diem-mat-cho-tuong-dat.mp4` · 38s · cảnh 04.2, 04.3, 04.4, 04.5 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Hai giờ sáng, Hà ngồi cầm cọ hát: “Búp bê đất sét chẳng có lông mày, chẳng có mắt.” Đầu cọ vừa chấm xong con ngươi thứ hai, pho tượng như có hồn, trợn đôi mắt đen nhánh. Bách gọi được vợ tỉnh lại, nhưng trên bàn, pho tượng đã mở to đôi mắt đen ngòm nhìn hai vợ chồng.
Bạn có dám ở lại căn phòng đó đến sáng không?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #kinhdi #nuadem
```

**YouTube Shorts — tiêu đề** (80/100 ký tự)

```text
2 giờ sáng, vợ bầu ngồi hát rồi điểm mắt cho tượng đất nung | Oán Thai Đòi Mẹ P4
```

**YouTube Shorts — mô tả**

```text
Hai giờ sáng, Hà ngồi cầm cọ hát: “Búp bê đất sét chẳng có lông mày, chẳng có mắt.” Đầu cọ vừa chấm xong con ngươi thứ hai, pho tượng như có hồn, trợn đôi mắt đen nhánh. Bách gọi được vợ tỉnh lại, nhưng trên bàn, pho tượng đã mở to đôi mắt đen ngòm nhìn hai vợ chồng.

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 5: Nôi trống trơn, máy quét 3D lại thấy đứa trẻ

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
Hai giờ sáng, Hà ngồi cầm cọ hát: “Búp bê đất sét chẳng có lông mày, chẳng có mắt.” Đầu cọ vừa chấm xong con ngươi thứ hai, pho tượng như có hồn, trợn đôi mắt đen nhánh. Bách gọi được vợ tỉnh lại, nhưng trên bàn, pho tượng đã mở to đôi mắt đen ngòm nhìn hai vợ chồng.

Bạn có dám ở lại căn phòng đó đến sáng không? 👇
👉 Xem tiếp Phần 5: Nôi trống trơn, máy quét 3D lại thấy đứa trẻ
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #kinhdi #nuadem
```

### Phần 5/10 — Nôi trống trơn, máy quét 3D lại thấy đứa trẻ

`05-may-quet-thay-dua-tre.mp4` · 28s · cảnh 05.3, 05.4, 05.5 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
“Nhìn bằng mắt thường thì chiếc nôi trống không, ấy thế mà qua màn hình cảm biến, lại hiện lên một đứa trẻ đang nằm co ro bên trong lòng nôi.” Bách lao sang phòng phục chế: pho tượng trên bàn xoay đã biến mất, chỉ còn tiếng cào sột soạt dưới gầm bàn. Và người đang ôm khư khư pho tượng dưới đó là vợ anh.
Máy quét thấy được ma, bạn tin không?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #bian #tamlinh
```

**YouTube Shorts — tiêu đề** (85/100 ký tự)

```text
Nôi trống trơn, máy quét 3D lại thấy đứa trẻ nằm co ro bên trong | Oán Thai Đòi Mẹ P5
```

**YouTube Shorts — mô tả**

```text
“Nhìn bằng mắt thường thì chiếc nôi trống không, ấy thế mà qua màn hình cảm biến, lại hiện lên một đứa trẻ đang nằm co ro bên trong lòng nôi.” Bách lao sang phòng phục chế: pho tượng trên bàn xoay đã biến mất, chỉ còn tiếng cào sột soạt dưới gầm bàn. Và người đang ôm khư khư pho tượng dưới đó là vợ anh.

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 6: Soi gương, thấy hình nhân bùn đất bám chặt trước ngực

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
“Nhìn bằng mắt thường thì chiếc nôi trống không, ấy thế mà qua màn hình cảm biến, lại hiện lên một đứa trẻ đang nằm co ro bên trong lòng nôi.” Bách lao sang phòng phục chế: pho tượng trên bàn xoay đã biến mất, chỉ còn tiếng cào sột soạt dưới gầm bàn. Và người đang ôm khư khư pho tượng dưới đó là vợ anh.

Máy quét thấy được ma, bạn tin không? 👇
👉 Xem tiếp Phần 6: Soi gương, thấy hình nhân bùn đất bám chặt trước ngực
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #bian #tamlinh
```

### Phần 6/10 — Soi gương, thấy hình nhân bùn đất bám chặt trước ngực

`06-hinh-nhan-trong-guong.mp4` · 38s · cảnh 06.2, 06.3, 06.4, 06.5 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Đêm soi vào gương tủ, Hà không còn thấy bóng mình, chỉ thấy một hình nhân phủ đất bùn đang bám chặt lấy ngực. Từ chiếc rương gỗ lim khóa kín, tiếng khóc oe oe nghẹt thở vọng ra: “Bách ơi, cứu lấy con mình với!” Chiếc khóa đồng tự bung chốt, và Bách hiểu chẳng thứ khoa học nào giải thích nổi tai họa trong ngôi nhà này nữa.
Nếu là Bách, bạn sẽ làm gì tiếp theo?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #kinhdi #guongma
```

**YouTube Shorts — tiêu đề** (92/100 ký tự)

```text
Soi gương thấy hình nhân bùn đất, rương khóa kín vọng ra tiếng trẻ khóc | Oán Thai Đòi Mẹ P6
```

**YouTube Shorts — mô tả**

```text
Đêm soi vào gương tủ, Hà không còn thấy bóng mình, chỉ thấy một hình nhân phủ đất bùn đang bám chặt lấy ngực. Từ chiếc rương gỗ lim khóa kín, tiếng khóc oe oe nghẹt thở vọng ra: “Bách ơi, cứu lấy con mình với!” Chiếc khóa đồng tự bung chốt, và Bách hiểu chẳng thứ khoa học nào giải thích nổi tai họa trong ngôi nhà này nữa.

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 7: Mở túi ra mới biết tượng thật vẫn ở nhà với vợ

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
Đêm soi vào gương tủ, Hà không còn thấy bóng mình, chỉ thấy một hình nhân phủ đất bùn đang bám chặt lấy ngực. Từ chiếc rương gỗ lim khóa kín, tiếng khóc oe oe nghẹt thở vọng ra: “Bách ơi, cứu lấy con mình với!” Chiếc khóa đồng tự bung chốt, và Bách hiểu chẳng thứ khoa học nào giải thích nổi tai họa trong ngôi nhà này nữa.

Nếu là Bách, bạn sẽ làm gì tiếp theo? 👇
👉 Xem tiếp Phần 7: Mở túi ra mới biết tượng thật vẫn ở nhà với vợ
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #kinhdi #guongma
```

### Phần 7/10 — Mở túi ra mới biết tượng thật vẫn ở nhà với vợ

`07-ke-dieu-ho-ly-son.mp4` · 29s · cảnh 09.3, 09.4, 09.5 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Từ phía sau bộ hài cốt trong lò, vong hồn bà Lụa hiện lên, tuyệt vọng lắc đầu chỉ vào chiếc túi vải trên tay Bách. Mở túi ra, cả hai chết điếng: thứ mang tới lò chỉ là khối đất nặn giả đang tan thành bùn, còn pho tượng thật vẫn nằm ở nhà bên cạnh Hà. “Trúng kế điệu hổ ly sơn của nó rồi! Nó định ra tay đúng canh ba đêm nay đấy!”
Ở nhà một mình với pho tượng thật, Hà sẽ ra sao?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #plottwist #kinhdi
```

**YouTube Shorts — tiêu đề** (87/100 ký tự)

```text
Mang tượng về trấn lại lò, mở túi ra mới biết tượng thật vẫn ở nhà | Oán Thai Đòi Mẹ P7
```

**YouTube Shorts — mô tả**

```text
Từ phía sau bộ hài cốt trong lò, vong hồn bà Lụa hiện lên, tuyệt vọng lắc đầu chỉ vào chiếc túi vải trên tay Bách. Mở túi ra, cả hai chết điếng: thứ mang tới lò chỉ là khối đất nặn giả đang tan thành bùn, còn pho tượng thật vẫn nằm ở nhà bên cạnh Hà. “Trúng kế điệu hổ ly sơn của nó rồi! Nó định ra tay đúng canh ba đêm nay đấy!”

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 8: Đập vỡ tượng đất là mất cả hai mẹ con

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
Từ phía sau bộ hài cốt trong lò, vong hồn bà Lụa hiện lên, tuyệt vọng lắc đầu chỉ vào chiếc túi vải trên tay Bách. Mở túi ra, cả hai chết điếng: thứ mang tới lò chỉ là khối đất nặn giả đang tan thành bùn, còn pho tượng thật vẫn nằm ở nhà bên cạnh Hà. “Trúng kế điệu hổ ly sơn của nó rồi! Nó định ra tay đúng canh ba đêm nay đấy!”

Ở nhà một mình với pho tượng thật, Hà sẽ ra sao? 👇
👉 Xem tiếp Phần 8: Đập vỡ tượng đất là mất cả hai mẹ con
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #plottwist #kinhdi
```

### Phần 8/10 — Đập vỡ tượng đất là mất cả hai mẹ con

`08-dap-vo-tuong-mat-ca-hai.mp4` · 30s · cảnh 11.1, 11.2, 11.3 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Bách vớ chiếc búa gỗ định đập tan pho tượng, thầy Phong lao tới chụp chặt cổ tay anh: “Dừng tay lại ngay! Giọt máu của vợ cậu đã nối liền pho tượng với cái thai rồi.” Đập vỡ tượng là hại chết vợ con, mà để yên tới 3 giờ sáng thì đứa bé trong bụng sẽ bị Oán Thai cướp mất.
Nếu là Bách, bạn sẽ chọn thế nào?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #plottwist #tamlinh
```

**YouTube Shorts — tiêu đề** (92/100 ký tự)

```text
Định đập vỡ tượng đất cứu vợ, thầy pháp hét dừng tay: mất cả hai mẹ con | Oán Thai Đòi Mẹ P8
```

**YouTube Shorts — mô tả**

```text
Bách vớ chiếc búa gỗ định đập tan pho tượng, thầy Phong lao tới chụp chặt cổ tay anh: “Dừng tay lại ngay! Giọt máu của vợ cậu đã nối liền pho tượng với cái thai rồi.” Đập vỡ tượng là hại chết vợ con, mà để yên tới 3 giờ sáng thì đứa bé trong bụng sẽ bị Oán Thai cướp mất.

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 9: Người cha xin nhận lời nguyền thay vợ con

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
Bách vớ chiếc búa gỗ định đập tan pho tượng, thầy Phong lao tới chụp chặt cổ tay anh: “Dừng tay lại ngay! Giọt máu của vợ cậu đã nối liền pho tượng với cái thai rồi.” Đập vỡ tượng là hại chết vợ con, mà để yên tới 3 giờ sáng thì đứa bé trong bụng sẽ bị Oán Thai cướp mất.

Nếu là Bách, bạn sẽ chọn thế nào? 👇
👉 Xem tiếp Phần 9: Người cha xin nhận lời nguyền thay vợ con
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #plottwist #tamlinh
```

### Phần 9/10 — Người cha xin nhận lời nguyền thay vợ con

`09-nguoi-cha-nhan-thay.mp4` · 50s · cảnh 11.5, 11.6, 12.1, 12.2, 12.3 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
“Thầy Phong, nếu không đập vỡ tượng được thì có cách nào chuyển sợi dây nối mạng từ vợ tôi sang người tôi không hả thầy?” Sợi chỉ đỏ được tháo khỏi cổ tay vợ, buộc sang cổ tay chồng, chữ Mẫu trong huyết ấn đổi thành chữ Phụ. Hà bừng tỉnh, níu chặt vạt áo Bách: “Đừng làm thế mà Bách ơi! Em van anh đừng nhận nó vào người.”
Câu nói nào làm bạn rưng rưng nhất?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#oanthaidoime #phimkinhdi #truyenma #tinhcha #camdong
```

**YouTube Shorts — tiêu đề** (81/100 ký tự)

```text
Người cha xin nhận lời nguyền thay vợ con, vợ níu áo van xin | Oán Thai Đòi Mẹ P9
```

**YouTube Shorts — mô tả**

```text
“Thầy Phong, nếu không đập vỡ tượng được thì có cách nào chuyển sợi dây nối mạng từ vợ tôi sang người tôi không hả thầy?” Sợi chỉ đỏ được tháo khỏi cổ tay vợ, buộc sang cổ tay chồng, chữ Mẫu trong huyết ấn đổi thành chữ Phụ. Hà bừng tỉnh, níu chặt vạt áo Bách: “Đừng làm thế mà Bách ơi! Em van anh đừng nhận nó vào người.”

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
👉 Xem tiếp Phần 10: “Sinh con ra nhớ đặt tên con là Bình An”

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
“Thầy Phong, nếu không đập vỡ tượng được thì có cách nào chuyển sợi dây nối mạng từ vợ tôi sang người tôi không hả thầy?” Sợi chỉ đỏ được tháo khỏi cổ tay vợ, buộc sang cổ tay chồng, chữ Mẫu trong huyết ấn đổi thành chữ Phụ. Hà bừng tỉnh, níu chặt vạt áo Bách: “Đừng làm thế mà Bách ơi! Em van anh đừng nhận nó vào người.”

Câu nói nào làm bạn rưng rưng nhất? 👇
👉 Xem tiếp Phần 10: “Sinh con ra nhớ đặt tên con là Bình An”
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #tinhcha #camdong
```

### Phần 10/10 — “Sinh con ra nhớ đặt tên con là Bình An”

`10-dat-ten-con-la-binh-an.mp4` · 30s · cảnh 13.2, 13.3, 13.4 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Giữ chặt pho tượng trong tay, Bách dặn vợ: “Hà ơi, sinh con ra nhớ đặt tên con là Bình An em nhé!” Đúng lúc ấy, vong hồn bà Lụa lao tới ôm chầm lấy tượng đất, tự nguyện hút ngược tử khí về mình để chuộc lỗi. Người mẹ làm gốm năm xưa mỉm cười thanh thản, cùng đứa con tội lỗi hóa thành một khối đất câm lặng mãi mãi.
Bà Lụa có xứng đáng được tha thứ không?

🎬 Xem trọn bộ 14 phút trên kênh YouTube.
#oanthaidoime #phimkinhdi #truyenma #camdong #tinhcha
```

**YouTube Shorts — tiêu đề** (81/100 ký tự)

```text
Giữ chặt tượng đất, người cha dặn vợ đặt tên con là Bình An | Oán Thai Đòi Mẹ P10
```

**YouTube Shorts — mô tả**

```text
Giữ chặt pho tượng trong tay, Bách dặn vợ: “Hà ơi, sinh con ra nhớ đặt tên con là Bình An em nhé!” Đúng lúc ấy, vong hồn bà Lụa lao tới ôm chầm lấy tượng đất, tự nguyện hút ngược tử khí về mình để chuộc lỗi. Người mẹ làm gốm năm xưa mỉm cười thanh thản, cùng đứa con tội lỗi hóa thành một khối đất câm lặng mãi mãi.

🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”
🎬 Xem trọn bộ 14 phút trên kênh YouTube.

#Shorts #oanthaidoime #phimkinhdi #truyenma
```

**Facebook Reels**

```text
Giữ chặt pho tượng trong tay, Bách dặn vợ: “Hà ơi, sinh con ra nhớ đặt tên con là Bình An em nhé!” Đúng lúc ấy, vong hồn bà Lụa lao tới ôm chầm lấy tượng đất, tự nguyện hút ngược tử khí về mình để chuộc lỗi. Người mẹ làm gốm năm xưa mỉm cười thanh thản, cùng đứa con tội lỗi hóa thành một khối đất câm lặng mãi mãi.

Bà Lụa có xứng đáng được tha thứ không? 👇
🎬 Xem trọn bộ 14 phút trên kênh YouTube.
🎬 Full phim 14 phút có trên kênh YouTube, tìm “Oán Thai Đòi Mẹ”

#OanThaiDoiMe #PhimKinhDi #TruyenMa #TamLinh #camdong #tinhcha
```
