# CUỐN SÁCH TRAO TAY
*Phim truyện chính kịch hư cấu, ~25 phút, 96 clip × 15 giây, dựng bằng Google Flow (Gemini Omni 1.2 Flash)*

---

## 0. Ghi chú trước khi làm

**Tính hư cấu.** Nhân vật, công ty và sự kiện trong phim đều là hư cấu. Kịch bản không dùng tên công ty, nhãn hàng, năm tháng, con số hay câu nói có thật. Thời gian chỉ được gợi qua bối cảnh (đồ vật, trang phục, công nghệ từng thời). Khi chỉnh sửa, giữ nguyên nguyên tắc này: không thêm mốc năm, số tiền cụ thể hay tên riêng có thật.

- Thẻ mở đầu phim: *"Phim hư cấu. Mọi nhân vật, tổ chức và sự kiện đều do tác giả sáng tạo."*
- Khi đăng phim, không nên giới thiệu đây là phim về một người có thật.

**Model.** Dùng **Gemini Omni 1.2 Flash** trong Google Flow: tạo clip 15 giây liền mạch, nhận tối đa 6 ảnh tham chiếu mỗi lần tạo, chỉnh sửa tiếp bằng hội thoại. Nên nháp ở 360p, chốt bản đẹp ở 720p. Giá credit xem trong Settings của Flow vì Google thay đổi thường xuyên.

**Hình ảnh trên Flow.** Mọi nhân vật do "diễn viên AI" hư cấu đóng. Trong prompt chỉ dùng @Tag. Không để Omni vẽ chữ hay logo (Omni hay vẽ sai chữ). Phụ đề và tên phim chèn ở khâu dựng.

**Âm thanh.** Omni tạo tiếng tiếng Việt chưa ổn định. Khuyến nghị: clip chỉ có tiếng môi trường và vài câu thoại ngắn; **lời dẫn (V.O.) thu riêng** (giọng thật hoặc TTS) rồi ghép khi dựng.

---

## 1. Logline

Một chàng trai vùng quê vừa học xong cấp ba đi nhặt ve chai để mua sách lập trình, được mẹ bán đôi bông tai hồi môn mua cho chiếc máy tính trước ngày lên thành phố học đại học. Lớn lên, anh lập công ty từ số vốn ít ỏi và dựng nên một tập đoàn công nghệ. Đến khi một tập đoàn nước ngoài ngỏ ý mua lại tất cả, anh trở về quê — và tìm thấy điều không thể bán. Một câu chuyện về khát vọng, cội nguồn và sự trao truyền.

**Giọng phim:** điềm tĩnh, không tô vẽ. Ánh sáng ấm ở nửa đầu (thời trẻ, khởi nghiệp), chuyển dần sang lạnh, kính và thép (đỉnh cao), rồi trở lại ấm áp, mộc mạc khi anh về quê.

---

## 2. Nhân vật (@Tag dùng trong prompt Flow)

| @Tag | Tên trong phim | Giai đoạn | Khuôn mặt, dáng người (giữ nguyên mọi look) |
|---|---|---|---|
| @KhangYoung | Khang (thanh niên) | 18–29 tuổi | Thanh niên mảnh khảnh, da rám nắng, gò má cao, kính không viền, tóc rẽ ngôi gọn. Trang phục: K1–K2, T1–T3, Y1–Y8 |
| @KhangMid | Nguyễn Minh Khang | 32–45 tuổi | Đàn ông mặt đầy đặn hơn, kính chữ nhật gọng đen, tóc ngắn điểm bạc ở thái dương. Trang phục: M0–M6 |
| @MeHanh | Bà Hạnh – mẹ Khang | Ngoài 40 → ngoài 70 tuổi | Phụ nữ Việt dáng gầy, gương mặt hiền, nếp nhăn khóe mắt, tóc dài ngang vai. Trang phục: H1–H4 |
| @Mai | Mai – cô gái trong làng | 18 tuổi | Cô gái Việt gầy, da rám nắng, mắt to đen láy, tóc dài buộc đuôi ngựa. Trang phục: P1 |
| @CoLan | Cô Lan – bán sách | Ngoài 30 → ngoài 60 tuổi | Phụ nữ mặt tròn, tóc uốn ngắn, đeo kính. Trang phục: L1–L2 |

Nhân vật phụ (không cần ảnh tham chiếu, mô tả trực tiếp trong prompt): nhân viên công ty, khách hàng, xã viên hợp tác xã, đại diện tập đoàn nước ngoài, các cổ đông, thanh niên trong làng (người phụ luôn quay từ xa hoặc sau lưng, không rõ mặt).

### 2b. Bảng trang phục theo hoàn cảnh

