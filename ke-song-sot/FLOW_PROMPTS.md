# Kẻ Sống Sót — Bóng Ma — Prompt Google Flow (Gemini Omni)

> Quy trình chung: [../FLOW_GUIDE.md](../FLOW_GUIDE.md) · Kế hoạch và phân tích phim gốc: [README.md](README.md) · Kịch bản tổng: [KICH_BAN_60_PHUT.md](KICH_BAN_60_PHUT.md) · Hồ sơ tính cách và prompt ảnh: [NHAN_VAT.md](NHAN_VAT.md)

**Định dạng:** một phim liền **60 phút** (360 clip × 10 s), **60 cảnh** đúng 60 giây, **16:9**, Gemini Omni, thoại tiếng Việt giọng miền Nam, không chữ trên hình. **Phim noir hành động tâm lý**: kể bằng lời dẫn của sát thủ, hiện tại và quá khứ đan xen; màu hiện tại là thị trấn biển bạc nắng, màu quá khứ là thành phố đêm ám vàng.

**Thế giới:** **Sơn "Bóng Ma"**, sát thủ hợp đồng nổi tiếng của đường dây **Rắn Đen** chuyên thuốc **Tê** (chất gây liệt toàn thân, nhìn như chết). Hợp đồng cuối: hạ doanh nhân **Vũ Kiên**. Trong lúc theo dõi mục tiêu, Sơn gặp **Hạ**, cô chủ tiệm hoa dưới tòa nhà của Kiên; Hạ xin anh bỏ nghề đi cùng cô, anh từ chối. Hợp đồng đổ bể, Rắn Đen phản bội, Hạ bị bắt và bị giết. Sơn trốn về **Hòn Sóng**, thị trấn biển nhỏ, thuê căn nhà gỗ ven rừng dương, tự cho mình **bảy ngày** để phơi bày sổ tiền của Rắn Đen; ngày thứ bảy không xong thì anh không chạy nữa. **Đại úy Mây**, trưởng công an thị trấn, nhận ra người lạ không phải khách du lịch. Một **Người Môi Giới** giấu mặt kéo anh trở lại nghề bằng một hợp đồng cuối. Câu của phim: **"Bóng ma không chết. Bóng ma chỉ hết việc."**

**Xương sống mỗi cảnh:** 2 giây đầu là hook; giữa cảnh là một mối đe dọa, một manh mối hoặc một mảnh quá khứ; cuối cảnh có cú lật hoặc câu móc. Clip mở bằng "Quá khứ:" là cắt về thành phố đêm, dán ở Ingredients với khóa **đồ quá khứ**.

- **Lời dẫn:** Sơn kể ở ngôi thứ nhất, câu ngắn, lạnh, không quá 10 âm tiết một câu; mỗi cảnh tối đa 2 câu dẫn (cảnh hồi tưởng được 3).
- **Thoại ngắn:** mỗi câu tối đa khoảng 10 âm tiết, mỗi clip tối đa khoảng 31 âm tiết.
- **Mỗi nhịp một động tác**; mỗi pha có một nhịp quay chậm.

**Luật, an toàn, chính sách (đã chặn trong [AVOID]):**
- **Không máu, không vết thương hở, không ai chết trên hình.** Việc giết người trong quá khứ chỉ hiện qua lời dẫn, ảnh, vỏ đạn, một cánh cửa đóng. Cái chết của Hạ chỉ hiện qua tiệm hoa tan hoang, khăn lụa, băng niêm phong.
- **Súng** chỉ trong bao hoặc giơ lên, **không bắn vào người**; đòn kết thúc là khóa tay, còng, hoặc thuốc Tê (ngủ, không chết).
- **Ma túy:** Tê chỉ mô tả như "lọ thuốc trong", không có cảnh sử dụng để phê; mô tả như thuốc gây liệt dùng làm vũ khí và làm giả cái chết.
- **Không tự sát trên hình, không nói chữ tự sát**: "ngày thứ bảy tôi không chạy nữa".
- **Không nhắc cơ quan có thật, không phù hiệu đọc được;** công an thị trấn là phe tốt. **Không mô phỏng diễn viên thật**, không dùng tên diễn viên của phim gốc.
- **Nhãn AI** trên TikTok và YouTube; caption ghi "phim hư cấu do AI tạo".

