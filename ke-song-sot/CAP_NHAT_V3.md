# Các thay đổi bản 3 — 30/10/2026

Đã viết lại toàn bộ 360 cú máy, sinh đồng bộ 60 README cảnh, 60 caption, kịch bản tổng, hồ sơ và khóa. Không tạo video hoặc thay file MP4 trong đợt này.

## Chuyển cảnh và chống lặp

- Mỗi clip có start frame, hành động mới và end frame cụ thể. 360 hành động khác nhau; không lặp nguyên câu thoại giữa các clip.
- Có bảng riêng cho đủ 359 mối ghép, gồm ranh giới 59 cảnh. 38 điểm dùng frame nối trong cùng cú máy; 321 điểm dùng cắt có ý đồ, đổi địa điểm/thời gian rõ.
- Bỏ giữ đứng hình 0,5 giây, chia ba góc theo template, slow motion ngẫu nhiên, nhạc riêng từng clip và việc lấy từ “chạy” để gán máy quay rượt đuổi.
- Một camera setup trong một clip. Với cú cắt cùng phòng, thay góc coverage rõ trong cùng nửa trục; với CONTINUE, giữ nguyên camera và tiếp hành động thay vì diễn lại.
- Đã rà riêng âm nối cuối từng cảnh sang cảnh sau, bỏ các âm/match hình dựa vào một sự kiện xảy ra từ vài clip trước.

## Kịch bản và liên tục

- Hạn bảy ngày gắn chuyến tàu chuyển Hạ; dữ liệu khóa thực sự được mở bằng token ở 25.2.
- Cao trào là trao đổi bị phản bội. Dũng dùng Tê giữ Sơn sống; phản diện nhận biết đúng chất của chúng. Không còn mẹo công khai báo 40 phút rồi đánh lừa chính người sản xuất thuốc.
- Mây xác minh trước khi hợp tác, xin hỗ trợ trước chuyến thành phố, giữ dân ngoài vùng nguy hiểm và dẫn tiếp cận hải đăng. Kiên hết đường xe nên dùng lối bộ kỹ thuật.
- Hạ chủ động để khăn, gửi dấu qua video, trì hoãn và giữ cửa cho lực lượng bằng kẹp tóc. Cô bắt đầu làm sạp hoa vì đời sống của mình.
- Một đồng hồ duy nhất: không mở trước 52.2, không có chiếc thứ hai ở kết. Ảnh để Mây nhận ra Hạ là ảnh rời.
- Khăn, sổ đen/đỏ, USB gốc/bản làm việc, token, còng và súng đều có đường đi rõ. Băng tay Sơn giữ bên trái. Hạ chỉ đổi đồ tại đồn; Sơn vest tay trần ở chuỗi cao trào.
- Thống nhất quá khứ xa cách 25 năm: Sơn 20, Bà Hai 35, giữ nguyên chín danh tính. Cảnh sau nhiều năm dùng đúng tuổi tăng thêm.
- Giảm lời dẫn và các lượt giải thích trùng; giữ giá phải trả qua lời khai và việc Sơn tự nhận còng. Không tạo thêm kết bằng một dãy vạch chờ mới.

## Nguồn và kiểm tra

`PHAN_CANH_V3.json` là nguồn duy nhất; `build_prompts_v3.py` biên dịch, lệnh cũ vẫn chạy được. `--check` kiểm tra cả dữ liệu và toàn bộ 485 file sinh ra khớp nguồn. Bộ 9 kiểm tra tự động bao gồm lỗi nối frame, đổi địa điểm trong CONTINUE, trang phục giải cứu, lần mở đồng hồ đầu, hành động lặp, tag lọt vào lời đọc chế độ tạo đúng kiểu cắt và reference chỉ cho người trong hình/ảnh được chỉ định.

`RENDER_MANIFEST_V3.json` ghi hash cho từng prompt. Trạng thái CMS/file MP4 cũ chưa được chuyển thành video bản 3. Sau khi tạo lại cần xem ghép đôi và kiểm tra toàn phim để xác nhận độ mượt hình/khẩu hình/âm thanh thực tế.

Đã chỉnh bộ chọn reference của runner để lời dẫn/đầu nối không kéo thêm nhân vật vào hình. Shot không có danh tính được chỉ định dùng text-to-video; hành vi chọn reference cũ vẫn giữ cho prompt đời trước.

Bản trước khi sửa: `revisions/before_v3_20261030_143044.zip`.