Mỗi nhân vật có nhiều bộ trang phục (mã "look"), đổi theo tuổi, hoàn cảnh sống và vị trí xã hội. Khuôn mặt giữ nguyên trong mọi look. Ảnh tham chiếu đặt tên `character_refs/<Tag>_<mã look>.png`, ví dụ `KhangMid_M0.png`. Ảnh `<Tag>.png` (không mã) là ảnh mặt trung tính, dùng để giữ khuôn mặt.

**Khang — mười tám tuổi, vừa học xong cấp ba (@KhangYoung)**

| Mã | Hoàn cảnh | Trang phục |
|---|---|---|
| K1 | Ra hiệu sách, đi nhặt ve chai | Áo sơ mi trắng cộc tay cũ hơi ngả vàng, quần âu xanh đen sờn gấu, dép quai hậu, ba lô vải bạt bạc màu |
| K2 | Ở nhà buổi tối, ký ức | Áo ba lỗ trắng cũ giãn cổ, quần vải kẻ ca rô, chân đất |

**Khang — mười tám tuổi, trước ngày lên thành phố (@KhangYoung)**

| Mã | Hoàn cảnh | Trang phục |
|---|---|---|
| T1 | Ở nhà, học đêm | Áo phông bạc màu sờn cổ, quần âu cũ xắn gấu, kính gọng kim loại, dép tổ ong |
| T2 | Theo mẹ lên phố | Sơ mi kẻ ca rô cộc tay cài kín cúc, quần âu xám, dép quai hậu, tóc chải gọn |
| T3 | Đi buôn ở chợ | Áo phông xám ướt mồ hôi, khăn mặt vắt vai, quần lửng, mũ cối, khi mưa khoác áo mưa nilon xanh |

**Khang — thanh niên (@KhangYoung)**

| Mã | Hoàn cảnh | Trang phục |
|---|---|---|
| Y1 | Sinh viên giảng đường, ký túc xá | Sơ mi trắng dài tay xắn đến khuỷu, quần vải xanh đen, ba lô đen, đồng hồ điện tử nhựa |
| Y2 | Phòng thuê khởi nghiệp | Áo phông trắng in hình mờ, quần jeans bạc, dép tổ ong, tóc hơi bù |
| Y3 | Đi bán phần mềm dạo | Sơ mi dài tay trắng sơ vin, quần âu đen, giày da cũ, mũ bảo hiểm nửa đầu, ba lô đầy đĩa CD |
| Y4 | Đêm lũ | Áo mưa nilon rách, áo phông ướt sũng dính người, quần lửng xắn, chân trần lội nước, đèn pin kẹp miệng |
| Y5 | Khắc phục sự cố, điều hành | Sơ mi xanh nhạt cài cúc cổ, quần âu, thắt lưng da, tóc gọn |
| Y6 | Đi chào hàng hợp tác xã | Bộ vest đen đầu tiên hơi rộng vai, sơ mi trắng, cà vạt đỏ đô, giày da mới |
| Y7 | Làm việc với đội kỹ sư | Sơ mi kẻ xanh xắn tay, thẻ nhân viên đeo cổ, bút dạ trong túi áo |
| Y8 | Ra đồng cùng nông dân | Áo phông xám, quần âu xắn ống, ủng cao su, nón lá, máy ảnh số đeo cổ |

**Khang — trung niên (@KhangMid)**

| Mã | Hoàn cảnh | Trang phục |
|---|---|---|
| M0 | Đêm một mình ở văn phòng | Vest navy cởi vắt lưng ghế, sơ mi trắng mở cúc cổ, tay áo xắn, cà vạt tháo lỏng vắt bàn, đồng hồ bạc |
| M1 | Khủng hoảng | Sơ mi trắng nhàu, không cà vạt, tay áo xắn, râu lún phún, mắt thâm |
| M2 | Tái thiết | Áo polo xanh đen, quần kaki be, giày lười |
| M3 | Chủ tịch tập đoàn | Vest xanh navy may đo, sơ mi trắng, không cà vạt, đồng hồ bạc, giày da bóng |
| M4 | Đàm phán bán công ty | Vest ba mảnh đen, sơ mi trắng, cà vạt bạc, khuy măng sét, giày da bóng, tóc chải gọn |
| M5 | Về quê | Sơ mi cotton trắng xắn tay, quần kaki be, dép quai hậu, áo khoác mỏng vắt vai |
| M6 | Ngày khai trương phòng máy | Áo polo trắng, quần kaki xanh rêu, giày vải, tay dính bụi phấn |

**Bà Hạnh (@MeHanh)**

