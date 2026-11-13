# Bí Mật Phòng 613: Lời Cảnh Báo Đêm Rằm — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **các cảnh hay nhất** của phim 15 phút, gồm **11 phần dọc 9:16**, không phải cả phim. Mỗi phần là một khoảnh khắc trọn vẹn dài khoảng 35–50 giây (mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger), xếp theo thứ tự truyện và đăng nối tiếp như một series.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn đỏ đèn thờ “BÍ MẬT PHÒNG 613 • PHẦN N” và câu hook ở trên khung phim (cụm nhấn màu xanh ngọc); phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau, phần cuối đổi thành “XEM FULL PHIM”. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy nguyên từ tiếng thật trong clip (Whisper). Phim không có file phân cảnh JSON nên phụ đề không đối chiếu kịch bản; tên riêng hay chữ nghe sai thì sửa bằng `subtitle_replace` trong plan.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm); clip nào Omni nói lặp lại mấy chữ cuối thì cắt trước đoạn lặp.
- **File:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; caption TikTok, tiêu đề + mô tả YouTube và caption Facebook của mọi phần nằm ở cuối `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py bi-mat-phong-613              # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py bi-mat-phong-613 --only 7     # một phần
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py bi-mat-phong-613 --captions   # chỉ ghi lại README (lịch + caption)
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-nen-nhang-giua-tu-tat.mp4`](01-nen-nhang-giua-tu-tat.mp4) | Cúng nhập trạch phòng 613, nén nhang giữa tự tắt | 01.2, 01.3, 01.4, 01.5, 01.6 | 50s | Thứ Bảy 14/11 – 11:00 |  |
| 2 | [`02-tieng-go-cua-phong-tam.mp4`](02-tieng-go-cua-phong-tam.mp4) | Ai gõ ba tiếng lên cửa phòng tắm lúc nửa đêm? | 03.1, 03.2, 03.3, 03.4, 03.5 | 49s | Thứ Bảy 14/11 – 19:00 |  |
| 3 | [`03-bong-vay-trang-trong-guong.mp4`](03-bong-vay-trang-trong-guong.mp4) | Nửa đêm soi gương, thấy bóng váy trắng sau lưng | 04.1, 04.2, 04.3, 04.4 | 39s | Chủ Nhật 15/11 – 11:00 | ⭐ |
| 4 | [`04-dot-la-bua-tren-tu.mp4`](04-dot-la-bua-tren-tu.mp4) | Cô bạn cứng vía đốt lá bùa niêm phong tủ gỗ | 05.2, 05.3, 05.4, 05.5, 05.6 | 47s | Chủ Nhật 15/11 – 19:00 |  |
| 5 | [`05-loi-canh-bao-duoi-anh-nen.mp4`](05-loi-canh-bao-duoi-anh-nen.mp4) | Cô gái áo trắng hiện ra, dặn đừng nghe ông bảo vệ | 07.1, 07.2, 07.3, 07.4 | 40s | Thứ Hai 16/11 – 11:00 |  |
| 6 | [`06-ong-bay-bao-ve.mp4`](06-ong-bay-bao-ve.mp4) | Chưa kể gì, ông bảo vệ đã biết cô ấy gặp ai | 07.6, 08.1, 08.2, 08.3 | 40s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-dien-thoai-dut-day-do-chuong.mp4`](07-dien-thoai-dut-day-do-chuong.mp4) | Điện thoại đứt dây tự đổ chuông giữa đêm | 09.2, 09.3, 09.4, 09.5 | 40s | Thứ Ba 17/11 – 11:00 | ⭐ |
| 8 | [`08-dot-hop-sat-truoc-3-gio.mp4`](08-dot-hop-sat-truoc-3-gio.mp4) | Ông bảo vệ ép đốt hộp sắt trước 3 giờ sáng | 10.2, 10.3, 10.4, 10.5, 10.6 | 49s | Thứ Ba 17/11 – 19:00 |  |
| 9 | [`09-mo-hop-sat.mp4`](09-mo-hop-sat.mp4) | Mở hộp sắt bị cấm, thấy cô gái trong gương | 11.2, 11.3, 11.4, 11.5, 11.6 | 50s | Thứ Tư 18/11 – 11:00 |  |
| 10 | [`10-khoa-trai-cua-luc-3-gio.mp4`](10-khoa-trai-cua-luc-3-gio.mp4) | 3 giờ sáng, ông bảo vệ khóa trái cửa phòng 613 | 12.2, 12.3, 12.4, 12.5, 12.6 | 50s | Thứ Tư 18/11 – 19:00 |  |
| 11 | [`11-hai-tam-di-anh.mp4`](11-hai-tam-di-anh.mp4) | Bốt bảo vệ bỏ hoang 8 năm, bên trong có hai di ảnh | 14.5, 14.6, 15.1, 15.2, 15.3 | 50s | Thứ Năm 19/11 – 11:00 | ⭐ |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Bí Mật Phòng 613”. Chọn ảnh bìa bằng khung hình có hook (giây đầu). Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả ở phần caption bên dưới; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption; tắt “Tạo phụ đề tự động” vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00), 3 nền tảng cùng giờ, bắt đầu 14/11/2026. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Kiểm tra trước khi đăng

- `subtitle_replace` đang để trống: xem phụ đề Whisper rồi thêm cặp sửa chữ khi cần (bản Whisper hiện có: “Chính”/“Trình” thay cho Trinh, “dèm” thay cho rèm, “nhan” thay cho nhang, “cầu giao” thay cho cầu dao, “lô xe” thay cho lô C), dựng lại phần đó bằng `--only`.
- Caption và câu trích đã so với bản Whisper ngày 13/11: Omni nói rút gọn nhiều câu ở cảnh 10–14 so với prompt, nên caption chỉ kể những gì nghe thấy trong clip.
- `canh-01/clip-2.md` bị hỏng (chỉ còn 2 ký tự); bản render 01.2 vẫn nói đúng thoại của shot 01.2 trong `KICH_BAN_15_PHUT.md` (đã so với Whisper) nên phần 1 có dùng.

## Lỗi hình thấy trong clip đã chọn (chưa xử lý)

Plan chưa có `from`/`to` hay `fixes`; xem lại rồi render lại clip, hoặc cắt bằng `from` / `fixes` trước khi đăng.

- **09.3** (phần 7, ⭐): viền khung phim đen bo góc suốt cả clip. Script không tự cắt được (dò viền ra 1250×720, cao đủ 720), cần thêm `fixes` crop cho clip này hoặc render lại.
- **03.1** (phần 2): chữ “tok... tok...” hiện trên cửa kính phòng tắm khoảng giây thứ 5. Dòng “ĐỪNG ĐỐT” trên kính ở 03.2 là có trong kịch bản.
- **03.3** (phần 2): viền đen trên dưới khoảng 0–1,2 s.

## Caption từng phần (copy dán)

### Phần 1/11 — Cúng nhập trạch phòng 613, nén nhang giữa tự tắt

`01-nen-nhang-giua-tu-tat.mp4` · 50s · cảnh 01.2, 01.3, 01.4, 01.5, 01.6 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
Phương đang cúng nhập trạch trước cửa phòng 613 thì Trinh xách xô nước đi qua làm tắt ngúm cả chậu vàng mã, rồi còn cười chuyện cúng bái. Phương thấy gương Bát Quái trên đầu cửa bị lật úp vào tường, vừa bước qua bậc cửa đã lạnh buốt sống lưng như có ai nhìn từ góc phòng. Ba nén nhang ngoài hành lang, cây chính giữa tự tắt lịm: “điềm người khuất mặt không đồng ý cho ở...”
Gặp điềm này, bạn có dám ở lại không?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #tamlinh #chungcucu
```

