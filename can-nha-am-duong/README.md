# Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít — Phim Ma Kể Chuyện Điện Ảnh (15 Cảnh × 6 Clips × 10s = 90 Clips / 15 Phút | Google Flow Omni 10s)

![Poster Key Art — Căn Nhà Âm Dương](scene_refs/04_poster_key_art.jpg)

Dự án **Phim Ma Kể Chuyện Điện Ảnh 15 Phút** (**15 Cảnh × 6 Clips × 10 giây = 90 Clips = 900 giây / 15 phút**, tỉ lệ **16:9 Cinema 24fps**, model **`omni_flash` 10s**) lấy cảm hứng từ truyện ma **"Căn Nhà Âm Dương"** (Tác giả Thu Thảo — Kênh **HẺM Truyện Ma**, giọng kể **MC Đình Soạn**):
- **Quy Định Giọng Người Dẫn Chuyện (`VOICE_LOCK_NARRATOR_CNHADG` — 80% thời lượng / 72 Clips):** Cố định 100% giọng Nam trung niên 42 tuổi chuẩn Hà Nội - miền Bắc (`~110 Hz` mid-baritone trầm ấm, thanh thoát, nhấn nhá rùng rợn lúc đêm khuya chuẩn phong cách **MC Đình Soạn — HẺM Truyện Ma**, tốc độ `0.95x`, nhân vật trên màn hình khép miệng tự nhiên suốt đoạn VO).
- **Khóa Danh Tính & Giọng Nói Từng Nhân Vật (`CHARACTER_LOCK` + `VOICE_LOCK` — 20% On-screen Lip-Sync / 18 Clips):** Kết nối cứng `media_id` trên Google Flow Project `3b955883-7851-42fe-a986-5ef82b4912e5` cùng hồ sơ âm sắc giọng Bắc riêng biệt cho cả 6 nhân vật (`@Binh`, `@BaPhuong`, `@OngQuan`, `@OngBay`, `@VongCuXa`, `@VongLa`).
- **Thiết Kế Chuyển Cảnh Mượt (`3-Beat Match-On-Action Continuity`):** Mỗi clip 10s chia làm 3 nhịp liên hoàn (`Beat 1: 0.0–3.0s` khớp nối trực tiếp từ `END FRAME` của clip trước → `Beat 2: 3.0–7.0s` diễn biến chính → `Beat 3: 7.0–10.0s` tạo điểm neo dẫn mượt sang `START FRAME` của clip kế tiếp).
- **Danh mục 90 files kịch bản chi tiết:** [`canh-01/clip-1.md`](canh-01/clip-1.md) → [`canh-15/clip-6.md`](canh-15/clip-6.md) và tổng hợp tại [`FLOW_PROMPTS.md`](FLOW_PROMPTS.md).

---

## PHẦN 1: QUY ĐỊNH GIỌNG NGƯỜI DẪN CHUYỆN & KHÓA 6 NHÂN VẬT (`VOICE_LOCK` & `CHARACTER_SPECS`)

### 1. Quy Định Cố Định Giọng Người Dẫn Chuyện (`VOICE_LOCK_NARRATOR_CNHADG`)
- **Mã khóa giọng:** `VOICE_LOCK_NARRATOR_CNHADG`
- **Hình mẫu & Phong cách:** **MC Đình Soạn — HẺM Truyện Ma** (Giọng nam 42 tuổi chuẩn Hà Nội - miền Bắc, âm vực trung trầm `~110 Hz`, thanh thoát, trầm ấm nhưng sắc lạnh ở những đoạn cao trào tâm linh).
- **Tốc độ & Nhịp điệu:** `0.95x` (`~135 từ/phút`), ngắt nghỉ `0.4s` ở dấu ba chấm (`…`), tuyệt đối không dùng giọng miền Nam/miền Trung, không dùng giọng đọc máy công nghiệp.
- **Quy tắc hình ảnh khi đọc VO:** Toàn bộ nhân vật trên hình giữ miệng khép tự nhiên (`mouths remain naturally closed 0.0–10.0s`), chỉ diễn xuất bằng ánh mắt, hơi thở và cử chỉ cơ thể.

### 2. Bảng Khóa 6 Nhân Vật & Giọng Thoại Riêng (`CHARACTER_SPECS`)

| Tag | Nhân Vật | Google Flow `media_id` | Mô Tả Tạo Hình Cố Định (16:9) | Hồ Sơ Giọng Thoại (`VOICE_LOCK`) |
|---|---|---|---|---|
| **`@Binh`** | **Nguyễn Hòa Bình** (21t) | `a1a78643-ce72-4217-86c7-b53b927e637a` | Nam sinh viên năm cuối, cao 1m72, gầy nhợt nhạt, mắt thâm quầng, mặc áo hoodie xám bạc ngoài áo thun trắng, đeo ba lô đen. | `VOICE_LOCK_BINH_CNHADG`: Nam trẻ 21t chuẩn Bắc (`~135 Hz`), run rẩy, nghẹn ngào. |
| **`@BaPhuong`** | **Bà Phượng** (50t) | `a17f2e3b-8272-4cff-8de0-1c3ec43a11b1` | Mẹ Bình, giáo viên về hưu, tóc búi thấp điểm bạc, mặt trái xoan nhân hậu phiền muộn, mặc áo sơ mi xanh nhạt. | `VOICE_LOCK_PHUONG_CNHADG`: Nữ trung niên 50t chuẩn Bắc (`~205 Hz`), ấm áp, lo âu. |
| **`@OngQuan`** | **Ông Quân** (55t) | `e845a88f-7cd2-4b8f-9fa3-e75e7e337674` | Bố Bình, nhân viên văn phòng, dáng chắc, tóc húi cua điểm bạc, mặt nghiêm nghị, áo sơ mi trắng xắn tay. | `VOICE_LOCK_QUAN_CNHADG`: Nam trung niên 55t chuẩn Bắc (`~105 Hz`), trầm đanh, uy nghiêm. |
| **`@OngBay`** | **Ông Bảy** (60t) | `10e5cdcf-3dd1-4b41-b999-21922b65de89` | Nông dân hàng xóm tốt bụng, da ngăm phong sương, tóc bạc, áo sơ mi kẻ nâu cũ, đi dép cao su, dắt xe đạp cổ. | `VOICE_LOCK_BAY_CNHADG`: Nam cao niên 60t chuẩn Bắc (`~115 Hz`), mộc mạc, ấm áp. |
| **`@VongCuXa`** | **Vong Cụ Xá** (80t) | `f8d1ff26-6134-4fa4-8c0f-13e8405e5f64` | Vong hồn ông nội Bình, gầy gò bán trong suốt dưới ánh trăng lạnh, râu tóc bạc trắng, mặc áo bà ba nâu sồng. | `VOICE_LOCK_CUXA_CNHADG`: Cụ già 80t chuẩn Bắc (`~98 Hz`), khàn đục, vọng âm. |
| **`@VongLa`** | **Vong Gốc Mít** (28t) | `0c2ade1f-c1cd-4c93-98e2-697231a54887` | Vong hồn vụ tai nạn xe rước dâu, da xám ngoét, hốc mắt đen ngòm, năm ngón tay móng dài đen kịt. | `VOICE_LOCK_VONGLA_CNHADG`: Giọng ma vọng lạnh lẽo chuẩn Bắc từ bốn phía. |

---

## PHẦN 2: KỊCH BẢN CHI TIẾT 15 CẢNH — 15 PHÚT (90 CLIPS × 10 GIÂY)

#### **Cảnh 01 (`00:00–01:00` | 6 Clips × 10s): Chuyến Xe Khách Đêm Khuya & Món Nợ Bốn Trăm Triệu**
- **Clip 1 (`00:00–00:10` — VO | On-screen: `@Binh`):** Toàn cảnh flycam chậm lướt qua cánh đồng lúa Bắc Bộ tối mịt mù trong sương đêm, tiến sát vào ô cửa kính đọng mưa của chiếc xe khách giường nằm nơi `@Binh` đang ngồi co ro.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Người ta vẫn thường bảo… trần gian có những bước đường cùng mà con người ta thà đối mặt với ma quỷ, còn hơn phải nhìn mặt người sống. Và chỉ vì một khoản nợ hơn bốn trăm triệu đồng… Bình đã phải bỏ lại tất cả, trốn về căn nhà cũ bỏ hoang gần hai mươi năm của ông nội."
- **Clip 2 (`00:10–00:20` — VO | On-screen: `@Binh`):** Nối tiếp từ khung cửa kính đọng nước mưa, máy quay lướt vào khoang ghế tối: `@Binh` ôm chặt chiếc ba lô đen trước ngực, ánh đèn đường vàng vọt quét qua gương mặt tái nhợt hốc hác.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Thế nhưng Bình đâu hề biết rằng… sau cái đêm tai nạn thảm khốc cướp đi sáu mạng người ngay trước cổng mười ba năm về trước, căn nhà hoang ấy đã trở thành chốn dung thân của những oan hồn không nơi nương tựa."
- **Clip 3 (`00:20–00:30` — Lip-Sync `@Binh` | On-screen: `@Binh`):** Đang ôm ba lô nhìn ra cửa kính, chiếc điện thoại trong túi áo hoodie của `@Binh` rung bần bật. `@Binh` giật mình rút máy ra, lấy tay che miệng áp sát điện thoại vào tai thì thầm.
  - *Thoại (@Binh):* "Con nghe đây mẹ ơi… Con đang trên xe khách về quê nội rồi, mẹ đừng gọi nhiều nhỡ người ta nghe thấy."
