# Ma Da Đầm Sen: Lời Nguyền Tháng Bảy — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **các cảnh hay nhất** của phim 15 phút: **11 phần dọc 9:16**, không phải cả phim. Mỗi phần là một khoảnh khắc rùng rợn, bí ẩn hoặc một cú lật, dài 30–60 giây (mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger), đăng nối tiếp theo thứ tự truyện.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn tím than “MA DA ĐẦM SEN • PHẦN N” và câu hook ở trên khung phim; phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chính tả và tên riêng sửa theo `PHAN_CANH_OMNI.json`. Câu Omni nói khác kịch bản thì phụ đề theo tiếng thật.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm); câu Omni nói lặp ở cuối clip bị cắt bỏ.
- **Kết quả:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; lịch đăng và caption TikTok / YouTube / Facebook của mọi phần nằm trong `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ma-da-dam-sen            # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ma-da-dam-sen --only 3   # một phần
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py ma-da-dam-sen --captions   # chỉ ghi lại README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-dam-sen-doi-mot-mang-nguoi.mp4`](01-dam-sen-doi-mot-mang-nguoi.mp4) | Tháng bảy nào đầm sen cũng đòi một mạng người | 01.1, 01.2, 01.3, 01.4, 01.5, 01.6 | 52s | Thứ Bảy 14/11 – 11:00 |  |
| 2 | [`02-vet-ngon-tay-o-co-chan.mp4`](02-vet-ngon-tay-o-co-chan.mp4) | Cổ chân em trai hằn vết ngón tay ai nắm chặt | 02.2, 02.3, 02.4, 02.5, 02.6 | 44s | Thứ Bảy 14/11 – 19:00 |  |
| 3 | [`03-giong-con-gai-goi-ten.mp4`](03-giong-con-gai-goi-ten.mp4) | Nửa đêm, giọng con gái dưới đầm gọi tên em trai | 03.1, 03.2, 03.3, 03.4, 03.5, 03.6 | 50s | Chủ Nhật 15/11 – 11:00 | ⭐ |
| 4 | [`04-dau-chan-uot-vao-giuong.mp4`](04-dau-chan-uot-vao-giuong.mp4) | Dấu chân ướt từ đầm vào tận giường em trai | 04.1, 04.2, 04.3, 04.4 | 34s | Chủ Nhật 15/11 – 19:00 |  |
| 5 | [`05-nen-tat-tu-mep-nuoc.mp4`](05-nen-tat-tu-mep-nuoc.mp4) | Mười hai ngọn nến tắt dần từ phía mép nước | 06.2, 06.3, 06.4, 06.5, 06.6 | 41s | Thứ Hai 16/11 – 11:00 | ⭐ |
| 6 | [`06-ca-lang-dung-nhin.mp4`](06-ca-lang-dung-nhin.mp4) | Cả làng cầm đuốc đứng nhìn cô gái chìm xuống đầm | 08.3, 08.4, 08.5, 08.6 | 36s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-dem-mua-ba-muoi-nam-truoc.mp4`](07-dem-mua-ba-muoi-nam-truoc.mp4) | Đêm mưa ba mươi năm trước, không ai cứu Thắm | 09.1, 09.2, 09.3, 09.4, 09.5 | 42s | Thứ Ba 17/11 – 11:00 |  |
| 8 | [`08-dem-ram-chai-dau.mp4`](08-dem-ram-chai-dau.mp4) | Đêm rằm, em trai chải đầu bằng trâm bạc như con gái | 10.1, 10.2, 10.3, 10.4 | 35s | Thứ Ba 17/11 – 19:00 | ⭐ |
| 9 | [`09-hop-trau-duoi-day-dam.mp4`](09-hop-trau-duoi-day-dam.mp4) | Ma da chỉ xuống bùn, dưới đó là hộp trầu nhà trưởng thôn | 10.5, 10.6, 11.1, 11.2, 11.3 | 43s | Thứ Tư 18/11 – 11:00 |  |
| 10 | [`10-ong-ly-bi-goi-ten.mp4`](10-ong-ly-bi-goi-ten.mp4) | Ma da gọi đúng tên cúng cơm của ông trưởng thôn | 12.1, 12.2, 12.3, 12.4 | 35s | Thứ Tư 18/11 – 19:00 |  |
| 11 | [`11-bong-nguoi-thu-hai.mp4`](11-bong-nguoi-thu-hai.mp4) | Một năm sau, góc đầm lại có một bóng người khác | 15.3, 15.4, 15.5, 15.6 | 37s | Thứ Năm 19/11 – 11:00 |  |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Ma Da Đầm Sen”. Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả ở phần caption bên dưới; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption; tắt phụ đề tự động vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00), 3 nền tảng cùng giờ, bắt đầu Thứ Bảy 14/11. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Ghi chú bản short

- **Chọn cảnh:** 11 khoảnh khắc mạnh nhất (khoảng 8,7 phút clip thô trên 15 phút phim). Cuộc gặp ông Lý ở cảnh 5, Khôi mất tích giữa trưa, lời thú tội trước sân đình và lễ thả đèn hoa đăng chỉ có trong bản FULL.
- **Phụ đề:** đã nghe thử cả 90 clip bằng Whisper (13/11): thoại khớp `PHAN_CANH_OMNI.json`, nên phụ đề lấy chính tả và tên riêng theo kịch bản. `subtitle_replace` còn trống; điền sau khi xem bản Whisper nếu còn chữ nghe nhầm (Whisper hay nghe “ma da” thành “ma ra”, “trâm” thành “châm”).
- **Thoại bắt đầu muộn:** ở clip 11.3 (phần 9) và 15.3 (phần 11), lời thoại bắt đầu khoảng giây thứ 3. Whisper bản nhanh bịa câu chào kênh ở hai clip này, nên bản phụ đề trong `_whisper/` là bản nghe lại bằng faster-whisper có lọc VAD (đã đúng lời).
- **Logo đài truyền hình** Omni tự vẽ ở góc phải clip 05.4, từ khoảng giây 6,3 đến hết clip. Short không dùng clip này; **bản FULL vẫn còn logo** (khoảng 04:36–04:40), nên render lại hoặc xoá logo trước khi đăng phim dài.

## Caption từng phần (copy dán)

### Phần 1/11 — Tháng bảy nào đầm sen cũng đòi một mạng người

`01-dam-sen-doi-mot-mang-nguoi.mp4` · 52s · cảnh 01.1, 01.2, 01.3, 01.4, 01.5, 01.6 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
“Làng Hạ Liên có đầm sen đẹp nhất vùng, nhưng cứ vào tháng bảy âm lịch, đầm lại đòi đúng một mạng người.” Ngân vừa về quê đã thấy một cô gái áo trắng đứng ngập nước giữa đầm sen, im lìm nhìn về phía mình. Chớp mắt, bóng trắng biến mất, chỉ còn một hàng dấu chân trần ướt sũng dẫn thẳng về làng.
Nếu là Ngân, bạn có dám đi theo hàng dấu chân ấy không?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #mada #langque
```

