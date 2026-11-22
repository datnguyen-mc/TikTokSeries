# TẬP 17 · POMPEII – 32 giờ cuối cùng của thành phố La Mã

Kế hoạch sản xuất Stickman tập 17, cùng format với 15 Chernobyl và 16 Titanic.

| Hạng mục | Thông số |
|---|---|
| Phim chính | 16:9, khoảng 12,5 phút, 12 chương + mở đầu + kết |
| Shorts | 12 video 9:16 (mỗi chương một video), VI + EN |
| Lời dẫn VI | `script_src.py`: 2.551 âm tiết, khoảng 11,5 phút chưa tính thẻ chương và pad |
| Nền | 58 prompt `p01`–`p58` trong `flow/prompts.py` |
| Clip Veo | 24 prompt `k1`–`k24` trong `flow/prompts.py` |
| Thư mục | `17-pompeii/` với cấu trúc như `16-titanic/`: `phim_16x9/`, `shorts_9x16/`, `EN/`, `flow_refs/` |

---

## 1. Cách kể

- **Một ngày bình thường bị giữ lại.** Mở bằng cảnh đời thường (chợ, lò bánh mì, khẩu hiệu tranh cử) rồi mới đến tai họa. Kết lại về con người, không về con số.
- **Giữ nhịp từng giờ như Titanic.** Chương 3–7 đi theo đồng hồ 32 giờ (nghiên cứu Scarpati và cộng sự, 2025). Góc màn hình có đồng hồ đếm giờ: T+0h, T+6h, T+18h, T+32h.
- **Hai câu gài – một câu trả:**
  - Ch.3 gài: *"Theo lá thư, hôm đó là ngày 24/8. Hãy nhớ con số này."* → Ch.10 trả: dòng chữ than 17/10 làm ngày tháng bị đặt lại câu hỏi.
  - Ch.12 nối lại: *đêm 24/8/1943*, đúng "ngày Pompeii bị hủy diệt" theo sách sử, máy bay Đồng minh ném bom khu di tích.
- **Nhân vật xuyên suốt:** Pliny Trẻ (17 tuổi, nhân chứng) và Pliny Già (đô đốc, đi cứu người). Họ là "Alex" của tập này, nhưng là người thật.
- **Kết bằng câu hỏi bình luận:** *"Bạn sẽ chạy, hay ở lại?"* Đây là lựa chọn có thật của người Pompeii ở Ch.4.

---

## 2. Mười hai chương

Số âm tiết và thời lượng lấy từ lần chạy `script_src.py`, ước 3,7 âm tiết mỗi giây.