- **Clip 4 (`00:30–00:40` — Lip-Sync `@BaPhuong` | On-screen: `@BaPhuong`):** Ở đầu dây bên kia cuộc gọi, `@BaPhuong` đứng dưới ánh đèn vàng yếu ớt nơi góc bếp, một tay áp chặt điện thoại vào tai, một tay bấu vào mép bàn gỗ, nước mắt lưng tròng.
  - *Thoại (@BaPhuong):* "Bố mày chưa biết chuyện đâu… Nhưng đám chủ nợ đằng nào chả tìm tới nhà! Mày về dưới quê ông nội thì phải cẩn thận đấy con ơi!"
- **Clip 5 (`00:40–00:50` — VO | On-screen: `@Binh`):** Trở lại ghế xe khách tối tăm, `@Binh` hạ điện thoại xuống nhìn màn hình sáng xanh hiện bức ảnh chụp tài khoản tiền ảo cháy đỏ rực, hai bàn tay cậu run rẩy ôm lấy đầu.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Tất cả cũng chỉ bắt đầu từ cái bẫy đầu tư tiền ảo trên mạng… Ban đầu thấy kiếm được vài đồng bạc lẻ, lòng tham cứ thế cuốn lấy tâm trí, để rồi khi sàn sập… số nợ lãi mẹ đẻ lãi con đã vọt lên hơn bốn trăm triệu đồng."
- **Clip 6 (`00:50–01:00` — VO | On-screen: `@Binh`):** `@Binh` tắt màn hình điện thoại, tựa trán vào mặt kính xe khách lạnh buốt nhìn bóng phản chiếu tuyệt vọng của chính mình khi chiếc xe lao sâu vào màn sương trắng vùng quê.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Không còn mặt mũi nào nhìn bố, cũng chẳng còn chốn dung thân nơi phố thị… Bình đành đánh liều tìm về căn nhà cổ của ông nội, mà không ngờ mình đang tự bước chân vào cõi âm dương giao hòa."

---

#### **Cảnh 02 (`01:00–02:00` | 6 Clips × 10s): Bến Xe Thị Xã, Quán Cơm Bụi & Cánh Cổng Sắt Dưới Gốc Mít Cổ Thụ**
- **Clip 1 (`01:00–01:10` — VO | On-screen: `@Binh`):** Từ màn sương trên quốc lộ chuyển sang nắng quái chiều tà: chiếc xe khách vừa rời đi bên lề đường thị xã, `@Binh` khoác ba lô đen bước xuống giữa làn bụi mù, thở phào ngước nhìn quanh.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Kim đồng hồ chỉ hơn hai giờ chiều khi chiếc xe khách thả Bình xuống một bến xe thị xã nhỏ. Giữa nơi đất khách quê người không một ai quen biết, lần đầu tiên sau nhiều tuần lễ, cậu mới dám thở phào một hơi nhẹ nhõm."
- **Clip 2 (`01:10–01:20` — VO | On-screen: `@Binh`):** `@Binh` bước vào ngồi một mình bên chiếc bàn nhựa thấp ở quán cơm bụi ngay đầu đường làng, mắt nhìn tin nhắn mẹ vừa chuyển năm trăm nghìn cuối cùng bên cạnh đĩa cơm nguội.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Ngồi bên quán cơm bụi ven đường, nghe tiếng mẹ nghẹn ngào dặn dò qua điện thoại rằng vừa gom góp chuyển nốt cho cậu năm trăm nghìn cuối cùng… sống mũi Bình cay xè, miếng cơm nghẹn đắng nơi cổ họng."
- **Clip 3 (`01:20–01:30` — VO | On-screen: `@Binh`):** `@Binh` cất điện thoại vào túi áo hoodie, đôi mắt đỏ hoe nhìn xuống đôi bàn tay gầy guộc đang run lên, rồi lặng lẽ đứng dậy khoác ba lô bước dọc theo con đường bê tông về làng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Cậu tự hứa với lòng mình sẽ ẩn náu ở quê nội một thời gian cho qua cơn sóng gió… nhưng khi hỏi thăm đường về nhà cụ Xá, sắc mặt người dân trong vùng bỗng nhiên biến đổi hẳn."
- **Clip 4 (`01:30–01:40` — VO | On-screen: `@Binh`):** `@Binh` lầm lũi bước đi trên con đường bê tông hẹp giữa hai cánh đồng lúa chiều muộn, gió thổi hun hút làm những rặng tre già đầu làng nghiêng ngả phát ra tiếng kẽo kẹt.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Con đường dẫn vào thôn quê cứ hẹp dần giữa hai cánh đồng lúa chiều vắng lặng, rợp bóng tre già âm u và lạnh lẽo đến rợn người."
- **Clip 5 (`01:40–01:50` — Lip-Sync `@OngBay` | On-screen: `@Binh, @OngBay`):** Bắt gặp `@OngBay` đang vác cuốc đứng bên lề đường đầu xóm, `@Binh` dừng lại hỏi thăm. `@OngBay` chỉ tay về phía ngọn cây mít cổ thụ cuối xóm, đôi mắt nheo lại nhìn `@Binh` đầy vẻ cảnh giác.
  - *Thoại (@OngBay):* "Căn nhà cuối xóm có gốc mít cổ thụ ấy bỏ hoang gần hai mươi năm nay rồi cậu ơi… Mà tôi nói thật nhé, nhà ấy nặng âm khí, có ma đấy!"
- **Clip 6 (`01:50–02:00` — VO | On-screen: `@Binh`):** Theo hướng tay chỉ, `@Binh` bước tới đứng sững trước cánh cổng sắt sơn đen đã bong tróc rỉ sét. Bên trong sân cỏ dại mọc lút đầu gối, gốc mít cổ thụ xù xì che rợp mái ngói ba gian u tối.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đứng trước cánh cổng sắt sơn đen bong tróc và gốc mít cổ thụ vặn vẹo như những cánh tay khô héo vươn lên trời chiều… một luồng khí lạnh từ trong ngôi nhà hoang phả thẳng vào mặt khiến Bình bất giác rùng mình."

---

#### **Cảnh 03 (`02:00–03:00` | 6 Clips × 10s): Ông Bảy Hàng Xóm & Lời Kể Rợn Tóc Gáy Về Vụ Lật Xe Lúc Ba Giờ Sáng**
- **Clip 1 (`02:00–02:10` — Lip-Sync `@OngBay` | On-screen: `@Binh, @OngBay`):** `@Binh` đang đứng tần ngần nắm chấn song cổng sắt rỉ sét thì `@OngBay` dắt chiếc xe đạp Phượng Hoàng cũ dừng kịt lại ngay phía sau, ánh mắt sắc lạnh nhìn dò xét.
  - *Thoại (@OngBay):* "Này cậu thanh niên kia, đứng rình mò gì trước cổng nhà người ta thế hả? Làng này vừa bắt được mấy đứa trộm cắp đấy nhé!"
- **Clip 2 (`02:10–02:20` — Lip-Sync `@Binh` | On-screen: `@Binh, @OngBay`):** `@Binh` buông tay khỏi cổng sắt, vội vàng quay lại cúi đầu lễ phép giải thích với `@OngBay`. Ông Bảy nghe xong liền giãn cơ mặt, bước tới vỗ ấm áp lên vai cậu.
  - *Thoại (@Binh):* "Dạ cháu không phải kẻ gian đâu bác ơi… Cháu là Bình, cháu nội cụ Xá, con trai bố Quân trên thành phố về thăm nhà ạ!"
