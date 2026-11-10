# Tây Du Ký 2026 — Prompt Google Flow (Gemini Omni)

> **🗣️ QUY TẮC GIỌNG (từ 07/11/2026 — ưu tiên cao nhất, thay mọi chỗ ghi "giọng miền Nam" bên dưới):** toàn bộ thoại dùng **giọng Bắc thanh thoát** — giọng Hà Nội chuẩn, nhẹ, rõ, tinh tế. Trong prompt: câu FORMAT ghi "a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent"; mỗi `Voice:` kết thúc bằng "elegant standard Hà Nội Northern Vietnamese accent"; AVOID có "Southern or Central Vietnamese accents". Từ ngữ cũng theo miền Bắc: này/đây, nhé, không, vào, thật, quá/thế, thìa, bát, cốc, lợn, đắt, quả, hoa, nhặt, rơi, xem, gọi (không dùng nè, nghen, hông, vô, thiệt, ghê, muỗng, chén, ly, heo, mắc, trái, lượm, rớt, coi, kêu). Chuẩn viết clip: `flowkit/docs/TIKTOK_PROMPT_SPEC.md`, kiểm tra bằng `python3 flowkit/scripts/check_tiktok_episode.py <thư mục tập>`.


> Quy trình, thiết lập, lỗi thường gặp: xem [../FLOW_GUIDE.md](../FLOW_GUIDE.md)

**Định dạng chuẩn bắt buộc:** **Mỗi tập là CLIP HÀI 60 GIÂY (`6 clip × 10s = 60s`) TỔNG KẾT HOT TREND VÀ DRAMA CỦA NGÀY** · tạo bằng **Gemini Omni** trong Google Flow · 9:16 · hoạt hình 2D · thoại tiếng Việt **tự nhiên như người thật** · không chữ trên video · **bắt buộc tổng hợp các tin hot, xu hướng mạng xã hội và drama ồn ào nhất trong ngày** thành một câu chuyện hài hước liền mạch 60 giây tại nhà trọ hẻm Sài Gòn của 4 thầy trò Đường Tăng (`@Thay`, `@DaiCa`, `@HeoLuoi`, `@UtKho`) và chị chủ `La Sát`.

**Đặt tên file:** video `TDK_T01_C1_v1` (tập 01, clip 1, phiên bản 1) · ảnh tham chiếu `TDK_REF_<TÊN>` (xem mục 4)

---

## Ghi chú tạo hình

README của series mới chỉ có ý tưởng chung, nên tạo hình dưới đây được thiết kế mới và **cố định cho mọi tập**.

- **Ý tưởng:** Thỉnh kinh xong, bốn thầy trò về Sài Gòn năm 2026, thuê chung một căn nhà ống trong hẻm. Mỗi tập là một drama đời thường như ăn vụng, tiền điện, chạy giao hàng, ngày lễ. Phép thuật cổ (gậy Như Ý, Cân Đẩu Vân, quạt Ba Tiêu) bị đem ra dùng vào chuyện vặt để gây cười.
- **Tên nhân vật (theo bản hoạt hình 2D):** Thầy (Đường Tăng) · Đại Ca (Ngộ Không) · Heo Lười (Bát Giới) · Út Khờ (Sa Tăng). Thoại cũng gọi bằng tên này: đồ đệ gọi "Thầy" (gọi to: "Thầy ơi!"), không dùng lại "Sư phụ", "Lão Tôn", "lão Trư", "Đại sư huynh". Tên cũ chỉ còn ở câu mở của Tập 9 (tập ra mắt tên mới).
- **Phong cách hình:** hoạt hình 2D vẽ tay (đổi từ 3D ngày 26/10/2026): nét viền đậm, màu phẳng, đổ bóng cel đơn giản, nền vẽ 2D. Phong cách được khóa ở [FORMAT] của Clip 1 và câu mở đầu Clip 2/3 (mục 3); cuối mọi [AVOID] có câu chặn hình 3D/CGI. Chỉ đính ảnh nhân vật bản 2D.
- **Tạo hình gốc, không sao chép phim:** không dùng trang phục hay gương mặt của phim Tây Du Ký 1986 hoặc của bất kỳ diễn viên nào, để tránh vi phạm bản quyền. Mỗi nhân vật chỉ giữ dấu hiệu nhận diện kinh điển, phối thêm đồ hiện đại:
  - **Đại Ca:** vòng kim cô, gậy Như Ý thu nhỏ, áo bomber.
  - **Heo Lười:** tai to, bụng phệ, cào chín răng dùng để gãi lưng.
  - **Út Khờ:** da xanh xám, râu đỏ, chuỗi hạt gỗ, tạp dề làm việc nhà. Bỏ chuỗi đầu lâu cho hợp TikTok.
  - **Thầy:** áo cà sa cam nghệ, điện thoại giắt trong tay áo.
- **Tôn trọng Phật giáo:** Thầy hiền, hơi ngây thơ, ăn chay và không bao giờ bị chế giễu; tiếng cười đến từ tình huống. Kệ thờ Phật trong nhà luôn ngay ngắn, không ai chạm vào, gió bão cũng không làm xê dịch (đã ghi sẵn trong [AVOID]).
- **Giọng:** từ 07/11/2026 cả nhà nói giọng Bắc thanh thoát (giọng Hà Nội chuẩn), đồng bộ với các series TikTok khác của kênh (trừ Mít & Đú).
- **Nhạc nền:** đàn tranh, cồng, phách trên nền beat hip-hop nhẹ, chất cổ trang gặp hiện đại.
- **Màu phép thuật:** mọi hiệu ứng phép (gậy dài ra, mây bay, gió quạt) đều có ánh vàng, để thống nhất cả series.
- **Tỉ lệ chiều cao:** Út Khờ cao nhất, rồi đến La Sát và Thầy (ngang nhau). Heo Lười thấp hơn Thầy một cái đầu nhưng ngang gấp đôi. Đại Ca thấp nhất, chỉ tới ngực Thầy.

**Cấu trúc chuẩn bắt buộc (Clip Hài 60 Giây = 6 Clip × 10s — Tổng Kết Hot & Drama Của Ngày):**
Mỗi tập là một **Bản Tin Hài Tổng Kết Hot Trend & Drama Mạng Xã Hội Trong Ngày (`60s = 6 clip × 10s`)** diễn ra tại căn nhà trọ hẻm Sài Gòn của 4 thầy trò Đường Tăng (`@Thay`, `@DaiCa`, `@HeoLuoi`, `@UtKho`) và chị chủ `La Sát`:

