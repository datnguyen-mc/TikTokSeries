# Biệt Đội Gara — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **12 khoảnh khắc hay nhất** của series 10 tập, không phải cả phim: cướp phá gara, biến hình, đua cứu em út, trùm Sói Xám lộ mặt, nghi oan trong nhà, mất giáp, rượt đuổi ở cảng và cái kết. Mỗi phần là một mạch liền 40–60 giây (4–6 clip liên tiếp), mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger, đăng nối tiếp theo thứ tự truyện.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn đỏ “BIỆT ĐỘI GARA • PHẦN N” và câu hook ở trên khung phim (cụm nhấn màu xanh băng); phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau, phần cuối đổi thành “XEM FULL PHIM”. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper, giọng miền Nam). Phim không có kịch bản trong repo nên phụ đề giữ chữ Whisper nghe được (`match_script: false`); tên riêng và chữ nghe nhầm sửa bằng `subtitle_replace` sau khi duyệt.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm); clip có đuôi nói lặp thì cắt trước đoạn lặp.
- **Đầu ra:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; lịch đăng và caption TikTok / YouTube / Facebook của mọi phần nằm trong `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py biet-doi-gara            # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py biet-doi-gara --only 3   # một phần
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py biet-doi-gara --captions # chỉ ghi lại README
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-cuop-pha-gara-giua-bua-com.mp4`](01-cuop-pha-gara-giua-bua-com.mp4) | Cướp phá cửa gara giữa bữa cơm, đòi bức thư của Bác Bảy | 02.1, 02.2, 02.3, 02.4, 02.5, 02.6 | 49s | Thứ Bảy 14/11 – 11:00 | ⭐ |
| 2 | [`02-loi-bay-khoi-dong.mp4`](02-loi-bay-khoi-dong.mp4) | “Lõi Bảy, khởi động!” Bốn anh em thợ máy biến hình | 03.3, 03.4, 03.5, 03.6 | 32s | Thứ Bảy 14/11 – 19:00 |  |
| 3 | [`03-buc-thu-rach-doi.mp4`](03-buc-thu-rach-doi.mp4) | Giành lại di thư Bác Bảy, ai ngờ chỉ còn một nửa | 04.4, 04.5, 04.6, 05.1 | 38s | Chủ Nhật 15/11 – 11:00 |  |
| 4 | [`04-cup-vo-dich-de-lam-gi.mp4`](04-cup-vo-dich-de-lam-gi.mp4) | Sắp về nhất, anh hỏi: Cúp vô địch để làm gì? | 10.5, 11.1, 11.2, 11.3 | 34s | Chủ Nhật 15/11 – 19:00 | ⭐ |
| 5 | [`05-soi-xam-thao-mat-na.mp4`](05-soi-xam-thao-mat-na.mp4) | Trùm Sói Xám tháo mặt nạ: sư huynh mất tích 15 năm | 20.3, 20.4, 20.6, 21.1 | 33s | Thứ Hai 16/11 – 11:00 |  |
| 6 | [`06-con-chip-trong-gang-tay.mp4`](06-con-chip-trong-gang-tay.mp4) | Nghi oan anh Hải phản bội, hóa ra là con chip nghe lén | 24.4, 24.5, 24.6, 25.1, 25.2, 25.3 | 49s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-khoi-bi-bat-coc.mp4`](07-khoi-bi-bat-coc.mp4) | Bị trùm Sói Xám bắt đi, cậu út kịp gài một con bọ | 26.6, 27.1, 27.2, 27.3, 27.4 | 39s | Thứ Ba 17/11 – 11:00 |  |
| 8 | [`08-lan-mat-loi-giap.mp4`](08-lan-mat-loi-giap.mp4) | Lan bị giật mất lõi giáp giữa cơn mưa | 29.3, 29.4, 29.5, 29.6, 30.1, 30.2 | 49s | Thứ Ba 17/11 – 19:00 |  |
| 9 | [`09-xe-bay-qua-dau-dich.mp4`](09-xe-bay-qua-dau-dich.mp4) | Xả nitro lõi đỏ, xe đua bay qua đầu xe địch | 39.2, 39.3, 39.4, 39.5, 39.6 | 36s | Thứ Tư 18/11 – 11:00 |  |
| 10 | [`10-luon-qua-gam-xe-cau.mp4`](10-luon-qua-gam-xe-cau.mp4) | Mất giáp vẫn lái xe của ba luồn qua gầm xe cẩu | 40.2, 40.3, 40.4, 40.5, 40.6 | 38s | Thứ Tư 18/11 – 19:00 |  |
| 11 | [`11-cao-bang-tro-lai.mp4`](11-cao-bang-tro-lai.mp4) | Tay trần giật lại lõi giáp: Cáo Băng trở lại | 43.2, 43.3, 43.4, 43.5, 43.6 | 33s | Thứ Năm 19/11 – 11:00 | ⭐ |
| 12 | [`12-ve-nha-an-com-di-con.mp4`](12-ve-nha-an-com-di-con.mp4) | Lời nhắn của người thầy khiến trùm phản diện quỳ khóc | 44.3, 44.4, 44.5, 44.6 | 38s | Thứ Năm 19/11 – 19:00 |  |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Biệt Đội Gara”. Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả ở dưới; điền link playlist trọn bộ 10 tập vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về tập 1.
- **Facebook Reels:** dán caption; tắt phụ đề tự động vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00), 3 nền tảng cùng giờ, bắt đầu 14/11. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Cần kiểm tra trước khi đăng

- **Hook và caption viết theo shot list của prompt**, không theo kịch bản (repo không có). Từ cảnh 07 trở đi shot list dùng khung câu mẫu (“tiếng gầm rú động cơ”, “không gian xưởng gara”…) cả ở cảnh thoại, nên hình thật có thể khác mô tả: xem lại từng phần, nhất là phần 4–12, và sửa caption nếu cảnh không khớp.
- **Chưa duyệt bản Whisper:** `subtitle_replace` và `fixes` đang để trống. Tên riêng dễ bị nghe sai: Thắng, Khôi, Hải, Minh, Tú, Hùng, Bác Bảy, Sói Xám, Găng Xám, Hắc Phong, Cáo Băng, Lõi Bảy. Ở clip 11.1 (phần 4) câu “Thắng không ăn!” là phanh không ăn, không phải tên anh cả.
- **Clip chưa render:** 11.4–11.6 và toàn bộ cảnh 12–15 (đoạn cứu Tú) chưa có, nên không có short nào từ đoạn này; phần 4 dừng ở câu “Cúp vô địch để làm gì khi mất đi người nhà?”.
- **Clip chỉ có prompt thô, không có shot list:** 16.5, 17.1, 18.1, 18.3, 19.2, 20.2, 21.2, 25.5, 28.6, 29.1, 30.3, 32.1, 33.4, 34.3, 36.1, 41.6, 43.1, 44.2, 45.4; clip 44.1 dùng prompt chung chung. Không short nào dùng các clip này.
- 10.6 bỏ khỏi phần 4: clip có phụ đề in cứng (“Lan: Tú mất lái rồi anh Thắng!”) và không có thoại.
- 20.5 bỏ khỏi phần 5: bản render cho anh Hải nói thoại của Hùng (“Lão giấu 5 chiếc lõi giáp…”); 20.2 cũng bị lỗi này. Nên render lại hai clip này trong phim full.

## Caption từng phần (copy dán)

### Phần 1/12 — Cướp phá cửa gara giữa bữa cơm, đòi bức thư của Bác Bảy

`01-cuop-pha-gara-giua-bua-com.mp4` · 49s · cảnh 02.1, 02.2, 02.3, 02.4, 02.5, 02.6 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
Cả nhà đang ăn cơm thì cửa cuốn gara bị xe tải giật bung, bốn tên Găng Xám tràn vào đòi chiếc hộp sắt chứa bức thư của Bác Bảy. Anh Hải cầm cờ lê đỡ đòn, Lan tung cước giữ xe của ba: “Đừng hòng đụng vô xe của ba tao, gãy răng ráng chịu nha mấy cưng!” Bức thư bị cướp mất, nhưng chiếc hộp vỡ ra năm khối lõi phát sáng…
Năm khối lõi phát sáng đó là gì nhỉ?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #giadinh #sieuanhhung
```