**YouTube Shorts — tiêu đề** (97/100 ký tự)

```text
Tháng bảy nào đầm sen cũng đòi một mạng người, cô gái áo trắng giữa đầm là ai? | Ma Da Đầm Sen P1
```

**YouTube Shorts — mô tả**

```text
“Làng Hạ Liên có đầm sen đẹp nhất vùng, nhưng cứ vào tháng bảy âm lịch, đầm lại đòi đúng một mạng người.” Ngân vừa về quê đã thấy một cô gái áo trắng đứng ngập nước giữa đầm sen, im lìm nhìn về phía mình. Chớp mắt, bóng trắng biến mất, chỉ còn một hàng dấu chân trần ướt sũng dẫn thẳng về làng.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 2: Cổ chân em trai hằn vết ngón tay ai nắm chặt

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
“Làng Hạ Liên có đầm sen đẹp nhất vùng, nhưng cứ vào tháng bảy âm lịch, đầm lại đòi đúng một mạng người.” Ngân vừa về quê đã thấy một cô gái áo trắng đứng ngập nước giữa đầm sen, im lìm nhìn về phía mình. Chớp mắt, bóng trắng biến mất, chỉ còn một hàng dấu chân trần ướt sũng dẫn thẳng về làng.

Nếu là Ngân, bạn có dám đi theo hàng dấu chân ấy không? 👇
👉 Xem tiếp Phần 2: Cổ chân em trai hằn vết ngón tay ai nắm chặt
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #mada #langque
```