| Clip | Giây | Việc của clip (Cấu trúc 60s Tổng Kết Hot & Drama Của Ngày) |
| --- | --- | --- |
| 1 | 0–10 | **Hook 0–2 giây & Tin Hot / Drama #1 trong ngày:** Mở màn bằng một hành động bắt trend lố bịch của Heo Lười hoặc Đại Ca; khơi mào ngay vụ việc / trào lưu đang gây bão mạng xã hội trong ngày bằng câu thoại đời thường hài hước |
| 2 | 10–20 | **Tin Hot / Drama #2 & Màn bóc phốt / bày mưu:** Đại Ca, Út Khờ và Thầy tung hứng thêm tin nóng thứ hai trong ngày; Đại Ca rút gậy Như Ý bày kế dùng phép thuật xử lý tình huống |
| 3 | 20–30 | **Phép thuật 72 biến ra tay & Lỗi kỹ thuật dở khóc dở cười (Drama #3):** Đại Ca hoặc Heo Lười thi triển phép thuật bám sát chi tiết drama/trend trong ngày nhưng phép bị lỗi nửa mùa (ví dụ: hóa tôm hùm lòi đuôi mì gói, hóa cằm V-line méo tường, hóa loa phóng thanh nổ bình ắc quy) |
| 4 | 30–40 | **Cao trào leo thang & Chị chủ La Sát xuất hiện (Drama #4):** Chị chủ `La Sát` cầm quạt Ba Tiêu bước vào đúng lúc phép thuật phản tác dụng, kéo theo drama tiền trọ / sao kê / kiểm tra phòng làm cả bọn nhốn nháo |
| 5 | 40–50 | **Đổ thừa & Phát hiện bất ngờ:** Đại Ca và Heo Lười quýnh quáng đổ thừa nhau hoặc kêu `"Oan!"`, trước khi Út Khờ thật thà chỉ ra sự thật tréo ngoe ngay trước mắt |
| 6 | 50–60 | **Lật kèo chốt sổ bằng quạt Ba Tiêu & Câu hiền của Thầy:** Cú quạt Ba Tiêu dẹp loạn hoặc câu đúc kết hiền hậu mà thấm thía của Thầy (`"A Di Đà Phật..."`); 1–2 giây cuối là khung hình Thumbnail 5 nhân vật |

Luôn đảm bảo đủ **6 clip × 10s = 60 giây** cho mỗi tập tổng kết hot và drama của ngày. Clip 1 làm bằng Ingredients và đính ảnh của **mọi** nhân vật xuất hiện trong tập; Clip 2–6 nối khung cuối clip trước (`Seamless Frame Chaining`), nhân vật mới vào khung thì dán FULL LOCK của người đó trong `[CHARACTERS]`.

**Tin hot top trend (bắt buộc từ Tập 16):**
1. **Quét trong ngày viết:** [RSS Google Trends VN](https://trends.google.com/trending/rss?geo=VN&hl=vi), RSS VnExpress (tin nổi bật, thời sự, đời sống, giải trí), Dân trí, Tuổi Trẻ (nhịp sống trẻ), trang khám phá TikTok qua nguồn thứ cấp. Tin phải lên báo trong 24–48 giờ và còn trong khung đó lúc đăng.
2. **Chọn tin hợp Tây Du Ký nhất,** không phải tin nhiều lượt tìm nhất: ưu tiên tin dân mạng đã tự nhắc tới Tây Du Ký (Tập 16: đường phố Thâm Quyến bị ví như Hoa Quả Sơn), tin đời sống Sài Gòn có thể làm thành drama nhà trọ, và tin có chi tiết cụ thể cho phép thuật bám vào.
3. **Loại:** tai nạn, người chết, án hình sự nặng, chính trị, người thật có tên (nghệ sĩ, doanh nhân), thương hiệu; tin kênh khác trong ngày đã dùng (ví dụ Phèo) thì tránh trùng nếu còn tin khác.
4. **Ghi lại:** README tập có dòng **⚡ Vì sao hot** (nguồn, giờ đăng, ngày kiểm) và **Đã quét và không chọn**; ghi một mục vào [TRENDS.md](../TRENDS.md). Tin cũ hơn 48 giờ mà tập chưa render thì thay bằng tin mới (Tập 16 cũ về vụ 31,7 tỷ đã thay như vậy).

**Thoại tự nhiên như người thật (từ Tập 16):**
- Câu ngắn 2–9 âm tiết, khẩu ngữ miền Bắc (này, nhé, không, à, ơ, trời ơi, tí), nói với nhau chứ không nói với khán giả; giữ câu cửa miệng ("Khai mau!", "Oan!", "Đại Ca nói phải.", "A Di Đà Phật") nhưng không ép câu nào cũng có.
- **Cấm:** đọc bản tin ("Chùa online sáu trăm ngàn người vô…", "vụ mất 31,7 tỷ…"), con số, điều luật, mức phạt trong thoại (để ở caption và README); câu dài hơn 10 âm tiết; giảng giải bài học.
- Mỗi clip 2–3 câu, khoảng 13–20 âm tiết, không quá 4,5 âm tiết mỗi giây (Thầy nói chậm, giữ dưới 3,5 âm tiết mỗi giây). Không bắt buộc ai cũng có câu; 30 giây chỉ cần 3–4 nhân vật nói.
- Gag hình và âm thanh (sóng âm, loa rú, cả hẻm bật đèn) làm phần lớn tiếng cười; im thoại trong lúc gag xảy ra.
- [AVOID] có thêm `a narrator voice or voiceover`.

**Quy tắc viral (từ Tập 16):** caption dòng đầu là hook khoảng 80 ký tự nhắc thẳng tin hot; một câu hỏi kéo bình luận gắn với tin ("nếu Việt Nam cấm còi 24/24 thì bạn hét hay xài loa?"); bài học đời thật viết gọn trong caption; đúng 5 hashtag (2 rộng, 3 ngách theo tin); bình luận ghim chỉ ra giây đáng xem lại.

**Cấu trúc tập 30–60 giây cũ (Tập 8–15, tối đa 60 giây = 3–6 clip × 10s):** kịch bản chi tiết như chuyện thật trong một căn nhà trọ Sài Gòn (tra cứu Google Search khi cần cập nhật trend/sự kiện thực tế). Tập 6 clip đi đủ sáu nhịp dưới đây; tập 5 clip gộp kế hoạch với phép thuật; tập 4 clip đi: hook và kế hoạch → phép thuật → lật kèo → chốt; tập 3 clip (30s) đi: hook & phép thuật → lật kèo → chốt.

| Clip | Vai trò | Gợi ý |
| --- | --- | --- |
| 1 | Hook và vấn đề | 2 giây đầu có cảnh lạ hoặc câu gây tò mò; nêu ngay chuyện của nhà (tiền nhà, ăn vụng, việc nhà, tin hot trong ngày) |
| 2 | Kế hoạch | Ai đó bày cách, thường là Đại Ca với phép thuật; người khác nghi ngờ |
| 3 | Phép thuật ra tay | Gag hình ảnh chính. Ưu tiên phép chưa dùng (tra cột Phép chính ở mục 5): 72 phép biến hóa (biến thành đồ vật hoặc thành người khác), định thân pháp, gậy Như Ý to nhỏ dài ngắn, Heo Lười biến hình, Út Khờ gánh đồ |
| 4 | Leo thang | Phép phản tác dụng, hoặc La Sát xuất hiện làm mọi chuyện rối thêm |
| 5 | Lật kèo | Một nhân vật bất ngờ đảo tình thế (Út Khờ, Heo Lười, La Sát); không lặp twist của các tập trước |
| 6 | Chốt | Câu hiền của Thầy (không bao giờ bị chế giễu) hoặc punchline; khung thumbnail đứng yên 1 giây |

- **Như người thật:** chi tiết đời sống Sài Gòn có thật (món ăn, giá cả, thói quen trong hẻm, tin trong ngày có nguồn). Tập 8–15: ai cũng có ít nhất một câu, mỗi clip 2–4 câu thoại, tối đa khoảng 31 âm tiết; từ Tập 16 theo mục Thoại tự nhiên ở trên.
- **Một bài học nhỏ đời thật** (an toàn, tiết kiệm, chống lừa đảo…) nếu có thì nói bằng tình huống và câu đùa, không giảng giải.
- **Không lặp:** không dùng cùng kiểu lật kèo trong 3 tập liên tiếp; viết xong tập nào thì ghi phép chính và kiểu lật kèo vào bảng mục 5.
- **Neo nhân vật:** tập 5–6 clip mở lại một clip bằng Ingredients sau 3–4 clip (cắt theo hành động hoặc nhảy thời gian, dán [FORMAT] và FULL LOCK, không dán câu Continue…), như FLOW_GUIDE mục 1–2. Tập 4 clip có cảnh nhảy thời gian thì clip đó cũng mở bằng Ingredients.

**Xưng hô và dấu ấn nhân vật** (giữ cố định để khán giả nhớ):

| Nhân vật | Tính cách | Xưng hô | Dấu ấn |
| --- | --- | --- | --- |
| Thầy | Hiền, chậm rãi, hơi ngây thơ | xưng "ta", gọi đệ tử là "đồ nhi" | chắp tay: "A Di Đà Phật..." |
| Đại Ca | Lanh, nóng tính, mê "phá án" | tự xưng "Đại Ca"; gọi thẳng tên "Heo Lười", "Út Khờ" | rút gậy chỉ mặt: "Khai mau!" |
| Heo Lười | Lười, ham ăn, hay kêu oan | tự xưng "Heo Lười" | tay luôn cầm đồ ăn: "Oan!" |
| Út Khờ | Ít nói, hiền, lo việc nhà | gọi "Thầy", "Đại Ca" | "Đại Ca nói phải." |
| La Sát (bà chủ trọ) | Đanh đá, sang chảnh, dễ mềm lòng | xưng "chị", gọi cả bọn là "mấy đứa" | bung quạt "phạch" là có gió bão |

---

## 1. Khóa nhân vật (Character Bible)

**Tên nhân vật trên Flow:** `@Thay` · `@DaiCa` · `@HeoLuoi` · `@UtKho`. Mỗi dòng khóa của nhân vật chính bắt đầu bằng `@Tên = …`, để Flow gọi đúng nhân vật đã lưu và model hiểu tên đó là nhân vật nào trong prompt.

> **FULL LOCK** dán vào mọi Clip 1 và vào clip mà nhân vật xuất hiện lần đầu trong tập (ví dụ La Sát vào ở Clip 4, dưới nhãn [NEW IN THIS SEGMENT — …]); **SHORT LOCK** dán từ Clip 2 đến clip cuối cho nhân vật đã có mặt ở clip ngay trước. Giữ nguyên văn, không sửa chữ nào. Giọng nói đã nằm sẵn trong khóa.

### 1.1 THẦY (Đường Tăng)

Nhà sư trẻ chừng 27–29 tuổi, đầu cạo trọc, mặt tròn phúc hậu, mắt hiền. Áo cà sa cam nghệ, dải cà sa đỏ đậm vắt vai trái, chuỗi hạt gỗ nâu, dép cỏ, điện thoại giắt trong tay áo. Đi đứng chậm rãi, hay chắp tay, hơi ngây thơ, ăn chay.
**Giọng:** nam trẻ, nhẹ nhàng, chậm rãi, êm ái.

**FULL LOCK**

```text
@Thay = THẦY: a young human Buddhist monk in his late twenties, slim build, medium height, smooth shaved head, soft round face with gentle rosy cheeks, calm kind almond-shaped dark-brown eyes and a faint serene smile; wears a loose saffron-orange monk's robe with a deep-red kasaya sash draped over the left shoulder, a string of polished brown wooden prayer beads around his neck and simple straw sandals; a modern smartphone tucked inside his wide right sleeve. Moves slowly and gracefully, hands often pressed together at the chest. Voice: gentle, slow, soothing young male voice.
```

**SHORT LOCK**

```text
@Thay = THẦY: young shaved-head human monk, soft round face, calm kind eyes, saffron-orange robe with deep-red kasaya sash, brown wooden prayer beads; gentle, slow, soothing young male voice.
```

### 1.2 ĐẠI CA (Ngộ Không) — Biến thể A (mặc định)

Khỉ nhân hóa nhỏ con, lanh lẹ, thấp nhất nhóm; lông nâu vàng, mặt đỏ hồng hình trái tim, mắt hổ phách tinh nghịch, đuôi dài cong; vòng kim cô vàng mảnh. Áo bomber đỏ, áo thun vàng trơn, quần túi hộp vằn hổ cam đen, đi chân trần; gậy Như Ý thu nhỏ bằng cây bút giắt sau tai phải.
**Giọng:** nam trẻ, nói nhanh, sắc, lanh lợi, nóng tính.

**FULL LOCK**

```text
@DaiCa = ĐẠI CA: an anthropomorphic monkey with a small, wiry, agile build, the shortest of the group, golden-brown fur, a heart-shaped pinkish-red bare face, bright amber eyes with a mischievous spark, large expressive ears and a long curling tail; a thin golden circlet headband around his head; wears a red bomber jacket over a plain yellow t-shirt and orange-and-black tiger-stripe cargo shorts, barefoot; a pen-sized red-and-gold staff tucked behind his right ear that can instantly extend into a long staff. Quick, restless, acrobatic movements; often perches on furniture. Voice: fast, sharp, quick-witted, hot-tempered young male voice.
```

**SHORT LOCK**

```text
@DaiCa = ĐẠI CA: small golden-brown monkey, heart-shaped pinkish-red face, amber eyes, thin golden circlet headband, red bomber jacket over plain yellow t-shirt, tiger-stripe cargo shorts, pen-sized staff behind right ear; fast, sharp, quick-witted, hot-tempered young male voice.
```

### 1.3 ĐẠI CA — Biến thể B (áo giao hàng · Tập 3)

Giữ nguyên khuôn mặt, màu lông và vòng kim cô (lộ ra dưới vành mũ). Áo khoác shipper xanh lá phối vàng, trơn, không logo; mũ bảo hiểm nửa đầu màu xanh lá; điện thoại gắn ở cẳng tay trái; đứng trên **Cân Đẩu Vân** (đám mây vàng nhỏ) như đứng trên ván trượt bay. Bỏ gậy sau tai vì vướng mũ.
**Giọng:** như biến thể A.

**FULL LOCK**

```text
@DaiCa = ĐẠI CA (DELIVERY OUTFIT): the same anthropomorphic monkey with a small, wiry, agile build, golden-brown fur, a heart-shaped pinkish-red bare face, bright amber eyes with a mischievous spark, large expressive ears and a long curling tail; the thin golden circlet headband visible across his forehead under an open-face green helmet; wears a plain green-and-yellow delivery rider jacket with no logos or text and orange-and-black tiger-stripe cargo shorts, barefoot; a smartphone in a clear holder strapped to his left forearm; he rides CÂN ĐẨU VÂN, a small fluffy golden cloud he stands on like a hoverboard. Quick, restless, acrobatic movements. Voice: fast, sharp, quick-witted, hot-tempered young male voice.
```

**SHORT LOCK**

```text
@DaiCa = ĐẠI CA (DELIVERY OUTFIT): small golden-brown monkey, heart-shaped pinkish-red face, amber eyes, golden circlet under an open-face green helmet, plain green-and-yellow rider jacket, tiger-stripe cargo shorts, phone on left forearm, rides a small golden cloud; fast, sharp, quick-witted, hot-tempered young male voice.
```

### 1.4 HEO LƯỜI (Bát Giới)

Heo nhân hóa tròn ủng, bụng phệ, da hồng, tai to cụp che đôi mắt híp, mõm to. Áo thun đen trơn rộng thùng thình, khoác áo choàng xanh navy mở vạt, dép kẹp cao su đen. Cây cào chín răng nhỏ luôn kè kè bên người (đeo chéo lưng hoặc dựng bên cạnh) để gãi lưng; tay gần như lúc nào cũng cầm đồ ăn. Dáng lười, đi lạch bạch.
**Giọng:** nam, mập mạp, lười biếng, hay than, giọng mũi hài hước.

**FULL LOCK**

```text
@HeoLuoi = HEO LƯỜI: an anthropomorphic pig, chubby and very round with a big bouncy belly, soft pink skin, large floppy ears hanging over small squinting dark eyes, a wide pink snout, rosy cheeks and a short curly tail; wears an oversized plain black t-shirt under an open, loose navy-blue robe with wide sleeves, and black rubber flip-flops; his small nine-tooth iron rake is always nearby, slung across his back or leaning beside him, and he uses it as a back-scratcher; almost always holding a snack. Lazy, slouching posture; waddles when he walks. Voice: chubby, lazy, whiny, comically nasal male voice.
```

**SHORT LOCK**

```text
@HeoLuoi = HEO LƯỜI: chubby round pink pig, big belly, floppy ears, small squinting eyes, wide snout, oversized plain black t-shirt under open navy-blue robe, black flip-flops, small nine-tooth rake nearby; chubby, lazy, whiny, comically nasal male voice.
```

### 1.5 ÚT KHỜ (Sa Tăng)

Người khổng lồ hiền lành, cao nhất nhóm, vai rộng; da xanh xám, đầu trọc, râu đỏ gạch ngắn gọn, lông mày rậm, mắt nhỏ hiền. Áo choàng nâu đất xắn tay, tạp dề xanh ô liu bạc màu, chuỗi hạt gỗ sẫm hạt to (không có đầu lâu). Chậm rãi, hay khuân vác giúp mọi người, rất ít nói.
**Giọng:** nam, rất trầm, chậm, điềm tĩnh.

**FULL LOCK**

```text
@UtKho = ÚT KHỜ: a very tall, broad-shouldered gentle giant, the tallest of the group, smooth blue-grey skin, a bald head, a short neat rust-red beard, thick eyebrows, small kind dark eyes and a calm, patient expression; wears a plain earth-brown robe with rolled-up sleeves, a faded olive-green kitchen apron tied over it, and a long necklace of large round dark-wood prayer beads; huge, careful hands. Moves slowly and steadily, often holding or carrying things for the others; speaks very few words. Voice: very deep, slow, calm male voice.
```

**SHORT LOCK**

```text
@UtKho = ÚT KHỜ: very tall gentle giant, blue-grey skin, bald, short rust-red beard, earth-brown robe, faded olive-green kitchen apron, large dark-wood prayer-bead necklace; very deep, slow, calm male voice.
```

### 1.6 LA SÁT — bà chủ trọ (nhân vật phụ · Tập 2, 4, 8, 9)

Thiết Phiến Công Chúa phiên bản bà chủ nhà trọ, ở ngay sát vách. Cao, mảnh mai, da trắng sứ, mày xếch, kẻ mắt đỏ, môi đỏ; búi tóc cao cài trâm vàng; áo dài lụa đỏ thêu phượng vàng, quần lụa đen, vòng vàng. Cầm quạt Ba Tiêu khổng lồ hình lá chuối xanh thẫm, cán sơn mài đỏ; bung quạt là có gió bão.
**Giọng:** nữ, sắc, đanh, ra lệnh dứt khoát.

**FULL LOCK**

```text
LA SÁT: an elegant, fierce human woman in her late thirties, the landlady; tall and slender with porcelain skin, sharp winged eyebrows, intense dark eyes with red eyeliner and bold red lips; glossy black hair in a high bun held by long gold hairpins; wears a fitted red silk áo dài with subtle gold phoenix embroidery over black silk trousers, and gold bangles; carries QUẠT BA TIÊU, a giant fan shaped like a deep-green banana leaf with a red-lacquered handle, which she snaps open and shut. Proud, upright posture and dramatic gestures. Voice: sharp, commanding, crisp female voice.
```

**SHORT LOCK**

```text
LA SÁT: elegant fierce landlady, high black bun with gold hairpins, bold red lips, fitted red silk áo dài with gold phoenix embroidery, giant deep-green banana-leaf fan with red handle; sharp, commanding, crisp female voice.
```

### 1.7 KHÁCH — cô khách đặt bún (nhân vật phụ · Tập 3)

Nhân viên văn phòng chừng 25 tuổi, nhỏ nhắn, tóc đen thẳng ngang vai, mái bằng, kính tròn gọng đồi mồi. Áo sơ mi trắng tay ngắn, quần lưng cao xanh nhạt, giày sneaker trắng; tay cầm điện thoại. Biểu cảm nhiều, dễ giật mình.
**Giọng:** nữ trẻ, trong, cao.

**FULL LOCK**

```text
KHÁCH: a young Vietnamese office woman in her mid-twenties, petite, with shoulder-length straight black hair and blunt bangs, round tortoiseshell glasses and wide expressive eyes; wears a crisp white short-sleeve blouse, light-blue high-waisted trousers and white sneakers; holds a smartphone. Expressive and easily startled. Voice: bright, high-pitched young female voice.
```

**SHORT LOCK**

```text
KHÁCH: petite young office woman, shoulder-length black hair with blunt bangs, round tortoiseshell glasses, white blouse, light-blue trousers, white sneakers, smartphone in hand; bright, high-pitched young female voice.
```

### 1.8 PHÂN THÂN ĐẠI CA — 5 bản sao tí hon (hiệu ứng phép · Tập 5)

Đại Ca nhổ một nhúm lông, thổi ra ánh vàng thành 5 bản sao cao bằng cái tách trà. Bản sao giống hệt Đại Ca biến thể A (không có gậy), luôn cử động đồng loạt và **bắt chước y chang tính khí của Đại Ca**. Không cần ảnh tham chiếu riêng: model dựng từ chính Đại Ca đang có trong khung hình.
**Giọng:** bản cao vút của giọng Đại Ca, luôn nói đồng thanh.

**FULL LOCK** (dùng ở clip bản sao xuất hiện lần đầu)

```text
ĐẠI CA CLONES: five magical palm-sized copies of ĐẠI CA, each only as tall as a teacup, identical to him in every detail: an anthropomorphic monkey with a small, wiry, agile build, golden-brown fur, a heart-shaped pinkish-red bare face, bright amber eyes with a mischievous spark, large expressive ears and a long curling tail; a thin golden circlet headband around his head; wears a red bomber jacket over a plain yellow t-shirt and orange-and-black tiger-stripe cargo shorts, barefoot; no staff. They pop into existence in a puff of golden sparkles, move in perfect unison and copy ĐẠI CA's own attitude exactly. Voice: a higher-pitched copy of ĐẠI CA's fast, sharp, quick-witted young male voice, always speaking in unison.
```

**SHORT LOCK**

```text
ĐẠI CA CLONES: five teacup-tall identical copies of ĐẠI CA (golden-brown monkeys, heart-shaped pinkish-red faces, thin golden circlets, red bomber jackets over plain yellow t-shirts, tiger-stripe cargo shorts, no staff), moving in perfect unison; higher-pitched copy of his voice, speaking in unison.
```

### 1.9 BẠCH MÃ — ngựa trắng của Thầy (nhân vật phụ · Tập 14)

Ngựa trắng của Thầy đứng ở khoảng sân / hẻm ngay ngoài cổng sắt xếp. Lông trắng muốt, bờm và đuôi trắng bạc, mắt nâu to biểu cảm hài hước, đeo dây cương vải đỏ đơn giản có chuông đồng nhỏ.

**FULL LOCK**

```text
@BachMa = BẠCH MÃ: a handsome cartoon white horse with a glossy snow-white coat, a flowing silver-white mane and tail, expressive dark-brown eyes and comedic equine facial expressions, standing just outside the open green metal gate in the courtyard alley; wears a simple red fabric halter strap with a small brass bell and no text or logos.
```

**SHORT LOCK**

```text
@BachMa = BẠCH MÃ: handsome cartoon white horse with silver-white mane, expressive dark eyes, simple red halter strap with brass bell, standing just outside the open green gate.
```

---

## 2. Bối cảnh cố định

> Dán nguyên văn vào mục [SETTING]. Đạo cụ riêng của từng tập được ghi thêm ở dòng `Props:` ngay bên dưới khối bối cảnh.

### 2.1 NHÀ TRỌ — PHÒNG KHÁCH (Tập 1, 2, 5, 8–11)

Bố cục nhìn từ cửa vào:
- sofa vàng mù tạt sát tường trái, máy lạnh treo phía trên, bàn trà gỗ thấp phía trước;
- góc thiền (bồ đoàn) ở góc trong cùng bên trái, sau đầu sofa;
- bếp nhỏ dọc tường sau, tủ lạnh mini ở góc trong bên phải;
- kệ thờ Phật trên cao ở tường sau.

```text
Ground-floor living room of a narrow, cozy rented tube house in a Saigon alley, 2026. Facing in from the open front entrance (a green folding metal gate that leads straight out to the alley): a worn mustard-yellow fabric sofa with mismatched cushions against the left wall, a white wall-mounted air conditioner above it and a low wooden coffee table in front of it; a round saffron meditation cushion on a woven mat in the left back corner, beyond the end of the sofa; a tiny kitchen corner along the back wall with a two-burner gas stove, hanging pots and a dish rack; a small white mini-fridge in the right back corner; a simple wooden altar shelf high on the back wall holding a small serene seated Buddha statue and a small vase of flowers, always neat and never touched; a messy pile of slippers and shoes by the entrance; pastel-green walls with slightly peeling paint and a slowly turning ceiling fan. Lighting: warm late-afternoon sunlight pouring in through the entrance, mixed with a soft tungsten ceiling lamp. All objects have blank or unreadable labels.
```

### 2.2 HẺM TRƯỚC NHÀ (Tập 2, 4)

Cửa sắt xếp màu xanh lá của nhà trọ. Sát vách là nhà bà chủ La Sát, cửa gỗ đôi sơn đỏ. Xe máy dựng dọc tường, dây điện chằng chịt, đèn dây vừa bật.

```text
A narrow Saigon alley (hẻm) at golden late afternoon, 2026: the green folding metal gate of the rented tube house standing open; right next door, the landlady's house with a glossy red double wooden door and two potted plants with small red flowers beside it; three motorbikes parked along the wall; ferns and bougainvillea spilling from small balconies above; tangled overhead power lines; a few warm string lights just switched on; mossy plastered walls in faded yellow and pink. No other people. All signs, house numbers and license plates are blank or unreadable.
```

### 2.3 PHỐ (Tập 3)

Con phố nhỏ vắng xe. Cuối phố có xe bún không người trông; tiền cảnh là bậc thềm tòa văn phòng, nơi cô khách đứng.

```text
A quiet Saigon side street at golden late afternoon, 2026: rows of narrow, colorful tube houses with small balconies and potted bougainvillea, tangled overhead power lines, tall tamarind trees casting dappled shadows, motorbikes parked along the curb, no traffic and no other people; far down the street, an unattended street-side noodle stall with a big pot and low red plastic stools; in the foreground, the glass-door entrance of a small modern office building with three wide grey stone steps. All signs, awnings, storefronts and license plates are blank or unreadable.
```

### 2.4 BẾN BẠCH ĐẰNG — NHỊP CẦU LÁ DỪA (Tập 6)

Lối đi bộ ven sông ở công viên bến Bạch Đằng lúc hoàng hôn: nền đá xám nhạt, lan can trắng thấp sát mép nước, thảm cỏ có hàng cau non và vài ghế đá thấp. Sát bờ là sà lan khổng lồ chở nhịp vòm thép trắng uốn cong hình tàu lá dừa nước, tức nhịp chính của cầu đi bộ qua sông Sài Gòn, **chưa lắp, chưa cho người đi**. Bên kia sông là các tòa nhà Thủ Thiêm dưới trời cam hồng. Không có người qua lại gần nhân vật; mọi biển hiệu, băng rôn, tên tàu để trống.

```text
A wide riverside promenade in Bạch Đằng wharf park, central Saigon, at golden hour, 2026: smooth light-grey stone paving, a low white metal railing along the water's edge, a strip of green lawn with young palm trees and a few low stone benches. Moored right alongside the bank on the wide brown Saigon River sits a huge flat steel super barge carrying a gigantic, gracefully curved white steel arch shaped like a single nipa palm (lá dừa nước) frond, with slender steel ribs and cables fanning out along its curve like leaflets: the main span of the new pedestrian bridge, still waiting to be installed and not open to anyone. Across the river, the modern towers of the Thủ Thiêm skyline glow under a warm orange-pink sky, their reflections shimmering on the water. No other people on the promenade; at most a few tiny, blurred silhouettes far away on the opposite bank. All signs, banners, boat names and markings are blank or unreadable.
```

### 2.5 NHÀ TRỌ — PHÒNG KHÁCH LÚC RẠNG SÁNG (Tập 11)

Cùng bố cục với 2.1, chỉ khác ánh sáng: 5 giờ sáng, ánh xanh lạnh từ cửa vào, đèn trần tắt. Dùng cho clip nhảy sang sáng hôm sau.

```text
Ground-floor living room of a narrow, cozy rented tube house in a Saigon alley, 2026. Facing in from the open front entrance (a green folding metal gate that leads straight out to the alley): a worn mustard-yellow fabric sofa with mismatched cushions against the left wall, a white wall-mounted air conditioner above it and a low wooden coffee table in front of it; a round saffron meditation cushion on a woven mat in the left back corner, beyond the end of the sofa; a tiny kitchen corner along the back wall with a two-burner gas stove, hanging pots and a dish rack; a small white mini-fridge in the right back corner; a simple wooden altar shelf high on the back wall holding a small serene seated Buddha statue and a small vase of flowers, always neat and never touched; a messy pile of slippers and shoes by the entrance; pastel-green walls with slightly peeling paint and a slowly turning ceiling fan. Lighting: cool blue early-dawn light coming in through the open entrance, the ceiling lamp switched off, quiet and soft. All objects have blank or unreadable labels.
```

---

## 3. Khóa phong cách

**[FORMAT]**: dán ở đầu mọi Clip 1

```text
[FORMAT]
Vertical 9:16, 10-second clip, 2D animated comedy cartoon with a hand-drawn cel animation look in the exact art style of the attached character references, original character designs, clean bold outlines, flat colors with simple cel shading, painted 2D backgrounds, vibrant color palette, 24fps, snappy comedic timing with expressive squash-and-stretch cartoon acting. Spoken dialogue in Vietnamese with a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent and accurate lip-sync; non-speaking characters keep their mouths closed. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Cut only where the shot list says, and never flash or cut to an attached character reference turnaround sheet or plain grey studio backdrop at the start or end of the clip. No subtitles, no captions, no on-screen text, no logos, no watermark.
```

**Nhạc nền**: câu cố định, luôn có trong [SOUND]

```text
Music: playful comedic score of plucked đàn tranh, punchy gong hits and wood-block percussion over a light modern hip-hop beat.
```

**Câu mở đầu clip 2 trở đi** (làm bằng Frames với start frame = khung cuối clip trước, hoặc bằng Extend): dán ở đầu mọi clip từ Clip 2 đến clip cuối, trừ clip mở bằng Ingredients

```text
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, same outfits, same location, same lighting and color grade, same 2D hand-drawn cartoon style with clean bold outlines and flat cel-shaded colors. Flawless continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, same animation style. Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a soft, clear, elegant Northern (Hà Nội) accent and accurate lip-sync, never shown as text. Cut only where the shot list says, and never flash or cut to a standalone character reference sheet at the start or end of the clip. No subtitles, no captions, no on-screen text.
```

**Câu chặn 3D & thẻ tham chiếu**: luôn là mục cuối của [AVOID] ở mọi clip

```text
cutting to or flashing a standalone character reference turnaround sheet or plain grey studio backdrop at the start or end of the clip, 3D or CGI look, photorealistic rendering.
```

---

## 4. Ảnh tham chiếu nhân vật

Tạo bằng chế độ tạo ảnh trong Flow (Nano Banana / Imagen), tỉ lệ **16:9**. Mỗi nhân vật chạy 2–4 lần, chọn ảnh đẹp nhất, lưu đúng tên file rồi dùng lại cho mọi tập. Ảnh 3D tạo trước ngày 26/10/2026 không dùng nữa: tạo lại bằng các prompt 2D dưới đây, hoặc dùng ảnh 2D đã có của nhân vật trên Flow.

Nếu cần thêm ảnh cận mặt, giữ nguyên prompt nhưng thay câu `Full body shown in four views side by side: front, three-quarter, side profile and back.` bằng `Close-up head-and-shoulders portrait, front view.`

### 4.1 `TDK_REF_THAY` — Thầy

```text
Character turnaround sheet of an original 2D cartoon character: a young human Buddhist monk in his late twenties, slim build, medium height, smooth shaved head, soft round face with gentle rosy cheeks, calm kind almond-shaped dark-brown eyes and a faint serene smile; wears a loose saffron-orange monk's robe with a deep-red kasaya sash draped over the left shoulder, a string of polished brown wooden prayer beads around his neck and simple straw sandals; a modern smartphone tucked inside his wide right sleeve. Full body shown in four views side by side: front, three-quarter, side profile and back. Neutral standing pose with hands pressed together at the chest, calm, kind expression. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading, plain light-grey background. No text, no labels, no numbers, no watermark.
```

### 4.2 `TDK_REF_DAICA_A` — Đại Ca (biến thể A)

```text
Character turnaround sheet of an original 2D cartoon character: an anthropomorphic monkey with a small, wiry, agile build, the shortest of the group, golden-brown fur, a heart-shaped pinkish-red bare face, bright amber eyes with a mischievous spark, large expressive ears and a long curling tail; a thin golden circlet headband around his head; wears a red bomber jacket over a plain yellow t-shirt and orange-and-black tiger-stripe cargo shorts, barefoot; a pen-sized red-and-gold staff tucked behind his right ear that can instantly extend into a long staff. Full body shown in four views side by side: front, three-quarter, side profile and back. Neutral standing pose, confident cheeky grin, tail curled. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading, plain light-grey background. No text, no labels, no numbers, no watermark.
```

### 4.3 `TDK_REF_DAICA_B` — Đại Ca (biến thể B, áo giao hàng)

```text
Character turnaround sheet of an original 2D cartoon character: an anthropomorphic monkey with a small, wiry, agile build, golden-brown fur, a heart-shaped pinkish-red bare face, bright amber eyes with a mischievous spark, large expressive ears and a long curling tail; the thin golden circlet headband visible across his forehead under an open-face green helmet; wears a plain green-and-yellow delivery rider jacket with no logos or text and orange-and-black tiger-stripe cargo shorts, barefoot; a smartphone in a clear holder strapped to his left forearm; he rides CÂN ĐẨU VÂN, a small fluffy golden cloud he stands on like a hoverboard. Full body shown in four views side by side: front, three-quarter, side profile and back. Standing on the small fluffy golden cloud hovering just above the ground, confident cheeky grin, tail curled. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading, plain light-grey background. No text, no labels, no numbers, no watermark.
```

### 4.4 `TDK_REF_HEOLUOI` — Heo Lười

```text
Character turnaround sheet of an original 2D cartoon character: an anthropomorphic pig, chubby and very round with a big bouncy belly, soft pink skin, large floppy ears hanging over small squinting dark eyes, a wide pink snout, rosy cheeks and a short curly tail; wears an oversized plain black t-shirt under an open, loose navy-blue robe with wide sleeves, and black rubber flip-flops; his small nine-tooth iron rake is always nearby, slung across his back or leaning beside him, and he uses it as a back-scratcher; almost always holding a snack. Full body shown in four views side by side: front, three-quarter, side profile and back. Neutral standing pose, belly forward, lazy happy smile, the rake slung across his back. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading, plain light-grey background. No text, no labels, no numbers, no watermark.
```

### 4.5 `TDK_REF_UTKHO` — Út Khờ

```text
Character turnaround sheet of an original 2D cartoon character: a very tall, broad-shouldered gentle giant, the tallest of the group, smooth blue-grey skin, a bald head, a short neat rust-red beard, thick eyebrows, small kind dark eyes and a calm, patient expression; wears a plain earth-brown robe with rolled-up sleeves, a faded olive-green kitchen apron tied over it, and a long necklace of large round dark-wood prayer beads; huge, careful hands. Full body shown in four views side by side: front, three-quarter, side profile and back. Neutral standing pose, huge hands clasped in front of the apron, calm gentle smile. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading, plain light-grey background. No text, no labels, no numbers, no watermark.
```

### 4.6 `TDK_REF_LASAT` — La Sát

```text
Character turnaround sheet of an original 2D cartoon character: an elegant, fierce human woman in her late thirties, the landlady; tall and slender with porcelain skin, sharp winged eyebrows, intense dark eyes with red eyeliner and bold red lips; glossy black hair in a high bun held by long gold hairpins; wears a fitted red silk áo dài with subtle gold phoenix embroidery over black silk trousers, and gold bangles; carries QUẠT BA TIÊU, a giant fan shaped like a deep-green banana leaf with a red-lacquered handle, which she snaps open and shut. Full body shown in four views side by side: front, three-quarter, side profile and back. Proud upright standing pose, the closed giant fan held in her right hand, one eyebrow raised. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading, plain light-grey background. No text, no labels, no numbers, no watermark.
```

### 4.7 `TDK_REF_KHACH` — Cô khách

```text
Character turnaround sheet of an original 2D cartoon character: a young Vietnamese office woman in her mid-twenties, petite, with shoulder-length straight black hair and blunt bangs, round tortoiseshell glasses and wide expressive eyes; wears a crisp white short-sleeve blouse, light-blue high-waisted trousers and white sneakers; holds a smartphone. Full body shown in four views side by side: front, three-quarter, side profile and back. Neutral standing pose holding the smartphone at chest height, friendly expression. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading, plain light-grey background. No text, no labels, no numbers, no watermark.
```

### 4.8 `TDK_REF_GROUP` — Ảnh xếp hàng bốn thầy trò

Ảnh này khóa tỉ lệ chiều cao. Khi Flow giới hạn số ảnh đính kèm, có thể đính **một ảnh nhóm này thay cho bốn ảnh lẻ** của Thầy, Đại Ca (A), Heo Lười và Út Khờ.

```text
Height comparison lineup of four original 2D cartoon characters standing side by side, full body, front view, on a plain light-grey background. From left to right: a very tall gentle giant, blue-grey skin, bald, short rust-red beard, earth-brown robe, faded olive-green kitchen apron, large dark-wood prayer-bead necklace (the tallest of the group); a young shaved-head human monk, soft round face, calm kind eyes, saffron-orange robe with deep-red kasaya sash, brown wooden prayer beads (medium height); a chubby round pink pig, big belly, floppy ears, small squinting eyes, wide snout, oversized plain black t-shirt under open navy-blue robe, black flip-flops, small nine-tooth rake nearby (a head shorter than the monk but twice as wide); a small golden-brown monkey, heart-shaped pinkish-red face, amber eyes, thin golden circlet headband, red bomber jacket over plain yellow t-shirt, tiger-stripe cargo shorts, pen-sized staff behind right ear (the shortest, reaching the monk's chest). Neutral standing poses, friendly expressions. 2D hand-drawn cartoon style, clean bold outlines, flat colors with simple cel shading. No text, no labels, no numbers, no watermark.
```

---

## 5. Danh sách tập

| Tập | Tên | Nội dung | Sản phẩm | Phép chính | Kiểu lật kèo |
| --- | --- | --- | --- | --- | --- |
| 1 | Ai ăn vụng hộp bánh? | Hộp bánh pía của Út Khờ chỉ còn vụn. Đại Ca "phá án", kết tội Heo Lười. Thủ phạm thật là Thầy: "bánh chay mà, ta tưởng đồ nhi cúng dường ta". | — | — | Thầy hóa ra là thủ phạm |
| 2 | Hóa đơn tiền điện | Tiền điện tăng gấp ba vì Heo Lười bật máy lạnh suốt ngày. Đại Ca đòi mượn quạt Ba Tiêu, La Sát quạt một phát thổi bay ba đồ đệ ra hẻm. Chỉ Thầy ngồi thiền bất động: "Tâm tĩnh... tự nhiên mát." | — | quạt Ba Tiêu (La Sát) | người ngồi yên (Thầy) lại thắng |
| 3 | Đại Ca đi giao hàng | Giao bún bằng Cân Đẩu Vân trong 1 giây, nhưng gió hất tung tô bún lên người khách. Kết quả: bị đánh giá 1 sao. | — | Cân Đẩu Vân | phép quá nhanh gây họa |
| 4 | Quà 20/10 cho bà chủ trọ | Ba đồ đệ tặng hoa và bánh kem, mong được giảm tiền nhà. Heo Lười ăn vụng một góc bánh. La Sát giảm tiền nhà cho cả bọn, riêng Heo Lười phải đóng gấp đôi. Hợp đăng dịp 20/10. | — | quạt Ba Tiêu (La Sát) | La Sát phạt riêng Heo Lười |
| 5 | Ai rửa chén? | Chén dơ chất thành tháp, Đại Ca không chịu rửa nên thổi lông ra 5 bản sao tí hon. Bản sao nằm dài ăn bánh với Heo Lười: "Tụi em giống Đại Ca mà!" Thầy: "nhân nào quả nấy". Đại Ca đeo găng rửa chén cạnh Út Khờ. | — | phân thân | bản sao lười y như chủ |
| 6 | Nhịp cầu lá dừa | ⚡ Trend cầu lá dừa: cả nhà ra bến Bạch Đằng xem nhịp vòm 3.400 tấn hình lá dừa nước; Đại Ca đòi nhấc cầu một tay, Thầy cản; Heo Lười hẹn "Tết qua cầu ăn bánh tét"; Cân Đẩu Vân chở Heo Lười không nổi; cả nhà selfie hẹn Tết. | — | gậy Như Ý, Cân Đẩu Vân | mây chở không nổi Heo Lười |
| 7 | Đại chiến bóng đá đêm khuya | ⚡ Trend bóng đá châu Âu: 3 giờ sáng Đại Ca cổ vũ cuồng nhiệt, Heo Lười trù "HLV bay ghế" rồi rủ cá chầu hủ tiếu, Út Khờ can; Thầy bước ra tưởng sắp mắng, hóa ra rút điện thoại hóng VAR. | — | — | Thầy hóa ra cũng mê (hóng VAR) |
| 8 | Vé nội bộ hóa lá khô | ⚡ Trend "đu concert" Mỹ Đình 24–25/10: La Sát khoe vé "nội bộ" giá năm trăm; hỏa nhãn kim tinh soi ra vé hóa lá khô, vé Heo Lười lén mua cũng vậy ("Oan!"); Út Khờ: "Tham rẻ... hóa lá khô." Vé bay ra Hà Nội bảy triệu, Đại Ca gọi Cân Đẩu Vân "một giây tới nơi"; một chớp mắt sau La Sát về, tóc dính hoa sữa: "Một giây... chỉ kịp hít hoa sữa!" | — | hỏa nhãn kim tinh, Cân Đẩu Vân | lừa đảo bị lật tẩy, đi một giây về tay trắng |
| 9 | Tên ở nhà | Tập ra mắt tên mới. La Sát kêu "Tôn Ngộ Không! Trư Bát Giới!" tới hụt hơi, quên luôn "Sa gì đó", nên đặt tên ở nhà cho cả bọn: Thầy (cả hẻm kêu vậy rồi), Heo Lười (vừa cãi "siêng lắm" đã ngáy), Đại Ca (lùn nhất nhà mà đòi làm anh lớn, biến khổng lồ rồi hắt xì teo bằng tách trà), Út Khờ (bự nhất mà là em út, kêu ai cũng "Dạ!"). Thầy: "Tên đổi... lòng không đổi." | — | 72 phép biến hóa (biến khổng lồ, teo nhỏ) | người bự nhất thành "Út", người lùn nhất thành "Đại Ca" |
| 10 | Triều cường gõ cửa | ⚡ Triều cường TP.HCM đỉnh 26–28/10: 5 giờ rưỡi chiều nước tràn qua bậc cửa; Đại Ca đắp đê bằng gậy Như Ý, Út Khờ khiêng nguyên sofa (cả Heo Lười) kê lên gạch; nước lại trào lên từ cống, Heo Lười chỉ ổ điện sát đất; Thầy bình tĩnh cúp cầu dao; Út Khờ chặn cống bằng bao cát ("Hồi xưa sống dưới sông, quen rồi"); cả nhà ngồi chờ triều xuống dưới ánh đê vàng. | — | gậy Như Ý (đê vàng, thành đèn), Út Khờ khiêng đồ | nước vô từ cống chứ không phải từ cửa; Út Khờ "khờ" mà rành nước nhất |
| 11 | Dự án ma | ⚡ Trend #duanma: Heo Lười hứa năm giờ sáng chạy mười cây số; Đại Ca dùng định thân pháp "giữ miệng giùm" khi Heo Lười lao vào nồi chè bắp; sáng hôm sau Heo Lười tắt báo thức ngủ tiếp, hóa ra Thầy và Út Khờ sáng nào cũng đi bộ nhanh ba chục phút; Heo Lười cầm ổ bánh mì đi vòng quanh bàn liền. Thầy: "Bắt đầu nhỏ... là bắt đầu thật." | — | định thân pháp | người chậm rãi nhất (Thầy) lại tập đều nhất; Heo Lười đi liền, không đợi mai |
| 12 | Săn sale nửa đêm | Nửa đêm Heo Lười thức canh sale 1k bấm mỏi tay không kịp; Đại Ca biến ra 10 bàn tay vàng bấm siêu tốc; sáng ra nhận 50 thùng tăm bông vì đè nhầm nút nhân 50, còn Út Khờ mua đúng nồi cơm điện giảm giá thật từ chiều hôm qua. Thầy: "Thứ cần thì mua một... thứ ham rẻ thì ôm năm mươi." | — | 72 phép biến hóa (10 cánh tay) | bấm nhanh quá hóa mua lố; Út Khờ mua chậm mà trúng thứ cần |
| 13 | Cúp điện giữa trưa | Giữa trưa Sài Gòn máy lạnh tắt phụt; Đại Ca xoay gậy Như Ý làm quạt số 10 thổi Heo Lười phồng tròn như bóng bay; La Sát bước vô báo nguyên con hẻm điện sáng trưng, hóa ra chỉ mỗi phòng bị nhảy cầu dao vì Heo Lười cắm nồi lẩu, ấm siêu tốc và lò nướng chung một ổ cắm; Út Khờ rút bớt phích cắm rồi bật lại cầu dao. Thầy: "Một ổ cắm gánh ba nồi... điện cũng biết mệt." | — | gậy Như Ý (xoay làm quạt gió) | tưởng cả hẻm cúp điện, hóa ra nhảy cầu dao phòng vì Heo Lười cắm 3 nồi chung 1 ổ |
| 14 | Karaoke kẹo kéo xóm trọ | Chiều cuối tuần Heo Lười ôm loa kéo gào nhạc thất tình làm chén trà rung bần bật, Bạch Mã lấy móng bịt tai; sợ La Sát qua mắng, Đại Ca rút lông thổi phép biến micro thành "Micro Tắt Tiếng" kêu vo ve như muỗi; ai dè La Sát bước vô xin hát ké bolero rồi giật luôn chiếc micro trúng phép, ngân vọng cổ mà loa kêu "í a lí nhí" như dế kêu; Út Khờ vặn loa về mức số 2 vừa đủ nghe. Thầy: "Hát vừa đủ nghe, hàng xóm mới thương." | — | rút lông biến micro thành "Micro Tắt Tiếng Định Hướng" | tưởng La Sát qua mắng, hóa ra qua xin hát ké rồi dính luôn phép tắt tiếng của Đại Ca |
| 15 | Chùa online gõ mõ công đức & Bẫy cúng dường dỏm | ⚡ Trend chùa online 600.000 lượt vào (03/11): Heo Lười nằm phơi bụng bấm mõ điện tử rồi định chuyển 500k "gói đại công đức xóa nghiệp ăn vụng"; Đại Ca bật Hỏa Nhãn Kim Tinh soi ra bẫy giả mạo nhà chùa, hóa phép hai chiếc mõ gỗ có cánh vàng cản kịp lúc La Sát định chuyển 1 triệu cầu tài lộc; La Sát bắt Heo Lười đi quét sạch nguyên con hẻm để "tích công đức offline thật sự". | — | Hỏa Nhãn Kim Tinh, gậy Như Ý hóa mõ gỗ có cánh vàng | đòi tích công đức online trên mạng, kết cục phải đi quét rác nguyên con hẻm offline |
| 16 | Cấm bóp còi thì… hét | ⚡ Trend Thâm Quyến cấm bóp còi từ 01/11, dân mạng ví đường phố như Hoa Quả Sơn (VnExpress 03/11): 22:30 Bạch Mã ngủ chắn hẻm, Heo Lười bị cấm bóp còi nên hét, Đại Ca biến thành loa vàng mặt khỉ rú cả hẻm bật đèn, La Sát: "Tưởng Hoa Quả Sơn hả?"; Thầy vuốt cổ ngựa, ngựa lặng lẽ nhường đường; Heo Lười chồm tới, bụng đè nút còi, bị quạt thổi xoay vô nhà. Tập 30 giây đầu tiên | — | 72 phép biến hóa (Đại Ca hóa loa vàng) | người nói nhỏ nhất mở được đường; cái bụng bóp còi thay chủ |
| 17 | Đọ quai hàm chụp ảnh nhà trọ | ⚡ Trend từ điển Collins chọn "mogging" (đọ quai hàm lấn át ngoại hình) làm Từ của năm 2026 (Tuổi Trẻ 04/11): La Sát bắt xếp hàng chụp hình làm sổ nhà trọ; Heo Lười hóp má tới tím mặt chen đứng trước, Đại Ca dùng gậy Như Ý biến cằm V-line kim cương lấp lánh sao vàng chắn ống kính; đúng lúc bấm máy Heo Lười hết hơi thở phì ra hất Đại Ca bay nhòe khỏi ảnh, chỉ có Thầy và Út Khờ đứng yên phía sau là sáng rực đẹp nhất hình. | — | 72 phép biến hóa / gậy Như Ý (biến cằm V-line kim cương) | hai đứa giành spotlight bị nhòe nhoẹt, Thầy và Út Khờ đứng yên tự nhiên lại sáng bừng nhất ảnh |
| 18 | Đại hội tin nóng phòng trọ — Hộ nghèo kiểu mới, AI đi chợ & Tiền trọ giắt vòng kim cô | ⚡ Tổng kết 5 tin hot ngày 05/11: Heo Lười đeo kính râm xách túi hiệu trả góp nhưng mở ví ra bay con bướm ("hộ nghèo kiểu mới"), đòi nghỉ việc chờ lãnh trợ cấp thất nghiệp 28,5 triệu; Đại Ca và Thầy nhắc chuyện Bot AI đi chợ hộ và học đêm chống tụt hậu; Đại Ca hóa phép biến mì gói thành bàn tiệc tôm hùm vàng khè La Sát nhưng phép lỗi lòi đuôi mì gói; La Sát đòi tăng tiền trọ gấp đôi làm phép tắt phụt; cả đám tưởng rớt tiền nhà ngoài tiệm (như vụ mất 50g vàng), hóa ra chính Đại Ca giắt phong bì tiền nhà dưới vòng kim cô trên trán mình. | — | gậy Như Ý / 72 phép biến hóa (biến bàn trà & mì gói thành bàn tiệc tôm hùm vàng bị lỗi lòi đuôi mì gói) | giả giàu bị đòi tăng tiền trọ gấp đôi; tưởng rớt tiền ngoài tiệm hóa ra Đại Ca giắt ngay dưới vòng kim cô |
| 19 | Chia tay đòi sao kê trà sữa, xé túi mù & tờ giấy nợ tiền điện | ⚡ Tổng kết drama tình phí chia tay đòi sao kê từng ly trà sữa từ 3 năm trước & cơn sốt xé túi mù (blindbox): Đại Ca bật Hỏa Nhãn Kim Tinh bóc mẽ sổ nợ trà sữa ghi khống của Heo Lười; Heo Lười lấy tiền chợ mua 10 túi mù khui ra đúng 10 cục đá cuội; La Sát tặng túi mù siêu to khui ra hóa đơn tiền điện máy lạnh 24/24 bắt đi rửa chén trừ nợ. | — | Hỏa Nhãn Kim Tinh, gậy Như Ý biến giấy nợ thành máy bay giấy | khui 10 túi mù ra 10 cục đá cuội; túi mù độc đắc của La Sát là hóa đơn tiền điện |
| 20 | Khóa học đêm chống tụt hậu, phép phân thân học hộ & cơm bình dân giá trên trời | ⚡ Tổng kết trend mở khóa học đêm chống sợ tụt hậu (FOMO), trào lưu trợ lý thông minh học hộ & drama cơm bình dân chặt chém: Heo Lười bật 5 màn hình học đêm rồi ngủ gật; Đại Ca hóa 3 khỉ phân thân học hộ nhưng bản sao lăn ra ngáy và đạp màn hình đặt đồ ăn khuya; Heo Lười la làng đĩa trứng mỏng lét giá 640 cành nhưng Hỏa Nhãn Kim Tinh soi ra 20 hộp chân gà ăn vụng dưới gầm ghế; La Sát quạt Ba Tiêu gom rác túi nilon bắt học khóa chà sàn tới sáng. | — | phép phân thân (3 khỉ tí hon học hộ), Hỏa Nhãn Kim Tinh, quạt Ba Tiêu | tưởng quán cơm chặt chém hóa ra tự đặt 20 hộp chân gà giấu gầm ghế; sợ tụt hậu học đêm thành học chà sàn |
| 21 | Trend 'chữa lành giữa trưa nắng', phông bạt cà phê 5 sao bằng ly tái chế & cú quạt Ba Tiêu đòi tiền rác | ⚡ Tổng kết trend gõ chuông xoay chữa lành & drama phông bạt gom vỏ ly cà phê sang chảnh sống ảo: Heo Lười mở tủ lạnh gõ nồi kho cá làm chuông xoay, tập thiền bay làm gãy ghế nhựa; xếp 10 vỏ ly giấy lượm ngoài hẻm giả làm tổng tài uống cà phê 5 sao nhưng bị Đại Ca khui ra trà đá nguội và sổ nợ bánh tráng trộn; La Sát quạt Ba Tiêu gom đống ly rác, thu tiền rác gấp đôi và bắt cả bọn quét hẻm phân loại rác. | — | gậy Như Ý hóa mây vàng đỡ Heo Lười, quạt Ba Tiêu gom rác | tổng tài cà phê 5 sao hóa ra uống trà đá nguội nợ tiền cá viên chiên; chữa lành trên mạng thành cầm chổi quét hẻm |
| 22 | Văn mẫu xin nghỉ gặp mùa cưới | ⚡ Tổng kết 3 drama mạng 08–09/11 (Tuổi Trẻ: văn mẫu xin nghỉ "Alo sếp nghe rõ không"; Tuổi Trẻ: đi cưới 500 nghìn bị chê; Dân trí: lớp 2 đổi chỗ ngồi "như lập trình"): giữa trưa nắng Heo Lười đắp khăn gọi chị chủ "Em sốt, nhức đầu, trời mưa to…" để khỏi đi cỗ cưới cháu La Sát vì sợ phong bì ("Mừng ít bị chê, mừng nhiều thì đói!"); Đại Ca gọi mưa cho "thật", mây vàng tí hon chỉ mưa đúng đầu Heo Lười, cả bọn "đổi chỗ như lập trình" mà mây vẫn bám; La Sát: "Mưa to ở mỗi đầu em à?"; Út Khờ mở thiệp: "Thiệp dặn không nhận phong bì mà."; La Sát: "Ốm thì ở nhà, cỗ chỉ đón người khỏe!"; Thầy: "Nói dối một câu, mưa theo cả ngày." | — | phép gọi mưa (mây mưa vàng tí hon bám người), lần đầu | nói dối ốm để né phong bì, hóa ra thiệp không nhận phong bì; đã khai ốm nên phải ở nhà, mất cỗ |
| 23 | Đứt chuỗi ba trăm ngày lúc nửa đêm | ⚡ Tổng kết 3 drama mạng 09–10/11 (Tuổi Trẻ: bạn bè giận nhau vì đứt chuỗi TikTok; Thanh Niên: chi tiền triệu thuê người "gánh" pickleball để được lên bục nhận giải; Tuổi Trẻ: đi làm phải "ghê gớm" mới không bị cướp công): gần nửa đêm Heo Lười khum tay che điện thoại như che nến: "Lửa chuỗi ba trăm ngày sắp tắt!", Đại Ca ngồi ngay cạnh vẫn đòi "đến lượt Heo Lười gửi"; hai đứa tranh công "Ngày nào cũng Heo Lười giữ lửa" – "Đại Ca giữ chứ!" và giật điện thoại khỏi bàn tay chìa ra của Út Khờ; Đại Ca dùng định thân pháp "cho lửa khỏi tắt" nhưng định trúng Út Khờ đang với lấy máy, lửa hóa xám; La Sát sang mắng "Nửa đêm gào gì thế mấy đứa?!", thấy Út Khờ đứng như tượng; "Oan!", đổ thừa; Út Khờ được giải phép, giơ quả chuối và cái bánh bao: "Cả hai đều thuê Út Khờ gánh chuỗi."; La Sát quay điện thoại ra: "Chuỗi của chị với Út Khờ vẫn cháy này!"; Thầy: "Tình bạn… đâu thuê ai giữ hộ được." | — | định thân pháp (lần hai, sau Tập 11), định nhầm người | hai đứa tranh công giữ chuỗi, hóa ra cùng lén thuê Út Khờ gánh hộ; chuỗi duy nhất còn cháy là chuỗi thật của Út Khờ với La Sát |

---

## 6. Các tập — mỗi ngày 1 tập

Mỗi tập (từ Tập 16: 30–60s = 3–6 clip × 10s; Tập 8–15: 30–60s = 3–6 clip) là một ngày đăng, nằm trong thư mục riêng `tap-{số}/` cùng thư mục này: `README.md` là tổng quan tập, `clip-1.md` … `clip-N.md` là prompt của từng clip 10 giây. Tập mới đánh số tiếp và dùng nguyên các khóa ở mục 1–3. Thư mục Tập 1–7 đã gỡ khỏi repo ở commit `d536686` (26/10/2026); nội dung vẫn còn trong lịch sử git (commit `4d7f4a4`) và tóm tắt ở mục 5.

| Ngày | File | Tên tập | Độ dài |
| --- | --- | --- | --- |
| 8 | [tap-8/](tap-8/README.md) | Vé nội bộ hóa lá khô | 30s · 3 clip |
| 9 | [tap-9/](tap-9/README.md) | Tên ở nhà | 60s · 6 clip |
| 10 | [tap-10/](tap-10/README.md) | Triều cường gõ cửa | 50s · 5 clip |
| 11 | [tap-11/](tap-11/README.md) | Dự án ma | 40s · 4 clip |
| 12 | [tap-12/](tap-12/README.md) | Săn sale nửa đêm | 40s · 4 clip |
| 13 | [tap-13/](tap-13/README.md) | Cúp điện giữa trưa | 60s · 6 clip |
| 14 | [tap-14/](tap-14/README.md) | Karaoke kẹo kéo xóm trọ | 50s · 5 clip |
| 15 | [tap-15/](tap-15/README.md) | Chùa online gõ mõ công đức & Bẫy cúng dường dỏm | 50s · 5 clip |
| 16 | [tap-16/](tap-16/README.md) | Cấm bóp còi thì… hét | 60s · 6 clip |
| 17 | [tap-17/](tap-17/README.md) | Đọ quai hàm chụp ảnh nhà trọ | 60s · 6 clip |
| 18 | [tap-18/](tap-18/README.md) | Đại hội tin nóng phòng trọ | 60s · 6 clip |
| 19 | [tap-19/](tap-19/README.md) | Chia tay đòi sao kê trà sữa & cơn sốt xé túi mù | 60s · 6 clip |
| 20 | [tap-20/](tap-20/README.md) | Khóa học đêm chống tụt hậu, phân thân học hộ & cơm bình dân giá trên trời | 60s · 6 clip |
| 21 | [tap-21/](tap-21/README.md) | Trend 'chữa lành giữa trưa nắng', phông bạt cà phê 5 sao & cú quạt Ba Tiêu đòi tiền rác | 60s · 6 clip |
| 22 | [tap-22/](tap-22/README.md) | Văn mẫu xin nghỉ, phong bì mừng cưới & đổi chỗ như lập trình | 60s · 6 clip |
| 23 | [tap-23/](tap-23/README.md) | Đứt chuỗi ba trăm ngày, thuê người gánh & tranh công lúc nửa đêm | 60s · 6 clip |