**YouTube Shorts — tiêu đề** (72/100 ký tự)

```text
Cướp phá cửa gara giữa bữa cơm chỉ để lấy một bức thư | Biệt Đội Gara P1
```

**YouTube Shorts — mô tả**

```text
Cả nhà đang ăn cơm thì cửa cuốn gara bị xe tải giật bung, bốn tên Găng Xám tràn vào đòi chiếc hộp sắt chứa bức thư của Bác Bảy. Anh Hải cầm cờ lê đỡ đòn, Lan tung cước giữ xe của ba: “Đừng hòng đụng vô xe của ba tao, gãy răng ráng chịu nha mấy cưng!” Bức thư bị cướp mất, nhưng chiếc hộp vỡ ra năm khối lõi phát sáng…

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 2: “Lõi Bảy, khởi động!” Bốn anh em thợ máy biến hình

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Cả nhà đang ăn cơm thì cửa cuốn gara bị xe tải giật bung, bốn tên Găng Xám tràn vào đòi chiếc hộp sắt chứa bức thư của Bác Bảy. Anh Hải cầm cờ lê đỡ đòn, Lan tung cước giữ xe của ba: “Đừng hòng đụng vô xe của ba tao, gãy răng ráng chịu nha mấy cưng!” Bức thư bị cướp mất, nhưng chiếc hộp vỡ ra năm khối lõi phát sáng…

Năm khối lõi phát sáng đó là gì nhỉ? 👇
👉 Xem tiếp Phần 2: “Lõi Bảy, khởi động!” Bốn anh em thợ máy biến hình
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #giadinh #sieuanhhung
```