**Cách dán:** `clip-{số}.md` là một lần dán. **FULL LOCK** ở clip Ingredients và nhân vật vào giữa chuỗi; **SHORT LOCK** ở Frames / Extend. Sơn có hai khóa: **hiện tại** và **quá khứ**.

---

## 1. Khóa nhân vật

**Tên trên Flow (`0aac1598-f1d9-4de2-84e8-9a5c0edb1df8`):** `@Son` · `@May` · `@Ha` · `@HaiNgoc` · `@Dũng` · `@Vũ Kiên` · `@Phó Thành` · `@Bác sĩ Linh` · `@Ông Bảy`. Trong prompt gọi là SƠN · MÂY · HẠ · BÀ HAI NGỌC · DŨNG "ĐINH" · VŨ KIÊN · PHÓ THÀNH · BÁC SĨ LINH · ÔNG BẢY.

| Nhân vật | Tag trên Flow | `media_id` đã khóa trên Google Flow |
|---|---|---|
| Sơn (Bóng Ma) | `@Son` | `28356180-dea1-4c6c-bd80-8c3a41106957` |
| Đại úy Mây | `@May` | `b210621a-c403-42cb-94d5-8c0024496843` |
| Hạ (Tiệm hoa) | `@Ha` | `61e353d9-8e8a-48b1-934e-2f466ab87d09` |
| Bà Hai Ngọc | `@HaiNgoc` | `ff423460-c3ce-4d3f-8c4b-f74d2a657a2f` |
| Dũng "Đinh" | `@Dũng` | `29967c42-6378-4e6e-a656-101fbda18b0b` |
| Vũ Kiên | `@Vũ Kiên` | `cb559421-6180-43b2-bf78-ecc674c3b698` |
| Phó Thành | `@Phó Thành` | `80289d04-f26d-4ac0-892b-5515509ea1fb` |
| Bác sĩ Linh | `@Bác sĩ Linh` | `d51873af-f5d5-48cd-844e-7d6fc9bf99a7` |
| Ông Bảy | `@Ông Bảy` | `eefba81d-07c5-42a5-bfe3-11bc176c6d4c` |

### Sơn "Bóng Ma" — sát thủ hợp đồng, người kể chuyện

FULL LOCK — hiện tại (Hòn Sóng)
```text
@Son = SƠN (45, a famous contract killer known as "the Ghost", now hiding in a small seaside town): a real Vietnamese man, about 176 cm tall, lean and quiet, cropped black hair greying at the temples, a weathered calm face with deep lines, dark unreadable eyes, a thin old white scar across the bridge of his nose (signature detail), a silver pocket-watch chain hanging from his belt (signature detail). Present-day outfit: a faded olive field jacket over a grey shirt, dark trousers, worn brown boots, no hat. Voice: low, dry, unhurried Southern Vietnamese male voice, mid-40s.
```
SHORT LOCK — hiện tại
```text
@Son = SƠN: Vietnamese man, 45, cropped hair greying at the temples, thin white scar across the bridge of his nose, silver pocket-watch chain on his belt, faded olive field jacket over a grey shirt; low, dry Southern male voice.
```
FULL LOCK — quá khứ (thành phố, trước khi trốn)
```text
@Son = SƠN in the past (45, the Ghost at the height of his trade): the same man (cropped greying hair, thin white scar across the bridge of his nose) in a plain black suit with no tie, white shirt open at the collar, polished black shoes, black leather gloves he takes off slowly, no pocket watch yet. Voice: low, dry, unhurried Southern Vietnamese male voice.
```
SHORT LOCK — quá khứ
```text
@Son = SƠN in the past: 45, cropped greying hair, scar across the bridge of his nose, black suit no tie, white shirt, black gloves; low, dry Southern male voice.
```