**YouTube Shorts — tiêu đề** (80/100 ký tự)

```text
Cúng nhập trạch phòng 613, nén nhang chính giữa tự tắt lịm | Bí Mật Phòng 613 P1
```

**YouTube Shorts — mô tả**

```text
Phương đang cúng nhập trạch trước cửa phòng 613 thì Trinh xách xô nước đi qua làm tắt ngúm cả chậu vàng mã, rồi còn cười chuyện cúng bái. Phương thấy gương Bát Quái trên đầu cửa bị lật úp vào tường, vừa bước qua bậc cửa đã lạnh buốt sống lưng như có ai nhìn từ góc phòng. Ba nén nhang ngoài hành lang, cây chính giữa tự tắt lịm: “điềm người khuất mặt không đồng ý cho ở...”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 2: Ai gõ ba tiếng lên cửa phòng tắm lúc nửa đêm?

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Phương đang cúng nhập trạch trước cửa phòng 613 thì Trinh xách xô nước đi qua làm tắt ngúm cả chậu vàng mã, rồi còn cười chuyện cúng bái. Phương thấy gương Bát Quái trên đầu cửa bị lật úp vào tường, vừa bước qua bậc cửa đã lạnh buốt sống lưng như có ai nhìn từ góc phòng. Ba nén nhang ngoài hành lang, cây chính giữa tự tắt lịm: “điềm người khuất mặt không đồng ý cho ở...”

Gặp điềm này, bạn có dám ở lại không? 👇
👉 Xem tiếp Phần 2: Ai gõ ba tiếng lên cửa phòng tắm lúc nửa đêm?
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #tamlinh #chungcucu
```