### Phần 2/12 — “Lõi Bảy, khởi động!” Bốn anh em thợ máy biến hình

`02-loi-bay-khoi-dong.mp4` · 32s · cảnh 03.3, 03.4, 03.5, 03.6 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Nhớ lời Bác Bảy dặn phải bảo vệ nhau khi nhà gặp nạn, Thắng giơ cao nắm đấm: “Lõi Bảy, khởi động!” Giáp nano đỏ đen bọc kín người anh cả, rồi tới Lan, anh Hải và Khôi. Cả nhà lao đi đuổi theo xe tải cướp thư… còn Khôi vẫn lo nồi thịt kho chưa tắt bếp.
Bạn thích bộ giáp của ai nhất?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #bienhinh #sieuanhhung
```

**YouTube Shorts — tiêu đề** (85/100 ký tự)

```text
“Lõi Bảy, khởi động!” Bốn anh em thợ máy biến hình chiến binh giáp | Biệt Đội Gara P2
```

**YouTube Shorts — mô tả**

```text
Nhớ lời Bác Bảy dặn phải bảo vệ nhau khi nhà gặp nạn, Thắng giơ cao nắm đấm: “Lõi Bảy, khởi động!” Giáp nano đỏ đen bọc kín người anh cả, rồi tới Lan, anh Hải và Khôi. Cả nhà lao đi đuổi theo xe tải cướp thư… còn Khôi vẫn lo nồi thịt kho chưa tắt bếp.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 3: Giành lại di thư Bác Bảy, ai ngờ chỉ còn một nửa

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Nhớ lời Bác Bảy dặn phải bảo vệ nhau khi nhà gặp nạn, Thắng giơ cao nắm đấm: “Lõi Bảy, khởi động!” Giáp nano đỏ đen bọc kín người anh cả, rồi tới Lan, anh Hải và Khôi. Cả nhà lao đi đuổi theo xe tải cướp thư… còn Khôi vẫn lo nồi thịt kho chưa tắt bếp.

Bạn thích bộ giáp của ai nhất? 👇
👉 Xem tiếp Phần 3: Giành lại di thư Bác Bảy, ai ngờ chỉ còn một nửa
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #bienhinh #sieuanhhung
```

### Phần 3/12 — Giành lại di thư Bác Bảy, ai ngờ chỉ còn một nửa

`03-buc-thu-rach-doi.mp4` · 38s · cảnh 04.4, 04.5, 04.6, 05.1 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Thắng tung một cú đấm chặn đứng xe tải bọc thép, giật lại bức thư kẹt trên gương: “Định chạy đi đâu với thư của nhà tao?” Nhưng thư đã rách làm đôi, nửa trong tay chỉ còn dòng chữ về cảng container Sài Gòn và chiếc lõi thứ năm. Rồi một chùm đèn pha rọi tới, một cô gái lạ cầm máy dò bước xuống.
Nửa bức thư kia viết gì mà tụi cướp phải giành?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #dithu #plottwist
```

