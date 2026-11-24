# Bức Tường Mỏng — Rà lỗi kịch bản trên giấy (bản 1)

*23/11/2026. Rà toàn bộ 293 shot theo `chi-oi-den-roi/REVIEW_PROMPT.md` (mục A–D, H) trước khi tạo ảnh và render. Mục E–G (kỹ thuật hình, tiếng, phụ đề) chỉ rà được sau khi có clip.*

## Con số

| | |
|---|---|
| Cảnh / shot | 25 cảnh · 293 shot |
| Thời lượng thô | 26:04 (sau khi cắt đầu đuôi clip, dự kiến **~23–24 phút**, cộng thẻ chữ và nhạc kết ≈ 25 phút) |
| Cần tạo trên Flow | 1.564 giây video, ước **~6.250 credit** (Omni 1.2 Flash, 720p, x1), chưa tính làm lại |
| Ảnh nhân vật | 27 ảnh: 17 bộ đồ + 10 ảnh sau lưng cho góc qua vai |

## Máy kiểm tra (build.py + review_paper.py) — đạt
- Mỗi shot tối đa 2 nhân vật gắn ảnh; ai nói thì phải có trong khung; sắc thái đủ "en|vi".
- Không câu thoại nào lặp lại nguyên văn; không có chữ số trong thoại (số căn hộ viết bằng chữ: "mười hai không sáu").
- Không nhắc @tên của người không gắn ảnh trong camera/hành động (tránh lộ mặt lạ).
- Tường chung: trong phòng thu nhà Ngân luôn ở **bên PHẢI khung**, trong phòng ngủ nhà Diễm luôn **bên TRÁI**; hành lang: cửa nhà Ngân trái, cửa nhà Diễm phải; ban công: vách ngăn bên phải khi đứng phía Ngân.
- Nhẫn cưới: còn trên tay Hưng đến 21-08 (tháo nhẫn); từ cảnh 22 chỉ dùng bộ "Sơ mi nhàu không nhẫn" + dòng cấm nhẫn.
- Vòng của mẹ: trên tay Diễm từ cảnh 10 đến 22-02; sau đó trên tay Ngân (22-10, 24-02); Diễm cổ tay trống ở 24-06.
- Mỗi cảnh một bộ đồ / người. Ba chỗ đổi đồ có chủ đích: 02 (Hưng thay com-lê đi làm), 06 (Hưng cởi vest sang nhà bên, áo vest còn vắt ở đó trong cảnh 08), 06 (Diễm về nhà thay đồ).

## Lỗi tìm thấy khi rà tay và đã sửa
| Shot | Lỗi | Đã sửa |
|---|---|---|
| 05-14 | Góc từ chỗ Hưng ngồi mà đặt Ngân bên trái → lật trục 180° | Diễm bên TRÁI, Ngân (đầu bàn) bên PHẢI |
| 05-07 | Bát canh đưa về phía trái, ngược chỗ Hưng ngồi | Đưa về mép PHẢI khung |
| 14-01 | Ghế bà Lụa đặt sát tường nhưng 14-02/08 Ngân mới là người ngồi sát tường | Bà Lụa ngồi giữa phòng, Ngân ngồi ghế đẩu sát tường |
| 19-08 → 19-09 | Hai shot liền cùng góc mà bà Lụa và Ngân đổi chỗ | Giữ bà Lụa trái, Ngân phải |
| 20-09 | Diễm nói "tin nhắn dặn đóng giả" nhưng cảnh 16 Hưng dặn miệng | Đổi thành "hợp đồng anh bảo em ký, tin nhắn anh hẹn em ra công chứng" |
| 21-09 | Bà Lụa tự tuyên bố căn hộ về cháu mình (không đủ thẩm quyền) | Chị Mai tuyên bố hợp đồng vô hiệu; bà Lụa chỉ reo "Cháu tôi đấy!" |
| 21-07, 21-11, 05-14 | Nhắc @Hung/@ChiMai khi họ không gắn ảnh | Viết lại không gọi tên |
| 18-02/05/12, 24-01/03 | Công chứng viên, Tuấn xuất hiện nhiều shot mà không có ảnh → mặt đổi giữa các shot | Tạo ảnh riêng "Công chứng viên · Sơ mi cà vạt", "Tuấn · Áo hoodie xám" |
| 24-01 | Dòng cấm "phụ nữ" mâu thuẫn với bà Lụa trong khung | Đổi thành "a young woman, a baby or any child" |
| Bối cảnh | "Cửa ở bên phải căn phòng nhìn từ cửa" tự mâu thuẫn | Ghi theo khung hình: phòng thu cửa luôn bên TRÁI khung, phòng Diễm cửa luôn bên PHẢI khung |

## Rủi ro cần canh khi render (soát kỹ từng clip)
1. **Bên trái/phải của bức tường** ở tất cả shot áp tai (CAM_WALL_N/D). Sai chiều thì lật ngang khi dựng được (trong phòng không có chữ).
2. **Khẩu trang của Diễm ở 18-01 → 18-09:** không được lộ miệng mũi trước 18-10.
3. **Ba tiếng gõ** phải đúng ba tiếng (01-13, 01-14, 12-03, 12-10/11, 17-09/12, 23-01, 23-08, 25-02/06/07). Thiếu/thừa thì thay tiếng gõ khi dựng.
4. **Nhẫn và vòng** là đạo cụ nhỏ: shot đặc tả (02-02, 16-06, 19-04, 21-08, 10-04, 22-03) phải rõ; shot thường chấp nhận không thấy.
5. **Bin (8 tuổi):** ảnh tham chiếu trẻ em, giữ mặt đồng nhất qua 3 bộ đồ; không cảnh nguy hiểm.
6. **Người đông** (20-01, họp cư dân): cư dân phải mờ, không ai nhìn thẳng máy.
7. **Không cảnh giường:** 01-03/05/14, 06-09, 16-01/05 Hưng và Diễm chỉ ngồi, không hôn, không nằm.

## Ghi chú dựng (đã ghi trong từng shot)
- **Nghe qua tường:** tiếng của shot bên kia tường được lọc đục (low-pass ~800 Hz, giảm 12 dB, thêm chút vang phòng) và đặt dưới shot của người đang nghe. Các shot có ghi "(Dựng: …)".
- **09-06:** phát lại câu truyện ma của 01-02 qua loa, vang rợn.
- **14-10 / 14-11:** dựng liền nhau như hai nửa một tấm gương.
- Thẻ chữ: tên phim sau 01-01; "Ba tháng sau" trước cảnh 24.
- Nhạc: chủ đề "Bức tường" (cello) và "Ba tiếng gõ" (piano); nhiều cảnh không nhạc, đã ghi ở từng cảnh.
