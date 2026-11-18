# Nhật ký Flow — Ai Là Vợ Bệnh Nhân?

Project: https://flow.google.com/project/45268b8f-8bfd-459f-a027-247f4a7d2499 (tạo 18/11/2026, tài khoản Ultra)
Mở nhân vật: `.../project/45268b8f-8bfd-459f-a027-247f4a7d2499/character/<id>`
Giọng: không gắn preset; giọng do câu tả giọng cố định trong prompt quyết định (`_tools/phim.py`, PEOPLE[...]["voice"]).

## Nhân vật theo bộ đồ (16/16 đã có ảnh, tạo 18/11/2026 bằng Nano Banana 2.1)

Bộ gốc (HA1, MA1, LY1, DU2, TH1, BV1, OL1) tạo bằng prompt đầy đủ; các bộ còn lại tạo bằng cách đính nhân vật gốc vào ô lệnh rồi tả bộ đồ mới.

| Mã | Tên trên Flow | ID |
|---|---|---|
| HA1 | Hạnh · Vest xám | 77abf8a5-cfbe-470c-892d-ed6294913bd6 |
| HA2 | Hạnh · Sơ mi ngà | 85173985-3a15-435e-b683-6085f9936de9 |
| HA3 | Hạnh · Cô dâu áo dài đỏ | ad665e96-2e38-4491-b705-95330b997ae0 |
| HA4 | Hạnh · Ở nhà | 4165980e-3cc3-4529-941b-f27744c310e4 |
| MA1 | Mai · Đồ ngủ hồng | 3ee7ddd0-1143-4299-b2d0-8e359b2effc5 |
| MA2 | Mai · Khoác vest xám | a59ccfd4-f0fc-4f1a-a82b-22a6680961bd |
| MA3 | Mai · Cô dâu váy trắng | 7d7e101b-d716-4392-b2aa-d3d2d8fa0318 |
| MA4 | Mai · Ở nhà | e6229219-965b-496c-8bae-e147b9c5ac71 |
| LY1 | Ly · Váy xanh lam | eede8d3e-1f52-4c4c-9d05-84af099fb988 |
| DU1 | Dũng · Áo bệnh nhân | 0bdcb59a-ae7e-466f-9fe5-f1ce0cd34316 |
| DU2 | Dũng · Sơ mi trắng | bf723518-70ba-4fb9-8626-92676d4425a5 |
| DU3 | Dũng · Vest xám chú rể | 9681be2d-0a1e-4858-a385-006440669c43 |
| TH1 | Chị Thơm · Điều dưỡng | 5fa7b78a-d144-4385-a491-a385a185ddd3 |
| BV1 | Bà Vượng · Áo bông nâu | f7d9e4da-35fe-4147-b151-5eb9cda71f61 |
| BV2 | Bà Vượng · Áo dài nhung | 3e5ceac0-d56c-43a9-aa8e-ce697990a163 |
| OL1 | Ông Lộc · Gi-lê len | 0ab944c4-b323-4ef9-9252-87d2c6f51f21 |

Lưu ý khi tạo: Flow báo "hoạt động bất thường" nếu gửi hai lệnh tạo cách nhau dưới ~30 giây hoặc rời trang khi ảnh chưa xong. Gửi từng lệnh một, chờ xong mới gửi tiếp.

## Clip đã render

Quy trình: mỗi clip quay xong được đổi tên trên Flow thành `VBN <shot> · <tên>`, tải 720p về ~/Downloads (`VBN_<shot>_…mp4`), rồi `python3 ai-la-vo-benh-nhan/_tools/gom_clip.py` chép vào `film/clips/<shot>.mp4`. Clip hỏng giữ lại trong `film/_loi/`.

Kiểm tra sau khi quay: xem khung hình (`film/_check/*.jpg`) và nghe lại thoại bằng nhận dạng giọng nói tiếng Việt.

| Shot | Trạng thái | Ghi chú (18/11/2026) |
|---|---|---|
| 00-01 | đạt | đèn đỏ, đồng hồ, cửa sổ mưa; không lời |
| 00-02 | đạt | thoại đúng: "Ai là người nhà bệnh nhân Dũng?" |
| 00-03 | QUAY LẠI | chỉ nói được "Tôi." — đã đổi thoại thành "Tôi là vợ anh ấy." |
| 00-04 | đạt | thoại đúng: "Em! Em là vợ ạ!" |
| 00-05 | đạt | hai người quay sang nhìn nhau; không lời |
| 00-06 | đạt | thoại đúng: "Bệnh nhân này… có mấy vợ?" |
| 00-07 | QUAY LẠI | hình dính viền khung phim bo góc — đã thêm câu chống viền vào [LOOK] |
| 01-01 | đạt | Hạnh chốt sổ, điện thoại rung; không lời |
| 01-02 | đã quay, chưa tải được | Flow đăng xuất giữa chừng |
| 01-03 | lỗi | Flow báo "có thể vi phạm chính sách" (được hoàn tín dụng) — thử lại |
| 01-04 | lỗi | "không tạo được video" đúng lúc phiên đăng nhập hết hạn — thử lại |

Sự cố 18/11 ~10:16: Flow báo "Không lưu được một số nội dung", tải lại trang thì tài khoản Google đã bị đăng xuất → phải đăng nhập lại mới quay tiếp được.