**YouTube Shorts — tiêu đề** (84/100 ký tự)

```text
Một cú đấm chặn đứng xe tải, giành lại di thư thì chỉ còn một nửa | Biệt Đội Gara P3
```

**YouTube Shorts — mô tả**

```text
Thắng tung một cú đấm chặn đứng xe tải bọc thép, giật lại bức thư kẹt trên gương: “Định chạy đi đâu với thư của nhà tao?” Nhưng thư đã rách làm đôi, nửa trong tay chỉ còn dòng chữ về cảng container Sài Gòn và chiếc lõi thứ năm. Rồi một chùm đèn pha rọi tới, một cô gái lạ cầm máy dò bước xuống.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 4: Sắp về nhất, anh hỏi: Cúp vô địch để làm gì?

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Thắng tung một cú đấm chặn đứng xe tải bọc thép, giật lại bức thư kẹt trên gương: “Định chạy đi đâu với thư của nhà tao?” Nhưng thư đã rách làm đôi, nửa trong tay chỉ còn dòng chữ về cảng container Sài Gòn và chiếc lõi thứ năm. Rồi một chùm đèn pha rọi tới, một cô gái lạ cầm máy dò bước xuống.

Nửa bức thư kia viết gì mà tụi cướp phải giành? 👇
👉 Xem tiếp Phần 4: Sắp về nhất, anh hỏi: Cúp vô địch để làm gì?
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #dithu #plottwist
```

### Phần 4/12 — Sắp về nhất, anh hỏi: Cúp vô địch để làm gì?

`04-cup-vo-dich-de-lam-gi.mp4` · 34s · cảnh 10.5, 11.1, 11.2, 11.3 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Tú, đứa em út của gara, bị ép đua chiếc xe gài khóa xung điện. Thắng dùng thân xe chặn chiếc bán tải chơi xấu: “Muốn đụng em tao hả? Qua tao đã!” Rồi xe Tú mất thắng lao về phía vực taluy, vạch đích chỉ còn 200 mét, và Thắng ngoái nhìn qua gương chiếu hậu.
Là bạn, bạn chọn cúp hay chọn người nhà?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #duaxe #tinhanhem
```

**YouTube Shorts — tiêu đề** (91/100 ký tự)

```text
Sắp về nhất vẫn ngoái lại: “Cúp vô địch để làm gì khi mất đi người nhà?” | Biệt Đội Gara P4
```

**YouTube Shorts — mô tả**

```text
Tú, đứa em út của gara, bị ép đua chiếc xe gài khóa xung điện. Thắng dùng thân xe chặn chiếc bán tải chơi xấu: “Muốn đụng em tao hả? Qua tao đã!” Rồi xe Tú mất thắng lao về phía vực taluy, vạch đích chỉ còn 200 mét, và Thắng ngoái nhìn qua gương chiếu hậu.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 5: Trùm Sói Xám tháo mặt nạ: sư huynh mất tích 15 năm

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Tú, đứa em út của gara, bị ép đua chiếc xe gài khóa xung điện. Thắng dùng thân xe chặn chiếc bán tải chơi xấu: “Muốn đụng em tao hả? Qua tao đã!” Rồi xe Tú mất thắng lao về phía vực taluy, vạch đích chỉ còn 200 mét, và Thắng ngoái nhìn qua gương chiếu hậu.

Là bạn, bạn chọn cúp hay chọn người nhà? 👇
👉 Xem tiếp Phần 5: Trùm Sói Xám tháo mặt nạ: sư huynh mất tích 15 năm
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #duaxe #tinhanhem
```

### Phần 5/12 — Trùm Sói Xám tháo mặt nạ: sư huynh mất tích 15 năm

`05-soi-xam-thao-mat-na.mp4` · 33s · cảnh 20.3, 20.4, 20.6, 21.1 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
Giữa kho xe trộm, mặt nạ của trùm Sói Xám tách đôi, lộ ra gương mặt đầy sẹo của Hùng: “Nhớ tao không Thắng? Mười lăm năm rồi!” Lan nghẹn giọng khuyên anh quay đầu, nhưng Hùng chỉ ra lệnh: “Bắt sống tụi nó cho tao!” Cả đám Găng Xám ùa tới, và cả nhà gara lao vào trận.
Hùng đáng giận hay đáng thương?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #plottwist #phandien
```