| Mã | Hoàn cảnh | Trang phục |
|---|---|---|
| H1 | Ở nhà, làm việc nhà | Áo cánh hoa nhỏ màu nâu, quần lụa đen, tóc búi thấp, dép nhựa |
| H2 | Ra phố, đèo con | Sơ mi hoa nhạt, quần vải đen, nón lá, xe đạp cũ |
| H3 | Đi bán bông tai ở tiệm vàng | Áo sơ mi trắng là phẳng cài kín cúc, quần âu đen, tóc búi gọn, túi xách da cũ |
| H4 | Tuổi già, hiện tại | Áo len cardigan nâu cũ, áo cánh bên trong, quần lụa đen, tóc bạc trắng búi thấp, chống gậy tre |

**Cô Lan (@CoLan)**

| Mã | Hoàn cảnh | Trang phục |
|---|---|---|
| L1 | Bán sách | Áo blouse xanh nhạt, áo len mỏng khoác ngoài, kính đeo dây, tay áo bọc vải |
| L2 | Tuổi già, hiện tại | Áo khoác len xám sờn, khăn quàng mỏng, kính lão dày, tóc bạc cắt ngắn |

**Mai (@Mai)**

| Mã | Hoàn cảnh | Trang phục |
|---|---|---|
| P1 | Cô gái làng vừa học xong cấp ba, hiện tại | Áo sơ mi trắng cũ hơi rộng, quần âu xanh đen, dép quai hậu, ba lô vải bạc màu, tóc dài buộc đuôi ngựa |

---

## 3. Cấu trúc tổng

| Cảnh | Tên | Thời gian phim | Giai đoạn đời | Số clip | Nhân vật chính |
|---|---|---|---|---|---|
| 01 | Mở đầu: Căn phòng kính | 00:00–01:00 | Hiện tại | 4 | @KhangMid, @KhangYoung |
| 02 | Hiệu sách ở quê | 01:00–03:00 | Mười tám tuổi | 8 | @KhangYoung, @CoLan, @MeHanh |
| 03 | Đôi bông tai và chiếc máy tính | 03:00–05:00 | Mười tám tuổi | 8 | @KhangYoung, @MeHanh |
| 04 | Bài học đầu tiên về tiền | 05:00–06:30 | Năm nhất đại học | 6 | @KhangYoung |
| 05 | Công ty đầu tiên | 06:30–08:30 | Sinh viên | 8 | @KhangYoung |
| 06 | Chợ trên mạng | 08:30–10:00 | Đầu tuổi 20 | 6 | @KhangYoung |
| 07 | Đêm lũ | 10:00–12:00 | Giữa tuổi 20 | 8 | @KhangYoung |
| 08 | Khách hàng lớn đầu tiên | 12:00–14:00 | Cuối tuổi 20 | 8 | @KhangYoung |
| 09 | Sóng lớn | 14:00–16:00 | Đầu tuổi 30 | 8 | @KhangMid |
| 10 | Tập đoàn | 16:00–17:30 | Tuổi 30 | 6 | @KhangMid |
| 11 | Lời đề nghị | 17:30–19:30 | Ngoài 40 | 8 | @KhangMid |
| 12 | Đường về | 19:30–21:30 | Ngoài 40 | 8 | @KhangMid, @CoLan, @MeHanh, @Mai |
| 13 | Quyết định | 21:30–23:00 | Ngoài 40 | 6 | @KhangMid, @CoLan, @MeHanh |
| 14 | Kết: Phòng máy ở hiệu sách | 23:00–24:00 + credit | Ngoài 40 | 4 | @KhangMid, @Mai, @CoLan |
| | **Tổng** | **~25:00 (gồm 1 phút credit)** | | **96** | |

---

## 4. Kịch bản phân cảnh

Quy ước cột "Flow": **I** = Ingredients (dùng ảnh nhân vật tham chiếu), **F** = Frames (nối khung cuối clip trước), **T** = chỉ text (cảnh không có nhân vật chính).

### CẢNH 01 — MỞ ĐẦU: CĂN PHÒNG KÍNH — 4 clip
*Prompt đầy đủ: `canh-01/clip-1.md` → `clip-4.md`*

| Clip | Flow | Hình ảnh | Âm thanh |
|---|---|---|---|
| 1 | I | Thành phố về đêm nhìn từ tầng cao. Văn phòng kính tối, chỉ còn đèn bàn. @KhangMid ngồi một mình, điện thoại úp trên bàn rung liên tục | Tiếng rung điện thoại, điều hòa, xe cộ xa |
| 2 | F | Anh không lật điện thoại. Kéo ngăn tủ thấp, lấy ra hộp giấy cũ: một cuốn sách lập trình bìa sờn, chiếc đĩa mềm | Tiếng ngăn kéo, giấy sột soạt |
| 3 | F | Cận tay lật trang sách: nét chữ nắn nót thời trẻ viết bút bi ở trang đầu. Ánh đèn bàn ấm dần lên | Nhạc piano một nốt, kéo dài |
| 4 | I | Chuyển cảnh khớp hình: trang sách cũ → cùng trang sách mới tinh trên đùi @KhangYoung, nắng chiều trong hiệu sách | Tiếng xe đạp, tiếng ve. Tên phim chèn khi dựng |

