# Mai Hoa Thung — Lân Chợ Lớn — Prompt Google Flow (Gemini Omni)

> Quy trình, thiết lập, lỗi thường gặp: xem [../FLOW_GUIDE.md](../FLOW_GUIDE.md) · Kế hoạch series: [README.md](README.md) · Kịch bản tổng: [KICH_BAN_60_PHUT.md](KICH_BAN_60_PHUT.md)

**Định dạng:** **một phim liền 60 phút** (360 clip × 10 s) đăng YouTube, chia thành **60 cảnh** (`canh-01` … `canh-60`), mỗi cảnh đúng 60 giây và cắt đăng TikTok được ngay · tạo bằng **Gemini Omni** trong Google Flow · **16:9** · thoại tiếng Việt giọng miền Nam · không chữ trên video · **hình người thật kiểu phim võ thuật điện ảnh**: đồ đoàn lân lụa đỏ, đầu lân thật, trống thật, đánh tay không, dây lụa, côn gỗ.

**Thế giới:** Chợ Lớn, những ngày giáp Tết. **Nghĩa Hòa Đường** là đoàn lân trăm tuổi của **Sư phụ Tư Lân**, đóng ở gác gỗ cạnh Miếu Bà. Năm người trẻ sống với đoàn như một nhà: Long, Mai, Phúc, Tí, và sau này là Hân. **Hắc Hổ Đường** của **Lý Hổ** (đại đệ tử bị đuổi 15 năm trước) dùng vỏ bọc đoàn lân để thu tiền bảo kê và ép dân phố ký giấy bán đất. Hắc Hổ cướp **Đầu Lân Tổ**; theo **lời thề tổ**, hai đoàn phải phân cao thấp trên **Mai Hoa Thung** ngày mùng 3 Tết, đoàn thua phải giải tán. Câu của đoàn: **"Lân nằm ở tim!"**

**Xương sống mỗi cảnh:** 2 giây đầu là hook; giữa cảnh là hành động hoặc cảm xúc chính; cuối cảnh có cú lật hoặc câu móc sang cảnh sau. Clip 1 của mỗi cảnh mở bằng Ingredients để neo lại mặt nhân vật.

- **Gia đình là trái tim:** cảnh nào cũng có một khoảnh khắc thương nhau (tô hủ tiếu, cái vỗ vai, câu nói về thầy). Phúc nấu cho cả đoàn.
- **Thoại ngắn:** mỗi câu tối đa khoảng 10 âm tiết, không quá 4,5 âm tiết mỗi giây, mỗi clip tối đa khoảng 31 âm tiết. Ai nói thì máy thấy rõ mặt người đó; Long nói **trước hoặc sau** khi chui vào đầu lân.
- **Quay như phim:** mỗi prompt có khối `[CAMERA & LIGHT]` và `[SHOT LIST]` chia nhịp 1–2,5 giây, mỗi nhịp một động tác (một cú đá, một cú né, một cú nhảy cột). Mỗi pha có một nhịp quay chậm làm điểm nhấn.
- **Cảnh nối nhau hợp lý:** mỗi clip bắt đầu đúng chỗ clip trước dừng; cắt cảnh chỉ khi đổi địa điểm hoặc nhảy thời gian.

**Luật, an toàn, chính sách (bắt buộc, đã chặn trong [AVOID]):**
- **Không súng, không dao, không máu, không lửa lớn**, không vết thương hở, không ai chết. Kẻ xấu bị đánh ngã, bị khóa tay, rồi bàn giao cho công an phường (đồng phục không chữ, không phù hiệu đọc được).
- **Xe máy** chỉ chạy trong hẻm vắng, luôn đội mũ bảo hiểm; **ghe** trên kênh đi chậm, có áo phao.
- **Không giống thương hiệu hay phim có sẵn:** đầu lân, tên đoàn, câu hô là sáng tác mới; biển hiệu, cờ, giấy tờ không chữ đọc được.
- **Nhãn AI:** bản TikTok bật nhãn **Nội dung do AI tạo**, bản YouTube khai báo **nội dung tổng hợp**; caption ghi "Phim hư cấu do AI tạo".

**Cách dán prompt:** mỗi file `clip-{số}.md` là một lần dán. **FULL LOCK** dùng ở clip mở bằng Ingredients và cho nhân vật mới vào giữa chuỗi; **SHORT LOCK** dùng ở clip làm bằng Frames hoặc Extend. Hân có **ba khóa** theo ba giai đoạn (đen Hắc Hổ · đen trơn khăn đỏ · đỏ Nghĩa Hòa).

---

## 1. Khóa nhân vật