**YouTube Shorts — tiêu đề** (79/100 ký tự)

```text
Trùm Sói Xám tháo mặt nạ, hóa ra là sư huynh mất tích 15 năm | Biệt Đội Gara P5
```

**YouTube Shorts — mô tả**

```text
Giữa kho xe trộm, mặt nạ của trùm Sói Xám tách đôi, lộ ra gương mặt đầy sẹo của Hùng: “Nhớ tao không Thắng? Mười lăm năm rồi!” Lan nghẹn giọng khuyên anh quay đầu, nhưng Hùng chỉ ra lệnh: “Bắt sống tụi nó cho tao!” Cả đám Găng Xám ùa tới, và cả nhà gara lao vào trận.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 6: Nghi oan anh Hải phản bội, hóa ra là con chip nghe lén

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Giữa kho xe trộm, mặt nạ của trùm Sói Xám tách đôi, lộ ra gương mặt đầy sẹo của Hùng: “Nhớ tao không Thắng? Mười lăm năm rồi!” Lan nghẹn giọng khuyên anh quay đầu, nhưng Hùng chỉ ra lệnh: “Bắt sống tụi nó cho tao!” Cả đám Găng Xám ùa tới, và cả nhà gara lao vào trận.

Hùng đáng giận hay đáng thương? 👇
👉 Xem tiếp Phần 6: Nghi oan anh Hải phản bội, hóa ra là con chip nghe lén
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #plottwist #phandien
```

### Phần 6/12 — Nghi oan anh Hải phản bội, hóa ra là con chip nghe lén

`06-con-chip-trong-gang-tay.mp4` · 49s · cảnh 24.4, 24.5, 24.6, 25.1, 25.2, 25.3 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Bị nghi báo tin cho Sói Xám, anh Hải quỳ trước bàn kỷ niệm của Bác Bảy mà thề: “Em mà phản bội cái nhà này, sét đánh chết em liền!” Lan khóc bênh anh, Thắng buông tay hỏi tin lộ từ đâu. Đúng lúc đó máy của Khôi báo sóng lạ, và Minh xé lớp lót chiếc găng xám treo trên tường: một con chip nghe lén đang chớp đèn đỏ.
Bạn từng nghi oan người thân chưa?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #nghioan #giadinh
```

**YouTube Shorts — tiêu đề** (91/100 ký tự)

```text
Cả nhà nghi anh Hải phản bội, hóa ra thủ phạm là con chip trong găng tay | Biệt Đội Gara P6
```

**YouTube Shorts — mô tả**

```text
Bị nghi báo tin cho Sói Xám, anh Hải quỳ trước bàn kỷ niệm của Bác Bảy mà thề: “Em mà phản bội cái nhà này, sét đánh chết em liền!” Lan khóc bênh anh, Thắng buông tay hỏi tin lộ từ đâu. Đúng lúc đó máy của Khôi báo sóng lạ, và Minh xé lớp lót chiếc găng xám treo trên tường: một con chip nghe lén đang chớp đèn đỏ.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 7: Bị trùm Sói Xám bắt đi, cậu út kịp gài một con bọ

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Bị nghi báo tin cho Sói Xám, anh Hải quỳ trước bàn kỷ niệm của Bác Bảy mà thề: “Em mà phản bội cái nhà này, sét đánh chết em liền!” Lan khóc bênh anh, Thắng buông tay hỏi tin lộ từ đâu. Đúng lúc đó máy của Khôi báo sóng lạ, và Minh xé lớp lót chiếc găng xám treo trên tường: một con chip nghe lén đang chớp đèn đỏ.

Bạn từng nghi oan người thân chưa? 👇
👉 Xem tiếp Phần 7: Bị trùm Sói Xám bắt đi, cậu út kịp gài một con bọ
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #nghioan #giadinh
```

### Phần 7/12 — Bị trùm Sói Xám bắt đi, cậu út kịp gài một con bọ

`07-khoi-bi-bat-coc.mp4` · 39s · cảnh 26.6, 27.1, 27.2, 27.3, 27.4 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Sói Xám từ mái nhà nhảy xuống, đá văng bàn máy tính, bóp nát drone rồi xách Khôi đi để mở khóa hệ thống tàu. Bị nhấc bổng giữa không trung, Khôi vẫn lén gắn con drone bọ cánh cứng tí hon vào áo khoác của hắn: “Chết mày với tao nghe con sói già...” Rồi cậu bị mang qua lỗ thủng mái nhà, gào gọi anh chị giữa màn mưa.
Con bọ của Khôi sẽ giúp gì cho cả nhà?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #batcoc #hacker
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
Bị trùm Sói Xám bắt cóc, cậu út kịp gài một con bọ lên người hắn | Biệt Đội Gara P7
```

