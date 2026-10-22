# 🔒 MASTER CONTEXT — 365 NGÀY VIỆT NAM (SINGLE SOURCE OF TRUTH)

> **MỤC ĐÍCH FILE NÀY:**  
> File này là **BỘ NÃO TỔNG HỢP DUY NHẤT** của toàn series. **BẮT BUỘC** phải crawl đọc và kiểm tra file này TRƯỚC KHI viết bất kỳ kịch bản clip nào (clip mới hoặc viết lại clip cũ).  
> Mọi thông tin nhân vật, quy tắc đạo diễn, format prompt, lộ trình, trạng thái đạo cụ, giọng nói, trang phục đều phải lấy từ đây.  
> **KHÔNG ĐƯỢC** tự sáng tạo thêm bất kỳ chi tiết nào ngoài file này.

---

## 📋 QUY TRÌNH BẮT BUỘC KHI TẠO TẬP MỚI (MANDATORY WORKFLOW)

```
BƯỚC 1: Crawl & đọc MASTER_CONTEXT.md (file này)
BƯỚC 2: Đọc README.md của tập trước đó để nắm khung hình cuối & nối cảnh
BƯỚC 3: Xác định tỉnh/thành tiếp theo theo BẢNG LỘ TRÌNH bên dưới
BƯỚC 4: Viết README.md của tập mới (tóm tắt lộ trình, danh sách clip, logic đạo cụ)
BƯỚC 5: Viết từng clip-{số}.md theo đúng TEMPLATE PROMPT bên dưới
BƯỚC 6: Cross-check tất cả clip vừa viết với:
         ✅ 9 QUY TẮC ĐẠO DIỄN (mục II)
         ✅ KHÓA NHÂN VẬT (mục III) — copy nguyên văn, không sửa
         ✅ LOGIC ĐẠO CỤ MŨ BẢO HIỂM (mục IV) — kiểm tra nguồn gốc vật lý
         ✅ TRẠNG THÁI NỐI CẢNH (mục V) — end frame clip N = start clip N+1
         ✅ THOẠI & GIỌNG NÓI (mục VI) — đúng âm sắc, đúng số âm tiết
         ✅ ĐỊA DANH VIẾT HOA (mục VII)
BƯỚC 7: Cập nhật BẢNG TRẠNG THÁI CÁC TẬP ĐÃ HOÀN THÀNH (mục IX)
```

---

## I. THÔNG TIN SERIES TỔNG QUAN

- **Tên series:** 365 Ngày Việt Nam — Vy & Joi (Chuyện Tình Xuyên Việt)
- **Thể loại:** Authentic Experiential Travel Vlog, Phim ngắn du lịch điện ảnh
- **Hành trình:** 365 ngày từ Cực Bắc (Hà Giang) đến Cực Nam (Cà Mau), xuyên suốt 63 tỉnh thành
- **Thời lượng mỗi tập:** 60 – 70 giây (6 – 7 clip × đúng 10 giây/clip)
- **Quy chuẩn mỗi clip:** Đúng 10 giây, khung hình dọc 9:16, 24fps, Single Continuous Shot
- **Tông điệu:** Trẻ trung, tự do, phóng khoáng, ngọt ngào, đậm tình yêu đôi lứa, tự hào cảnh sắc Việt Nam
- **Model AI:** Veo 3.1 (Google Flow) — 8 giây mỗi lần tạo, ghép scene

---

## II. 🛡️ 9 QUY TẮC ĐẠO DIỄN BẮT BUỘC (COPY NGUYÊN VĂN VÀO MỌI CLIP)