**Tên nhân vật trên Flow:** `@Long` · `@Mai` · `@Phuc` · `@Ti` · `@Han`. Trong phần còn lại của prompt gọi là LONG · MAI · PHÚC · TÍ · HÂN. Sư phụ Tư Lân, Lý Hổ, Bà Tám và đàn em Hắc Hổ được mô tả bằng chữ (có ảnh tham chiếu `REF_…` đính kèm khi cần).

**Đồng phục Nghĩa Hòa (mặc định mọi cảnh):** áo võ lụa đỏ thẫm cổ tàu, nút thắt và viền vàng, quần vải đen rộng, đai lụa đỏ, giày vải trắng. **Thường phục** chỉ ở bệnh viện (Cảnh 11, 24, 39) và bến xe (Cảnh 31, 32).

### Long "Đầu Lân" — trưởng đoàn, người cầm đầu lân

FULL LOCK — đồ đoàn
```text
@Long = LONG (28, head of the lion and new leader of the Nghĩa Hòa troupe): a real Vietnamese man, about 175 cm tall, lean wiry acrobatic build, sharp focused dark eyes, calm face, black hair in an undercut with a small top knot, a small jade pendant shaped like a lion's tooth on a red cord around his neck (signature detail). Troupe outfit: a crimson silk kung-fu jacket with gold frog buttons and gold trim, loose black trousers, a red silk sash, white cloth kung-fu shoes. Voice: low, steady, warm Southern Vietnamese male voice, late 20s.
```
SHORT LOCK — đồ đoàn
```text
@Long = LONG: Vietnamese man, 28, undercut with a small top knot, jade lion-tooth pendant on a red cord, crimson silk kung-fu jacket with gold trim, red sash; low, steady Southern male voice.
```
FULL LOCK — thường phục (Cảnh 11, 24, 31, 32, 39)
```text
@Long = LONG in civilian clothes: the same man (undercut with a small top knot, jade lion-tooth pendant on a red cord) in a plain grey T-shirt, black jeans and white sneakers. Voice: low, steady, warm Southern Vietnamese male voice.
```
SHORT LOCK — thường phục
```text
@Long = LONG in civilian clothes: 28, top knot, jade lion-tooth pendant, grey T-shirt, black jeans; low, steady Southern male voice.
```

### Mai "Đuôi Lân" — người cầm đuôi lân, nhào lộn, dây lụa

FULL LOCK — đồ đoàn
```text
@Mai = MAI (24, tail of the lion and acrobat of the troupe): a real Vietnamese woman, about 160 cm tall, petite gymnast build, bright playful eyes, light freckles across her nose, black hair in two braids tied with red thread (signature detail). Troupe outfit: a crimson silk kung-fu jacket with gold trim, loose black trousers, a red silk sash, white cloth shoes, a long red silk ribbon wound around her LEFT wrist that she uses as a whip-like ribbon. Voice: quick, bright, teasing Southern Vietnamese female voice, mid-20s.
```
SHORT LOCK — đồ đoàn
```text
@Mai = MAI: Vietnamese woman, 24, two braids tied with red thread, freckles, crimson kung-fu jacket, red silk ribbon on her LEFT wrist; quick, bright Southern female voice.
```
FULL LOCK — thường phục
```text
@Mai = MAI in civilian clothes: the same woman (two braids tied with red thread, freckles) in a white T-shirt, a denim jacket, black leggings and sneakers. Voice: quick, bright, teasing Southern Vietnamese female voice.
```
SHORT LOCK — thường phục
```text
@Mai = MAI in civilian clothes: 24, two braids with red thread, denim jacket over a white T-shirt; quick, bright Southern female voice.
```

### Phúc "Trống" — tay trống, người nấu ăn, cựu võ sĩ quyền anh

FULL LOCK — đồ đoàn
```text
@Phuc = PHÚC (30, the troupe's drummer, cook and former boxer): a real Vietnamese man, about 185 cm tall, big broad-shouldered and barrel-chested, completely shaved head (signature detail), thick black eyebrows, warm wide grin. Troupe outfit: a sleeveless crimson silk kung-fu vest with gold trim showing thick arms, loose black trousers, a red silk sash with two wooden drum sticks tucked into it, white cloth shoes. Voice: big, booming, warm Southern Vietnamese male voice, early 30s.
```
SHORT LOCK — đồ đoàn
```text
@Phuc = PHÚC: very big Vietnamese man, 30, shaved head, thick eyebrows, sleeveless crimson vest, two drum sticks in his red sash; booming, warm Southern male voice.
```
FULL LOCK — thường phục
```text
@Phuc = PHÚC in civilian clothes: the same big shaved-headed man in a black polo shirt, grey trousers and sandals. Voice: big, booming, warm Southern Vietnamese male voice.
```
SHORT LOCK — thường phục
```text
@Phuc = PHÚC in civilian clothes: 30, very big, shaved head, black polo shirt; booming, warm Southern male voice.
```