### Phần 2/11 — Ai gõ ba tiếng lên cửa phòng tắm lúc nửa đêm?

`02-tieng-go-cua-phong-tam.mp4` · 49s · cảnh 03.1, 03.2, 03.3, 03.4, 03.5 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Trinh đang gội đầu thì có tiếng gõ lên cửa kính mờ, vòi sen tắt ngang, một bóng tóc dài lướt qua. Phương thề nãy giờ chỉ đứng góc phòng dò sóng điện thoại: vậy thì “ai vừa gõ ba tiếng lên kính mờ rồi lướt qua cửa nhà tắm lúc nước tắt?!” Dưới sàn còn in một hàng dấu bàn chân trần ướt sũng, trong khi Trinh vẫn đi dép nhựa khô nguyên.
Theo bạn, dấu chân ướt đó là của ai?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #phimkinhdi #phongtro
```

**YouTube Shorts — tiêu đề** (67/100 ký tự)

```text
Ai gõ ba tiếng lên cửa phòng tắm lúc nửa đêm? | Bí Mật Phòng 613 P2
```

**YouTube Shorts — mô tả**

```text
Trinh đang gội đầu thì có tiếng gõ lên cửa kính mờ, vòi sen tắt ngang, một bóng tóc dài lướt qua. Phương thề nãy giờ chỉ đứng góc phòng dò sóng điện thoại: vậy thì “ai vừa gõ ba tiếng lên kính mờ rồi lướt qua cửa nhà tắm lúc nước tắt?!” Dưới sàn còn in một hàng dấu bàn chân trần ướt sũng, trong khi Trinh vẫn đi dép nhựa khô nguyên.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 3: Nửa đêm soi gương, thấy bóng váy trắng sau lưng

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Trinh đang gội đầu thì có tiếng gõ lên cửa kính mờ, vòi sen tắt ngang, một bóng tóc dài lướt qua. Phương thề nãy giờ chỉ đứng góc phòng dò sóng điện thoại: vậy thì “ai vừa gõ ba tiếng lên kính mờ rồi lướt qua cửa nhà tắm lúc nước tắt?!” Dưới sàn còn in một hàng dấu bàn chân trần ướt sũng, trong khi Trinh vẫn đi dép nhựa khô nguyên.

Theo bạn, dấu chân ướt đó là của ai? 👇
👉 Xem tiếp Phần 3: Nửa đêm soi gương, thấy bóng váy trắng sau lưng
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #phimkinhdi #phongtro
```

### Phần 3/11 — Nửa đêm soi gương, thấy bóng váy trắng sau lưng

`03-bong-vay-trang-trong-guong.mp4` · 39s · cảnh 04.1, 04.2, 04.3, 04.4 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Gần mười hai giờ đêm rằm, Phương ngồi chải tóc trước chiếc gương tròn và thấy một bóng váy trắng đứng sau tấm rèm xanh. Quay lại thì Trinh vẫn ngủ say, còn cửa phòng tự mở hé. Ngoài khe cửa, cô gái áo trắng thì thầm: “Đừng để ông ta lấy mất cuốn sổ trong chiếc tủ gỗ...”
Bạn có dám soi gương lúc nửa đêm không?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #chuyenma #demram
```

