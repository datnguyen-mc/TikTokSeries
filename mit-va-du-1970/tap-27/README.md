# Mít và Đú (1970) — Tập 27: Con bù nhìn rơm giống ba & Bầy chim sẻ phá ruộng lúa chín

**Ngày 27** · **Phim tình cảm gia đình miền Tây những năm 1970 cảm động & hài hước** · **Tập dài 60 giây = 6 clip × 10s** · **9:16 Dọc** · **Hoạt hình 3D**

> **Cách dựng:** cả 6 clip đều render **Ingredients** (chỉ gắn ảnh của nhân vật có mặt trong clip), không dùng khung cuối của clip trước. Mỗi prompt tự mang đủ bối cảnh, đạo cụ và trạng thái nhân vật (xem mục 3). Mỗi clip là `ONE CONTINUOUS SHOT`; giữa các clip là cắt cảnh. **Tập thôn quê, không nấu ăn, không ăn uống gì (chỉ có ly nước má mang ra đồng cho ba).**

---

## 1. Câu chuyện (Cảm động & Hài hước)
Cuối mùa lúa ở Cái Mơn – Bến Tre năm 1970, đám ruộng nhỏ bên bờ kênh của nhà Mit đang chín vàng thì bầy **chim sẻ** kéo về phá. Ba Mit đứng trên bờ ruộng vẫy tay, vỗ tay đuổi, chim bay lên một vòng rồi đáp lại y chỗ cũ; bé Nở đứng trên bờ đất khô cười khúc khích: "Chim hổng sợ ba chút nào hết trơn!" Ba chống nạnh: "Được, ba làm con bù nhìn canh lúa liền!" Ngoài sân, ba buộc khung tre chữ thập, má Đú đưa cái áo cũ bạc màu của má với mấy bó rơm, Nở nhồi rơm cho bụng bù nhìn "mập mập". Dựng lên rồi mới thấy: bụng rơm tròn vo, hai túm rơm rủ hai bên như tai, đội nón lá, đứng kế ba thì **giống ba y chang**, hai mẹ con cười nghiêng ngả. Ra ruộng cắm bù nhìn, ai dè chim sẻ đậu nguyên hàng trên tay nó; ba đứng kế bên vỗ cánh đuổi, Nở chỉ ba: "Ba mới là con bù nhìn thiệt nè!" Chiều tà, má Đú mang ly nước ra bờ ruộng, ba mới nói thiệt: mùa lúa này là tiền học cả năm của Nở; má lặng lẽ tựa đầu vào vai ba. Hoàng hôn, bầy chim bay về tổ, Nở chạy ra khoe trang tập (`SP_TAP`, `SP_BUTMAU`) vẽ hai con bù nhìn đứng cạnh nhau — "con bù nhìn với ba" — cả nhà cười vang giữa ruộng lúa vàng.

## 2. Danh sách 6 Clip Prompt (60 giây = 6 clips × 10s)

| Clip | Thời lượng | Bối cảnh | Nội dung phân cảnh | File Prompt |
| :---: | :---: | :---: | :--- | :---: |
| **Clip 1** | `00:00–00:10` | A · Bờ ruộng, chiều | Mở màn máy cẩu hạ từ trên ruộng lúa chín; bầy chim sẻ phá lúa, ba Mit vẫy tay vỗ tay đuổi, chim bay một vòng rồi đáp lại; Nở đứng trên bờ đất khô cười; ba hứa làm bù nhìn | [clip-1.md](clip-1.md) |
| **Clip 2** | `00:10–00:20` | B · Sân trước, chiều | Ba Mit siết dây khung tre chữ thập; má Đú đưa áo cũ và bó rơm; Nở nhồi rơm cho bụng bù nhìn "mập mập" | [clip-2.md](clip-2.md) |
| **Clip 3** | `00:20–00:30` | B · Sân trước, chiều | Miếng hài: ba dựng con bù nhìn đội nón lá đứng lên, bụng rơm tròn và tai rơm rủ — giống ba y chang; hai mẹ con cười, ba vỗ bụng ngơ ngác | [clip-3.md](clip-3.md) |
| **Clip 4** | `00:30–00:40` | A · Bờ ruộng, chiều | Ba cắm bù nhìn ở mép ruộng; chim sẻ vẫn đậu nguyên hàng trên tay nó; ba đứng kế bên vỗ cánh đuổi — "con bù nhìn thiệt" | [clip-4.md](clip-4.md) |
| **Clip 5** | `00:40–00:50` | C · Bờ ruộng, hoàng hôn | Nốt lặng: má Đú mang ly nước ra cho ba; ba nói mùa lúa này là tiền học cả năm của Nở; má tựa đầu vào vai ba | [clip-5.md](clip-5.md) |
| **Clip 6** | `00:50–01:00` | C · Bờ ruộng, hoàng hôn | Bầy chim bay về tổ; Nở khoe tranh hai con bù nhìn trong tập (`SP_TAP`, `SP_BUTMAU`) — "con bù nhìn với ba"; cả nhà cười vang | [clip-6.md](clip-6.md) |

- **Caption:** [caption.md](caption.md)

## 3. Khóa bối cảnh & đạo cụ

Mỗi clip có các khối `[SET LOCK]`, `[CHARACTER STATE IN THIS CLIP]`, `[PROPS IN THIS CLIP]`, `[BLOCKING]` và `[END FRAME]`. Mỗi bối cảnh có **một** khối `[SET LOCK]` chép y nguyên vào mọi clip quay ở đó; mỗi đạo cụ được tả bằng đúng một câu, chép y nguyên sang mọi clip có đạo cụ đó.