### Tí "Ông Địa" — út đoàn, diễn Ông Địa, parkour, gây cười

FULL LOCK — đồ đoàn
```text
@Ti = TÍ (19, the youngest of the troupe, who plays the laughing Ông Địa character): a real Vietnamese young man, about 168 cm tall, skinny and springy, copper-dyed fringe over black hair (signature detail), a gap-toothed cheeky grin. Troupe outfit: a crimson silk kung-fu jacket with gold trim, loose black trousers, a red sash, sneakers, a round paper fan always in his hand; a round pink smiling Ông Địa mask pushed up on top of his head so his face stays fully visible. Voice: high, fast, cheeky Southern Vietnamese male voice, late teens.
```
SHORT LOCK — đồ đoàn
```text
@Ti = TÍ: skinny Vietnamese young man, 19, copper-dyed fringe, gap-toothed grin, crimson kung-fu jacket, paper fan in hand, pink Ông Địa mask pushed up on his head; high, fast, cheeky Southern male voice.
```
FULL LOCK — thường phục
```text
@Ti = TÍ in civilian clothes: the same skinny young man (copper-dyed fringe, gap-toothed grin) in an oversized black hoodie, shorts and sneakers, paper fan in his hand. Voice: high, fast, cheeky Southern Vietnamese male voice.
```
SHORT LOCK — thường phục
```text
@Ti = TÍ in civilian clothes: 19, copper fringe, oversized black hoodie, paper fan; high, fast, cheeky Southern male voice.
```

### Hân "Song Côn" — võ sĩ Hắc Hổ bỏ hàng ngũ (xuất hiện từ Cảnh 7)

FULL LOCK — đồ Hắc Hổ (Cảnh 7 – 27)
```text
@Han = HÂN (27, a fighter of the Hắc Hổ troupe): a real Vietnamese woman, about 168 cm tall, athletic, serious almond eyes, short black hair with a single shaved line above her LEFT ear (signature detail). Hắc Hổ outfit: a black kung-fu jacket with gold tiger stripes on the sleeves, black trousers, a black sash, black cloth shoes, two short rattan sticks in her sash. Voice: low, cool, clipped Southern Vietnamese female voice, late 20s.
```
SHORT LOCK — đồ Hắc Hổ
```text
@Han = HÂN: Vietnamese woman, 27, short hair with a shaved line above her LEFT ear, black kung-fu jacket with gold tiger stripes, two rattan sticks in her sash; low, cool Southern female voice.
```
FULL LOCK — đồ tạm của đoàn (Cảnh 28 – 58)
```text
@Han = HÂN in borrowed troupe clothes: the same woman (short hair with a shaved line above her LEFT ear) in a plain black kung-fu jacket with no stripes, black trousers, a red bandana tied around her neck, two short rattan sticks in a black sash. Voice: low, cool, clipped Southern Vietnamese female voice.
```
SHORT LOCK — đồ tạm
```text
@Han = HÂN: 27, shaved line above her LEFT ear, plain black kung-fu jacket, red bandana around her neck, two rattan sticks; low, cool Southern female voice.
```
FULL LOCK — đồ Nghĩa Hòa (Cảnh 59 – 60)
```text
@Han = HÂN in the Nghĩa Hòa troupe outfit: the same woman (short hair with a shaved line above her LEFT ear) in a crimson silk kung-fu jacket with gold trim, black trousers, a red sash, two short rattan sticks in her sash, a soft proud smile. Voice: low, cool, clipped Southern Vietnamese female voice.
```
SHORT LOCK — đồ Nghĩa Hòa
```text
@Han = HÂN: 27, shaved line above her LEFT ear, crimson kung-fu jacket with gold trim, two rattan sticks in her red sash; low, cool Southern female voice.
```

### Nhân vật phụ (mô tả bằng chữ, đính ảnh REF khi cần)