- **Clip 3 (`02:20–02:30` — VO | On-screen: `@Binh, @OngBay`):** `@OngBay` niềm nở dắt xe đạp đi sóng đôi cùng `@Binh` rời khỏi cổng sắt rỉ sét, hướng về ngôi nhà ngói ba gian giản dị của ông ở ngay đầu ngõ khi bóng chiều sập tối.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Nhận ra đứa cháu nội của ông cụ hàng xóm quá cố, ông Bảy mừng rỡ dẫn Bình về nhà mình nghỉ tạm qua đêm, bởi ngôi nhà hoang bụi bặm kia đâu thể dọn dẹp xong trong một buổi chiều tà."
- **Clip 4 (`02:30–02:40` — VO | On-screen: `@Binh, @OngBay`):** Bên hiên nhà ngói ấm ánh đèn vàng, trong khi `@Binh` ngồi uống chén nước chè xanh bốc khói, `@OngBay` đứng ở góc hiên lắng nghe vợ thì thầm với gương mặt trầm ngâm lo lắng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Thế nhưng vừa nghe chồng bảo ngày mai sẽ cho thằng nhỏ dọn sang căn nhà hoang ấy ở… vợ ông Bảy đã tái mặt kéo chồng ra góc hiên, giọng thì thầm đầy kinh hãi."
- **Clip 5 (`02:40–02:50` — VO | On-screen: `@OngBay`):** Từ hiên nhà, `@OngBay` trầm ngâm nhìn xuyên qua màn sương mù dày đặc hướng về khúc cua quốc lộ ngay trước cổng sắt và gốc mít nhà cụ Xá chìm trong bóng tối lạnh ngắt.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Bà nhắc lại rằng mười ba năm về trước, đúng vào khung giờ Dần ba giờ sáng… một chiếc xe mười sáu chỗ đi rước dâu qua khúc cua trước cổng nhà cụ Xá đã bất ngờ mất lái, lật nhào bốn năm vòng làm sáu mạng người chết thảm ngay tại chỗ."
- **Clip 6 (`02:50–03:00` — VO | On-screen: `@VongLa`):** Máy quay đẩy chậm từ khúc cua sương mù tới dưới gốc mít cổ thụ trước cổng sắt: bóng `@VongLa` cao gầy ướt đẫm sương đêm đang đứng lờ mờ sau rặng cỏ dại nhìn chằm chằm vào căn nhà hoang.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Thầy cao tay trong vùng bảo những vong hồn chết bất đắc kỳ tử ấy không tìm được đường về, thấy ngôi nhà cụ Xá bỏ không bèn kéo cả vào trong đó trú ngụ… Từ đấy về sau, đêm nào người đi làm đồng về khuya cũng thấy bóng trắng lượn lờ dưới gốc mít."

---

#### **Cảnh 04 (`03:00–04:00` | 6 Clips × 10s): Phá Khóa Dọn Nhà Hoang & Cuộc Gọi Tuyệt Vọng Từ Mẹ**
- **Clip 1 (`03:00–03:10` — VO | On-screen: `@Binh`):** Sương đêm dưới gốc mít tan dần dưới ánh nắng ban mai: `@Binh` vác chổi tre bước tới trước cánh cổng sắt rỉ sét của căn nhà hoang, lắng nghe tiếng gà gáy sáng vang vọng khắp xóm làng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Tiếng gà gáy sáng vang lên đánh thức Bình sau một đêm ngủ say hiếm hoi. Giữa cái nắng sớm trong trẻo của vùng quê Bắc Bộ, những lời đồn thổi ma quỷ tối hôm qua dường như cũng tan biến theo làn sương sớm."
- **Clip 2 (`03:10–03:20` — VO | On-screen: `@Binh, @OngBay`):** Ngay trước cổng sắt, `@OngBay` dùng cán cuốc chim luồn vào ổ khóa sắt rỉ sét bên cạnh `@Binh`, bẩy mạnh một cái làm ổ khóa gãy 'RẮC!' rơi xuống nền gạch rêu phong.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Sáng hôm ấy, bác Bảy vác cuốc sang phụ Bình mở cổng dọn nhà. Chỉ một cú bẩy mạnh bằng cán cuốc gỗ, chiếc ổ khóa sắt rỉ sét khóa chặt suốt gần hai mươi năm đã gãy tung, mở toang cánh cổng bước vào thế giới bụi mờ."
- **Clip 3 (`03:20–03:30` — VO | On-screen: `@Binh`):** Cánh cổng sắt mở rộng, `@Binh` cầm chổi tre quét dọn lớp lá mít mục nát và cỏ dại um tùm ngoài sân gạch, từng đám bụi mù và mạng nhện chằng chịt được gỡ xuống khỏi hiên nhà ngói.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Suốt ba tiếng đồng hồ phát cỏ và quét mạng nhện, khoảng sân gạch rêu phong dưới gốc mít cổ thụ mới dần lộ ra ánh sáng. Nhưng khi bước chân vào bên trong gian nhà chính… một mùi ẩm mốc lạnh lẽo vẫn đặc quánh trong không khí."
- **Clip 4 (`03:30–03:40` — VO | On-screen: `@Binh`):** Từ hiên nhà, `@Binh` bước qua ngưỡng cửa gỗ vào đứng một mình giữa gian phòng khách trống huơ trống hoắc, từng luồng nắng xiên chiếu qua khe ngói làm lộ rõ lớp bụi bay lơ lửng quanh tường vôi bong tróc.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Nhìn gian nhà trống huơ không một nén hương sưởi ấm, lòng Bình chợt chùng xuống… Nhưng cậu tự nhủ, thôi thì coi như đây là sự trừng phạt cho những sai lầm tuổi trẻ của mình."
- **Clip 5 (`03:40–03:50` — Lip-Sync `@BaPhuong` | On-screen: `@BaPhuong`):** Điện thoại reo vang chói tai phá tan sự tĩnh lặng. Ở đầu dây bên kia, `@BaPhuong` đứng nép trong góc phòng tối trên thành phố, hai tay giữ chặt điện thoại khóc nức nở trong sự hoảng loạn tột độ.
  - *Thoại (@BaPhuong):* "Bình ơi! Bố mày biết hết chuyện nợ nần rồi con ơi! Ông ấy đang điên tiết lùng sục khắp nơi tìm mày đấy, mày khóa máy ngay đi đừng về lúc này!"
- **Clip 6 (`03:50–04:00` — VO | On-screen: `@Binh`):** Nghe tiếng mẹ tắt phụt, `@Binh` buông thõng bàn tay cầm điện thoại, trượt dài lưng theo bức tường vôi ẩm mốc của gian nhà hoang rồi ngồi bệt xuống nền gạch lạnh toát, hai tay ôm đầu tuyệt vọng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Cuộc gọi tắt phụt như cắt đứt sợi dây cứu sinh cuối cùng… Bình ngồi gục xuống nền gạch lạnh ngắt, nhận ra từ giây phút này, cậu thực sự chỉ còn trơ trọi một mình trong căn nhà mà cả làng gọi là nhà ma."

---

#### **Cảnh 05 (`04:00–05:00` | 6 Clips × 10s): Đêm Đầu Tiên Một Mình & Vết Bầm Năm Ngón Tay Lúc Rạng Sáng**
- **Clip 1 (`04:00–04:10` — VO | On-screen: `@Binh`):** Từ nền gạch lạnh lẽo ban ngày chuyển sang màn đêm tĩnh mịch: dưới ánh đèn dây tóc 15W vàng vọt tù mù, `@Binh` nằm co ro trên chiếc giường xếp cũ cót két, bên ngoài giăng tấm màn tuyn trắng mỏng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đêm đầu tiên ngủ lại một mình… ngoài sân chỉ có tiếng ếch nhái kêu râm ran và tiếng gió đêm lùa qua kẽ ngói. Dưới ánh đèn dây tóc vàng vọt như đom đóm, Bình kéo chăn ngang ngực, tự trấn an rằng đây là nhà của ông nội mình."
- **Clip 2 (`04:10–04:20` — VO | On-screen: `@Binh, @VongLa`):** Góc máy từ trên trần nhà tối đen hạ thấp xuống chiếc màn trắng nơi `@Binh` đang thiu thiu ngủ: bóng tối bốn góc phòng đặc quánh lại, và bóng đen cao gầy của `@VongLa` bắt đầu lượn lờ ngay sát bên ngoài lớp màn.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Thế nhưng khi cơn mê man vừa kéo đến… giữa không gian tĩnh lặng như tờ, Bình bỗng cảm thấy không khí trong phòng đặc quánh lại. Ngay bên ngoài lớp màn mỏng… có một bóng người đang lặng lẽ đi vòng quanh giường cậu!"
- **Clip 3 (`04:20–04:30` — Lip-Sync `@Binh` | On-screen: `@Binh, @VongLa`):** Từ sát mép màn tuyn, bàn tay lạnh buốt của `@VongLa` vươn ra bóp chặt lấy cổ tay trái của `@Binh`. `@Binh` trợn trừng mắt, gồng người vùng vẫy trên giường xếp nhưng toàn thân cứng đờ như đá.
  - *Thoại (@Binh):* "Ai đó?! Bỏ tay tôi ra… Cứu tôi với, bỏ tôi ra!!"