### Đại úy Mây — trưởng công an thị trấn Hòn Sóng

FULL LOCK
```text
@May = MÂY (38, head of the small-town police post of Hòn Sóng): a real Vietnamese woman, about 166 cm tall, athletic, sun-lined face, sharp warm eyes, short black hair with a single white streak at the front (signature detail). Outfit: a plain khaki shirt with sleeves rolled, dark trousers, canvas shoes, no badge or readable insignia, a small notebook in her chest pocket; sometimes a dark rain jacket. Voice: firm, dry, slightly amused Southern Vietnamese female voice, late 30s.
```
SHORT LOCK
```text
@May = MÂY: Vietnamese woman, 38, short hair with a white streak at the front, sun-lined face, khaki shirt with rolled sleeves, notebook in her chest pocket, no insignia; firm, dry Southern female voice.
```

### Hạ — cô chủ tiệm hoa, chỉ xuất hiện trong quá khứ

FULL LOCK
```text
@Ha = HẠ (32, a florist in the city, Sơn's lover; appears only in the past): a real Vietnamese woman, about 162 cm tall, slim, gentle bright face, long black hair tied loosely, a pale-blue silk scarf always around her neck or in her hair (signature detail). Outfit: a cream linen dress, a green canvas apron with pockets, flat sandals, flower stems in her hands. Voice: soft, warm, clear Southern Vietnamese female voice, early 30s.
```
SHORT LOCK
```text
@Ha = HẠ: Vietnamese woman, 32, long loose black hair, pale-blue silk scarf, cream linen dress with a green florist apron; soft, warm Southern female voice.
```

### Bà Hai Ngọc — trùm đường dây Rắn Đen

FULL LOCK
```text
@HaiNgoc = BÀ HAI NGỌC (60, matriarch of the Rắn Đen syndicate, owner of a silk shop as a front): a real Vietnamese woman, about 158 cm tall, small and upright, silver hair in a tight bun, powdered calm face, eyes that never blink first, a thick jade bracelet on her LEFT wrist (signature detail), a long black cigarette holder she rarely lights. Outfit: a violet silk áo bà ba with a high collar, black silk trousers, embroidered slippers. Voice: soft, slow, sweet Southern Vietnamese female voice, around 60.
```
SHORT LOCK
```text
@HaiNgoc = BÀ HAI NGỌC: 60, silver bun, powdered calm face, jade bracelet on her LEFT wrist, black cigarette holder, violet silk áo bà ba; soft, slow, sweet Southern female voice.
```

### Nhân vật phụ (5 nhân vật đã tạo trên Flow với `@Tag`)

```text
@Dũng = DŨNG "ĐINH" (35, Rắn Đen's enforcer): a real Vietnamese man, about 180 cm tall, heavy-shouldered, buzz cut, a small nail-shaped silver earring in his LEFT ear (signature detail), a black sleeveless shirt, black jeans, boots, a leather holster that stays closed. Voice: rough, loud Southern Vietnamese male voice.
@Vũ Kiên = VŨ KIÊN (50, construction tycoon, the contract's target): a tall Vietnamese man with slicked black hair, a white tailored suit, gold watch, a wide politician's smile. Voice: smooth, confident Southern Vietnamese male voice.
@Phó Thành = PHÓ THÀNH (26, Mây's young deputy): a skinny Vietnamese man with round glasses, neat side-parted hair, a plain light-blue shirt, eager face, no insignia. Voice: quick, polite Southern Vietnamese male voice.
@Bác sĩ Linh = BÁC SĨ LINH (55, the town doctor): a thin Vietnamese man with grey hair, wire glasses, a worn white coat over a checked shirt. Voice: tired, precise Southern Vietnamese male voice.
@Ông Bảy = ÔNG BẢY (70, owner of the seafront coffee stall): a stout old Vietnamese man with a white moustache, singlet and shorts, conical hat, always wiping a glass. Voice: loud, cheerful elderly Southern voice.
```