### QUY TẮC 1: BÁM SÁT TUYỆT ĐỐI GIỮA GIỌNG NÓI VÀ NHÂN VẬT (MANDATORY CHARACTER-VOICE LOCK & REAL-TIME LIP SYNC)
- **Khóa chặt camera vào người nói:** Giọng nói PHẢI phát ra từ chính nhân vật đang xuất hiện rõ mặt trong khung hình. Khi @Vy cất tiếng nói thì máy quay lập tức khóa chặt cận cảnh gương mặt @Vy; khi @Joi cất tiếng nói thì máy quay lia êm khóa chặt cận cảnh gương mặt @Joi. Tuyệt đối KHÔNG ĐƯỢC để tiếng người này nhưng cam quay người khác hoặc quay phong cảnh/món ăn mà không thấy mặt người nói.
- **Khẩu hình bám sát từng âm tiết 100%:** Từng cử động cơ mặt, bờ môi đóng mở, răng và khẩu hình miệng phải bám sát chính xác từng mili-giây với từng âm tiết tiếng Việt phát ra theo thời gian thực (real-time phoneme-to-viseme match).
- **Đồng bộ âm sắc nhân vật:** Giọng nữ @Vy trong trẻo, ngọt ngào, phát âm chuẩn thanh điệu tiếng Việt; giọng nam @Joi trầm ấm, hào sảng, nói tiếng Việt tự nhiên. Hai giọng nói tách biệt rõ rệt và bám chặt 100% vào khuôn mặt từng nhân vật.
- **Tuyệt đối cấm:** Cấm hoàn toàn voiceover (tiếng nói ngoài khung hình), cấm lồng tiếng lệch (desync), cấm mấp máy môi mà không có tiếng, cấm có tiếng mà khẩu hình môi đứng yên.

### QUY TẮC 2: VIẾT HOA CHUẨN XÁC TẤT CẢ ĐỊA DANH (STRICT CAPITALIZATION OF PLACE NAMES)
Mọi danh từ riêng chỉ địa danh trong lời thoại và kịch bản bắt buộc phải VIẾT HOA chuẩn ngữ pháp tiếng Việt để AI nhận dạng chính xác và phát âm đúng 100% ngữ điệu, không đọc sai.

### QUY TẮC 3: CÚ MÁY FLYCAM MỞ MÀN & ZOOM VÀO NHÂN VẬT (FLYCAM OPENING & SMOOTH ZOOM-IN)
Chỉ áp dụng cho **Clip 1 của mỗi tập**. Cảnh flycam lướt nhẹ lấy đại cảnh trong 1s đến 1.5s đầu. Ngay khi nhân vật cất tiếng nói (`00:01.5`), flycam lập tức sà xuống và zoom lên mượt mà tiến sát vào cận/trung cận nhân vật đang nói.

### QUY TẮC 4: KHOẢNG ĐỆM KHÔNG THOẠI CUỐI CLIP (00:07.5–00:10) ĐỂ CHUYỂN CẢNH MƯỢT (SILENT OUTRO BUFFER)
Thoại nhân vật kết thúc dứt điểm hoàn toàn TRƯỚC giây `00:07.5`. Từ `00:07.5` đến `00:10` (2.5 giây cuối) TUYỆT ĐỐI KHÔNG CÓ THOẠI, dành trọn vẹn cho hành động tạo đà chuyển cảnh và âm thanh tự nhiên/nhạc nền.

### QUY TẮC 5: NỐI CẢNH ĐẦU — CUỐI LIỀN MẠCH PHÙ HỢP NỘI DUNG & ĐỊA LÝ (SEAMLESS MATCH-CUT & GEOGRAPHICAL CONTINUITY)
Cuối Clip N tạo đà hành động / hướng di chuyển thực tế; đầu Clip N+1 tiếp nối chính xác hành động và vị trí đó theo đúng cung đường di chuyển ngoài đời thực, không nhảy cóc không gian.

### QUY TẮC 6: TẬP TRUNG MỘT CÚ MÁY (SINGLE CONTINUOUS SHOT)
Toàn bộ phân cảnh 10 giây được ghi hình trong một cú máy mượt mà duy nhất, không cắt góc đột ngột.

### QUY TẮC 7: PHONG CÁCH DIỄN XUẤT ĐỜI THỰC — TUYỆT ĐỐI KHÔNG THÊM THÔNG TIN NHÂN VẬT (AUTHENTIC VLOGGING — NO CHARACTER BIO)
100% biểu cảm, cử chỉ và giọng nói của người đi du lịch trải nghiệm thật; tuyệt đối không giới thiệu tên tuổi rập khuôn ("mình là Vy", "đây là Joi"), chỉ chào và rủ đi khám phá tự nhiên. Tuyệt đối không hiển thị bất kỳ thẻ tên, bảng thông tin hay profile nhân vật nào trong video.

### QUY TẮC 8: KHÔNG PHỤ ĐỀ, KHÔNG CHỮ, KHÔNG WATERMARK
Khung hình 9:16 dọc chuẩn điện ảnh 24fps sạch sẽ 100%.