**YouTube Shorts — tiêu đề** (74/100 ký tự)

```text
Nửa đêm soi gương, thấy bóng váy trắng đứng sau lưng | Bí Mật Phòng 613 P3
```

**YouTube Shorts — mô tả**

```text
Gần mười hai giờ đêm rằm, Phương ngồi chải tóc trước chiếc gương tròn và thấy một bóng váy trắng đứng sau tấm rèm xanh. Quay lại thì Trinh vẫn ngủ say, còn cửa phòng tự mở hé. Ngoài khe cửa, cô gái áo trắng thì thầm: “Đừng để ông ta lấy mất cuốn sổ trong chiếc tủ gỗ...”

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 4: Cô bạn cứng vía đốt lá bùa niêm phong tủ gỗ

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Gần mười hai giờ đêm rằm, Phương ngồi chải tóc trước chiếc gương tròn và thấy một bóng váy trắng đứng sau tấm rèm xanh. Quay lại thì Trinh vẫn ngủ say, còn cửa phòng tự mở hé. Ngoài khe cửa, cô gái áo trắng thì thầm: “Đừng để ông ta lấy mất cuốn sổ trong chiếc tủ gỗ...”

Bạn có dám soi gương lúc nửa đêm không? 👇
👉 Xem tiếp Phần 4: Cô bạn cứng vía đốt lá bùa niêm phong tủ gỗ
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #chuyenma #demram
```

### Phần 4/11 — Cô bạn cứng vía đốt lá bùa niêm phong tủ gỗ

`04-dot-la-bua-tren-tu.mp4` · 47s · cảnh 05.2, 05.3, 05.4, 05.5, 05.6 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Để Phương hết sợ, Trinh giật lá bùa vàng trên tủ gỗ châm lửa đốt, mặc Phương can: “Đêm rằm mà tự ý xé rồi đốt bùa trấn yểm là đại kỵ đấy!” Lửa bén lên màu xanh lạnh, rồi Trinh còn bê rổ quần áo ra sân phơi lúc quá nửa đêm. Cô vừa khuất bóng, chốt chiếc tủ gỗ đã tự nảy ra.
Trinh liều hay Phương nhát, bạn đứng về phía ai?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #kiengky #tamlinh
```

**YouTube Shorts — tiêu đề** (81/100 ký tự)

```text
Đêm rằm, cô bạn cùng phòng đốt lá bùa niêm phong trên tủ gỗ | Bí Mật Phòng 613 P4
```

**YouTube Shorts — mô tả**

```text
Để Phương hết sợ, Trinh giật lá bùa vàng trên tủ gỗ châm lửa đốt, mặc Phương can: “Đêm rằm mà tự ý xé rồi đốt bùa trấn yểm là đại kỵ đấy!” Lửa bén lên màu xanh lạnh, rồi Trinh còn bê rổ quần áo ra sân phơi lúc quá nửa đêm. Cô vừa khuất bóng, chốt chiếc tủ gỗ đã tự nảy ra.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 5: Cô gái áo trắng hiện ra, dặn đừng nghe ông bảo vệ

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Để Phương hết sợ, Trinh giật lá bùa vàng trên tủ gỗ châm lửa đốt, mặc Phương can: “Đêm rằm mà tự ý xé rồi đốt bùa trấn yểm là đại kỵ đấy!” Lửa bén lên màu xanh lạnh, rồi Trinh còn bê rổ quần áo ra sân phơi lúc quá nửa đêm. Cô vừa khuất bóng, chốt chiếc tủ gỗ đã tự nảy ra.