| # | Slug | Tựa VI | Tựa EN | Mốc | Ý chính | Âm tiết · giây |
|---|---|---|---|---|---|---|
| 00 | mo-dau | POMPEII | POMPEII | 79 | Một ngày bình thường, chưa đầy 2 ngày sau biến mất, bị quên 1.700 năm | 74 · 20s |
| 01 | thanh-pho | THÀNH PHỐ DƯỚI CHÂN NÚI | THE CITY BELOW THE MOUNTAIN | Trước 79 | Cảng sầm uất, garum ("nước mắm La Mã"), khoảng 80 quầy đồ ăn nóng, đấu trường 20.000 chỗ, graffiti "Hỡi bức tường…", núi phủ vườn nho | 167 · 45s |
| 02 | con-rung | NHỮNG CƠN RUNG | THE TREMORS | 62 – 79 | Động đất 5/2/62, đàn 600 con cừu chết (Seneca), 17 năm vẫn sửa dở, rung dày hơn những ngày cuối | 169 · 46s |
| 03 | dam-may | ĐÁM MÂY HÌNH CÂY THÔNG | THE PINE-TREE CLOUD | Ngày 1 · đầu chiều | Pliny Trẻ 17 tuổi ở Misenum, cột tro hơn 30 km (gần 4 lần Everest), lá thư gửi Tacitus, "Plinian", **gài 24/8** | 185 · 50s |
| 04 | mua-da | TRỜI TỐI GIỮA BAN NGÀY | DARKNESS AT NOON | Ngày 1 · chiều | Gió đông nam, mưa đá bọt 15 cm/giờ suốt khoảng 17 tiếng, chạy hay ở lại, mái sập dưới gần 3 m đá | 173 · 47s |
| 05 | do-doc | CHUYẾN TÀU CỦA ĐÔ ĐỐC | THE ADMIRAL'S VOYAGE | Ngày 1 | Thư cầu cứu của Rectina, chiến thuyền, *"Vận may đứng về phía người dũng cảm"*, Stabiae, Pliny Già mất trên bờ biển | 214 · 58s |
| 06 | herculaneum | NỬA ĐÊM Ở HERCULANEUM | MIDNIGHT AT HERCULANEUM | Đêm ngày 1 | Người dân chờ tàu trong hầm thuyền, cột tro sụp, dòng chảy hỏa thành vụn, hơn 300 bộ hài cốt (thập niên 1980), não hóa thủy tinh, vùi hơn 20 m | 196 · 53s |
| 07 | buoi-sang | BUỔI SÁNG CUỐI CÙNG | THE LAST MORNING | Ngày 2 | Ngay sau 7 giờ sáng, dòng chảy tràn qua tường thành; mẹ con Pliny Trẻ chạy trong bóng tối; khoảng 32 giờ thì dừng | 187 · 51s |
| 08 | lang-quen | THÀNH PHỐ BỊ LÃNG QUÊN | THE FORGOTTEN CITY | 79 – 1763 | Titus cứu trợ, người nghèo quay lại sống tạm (phát hiện 2025), "La Civita", kênh đào xuyên thành phố, năm 1738, 1748, 1763 | 229 · 62s |
| 09 | khoang-trong | NHỮNG KHOẢNG TRỐNG TRONG TRO | THE HOLES IN THE ASH | 1863 | Fiorelli đổ thạch cao vào khoảng rỗng, chú chó bị xích, hơn 100 tượng, hệ đánh số nhà | 216 · 58s |
| 10 | bi-mat-moi | NHỮNG BÍ MẬT MỚI | NEW SECRETS | 2018 – 2024 | **Trả 24/8**: chữ than 17/10, trái cây mùa thu; ADN năm 2024 lật lại chuyện "mẹ con", "hai chị em"; tổ tiên phía đông Địa Trung Hải | 218 · 59s |
| 11 | thu-vien | THƯ VIỆN HÓA THAN | THE CHARRED LIBRARY | 1752 – 2026 | Biệt thự Giấy cói, khoảng 1.800 cuộn, Vesuvius Challenge, chữ "màu tím" (10/2023), giải 700.000 USD (2/2024), tên sách *Bàn về các thói xấu* (5/2025), hơn 70 cột chữ (6/2026) | 238 · 64s |
| 12 | van-thuc | NÚI LỬA VẪN THỨC | THE VOLCANO IS STILL AWAKE | 1943 – nay | Bom ngày 24/8/1943, phun trào 3/1944 hủy khoảng 80 máy bay B-25, vùng đỏ khoảng 700.000 dân và sơ tán trong 72 giờ, Campi Flegrei M4,7 (31/7/2026), hơn 4 triệu khách mỗi năm, 1/3 thành phố còn dưới tro | 229 · 62s |
| 13 | ket | HẾT | THE END | — | "Một ngày bình thường được giữ lại…", hỏi: chạy hay ở lại? | 56 · 15s |

---

## 3. Dàn cảnh từng chương

Cột "Nền / Veo" dùng mã trong `flow/prompts.py`. "Đồ họa" là phần vẽ bằng code trong `common.mjs`.