### QUY TẮC 9: QUY ĐỊNH BẮT BUỘC ĐỘI MŨ BẢO HIỂM KHI LÁI XE & LOGIC ĐẠO CỤ VẬT LÝ (MANDATORY PROP BLOCKING & HELMET RULE)
- **Tuyệt đối không tự nhiên xuất hiện hoặc biến mất:** Mũ bảo hiểm phải có nguồn gốc vật lý cụ thể trong khung hình (móc trên ghi-đông xe, đặt trên bàn gỗ, để trên giá gỗ). Khi cần đội hoặc tháo, nhân vật phải có động tác hình thể thực tế: vươn tay gỡ móc/nhấc mũ, nâng mũ chụp lên đầu, ngón tay luồn dưới cằm cài chốt khóa quai (tiếng "tách" cơ học) hoặc bấm chốt nhả khóa nhấc mũ ra.
- Khi điều khiển hoặc ngồi trên xe mô tô Scrambler di chuyển trên đường, cả @Vy và @Joi BẮT BUỘC PHẢI ĐỘI MŨ BẢO HIỂM.
- **Quy chuẩn mũ bảo hiểm điện ảnh:** Mũ bảo hiểm 3/4 phong cách cổ điển (vintage open-face helmet) cao cấp, quai cài chắc chắn, trang bị kính chắn gió trong suốt (clear visor), đảm bảo **100% gương mặt, ánh mắt, biểu cảm và cử động môi lộ rõ hoàn toàn**.
- **Mũ của @Vy:** Mũ 3/4 màu be ngà / kem viền da nâu vintage.
- **Mũ của @Joi:** Mũ 3/4 màu xanh rêu nhám / xám titan viền da nâu mạnh mẽ.
- Khi dừng xe vào quán ăn, đi thuyền hoặc đứng tham quan cố định: Tháo mũ bảo hiểm cầm tay hoặc móc gọn gàng trên ghi-đông xe Scrambler.

---

## III. 🔒 BẢNG KHÓA NHẬN DIỆN NHÂN VẬT & XE (COPY NGUYÊN VĂN — KHÔNG ĐƯỢC SỬA)

### 🌸 @Vy — Nữ chính

**Ngoại hình chi tiết:**
- **Gương mặt:** Nét đẹp Á Đông thuần khiết, mặt trái xoan thanh tú, da trắng hồng mịn màng rạng rỡ, mắt bồ câu đen láy sâu thẳm, lông mi cong, nụ cười ngọt ngào e ấp lộ má lúm đồng tiền nhẹ bên má trái.
- **Vóc dáng:** Cao 1m64, thân hình thon gọn mảnh mai nữ tính (slim toned), khung xương thanh thoát.
- **Tóc:** Tóc đen hạt dẻ tự nhiên dài ngang lưng, uốn sóng lơi nhẹ bồng bềnh, rẽ ngôi 5/5, có hai lọn tóc mai uốn nhẹ buông lơi ôm gò má.

**Trang phục Chặng Đông Bắc Bộ (Tập 1 – 5):**
Áo len dệt kim mỏng cổ lọ màu be ngà + áo khoác gió lửng màu hồng đất pastel + khăn len thổ cẩm quả trám đỏ cam + quần jeans cạp cao xanh nhạt vintage + boots da lộn nâu cà phê + túi mây tròn quai da đeo chéo. Khi đi xe môtô: Mũ bảo hiểm 3/4 vintage màu be ngà viền da nâu, kính chắn gió trong suốt lộ rõ toàn bộ gương mặt và khẩu hình miệng.

**Giọng nói:** Giọng nữ trong trẻo, ngọt ngào, phát âm chuẩn thanh điệu tiếng Việt.

**Prompt lock tiếng Anh (copy nguyên văn):**
```
@Vy = Vy: A gorgeous 24-year-old Vietnamese woman, 164cm tall, slim toned feminine build. Oval face, fair radiant natural skin, warm expressive dark almond eyes, sweet dimpled smile. Long wavy dark chocolate hair falling past shoulders with soft wispy face-framing strands. Dressed in ivory cream turtleneck sweater, dusty rose crop windbreaker jacket, burgundy-orange woven wool scarf, light-wash vintage straight jeans, brown suede hiking boots, round rattan crossbody bag. When riding motorcycle: wears ivory cream 3/4 vintage open-face helmet with brown leather trim and clear visor showing entire face and lips. Authentic, elegant, lively travel vlogger.
```

---

### 🌲 @Joi — Nam chính