**Trang phục:** Clip 1–3: @KhangMid **M0**. Clip 4: @KhangYoung **K1**.

**V.O.:**
> "Đêm nay, Nguyễn Minh Khang phải quyết định có bán đi tất cả những gì mình đã xây hay không. Nhưng câu chuyện bắt đầu sớm hơn nhiều — từ một cuốn sách mà một chàng trai mười tám tuổi không dám xin tiền mẹ để mua."

### CẢNH 02 — HIỆU SÁCH Ở QUÊ — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | I | Con đường quê ngày xưa: xe đạp, hàng tre, ruộng lúa xa xa, biển hiệu sơn tay ở dãy hàng chợ. @KhangYoung đạp chiếc xe đạp cũ đi qua | Chuông xe đạp, loa phường |
| 2 | I | Trong hiệu sách nhỏ, @KhangYoung đứng lặng nhìn kệ sách tin học, ngón tay chạm gáy một cuốn sách lập trình | Quạt trần |
| 3 | I | Cậu lật xem giá ở bìa sau, đếm mấy tờ tiền lẻ trong túi — không đủ | — |
| 4 | I | @KhangYoung nói với @CoLan | **Khang:** "Cô ơi, cô giữ cuốn này cho cháu mấy hôm được không ạ?" |
| 5 | I | Sau những buổi ôn thi, cậu đi dọc đường làng nhặt vỏ lon, giấy vụn, bán cho bà đồng nát, bỏ đồng xu vào ống tre tiết kiệm | Tiếng rao đồng nát |
| 6 | F | Lặp lại nhiều buổi chiều (cắt nhanh), bao ve chai to dần, ống tre nặng dần | Nhạc nhẹ, nhịp tăng |
| 7 | I | Quay lại hiệu sách, cậu đặt nắm tiền lẻ lên quầy, @CoLan mỉm cười đưa sách | **Cô Lan:** "Đây, của cháu đây." |
| 8 | I | Đêm, bóng đèn tròn, cậu ngồi bên bàn học đọc sách, vẽ sơ đồ lên vở. @MeHanh ghé nhìn qua khe cửa | Dế kêu, tiếng mẹ dọn dẹp |

**Trang phục:** Clip 1–7: @KhangYoung **K1**, @CoLan **L1**. Clip 8: @KhangYoung **K2**, @MeHanh **H1**.

**V.O.:**
> "Cậu nhờ cô bán sách giữ lại cuốn sách, rồi suốt nhiều tuần đi nhặt ve chai sau giờ học để đủ tiền mua. Cậu không dám xin mẹ — nhà còn chưa dư dả gì."

### CẢNH 03 — ĐÔI BÔNG TAI VÀ CHIẾC MÁY TÍNH — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | I | Sinh nhật mẹ. @MeHanh hỏi con thích gì. @KhangYoung ngập ngừng | **Bà Hạnh:** "Sinh nhật mẹ, con thích mua gì?" |
| 2 | I | @MeHanh đèo con bằng xe đạp lên phố, tới khu trường đại học, hai mẹ con ở sạp sách cũ, cậu ôm chồng sách lập trình | Phố đông, xe máy |
| 3 | I | Đêm, @MeHanh ngồi bên đèn, tháo đôi bông tai vàng đặt lên lòng bàn tay, ngắm lặng lẽ | Tiếng đồng hồ quả lắc |
| 4 | I | Tiệm vàng nhỏ ở chợ quê: @MeHanh đẩy đôi bông tai qua quầy kính (quay sau lưng chủ tiệm) | Tiếng cân tiểu ly |
| 5 | I | Một chiếc máy tính để bàn màu be, màn hình CRT được khiêng vào nhà. @KhangYoung đứng sững | **Bà Hạnh:** "Của con đấy. Học cho tử tế." |
| 6 | F | Cận màn hình CRT bật lên, ánh xanh dương chiếu lên mặt cậu | Tiếng ổ cứng khởi động, quạt |
| 7 | I | Những đêm gõ phím, giấy nháp đầy mã, ánh màn hình, mẹ đặt cốc sữa bên cạnh | Tiếng bàn phím |
| 8 | F | Gà gáy, trời sáng xám, cậu ngủ gục trên bàn phím, màn hình vẫn sáng | Gà gáy |

**Trang phục:** Clip 1: @KhangYoung **T1**, @MeHanh **H1**. Clip 2: @KhangYoung **T2**, @MeHanh **H2**. Clip 3–4: @MeHanh **H3**. Clip 5–8: @KhangYoung **T1**, @MeHanh **H1**.