### Phần 2/11 — Cổ chân em trai hằn vết ngón tay ai nắm chặt

`02-vet-ngon-tay-o-co-chan.mp4` · 44s · cảnh 02.2, 02.3, 02.4, 02.5, 02.6 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Bà Hạnh dặn: “Nhớ lời bà, tháng bảy này tối đến tuyệt đối không được bén mảng ra gần đầm sen.” Khôi cười xòa bảo chuyện ma da chỉ để dọa trẻ con, nhưng cả tuần nay đêm nào cậu cũng mơ thấy mình đang chìm. Rồi Ngân thấy trên cổ chân em một vệt bầm tím, hằn rõ như vết ngón tay ai đó vừa nắm chặt.
Bà Hạnh biết điều gì mà mặt cắt không còn giọt máu?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #tamlinh #mada
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
Em trai cười chuyện ma da, cổ chân lại hằn vết ngón tay lạ | Ma Da Đầm Sen P2
```

**YouTube Shorts — mô tả**

```text
Bà Hạnh dặn: “Nhớ lời bà, tháng bảy này tối đến tuyệt đối không được bén mảng ra gần đầm sen.” Khôi cười xòa bảo chuyện ma da chỉ để dọa trẻ con, nhưng cả tuần nay đêm nào cậu cũng mơ thấy mình đang chìm. Rồi Ngân thấy trên cổ chân em một vệt bầm tím, hằn rõ như vết ngón tay ai đó vừa nắm chặt.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 3: Nửa đêm, giọng con gái dưới đầm gọi tên em trai

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Bà Hạnh dặn: “Nhớ lời bà, tháng bảy này tối đến tuyệt đối không được bén mảng ra gần đầm sen.” Khôi cười xòa bảo chuyện ma da chỉ để dọa trẻ con, nhưng cả tuần nay đêm nào cậu cũng mơ thấy mình đang chìm. Rồi Ngân thấy trên cổ chân em một vệt bầm tím, hằn rõ như vết ngón tay ai đó vừa nắm chặt.

Bà Hạnh biết điều gì mà mặt cắt không còn giọt máu? 👇
👉 Xem tiếp Phần 3: Nửa đêm, giọng con gái dưới đầm gọi tên em trai
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #tamlinh #mada
```

### Phần 3/11 — Nửa đêm, giọng con gái dưới đầm gọi tên em trai

`03-giong-con-gai-goi-ten.mp4` · 50s · cảnh 03.1, 03.2, 03.3, 03.4, 03.5, 03.6 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Nửa đêm, Khôi choàng tỉnh vì giọng con gái ngoài đầm: “Khôi ơi, dưới đầm mát lắm, xuống đây với em đi.” Cậu bước ra như bị ai giật dây, mắt mở trừng trừng. Ngân kéo được em lại khi nước đã ngập đến đầu gối, nhưng ngay chỗ em vừa đứng, mặt nước nổi lên một nắm tóc dài đen nhánh.
Nghe tiếng gọi tên lúc nửa đêm, bạn có dám trả lời không?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #kinhdi #nuadem
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
Nửa đêm, giọng con gái dưới đầm sen gọi em trai xuống nước | Ma Da Đầm Sen P3
```

**YouTube Shorts — mô tả**