**Ngoại hình chi tiết:**
- **Gương mặt:** Nét điển trai góc cạnh nam tính Tây Âu, quai hàm sắc nét, mắt xanh lam khói (steel-blue eyes) sâu thẳm ấm áp, lông mày rậm, ánh mắt si tình cưng chiều bạn gái.
- **Râu & Tóc:** Râu quai nón tỉa ngắn 3mm bao quanh cằm; mái tóc nâu xoăn gợn sóng lãng tử bồng bềnh tự nhiên.
- **Vóc dáng:** Cao 1m85, vóc dáng thể thao vạm vỡ săn chắc (athletic muscular broad-shouldered build), ngực nở, bắp tay rắn rỏi gân guốc.

**Trang phục Chặng Đông Bắc Bộ (Tập 1 – 5):**
Áo thun henley xám lông chuột dệt waffle + áo khoác dã ngoại canvas rêu quân đội 4 túi hộp + quần cargo kaki be cát + boots da bò sáp cao cổ nâu sẫm + balo phượt 50L. Khi lái xe môtô: Mũ bảo hiểm 3/4 vintage màu xanh rêu nhám viền da nâu, kính chắn gió trong suốt lộ rõ đôi mắt và khẩu hình miệng.

**Giọng nói:** Giọng nam trầm ấm, hào sảng, nói tiếng Việt tự nhiên.

**Prompt lock tiếng Anh (copy nguyên văn):**
```
@Joi = Joi: A handsome 26-year-old European man, 185cm tall, broad shoulders with athletic muscular build. Rugged jawline, neat 3mm stubble beard, warm steel-blue eyes, messy wavy dirty-blonde/light brown hair. Charcoal grey waffle long-sleeve henley shirt under an olive army-green heavy canvas field jacket with utility flap pockets, relaxed sand beige cargo pants, dark brown waxed leather heritage work boots, 50L dark olive expedition backpack. When riding motorcycle: wears matte olive green 3/4 vintage open-face helmet with brown leather trim and clear visor showing full face and lips. Rugged, protective, masculine, deeply affectionate.
```

---

### 🛵 Xe Mô Tô Scrambler Xuyên Việt

Môtô Scrambler cổ điển 400cc màu xám xi măng nhám, yên da bò nâu bò chần quả trám, cờ đỏ sao vàng mini sau đuôi xe tung bay trong gió, hai bên hông xe treo hai túi da chống nước màu nâu cà phê.

---

## IV. 🎬 BẢNG TRẠNG THÁI ĐẠO CỤ MŨ BẢO HIỂM THEO BỐI CẢNH (HELMET STATE MATRIX)

> Dùng bảng này để kiểm tra logic đạo cụ mũ bảo hiểm cho từng loại cảnh trong mỗi clip.

| Loại bối cảnh | Trạng thái mũ bảo hiểm | Hành động chuyển tiếp bắt buộc |
|---|---|---|
| **Đang lái xe trên đường** | ĐỘI trên đầu, cài quai, kính trong suốt gạt mở nhẹ | — |
| **Vừa dừng xe, tham quan** | ĐỘI trên đầu (kính đẩy cao trên trán) | Khi rời xe đi bộ: bấm nhả quai → nhấc mũ → cầm tay/móc ghi-đông |
| **Trong quán ăn / nhà sàn** | ĐẶT trên bàn gỗ / giá gỗ cạnh cửa | Khi ra: nhấc mũ từ bàn/giá → cầm tay → bước ra xe |
| **Trên thuyền / sông nước** | MÓC trên ghi-đông xe ở bến (không mang theo) + mặc áo phao cam | — |
| **Ngắm hoàng hôn / tham quan cố định** | MÓC trên ghi-đông xe gần đó | Khi chuẩn bị lái xe: nhấc mũ từ ghi-đông → đội → cài quai |

**NGUYÊN TẮC VÀNG:** Mũ không bao giờ "tự xuất hiện" hay "tự biến mất". Luôn phải có hành động vật lý rõ ràng: LẤY → ĐỘI → CÀI hoặc NHẢ → THÁO → ĐẶT/MÓC.

---

## V. 📐 TEMPLATE CẤU TRÚC PROMPT CHO MỖI CLIP (BẮT BUỘC TUÂN THỦ)

### Template Clip 1 (Mở Màn Tập — Flycam):