**YouTube Shorts — mô tả**

```text
Sói Xám từ mái nhà nhảy xuống, đá văng bàn máy tính, bóp nát drone rồi xách Khôi đi để mở khóa hệ thống tàu. Bị nhấc bổng giữa không trung, Khôi vẫn lén gắn con drone bọ cánh cứng tí hon vào áo khoác của hắn: “Chết mày với tao nghe con sói già...” Rồi cậu bị mang qua lỗ thủng mái nhà, gào gọi anh chị giữa màn mưa.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 8: Lan bị giật mất lõi giáp giữa cơn mưa

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Sói Xám từ mái nhà nhảy xuống, đá văng bàn máy tính, bóp nát drone rồi xách Khôi đi để mở khóa hệ thống tàu. Bị nhấc bổng giữa không trung, Khôi vẫn lén gắn con drone bọ cánh cứng tí hon vào áo khoác của hắn: “Chết mày với tao nghe con sói già...” Rồi cậu bị mang qua lỗ thủng mái nhà, gào gọi anh chị giữa màn mưa.

Con bọ của Khôi sẽ giúp gì cho cả nhà? 👇
👉 Xem tiếp Phần 8: Lan bị giật mất lõi giáp giữa cơn mưa
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #batcoc #hacker
```

### Phần 8/12 — Lan bị giật mất lõi giáp giữa cơn mưa

`08-lan-mat-loi-giap.mp4` · 49s · cảnh 29.3, 29.4, 29.5, 29.6, 30.1, 30.2 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Trên mái nhà giữa mưa bão, găng tay Sói Xám truyền luồng điện đen ép lõi giáp nhả ra rồi giật phăng khỏi cổ tay Lan. Giáp Cáo tan thành ánh sáng, Lan trượt khỏi mép mái, Thắng lao tới ôm kịp em gái. “Em mất lõi rồi... Giáp của em... mất thật rồi anh ơi...”
Không còn giáp, Lan có quay lại chiến đấu không?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #xucdong #anhhung
```

**YouTube Shorts — tiêu đề** (76/100 ký tự)

```text
Bị trùm giật mất lõi giáp giữa mưa bão, Giáp Cáo tan biến | Biệt Đội Gara P8
```

**YouTube Shorts — mô tả**

```text
Trên mái nhà giữa mưa bão, găng tay Sói Xám truyền luồng điện đen ép lõi giáp nhả ra rồi giật phăng khỏi cổ tay Lan. Giáp Cáo tan thành ánh sáng, Lan trượt khỏi mép mái, Thắng lao tới ôm kịp em gái. “Em mất lõi rồi... Giáp của em... mất thật rồi anh ơi...”

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 9: Xả nitro lõi đỏ, xe đua bay qua đầu xe địch

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Trên mái nhà giữa mưa bão, găng tay Sói Xám truyền luồng điện đen ép lõi giáp nhả ra rồi giật phăng khỏi cổ tay Lan. Giáp Cáo tan thành ánh sáng, Lan trượt khỏi mép mái, Thắng lao tới ôm kịp em gái. “Em mất lõi rồi... Giáp của em... mất thật rồi anh ơi...”

Không còn giáp, Lan có quay lại chiến đấu không? 👇
👉 Xem tiếp Phần 9: Xả nitro lõi đỏ, xe đua bay qua đầu xe địch
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #xucdong #anhhung
```

### Phần 9/12 — Xả nitro lõi đỏ, xe đua bay qua đầu xe địch

`09-xe-bay-qua-dau-dich.mp4` · 36s · cảnh 39.2, 39.3, 39.4, 39.5, 39.6 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
Hai xe bán tải bọc thép chắn kín cầu dẫn vào cảng. Thắng chạm lõi đỏ vào nút nitro: “Gió Đỏ, toàn lực xả ga!” Chiếc Hắc Phong phụt lửa, lao lên gờ dốc bay vút qua đầu bọn cướp đang há hốc mồm, rồi tiếp đất ngọt xớt.
Cú bay này bạn chấm mấy điểm?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #xebay #nitro
```