Trinh liều hay Phương nhát, bạn đứng về phía ai? 👇
👉 Xem tiếp Phần 5: Cô gái áo trắng hiện ra, dặn đừng nghe ông bảo vệ
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #kiengky #tamlinh
```

### Phần 5/11 — Cô gái áo trắng hiện ra, dặn đừng nghe ông bảo vệ

`05-loi-canh-bao-duoi-anh-nen.mp4` · 40s · cảnh 07.1, 07.2, 07.3, 07.4 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
Mất điện giữa sân phơi, Trinh cầm ly nến đỏ đi giữa giàn đồ, run rẩy xin lỗi vì trót đốt tờ giấy vàng. Cô gái áo trắng hiện ra, không hù dọa mà cảnh báo: “hai em tuyệt đối đừng nghe lời ông bảo vệ mà đốt chiếc hộp sắt trong tủ...” Cô bạn không tin ma quỷ bật khóc gọi Phương.
Nên tin cô gái áo trắng hay ông bảo vệ?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #chuyenma #bian
```

**YouTube Shorts — tiêu đề** (89/100 ký tự)

```text
Cô gái áo trắng hiện ra giữa sân phơi, dặn đừng nghe lời ông bảo vệ | Bí Mật Phòng 613 P5
```

**YouTube Shorts — mô tả**

```text
Mất điện giữa sân phơi, Trinh cầm ly nến đỏ đi giữa giàn đồ, run rẩy xin lỗi vì trót đốt tờ giấy vàng. Cô gái áo trắng hiện ra, không hù dọa mà cảnh báo: “hai em tuyệt đối đừng nghe lời ông bảo vệ mà đốt chiếc hộp sắt trong tủ...” Cô bạn không tin ma quỷ bật khóc gọi Phương.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 6: Chưa kể gì, ông bảo vệ đã biết cô ấy gặp ai

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Mất điện giữa sân phơi, Trinh cầm ly nến đỏ đi giữa giàn đồ, run rẩy xin lỗi vì trót đốt tờ giấy vàng. Cô gái áo trắng hiện ra, không hù dọa mà cảnh báo: “hai em tuyệt đối đừng nghe lời ông bảo vệ mà đốt chiếc hộp sắt trong tủ...” Cô bạn không tin ma quỷ bật khóc gọi Phương.

Nên tin cô gái áo trắng hay ông bảo vệ? 👇
👉 Xem tiếp Phần 6: Chưa kể gì, ông bảo vệ đã biết cô ấy gặp ai
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #chuyenma #bian
```

### Phần 6/11 — Chưa kể gì, ông bảo vệ đã biết cô ấy gặp ai

`06-ong-bay-bao-ve.mp4` · 40s · cảnh 07.6, 08.1, 08.2, 08.3 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Chạy khỏi sân phơi, Trinh đâm sầm vào ông Bảy, bảo vệ gác đêm lô C. Cô chưa kịp kể, ông đã hỏi: “chắc vừa thấy con bé mặc váy trắng đứng sau tấm ga giường ở sân phơi rồi phải không?” Vừa nghe nhắc tới chiếc hộp sắt trong tủ gỗ, mặt ông biến sắc.
Sao ông Bảy lại biết rõ thế nhỉ?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #baove #bian
```

**YouTube Shorts — tiêu đề** (69/100 ký tự)

```text
Chưa kể gì, ông bảo vệ đã biết cô ấy vừa gặp ai | Bí Mật Phòng 613 P6
```

**YouTube Shorts — mô tả**

```text
Chạy khỏi sân phơi, Trinh đâm sầm vào ông Bảy, bảo vệ gác đêm lô C. Cô chưa kịp kể, ông đã hỏi: “chắc vừa thấy con bé mặc váy trắng đứng sau tấm ga giường ở sân phơi rồi phải không?” Vừa nghe nhắc tới chiếc hộp sắt trong tủ gỗ, mặt ông biến sắc.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 7: Điện thoại đứt dây tự đổ chuông giữa đêm

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Chạy khỏi sân phơi, Trinh đâm sầm vào ông Bảy, bảo vệ gác đêm lô C. Cô chưa kịp kể, ông đã hỏi: “chắc vừa thấy con bé mặc váy trắng đứng sau tấm ga giường ở sân phơi rồi phải không?” Vừa nghe nhắc tới chiếc hộp sắt trong tủ gỗ, mặt ông biến sắc.