```text
SƯ PHỤ TƯ LÂN (70, master of the Nghĩa Hòa troupe): a slim elderly Vietnamese man with cropped white hair, a short white goatee, kind deeply lined face, in a dark-blue Chinese-style long jacket with cloth buttons, black trousers, cloth shoes, leaning on a wooden cane with a carved lion-head handle. Voice: warm, slow, elderly Southern Vietnamese male voice.
```
```text
LÝ HỔ (45, boss of the Hắc Hổ troupe, the master's expelled first disciple): a tall Vietnamese man with slicked-back black hair greying at the temples, cold narrow eyes, a scar cutting through his LEFT eyebrow (signature detail), in a black silk kung-fu jacket with gold tiger stripes, black trousers, gold rings, a black lacquered tiger-face mask pushed up on his forehead. Voice: deep, cold, unhurried Southern Vietnamese male voice.
```
```text
HẮC HỔ HENCHMEN: men in identical black kung-fu outfits with gold tiger stripes, black tiger-face masks covering their whole faces, wooden staffs; they never speak.
```
```text
BÀ TÁM (62, lantern maker and lion-head artisan): a plump elderly Vietnamese woman with a grey bun, reading glasses on a beaded chain, a floral apron over a brown blouse, hands stained with paint and glue. Voice: warm, chatty, elderly Southern Vietnamese female voice.
```

Khóa ngắn:
```text
SƯ PHỤ TƯ LÂN: 70, cropped white hair, white goatee, dark-blue long jacket, lion-head cane; warm elderly Southern voice.
LÝ HỔ: 45, slicked-back greying hair, scar through his LEFT eyebrow, black silk jacket with gold tiger stripes, tiger mask on his forehead; deep, cold Southern voice.
HẮC HỔ HENCHMEN: black outfits with gold tiger stripes, full black tiger masks, wooden staffs, silent.
BÀ TÁM: 62, grey bun, reading glasses on a chain, floral apron; warm chatty elderly Southern voice.
```

## 2. Khóa đạo cụ

```text
LÂN TỔ (the ancestral lion head, 100 years old): a classic Southern lion-dance head, faded crimson and antique gold, long white fur beard and eyebrows, big mirrored eyes that blink, a black-lacquered horn with a red ribbon, one jade tooth missing from its upper jaw; a red-gold scaled cloth body with white fur trim.
LÂN MỚI (the new lion head the troupe builds): a bright crimson-and-gold lion-dance head with white fur beard, green mirrored eyes, a gold horn with a red ribbon, hand-painted gold swirls still fresh; a red-gold scaled cloth body.
LÂN HẮC HỔ (the Hắc Hổ lion): a black lion-dance head with silver stripes, red mirrored eyes, a black fur beard; a black-and-silver cloth body.
TRỐNG TỔ (the ancestral drum): a big red lacquered lion-dance drum with brass studs and a worn hide, on a wooden stand, with a faded gold lion painted on its side.
MAI HOA THUNG (the plum-blossom poles): twenty-one red-painted steel poles of different heights from one to three metres, each topped with a round steel pad, arranged in a plum-blossom pattern on a square in front of the temple, with safety mats below.
```

## 3. Bối cảnh (không chữ đọc được)

```text
TEMPLE SQUARE: a small old temple with a curved tile roof, hanging coils of incense, a red-brick courtyard with an old apricot-blossom tree, red lanterns, a wooden rack holding lion heads and a big drum; Chợ Lớn alley houses around it.
TROUPE LOFT: a wooden loft above an alley hung with lion heads, drums and cymbals, a long wooden dining table, a small kitchen with a steaming noodle pot, warm tungsten bulbs, a small altar with a black-and-white photo.
LANTERN ALLEY & WORKSHOP: a long narrow alley roofed with hundreds of red lanterns; at its end a cluttered workshop with bamboo frames, paper, glue pots, paint and half-finished lion heads.
BÌNH TÂY MARKET (fictional): a huge old market with tiled roofs, aisles of fabric, candied fruit and lantern stalls, crowds blurred in the background, no readable signs.
TÀU HỦ CANAL: a dark city canal with small wooden boats, an old iron bridge, lantern reflections on the water, life jackets hanging on the boats.
ICE FACTORY: a cold industrial ice factory with fog, huge ice blocks, chains and hooks, wet slippery concrete, green fluorescent light.
OLD KILN: an abandoned brick kiln yard with rows of clay jars, dust, a round brick kiln with its door open and no fire.
CHỢ LỚN ROOFTOPS: old tile roofs, water tanks, tangled wires, strings of red lanterns, the night city glowing beyond.
HOSPITAL ROOM: a simple hospital room, white sheets, a window with afternoon light, a bedside stool with a bowl of soup.
BUS STATION AT NIGHT: a provincial bus station, sleeper buses, plastic chairs, fluorescent light, a vendor cart.
FESTIVAL SQUARE: the square in front of the temple on the third day of Tết, the Mai Hoa Thung poles in the centre, bamboo stands full of blurred spectators, red flags, big drums, afternoon sun.
HẮC HỔ HALL: a dim martial-arts hall with black-and-gold banners without text, a black lion head on an altar, a wooden desk piled with folders.
```