- **Clip 4 (`04:30–04:40` — VO | On-screen: `@Binh`):** Ánh nắng ban mai chiếu xiên qua song cửa sổ gỗ vào đúng chiếc giường xếp: `@Binh` giật mình ngồi bật dậy thở dốc, rồi chết lặng khi nhìn xuống cổ tay trái in hằn vết bầm tím sẫm hình năm ngón tay!
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Giật mình choàng tỉnh khi trời vừa hửng sáng, mồ hôi lạnh ướt đẫm lưng áo… Bình bàng hoàng nhìn xuống cổ tay mình. Trên làn da trắng nhợt, một vết bầm tím đen hình năm ngón tay dài ngoẵng đang hằn sâu như vừa bị ai bóp nát!"
- **Clip 5 (`04:40–04:50` — Lip-Sync `@OngBay` | On-screen: `@Binh, @OngBay`):** Từ ngoài cổng sắt vang lên tiếng gọi ấm áp của `@OngBay`. `@Binh` vội vã vén màn bước ra hiên định giơ cổ tay lên cho `@OngBay` xem, nhưng dưới nắng sớm vết bầm đã biến mất sạch trơn.
  - *Thoại (@OngBay):* "Bình ơi! Dậy chưa cháu? Rửa mặt mũi đi rồi sang nhà bác ăn bát cháo nóng cho ấm bụng nào!"
- **Clip 6 (`04:50–05:00` — VO | On-screen: `@Binh, @VongLa`):** `@Binh` đứng trên hiên nhà ngơ ngác xoay cổ tay hoàn toàn lành lặn dưới nắng sớm, trong khi máy quay lùi chậm vào góc tối gian phòng sau lưng cậu nơi bóng đen `@VongLa` đứng nhìn chằm chằm rồi tan biến.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Lạ lùng thay… vừa bước chân ra tới ánh nắng ngoài hiên, vết bầm tím đen kia đã biến mất không còn một dấu vết. Bình cố tự nhủ rằng mình chỉ hoa mắt… mà không hề biết rằng trong góc tối sau lưng, có kẻ vẫn đang dõi theo từng nhịp thở của cậu."

---

#### **Cảnh 06 (`05:00–06:00` | 6 Clips × 10s): Chuyện Rượu Đêm Của Ông Tư — Bóng Ma Xin Thuốc Lá Dưới Gốc Mít**
- **Clip 1 (`05:00–05:10` — VO | On-screen: `@Binh, @OngBay`):** Nối tiếp ánh nắng ngoài hiên, `@Binh` đi sóng đôi cùng `@OngBay` dọc theo bờ ruộng lúa xanh mướt dưới nắng chiều yên ả, gương mặt cậu giãn ra nhẹ nhõm giữa khung cảnh làng quê thanh bình.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Hai ngày tiếp theo trôi qua êm ả đến lạ thường. Ban ngày Bình theo ông Bảy ra thăm đồng, chiều về ăn cơm trò chuyện cùng gia đình ông, sự bình yên thôn dã khiến cậu vơi đi phần nào nỗi ám ảnh."
- **Clip 2 (`05:10–05:20` — VO | On-screen: `@Binh, @OngBay`):** Từ đường đồng về tới hiên nhà ngói, `@Binh` ngồi bên bàn gỗ nâng chén nước chè xanh bốc khói cùng `@OngBay`, khẽ mỉm cười lắng nghe tiếng chim chiều ríu rít ngoài vườn.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Thậm chí có những khoảnh khắc ngồi uống chén chè xanh nơi hiên nhà hàng xóm, Bình đã thoáng nghĩ… hay là cứ ở lại mảnh đất quê nghèo này mãi mãi để trốn chạy cuộc đời."
- **Clip 3 (`05:20–05:30` — VO | On-screen: `@Binh, @OngBay`):** Bóng chiều tắt dần thành đêm tối bên bàn rượu quê dưới ánh đèn vàng: `@OngBay` ngà ngà say bỗng hạ giọng ghé sát về phía `@Binh`, chỉ tay về hướng gốc mít cổ thụ đầu cổng với ánh mắt kinh hoàng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Nhưng rồi vào cái đêm ngồi uống rượu cùng các bác hàng xóm… khi hơi men đã ngà ngà, người ta bỗng ghé sát tai Bình, giọng run rẩy kể lại cái đêm ông Tư chạm mặt thứ tà ma dưới gốc mít nhà cậu."
- **Clip 4 (`05:30–05:40` — VO | On-screen: `@VongLa`):** Máy quay lướt theo hướng tay chỉ ra gốc mít cổ thụ ngập sương trắng lúc nửa đêm: bóng `@VongLa` ngồi thu lu giữa đám rễ mít, từ từ ngẩng khuôn mặt trắng bệch với hai hốc mắt đen ngòm sâu hoắm dưới ánh lửa bật lửa.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đêm ấy ông Tư đi uống rượu về khuya, thấy có bóng người ngồi co ro dưới gốc mít nhà cụ Xá bèn rút điếu thuốc mời… Nào ngờ khi ánh lửa bật lên, trước mặt ông là một khuôn mặt méo mó trắng bệch, hai hốc mắt đen ngòm không có con ngươi!"
- **Clip 5 (`05:40–05:50` — VO | On-screen: `@VongLa`):** Bóng `@VongLa` nhoẻn miệng cười lạnh lẽo rồi lùi dần tan vào thân cây mít cổ thụ xù xì, để lại bao thuốc lá nằm trơ trọi trên đám rễ mít đẫm sương đêm và bùn lạnh.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Thứ đó nhoẻn cái miệng rộng ngoác cười khanh khách rồi tan biến vào thân cây mít… Để rồi sáng hôm sau khi dân làng chạy ra xem, bao thuốc lá của ông Tư vẫn còn nằm nguyên vẹn ngay trên rễ mít lạnh ngắt."
- **Clip 6 (`05:50–06:00` — VO | On-screen: `@Binh`):** Ngay tại gốc mít cổ thụ ấy trong đêm khuya, `@Binh` một mình bước qua cánh cổng sắt trở về căn nhà hoang, ánh mắt bất an ngước nhìn tán mít đen đặc đang xào xạc giữa cơn gió lạnh.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Bước chân về lại căn nhà hoang khi đêm đã khuya khoắt, đi ngang qua gốc mít cổ thụ đen đặc… sống lưng Bình lạnh toát như có ai đang cầm cục nước đá chà dọc xương sống."

---

#### **Cảnh 07 (`06:00–07:00` | 6 Clips × 10s): Đêm Thứ Ba — Chiếc Xoong Nhôm Rơi Chói Tai & Bóng Trắng Ngoài Cửa Sổ**
- **Clip 1 (`06:00–06:10` — VO | On-screen: `@Binh`):** Đêm thứ ba trong căn nhà hoang: `@Binh` đang thiu thiu ngủ trên giường xếp trong bóng tối thì từ dưới gian bếp tiếp giáp vang lên tiếng 'CHOANG!!' chói tai của kim loại rơi xuống nền gạch.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đêm thứ ba… khi cả xóm làng đã chìm sâu vào giấc ngủ chết chóc và Bình vừa mới chợp mắt, thì từ dưới gian bếp tối om, một tiếng động chói tai bỗng nổ vang xé toạc màn đêm!"
- **Clip 2 (`06:10–06:20` — Lip-Sync `@Binh` | On-screen: `@Binh`):** `@Binh` giật bắn mình vén màn bước xuống gian bếp, bật đèn pin điện thoại soi xuống nền gạch: chiếc xoong nhôm vốn treo trên đinh cao nay nằm lăn lóc giữa nhà. Tay `@Binh` run bần bật cúi xuống nhặt.
  - *Thoại (@Binh):* "Chắc là chuột… chỉ là con chuột chạy làm rơi xoong thôi mà…"