**YouTube Shorts — tiêu đề** (66/100 ký tự)

```text
Xả nitro lõi đỏ, xe đua bay vút qua đầu xe địch | Biệt Đội Gara P9
```

**YouTube Shorts — mô tả**

```text
Hai xe bán tải bọc thép chắn kín cầu dẫn vào cảng. Thắng chạm lõi đỏ vào nút nitro: “Gió Đỏ, toàn lực xả ga!” Chiếc Hắc Phong phụt lửa, lao lên gờ dốc bay vút qua đầu bọn cướp đang há hốc mồm, rồi tiếp đất ngọt xớt.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 10: Mất giáp vẫn lái xe của ba luồn qua gầm xe cẩu

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Hai xe bán tải bọc thép chắn kín cầu dẫn vào cảng. Thắng chạm lõi đỏ vào nút nitro: “Gió Đỏ, toàn lực xả ga!” Chiếc Hắc Phong phụt lửa, lao lên gờ dốc bay vút qua đầu bọn cướp đang há hốc mồm, rồi tiếp đất ngọt xớt.

Cú bay này bạn chấm mấy điểm? 👇
👉 Xem tiếp Phần 10: Mất giáp vẫn lái xe của ba luồn qua gầm xe cẩu
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #xebay #nitro
```

### Phần 10/12 — Mất giáp vẫn lái xe của ba luồn qua gầm xe cẩu

`10-luon-qua-gam-xe-cau.mp4` · 38s · cảnh 40.2, 40.3, 40.4, 40.5, 40.6 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Không còn giáp, Lan lái chiếc hatchback trắng của ba bám sát đầu kéo của Sói Xám để cứu Khôi. Hắn ép cô về phía dãy container, trước mặt là gầm xe cẩu chỉ cao 1m30, Lan giật phanh tay, nghiêng xe luồn qua: “Qua gầm ngọt xớt!” Cô tạt đầu chặn xe hắn… nhưng hắn vẫn lao thẳng lên tàu.
Tay lái cỡ này, ai còn dám chê tay lái nữ?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #laixe #taylainu
```

**YouTube Shorts — tiêu đề** (79/100 ký tự)

```text
Mất giáp vẫn lái xe của ba luồn qua gầm xe cẩu chỉ cao 1m30 | Biệt Đội Gara P10
```

**YouTube Shorts — mô tả**

```text
Không còn giáp, Lan lái chiếc hatchback trắng của ba bám sát đầu kéo của Sói Xám để cứu Khôi. Hắn ép cô về phía dãy container, trước mặt là gầm xe cẩu chỉ cao 1m30, Lan giật phanh tay, nghiêng xe luồn qua: “Qua gầm ngọt xớt!” Cô tạt đầu chặn xe hắn… nhưng hắn vẫn lao thẳng lên tàu.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 11: Tay trần giật lại lõi giáp: Cáo Băng trở lại

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Không còn giáp, Lan lái chiếc hatchback trắng của ba bám sát đầu kéo của Sói Xám để cứu Khôi. Hắn ép cô về phía dãy container, trước mặt là gầm xe cẩu chỉ cao 1m30, Lan giật phanh tay, nghiêng xe luồn qua: “Qua gầm ngọt xớt!” Cô tạt đầu chặn xe hắn… nhưng hắn vẫn lao thẳng lên tàu.

Tay lái cỡ này, ai còn dám chê tay lái nữ? 👇
👉 Xem tiếp Phần 11: Tay trần giật lại lõi giáp: Cáo Băng trở lại
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #laixe #taylainu
```

### Phần 11/12 — Tay trần giật lại lõi giáp: Cáo Băng trở lại

`11-cao-bang-tro-lai.mp4` · 33s · cảnh 43.2, 43.3, 43.4, 43.5, 43.6 · đăng Thứ Năm 19/11 – 11:00

**TikTok**

```text
Không giáp, chỉ bằng tay trần và đòn khóa Vovinam, Lan giật phăng lõi trắng xanh khỏi găng tay Sói Xám. Lõi nhận lại người chủ, giáp nano bọc kín cô rực rỡ hơn bao giờ hết: “Cáo Băng trở lại rồi đây!” Cả năm chiến binh đứng thành hàng ngang trước mặt hắn.
Khoảnh khắc này có làm bạn nổi da gà không?

