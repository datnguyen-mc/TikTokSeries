# Tây Du Ký 2026 — Tập 9: Tên ở nhà

**Ngày 9** · Tập 60s = 6 clip × 10s · 9:16 · hoạt hình 2D · thoại tiếng Việt · không chữ trên video

**Tập ra mắt tên mới:** từ tập này bốn thầy trò mang tên ở nhà Thầy, Đại Ca, Heo Lười, Út Khờ. Chỉ câu mở của La Sát còn nhắc tên cũ để khán giả hiểu vì sao đổi; các tập sau chỉ dùng tên mới.

> **Cách dựng:** Clip 1 và Clip 4: **Video → Gemini Omni → Ingredients**, độ dài 10s, đính ảnh tham chiếu, dán prompt. Clip 2, 3, 5, 6: **Save frame** khung cuối clip trước → **Frames**, đặt làm **Start frame**, độ dài 10s, dán prompt; nếu Flow đã có **Extend** cho Omni thì bấm Extend trên clip trước rồi dán prompt clip sau, khỏi Save frame. Clip 4 mở lại bằng Ingredients để neo nhân vật (cắt theo hành động, không nhảy thời gian). Ghép 6 clip trong Scenebuilder. Chi tiết: FLOW_GUIDE mục 1.
> **Copy prompt:** mỗi file `clip-{số}.md` chỉ chứa đúng prompt: mở file, bấm Cmd+A rồi Cmd+C, dán thẳng vào ô prompt của Flow, không sửa gì.
> **Khóa nhân vật, bối cảnh, ảnh tham chiếu:** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Quy trình, xử lý lỗi:** [FLOW_GUIDE.md](../../FLOW_GUIDE.md)

← Hôm trước: [Tập 8 — Vé nội bộ hóa lá khô](../tap-8/README.md) · Hôm sau: [Tập 10 — Triều cường gõ cửa](../tap-10/README.md) →

---

**Tóm tắt:** Chiều trong hẻm, bà chủ trọ La Sát đứng ở cửa kêu "Tôn Ngộ Không! Trư Bát Giới!" tới hụt hơi, tới người thứ ba thì quên luôn: "Còn... Sa gì đó ta?". Người khổng lồ trong bếp vẫn ngoan ngoãn "Dạ!". Chị tuyên bố hẻm này ai cũng có tên ở nhà cho dễ kêu: nhà sư thì cả hẻm kêu "Thầy" sẵn rồi; chú heo đang nằm ăn bánh thành "Heo Lười", vừa cãi "siêng lắm" đã ngáy. Chú khỉ lùn nhất nhà đòi được kêu "Đại Ca", bị chê lùn nên dùng 72 phép biến hóa biến khổng lồ, nhưng gió quạt trần làm hắt xì, teo lại bằng cái tách trà. Người khổng lồ nâng Đại Ca tí hon lên tay: "Đại Ca nói phải." La Sát đặt cho anh tên "Út" vì bự nhất nhà mà là em út; chị vừa kêu "Heo Lười ơi!" thì Út lại "Dạ!" thay, thành "Út Khờ". Đại Ca hắt xì lần nữa, về lại cỡ cũ. Thầy chắp tay: "Tên đổi... lòng không đổi."

**Nhân vật & ảnh cần đính kèm:** Clip 1 và Clip 4: `TDK_REF_GROUP` (khóa tỉ lệ chiều cao bốn thầy trò) và `TDK_REF_LASAT`. Omni nhận nhiều ảnh hơn Veo, nên nếu Flow cho thì đính thêm ảnh lẻ `TDK_REF_THAY`, `TDK_REF_DAICA_A`, `TDK_REF_HEOLUOI`, `TDK_REF_UTKHO`. Chỉ dùng ảnh bản 2D. Đại Ca khổng lồ và Đại Ca tí hon là phép, đã tả trong prompt, không cần ảnh riêng.

**Trang phục:** mặc định (Đại Ca biến thể A; La Sát áo dài lụa đỏ như khóa 1.6).