```text
Nửa đêm, Khôi choàng tỉnh vì giọng con gái ngoài đầm: “Khôi ơi, dưới đầm mát lắm, xuống đây với em đi.” Cậu bước ra như bị ai giật dây, mắt mở trừng trừng. Ngân kéo được em lại khi nước đã ngập đến đầu gối, nhưng ngay chỗ em vừa đứng, mặt nước nổi lên một nắm tóc dài đen nhánh.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 4: Dấu chân ướt từ đầm vào tận giường em trai

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Nửa đêm, Khôi choàng tỉnh vì giọng con gái ngoài đầm: “Khôi ơi, dưới đầm mát lắm, xuống đây với em đi.” Cậu bước ra như bị ai giật dây, mắt mở trừng trừng. Ngân kéo được em lại khi nước đã ngập đến đầu gối, nhưng ngay chỗ em vừa đứng, mặt nước nổi lên một nắm tóc dài đen nhánh.

Nghe tiếng gọi tên lúc nửa đêm, bạn có dám trả lời không? 👇
👉 Xem tiếp Phần 4: Dấu chân ướt từ đầm vào tận giường em trai
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #kinhdi #nuadem
```

### Phần 4/11 — Dấu chân ướt từ đầm vào tận giường em trai

`04-dau-chan-uot-vao-giuong.mp4` · 34s · cảnh 04.1, 04.2, 04.3, 04.4 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Sáng hôm sau, từ mép đầm vào tận giường Khôi là một hàng dấu chân trần còn ướt, nhỏ nhắn như chân con gái. Trên gối là một chiếc lá sen đẫm nước, cuống lá quấn mấy sợi tóc dài không phải của ai trong nhà. Bà Hạnh nói: “Nó chọn thằng Khôi rồi con ạ. Ba mươi năm nay, tháng bảy nào nó cũng về đòi đúng một người.”
Vì sao nó lại chọn Khôi?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #kinhdi #langque
```

**YouTube Shorts — tiêu đề** (95/100 ký tự)

```text
Dấu chân con gái ướt sũng từ đầm vào tận giường, trên gối là lá sen quấn tóc | Ma Da Đầm Sen P4
```

**YouTube Shorts — mô tả**

```text
Sáng hôm sau, từ mép đầm vào tận giường Khôi là một hàng dấu chân trần còn ướt, nhỏ nhắn như chân con gái. Trên gối là một chiếc lá sen đẫm nước, cuống lá quấn mấy sợi tóc dài không phải của ai trong nhà. Bà Hạnh nói: “Nó chọn thằng Khôi rồi con ạ. Ba mươi năm nay, tháng bảy nào nó cũng về đòi đúng một người.”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 5: Mười hai ngọn nến tắt dần từ phía mép nước

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Sáng hôm sau, từ mép đầm vào tận giường Khôi là một hàng dấu chân trần còn ướt, nhỏ nhắn như chân con gái. Trên gối là một chiếc lá sen đẫm nước, cuống lá quấn mấy sợi tóc dài không phải của ai trong nhà. Bà Hạnh nói: “Nó chọn thằng Khôi rồi con ạ. Ba mươi năm nay, tháng bảy nào nó cũng về đòi đúng một người.”

Vì sao nó lại chọn Khôi? 👇
👉 Xem tiếp Phần 5: Mười hai ngọn nến tắt dần từ phía mép nước
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #kinhdi #langque
```

### Phần 5/11 — Mười hai ngọn nến tắt dần từ phía mép nước

`05-nen-tat-tu-mep-nuoc.mp4` · 41s · cảnh 06.2, 06.3, 06.4, 06.5, 06.6 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
Ngân đếm được mười hai ngọn nến cháy đều quanh mâm cúng. Rồi từng ngọn tắt phụt, lần lượt từ phía gần nước nhất: “Bà ơi, đứng dậy đi bà! Có cái gì đang đi lên từ dưới nước kìa!” Bộ quần áo giấy trắng ướt sũng từ từ đứng thẳng lên, còn trong nhà, Khôi đang ngủ bỗng cười khúc khích bằng giọng một cô gái lạ.
Khoảnh khắc nào làm bạn nổi da gà nhất?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #kinhdi #tamlinh
```