| Ch | Nền / Veo | Đồ họa và chữ trên màn hình | Người que |
|---|---|---|---|
| 00 | k1, p02, p04, k6 (cắt nhanh), tựa phim | Thẻ "79" → tựa POMPEII có vệt sáng lướt qua | Người bán hàng, thợ sơn tường |
| 01 | p01, p02, p03, k2, p04, p05, p06, p07, p08 | Bản đồ vịnh Naples: Pompeii, Herculaneum, Stabiae, Misenum, Naples, đỉnh Vesuvius; tag "~80 quầy ăn nóng", "20.000 chỗ" | Dân phố, người bán garum, thợ viết graffiti |
| 02 | k3, p09, p11, p10, p12 | Thẻ "5/2/62"; đồ thị địa chấn rung dần nhiều hơn; mặt cắt magma | Seneca (triết gia, áo choàng), thợ trát tường |
| 03 | p13, k4, k5, p14, p15 so với p14 (ghép đôi), p16, p17 | So sánh chiều cao: cột tro 33 km so với Everest 8,8 km; tag "PLINIAN"; **thẻ lịch 24/8 nhấp nháy** | Pliny Trẻ, mẹ, Pliny Già |
| 04 | p18, k6, p19, p20, k7, p21 | Bản đồ mũi tên gió đông nam + vùng tro rơi; **thước đo đá bọt** dâng dần cạnh người que (15 cm/giờ → 2,7 m); đồng hồ T+1h → T+18h | Gia đình chạy (mang túi, chìa khóa), người ở lại đóng cửa |
| 05 | p13, k8, p22, k9, p23, p24, k10, p25 | Bản đồ hành trình Misenum → bờ dưới chân núi → Stabiae; câu trích *"Vận may đứng về phía người dũng cảm"* | Pliny Già (đô đốc), người lái tàu, Rectina (chỉ là lá thư), Pomponianus |
| 06 | p26, p27, k11, p28, k12, p29, p30 | Bản đồ Herculaneum ở phía tây; tag "hàng trăm độ C", "nhanh hơn ô tô cao tốc"; thước đo **20 m** | Dân Herculaneum chờ tàu, chỉ dùng silhouette; nhà khảo cổ thập niên 1980 |
| 07 | p31, k13, p32, k14, p33, k15, p34 | Đồng hồ "7:00+"; câu trích Pliny về căn phòng tắt đèn; bản đồ tô xám 4 thành phố | Mẹ con Pliny Trẻ, đám đông silhouette |
| 08 | p35, p36, k16, p37, p38, k17, p39, p40 | Dòng thời gian 79 → 472 → 1590s → 1631 → 1738 → 1748 → 1763 | Hoàng đế Titus, người nghèo quay lại, thợ đào thế kỷ 16 và 18 |
| 09 | p41, k18, p42, p43 | Sơ đồ 3 bước: khoảng rỗng → đổ thạch cao → gỡ tro; lưới chia khu và đánh số nhà | Fiorelli (đồ thế kỷ 19, ria mép). **Tượng thạch cao vẽ thành silhouette trắng cách điệu, không vẽ chi tiết** |
| 10 | k19, p44, p45, p46 | **Lịch lật từ 24/8 sang 17/10 rồi 24/10?**; xoắn ADN; thẻ "MẸ CON?" gạch đỏ → "người đàn ông, không cùng huyết thống" | Nhà khảo cổ 2018, nhà khoa học ADN |
| 11 | p47, p48, k20, p49, k21, p50 | Thẻ "πορφύρας = MÀU TÍM"; tiền thưởng "$700.000"; tên sách "Bàn về các thói xấu – Philodemus" | Sinh viên 21 tuổi (áo hoodie, laptop), nhóm 3 người |
| 12 | p51, k22, p52, p53, p54, k23, p55, p56, k24, p57 | Bản đồ vùng đỏ 25 xã + mũi tên sơ tán "72 GIỜ"; tag "M4,7 · 31/7/2026"; "4 triệu khách/năm · trần 20.000/ngày"; tô 1/3 bản đồ chưa đào | Phi công B-25 (không quân hiệu), du khách hôm nay |
| 13 | p57 | Chữ kết | — |

**Cần thêm vào rig và common.mjs:**

- **Kit trang phục:** `toga`, `roman_civ` (tunic), `roman_admiral`, `sailor_rm`, `emperor` (vòng nguyệt quế), `worker_16c`, `worker_18c`, `archaeo_19c`, `scientist`, `student`, `usaaf`.
- **Đạo cụ:** chiến thuyền La Mã (bổ sung kiểu mới cho `ship()`), cuộn giấy cói, đèn dầu, xe kéo, vò amphora.
- **Bản đồ:** `land.json` hiện là bản đồ thế giới độ phân giải thấp, không vẽ rõ vịnh Naples. Cần xuất thêm `land_naples.json` từ Natural Earth 10m hoặc OSM coastline, khung lon 13.9–14.6, lat 40.6–40.95.