```markdown
# KỊCH BẢN PHÂN CẢNH ĐẠO DIỄN — TẬP {SỐ} / CLIP 1
**DỰ ÁN:** SERIES TIKTOK 365 NGÀY VIỆT NAM  
**PHÂN ĐOẠN:** TẬP {SỐ} — {TÊN TỈNH}: {TIÊU ĐỀ}  
**MÃ PHÂN CẢNH:** {MÃ}-C01 ({ĐỊA ĐIỂM})  
**THỜI LƯỢNG:** ĐÚNG 10 GIÂY (SINGLE CONTINUOUS SHOT)  
**QUY CÁCH HÌNH ẢNH:** KHUNG HÌNH DỌC 9:16 | 24 FPS | CINEMATIC 35MM {PHONG CÁCH}  

---

### [BỘ QUY TẮC ĐẠO DIỄN BẮT BUỘC — DIRECTORIAL LAWS]
{Copy 5-6 quy tắc quan trọng nhất từ mục II, tùy chỉnh mô tả context cho cảnh}

---

### [THIẾT LẬP BỐI CẢNH & ĐẠO CỤ — SCENE SETUP & PROPS CONTINUITY]
- **ĐỊA ĐIỂM:** {Mô tả chi tiết}
- **VỊ TRÍ PHƯƠNG TIỆN & ĐẠO CỤ GỐC (00:00):** {Mô tả vị trí xe, mũ bảo hiểm}

---

### [KHÓA NHÂN VẬT — CHARACTER LOCK]
{Copy trang phục & ngoại hình từ mục III, tùy chỉnh trạng thái cho cảnh}

---

### [KỊCH BẢN ĐẠO DIỄN HÀNH ĐỘNG TỪNG GIÂY — 10 GIÂY LIÊN TỤC]

**00:00–00:01.5 | ĐẠI CẢNH FLYCAM**
{Mô tả flycam establishing shot}

**00:01.5–00:04.5 | CẬN CẢNH KHÓA CHẶT @VY (CLOSE-UP SPEAKER LOCK)**
{Thoại @Vy — tối đa ~15 âm tiết cho 3 giây}

**00:04.5–00:07.5 | CẬN CẢNH KHÓA CHẶT @JOI (CLOSE-UP SPEAKER LOCK)**
{Thoại @Joi — tối đa ~14 âm tiết cho 3 giây}

**00:07.5–00:10.0 | ĐỆM HÀNH ĐỘNG VẬT LÝ (SILENT BUFFER & PROP BLOCKING)**
{Tuyệt đối KHÔNG CÓ THOẠI. Hành động đạo cụ vật lý.}

---

### [KHUNG HÌNH CUỐI & MATCH-CUT CHUYỂN TIẾP SANG CLIP 2]
{Mô tả chính xác khung hình cuối, giữ cố định 0.5s}

---

### [LOẠI TRỪ — NEGATIVE PROMPT]
{Liệt kê các lỗi cần tránh, cụ thể cho từng cảnh}
```

### Template Clip 2–7 (Các clip tiếp theo — Match-cut):

```markdown
# KỊCH BẢN PHÂN CẢNH ĐẠO DIỄN — TẬP {SỐ} / CLIP {SỐ CLIP}
{... header giống Clip 1 ...}

---

### [BỘ QUY TẮC ĐẠO DIỄN BẮT BUỘC — DIRECTORIAL LAWS]
{Copy quy tắc, KHÔNG có flycam, thay bằng match-cut nối cảnh}

---

### [THIẾT LẬP BỐI CẢNH & ĐẠO CỤ — SCENE SETUP & PROPS CONTINUITY]
{TRẠNG THÁI ĐẠO CỤ BAN ĐẦU (00:00): phải khớp 100% với khung hình cuối clip trước}

---

### [KỊCH BẢN ĐẠO DIỄN HÀNH ĐỘNG TỪNG GIÂY — 10 GIÂY LIÊN TỤC]

**00:00–00:03.0 | TIẾP NỐI HÀNH ĐỘNG MATCH-CUT TỪ CLIP {N-1}**
{Nối cảnh — KHÔNG lặp lại flycam}

**00:03.0–00:05.5 | CẬN CẢNH KHÓA CHẶT @{NGƯỜI NÓI 1} (CLOSE-UP SPEAKER LOCK)**
{Thoại — tối đa ~12 âm tiết cho 2.5 giây}

**00:05.5–00:07.5 | CẬN CẢNH KHÓA CHẶT @{NGƯỜI NÓI 2} (CLOSE-UP SPEAKER LOCK)**
{Thoại — tối đa ~9 âm tiết cho 2 giây}

**00:07.5–00:10.0 | ĐỆM HÀNH ĐỘNG VẬT LÝ (SILENT BUFFER & PROP BLOCKING)**
{Tuyệt đối KHÔNG CÓ THOẠI. Hành động đạo cụ.}

---

### [KHUNG HÌNH CUỐI & MATCH-CUT CHUYỂN TIẾP SANG CLIP {N+1}]
{Khung hình cuối, giữ cố định 0.5s}

---

### [LOẠI TRỪ — NEGATIVE PROMPT]
{Liệt kê lỗi cần tránh}
```