**YouTube Shorts — tiêu đề** (85/100 ký tự)

```text
Mười hai ngọn nến tắt dần từ mép nước, bộ áo giấy cúng tự đứng dậy | Ma Da Đầm Sen P5
```

**YouTube Shorts — mô tả**

```text
Ngân đếm được mười hai ngọn nến cháy đều quanh mâm cúng. Rồi từng ngọn tắt phụt, lần lượt từ phía gần nước nhất: “Bà ơi, đứng dậy đi bà! Có cái gì đang đi lên từ dưới nước kìa!” Bộ quần áo giấy trắng ướt sũng từ từ đứng thẳng lên, còn trong nhà, Khôi đang ngủ bỗng cười khúc khích bằng giọng một cô gái lạ.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 6: Cả làng cầm đuốc đứng nhìn cô gái chìm xuống đầm

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Ngân đếm được mười hai ngọn nến cháy đều quanh mâm cúng. Rồi từng ngọn tắt phụt, lần lượt từ phía gần nước nhất: “Bà ơi, đứng dậy đi bà! Có cái gì đang đi lên từ dưới nước kìa!” Bộ quần áo giấy trắng ướt sũng từ từ đứng thẳng lên, còn trong nhà, Khôi đang ngủ bỗng cười khúc khích bằng giọng một cô gái lạ.

Khoảnh khắc nào làm bạn nổi da gà nhất? 👇
👉 Xem tiếp Phần 6: Cả làng cầm đuốc đứng nhìn cô gái chìm xuống đầm
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #kinhdi #tamlinh
```

### Phần 6/11 — Cả làng cầm đuốc đứng nhìn cô gái chìm xuống đầm

`06-ca-lang-dung-nhin.mp4` · 36s · cảnh 08.3, 08.4, 08.5, 08.6 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Bà Hạnh kể lại: năm ấy hòm công đức mất sạch, ông Lý bảo chính mắt ông thấy Thắm lẻn vào đình. “Cả làng đuổi theo nó ra tận bờ đầm. Ông nhà bà cũng cầm đuốc đứng đó, nhìn nó khuất dưới đầm mà không ai giúp.” Ngân chợt hiểu: những người bị đầm bắt suốt ba mươi năm qua đều là con cháu của những kẻ đứng trên bờ đêm ấy.
Đứng nhìn mà không cứu, có phải cũng là có tội?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #plottwist #oankhuat
```

**YouTube Shorts — tiêu đề** (89/100 ký tự)

```text
Bí mật 30 năm: cả làng cầm đuốc đứng nhìn cô gái mồ côi chìm xuống đầm | Ma Da Đầm Sen P6
```

**YouTube Shorts — mô tả**

```text
Bà Hạnh kể lại: năm ấy hòm công đức mất sạch, ông Lý bảo chính mắt ông thấy Thắm lẻn vào đình. “Cả làng đuổi theo nó ra tận bờ đầm. Ông nhà bà cũng cầm đuốc đứng đó, nhìn nó khuất dưới đầm mà không ai giúp.” Ngân chợt hiểu: những người bị đầm bắt suốt ba mươi năm qua đều là con cháu của những kẻ đứng trên bờ đêm ấy.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 7: Đêm mưa ba mươi năm trước, không ai cứu Thắm

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Bà Hạnh kể lại: năm ấy hòm công đức mất sạch, ông Lý bảo chính mắt ông thấy Thắm lẻn vào đình. “Cả làng đuổi theo nó ra tận bờ đầm. Ông nhà bà cũng cầm đuốc đứng đó, nhìn nó khuất dưới đầm mà không ai giúp.” Ngân chợt hiểu: những người bị đầm bắt suốt ba mươi năm qua đều là con cháu của những kẻ đứng trên bờ đêm ấy.