---

## 4. Âm thanh

- **Nhạc:**
  - Ch.0–2: La Mã cổ, nhẹ, sáng (lyre/harp, sáo).
  - Ch.3–7: drone trầm, căng dần, dùng tiếng tim đập ở Ch.6–7.
  - Ch.8–11: tò mò, khám phá (pizzicato, piano).
  - Ch.12–13: ấm nhưng lơ lửng.
- **Âm thanh nền (ambience) theo chương:** chợ và chim (01), gió (02), sóng cảng Misenum (03), mưa đá bọt lộp độp kèm gió (04), biển động (05), sóng đêm (06), im lặng và gió tro (07), côn trùng đồng quê (08), xẻng và bàn chải (09–10), phòng máy (11), máy bay, còi và phố hiện đại (12).
- **SFX chính:** `rumble`, `quake`, `boom_far` (lúc phun), `pumice_patter` (cần tạo mới: sỏi rơi trên ngói), `roof_crack`, `oars`, `waves`, `whoosh_heat` (dòng chảy hỏa thành vụn), `plaster_pour`, `brush`, `scanner_hum`, `bomber_prop`, `siren`.
- **Tránh:** tiếng la hét rõ; đám đông chỉ là tiếng ồn xa.

---

## 5. Shorts 9:16

Mô tả chung: *"Phần N/12 – Câu chuyện Pompeii kể bằng người que. Xem bản đầy đủ trên kênh!"* + `#pompeii #lichsu #stickman #shorts`

| P | File VI | Tiêu đề VI | File EN | Tiêu đề EN |
|---|---|---|---|---|
| 01 | POM_P01_Thanh_Pho_Duoi_Chan_Nui.mp4 | Thành phố La Mã có 80 quầy ăn nhanh #shorts | POMPEII_EN_P01_The_City_Below_The_Mountain.mp4 | The Roman city with 80 fast-food bars #shorts |
| 02 | POM_P02_Nhung_Con_Rung.mp4 | 17 năm cảnh báo mà không ai nhận ra #shorts | POMPEII_EN_P02_The_Tremors.mp4 | 17 years of warnings nobody understood #shorts |
| 03 | POM_P03_Dam_May_Hinh_Cay_Thong.mp4 | Cậu bé 17 tuổi chứng kiến "ngày tận thế" #shorts | POMPEII_EN_P03_The_Pine_Tree_Cloud.mp4 | A 17-year-old watched the sky explode #shorts |
| 04 | POM_P04_Troi_Toi_Giua_Ban_Ngay.mp4 | Mưa đá bọt suốt 17 tiếng: chạy hay ở lại? #shorts | POMPEII_EN_P04_Darkness_At_Noon.mp4 | 17 hours of falling stone: run or stay? #shorts |
| 05 | POM_P05_Chuyen_Tau_Cua_Do_Doc.mp4 | Đô đốc La Mã lao vào núi lửa để cứu người #shorts | POMPEII_EN_P05_The_Admirals_Voyage.mp4 | The admiral who sailed toward a volcano #shorts |
| 06 | POM_P06_Nua_Dem_O_Herculaneum.mp4 | Hơn 300 người chờ tàu cứu trên bãi biển #shorts | POMPEII_EN_P06_Midnight_At_Herculaneum.mp4 | 300 people waiting for a rescue ship #shorts |
| 07 | POM_P07_Buoi_Sang_Cuoi_Cung.mp4 | Pompeii biến mất chỉ trong vài phút #shorts | POMPEII_EN_P07_The_Last_Morning.mp4 | Pompeii's last morning #shorts |
| 08 | POM_P08_Thanh_Pho_Bi_Lang_Quen.mp4 | Đào kênh xuyên qua Pompeii mà không ai biết #shorts | POMPEII_EN_P08_The_Forgotten_City.mp4 | They dug right through Pompeii and didn't notice #shorts |
| 09 | POM_P09_Nhung_Khoang_Trong_Trong_Tro.mp4 | Đổ thạch cao vào khoảng rỗng… và thấy con người #shorts | POMPEII_EN_P09_The_Holes_In_The_Ash.mp4 | The holes in the ash #shorts |
| 10 | POM_P10_Nhung_Bi_Mat_Moi.mp4 | Sách sử có thể đã ghi sai ngày Pompeii bị hủy diệt #shorts | POMPEII_EN_P10_New_Secrets.mp4 | Did history get Pompeii's date wrong? #shorts |
| 11 | POM_P11_Thu_Vien_Hoa_Than.mp4 | AI đọc cuộn giấy bị núi lửa thiêu 2.000 năm #shorts | POMPEII_EN_P11_The_Charred_Library.mp4 | AI read a scroll burned 2,000 years ago #shorts |
| 12 | POM_P12_Nui_Lua_Van_Thuc.mp4 | 700.000 người đang sống dưới chân Vesuvius #shorts | POMPEII_EN_P12_The_Volcano_Is_Still_Awake.mp4 | 700,000 people live under Vesuvius #shorts |