- **Clip 3 (`06:20–06:30` — VO | On-screen: `@Binh, @VongLa`):** Khi `@Binh` vừa đứng thẳng dậy định treo chiếc xoong nhôm lên đinh tường thì bóng đèn dây tóc trên trần kêu 'XẸT!' rồi tắt phụt. Trong bóng tối đen đặc, ngay sát sau gáy `@Binh` lù lù hiện ra bóng trắng `@VongLa`.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Nhưng ngay khoảnh khắc tay cậu vừa chạm vào chiếc đinh trên tường… bóng đèn vàng trên đầu bỗng nổ lách tách rồi tắt phụt! Bóng tối nuốt chửng lấy căn phòng, và hai bàn chân Bình như bị đóng đinh cứng ngắc xuống nền gạch."
- **Clip 4 (`06:30–06:40` — VO | On-screen: `@Binh, @VongLa`):** Trong bóng tối mờ xanh lạnh lẽo, một luồng hơi thở trắng xóa lạnh như băng từ `@VongLa` phả thẳng vào sau gáy `@Binh` làm tóc gáy cậu dựng đứng, rồi bóng đèn dây tóc chợt nhấp nháy bật sáng trở lại.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Giữa bóng tối đen đặc như mực… Bình nghe rõ mồn một tiếng thở khàn đục của một kẻ nào đó đang đứng sát rạt ngay sau gáy mình, phả từng luồng hơi lạnh buốt như băng vào cổ… Một phút trôi qua dài như cả thế kỷ, trước khi ánh đèn chập chờn bật sáng trở lại."
- **Clip 5 (`06:40–06:50` — VO | On-screen: `@Binh, @VongLa`):** Khi đèn vừa sáng lại, `@Binh` thở hồng hộc đặt vội chiếc xoong lên kệ gỗ, nhưng vừa liếc mắt qua khung cửa sổ gỗ bên cạnh, bóng trắng toát của `@VongLa` lướt vụt qua ngay ngoài chấn song!
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Tim đập thình thịch muốn nổ tung lồng ngực, cậu tự lừa dối mình rằng chỉ là điện chập… Nhưng vừa liếc mắt về phía khung cửa sổ gỗ, một cái bóng trắng toát không chân vừa lướt vụt qua ngay ngoài chấn song!"
- **Clip 6 (`06:50–07:00` — VO | On-screen: `@Binh, @VongLa`):** `@Binh` lao vội về chiếc giường xếp trùm kín chăn qua đầu, trong khi máy quay lùi chậm về phía khung cửa sổ gỗ nơi năm ngón tay trắng nhợt móng đen dài của `@VongLa` đang bấu chặt lên bệ cửa.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Bình phóng lên giường trùm chăn kín mít từ đầu đến chân… mà không hề nhìn thấy ngoài song cửa sổ, một bàn tay trắng bệch với năm móng tay đen dài đang bấu chặt lấy mép gỗ, kèm theo tiếng cười khúc khích lạnh gáy vọng lại từ gốc mít."

---

#### **Cảnh 08 (`07:00–08:00` | 6 Clips × 10s): Đêm Thứ Tư Kinh Hoàng — Bàn Tay Xám Ngoét Thò Qua Lớp Màn**
- **Clip 1 (`07:00–07:10` — VO | On-screen: `@Binh`):** Đêm thứ tư lúc 02:45 sáng: ánh trăng xanh lạnh ngoài tán mít cổ thụ hắt bóng cành cây kỳ dị qua khung cửa sổ gỗ vào chiếc giường xếp giăng màn trắng nơi `@Binh` đang nằm ngủ.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đêm thứ tư… cũng là cái đêm kinh hoàng nhất trong cuộc đời của Bình. Ánh trăng thượng tuần lạnh lẽo chiếu xuyên qua tán mít cổ thụ, hắt những mảng bóng đen kỳ dị như hình hài quỷ dữ lên vách nhà."
- **Clip 2 (`07:10–07:20` — VO | On-screen: `@Binh`):** Máy quay đẩy chậm xuyên qua bóng tối tới sát tấm màn tuyn trắng dưới ánh đèn vàng tù mù: `@Binh` đang nằm ngủ bỗng mở choàng đôi mắt thâm quầng vì cảm giác lạnh buốt sống lưng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đúng hai giờ bốn mươi lăm sáng… giữa lúc vạn vật chìm vào giờ âm thịnh nhất, Bình bỗng nhiên mở choàng mắt tỉnh giấc bởi cảm giác gai người… như thể đang có một đôi mắt vô hồn nhìn chằm chằm vào mặt cậu từ cự ly cực gần."
- **Clip 3 (`07:20–07:30` — Lip-Sync `@Binh` | On-screen: `@Binh, @VongLa`):** Từ góc nhìn của `@Binh` nhìn xuyên qua lớp vải màn tuyn trắng mỏng tang: cái bóng đen cao gầy méo mó của `@VongLa` đang đứng sừng sững ngay sát mép giường xếp, cúi gằm mặt nhìn thẳng xuống cậu.
  - *Thoại (@Binh):* "A… ai… Ai đang đứng ngoài màn đấy?!"
- **Clip 4 (`07:30–07:40` — VO | On-screen: `@Binh, @VongLa`):** Bóng `@VongLa` đứng bất động ngoài màn không đáp lời; đột nhiên, bàn tay xám ngoét da nhăn nheo lạnh ngắt với năm móng tay dài đen kịt của `@VongLa` đâm xuyên thẳng qua lớp vải màn tuyn vươn về phía `@Binh`!
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đáp lại tiếng hỏi run rẩy của cậu chỉ là sự im lặng chết chóc… Và rồi, xuyên qua lớp vải màn mỏng tang, một bàn tay xám ngoét như tay xác chết với năm móng dài đen đặc từ từ thò thẳng vào bên trong màn!"
- **Clip 5 (`07:40–07:50` — Lip-Sync `@VongLa` | On-screen: `@Binh, @VongLa`):** Bàn tay xác chết xám ngoét của `@VongLa` chụp xuống bóp chặt cứng lấy cổ tay trái của `@Binh`. `@Binh` trợn mắt ú ớ không thành tiếng khi gương mặt trắng bệch của `@VongLa` áp sát lớp màn thì thào.
  - *Thoại (@VongLa):* "Đi đi… Cút khỏi căn nhà này ngay… Đây không phải chỗ của người sống chúng mày…"
- **Clip 6 (`07:50–08:00` — VO | On-screen: `@Binh`):** Bàn tay xám ngoét từ từ rút khỏi lớp màn tan vào bóng tối; `@Binh` choàng tỉnh ngồi bật dậy đẫm mồ hôi lạnh, run rẩy giơ cổ tay trái lên — vết bầm tím đen năm ngón tay hằn sâu như máu tụ và không hề biến mất nữa!
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Bình ngất lịm đi trong nỗi kinh hoàng tột độ… Để rồi khi choàng tỉnh dậy, cậu run rẩy giơ cổ tay lên nhìn: vết bầm năm ngón tay nay đã chuyển sang màu tím đen như máu chết… và lần này, nó hằn sâu vào da thịt không hề biến mất nữa!"

---

#### **Cảnh 09 (`08:00–09:00` | 6 Clips × 10s): Vết Bầm Không Tan & Nỗi Tuyệt Vọng Không Chốn Dung Thân**
- **Clip 1 (`08:00–08:10` — Lip-Sync `@Binh` | On-screen: `@Binh, @OngBay`):** Tờ mờ sáng hôm sau, `@Binh` hớt hải chạy ra sân gạch với gương mặt cắt không còn giọt máu, xắn tay áo hoodie giơ vết bầm tím đen năm ngón tay ra trước mặt `@OngBay`.
  - *Thoại (@Binh):* "Bác Bảy ơi cứu cháu với! Đêm qua có bàn tay người chết thò qua màn bóp chặt tay cháu… Bác nhìn vết bầm năm ngón tay này đi!!"
- **Clip 2 (`08:10–08:20` — Lip-Sync `@OngBay` | On-screen: `@Binh, @OngBay`):** `@OngBay` nhíu chặt hàng lông mày bạc, cầm lấy cổ tay `@Binh` săm soi vết bầm tím đen rõ mồn một dưới ánh sáng ban mai, giọng ông trầm hẳn xuống đầy nghiêm trọng.
  - *Thoại (@OngBay):* "Lạy hồn… Vết bầm năm ngón tay rõ mồn một thế này thì không phải chuyện đùa rồi! Đi, để bác vào kiểm tra quanh nhà xem thế nào!"
- **Clip 3 (`08:20–08:30` — VO | On-screen: `@Binh, @OngBay`):** `@OngBay` cầm gậy gỗ đi dọc hiên ngôi nhà ngói ba gian cùng `@Binh`, kiểm tra từng chấn song cửa sổ và chốt cửa gỗ bên trong — tất cả đều còn cài chặt và phủ nguyên lớp bụi dày.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Ông Bảy cẩn thận đi vòng quanh ngôi nhà hoang, kiểm tra từng khung cửa sổ đến cái chốt cổng sắt… Thế nhưng tuyệt nhiên không có lấy một vết cạy cửa hay dấu chân người lạ nào lọt vào từ đêm qua."
- **Clip 4 (`08:30–08:40` — VO | On-screen: `@Binh, @OngBay`):** `@OngBay` dừng bước giữa sân gạch, ngước nhìn tán mít cổ thụ âm u rồi quay sang vỗ vai cố trấn an `@Binh` với ánh mắt đầy vẻ ái ngại và thương cảm.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Không muốn làm thằng nhỏ thêm hoảng loạn, ông Bảy đành gượng gạo bảo chắc cậu nằm mơ ngủ mê nên tự bấu vào tay mình… nhưng nhìn ánh mắt trốn tránh của ông, Bình hiểu bác hàng xóm biết rõ thứ gì đang ở trong nhà."
- **Clip 5 (`08:40–08:50` — Lip-Sync `@Binh` | On-screen: `@Binh`):** Khi `@OngBay` đã về, `@Binh` ngồi một mình trên bậc thềm gạch rêu phong rút điện thoại áp vào tai gọi cho mẹ, giọng cậu lạc đi vì sợ hãi và bế tắc.
  - *Thoại (@Binh):* "Mẹ ơi… Căn nhà của ông nội thật sự có cái gì đó đáng sợ lắm mẹ ạ… Nhưng giờ con biết đi đâu được nữa hả mẹ…"