Đứng nhìn mà không cứu, có phải cũng là có tội? 👇
👉 Xem tiếp Phần 7: Đêm mưa ba mươi năm trước, không ai cứu Thắm
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #plottwist #oankhuat
```

### Phần 7/11 — Đêm mưa ba mươi năm trước, không ai cứu Thắm

`07-dem-mua-ba-muoi-nam-truoc.mp4` · 42s · cảnh 09.1, 09.2, 09.3, 09.4, 09.5 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Ba mươi năm trước, Thắm chạy trối chết dọc bờ đầm, phía sau là cả một rừng đuốc: “Cháu không lấy! Cháu thề có trời đất, cháu không hề động vào hòm công đức của đình!” Không ai tin cô, và người hô to nhất chính là ông Lý thời trẻ. Một bàn tay nhô lên khỏi mặt nước như cầu cứu, nhưng hàng chục ngọn đuốc trên bờ không ai nhúc nhích.
Nếu đứng trên bờ đêm ấy, bạn có dám lên tiếng không?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #oankhuat #tamlinh
```

**YouTube Shorts — tiêu đề** (89/100 ký tự)

```text
Bị vu trộm tiền công đức, cô gái mồ côi chìm giữa đầm sen không ai cứu | Ma Da Đầm Sen P7
```

**YouTube Shorts — mô tả**

```text
Ba mươi năm trước, Thắm chạy trối chết dọc bờ đầm, phía sau là cả một rừng đuốc: “Cháu không lấy! Cháu thề có trời đất, cháu không hề động vào hòm công đức của đình!” Không ai tin cô, và người hô to nhất chính là ông Lý thời trẻ. Một bàn tay nhô lên khỏi mặt nước như cầu cứu, nhưng hàng chục ngọn đuốc trên bờ không ai nhúc nhích.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 8: Đêm rằm, em trai chải đầu bằng trâm bạc như con gái

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Ba mươi năm trước, Thắm chạy trối chết dọc bờ đầm, phía sau là cả một rừng đuốc: “Cháu không lấy! Cháu thề có trời đất, cháu không hề động vào hòm công đức của đình!” Không ai tin cô, và người hô to nhất chính là ông Lý thời trẻ. Một bàn tay nhô lên khỏi mặt nước như cầu cứu, nhưng hàng chục ngọn đuốc trên bờ không ai nhúc nhích.

Nếu đứng trên bờ đêm ấy, bạn có dám lên tiếng không? 👇
👉 Xem tiếp Phần 8: Đêm rằm, em trai chải đầu bằng trâm bạc như con gái
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #oankhuat #tamlinh
```

### Phần 8/11 — Đêm rằm, em trai chải đầu bằng trâm bạc như con gái

`08-dem-ram-chai-dau.mp4` · 35s · cảnh 10.1, 10.2, 10.3, 10.4 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Đêm rằm tháng bảy, Khôi bỗng hết sốt, ngồi dậy chải đầu bằng chiếc trâm bạc như một cô gái: “Chị ơi, cô ấy bảo đêm nay là đêm cuối cùng rồi. Em phải xuống trả lại cho cô ấy.” Cậu đi thẳng ra đầm, người nặng trịch và lạnh như khúc gỗ ngâm nước. Ngân hít một hơi thật sâu rồi lội xuống theo em.
Khôi phải “trả lại” thứ gì cho cô ấy?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #kinhdi #ramthangbay
```

**YouTube Shorts — tiêu đề** (89/100 ký tự)

```text
Đêm rằm tháng bảy, em trai chải đầu như con gái rồi đi thẳng xuống đầm | Ma Da Đầm Sen P8
```

**YouTube Shorts — mô tả**

```text
Đêm rằm tháng bảy, Khôi bỗng hết sốt, ngồi dậy chải đầu bằng chiếc trâm bạc như một cô gái: “Chị ơi, cô ấy bảo đêm nay là đêm cuối cùng rồi. Em phải xuống trả lại cho cô ấy.” Cậu đi thẳng ra đầm, người nặng trịch và lạnh như khúc gỗ ngâm nước. Ngân hít một hơi thật sâu rồi lội xuống theo em.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 9: Ma da chỉ xuống bùn, dưới đó là hộp trầu nhà trưởng thôn

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Đêm rằm tháng bảy, Khôi bỗng hết sốt, ngồi dậy chải đầu bằng chiếc trâm bạc như một cô gái: “Chị ơi, cô ấy bảo đêm nay là đêm cuối cùng rồi. Em phải xuống trả lại cho cô ấy.” Cậu đi thẳng ra đầm, người nặng trịch và lạnh như khúc gỗ ngâm nước. Ngân hít một hơi thật sâu rồi lội xuống theo em.