---

## 6. YouTube: phim 16:9 (bản nháp `phim_16x9/YT_POMPEII.md`)

**Tiêu đề (chọn 1)**

1. POMPEII: 32 giờ cuối cùng (hoạt hình người que)
2. Chuyện gì thật sự đã xảy ra ở Pompeii? – kể bằng người que
3. Thành phố bị núi lửa chôn vùi suốt 1.700 năm – Pompeii

**Mô tả**

> Năm 79, núi lửa Vesuvius thức dậy sau nhiều thế kỷ ngủ yên. Trong khoảng 32 giờ, Pompeii, Herculaneum, Stabiae và Oplontis biến mất dưới tro và đá. Qua 12 chương: thành phố cảng có "nước mắm La Mã", 17 năm động đất cảnh báo, đám mây hình cây thông mà cậu bé Pliny 17 tuổi chứng kiến, cơn mưa đá bọt suốt 17 tiếng, chuyến cứu nạn của đô đốc Pliny Già, đêm cuối ở Herculaneum, buổi sáng cuối cùng, 1.700 năm bị lãng quên, những tượng thạch cao của Fiorelli, bí ẩn ngày phun trào và ADN, thư viện hóa than được AI giải mã – và núi lửa vẫn đang thức.
>
> ⚠️ Video dùng hình người que và minh họa AI để kể lại sự kiện lịch sử; nhân vật có thật chỉ được thể hiện bằng người que kèm tên. Video không tái hiện hình ảnh thương vong. Ngày phun trào (24/8 hay khoảng cuối tháng 10 năm 79) vẫn đang được tranh luận.

**Chương:** điền mốc giờ sau khi dựng (Mở đầu, 12 chương, Lời kết).

**Hashtag:** `#pompeii #lichsu #thamhoa #nuilua #stickman #hoathinh`

**Tags:** Pompeii, núi lửa Vesuvius, Herculaneum, Pliny, Pliny Già, Pliny Trẻ, La Mã cổ đại, phun trào năm 79, tượng thạch cao Pompeii, Fiorelli, Vesuvius Challenge, cuộn giấy Herculaneum, Campi Flegrei, thảm họa núi lửa, lịch sử thế giới, stickman, hoạt hình lịch sử

**Bình luận ghim:** Nếu bạn ở Pompeii hôm đó, khi trời bắt đầu mưa đá bọt – bạn sẽ chạy hay ở lại? 👇 Và tập sau muốn xem gì: Điện Biên Phủ, Apollo 13 hay Cúm Tây Ban Nha 1918?

**Ghi chú (đưa vào mô tả)**

- Dân số Pompeii được ước tính rất khác nhau (từ khoảng 10.000 đến hơn 20.000). Công viên khảo cổ ước tính khoảng 15–20% cư dân thiệt mạng.
- Thời lượng 32 giờ và mốc "ngay sau 7 giờ sáng ngày thứ hai" theo nghiên cứu Scarpati và cộng sự (2025). Các nghiên cứu trước ước tính khoảng 18–19 giờ.
- Nhiệt độ dòng chảy hỏa thành vụn khác nhau theo nơi và theo đợt. Video dùng cách nói "hàng trăm độ".
- Số máy bay bị phá hủy năm 1944 dao động 78–88 tùy nguồn.
- Dân số vùng đỏ Vesuvius: Bảo vệ Dân sự Ý dùng con số khoảng 700.000. Một số nguồn tính cả một phần Naples nên ghi khoảng 800.000.