👉 Phần 12 ở trang cá nhân, Follow để xem tiếp!
#bietdoigara #phimhanhdong #phimngan #comeback #bienhinh
```

**YouTube Shorts — tiêu đề** (87/100 ký tự)

```text
Tay trần giật lại lõi giáp từ tay trùm phản diện: Cáo Băng trở lại! | Biệt Đội Gara P11
```

**YouTube Shorts — mô tả**

```text
Không giáp, chỉ bằng tay trần và đòn khóa Vovinam, Lan giật phăng lõi trắng xanh khỏi găng tay Sói Xám. Lõi nhận lại người chủ, giáp nano bọc kín cô rực rỡ hơn bao giờ hết: “Cáo Băng trở lại rồi đây!” Cả năm chiến binh đứng thành hàng ngang trước mặt hắn.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
👉 Xem tiếp Phần 12: Lời nhắn của người thầy khiến trùm phản diện quỳ khóc

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Không giáp, chỉ bằng tay trần và đòn khóa Vovinam, Lan giật phăng lõi trắng xanh khỏi găng tay Sói Xám. Lõi nhận lại người chủ, giáp nano bọc kín cô rực rỡ hơn bao giờ hết: “Cáo Băng trở lại rồi đây!” Cả năm chiến binh đứng thành hàng ngang trước mặt hắn.

Khoảnh khắc này có làm bạn nổi da gà không? 👇
👉 Xem tiếp Phần 12: Lời nhắn của người thầy khiến trùm phản diện quỳ khóc
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #comeback #bienhinh
```

### Phần 12/12 — Lời nhắn của người thầy khiến trùm phản diện quỳ khóc

`12-ve-nha-an-com-di-con.mp4` · 38s · cảnh 44.3, 44.4, 44.5, 44.6 · đăng Thứ Năm 19/11 – 19:00

**TikTok**

```text
Giáp sói vỡ vụn, Hùng quỵ gối, nửa bức thư còn lại rơi khỏi túi áo. Hai mảnh thư khớp lại, hình ảnh Bác Bảy hiện lên: “Hùng ơi... Về nhà ăn cơm đi con. Bác chờ con lâu lắm rồi.” Người sư huynh lầm lỡ gục xuống sàn tàu khóc xin lỗi cả nhà dưới ánh bình minh.
Câu nói nào của Bác Bảy làm bạn rưng rưng?

🎬 Xem trọn bộ 10 tập trên kênh YouTube.
#bietdoigara #phimhanhdong #phimngan #xucdong #giadinh
```

**YouTube Shorts — tiêu đề** (82/100 ký tự)

```text
“Về nhà ăn cơm đi con”: lời nhắn khiến trùm phản diện bật khóc | Biệt Đội Gara P12
```

**YouTube Shorts — mô tả**

```text
Giáp sói vỡ vụn, Hùng quỵ gối, nửa bức thư còn lại rơi khỏi túi áo. Hai mảnh thư khớp lại, hình ảnh Bác Bảy hiện lên: “Hùng ơi... Về nhà ăn cơm đi con. Bác chờ con lâu lắm rồi.” Người sư huynh lầm lỡ gục xuống sàn tàu khóc xin lỗi cả nhà dưới ánh bình minh.

🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”
🎬 Xem trọn bộ 10 tập trên kênh YouTube.

#Shorts #bietdoigara #phimhanhdong #phimngan
```

**Facebook Reels**

```text
Giáp sói vỡ vụn, Hùng quỵ gối, nửa bức thư còn lại rơi khỏi túi áo. Hai mảnh thư khớp lại, hình ảnh Bác Bảy hiện lên: “Hùng ơi... Về nhà ăn cơm đi con. Bác chờ con lâu lắm rồi.” Người sư huynh lầm lỡ gục xuống sàn tàu khóc xin lỗi cả nhà dưới ánh bình minh.

Câu nói nào của Bác Bảy làm bạn rưng rưng? 👇
🎬 Xem trọn bộ 10 tập trên kênh YouTube.
🎬 Trọn bộ 10 tập có trên kênh YouTube, tìm “Biệt Đội Gara”

#BietDoiGara #PhimHanhDong #PhimNgan #SieuAnhHung #xucdong #giadinh
```