**Đạo cụ:** quạt Ba Tiêu của La Sát cầm tay phải (bung ra chỉ lóe ánh vàng, không gió); bịch bánh phồng tôm trơn không nhãn và cây cào của Heo Lười; vá gỗ và nồi nhỏ trên bếp của Út Khờ. Bối cảnh: mục 2.1 của [FLOW_PROMPTS.md](../FLOW_PROMPTS.md); cả tập giữ một góc máy nhìn từ cửa vào để các clip nối khớp.

**Sản phẩm lồng ghép:** —

**Kịch bản nhanh:**

| Thời gian | Hình ảnh | Thoại |
| --- | --- | --- |
| 00:00–00:03 | La Sát đứng ở cửa, hít một hơi thật sâu, khum tay kêu vô nhà thật to **(hook)** | La Sát: "Tôn Ngộ Không! Trư Bát Giới!" |
| 00:03–00:05 | Hụt hơi, chị ngước lên trần, gõ quạt vô cằm, quên mất tên người thứ ba | La Sát: "Còn... Sa gì đó ta?" |
| 00:05–00:07 | Toàn cảnh: người khổng lồ trong bếp vẫn giơ tay dạ; Đại Ca trên tủ lạnh bật cười, Heo Lười nằm ăn, Thầy ngồi thiền | Út Khờ: "Dạ!" |
| 00:07–00:10 | La Sát bung quạt (chỉ lóe ánh vàng, không gió), quạt lấy quạt để | La Sát: "Tên gì dài thòng, kêu muốn hụt hơi!" |
| 00:10–00:13 | La Sát gập quạt, sải bước vô giữa phòng, chỉ quạt quanh một vòng như cô giáo cầm thước | La Sát: "Hẻm này ai cũng có tên ở nhà!" |
| 00:13–00:15 | Chị quay sang Thầy, cúi đầu lễ phép, giọng dịu hẳn | La Sát: "Thầy thì cả hẻm kêu Thầy rồi." |
| 00:15–00:17 | Thầy mở mắt, chắp tay, cười hiền | Thầy: "Gọi sao cũng là duyên." |
| 00:17–00:20 | Quạt chỉ sang sofa: chú heo nằm ngửa nhai bánh phồng tôm, lấy cào gãi lưng | La Sát: "Còn đứa này... Heo Lười!" |
| 00:20–00:23 | Heo Lười chống khuỷu tay dậy, vung cào phản đối, má còn phồng bánh | Heo Lười: "Oan! Heo này siêng lắm mà!" |
| 00:23–00:25 | Chưa cãi xong đã ngáp một cái thật dài, nằm vật xuống ngáy luôn | Út Khờ: "Ngủ rồi." |
| 00:25–00:28 | Chú khỉ lộn nhào từ tủ lạnh xuống đứng trước mặt La Sát, vỗ ngực; đứng dưới đất chỉ tới ngực chị | Đại Ca: "Tui lớn nhứt, kêu Đại Ca!" |
| 00:28–00:30 | La Sát nhìn xuống, che quạt nhịn cười | La Sát: "Lùn nhứt nhà mà Đại Ca?" |
| 00:30–00:32 | Cắt theo hành động: Đại Ca nhổ một sợi lông thổi phù, khói kim tuyến vàng bùng quanh người | Đại Ca: "Biến!" |
| 00:32–00:35 | 72 phép biến hóa: Đại Ca thành khổng lồ, đầu sát trần nhà cạnh quạt trần, gồng tay nhìn xuống La Sát | Đại Ca: "Giờ ai lớn nhứt?" |
| 00:35–00:37 | Heo Lười giật mình thức, dụi mắt ngước nhìn, miếng bánh khựng giữa chừng | Heo Lười: "Ăn gì mà lớn dữ vậy?" |
| 00:37–00:40 | Gió quạt trần làm nhột mũi, Đại Ca hắt xì một cái, bụp ánh vàng, teo lại bằng cái tách trà | Đại Ca: "Ủa... nhỏ xíu?" |
| 00:40–00:43 | Heo Lười lại ngủ; người khổng lồ bước tới, quỳ xuống nâng Đại Ca tí hon lên lòng bàn tay, nghiêm túc tuyệt đối | Út Khờ: "Đại Ca nói phải." |
| 00:43–00:45 | La Sát ngước nhìn người cao nhất nhà, gõ quạt vô cằm | La Sát: "Bự nhứt nhà... mà là Út!" |
| 00:45–00:47 | Chị thử kêu tên mới về phía sofa; Heo Lười vẫn ngáy | La Sát: "Heo Lười ơi!" |
| 00:47–00:49 | Heo Lười không nhúc nhích, Út lại giơ tay dạ thay | Út Khờ: "Dạ!" |
| 00:49–00:50 | La Sát đập quạt lên trán, bật cười | — |
| 00:50–00:52 | La Sát vừa cười vừa chỉ quạt lên người khổng lồ | La Sát: "Út... Khờ luôn!" |
| 00:52–00:54 | Đại Ca tí hon hắt xì lần nữa, bụp, về lại cỡ cũ, đáp xuống tạo dáng | Đại Ca: "Đại Ca về rồi!" |
| 00:54–00:57 | Thầy đứng dậy khỏi bồ đoàn, chắp tay, cười ấm áp | Thầy: "A Di Đà Phật... tên đổi, lòng không đổi." |
| 00:57–00:59 | Cả nhà đứng giữa phòng; Heo Lười vẫn ngáy, thổi bong bóng mũi | — |
| 00:59–01:00 | Cả năm đứng yên **(thumbnail)** | — |

