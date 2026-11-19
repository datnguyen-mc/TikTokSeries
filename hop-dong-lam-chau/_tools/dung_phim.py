"""Kế hoạch dựng bản V3.1 (sau góp ý 18/11): phim chạy theo thời gian, có chữ dẫn truyện.
- Bỏ cảnh 00 (mở đầu kể trước, trùng gần hết cảnh 11).
- Chèn thẻ chữ thời gian/nơi chốn trước các shot mốc (CARDS), theo trục thời gian của kịch bản.
- Ghi tên nhân vật ở lần xuất hiện đầu (NAMES).
- Phóng nhẹ các shot có viền đen mỏng để mất viền (CROP)."""
CUT_SCENES = {"00"}
# Bỏ khi soát 19/11: 02-04 (ghế ông sơn thành ghế to, lệch với 02-01/02-02), 12-02 (ghế "trẻ con" lại cỡ người lớn),
# 16-01 (di ảnh đen trắng, khác hẳn di ảnh màu ở 16-02…16-07)
CUT_SHOTS = {"02-04", "12-02", "16-01", "19-06"}

TITLE = "HỢP ĐỒNG LÀM CHÁU"
CARDS = {
    "01-01": "Sáng 26 Tết · Bến xe huyện",
    "01b-01": "Cùng ngày · Xe buýt về làng",
    "02-01": "Chiều 26 Tết · Nhà ông Thịnh",
    "04-09": "Đêm 26 Tết · Gác xép",
    "05-01": "Sáng 27 Tết · Chợ hoa huyện",
    "06-01": "Chiều 27 Tết · Gói bánh chưng",
    "07-01": "Đêm 27 Tết · Canh nồi bánh",
    "08-01": "Rạng sáng 28 Tết · Bếp một nhà hàng trên thành phố",
    "09-01": "Chiều 28 Tết · Nghĩa trang làng",
    "10-01": "Chiều tối 28 Tết",
    "10-07": "Khuya hôm ấy · Đầu làng",
    "11-01": "Sáng 29 Tết",
    "13-01": "Trưa 29 Tết · Sau nhà",
    "14-01": "Chiều 29 Tết",
    "17-01": "Chiều 30 Tết · Gác xép",
    "18-01": "Hoàng hôn tất niên",
    "18b-01": "Những đêm trước đó",
    "19-01": "Tối 30 Tết · Bến xe huyện",
    "20-01": "Giao thừa",
    "20-11": "Sáng mùng 1 Tết",
}
NAMES = {
    "01-01": "Đạt, 25 tuổi · lớn lên ở mái ấm",
    "01-03": "Bà Mận · thuê Đạt về làm cháu nội 5 ngày",
    "02-01": "Ông Thịnh · chồng bà Mận",
    "03-01": "Bà Thoa · hàng xóm, mê livestream",
    "08-01": "Minh · cháu nội thật, mười năm không về",
}
# (cũ) danh sách phóng 8% — nay ghep_tung_phan.py tự đo viền đen từng clip và cắt vừa đủ
CROP = {"01-11", "02-06", "02-07", "02-09", "04-09", "07-07", "07-08", "07-09", "08-06", "08-07", "10-01", "11-04", "11-05", "11-06", "11-08", "12-01", "12-03", "12-09", "12-11", "13-02", "14-04", "15-02", "16-07", "17-01", "17-08", "17-09", "18-07", "20-03"}

# phóng tay cho clip có khung viền kiểu cuộn phim (máy không đo được): tỉ lệ giữ lại
MANUAL_CROP = {"20-06": 0.88}

# độ dài riêng (giây) cho shot mà câu thoại dài hơn bảng shot
DUR = {"14-07": 8}