## 2. Khóa đạo cụ

```text
ĐỒNG HỒ QUẢ QUÝT (Hạ's pocket watch): an old silver pocket watch on a chain, engraved with a small flower on the lid (no readable text), its glass cracked; Sơn opens it to count days.
KHĂN LỤA XANH (Hạ's pale-blue silk scarf): a long pale-blue silk scarf, soft, slightly torn at one end.
LỌ TÊ (vial of the paralytic): a small clear glass vial with a rubber stopper holding a colourless liquid, kept in a tin box with a syringe; no label.
SỔ ĐEN (the Rắn Đen ledger): a black leather account book with columns of handwritten numbers (not readable) and a USB stick taped inside the back cover.
LỊCH BẢY NGÀY (the seven-day count): seven short lines scratched into the wooden doorframe of the cabin, one crossed each dawn.
```

## 3. Bối cảnh (không chữ đọc được)

```text
CABIN: an old wooden cabin among casuarina pines on a dune above a small seaside town, a sagging porch, a tin roof, a single room with a cot, a table, a radio, scratch marks on the doorframe; wind and sea sound.
HÒN SÓNG TOWN: a small Vietnamese seaside town, one main street, a fishing harbour with wooden boats, a seafront coffee stall under a tarp, a market, a concrete pier, white sun and glare; no readable signs.
POLICE POST: a small-town police post, a tiled front room with a desk, a ceiling fan, a holding room with a barred window, a motorbike outside; no readable insignia.
TOWN CLINIC: a small clinic with a steel bed, glass cabinets, a microscope, green curtains, afternoon light.
CITY NIGHT (past): a big Vietnamese city at night in amber light, glass towers, a parking garage, a rooftop, wet streets, neon reflections; no readable signs.
FLOWER SHOP (past): a small flower shop at the foot of a glass tower, buckets of lilies and roses, a wooden counter, warm bulbs, a back room with a kettle.
SILK SHOP (Rắn Đen front): a dim shop of silk bolts in a city lane, a back office with a teak desk, incense, a safe, a courtyard.
DRUG LAB (Rắn Đen): a hidden lab in a disused fish-sauce factory by the river, steel vats, glass flasks, clear vials on trays, masked workers blurred.
SEA CLIFF & LIGHTHOUSE: a cliff above the town with an old lighthouse, wind, long grass, the sea below.
HARBOUR AT NIGHT: the fishing harbour at night, boats knocking, a single lamp, nets, ice crates.
```

## 4. [FORMAT] và [AVOID] dùng chung

Mở clip Ingredients (hiện tại):
```text
[FORMAT]
Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action neo-noir crime thriller film style set in a small Vietnamese seaside town. 24fps high-budget cinematography, crisp 90-degree shutter angle, razor-sharp motion. Bleached white-sun colour grade with cool shadows for the present day. No blood, no on-screen shooting. Dialogue in Vietnamese with natural Southern accent and lip-sync; first-person narration allowed as voice-over. No subtitles or on-screen text.
```
Mở clip Ingredients (quá khứ): thay câu màu bằng `Warm amber night colour grade with deep shadows for the past.`

Chặn cuối:
```text
[AVOID]
blood, gore, visible wounds, on-screen shooting, muzzle flashes, bullet hits on people, deaths on camera, torture, drug use for pleasure, suicide, knives used on people, real brand logos, readable signs or documents, real police insignia, watermarks, text overlays, extra fingers, cartoon or anime look, slow sluggish motion, blurry motion smear, likeness of any real actor.
```