## Các clip — mỗi file là nguyên một prompt, copy cả file dán vào Flow

| Clip | Thời gian | Cách tạo | File prompt |
| --- | --- | --- | --- |
| 1 | 00:00–00:10 | Ingredients: đính `TDK_REF_GROUP`, `TDK_REF_LASAT` | [clip-1.md](clip-1.md) |
| 2 | 00:10–00:20 | Frames: start frame = khung cuối clip 1 (hoặc Extend) | [clip-2.md](clip-2.md) |
| 3 | 00:20–00:30 | Frames: start frame = khung cuối clip 2 (hoặc Extend) | [clip-3.md](clip-3.md) |
| 4 | 00:30–00:40 | Ingredients, neo lại nhân vật (cắt theo hành động): đính ảnh như Clip 1 | [clip-4.md](clip-4.md) |
| 5 | 00:40–00:50 | Frames: start frame = khung cuối clip 4 (hoặc Extend) | [clip-5.md](clip-5.md) |
| 6 | 00:50–01:00 | Frames: start frame = khung cuối clip 5 (hoặc Extend) | [clip-6.md](clip-6.md) |

**Ghi chú Tập 9:**
- **Tên ở nhà là chuyện thật của xóm hẻm miền Nam:** con út hay được kêu "Út", đứa mũm mĩm hay được kêu "Heo", còn nhà sư thì ai cũng gọi là "Thầy". La Sát đặt tên đúng kiểu đó nên video không cần giải thích thêm.
- **Tên cũ chỉ có ở hai câu mở** của La Sát ("Tôn Ngộ Không! Trư Bát Giới!", "Còn... Sa gì đó ta?"), là cái cớ để đặt tên ở nhà; từ 00:05 trở đi và ở mọi tập sau chỉ dùng tên mới.
- **Giọng Đại Ca đổi theo phép:** to và trầm khi khổng lồ, chút chít khi tí hon, về giọng cũ ở Clip 6. Nếu Omni giữ luôn giọng lạ sang clip sau thì tạo lại clip đó, hoặc lồng tiếng lại câu đó trong CapCut.
- **Đại Ca khổng lồ không đụng quạt trần** (đã chặn trong [AVOID]); nếu model cho đầu chạm quạt hay làm vỡ đồ thì tạo lại Clip 4.
- **Gag chính là Út Khờ "Dạ!" thay Heo Lười** ở 00:47: nếu Omni để Heo Lười trả lời thì tạo lại Clip 5.
- **Gợi ý caption:** "Ở hẻm Sài Gòn ai cũng có tên ở nhà. Nhà trọ này giờ có Thầy, Đại Ca, Heo Lười với Út Khờ. Nhà bạn ai có tên ở nhà dễ thương nhất?" · hashtag gợi ý: #tayduky2026 #tenonha #daica #heoluoi #utkho #haihuoc