## 4. [FORMAT] và [AVOID] dùng chung

Mở clip Ingredients:
```text
[FORMAT]
Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action martial-arts blockbuster film style set in Saigon's Chợ Lớn at Tết. 24fps high-budget cinematography, crisp 90-degree shutter angle capturing razor-sharp kinetic motion with zero blurry artifacts. Rich red-and-gold Tết colour grade with warm lantern light. No guns, no blades anywhere. Dialogue in Vietnamese with natural Southern accent and lip-sync. No subtitles or on-screen text.
```
Mở clip Frames / Extend:
```text
Continue the scene seamlessly from the final frame of clip N-1, which is the first frame of this clip. Same characters, outfits, props, lighting, and 16:9 cinematic widescreen framing. Flawless continuity with zero jump cut.
```
Chặn cuối:
```text
[AVOID]
guns, firearms, knives, blades, blood, gore, visible wounds, deaths, large fire, real brand logos, readable signs or documents, watermarks, text overlays, extra fingers, cartoon or anime look, slow sluggish motion, blurry motion smear.
```

## 5. Prompt tạo ảnh tham chiếu (Nano Banana Pro, 16:9 hoặc 3:4)

Tạo mỗi nhân vật một ảnh toàn thân nền xám trơn, ánh sáng studio dịu, rồi đặt tên nhân vật trên Flow đúng như bảng ở mục 1.

```text
REF @Long: Full-body photorealistic character reference of a 28-year-old Vietnamese man, 175 cm, lean acrobatic build, undercut with a small top knot, sharp calm eyes, a small jade lion-tooth pendant on a red cord, wearing a crimson silk kung-fu jacket with gold frog buttons and gold trim, loose black trousers, red sash, white cloth shoes, standing in a relaxed martial stance; plain grey studio background, soft light, 8K.
REF @Mai: Full-body photorealistic character reference of a 24-year-old Vietnamese woman, 160 cm, petite gymnast build, two black braids tied with red thread, freckles, bright playful smile, crimson silk kung-fu jacket with gold trim, black trousers, red sash, a long red silk ribbon wound around her left wrist; plain grey studio background, soft light, 8K.
REF @Phuc: Full-body photorealistic character reference of a 30-year-old Vietnamese man, 185 cm, big barrel-chested build, completely shaved head, thick eyebrows, wide warm grin, sleeveless crimson silk vest with gold trim, black trousers, red sash with two wooden drum sticks; plain grey studio background, soft light, 8K.
REF @Ti: Full-body photorealistic character reference of a 19-year-old skinny Vietnamese young man, 168 cm, copper-dyed fringe, gap-toothed grin, crimson silk kung-fu jacket, black trousers, red sash, sneakers, a round paper fan in his hand, a pink smiling Ông Địa mask pushed up on top of his head; plain grey studio background, soft light, 8K.
REF @Han: Full-body photorealistic character reference of a 27-year-old Vietnamese woman, 168 cm, athletic, serious almond eyes, short black hair with a shaved line above her left ear, black kung-fu jacket with gold tiger stripes on the sleeves, black trousers, black sash with two short rattan sticks; plain grey studio background, soft light, 8K.
REF_SuPhu: Full-body photorealistic reference of a slim 70-year-old Vietnamese man, cropped white hair, short white goatee, kind lined face, dark-blue Chinese-style long jacket, black trousers, cloth shoes, a wooden cane with a carved lion-head handle; plain grey studio background, 8K.
REF_LyHo: Full-body photorealistic reference of a tall 45-year-old Vietnamese man, slicked-back hair greying at the temples, cold narrow eyes, a scar through his left eyebrow, black silk kung-fu jacket with gold tiger stripes, gold rings, a black lacquered tiger-face mask pushed up on his forehead; plain grey studio background, 8K.
REF_LanTo: Product-style photo of an antique Southern lion-dance head, faded crimson and gold, long white fur beard and eyebrows, mirrored eyes, black-lacquered horn with a red ribbon, one jade tooth missing from the upper jaw, on a wooden stand; plain grey background, 8K.
REF_LanMoi: Product-style photo of a brand-new crimson-and-gold Southern lion-dance head with white fur beard, green mirrored eyes, gold horn with a red ribbon, fresh hand-painted gold swirls, on a wooden stand; plain grey background, 8K.
REF_LanHacHo: Product-style photo of a black Southern lion-dance head with silver stripes, red mirrored eyes and black fur beard, on a stand; plain grey background, 8K.
```