**V.O.:**
> "Thời ấy, một chiếc máy tính là cả gia tài. Người mẹ đã bán đôi bông tai vàng hồi môn để đổi lấy nó — đặt cược vào niềm đam mê mà chính bà cũng không hiểu hết."

### CẢNH 04 — BÀI HỌC ĐẦU TIÊN VỀ TIỀN — 6 clip

| Clip | Flow | Hình ảnh | Âm thanh |
|---|---|---|---|
| 1 | I | @KhangYoung chở hàng hóa trên xe đạp, mặc cả ở chợ | Chợ ồn ào |
| 2 | F | Hàng ế, cậu ngồi bệt đếm tiền, lỗ | Mưa lâm râm |
| 3 | I | Cậu viết phần mềm thuê cho một cửa hàng nhỏ, chủ quán đứng xem | Bàn phím |
| 4 | I | Nhận phong bì tiền công, mở ra: vài tờ tiền | — |
| 5 | I | @KhangYoung trong giảng đường đông, ghi chép, mắt nhìn ra cửa sổ | Giảng viên giảng bài |
| 6 | F | Đêm ký túc xá, cậu viết lên tờ giấy tên một công ty — khung hình không cho thấy rõ chữ | Bút trên giấy |

**Trang phục:** Clip 1–2: @KhangYoung **T3**. Clip 3–4: @KhangYoung **T1**. Clip 5–6: @KhangYoung **Y1**.

**V.O.:**
> "Lần đầu đi buôn, cậu lỗ sạch. Nhưng cậu nhận ra thứ mình bán được nhất là những dòng code. Số tiền công viết phần mềm thuê trở thành vốn liếng đầu tiên."

### CẢNH 05 — CÔNG TY ĐẦU TIÊN — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | I | Căn phòng thuê chật, 2 cái bàn, 1 máy tính. @KhangYoung dán tờ giấy lên cửa | Ve sầu, quạt cây |
| 2 | I | Anh đạp xe trong nắng gắt, ba lô đầy đĩa CD phần mềm | Còi xe |
| 3 | I | Gõ cửa một văn phòng, bị từ chối, cửa đóng | Tiếng cửa |
| 4 | I | Cửa hàng thứ hai, anh chạy thử phần mềm trên máy của khách, chủ cửa hàng nhíu mày | **Khang:** "Anh cho em năm phút thôi ạ." |
| 5 | F | Chủ cửa hàng gật đầu, bắt tay | — |
| 6 | I | Phòng thuê đông thêm 3–4 người trẻ, mì tôm, dây mạng chằng chịt | Tiếng modem quay số |
| 7 | I | Cả nhóm nhìn trang web đầu tiên tải từng dòng trên màn hình CRT | Modem, tiếng reo |
| 8 | F | Đêm, @KhangYoung đứng ở ban công nhìn phố, đèn đường vàng | Nhạc chủ đề lần đầu |

**Trang phục:** Clip 1, 6–8: @KhangYoung **Y2**. Clip 2–5: @KhangYoung **Y3**.

**V.O.:**
> "Khi vẫn còn là sinh viên, Khang lập công ty đầu tiên của mình. Những ngày đầu là đi bán phần mềm dạo, gõ từng cánh cửa."

### CẢNH 06 — CHỢ TRÊN MẠNG — 6 clip

| Clip | Flow | Hình ảnh | Âm thanh |
|---|---|---|---|
| 1 | I | Màn hình hiện trang mua bán trực tuyến (giao diện mờ, không đọc rõ chữ), @KhangYoung giải thích cho nhóm | Bàn phím |
| 2 | T | Quán net thời mạng còn chậm, người dùng tò mò lướt web | Tiếng quán net |
| 3 | I | Khách hàng lớn tuổi lắc đầu, ôm chặt túi tiền | Chợ truyền thống |
| 4 | I | @KhangYoung ngồi phân tích bảng số liệu dán đầy tường | — |
| 5 | I | Họp nhóm căng thẳng, lương trễ | Im lặng |
| 6 | F | Anh đứng trước bảng trắng, vẽ một mũi tên đi lên | Nhạc nhịp chậm |

**Trang phục:** Clip 1, 4–6: @KhangYoung **Y5**. Khách hàng lớn tuổi: áo bộ đội bạc màu, mũ cối.

**V.O.:**
> "Anh mở một khu chợ trên mạng — khi hầu hết mọi người còn chưa biết mua bán qua internet là gì. Nhưng người ta chưa quen trả tiền cho thứ không cầm được trên tay. Công ty bắt đầu chật vật."