Sao ông Bảy lại biết rõ thế nhỉ? 👇
👉 Xem tiếp Phần 7: Điện thoại đứt dây tự đổ chuông giữa đêm
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #baove #bian
```

### Phần 7/11 — Điện thoại đứt dây tự đổ chuông giữa đêm

`07-dien-thoai-dut-day-do-chuong.mp4` · 40s · cảnh 09.2, 09.3, 09.4, 09.5 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Chiếc điện thoại nội bộ trên tường đã đứt dây từ lâu bỗng đổ chuông. Phương nhấc máy, nghe tiếng lửa cháy và tiếng một cô gái gào khóc “kêu chú Bảy mở khóa cửa sắt!”. Rồi hai cánh tủ gỗ tự bật mở, để lộ chiếc hộp sắt ám khói đen, đúng lúc ông Bảy cầm nhang quay lên tới cửa.
Nếu là bạn, bạn có dám nhấc máy không?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #phimkinhdi #chuyenma
```

**YouTube Shorts — tiêu đề** (88/100 ký tự)

```text
Điện thoại đứt dây tự đổ chuông, đầu dây là tiếng đám cháy năm xưa | Bí Mật Phòng 613 P7
```

**YouTube Shorts — mô tả**

```text
Chiếc điện thoại nội bộ trên tường đã đứt dây từ lâu bỗng đổ chuông. Phương nhấc máy, nghe tiếng lửa cháy và tiếng một cô gái gào khóc “kêu chú Bảy mở khóa cửa sắt!”. Rồi hai cánh tủ gỗ tự bật mở, để lộ chiếc hộp sắt ám khói đen, đúng lúc ông Bảy cầm nhang quay lên tới cửa.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 8: Ông bảo vệ ép đốt hộp sắt trước 3 giờ sáng

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Chiếc điện thoại nội bộ trên tường đã đứt dây từ lâu bỗng đổ chuông. Phương nhấc máy, nghe tiếng lửa cháy và tiếng một cô gái gào khóc “kêu chú Bảy mở khóa cửa sắt!”. Rồi hai cánh tủ gỗ tự bật mở, để lộ chiếc hộp sắt ám khói đen, đúng lúc ông Bảy cầm nhang quay lên tới cửa.

Nếu là bạn, bạn có dám nhấc máy không? 👇
👉 Xem tiếp Phần 8: Ông bảo vệ ép đốt hộp sắt trước 3 giờ sáng
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #phimkinhdi #chuyenma
```

### Phần 8/11 — Ông bảo vệ ép đốt hộp sắt trước 3 giờ sáng

`08-dot-hop-sat-truoc-3-gio.mp4` · 49s · cảnh 10.2, 10.3, 10.4, 10.5, 10.6 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Ông Bảy chỉ vào chiếc hộp sắt, bảo trong đó là “sổ sách tà đạo của con bé gặp nạn tám năm trước” và cấm mở ra đọc. Ông dúi lá bùa tro, ép hai cô trút hết giấy tờ ra chậu nhôm đốt thành tro trước ba giờ sáng, lúc ấy chỉ còn bốn mươi lăm phút. Trinh vặn lại: nguy hiểm thế, sao tám năm qua bác không tự đốt đi?
Bạn sẽ đốt hay mở hộp ra đọc?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #bian #tamlinh
```

**YouTube Shorts — tiêu đề** (84/100 ký tự)

```text
Ông bảo vệ ép đốt hộp sắt trước 3 giờ sáng, cấm không được đọc | Bí Mật Phòng 613 P8
```

**YouTube Shorts — mô tả**

```text
Ông Bảy chỉ vào chiếc hộp sắt, bảo trong đó là “sổ sách tà đạo của con bé gặp nạn tám năm trước” và cấm mở ra đọc. Ông dúi lá bùa tro, ép hai cô trút hết giấy tờ ra chậu nhôm đốt thành tro trước ba giờ sáng, lúc ấy chỉ còn bốn mươi lăm phút. Trinh vặn lại: nguy hiểm thế, sao tám năm qua bác không tự đốt đi?

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 9: Mở hộp sắt bị cấm, thấy cô gái trong gương

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Ông Bảy chỉ vào chiếc hộp sắt, bảo trong đó là “sổ sách tà đạo của con bé gặp nạn tám năm trước” và cấm mở ra đọc. Ông dúi lá bùa tro, ép hai cô trút hết giấy tờ ra chậu nhôm đốt thành tro trước ba giờ sáng, lúc ấy chỉ còn bốn mươi lăm phút. Trinh vặn lại: nguy hiểm thế, sao tám năm qua bác không tự đốt đi?