- **Clip 6 (`08:50–09:00` — VO | On-screen: `@Binh`):** `@Binh` hạ điện thoại xuống, ngồi bó gối trên bậc thềm đá lạnh lẽo quay đầu nhìn sâu vào khoảng tối u tịch bên trong gian nhà chính, đôi mắt vừa sợ hãi vừa lì lợm.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Tiến thoái lưỡng nan, quay về thành phố thì chủ nợ và cơn thịnh nộ của bố đang chờ, mà ở lại thì đêm đêm ma quỷ vây quanh… Giữa đường cùng tuyệt vọng, cái sợ trong lòng Bình bỗng biến thành một sự liều lĩnh lạ kỳ."

---

#### **Cảnh 10 (`09:00–10:00` | 6 Clips × 10s): Đêm Thứ Năm — Vong Hồn Ông Nội Hiện Hình Trong Góc Phòng**
- **Clip 1 (`09:00–09:10` — VO | On-screen: `@Binh`):** Đêm thứ năm buông xuống gian nhà chính: `@Binh` không giăng màn đi ngủ mà ngồi tựa lưng vào bức tường vôi lạnh toát, hai tay ôm gối, đôi mắt thâm quầng mở trừng trừng nhìn thẳng vào bóng tối.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đêm thứ năm… Bình quyết định không ngủ. Cậu ngồi tựa lưng vào bức tường vôi lạnh ngắt, mắt mở trừng trừng nhìn vào bóng tối, tự nhủ nếu thực sự có vong hồn nào trong ngôi nhà này, đêm nay cậu muốn nhìn thẳng vào mặt họ."
- **Clip 2 (`09:10–09:20` — VO | On-screen: `@Binh, @VongCuXa`):** Đồng hồ điểm 1 giờ sáng: nhiệt độ trong phòng đột ngột tụt xuống lạnh cóng, hơi thở của `@Binh` phả ra thành từng làn khói trắng xóa khi từ góc tối gian thờ cũ, bóng mờ bán trong suốt của `@VongCuXa` từ từ hiện lên.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đúng một giờ sáng… nhiệt độ trong gian nhà bỗng tụt xuống lạnh buốt như hầm băng, từng nhịp thở của Bình phả ra thành khói trắng. Và rồi từ góc tối nơi xưa kia đặt bàn thờ… một bóng người già nua, mờ ảo từ từ hiện ra kèm tiếng ho khàn đục."
- **Clip 3 (`09:20–09:30` — Lip-Sync `@VongCuXa` | On-screen: `@Binh, @VongCuXa`):** Bóng người già trong bộ áo bà ba nâu sồng bạc màu (`@VongCuXa`) chậm rãi quay mặt lại dưới ánh trăng lạnh chiếu qua cửa sổ. `@Binh` sững sờ nhận ra gương mặt hiền từ nhưng hốc hác của ông nội mình!
  - *Thoại (@VongCuXa):* "Bình đấy ư… Cháu nội của ông… Lại đây với ông nào con…"
- **Clip 4 (`09:30–09:40` — Lip-Sync `@VongCuXa` | On-screen: `@Binh, @VongCuXa`):** `@VongCuXa` ngước nhìn khoảng tường vôi trống trải lạnh lẽo bằng đôi mắt sâu hoắm đượm buồn, giọng ông khàn đục vang vọng giữa gian nhà trống.
  - *Thoại (@VongCuXa):* "Ngày ông mất, bố mày làm đám tang xong liền rước bát hương lên thành phố… nhưng không làm lễ rước vong, hồn ông không qua được cổng thành Hoàng nên phải chịu cảnh lạnh lẽo bơ vơ ở đây suốt bao năm trời…"
- **Clip 5 (`09:40–09:50` — Lip-Sync `@Binh` | On-screen: `@Binh, @VongCuXa`):** `@Binh` bò lết trên nền gạch tới quỳ sụp xuống trước bóng `@VongCuXa`, hai hàng nước mắt tuôn rơi nức nở trong niềm xót thương và hối hận.
  - *Thoại (@Binh):* "Ông nội ơi… Cháu có lỗi với ông! Cháu và bố cháu ở trên thành phố thật sự không ai biết ông phải chịu cảnh lạnh lẽo không hương khói thế này ông ơi!"
- **Clip 6 (`09:50–10:00` — VO | On-screen: `@Binh, @VongCuXa`):** `@VongCuXa` nhìn đứa cháu nội đang quỳ dưới nền gạch bằng ánh mắt thương xót rồi bóng hình ông nhạt dần vào làn sương đêm xanh lạnh, để lại `@Binh` quỳ lặng đi giữa gian nhà.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Vong hồn cụ Xá thở dài bảo rằng, chính ông đã sai vong hồn vụ tai nạn ngoài gốc mít vào hù dọa vì tưởng cháu về bán đất tổ tiên… Trước khi tan vào bóng tối, ông chỉ để lại một lời trăn trối: hãy gọi bố mày về đây chuộc lỗi với người âm!"

---

#### **Cảnh 11 (`10:00–11:00` | 6 Clips × 10s): Cuộc Gọi Cho Bố & Cái Tát Nảy Lửa Giữa Sân Quê**
- **Clip 1 (`10:00–10:10` — VO | On-screen: `@Binh`):** Rạng sáng hôm sau, `@Binh` bước từ gian thờ ra ngồi trên bậc thềm hiên nhà dưới ánh bình minh nhợt nhạt, đôi mắt sâu trũng nhưng đầy kiên định bấm gọi điện thoại cho bố.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Trắng đêm suy nghĩ sau cuộc gặp gỡ âm dương đẫm nước mắt với vong hồn ông nội… ngay khi trời vừa rạng sáng, Bình hít một hơi thật sâu, bấm gọi vào số điện thoại mà suốt mấy tuần qua cậu kinh sợ nhất: số của bố mình."
- **Clip 2 (`10:10–10:20` — Lip-Sync `@OngQuan` | On-screen: `@OngQuan`):** Ở đầu dây bên kia, `@OngQuan` đứng bên cửa sổ ánh sáng gắt, gương mặt đỏ gay đanh thép gầm lên dữ dội vào chiếc điện thoại đang áp chặt bên tai.
  - *Thoại (@OngQuan):* "Cái thằng nghịch tử kia! Mày phá gia chi tử nợ nần bốn trăm triệu rồi giờ còn dám lôi cả vong hồn ông nội đã khuất ra để lừa bố mày hả?!"
- **Clip 3 (`10:20–10:30` — Lip-Sync `@Binh` | On-screen: `@Binh`):** Ngoài hiên nhà quê, `@Binh` nắm chặt điện thoại, nước mắt chảy dài trên gò má tái nhợt nhưng giọng nói đanh lại, quỳ thẳng trên thềm gạch không hề né tránh.
  - *Thoại (@Binh):* "Bố ơi… Con gọi cuộc điện thoại này là con đã chấp nhận chịu đòn của bố rồi. Bố đánh gãy chân con cũng được, nhưng con van bố… hãy về quê xin lỗi ông nội đi bố ơi!"
- **Clip 4 (`10:30–10:40` — VO | On-screen: `@Binh`):** Tiếng máy cúp cái rập từ đầu dây bên kia; `@Binh` từ từ hạ điện thoại xuống lòng bàn tay, lặng lẽ ngồi trên bậc thềm đá nhìn ra cánh cổng sắt dưới gốc mít chờ đợi.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Tiếng quát tháo giận dữ của ông Quân tắt phụt trong điện thoại. Bình ngồi bất động nơi hiên nhà rêu phong, lòng đã sẵn sàng hứng chịu trận lôi đình, miễn sao cha mình chịu đặt chân về lại mái nhà xưa."
- **Clip 5 (`10:40–10:50` — VO | On-screen: `@Binh, @OngQuan, @BaPhuong`):** Nắng chiều nghiêng qua gốc mít cổ thụ: cánh cổng sắt mở toang, `@OngQuan` mặt đanh lại như thép nguội sải bước nhanh vào sân gạch nơi `@Binh` đang đứng chờ, theo sát phía sau là `@BaPhuong` hớt hải.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Quả nhiên ngay chiều hôm ấy, ông Quân cùng bà Phượng đã có mặt trước cổng ngôi nhà cổ. Gương mặt người cha đanh lại, đôi mắt long lên sòng sọc khi nhìn thấy đứa con trai độc nhất đang đứng chờ giữa sân."
- **Clip 6 (`10:50–11:00` — Lip-Sync `@Binh` | On-screen: `@Binh, @OngQuan, @BaPhuong`):** `@OngQuan` vung tay tát mạnh làm `@Binh` ngã quỵ xuống sân gạch. `@BaPhuong` nhào tới ôm chặt lấy cánh tay chồng khóc nức nở, còn `@Binh` lập tức quỳ thẳng dậy cúi đầu sát đất.
  - *Thoại (@Binh):* "Con xin lỗi bố mẹ… Chuyện nợ nần con xin chịu hết mọi hình phạt, nhưng tối nay bố hãy ngủ lại căn nhà này một đêm thôi bố ơi!"