### CẢNH 07 — ĐÊM LŨ — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | T | Mưa trắng trời trên phố đêm, nước dâng ngập bánh xe máy | Mưa xối xả, sấm |
| 2 | I | @KhangYoung lội nước đến đầu gối, đẩy cửa phòng thuê: nước tràn vào, ổ cắm chập điện tóe lửa | Tiếng nước, điện xèo |
| 3 | I | Cả nhóm hì hục khiêng máy chủ và thùng máy tính lên gác xép dưới ánh đèn pin | **Khang:** "Ổ cứng trước! Cứu ổ cứng trước!" |
| 4 | T | Cận một thùng máy chìm dần trong nước đục, đèn nguồn tắt | Bong bóng nước |
| 5 | I | Sáng hôm sau, nước rút, bùn đầy sàn, cả nhóm ngồi bệt im lặng | Tiếng chổi quét bùn |
| 6 | I | @KhangYoung gọi điện xin lỗi từng khách hàng, liệt kê trên tờ giấy (chữ mờ) | Giọng khách hàng giận dữ, mờ |
| 7 | I | Nhiều đêm liền, anh ngồi khôi phục dữ liệu từ những chiếc đĩa sao lưu, lau khô từng chiếc | Quạt sấy, bàn phím |
| 8 | F | Màn hình hiện dấu tích xanh (không chữ), anh ngả lưng ra ghế, bật cười giữa đống bùn | Nhạc giải tỏa |

**Trang phục:** Clip 2–3, 5: @KhangYoung **Y4**. Clip 6–8: @KhangYoung **Y5**.

**V.O.:**
> "Rồi một đêm, trận lũ lớn nhất trong nhiều năm nhấn chìm căn phòng thuê. Họ cứu được vài ổ cứng, mất gần hết máy móc. Khách hàng nổi giận. Anh mất ba tuần để khôi phục từng dòng dữ liệu — và học được rằng thứ quý nhất của một công ty là niềm tin của người dùng nó."

### CẢNH 08 — KHÁCH HÀNG LỚN ĐẦU TIÊN — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | I | @KhangYoung trong bộ vest rộng vai, đứng chờ trước trụ sở một hợp tác xã nông sản ở tỉnh, tay ôm tập hồ sơ | Ve sầu, tiếng máy cày xa |
| 2 | I | Phòng họp đơn sơ: anh trình bày trước các xã viên lớn tuổi (quay sau lưng họ) | Quạt trần, tiếng xì xào |
| 3 | I | Một ông lão xã viên khoát tay nghi ngờ, anh kiên nhẫn chỉ vào bản vẽ trên giấy | **Khang:** "Bác cứ thử một mùa thôi ạ." |
| 4 | I | Anh ra đồng cùng nông dân, chụp ảnh từng sọt rau, từng bao gạo bằng máy ảnh số | Gió đồng, tiếng gà |
| 5 | I | Văn phòng mới, đội kỹ sư dựng trang bán nông sản trực tuyến | Bàn phím rộn ràng |
| 6 | I | Đơn hàng đầu tiên: màn hình hiện dấu tích xanh (không chữ), cả đội reo hò | Tiếng "ting", vỗ tay |
| 7 | T | Xe tải chở nông sản lăn bánh trên đường làng lúc bình minh | Động cơ xe |
| 8 | I | Ông lão xã viên bắt tay anh, cười móm mém | Nhạc ấm |

**Trang phục:** Clip 1–3: @KhangYoung **Y6**. Clip 4, 8: @KhangYoung **Y8**. Clip 5–6: @KhangYoung **Y7**.

**V.O.:**
> "Khách hàng lớn đầu tiên không ở thành phố. Đó là một hợp tác xã nông sản — nơi người ta chưa từng bán thứ gì qua mạng. Anh ra tận ruộng, chụp từng sọt rau. Mùa đầu tiên, nông sản của họ đi xa hơn bao giờ hết."

### CẢNH 09 — SÓNG LỚN — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh |
|---|---|---|---|
| 1 | T | Xe giao hàng, biển quảng cáo của các sàn mua sắm lớn (không logo) tràn phố | Quảng cáo ồn |
| 2 | I | @KhangMid nhìn biểu đồ lượng truy cập đi xuống | Im |
| 3 | I | Họp hội đồng, gương mặt căng thẳng | Đồng hồ |
| 4 | I | Văn phòng vắng dần, ghế trống | Tiếng bước chân |
| 5 | I | Đêm, anh đứng một mình giữa văn phòng trống | Mưa |
| 6 | I | Anh vẽ sơ đồ hình bông hoa: ở giữa là thanh toán, các cánh là giao hàng, bán hàng | Bút dạ |
| 7 | I | Bên bàn làm việc với người vợ đồng sáng lập (quay nghiêng, không rõ mặt) | — |
| 8 | F | Bình minh trên tòa nhà mới, kính phản chiếu mặt trời | Nhạc dâng |

