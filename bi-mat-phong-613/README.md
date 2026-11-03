# Bí Mật Phòng 613: Lời Cảnh Báo Đêm Rằm — Phim Ngắn Tâm Lý Bí Ẩn (15 Cảnh × 6 Clips × 10s = 90 Clips | Google Flow Omni 10s (omni_flash))

Dự án phim ngắn (**15 Cảnh × 6 Clips × 10 giây = 90 Prompts = 900 giây (15 phút)**, chuẩn khung hình điện ảnh **16:9 24fps**, sử dụng model **`veo-lite` (`omni_flash`)** kết hợp **Extend Video / nối chuỗi khung hình cuối liền mạch từ Clip 1 đến Clip 6 mỗi cảnh**) được xây dựng từ việc phân tích chuyên sâu bộ phim ngắn triệu view **[Phim ngắn 613 | CFilm Shorts](https://www.youtube.com/watch?v=507rDK3xPcM)** (Đạo diễn Dinh Gốc, Biên kịch Nhật Khoa, DOP Sơn Thái Phạm — 14 phút 34 giây, ~1,78 triệu lượt xem), đồng thời **nâng cấp toàn diện kịch bản, giải quyết triệt để các điểm hạn chế được khán giả góp ý** và **chuẩn hóa 100% theo tiêu chuẩn an toàn & liên tục của Google Flow (`omni_flash` 8s)**.

- [Kịch bản chi tiết 15 Cảnh (90 Clips × 10s)](KICH_BAN_15_PHUT.md)
- [Khóa Nhân vật, Bối cảnh & Đạo cụ trên Google Flow](FLOW_PROMPTS.md)
- [Runner tự động hóa FlowKit (`omni_flash` 8s + Video Extend)](../flowkit/runners/bi_mat_phong_613.py)

---

## PHẦN 1: PHÂN TÍCH CHUYÊN SÂU "PHIM NGẮN 613 | CFILM SHORTS" (`https://www.youtube.com/watch?v=507rDK3xPcM`)

### 1. Thông số kỹ thuật & Ekip sản xuất gốc
- **Tựa gốc:** *Phim ngắn 613 | CFilm Shorts | Phim ngắn kinh dị hay nhất 2023*
- **Kênh phát hành:** CL Film (`@clfilm.celebgroup` — Celeb Network)
- **Thời lượng gốc:** `874 giây` (**14 phút 34 giây**, bao gồm ~13 phút 55 giây nội dung chính + ~39 giây credit & hậu trường).
- **Tỷ lệ khung hình:** `16:9` Widescreen (`1280×720` / `1920×1080`).
- **Model & Cấu hình Render Phim Mới:** `omni_flash` (`model_family="veo"`, **10 giây/clip**), Clip 1 tạo Start Frame khóa nhân vật bằng `nano_banana_pro` + `omni_flash`, Clip 2–6 **Extend Video** liên hoàn từ frame cuối của clip trước.
- **Tông màu chủ đạo (Color Palette):** Xanh ngọc / xanh rêu trầm của chung cư cũ (`Institutional Jade/Cyan Green`) đối lập với sắc cam/đỏ ấm của lửa vàng mã, nhang, ly nến đỏ và đèn thờ (`Warm Amber & Altar Crimson`).
- **Dàn nhân vật tối giản (4 nhân vật):**
  1. **Phương** (Choco Trúc Phương): Cô bạn yếu bóng vía, tin tâm linh, nhạy cảm, hay cúng kiếng và cầu khấn.
  2. **Trinh** (Thuỳ Trinh): Cô bạn cùng phòng cá tính, thực tế, không tin ma quỷ và liên tục phạm vào các điều kiêng kỵ dân gian.
  3. **Bác Bảo Vệ** (Duy Anh): Bảo vệ trực đêm gương mặt lạnh lùng, xuất hiện như người giúp đỡ nhưng thực chất là nhân tố dẫn dụ hai cô gái vào bẫy.
  4. **Ma Nữ** (Gia Linh): Cô gái mặc đầm trắng tóc dài xuất hiện trong gương, khu phơi đồ và hành lang.

### 2. Giải phẫu cấu trúc 7 Trường đoạn (175 Storyboard Frames từ `00:00` đến `14:34`)
1. **Trường đoạn 1 (`00:00–02:05` — Nhập trạch Phòng 613 & Điều kiêng kỵ số 1):**
   - Mở đầu bằng toàn cảnh dãy chung cư cũ kỹ và cận cảnh bảng số phòng **`613`** bằng gỗ mục cùng gương Bát Quái.
   - Phương ngồi xổm ngoài hành lang đốt vàng mã và cắm 3 nén nhang trong ly gạo. Trinh xách xô nước đi tới vô tình làm nước sánh tắt lửa cúng. Phương hốt hoảng chắp tay vái lạy xin lỗi khuất mặt khuất mày.
   - Bên trong phòng 613 (tường xanh ngọc, rèm vải xanh đậm), Trinh vào phòng tắm gội đầu dưới vòi sen thì đèn chập chờn và có cảm giác bị rình rập.
2. **Trường đoạn 2 (`02:05–04:10` — Bàn thờ cũ & Đốt lá bùa trấn):**
   - Trinh bước ra khỏi phòng tắm giật mình bởi bóng tóc dài sau rèm xanh (cú hù giả — hóa ra là Phương).
   - Khi thấy lá bùa vàng dán trong phòng, Trinh chế giễu sự mê tín của Phương rồi tự tay xé và **đốt lá bùa vàng** bất chấp Phương van xin (*Điều kiêng kỵ số 2*).
3. **Trường đoạn 3 (`04:10–06:15` — Soi gương tròn đêm trăng & Khe cửa hé mở):**
   - Đêm trăng tròn, Phương đeo băng đô trắng ngồi trang điểm trước chiếc gương tròn nhỏ (*Điều kiêng kỵ số 3: soi gương lúc nửa đêm*). Trong gương hiện lên bóng Ma Nữ đứng phía sau.
   - Cửa phòng tự hé mở; khi Phương ghé mắt nhìn qua khe cửa thì bị Ma Nữ hù dọa. Trinh vẫn không tin và ôm đồ đi ra hành lang phơi giữa đêm khuya (*Điều kiêng kỵ số 4: phơi đồ ban đêm*).
4. **Trường đoạn 4 (`06:15–08:20` — Khu phơi đồ cúp điện & Ly nến đỏ):**
   - Ngoài cầu thang bê tông và giàn phơi đồ tối om, Trinh thấy bóng Ma Nữ đứng trên bậc thang và ẩn hiện giữa những chiếc áo đen treo trên sào.
   - Điện cúp tối đen; Trinh phải cầm một **chiếc ly nến đỏ** dò dẫm giữa giàn đồ phơi và bị Ma Nữ dọa đến mức ngồi thụp xuống khóc thét.
5. **Trường đoạn 5 (`08:20–10:25` — Bác Bảo Vệ xuất hiện & Căn phòng 613 bị bao vây):**
   - Chạy khỏi khu phơi đồ, Trinh đụng phải **Bác Bảo Vệ** ở cầu thang. Ông ta đưa Trinh về lại phòng 613.
   - Trong phòng, cả Trinh và Phương đều bị hiện tượng tâm linh tấn công dồn vào góc tường dưới ánh đèn chập chờn.
6. **Trường đoạn 6 (`10:25–13:15` — Lá bùa của Bác Bảo Vệ & Cao trào hành lang):**
   - Bác Bảo Vệ bước vào phòng 613, châm một nén nhang, chỉ tay vào cửa và đưa cho Phương một lá bùa vàng bảo làm theo lời ông ta.
   - Thế nhưng ngay sau đó đèn tắt phụt, Ma Nữ xuất hiện ở cuối hành lang lao vào tấn công Phương.
7. **Trường đoạn 7 (`13:15–14:34` — Cú Twist buổi sáng: Ổ khóa ngoài, Gương cầu & Hai khung ảnh thờ đỏ):**
   - Sáng hôm sau, cửa sắt phòng 613 bị khóa ổ khóa bên ngoài, tấm rèm xanh khép kín.
   - Dưới sân chung cư, hai cô gái nhìn qua chiếc gương tròn và phát hiện trong căn phòng tối nhuộm **ánh đèn thờ đỏ** có treo **hai khung ảnh thờ** trên tường: thực chất cả Ma Nữ lẫn Bác Bảo Vệ đều là vong hồn, trong đó Ma Nữ hù dọa để đuổi hai cô gái đi sớm, còn Bác Bảo Vệ mới là kẻ muốn hại hai cô ở lại!

### 3. Đánh giá Ưu điểm & Nhược điểm từ Phản hồi Khán giả (YouTube Comments)
- **Điểm mạnh giúp phim đạt 1,78 triệu view:**
  - Bối cảnh phòng trọ / chung cư cũ Việt Nam cực kỳ gần gũi với sinh viên và người đi làm thuê nhà giá rẻ.
  - Khai thác trúng tâm lý **4 điều kiêng kỵ dân gian Việt Nam**: (1) Làm tắt lửa cúng nhập trạch; (2) Tự ý xé/đốt bùa niêm phong cũ; (3) Soi gương tròn chải tóc lúc nửa đêm; (4) Phơi quần áo ngoài hành lang vào ban đêm.
  - Thiết kế ánh sáng xanh rêu – đỏ nến/nhang tạo tương phản thị giác mạnh.
- **3 Điểm yếu lớn khán giả phàn nàn nhiều nhất (đã được khắc phục triệt để trong bản phim mới của chúng ta):**
  1. *Cốt truyện và cú twist cuối quá mơ hồ:* Rất nhiều khán giả bình luận *"Coi xong không hiểu rốt cuộc 2 con ma muốn gì, tại sao ông bảo vệ lại xúi đốt bùa"*. -> **Giải pháp của chúng ta:** Xây dựng đường dây điều tra rõ ràng qua **chiếc hộp sắt trong tủ gỗ** và **cuốn sổ nhật ký vụ cháy ngày 03/11/2016**, giúp người xem hiểu rõ 100% động cơ của Linh (bảo vệ bằng chứng và cứu hai cô gái) và Ông Bảy (muốn mượn tay hai cô đốt sạch bằng chứng tội lỗi năm xưa).
  2. *Lỗi rắc-co ánh sáng (Continuity error):* Khán giả chỉ ra *"Sạn ngay khúc Trinh đi phơi đồ trời tối, chuyển cảnh lên cầu thang lại là trời sáng"*. -> **Giải pháp của chúng ta:** Khóa chặt `FIXED SCENE SPATIAL & LIGHTING LOCK` xuyên suốt Cảnh 06–08 ở trạng thái đêm trăng rằm + cúp điện + ánh nến đỏ.
  3. *Cảnh bóp cổ cuối phim vừa giả vừa dễ vi phạm chính sách AI:* -> **Giải pháp của chúng ta:** Thay thế hoàn toàn bạo lực vật lý bằng **kịch tính tâm lý điện ảnh** (Ông Bảy khóa trái cửa sắt từ bên ngoài định nhốt hai cô gái như năm 2016, và Linh xuất hiện ở đầu hành lang làm bung ổ khóa sắt giải cứu hai cô), vừa sâu sắc giàu cảm xúc vừa **100% vượt qua bộ lọc an toàn của Google Flow / Google Flow Omni**.

---

## PHẦN 2: CẤU TRÚC PHIM "BÍ MẬT PHÒNG 613: LỜI CẢNH BÁO ĐÊM RẰM" (15 CẢNH × 6 CLIPS × 8S = 90 CLIPS)

| Hồi | Cảnh | Thời Lượng | Tựa Cảnh | Nội Dung Trọng Tâm |
|---|---|---|---|---|
| **HỒI I** | [Cảnh 01](canh-01/README.md) | `6 × 10s (60s)` | Bảng Số 613 & Chậu Than Cúng Nhập Trạch | Phương cúng nhập trạch trước cửa phòng 613; Trinh xách xô nước làm tắt lửa cúng; nén nhang giữa tự tắt. |
| **HỒI I** | [Cảnh 02](canh-02/README.md) | `6 × 10s (60s)` | Chiếc Gương Tròn & Lá Giấy Niêm Phong Trên Tủ Gỗ | Phương nhặt được vòng chỉ đỏ gắn chuông bạc bên gương tròn; ngăn Trinh bóc lá giấy vàng niêm phong tủ gỗ. |
| **HỒI I** | [Cảnh 03](canh-03/README.md) | `6 × 10s (60s)` | Tiếng Gõ Trong Phòng Tắm & Bóng Người Qua Rèm Xanh | Trinh tắm dưới vòi sen nghe 3 tiếng gõ kính mờ; bước ra giật mình gặp Phương sau rèm xanh; phát hiện vệt nước dẫn vào tủ gỗ. |
| **HỒI I** | [Cảnh 04](canh-04/README.md) | `6 × 10s (60s)` | Phản Chiếu Chậm Một Giây Trong Gương Tròn Đêm Trăng | Phương chải tóc đêm rằm trước gương tròn; bóng trong gương quay chậm 1 nhịp và hiện hình Linh chỉ tay vào tủ gỗ; cửa tự mở hé. |
| **HỒI I** | [Cảnh 05](canh-05/README.md) | `6 × 10s (60s)` | Trinh Đốt Lá Giấy Niêm Phong & Đi Phơi Đồ Đêm Khuya | Trinh xé và đốt lá giấy vàng trên tủ để trấn an Phương, rồi bê rổ quần áo ra sân phơi giữa đêm rằm. |
| **HỒI II** | [Cảnh 06](canh-06/README.md) | `6 × 10s (60s)` | Bóng Áo Trắng Giữa Giàn Đồ Phơi Đêm | Ngoài sân phơi và cầu thang tối, Trinh thấy Linh ẩn hiện giữa những chiếc áo đen; cầu dao điện sập tắt phụt; Trinh thắp ly nến đỏ. |
| **HỒI II** | [Cảnh 07](canh-07/README.md) | `6 × 10s (60s)` | Ánh Nến Đỏ & Lời Thì Thầm Giữa Cầu Thang | Cầm ly nến đỏ đi giữa giàn đồ, Trinh đối mặt Linh và nghe lời cảnh báo *"Đừng nghe ông bảo vệ đốt chiếc hộp trong tủ"*; chạy xuống đụng Ông Bảy. |
| **HỒI II** | [Cảnh 08](canh-08/README.md) | `6 × 10s (60s)` | Cuộc Gặp Ông Bảy Bảo Vệ Ở Hành Lang Lô C | Ông Bảy Bảo Vệ biến sắc khi nghe nhắc tới chiếc hộp sắt trong tủ, dẫn Trinh về phòng 613 và liếc nhìn vết giấy niêm phong bị xé. |
| **HỒI II** | [Cảnh 09](canh-09/README.md) | `6 × 10s (60s)` | Căn Phòng 613 Rung Chuyển & Cuộc Gọi Từ Máy Nội Bộ | Điện thoại nội bộ đứt dây trên tường tự đổ chuông phát ra tiếng lửa cháy ngày `03-11-2016`; hai cánh tủ gỗ tự bung mở lộ ra chiếc hộp sắt. |
| **HỒI II** | [Cảnh 10](canh-10/README.md) | `6 × 10s (60s)` | Ông Bảy Trao Lá Bùa Lạ & Xúi Đốt Cuốn Sổ Trong Tủ | Ông Bảy vào phòng châm nhang, đưa lá bùa xám và ép hai cô gái phải đốt sạch mọi giấy tờ trong hộp sắt trước 3 giờ sáng mà không được đọc. |
| **HỒI III** | [Cảnh 11](canh-11/README.md) | `6 × 10s (60s)` | Chiếc Hộp Sắt Mở Ra & Cuốn Nhật Ký Của Linh | Gương tròn chiếu ánh trăng ngăn Phương đốt hộp; mở hộp phát hiện thẻ sinh viên của Linh, bài báo vụ cháy 2016 và nhật ký tố cáo Ông Bảy. |
| **HỒI III** | [Cảnh 12](canh-12/README.md) | `6 × 10s (60s)` | Cú Twist Thứ Nhất — Kẻ Muốn Khóa Trái Cửa Phòng 613 | Đúng 3 giờ sáng, Ông Bảy phát hiện hai cô đã đọc cuốn sổ liền bấm ổ khóa sắt khóa nhốt hai cô từ bên ngoài như năm 2016; Linh xuất hiện ở cuối hành lang. |
| **HỒI III** | [Cảnh 13](canh-13/README.md) | `6 × 10s (60s)` | Đêm Đối Đầu Ở Hành Lang 613 — Bóng Áo Trắng Mở Khóa | Linh tiến tới đối diện khiến Ông Bảy kinh hoàng đánh rơi chùm chìa khóa đồng rồi tan biến vào bóng tối cầu thang; Linh chạm tay mở bung ổ khóa cứu hai cô. |
| **HỒI III** | [Cảnh 14](canh-14/README.md) | `6 × 10s (60s)` | Lời Hứa Lúc Rạng Đông & Căn Phòng 613 Khép Lại | Phương và Trinh hứa đưa cuốn sổ ra ánh sáng; Linh mỉm cười tan vào nắng sớm; hai cô khóa cửa trả phòng 613 và kéo vali xuống sân. |
| **HỒI III** | [Cảnh 15](canh-15/README.md) | `6 × 10s (60s)` | Cú Twist Cuối Dưới Sân Chung Cư — Hai Khung Ảnh Thờ Đỏ | Nhìn qua gương cầu tròn trước bốt bảo vệ bỏ hoang, hai cô phát hiện bên trong ánh đèn đỏ là **hai khung ảnh thờ** của cả Linh lẫn Ông Bảy (đều mất ngày 03/11/2016). |