---

#### **Cảnh 12 (`11:00–12:00` | 6 Clips × 10s): Giấc Mơ Đẫm Nước Mắt Của Ông Quân & Nén Hương Tạ Tội Trước Mộ Cha**
- **Clip 1 (`11:00–11:10` — VO | On-screen: `@OngQuan, @BaPhuong, @Binh`):** Đêm buông xuống ngôi nhà cổ: `@OngQuan` nằm trên chiếc giường gỗ đặt giữa gian phòng khách tối om với gương mặt còn hầm hầm giận dữ, trong khi `@BaPhuong` và `@Binh` ngồi thức trắng ở góc bàn bên cạnh.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đêm hôm ấy, ông Quân nhất quyết nằm ngay tại gian phòng khách cũ với lời tuyên bố đanh thép rằng sáng mai sẽ áp giải thằng con bất hiếu về thành phố… Thế nhưng, chính vào cái đêm định mệnh ấy…"
- **Clip 2 (`11:10–11:20` — VO | On-screen: `@OngQuan, @VongCuXa`):** Máy quay đẩy chậm vào gương mặt đang ngủ của `@OngQuan` dưới ánh trăng lạnh: đôi lông mày ông nhíu chặt đau đớn, hai hàng nước mắt nóng hổi trào ra khỏi khóe mắt khi bóng mờ `@VongCuXa` đứng lặng lẽ bên đầu giường.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Giữa đêm khuya thanh vắng… không một ai biết ông Quân đã gặp hay mơ thấy điều gì trong gian nhà lạnh lẽo ấy. Người ta chỉ thấy trong bóng tối mờ sương, người đàn ông sắt đá suốt mấy chục năm chưa từng rơi lệ… bỗng khóc nấc lên từng hồi trong giấc ngủ."
- **Clip 3 (`11:20–11:30` — VO | On-screen: `@OngQuan`):** Tờ mờ sáng trong màn sương trắng xóa ngoài nghĩa trang đồng làng, `@OngQuan` với đôi mắt đỏ hoe một mình quỳ sụp trước ngôi mộ đá rêu phong của cụ Xá, thành tâm cắm nén hương trầm nghi ngút khói.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Khi trời vừa tờ mờ sáng, chẳng còn thấy ông Quân quát tháo một lời nào nữa… Ông lặng lẽ mua hương hoa ra nghĩa trang đồng làng, một mình quỳ gục trước nấm mộ cỏ mọc xanh rì của cha suốt hàng giờ liền."
- **Clip 4 (`11:30–11:40` — VO | On-screen: `@OngQuan, @Binh`):** Trở về gian phòng khách căn nhà cổ, `@OngQuan` xắn tay áo cùng `@Binh` cẩn thận khiêng một chiếc tủ thờ gỗ gụ chạm trổ trang nghiêm đặt vào đúng vị trí trung tâm gian giữa.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Trở về từ nghĩa trang, ông Quân lập tức thuê thợ mộc đóng một chiếc tủ thờ gỗ gụ mới tinh, tự tay kê vào đúng chính giữa gian nhà — nơi ngày xưa cụ Xá vẫn thường ngồi uống trà mỗi buổi sớm mai."
- **Clip 5 (`11:40–11:50` — Lip-Sync `@OngQuan` | On-screen: `@OngQuan, @BaPhuong, @Binh`):** `@OngQuan` hai tay nâng di ảnh cụ Xá và bát hương đồng vừa rước về đặt lên tủ thờ gỗ gụ mới, thắp ba nén nhang trầm rồi quỳ xuống trước mặt `@BaPhuong` và `@Binh`, nghẹn ngào khấn nguyện.
  - *Thoại (@OngQuan):* "Bố ơi… Con bất hiếu quá, bao năm qua để hồn bố phải bơ vơ lạnh lẽo nơi quê nhà… Hôm nay con rước bố về lại gian thờ tổ, xin bố tha tội cho con!"
- **Clip 6 (`11:50–12:00` — VO | On-screen: `@OngQuan, @Binh`):** Bước ra dưới gốc mít cổ thụ ngoài cổng, `@OngQuan` cùng `@Binh` dựng một ngôi miếu gạch nhỏ trang nghiêm, khói nhang trầm tỏa nghi ngút hòa giải âm khí dưới tán cây.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Chưa dừng lại ở đó, ngay dưới gốc mít cổ thụ trước cổng, ông Quân còn cho xây một ngôi miếu gạch nhỏ và mời thầy về lập đàn cầu siêu ròng rã suốt bốn mươi chín ngày đêm cho sáu vong hồn tử nạn năm xưa."

---

#### **Cảnh 13 (`12:00–13:00` | 6 Clips × 10s): Bốn Mươi Chín Ngày Ăn Chay Cầu Siêu & Ngôi Miếu Nhỏ Dưới Gốc Mít**
- **Clip 1 (`12:00–12:10` — VO | On-screen: `@OngQuan, @BaPhuong, @Binh`):** Sáng sớm thanh tịnh: `@OngQuan` mặc áo sơ mi trắng giản dị thành tâm thắp nhang trước bàn thờ gỗ gụ, trong khi ngoài hiên `@BaPhuong` và `@Binh` cần mẫn quét dọn lá mít dưới nắng sớm.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Suốt bốn mươi chín ngày ròng rã, ông Quân xin nghỉ phép ở hẳn lại quê nhà, ăn chay trường và tự tay hương khói sớm hôm. Ngôi nhà hoang lạnh lẽo suốt hai thập kỷ bỗng ấm dần lên bởi hơi người và mùi trầm hương thanh tịnh."
- **Clip 2 (`12:10–12:20` — VO | On-screen: `@OngQuan`):** Từ hiên nhà bước ra gốc mít cổ thụ trong nắng chiều vàng dịu, `@OngQuan` thành kính đặt đĩa hoa quả tươi và thắp nhang tại ngôi miếu gạch nhỏ, làn khói bay thẳng lên tán lá xanh mát.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Ngôi miếu nhỏ dưới gốc mít trở thành nơi nương tựa ấm cúng có đèn nhang mỗi tối… để những vong hồn lỡ bước trên khúc cua năm nào không còn phải vất vưởng, lạnh lẽo tìm hơi người trong ngôi nhà hoang nữa."
- **Clip 3 (`12:20–12:30` — VO | On-screen: `@OngQuan, @Binh`):** Đêm thứ 49 bên trong gian thờ chính: `@OngQuan` và `@Binh` ngồi tĩnh lặng chắp tay trước bàn thờ cụ Xá rực ánh đèn dầu vàng ấm, khói hương cuộn tròn bay lên tạo cảm giác bình an kỳ lạ.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đêm thứ bốn mươi chín… cả căn nhà ngói ba gian tỏa ra một luồng sinh khí ấm áp lạ thường. Không còn những cơn gió âm hàn thổi lùa qua khe cửa, cũng chẳng còn bóng đen nào lảng vảng quanh chiếc giường ngủ."
- **Clip 4 (`12:30–12:40` — VO | On-screen: `@OngQuan, @Binh`):** Góc máy từ ngoài gốc mít nhìn xuyên qua sân gạch vào ngôi nhà trong đêm: ánh đèn vàng ấm áp tỏa ra từ các ô cửa sổ gỗ nơi `@OngQuan` và `@Binh` đang ngồi trò chuyện, tiếng chuông chùa ngân vang.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Nhìn từ ngoài cổng vào, lần đầu tiên sau gần hai mươi năm, người dân trong làng thấy căn nhà cụ Xá sáng bừng ánh đèn ấm áp… như thể mọi oán khí và nỗi cô quạnh của cõi âm đều đã được hóa giải trọn vẹn."
- **Clip 5 (`12:40–12:50` — Lip-Sync `@OngQuan` | On-screen: `@OngQuan, @BaPhuong, @Binh`):** Sáng hôm sau bên hiên nhà ngập nắng ấm, `@OngQuan` đặt tay lên vai `@Binh` và quay sang nhìn `@BaPhuong` với ánh mắt trầm tĩnh, bao dung hơn trước rất nhiều.
  - *Thoại (@OngQuan):* "Bà đưa thằng Bình về thành phố trước đi, gom góp tiền bạc trả dần nợ nần cho người ta… Tôi ở lại lo nốt lễ tuần chung thất cho ông cụ rồi sẽ lên sau."