---

## VI. 🎙️ QUY TẮC THOẠI & GIỌNG NÓI (DIALOGUE & VOICE RULES)

| Quy tắc | Chi tiết |
|---|---|
| **Ngôn ngữ thoại** | 100% tiếng Việt, giọng chuẩn miền Nam thân thiện |
| **Giọng @Vy** | Nữ trong trẻo, ngọt ngào, háo hức, phát âm chuẩn thanh điệu tiếng Việt |
| **Giọng @Joi** | Nam trầm ấm, hào sảng, nói tiếng Việt tự nhiên như người bản xứ |
| **Tốc độ thoại** | Tối đa 4.5 âm tiết/giây. Một câu thoại ≤ 15 âm tiết |
| **Thoại dứt điểm** | Luôn kết thúc ở giây `00:07.5`, KHÔNG BAO GIỜ kéo vào vùng 00:07.5–00:10 |
| **Ai nói → Camera khóa ai** | @Vy nói → cam khóa cận mặt @Vy. @Joi nói → cam khóa cận mặt @Joi. TUYỆT ĐỐI |
| **Xưng hô** | @Vy gọi @Joi: "anh ơi", "anh". @Joi gọi @Vy: "em à", "em". Gọi khán giả: "cả nhà", "mọi người", "tụi mình" |
| **Cấm** | Cấm voiceover, cấm giới thiệu tên ("mình là Vy", "đây là Joi"), cấm nói lệch khẩu hình |

---

## VII. 📍 DANH SÁCH ĐỊA DANH VIẾT HOA CHUẨN (MASTER PLACE NAME REGISTRY)

### Chặng 1: Đông Bắc Bộ (Tập 1–5)
- **Tập 1 (Hà Giang):** Cột Cờ Lũng Cú, Đồng Văn, Phố Cổ Đồng Văn, Đèo Mã Pí Lèng, Hẻm Tu Sản, Sông Nho Quế, Làng Pả Vi, Mèo Vạc, Hà Giang
- **Tập 2 (Cao Bằng):** Thác Bản Giốc, Sông Quây Sơn, Trùng Khánh, Pác Bó, Suối Lê Nin, Đèo Mã Phục, Cao Bằng
- **Tập 3 (Bắc Kạn):** Hồ Ba Bể, Sông Năng, Hang Động Puông, Bản Pác Ngòi, Đảo Bà Góa, Bắc Kạn
- **Tập 4 (Lạng Sơn):** Ải Chi Lăng, Động Tam Thanh, Nàng Tô Thị, Chợ Đêm Kỳ Lừa, Cột Cờ Phai Vệ, Lạng Sơn
- **Tập 5 (Tuyên Quang):** Na Hang, Cọc Vài Phạ, Thác Khuổi Nhi, Bản Nà Tông, Cây Đa Tân Trào, Chiêm Hóa, Tuyên Quang

---

## VIII. 🗺️ BẢNG LỘ TRÌNH 365 NGÀY (TỔNG QUAN 8 CHẶNG)