- **Bối cảnh A — Bờ ruộng cạnh kênh, chiều vàng (clip 1, 4):** nắng chiều thấp từ bên trái; máy quay đứng trên cỏ khô phía ngoài bờ ruộng, nhìn vào ruộng. Tiền cảnh là bờ ruộng đất khô chạy ngang khung hình; giữa là ruộng lúa chín cao ngang hông người lớn trên nền đất đã rút nước khô; nền là con kênh sau hàng dừa nước, dừa cao bên kia kênh, mái lá nhà tre xa xa bên trái. Mọi người chỉ đứng/ngồi trên bờ ruộng khô; không ai bước xuống ruộng hay lại gần mép nước.
- **Bối cảnh C — Cùng bờ ruộng lúc hoàng hôn (clip 5, 6):** bố cục y hệt A, chỉ đổi giờ: mặt trời sát hàng dừa bên trái, trời cam hồng, bóng đổ dài sang phải, vẫn còn sáng rõ (không phải đêm).
- **Bối cảnh B — Sân trước nhà tre, chiều (clip 2, 3):** giữ bố cục sân của series (nhà tre + lu nước phía sau, kênh và xuồng ba lá xa phía sau bên trái, bàn gỗ thấp với 3 ghế đẩu để trống ở giữa), thay giàn phơi bằng **một đống rơm** bên phải bàn; khoảng sân trống ở tiền cảnh là chỗ làm bù nhìn. Không bếp, không lửa, không nấu ăn.
- **Mit:** áo ba lỗ xám, quần đùi, chân trần, **không đội gì** ở cả 6 clip.
- **Đú:** có mặt ở clip 2, 3, 5, 6; áo bà ba hồng hoa nhí, quần đen, dép nâu, không đội gì.
- **Nở:** có mặt ở clip 1, 2, 3, 4, 6 (clip 5 chỉ có ba má); áo vàng hoa nhí, váy nâu, dép nâu, luôn đứng/đi bằng hai chân, không đội gì; ở ruộng luôn đứng trên bờ đất khô, xa mép nước.
- **Nón lá:** chỉ nằm trên đầu **con bù nhìn** (clip 3–6); không nhân vật nào đội gì trên đầu.
- **Chim sẻ:** chỉ bị đuổi bằng vẫy tay, vỗ tay; không ai chạm vào chim, không ná, không đá, không lưới.
- **Con bù nhìn:** một câu mô tả chép y nguyên ở clip 3–6 — khung tre chữ thập buộc dây xơ dừa, mặc áo cũ xám bạc màu của má, nhồi rơm bụng tròn, đầu rơm có hai túm rơm rủ như tai, chân mày xơ dừa, mắt nút gáo dừa, đội nón lá; là vật vô tri, không tự cử động. Cây cán tre không bao giờ chĩa vào ai.
- **Đạo cụ theo clip:**

| Đạo cụ | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Bầy chim sẻ | đáp xuống lúa → bay lên → đáp lại | — | — | đậu hàng trên tay bù nhìn + vành nón | — | bay về tổ |
| Khung bù nhìn (tre chữ thập + đầu rơm) | — | nằm dưới đất, Mit siết dây | — | — | — | — |
| Áo cũ xám bạc màu của má | — | tay Đú → Mit cài lên khung | trên bù nhìn | trên bù nhìn | trên bù nhìn | trên bù nhìn |
| Bó rơm | — | 1 dưới nách Đú + 2 cạnh Nở; Nở nhồi rơm | — | — | — | — |
| Bù nhìn hoàn chỉnh + nón lá | — | — | nằm → Mit dựng đứng, giữ cán | tay Mit → cắm ở mép ruộng | đứng ở mép ruộng | đứng ở mép ruộng |
| Ly đất nung đựng nước | — | — | — | — | tay Đú → Mit | — |
| `SP_TAP` + `SP_BUTMAU` | — | — | — | — | — | tập mở, tranh hai con bù nhìn; hộp bút kẹp nách |

## 4. Thoại (đúng như trong prompt, giọng Nam Bộ)

| Clip | Thời điểm | Người nói | Câu thoại | Âm tiết / giây |
| :---: | :---: | :---: | :--- | :---: |
| 1 | `00:04–00:07` | Nở | Chim hổng sợ ba chút nào hết trơn! | 8 / 3s |
| 1 | `00:07–00:10` | Mit | Được, ba làm con bù nhìn canh lúa liền! | 9 / 3s |
| 2 | `00:00–00:04.5` | Đú | Áo cũ của em đó, cho nó mặc đi mình. | 10 / 4.5s |
| 2 | `00:04.5–00:08` | Mit | Nhồi thêm rơm cho nó mập mập nghen con! | 9 / 3.5s |
| 3 | `00:04–00:07` | Nở | Má ơi, nó giống ba y chang! | 7 / 3s |
| 3 | `00:07–00:10` | Mit | Ủa, bụng ba bự dữ vậy hả? | 7 / 3s |
| 4 | `00:00–00:04` | Mit | Canh lúa giùm nghen, ông bù nhìn! | 7 / 4s |
| 4 | `00:07–00:10` | Nở | Ba mới là con bù nhìn thiệt nè! | 8 / 3s |
| 5 | `00:00–00:04.5` | Đú | Mình uống miếng nước đi, canh cả buổi rồi. | 9 / 4.5s |
| 5 | `00:04.5–00:08.5` | Mit | Mùa lúa này là tiền học cả năm của con Nở đó mình. | 13 / 4s |
| 6 | `00:03–00:06` | Nở | Con vẽ con bù nhìn với ba nè! | 8 / 3s |
| 6 | `00:06–00:09` | Mit | Ba với nó canh lúa cho con đi học mà! | 10 / 3s |