- **Clip 6 (`12:50–13:00` — VO | On-screen: `@OngQuan`):** `@OngQuan` đứng chắp tay cúi đầu trang nghiêm trước ngôi mộ đá đã được tu sửa khang trang của cụ Xá giữa cánh đồng lúa xanh rì trong gió sớm.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Biến cố tưởng chừng đẩy cả gia đình xuống vực thẳm ấy… rốt cuộc lại là sợi dây vô hình kéo người cha lầm lỗi trở về với cội nguồn, để từ đó cứ mỗi dịp rằm mồng một, ngôi nhà quê lại đỏ lửa khói hương."

---

#### **Cảnh 14 (`13:00–14:00` | 6 Clips × 10s): Món Nợ Được Hoàn Trả & Mâm Cơm Đoàn Tụ Nơi Quê Nội**
- **Clip 1 (`13:00–13:10` — VO | On-screen: `@Binh`):** Những ngày cuối năm ngập nắng ấm trên hiên ngôi nhà ngói ba gian ở quê nội: `@Binh` ngồi bên bàn gỗ mở laptop đọc thông báo của cơ quan công an về việc triệt phá đường dây lừa đảo và thu hồi tài sản.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Ở hiền thì gặp lành, lòng hiếu thảo và sự thành tâm chuộc lỗi dường như đã thấu tới trời xanh… Cuối năm ấy, công an triệt phá thành công đường dây lừa đảo tiền ảo và hoàn trả lại phần lớn số tiền mà Bình từng bị chiếm đoạt."
- **Clip 2 (`13:10–13:20` — VO | On-screen: `@Binh`):** Ngay bên chiếc laptop trên bàn gỗ hiên nhà, `@Binh` nâng tờ giấy báo tiếp nhận quay lại học tập của trường đại học trên tay, nở nụ cười rạng rỡ và biết ơn sau chuỗi ngày tăm tối.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Trả dứt được món nợ đè nặng trên vai, Bình được nhà trường đồng ý cho quay trở lại giảng đường hoàn thành năm học cuối… Một cánh cửa cuộc đời mới lại mở ra sau những tháng ngày tưởng như đã mất tất cả."
- **Clip 3 (`13:20–13:30` — VO | On-screen: `@OngQuan, @BaPhuong, @Binh`):** `@Binh` gấp laptop lại khi `@BaPhuong` bưng mâm cơm gỗ bốc khói nghi ngút ra hiên nhà: `@OngQuan`, `@BaPhuong` và `@Binh` quây quần ấm cúng bên nhau, phía xa là gốc mít xanh tốt.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Những ngày cuối năm se lạnh, cả gia đình lại cùng nhau quây quần nơi hiên nhà ngói ba gian quê nội. Bên mâm cơm đoàn viên bốc khói nghi ngút, không còn tiếng quát tháo giận dữ, chỉ còn sự bình yên sau giông bão."
- **Clip 4 (`13:30–13:40` — Lip-Sync `@OngQuan` | On-screen: `@OngQuan, @BaPhuong, @Binh`):** Bên mâm cơm gỗ đoàn viên, `@OngQuan` trầm ngâm rót chén rượu trắng đặt trước mặt con trai, ánh mắt nghiêm nghị nhưng ấm áp nhìn `@Binh` đang cúi đầu lắng nghe.
  - *Thoại (@OngQuan):* "Đời người ai chẳng có lúc lầm đường lạc lối hả con… Quan trọng là biết quay đầu, biết sống có hiếu với tổ tiên ông bà thì trời đất mới dung thứ."
- **Clip 5 (`13:40–13:50` — VO | On-screen: `@Binh`):** Sau bữa cơm chiều, `@Binh` bước qua sân gạch ra gốc mít cổ thụ trước cổng, thành kính thắp ba nén nhang thơm cắm vào bát hương của ngôi miếu gạch nhỏ.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Chiều muộn, Bình bước ra gốc mít cổ thụ, thành tâm thắp nén nhang thơm lên ngôi miếu nhỏ… Trong thâm tâm mình, cậu luôn thầm cảm ơn những đêm kinh hoàng ấy đã giúp gia đình cậu thức tỉnh và tìm lại được nhau."
- **Clip 6 (`13:50–14:00` — VO | On-screen: `@Binh, @OngQuan, @BaPhuong`):** Từ ngôi miếu nhỏ dưới gốc mít, máy quay nâng dần lên cao nhìn xuống ngôi nhà ngói ba gian sạch sẽ, sân gạch phẳng phiu nơi `@Binh`, `@OngQuan` và `@BaPhuong` đứng bên hiên đèn vàng ấm áp.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Ngôi nhà từng bị cả làng gọi là nhà ma với bao nỗi khiếp đảm… giờ đây đã thực sự trở thành chốn dương thịnh âm an, nơi người sống tìm thấy bình yên và người khuất tìm được chốn đi về."

---

#### **Cảnh 15 (`14:00–15:00` | 6 Clips × 10s): Đêm Trăng Thanh Tịnh — Dương Thịnh Âm An & Lời Nhắn Cõi Âm**
- **Clip 1 (`14:00–14:10` — VO | On-screen: `@Binh`):** Màn đêm trăng rằm dịu vợi buông xuống ngôi nhà ngói ba gian: máy quay đẩy chậm vào gốc mít cổ thụ và ngôi miếu gạch nhỏ với ba nén nhang vừa được `@Binh` thắp đang cháy đỏ rực trong đêm.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Quý vị và các bạn thân mến… trên cõi đời này, có những thứ mắt thường chúng ta không thể nhìn thấy, và có những nỗi tủi phận của người đã khuất mà người sống vô tình lãng quên."
- **Clip 2 (`14:10–14:20` — VO | On-screen: `@VongCuXa`):** Ánh trăng bạc xuyên qua kẽ lá mít in bóng xuống sân gạch sạch sẽ: bên hiên nhà, hình bóng mờ ảo của `@VongCuXa` khẽ mỉm cười thanh thản rồi tan thành những đốm sáng nhẹ bay lên trời đêm.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Đôi khi ranh giới giữa hai cõi âm dương mỏng manh hơn chúng ta tưởng rất nhiều… Và sợi dây duy nhất có thể hóa giải mọi oán hờn, sưởi ấm cả người sống lẫn người khuất, chính là chữ Hiếu và lòng thành kính từ tận đáy tâm can."
- **Clip 3 (`14:20–14:30` — VO | On-screen: `@Binh, @OngQuan, @BaPhuong`):** Máy quay lướt từ hiên trăng vào bên trong gian thờ chính: `@Binh` cùng `@OngQuan` và `@BaPhuong` đứng chắp tay trang nghiêm trước tủ thờ gỗ gụ ấm khói trầm hương dưới ánh đèn vàng.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Câu chuyện về Căn Nhà Âm Dương khép lại như một lời nhắc nhở sâu sắc cho mỗi người con đất Việt: dù đi đâu về đâu, giàu sang hay cơ hàn, cũng xin đừng bao giờ để lạnh khói hương nơi bàn thờ tổ tiên."
- **Clip 4 (`14:30–14:40` — VO | On-screen: `@OngBay`):** Ngoài cổng sắt mở rộng dưới ánh trăng, `@OngBay` đi bộ ngang qua đường làng, mỉm cười gật đầu nhìn vào ngôi nhà sáng đèn ấm áp rồi chậm rãi bước tiếp.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Bởi lẽ tổ tiên ông bà chẳng bao giờ đòi hỏi mâm cao cỗ đầy… thứ người đã khuất mong mỏi nhất chỉ là sự tưởng nhớ và tấm lòng hướng về cội nguồn của con cháu đời sau."
- **Clip 5 (`14:40–14:50` — VO | On-screen: `@Binh, @OngQuan, @BaPhuong`):** Toàn cảnh flycam đêm trăng rằm nâng cao dần: ngôi nhà ngói ba gian nơi `@Binh`, `@OngQuan` và `@BaPhuong` sum vầy tỏa ánh sáng vàng ấm áp giữa cánh đồng lúa Bắc Bộ mênh mông.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Cảm ơn quý vị và các bạn đã lắng nghe trọn vẹn bộ phim truyện ma đêm khuya Căn Nhà Âm Dương. Nếu yêu thích những câu chuyện tâm linh nhân quả làng quê Bắc Bộ, hãy nhấn đăng ký kênh để đồng hành cùng chúng tôi trong những đêm tiếp theo."
- **Clip 6 (`14:50–15:00` — VO | On-screen: `@Binh`):** Cận cảnh đốm lửa đỏ của ba nén nhang nơi ngôi miếu dưới gốc mít khẽ bùng sáng trong làn gió đêm, phía sau hiên nhà `@Binh` khép nhẹ cánh cửa gỗ dưới ánh trăng thanh tịnh.
  - *Lời dẫn (Narrator - VOICE_LOCK_NARRATOR_CNHADG):* "Còn bây giờ… khi đồng hồ đã điểm sang canh ba, xin chúc quý vị có một giấc ngủ thật bình yên… và hãy nhớ lắng nghe xem, ngoài hiên nhà mình đêm nay… có tiếng gió nào đang thì thầm hay không."

---