**Trang phục:** Clip 2–5: @KhangMid **M1**. Clip 6–7: @KhangMid **M2**.

**V.O.:**
> "Rồi những gã khổng lồ tràn vào, đốt tiền giành thị trường. Khách hàng lần lượt bỏ đi, khu chợ đầu tay mất dần chỗ đứng. Anh buông nó, tái cấu trúc tất cả, và xây lại theo một cách khác."

### CẢNH 10 — TẬP ĐOÀN — 6 clip

| Clip | Flow | Hình ảnh | Âm thanh |
|---|---|---|---|
| 1 | T | Kho hàng rộng, băng chuyền phân loại | Máy móc |
| 2 | T | Người bán hàng rong quẹt thẻ qua thiết bị thanh toán nhỏ | Tiếng "bíp" |
| 3 | I | @KhangMid đi giữa các tầng văn phòng, nhân viên trẻ chào | Văn phòng |
| 4 | I | Anh phát biểu trên sân khấu sự kiện công nghệ, màn hình LED phía sau (trừu tượng) | Vỗ tay |
| 5 | I | Phỏng vấn báo chí, anh nói về việc tin tưởng người trẻ | Máy quay |
| 6 | F | Toàn cảnh flycam tòa nhà văn phòng lúc hoàng hôn | Nhạc |

**Trang phục:** Clip 3–5: @KhangMid **M3**.

**V.O.:**
> "Ví điện tử, máy quẹt thẻ, kho vận, quỹ đầu tư… hàng chục công ty con. Báo chí bắt đầu gọi anh là một trong những người tiên phong của công nghệ Việt."

### CẢNH 11 — LỜI ĐỀ NGHỊ — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | T | Sảnh khách sạn cao cấp, đoàn luật sư mặc vest đen kéo vali tài liệu (không rõ mặt) | Bước chân trên đá hoa |
| 2 | I | Phòng họp tầng thượng, bàn kính dài. @KhangMid ngồi một bên, phía bên kia là đại diện một tập đoàn nước ngoài khổng lồ (quay sau lưng) | Điều hòa, giấy lật |
| 3 | I | Tập hồ sơ dày được đẩy qua bàn, @KhangMid mở ra, dừng lại ở một trang, ánh mắt khựng lại | **Đối tác (tiếng Anh, mờ, phụ đề khi dựng):** "Đây là con số cuối cùng." |
| 4 | I | Cận bàn tay anh gõ nhẹ cây bút lên bàn kính | Tiếng gõ đều |
| 5 | I | Phòng họp hội đồng của tập đoàn: các cổ đông tranh cãi, người muốn bán, người muốn giữ | Tiếng nói chồng lớp |
| 6 | I | @KhangMid đứng một mình bên cửa kính, nhìn xuống thành phố, điện thoại rung không ngừng | Rung điện thoại |
| 7 | T | Bàn làm việc: bút ký đặt cạnh bản hợp đồng (chữ mờ), đồng hồ chỉ gần nửa đêm | Đồng hồ tích tắc |
| 8 | F | Nối về đêm mở đầu phim: anh mở hộp đồ cũ, cầm cuốn sách lập trình (nối cảnh 01) | Một nốt piano |

**Trang phục:** Clip 2–4: @KhangMid **M4**. Clip 5–6, 8: @KhangMid **M0**.

**V.O.:**
> "Rồi một ngày, một tập đoàn nước ngoài khổng lồ ngỏ ý mua lại tất cả. Con số trên bàn đủ để anh không bao giờ phải làm việc nữa. Họ cho anh một đêm để quyết định. Và đó chính là cái đêm anh mở lại chiếc hộp cũ."

### CẢNH 12 — ĐƯỜNG VỀ — 8 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | T | Rạng sáng, xe ô tô chạy trên con đường quê, ruộng lúa phủ sương | Tiếng xe, chim sáo |
| 2 | I | @KhangMid bước xuống xe trước dãy hàng chợ quê, nhìn quanh như người lạ | Chợ sớm |
| 3 | I | Hiệu sách cũ giờ đã đóng cửa phần lớn, kệ trống. @CoLan, giờ đã già, ngồi xếp sách vào thùng | Quạt trần kẽo kẹt |
| 4 | I | @CoLan ngẩng lên, nheo mắt nhận ra anh | **Cô Lan:** "Khang đấy à… cậu sinh viên mua cuốn sách lập trình năm nào?" |
| 5 | I | Trước cổng trường cấp ba của làng, mấy cô cậu vừa thi xong chen nhau xem chung một chiếc điện thoại cũ màn hình nứt, trong đó có @Mai | Tiếng nói cười |
| 6 | I | Cận @Mai: cô gái lén đếm mấy đồng tiền lẻ trong túi áo, giống hệt Khang ngày trước | — |
| 7 | I | Nhà cũ. @MeHanh, giờ đã già, ra cửa đón con, hai mẹ con ôm nhau | **Bà Hạnh:** "Về rồi đấy à con." |
| 8 | F | Bữa cơm đơn sơ hai mẹ con, chiếc máy tính màu be phủ khăn ở góc nhà | Bát đũa, gió thổi qua tre |