| Chặng | Thời gian | Cung đường & Tỉnh thành | Tập tương ứng |
| :--- | :--- | :--- | :--- |
| **1** | Ngày 1 – 45 | Cực Bắc & Đông Bắc Bộ (Hà Giang, Cao Bằng, Bắc Kạn, Lạng Sơn, Tuyên Quang, Thái Nguyên...) | Tập 1 – 5 (đã lên kịch bản) |
| **2** | Ngày 46 – 90 | Tây Bắc (Lào Cai, Yên Bái, Lai Châu, Điện Biên, Sơn La, Hòa Bình) | Tập 6 – 10 |
| **3** | Ngày 91 – 140 | Hà Nội & Vùng Vịnh Di Sản (Hà Nội, Quảng Ninh, Hải Phòng, Ninh Bình) | Tập 11 – 15 |
| **4** | Ngày 141 – 190 | Bắc Trung Bộ (Thanh Hóa, Nghệ An, Hà Tĩnh, Quảng Bình, Quảng Trị, Huế) | Tập 16 – 20 |
| **5** | Ngày 191 – 245 | Nam Trung Bộ (Đà Nẵng, Quảng Nam, Bình Định, Phú Yên, Khánh Hòa, Ninh Thuận, Bình Thuận) | Tập 21 – 28 |
| **6** | Ngày 246 – 285 | Tây Nguyên (Kon Tum, Gia Lai, Đắk Lắk, Đắk Nông, Lâm Đồng) | Tập 29 – 33 |
| **7** | Ngày 286 – 325 | Đông Nam Bộ (TP.HCM, Đồng Nai, Tây Ninh, Bà Rịa - Vũng Tàu) | Tập 34 – 38 |
| **8** | Ngày 326 – 365 | Miền Tây & Cực Nam (Cần Thơ, An Giang, Kiên Giang, Bạc Liêu, Cà Mau) | Tập 39 – 45 |

---

## IX. ✅ BẢNG TRẠNG THÁI CÁC TẬP ĐÃ HOÀN THÀNH

| Tập | Tỉnh | Số clips | Trạng thái | Khung hình cuối (để nối sang tập tiếp theo) |
|:---:|---|:---:|:---:|---|
| **1** | Hà Giang | 7 | ✅ HOÀN THÀNH | Scrambler chở 2 người đội mũ 3/4 lăn bánh rời Mèo Vạc trong hoàng hôn → hướng Cao Bằng |
| **2** | Cao Bằng | 6 | ✅ HOÀN THÀNH | Scrambler chở 2 người đội mũ 3/4 (kính xuống) lăn bánh rời Đèo Mã Phục hoàng hôn → hướng Bắc Kạn |
| **3** | Bắc Kạn | 6 | 📋 OUTLINE | — |
| **4** | Lạng Sơn | 6 | 📋 OUTLINE | — |
| **5** | Tuyên Quang | 7 | 📋 OUTLINE | — |

---

## X. 🎵 PHONG CÁCH NHẠC NỀN THEO VÙNG MIỀN

| Vùng miền | Nhạc cụ dân tộc đặc trưng | Phong cách phối |
|---|---|---|
| Đông Bắc Bộ (Tập 1-5) | Sáo Mèo, Khèn H'Mông, Đàn Tính Tày | Acoustic Folk + Indie hiện đại |
| Tây Bắc (Tập 6-10) | Sáo trúc, Khèn bè Thái, Tính tẩu | Cinematic Folk + Ambient |
| Đồng bằng Bắc Bộ (Tập 11-15) | Đàn bầu, Đàn tranh, Sáo trúc | Lo-fi Jazz + Acoustic Pop |

---

## XI. 📏 CHECKLIST KIỂM TRA TRƯỚC KHI XÁC NHẬN HOÀN THÀNH MỖI CLIP

- [ ] Thoại dứt điểm ở 00:07.5, 2.5 giây cuối hoàn toàn im lặng
- [ ] Camera khóa chặt cận mặt đúng người đang nói (không quay cảnh vật khi có thoại)
- [ ] Mũ bảo hiểm có nguồn gốc vật lý rõ ràng (không tự xuất hiện/biến mất)
- [ ] Khi lái xe → đội mũ; khi vào quán/thuyền → tháo mũ (có hành động tháo/đặt)
- [ ] Tất cả địa danh viết hoa chuẩn tiếng Việt
- [ ] Trang phục nhân vật khớp 100% với KHÓA NHÂN VẬT (mục III)
- [ ] Khung hình cuối clip N = khung hình đầu clip N+1 (match-cut)
- [ ] Số âm tiết thoại ≤ 4.5 âm tiết/giây
- [ ] Không có voiceover, không desync, không phụ đề, không chữ, không watermark
- [ ] Không giới thiệu tên nhân vật ("mình là Vy"...), không thẻ tên, không profile card
- [ ] Giọng @Vy = nữ trong trẻo ngọt ngào; Giọng @Joi = nam trầm ấm hào sảng
- [ ] Single continuous shot — không cắt góc đột ngột trong 10 giây