Khôi phải “trả lại” thứ gì cho cô ấy? 👇
👉 Xem tiếp Phần 9: Ma da chỉ xuống bùn, dưới đó là hộp trầu nhà trưởng thôn
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #kinhdi #ramthangbay
```

### Phần 9/11 — Ma da chỉ xuống bùn, dưới đó là hộp trầu nhà trưởng thôn

`09-hop-trau-duoi-day-dam.mp4` · 43s · cảnh 10.5, 10.6, 11.1, 11.2, 11.3 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
Dưới đáy đầm, Thắm lặng lẽ chỉ tay xuống lớp bùn, nơi Ngân chạm phải một chiếc hộp kim loại quấn chặt rễ sen và tóc dài. Trong hộp là bạc trắng của đình làng, nắp khắc hình con hạc, vật gia truyền nhà ông Lý. Ngân tìm đến tận nhà ông: “Hộp trầu nhà ông, tiền công đức của đình, nằm dưới đáy đầm ba mươi năm nay đấy!”
Bạn đoán ra ai là kẻ trộm từ lúc nào?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #plottwist #bian
```

**YouTube Shorts — tiêu đề** (84/100 ký tự)

```text
Ma da chỉ xuống bùn, dưới đáy đầm là hộp trầu nhà ông trưởng thôn | Ma Da Đầm Sen P9
```

**YouTube Shorts — mô tả**

```text
Dưới đáy đầm, Thắm lặng lẽ chỉ tay xuống lớp bùn, nơi Ngân chạm phải một chiếc hộp kim loại quấn chặt rễ sen và tóc dài. Trong hộp là bạc trắng của đình làng, nắp khắc hình con hạc, vật gia truyền nhà ông Lý. Ngân tìm đến tận nhà ông: “Hộp trầu nhà ông, tiền công đức của đình, nằm dưới đáy đầm ba mươi năm nay đấy!”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 10: Ma da gọi đúng tên cúng cơm của ông trưởng thôn

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Dưới đáy đầm, Thắm lặng lẽ chỉ tay xuống lớp bùn, nơi Ngân chạm phải một chiếc hộp kim loại quấn chặt rễ sen và tóc dài. Trong hộp là bạc trắng của đình làng, nắp khắc hình con hạc, vật gia truyền nhà ông Lý. Ngân tìm đến tận nhà ông: “Hộp trầu nhà ông, tiền công đức của đình, nằm dưới đáy đầm ba mươi năm nay đấy!”

Bạn đoán ra ai là kẻ trộm từ lúc nào? 👇
👉 Xem tiếp Phần 10: Ma da gọi đúng tên cúng cơm của ông trưởng thôn
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #plottwist #bian
```

### Phần 10/11 — Ma da gọi đúng tên cúng cơm của ông trưởng thôn