Bạn sẽ đốt hay mở hộp ra đọc? 👇
👉 Xem tiếp Phần 9: Mở hộp sắt bị cấm, thấy cô gái trong gương
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #bian #tamlinh
```

### Phần 9/11 — Mở hộp sắt bị cấm, thấy cô gái trong gương

`09-mo-hop-sat.mp4` · 50s · cảnh 11.2, 11.3, 11.4, 11.5, 11.6 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
Bất chấp lời cấm, Trinh bật chốt hộp sắt: bên trong chỉ có thẻ sinh viên, bài báo cũ và một cuốn nhật ký bìa da. “Tấm ảnh trên thẻ sinh viên này chính là chị mặc đầm trắng tớ thấy trong gương.” Nhật ký của chị Linh ghi đêm mồng 3 tháng 11, chị phát hiện ông Bảy cắt trộm cáp đồng báo cháy, định sáng hôm sau nộp cuốn sổ, thì ngay đêm đó hành lang chập điện bốc cháy.
Bạn đã nghi ông Bảy từ lúc nào?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #plottwist #bian
```

**YouTube Shorts — tiêu đề** (86/100 ký tự)

```text
Mở hộp sắt bị cấm, thẻ sinh viên bên trong là cô gái trong gương | Bí Mật Phòng 613 P9
```

**YouTube Shorts — mô tả**

```text
Bất chấp lời cấm, Trinh bật chốt hộp sắt: bên trong chỉ có thẻ sinh viên, bài báo cũ và một cuốn nhật ký bìa da. “Tấm ảnh trên thẻ sinh viên này chính là chị mặc đầm trắng tớ thấy trong gương.” Nhật ký của chị Linh ghi đêm mồng 3 tháng 11, chị phát hiện ông Bảy cắt trộm cáp đồng báo cháy, định sáng hôm sau nộp cuốn sổ, thì ngay đêm đó hành lang chập điện bốc cháy.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 10: 3 giờ sáng, ông bảo vệ khóa trái cửa phòng 613

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Bất chấp lời cấm, Trinh bật chốt hộp sắt: bên trong chỉ có thẻ sinh viên, bài báo cũ và một cuốn nhật ký bìa da. “Tấm ảnh trên thẻ sinh viên này chính là chị mặc đầm trắng tớ thấy trong gương.” Nhật ký của chị Linh ghi đêm mồng 3 tháng 11, chị phát hiện ông Bảy cắt trộm cáp đồng báo cháy, định sáng hôm sau nộp cuốn sổ, thì ngay đêm đó hành lang chập điện bốc cháy.

Bạn đã nghi ông Bảy từ lúc nào? 👇
👉 Xem tiếp Phần 10: 3 giờ sáng, ông bảo vệ khóa trái cửa phòng 613
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #plottwist #bian
```

### Phần 10/11 — 3 giờ sáng, ông bảo vệ khóa trái cửa phòng 613

`10-khoa-trai-cua-luc-3-gio.mp4` · 50s · cảnh 12.2, 12.3, 12.4, 12.5, 12.6 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Phương vạch mặt ông Bảy: “Chính ông đã khóa trái cửa sắt bên ngoài lúc chập điện, làm chị Linh không thoát ra được!” Ông không chối, khóa luôn cửa nhốt hai cô từ bên ngoài như tám năm trước, rồi đặt tay lên hộp cầu dao điện. Tiếng chuông bạc ngân lên ở cuối hành lang, và chị Linh xuất hiện.
Chị Linh sẽ làm gì ông Bảy?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#bimatphong613 #phimma #phimngan #caotrao #phimkinhdi
```

**YouTube Shorts — tiêu đề** (80/100 ký tự)

```text
Đúng 3 giờ sáng, ông bảo vệ khóa trái cửa nhốt hai cô gái | Bí Mật Phòng 613 P10
```

**YouTube Shorts — mô tả**

```text
Phương vạch mặt ông Bảy: “Chính ông đã khóa trái cửa sắt bên ngoài lúc chập điện, làm chị Linh không thoát ra được!” Ông không chối, khóa luôn cửa nhốt hai cô từ bên ngoài như tám năm trước, rồi đặt tay lên hộp cầu dao điện. Tiếng chuông bạc ngân lên ở cuối hành lang, và chị Linh xuất hiện.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
👉 Xem tiếp Phần 11: Bốt bảo vệ bỏ hoang 8 năm, bên trong có hai di ảnh

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Phương vạch mặt ông Bảy: “Chính ông đã khóa trái cửa sắt bên ngoài lúc chập điện, làm chị Linh không thoát ra được!” Ông không chối, khóa luôn cửa nhốt hai cô từ bên ngoài như tám năm trước, rồi đặt tay lên hộp cầu dao điện. Tiếng chuông bạc ngân lên ở cuối hành lang, và chị Linh xuất hiện.

