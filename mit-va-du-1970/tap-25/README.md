# Mít và Đú (1970) — Tập 25: Đôi dép đứt quai của Nở & Màn hất chảo đội nón bánh xèo củ hủ dừa của ba Mit

**Ngày 25** · **Phim tình cảm gia đình miền Tây những năm 1970 cảm động & hài hước** · **Tập dài 60 giây = 6 clip × 10s** · **9:16 Dọc** · **Hoạt hình 3D**

> **Cách dựng:** cả 6 clip đều render **Ingredients** (`@Mit`, `@Đú`, `@Nở`), không dùng khung cuối của clip trước (runner `mit_va_du.py` từ 07/11). Vì vậy mỗi prompt tự mang đủ bối cảnh, đạo cụ và trạng thái nhân vật (xem mục 3). Mỗi clip là `ONE CONTINUOUS SHOT`; giữa các clip là cắt cảnh.

---

## 1. Câu chuyện gia đình thập niên 1970 (Cảm động & Hài hước)
Chiều quê Cái Mơn – Bến Tre năm 1970, bé Nở đi học về bị đứt quai đôi dép mủ cũ phải đi chân trần vào sân. Ba Mit đi đốn dừa mướn về mang theo khúc **củ hủ dừa trắng nõn ngọt lịm** và âm thầm giấu một bọc giấy nhỏ trong giỏ tre. Chiều đó, ngay ngoài sân, ba Mit đội chiếc rổ tre lên đầu làm "nón đầu bếp", giành phần đứng tráng **bánh xèo củ hủ dừa tép đồng** trên chảo gang bếp củi cho vợ con. Muốn lấy le biểu diễn màn "hất chảo lật bánh xèo trên không", ba Mit hất mạnh tay làm cái bánh xèo vàng giòn bay vút lên rồi đáp bộp ngay trên chiếc rổ đội đầu như cái nón lá vàng khè, làm hai mẹ con cười nghiêng ngả! Sau bữa bánh xèo cuốn cải bẹ xanh ấm cúng, ba Mit quỳ xuống mang đôi dép mới tinh vào chân cho Nở. Cả tập diễn ra ở sân trước nhà tre, trong cùng một buổi chiều vàng. Khoảnh khắc má Đú nhìn thấy gót chân trần của chồng phải quấn vải trắng vì dẫm gai dừa mà vẫn nhường hết tiền công mua dép mới cho con khiến cả nhà rưng rưng ôm chầm lấy nhau.

## 2. Danh sách 6 Clip Prompt (60 giây = 6 clips × 10s)

| Clip | Thời lượng | Nội dung phân cảnh | File Prompt |
| :---: | :---: | :--- | :---: |
| **Clip 1** | `00:00–00:10` | Bé Nở đưa má đôi dép đứt quai; ba Mit vác củ hủ dừa về và giấu bọc giấy trong giỏ | [clip-1.md](clip-1.md) |
| **Clip 2** | `00:10–00:20` | Ba Mit đội rổ tre làm đầu bếp, tráng bánh xèo củ hủ dừa tép đồng và đòi hất chảo lật bánh | [clip-2.md](clip-2.md) |
| **Clip 3** | `00:20–00:30` | Miếng hài hình thể: bánh xèo bay lên không đáp gọn lên rổ tre trên đầu ba Mit như cái nón vàng | [clip-3.md](clip-3.md) |
| **Clip 4** | `00:30–00:40` | Cả nhà quây quần cuốn bánh xèo củ hủ dừa với cải bẹ xanh chấm nước mắm chua ngọt giòn rụm | [clip-4.md](clip-4.md) |
| **Clip 5** | `00:40–00:50` | Cao trào xúc động: ba Mit mang dép mới cho con, lộ bàn chân trần quấn vải vì dẫm gai dừa | [clip-5.md](clip-5.md) |
| **Clip 6** | `00:50–01:00` | Bé Nở vẽ tranh "ba đội nón bánh xèo" vào tập vở (`SP_TAP`, `SP_BUTMAU`), cả nhà ôm nhau ấm áp | [clip-6.md](clip-6.md) |

- **Caption:** [caption.md](caption.md)

## 3. Khóa bối cảnh & đạo cụ (giống hệt nhau ở cả 6 clip)

Mỗi clip có các khối `[SET LOCK]`, `[CHARACTER STATE IN THIS CLIP]`, `[PROPS IN THIS CLIP]`, `[BLOCKING]` và `[END FRAME]`. Mỗi đạo cụ được tả bằng đúng một câu, chép y nguyên sang mọi clip có đạo cụ đó.

- **Không gian:** chỉ một bối cảnh là sân trước nhà tre, nắng vàng cuối chiều chiếu từ bên trái. Máy quay luôn đứng trong sân nhìn vào nhà, không vào trong nhà, không đèn dầu, không trời tối.
- **Sơ đồ cố định:** nhà tre và lu nước ở phía sau; kênh và xuồng ba lá phía sau bên trái; bàn gỗ thấp ở giữa với 3 ghế đẩu (Nở đầu trái, Đú giữa, Mit đầu phải); cà ràng và chảo gang ở tiền cảnh bên phải, luôn xa Nở.
- **Mit:** áo ba lỗ xám, quần đùi, chân trần, **gót chân phải quấn vải trắng ở cả 6 clip** (clip 5 mới lộ ra cho má Đú thấy). Đội **rổ tre chỉ ở clip 2–3**; các clip 1, 4, 5, 6 không đội gì trên đầu.
- **Nở:** luôn mặc áo vàng hoa nhí và váy nâu, luôn đi hoặc ngồi bằng hai chân như em bé. Đi **chân trần ở clip 1–4**, được mang **dép mới màu mật ong ở clip 5**, và mang dép đó ở clip 6.
- **Đạo cụ theo clip:**

| Đạo cụ | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Dép cũ đứt quai | Nở → Đú | — | — | — | — | — |
| Củ hủ dừa nguyên khúc | tay Mit → bàn | — | — | — | — | — |
| Giỏ tre (bọc quà bên trong) | tay trái Mit | đất, cạnh ghế Mit | đất | đất (Mit lấy bọc quà ra) | đất, rỗng | đất, rỗng |
| Bọc giấy nâu | trong giỏ | trong giỏ | trong giỏ | trên đùi Mit | mở ra → dép mới | — |
| Cà ràng + chảo gang | nguội | lửa nhỏ | lửa nhỏ, chảo trong tay Mit | than đỏ lụi | than đỏ lụi | than đỏ lụi |
| Bột, củ hủ dừa thái sợi, tép | — | đầu phải bàn | đầu phải bàn | — | — | — |
| Mâm bánh xèo, cải bẹ xanh, nước mắm | — | — | — | giữa bàn | giữa bàn | giữa bàn |
| `SP_TAP` + `SP_BUTMAU` | đóng, đầu trái bàn | đóng | đóng | đóng | đóng | mở, tranh "ba đội nón bánh xèo" |