`10-ong-ly-bi-goi-ten.mp4` · 35s · cảnh 12.1, 12.2, 12.3, 12.4 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Đêm ấy, ngoài đầm có tiếng con gái gọi đúng tên cúng cơm của ông Lý, cái tên chẳng ai còn nhớ. Vệt nước loang từ cửa sổ vào tận đầu giường, rồi Thắm đứng lặng ngay cuối giường nhìn ông, không một lời oán trách. “Là tao lấy, Thắm ạ! Tao sợ quá nên mới đổ tội cho mày.”
Thắm có nên tha cho ông Lý không?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#madadamsen #truyenma #phimma #kinhdi #thutoi
```

**YouTube Shorts — tiêu đề** (92/100 ký tự)

```text
Nửa đêm ma da về đứng cuối giường, ông trưởng thôn khai ra tội ác 30 năm | Ma Da Đầm Sen P10
```

**YouTube Shorts — mô tả**

```text
Đêm ấy, ngoài đầm có tiếng con gái gọi đúng tên cúng cơm của ông Lý, cái tên chẳng ai còn nhớ. Vệt nước loang từ cửa sổ vào tận đầu giường, rồi Thắm đứng lặng ngay cuối giường nhìn ông, không một lời oán trách. “Là tao lấy, Thắm ạ! Tao sợ quá nên mới đổ tội cho mày.”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
👉 Xem tiếp Phần 11: Một năm sau, góc đầm lại có một bóng người khác

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Đêm ấy, ngoài đầm có tiếng con gái gọi đúng tên cúng cơm của ông Lý, cái tên chẳng ai còn nhớ. Vệt nước loang từ cửa sổ vào tận đầu giường, rồi Thắm đứng lặng ngay cuối giường nhìn ông, không một lời oán trách. “Là tao lấy, Thắm ạ! Tao sợ quá nên mới đổ tội cho mày.”

Thắm có nên tha cho ông Lý không? 👇
👉 Xem tiếp Phần 11: Một năm sau, góc đầm lại có một bóng người khác
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #kinhdi #thutoi
```

### Phần 11/11 — Một năm sau, góc đầm lại có một bóng người khác

`11-bong-nguoi-thu-hai.mp4` · 37s · cảnh 15.3, 15.4, 15.5, 15.6 · đăng Thứ Năm 19/11 – 11:00

**TikTok**

```text
Một năm sau, Khôi đứng bên bờ đầm cùng chị: “Chị thấy không, năm nay ai cũng bảo đầm sen đẹp nhất từ trước tới giờ. Chắc cô ấy vui lắm.” Ngân ra bến xe, ngoảnh lại thấy mặt đầm phẳng lặng như gương. Nhưng ở góc đầm xa nhất, một bóng người khác đang đứng ngập trong nước.
Bóng người thứ hai dưới đầm là ai?

🎬 Xem trọn bộ 15 phút trên kênh YouTube.
#madadamsen #truyenma #phimma #ketphim #mada
```

**YouTube Shorts — tiêu đề** (81/100 ký tự)

```text
Một năm sau lời nguyền, góc đầm sen lại có bóng người thứ hai | Ma Da Đầm Sen P11
```

**YouTube Shorts — mô tả**

```text
Một năm sau, Khôi đứng bên bờ đầm cùng chị: “Chị thấy không, năm nay ai cũng bảo đầm sen đẹp nhất từ trước tới giờ. Chắc cô ấy vui lắm.” Ngân ra bến xe, ngoảnh lại thấy mặt đầm phẳng lặng như gương. Nhưng ở góc đầm xa nhất, một bóng người khác đang đứng ngập trong nước.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”
🎬 Xem trọn bộ 15 phút trên kênh YouTube.

#Shorts #madadamsen #truyenma #phimma
```

**Facebook Reels**

```text
Một năm sau, Khôi đứng bên bờ đầm cùng chị: “Chị thấy không, năm nay ai cũng bảo đầm sen đẹp nhất từ trước tới giờ. Chắc cô ấy vui lắm.” Ngân ra bến xe, ngoảnh lại thấy mặt đầm phẳng lặng như gương. Nhưng ở góc đầm xa nhất, một bóng người khác đang đứng ngập trong nước.

Bóng người thứ hai dưới đầm là ai? 👇
🎬 Xem trọn bộ 15 phút trên kênh YouTube.
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Ma Da Đầm Sen”

#MaDaDamSen #TruyenMa #PhimMa #TamLinh #ketphim #mada
```