**Trang phục:** Clip 2–4, 7–8: @KhangMid **M5**. Clip 3–4: @CoLan **L2**. Clip 5–6: @Mai **P1**. Clip 7–8: @MeHanh **H4**.

**V.O.:**
> "Sáng hôm sau, anh không đến phòng họp. Anh lái xe về quê. Hiệu sách năm xưa sắp đóng cửa. Và ở cổng trường làng, anh thấy chính mình của hơn hai mươi năm trước — trong đôi mắt một cô gái đang đếm từng đồng tiền lẻ."

### CẢNH 13 — QUYẾT ĐỊNH — 6 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | I | Đêm ở nhà cũ, @KhangMid lau bụi chiếc máy tính màu be, cắm điện, màn hình CRT chập chờn rồi sáng | Tiếng ổ cứng khởi động |
| 2 | I | Anh gọi điện cho hội đồng, đứng ngoài hiên, trăng sáng | **Khang:** "Tôi không bán." |
| 3 | I | Phòng họp hội đồng ở thành phố, các cổ đông nhìn nhau, có người đứng dậy bỏ đi (quay xa) | Ghế kéo |
| 4 | I | @KhangMid ngồi với @CoLan trong hiệu sách, trải bản vẽ phác lên quầy gỗ: kệ sách cũ và một dãy bàn máy tính | Bút chì |
| 5 | T | Thợ sơn lại mặt tiền hiệu sách, dãy máy tính mới được khiêng vào | Tiếng búa, tiếng cười |
| 6 | I | @MeHanh đứng nhìn con từ xa, mỉm cười | Nhạc chủ đề dâng lên |

**Trang phục:** Clip 1–2, 4: @KhangMid **M5**. Clip 3: các cổ đông mặc vest. Clip 4: @CoLan **L2**. Clip 6: @MeHanh **H4**.

**V.O.:**
> "Anh từ chối lời đề nghị. Có người gọi đó là sai lầm lớn nhất đời anh. Nhưng anh đã quyết: hiệu sách năm xưa sẽ không đóng cửa — nó sẽ trở thành một phòng máy miễn phí cho bọn trẻ trong làng."

### CẢNH 14 — KẾT: PHÒNG MÁY Ở HIỆU SÁCH — 4 clip

| Clip | Flow | Hình ảnh | Âm thanh / thoại |
|---|---|---|---|
| 1 | I | Hiệu sách mới: kệ sách cũ một bên, dãy máy tính một bên, thanh niên trong làng ùa vào, @CoLan đứng quầy | Tiếng reo |
| 2 | I | @Mai rụt rè ngồi trước máy, @KhangMid đặt cuốn sách lập trình cũ của mình lên bàn cô gái | **Khang:** "Của cháu đây." |
| 3 | I | Cận mặt @Mai, ánh màn hình xanh chiếu lên, mắt sáng lên — khớp hình với cảnh 03 khi Khang lần đầu bật máy | Tiếng bàn phím đầu tiên |
| 4 | T | Toàn cảnh hiệu sách lúc chiều tà nhìn từ con đường quê, đèn trong nhà sáng ấm, một chiếc xe đạp đi qua → đen | Chuông xe đạp, nhạc kết |

**Trang phục:** Clip 1–2: @KhangMid **M6**, @CoLan **L2**. Clip 2–3: @Mai **P1**.

**V.O.:**
> "Hơn hai mươi năm trước, một người mẹ đã bán đôi bông tai hồi môn để con mình có một chiếc máy tính. Giờ đây, đến lượt anh trao lại cuốn sách ấy. Có những thứ không bao giờ nên bán — vì chính chúng đã làm nên ta."

---

## 5. Hướng dẫn dựng hậu kỳ

- Tỉ lệ 16:9, 24fps. Màu: cảnh 02–05 ấm, hạt phim 35mm; cảnh 06–10 trung tính sáng; cảnh 11 lạnh, tương phản cao; cảnh 12–14 trở lại ấm, nắng quê.
- Không chèn mốc năm. Chuyển giai đoạn bằng hình ảnh (đồ vật, công nghệ, trang phục) và thẻ chương ngắn nếu cần, ví dụ "Phần 1: Cuốn sách".
- Lời dẫn: giọng nam trầm, tốc độ khoảng 140 từ/phút.
- Ghép: CapCut/Premiere, hoặc Scenebuilder trong Flow.