---

## 7. Bản EN

- Dịch lời dẫn sang tiếng Anh theo từng câu. Giữ nguyên cấu trúc `chNN/script.json`, giữ id cảnh `cNN_k` để dùng lại `scenes.mjs` và timeline.
- Tựa chương EN lấy từ bảng mục 2.
- Câu trích nên lấy bản dịch Anh quen thuộc: *"Fortune favours the brave"*; *"…like the black of closed and unlighted rooms"*.
- Thư mục `EN/film_16x9/POMPEII_Film_16x9.mp4`, `EN/shorts_9x16/…`, `YT_POMPEII_EN.md`.

---

## 8. Nội dung nhạy cảm và độ chính xác

- **Không vẽ thi thể.** Tượng thạch cao, hài cốt Herculaneum và nạn nhân dưới tro chỉ thể hiện bằng silhouette trắng hoặc xám rất cách điệu, hoặc bằng khung trống, giống cách xử lý ở Titanic và Chernobyl. Mọi prompt nền và Veo đã có ràng buộc `NO bodies, NO skeletons`.
- **Não hóa thủy tinh (Ch.6):** chỉ nói bằng lời. Hình ảnh dùng một mảnh kính đen trên nền trống, không vẽ đầu hay sọ.
- **Ch.10, câu chuyện ADN:** kể trung tính, nhấn vào chỗ "câu chuyện ta tự gán cho tượng có thể sai", không suy diễn quan hệ.
- **Người thật:** Pliny Già, Pliny Trẻ, Seneca, Titus, Fiorelli và sinh viên Vesuvius Challenge chỉ là người que kèm tên. Không ghi tên sinh viên trên màn hình (lời dẫn cũng không nêu tên).
- **Máy bay 1943–44:** không vẽ quân hiệu.
- **Những điểm cần kiểm tra lại trước khi thu âm:**
  1. Ch.1: "khoảng 80 quầy" (số liệu thường dẫn, có nguồn ghi 80–150).
  2. Ch.2: đàn 600 con cừu theo Seneca, *Naturales Quaestiones*, quyển 6.
  3. Ch.11: tình trạng mới nhất của PHerc. 172 (Diamond Light Source, 6/2026).

---

## 9. Nguồn

