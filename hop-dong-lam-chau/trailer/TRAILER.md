# Trailer — Hợp Đồng Làm Cháu (~60 giây, 16:9)

*Sinh bởi `_tools/build_flow_files.py`.* Trailer chỉ dùng nửa đầu phim, **không lộ cú lật** (ông biết từ đầu). Mỗi shot là một lần tạo trên Flow: **Video → Gemini Omni → Ingredients**, đính đúng các nhân vật ở cột *Đính*, dán nguyên file `prompts/TR-XX.txt`, đặt tên clip trên Flow là `TR-XX · <tên>` để `make_trailer.py` nhận ra. TR-09 không có nhân vật: dùng Text-to-Video.

| Shot | Tên trên Flow | Giây | Đính | Thoại |
|---|---|---|---|---|
| TR-01 | TR-01 · Bà dúi phong bì | 5 | Bà Mận · Áo bông đi đường, Đạt · Bomber ra mắt | Bà Mận: Năm ngày thôi. Cháu làm cháu nội tôi, đừng để ông biết. |
| TR-02 | TR-02 · Ông ơi cháu về rồi | 3 | Đạt · Bomber ra mắt | Đạt: Ông ơi! Cháu về rồi! |
| TR-03 | TR-03 · Mười năm lùn đi | 4 | Ông Thịnh · Áo nâu ở nhà | Ông Thịnh: Mười năm… mà mày lùn đi à? |
| TR-04 | TR-04 · Dị ứng lạc | 3 | Đạt · Bomber ra mắt | Đạt: Ngứa! Ngứa quá! |
| TR-05 | TR-05 · Bà Thoa qua rào | 4 | Bà Thoa · Áo nhung hoa | Bà Thoa: Lạ nhỉ! Thằng Minh hồi bé dị ứng lạc cơ mà? |
| TR-06 | TR-06 · Gói bánh chưng | 4 | Ông Thịnh · Áo nâu ở nhà, Đạt · Áo len mượn | — |
| TR-07 | TR-07 · Ông giận ông | 5 | Ông Thịnh · Áo len đêm, Đạt · Áo len mượn | Ông Thịnh: Ông không giận cháu. Ông giận ông. |
| TR-08 | TR-08 · Thằng đấy là ai | 4 | Minh · Áo đầu bếp | Minh: Thằng đấy… là ai? |
| TR-09 | TR-09 · Xe khách đêm | 3 | — (Text-to-Video) | — |
| TR-10 | TR-10 · Hai thằng Minh | 4 | Minh · Áo dạ đen, Đạt · Áo phao đỏ | — |
| TR-11 | TR-11 · Đứa nào cháu thật | 3 | Bà Thoa · Áo nhung hoa | Bà Thoa: Thế đứa nào là cháu thật? |
| TR-12 | TR-12 · Minh vào ăn sáng | 4 | Ông Thịnh · Áo bông xanh | Ông Thịnh: Minh, vào ăn sáng con. |
| TR-13 | TR-13 · Minh chết lặng | 3 | Minh · Áo dạ đen | — |

## Dựng

Tải các clip về `trailer/clips/` rồi chạy `python3 hop-dong-lam-chau/trailer/make_trailer.py hop-dong-lam-chau/trailer/clips`. Script chèn thẻ chữ (26 THÁNG CHẠP · MỘT ĐỨA CHÁU THUÊ… · …MỘT ĐỨA CHÁU THẬT · tựa phim · RA MẮT TRƯỚC TẾT) giữa các shot. Nhạc nền thêm khi hậu kỳ.