Chị Linh sẽ làm gì ông Bảy? 👇
👉 Xem tiếp Phần 11: Bốt bảo vệ bỏ hoang 8 năm, bên trong có hai di ảnh
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #caotrao #phimkinhdi
```

### Phần 11/11 — Bốt bảo vệ bỏ hoang 8 năm, bên trong có hai di ảnh

`11-hai-tam-di-anh.mp4` · 50s · cảnh 14.5, 14.6, 15.1, 15.2, 15.3 · đăng Thứ Năm 19/11 – 11:00

**TikTok**

```text
Sáng ra, hai cô phát hiện bốt bảo vệ dưới sân đã đóng cửa bỏ hoang: “Nếu bốt bảo vệ này đã bỏ hoang suốt tám năm qua, nói chuyện với tụi mình suốt đêm qua là ai?” Qua chiếc gương tròn, hai cô thấy bàn thờ với hai khung ảnh, chị Linh và ông Bảy. Đêm cháy năm ấy, khóa cửa nhốt chị Linh xong thì hộp cầu dao phát nổ, ông Bảy chết cùng đêm.
Bạn nhận ra ông Bảy là người đã khuất từ lúc nào?

🎬 Xem trọn bộ 15 phút trên kênh YouTube.
#bimatphong613 #phimma #phimngan #plottwist #ketphim
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
Bốt bảo vệ bỏ hoang 8 năm, bên trong có hai tấm di ảnh | Bí Mật Phòng 613 P11
```

**YouTube Shorts — mô tả**

```text
Sáng ra, hai cô phát hiện bốt bảo vệ dưới sân đã đóng cửa bỏ hoang: “Nếu bốt bảo vệ này đã bỏ hoang suốt tám năm qua, nói chuyện với tụi mình suốt đêm qua là ai?” Qua chiếc gương tròn, hai cô thấy bàn thờ với hai khung ảnh, chị Linh và ông Bảy. Đêm cháy năm ấy, khóa cửa nhốt chị Linh xong thì hộp cầu dao phát nổ, ông Bảy chết cùng đêm.

🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”
🎬 Xem trọn bộ 15 phút trên kênh YouTube.

#Shorts #bimatphong613 #phimmavietnam #phimngan
```

**Facebook Reels**

```text
Sáng ra, hai cô phát hiện bốt bảo vệ dưới sân đã đóng cửa bỏ hoang: “Nếu bốt bảo vệ này đã bỏ hoang suốt tám năm qua, nói chuyện với tụi mình suốt đêm qua là ai?” Qua chiếc gương tròn, hai cô thấy bàn thờ với hai khung ảnh, chị Linh và ông Bảy. Đêm cháy năm ấy, khóa cửa nhốt chị Linh xong thì hộp cầu dao phát nổ, ông Bảy chết cùng đêm.

Bạn nhận ra ông Bảy là người đã khuất từ lúc nào? 👇
🎬 Xem trọn bộ 15 phút trên kênh YouTube.
🎬 Full phim 15 phút có trên kênh YouTube, tìm “Bí Mật Phòng 613”

#BiMatPhong613 #PhimMaVietNam #PhimNgan #ChuyenMaChungCu #plottwist #ketphim
```