- Pliny the Younger, *Epistulae* 6.16 và 6.20 (thư gửi Tacitus) – [bản dịch York University](https://www.yorku.ca/pswarney/2100/pliny-6-16-20.htm)
- Scarpati và cộng sự (2025), *Journal of the Geological Society* 182(1): mốc 32 giờ, 17 đợt dòng chảy hỏa thành vụn – [DiSTAR Napoli](https://www.distar.unina.it/en/news/a-minute-by-minute-account-of-the-pompeii-eruption-revealed-in-agonizing-detail)
- Tranh luận về ngày phun trào – [Getty](https://www.getty.edu/news/when-did-vesuvius-erupt-august-october-24/), [National Geographic (1/2026)](https://www.nationalgeographic.com/history/article/mount-vesuvius-eruption-pompeii), [Archaeology (2018)](https://archaeology.org/news/2018/10/16/181016-pompeii-date-inscription/)
- Trận động đất năm 62 – [UVA IATH](https://www2.iath.virginia.edu/struct/pompeii/patterns/sec-02.html)
- Herculaneum, hầm thuyền và hơn 300 bộ hài cốt – [Parco Archeologico di Ercolano](https://ercolano.cultura.gov.it/i-fuggiaschi/?lang=en), [NPR 2024](https://www.npr.org/2024/06/22/nx-s1-5015177/herculaneum-beach-mount-vesuvius-opens-restoration)
- Não hóa thủy tinh, Giordano và cộng sự, *Scientific Reports* (2/2025) – [Science News](https://www.sciencenews.org/article/mount-vesuvius-ancient-brain-glass)
- Lịch sử khai quật (Fontana, 1738, 1748, 1763, Fiorelli) – [Britannica](https://www.britannica.com/place/Pompeii/History-of-excavations), [Smarthistory](https://smarthistory.org/the-rediscovery-of-pompeii-and-the-other-cities-of-vesuvius)
- Người sống sót quay lại Pompeii (8/2025) – [Archaeology](https://archaeology.org/news/2025/08/08/some-of-pompeiis-residents-returned-home/)
- ADN tượng thạch cao (*Current Biology*, 11/2024) – [Max Planck](https://www.mpg.de/23699890/dna-evidence-rewrites-pompeii-eruption-story), [Harvard Medical School](https://hms.harvard.edu/news/ancient-dna-challenges-stories-told-about-pompeii-victims)
- Quầy đồ ăn nóng Regio V – [Archaeology (2020)](https://archaeology.org/news/2020/12/28/201229-pompeii-snack-bar/)
- Cuộn giấy Herculaneum – [University of Kentucky (10/2023)](https://research.uky.edu/news/grand-prize-discovery-made-2000-year-old-herculaneum-scrolls), [UK (2/2024)](https://uknow.uky.edu/research/grand-prize-discovery-made-2000-year-old-herculaneum-scrolls), [Smithsonian (5/2025)](https://www.smithsonianmag.com/smart-news/these-ancient-scrolls-have-been-a-tantalizing-mystery-for-2000-years-researchers-just-deciphered-a-title-for-the-first-time-180986639/), [Diamond Light Source (6/2026)](https://www.diamond.ac.uk/Home/News/LatestNews/2026/New-secrets-revealed-from-the-Herculaneum-scrolls.html)
- Bom Đồng minh năm 1943 – [Open Culture / Pollard, *Bombing Pompeii*](https://www.openculture.com/2021/10/the-bombing-of-pompeii-during-world-war-ii.html)
- Phun trào năm 1944 và nhóm B-25 thuộc 340th Bomb Group – [alcpress 489th BS](https://alcpress.org/kaiser/489thbs/vesuvius/index.html)
- Vùng đỏ Vesuvius, 25 xã, sơ tán 72 giờ – [Protezione Civile](https://www.protezionecivile.gov.it/en/approfondimento/are-you-prepared-volcanic-risk-vesuvius/)
- Campi Flegrei: M4,4 ngày 21/5/2026 và M4,7 ngày 31/7/2026 – [Protezione Civile](https://rischi.protezionecivile.gov.it/en/volcanic/volcanoes-italy/phlegraen-fields/bradyseism-phlegraean-fields/), [INGV](https://terremoti.ingv.it/en/event/46725592)
- Lượng khách và trần 20.000 người mỗi ngày – [The Art Newspaper (6/2025)](https://www.theartnewspaper.com/2025/06/05/pompeii-tour-guides-decry-lengthy-queues-as-visitor-numbers-soar)

---

## 10. Checklist pipeline

Cùng quy trình với `10-the-chien-2`.

1. [ ] Duyệt lời dẫn (`script_src.py`), chạy `python3 script_src.py` → `chNN/script.json`, `chapters.json`
2. [ ] `python3 flow/prompts.py` → `all.json`, `setbg.js`, `veo.json` → tạo nền trên Flow (`flow_refs/bg`) và clip Veo (`flow_refs/veo/k1..k24.mp4`)
3. [ ] Thu giọng (`voice_vi.py`) → `chNN/timeline.json` (whisper word timing). Nghe thử phần phiên âm trong `NAMES`.
4. [ ] Bổ sung kit/đạo cụ (`rig.mjs`, `gear.mjs`) và `land_naples.json`
5. [ ] Viết `chNN/scenes.mjs` theo bảng mục 3 → `render.mjs`
6. [ ] `sfxw.py` / `mixw.py` (thêm `pumice_patter`, `whoosh_heat`, `plaster_pour`) → `assemble.py` → `phim_16x9/POMPEII_Phim_16x9.mp4` + `.srt`
7. [ ] Cắt 12 shorts 9:16 → `shorts_9x16/`
8. [ ] Dịch EN → dựng `EN/film_16x9` + `EN/shorts_9x16`
9. [ ] `yt_meta.py` → `YT_POMPEII.md`, `YT_shorts.md` (+ EN), điền mốc chương
10. [ ] QC: xem toàn bộ ở tốc độ thật có tiếng; kiểm số liệu với mục 8; không có hình thi thể
