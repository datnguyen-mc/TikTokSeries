# Ngã Rẽ — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Phim 25 phút cắt thành 12 phần dọc 9:16, mỗi phần gần trọn một cảnh (47–62 giây), đăng nối tiếp như một series.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên ở giữa, nền là chính cảnh đó làm mờ.
- **Chữ trên video:** nhãn vàng “NGÃ RẼ • PHẦN N/12” và câu hook ở trên khung phim; 2,5 giây cuối đổi thành “CÒN TIẾP » PHẦN N+1”.
- **Phụ đề:** chưa có phụ đề thoại (máy dựng không có Whisper). Các dòng tin nhắn/chữ đã in sẵn trong phim vẫn giữ.
- **Âm thanh:** chuẩn hoá −14 LUFS.
- **Nguồn:** các clip đã xử lý trong `build/full/` của bản phim v9.
- **Mỗi thư mục phần:** video `.mp4`, ảnh bìa `cover.jpg`, `caption.md` (caption TikTok, tiêu đề + mô tả YouTube, caption Facebook).

Dựng lại: `python3 make_shorts.py` (tất cả phần còn thiếu) hoặc `python3 make_shorts.py 3 7` (dựng lại vài phần). Nội dung từng phần nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Nội dung | Clip | Thời lượng | Đăng lúc (gợi ý) | Ưu tiên |
|---|---|---|---|---|---|
| 1 | [Con gái khoe tranh vẽ gia đình, mẹ không ngẩng lên](phan-01-me-oi-nhin-tranh-con-ve/caption.md) | 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.11 | 47s | Thứ Năm 26/11 – 09:00 | ⭐ |
| 2 | [Cô nhân viên trẻ mang cà phê cho sếp đang kiệt sức](phan-02-ly-ca-phe-co-len-sep/caption.md) | 4.2, 4.3, 4.4, 4.5, 4.6, 4.9, 4.11 | 55s | Thứ Năm 26/11 – 17:00 |  |
| 3 | [10 năm ngày cưới, chiếc bánh nằm trong tủ lạnh](phan-03-muoi-nam-ngay-cuoi/caption.md) | 5.1, 5.2, 5.3, 5.5, 5.7, 5.9, 5.12 | 60s | Thứ Sáu 27/11 – 09:00 | ⭐ |
| 4 | [Bố mẹ đùn nhau đón con, bé đứng chờ dưới mưa](phan-04-con-mua-truoc-cong-truong/caption.md) | 6.4, 6.5, 6.6, 6.7, 6.9, 6.10, 6.11 | 53s | Thứ Sáu 27/11 – 17:00 |  |
| 5 | [Người thứ ba ngồi một mình trong phòng trọ](phan-05-anh-khong-qua-duoc/caption.md) | 8.1, 8.2, 8.3, 8.7, 8.8, 8.9 | 50s | Thứ Bảy 28/11 – 09:00 | ⭐ |
| 6 | [Bé gái vô tình đọc tin nhắn “Em nhớ anh” trong máy bố](phan-06-con-gai-doc-duoc-tin-nhan/caption.md) | 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 9.10, 9.11 | 57s | Thứ Bảy 28/11 – 17:00 | ⭐ |
| 7 | [Vợ hỏi thẳng chồng về tin nhắn lạ](phan-07-vo-hoi-thang/caption.md) | 10.2, 10.3, 10.5, 10.7, 10.8, 10.9, 10.10 | 57s | Chủ Nhật 29/11 – 09:00 | ⭐ |
| 8 | [Người vợ tìm ra danh tính người thứ ba ở tiệm tóc](phan-08-o-tiem-toc/caption.md) | 12.1, 12.2, 12.4, 12.5, 12.6, 12.7, 12.8 | 55s | Chủ Nhật 29/11 – 17:00 |  |
| 9 | [Vợ tìm đến tận phòng trọ gặp người thứ ba](phan-09-go-cua-phong-tro/caption.md) | 13.4, 13.5, 13.6, 13.8, 14.3, 14.5, 14.6 | 62s | Thứ Hai 30/11 – 09:00 | ⭐ |
| 10 | [Trên sân thượng, người thứ ba nói lời dừng lại](phan-10-chiec-nhan-tren-san-thuong/caption.md) | 15.2, 15.3, 15.4, 15.6, 15.9, 15.11 | 51s | Thứ Hai 30/11 – 17:00 | ⭐ |
| 11 | [Bố đến đón, con gái hỏi một câu khiến anh nghẹn lời](phan-11-bo-don-con-o-cong-truong/caption.md) | 17.3, 17.4, 17.5, 17.6, 17.7, 17.8 | 49s | Thứ Ba 01/12 – 09:00 |  |
| 12 | [Bữa cơm đầu tiên sau biến cố: gia đình ngồi lại với nhau](phan-12-bua-com-ba-nguoi/caption.md) | 18.1, 18.3, 18.7, 18.10, 18.11, 18.13 | 51s | Thứ Ba 01/12 – 17:00 |  |

⭐ = phần có hook mạnh nhất, nên ghim hoặc dồn tương tác trước.
