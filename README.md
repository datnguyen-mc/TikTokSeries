# 🎬 TikTokSeries — Hệ Thống Tự Động Hóa Tạo Video Google Flow (FlowKit CLI)

Hướng dẫn chạy tự động tạo video liên hoàn (Text-to-Video & Seamless Image-to-Video Chaining, tự động tải video về máy, cắt frame cuối nối sang clip tiếp theo và đồng bộ Dashboard UI) cho toàn bộ **6 Series**.

---

## 📁 Cấu Trúc Các Script Chạy Tự Động (`flowkit/runners/`)

| Series | File Script | Tỉ Lệ Khung Hình | Dòng Sửa `PROJECT_ID` | Thư Mục Lưu Video Xuất Ra |
| :--- | :--- | :---: | :---: | :--- |
| **365 Ngày Việt Nam** | [`flowkit/runners/365ngayvietnam.py`](flowkit/runners/365ngayvietnam.py) | **9:16** (Dọc) | Dòng `26` | `365ngayvietnam/output_videos/` |
| **Mẹ và Bé** | [`flowkit/runners/me_va_be.py`](flowkit/runners/me_va_be.py) | **9:16** (Dọc) | Dòng `26` | `me-va-be/output_videos/` |
| **Mít và Đú 1970** | [`flowkit/runners/mit_va_du.py`](flowkit/runners/mit_va_du.py) | **9:16** (Dọc) | Dòng `26` | `mit-va-du-1970/output_videos/` |
| **365 Ngày Phèo Làm Nội Trợ** | [`flowkit/runners/pheo_va_no_meo.py`](flowkit/runners/pheo_va_no_meo.py) | **9:16** (Dọc) | Dòng `26` | `pheo-va-no-meo/output_videos/` |
| **Tây Du Ký 2026** | [`flowkit/runners/tay_du_ky.py`](flowkit/runners/tay_du_ky.py) | **9:16** (Dọc) | Dòng `26` | `tay-du-ky-2026/output_videos/` |
| **Biệt Đội Gara** | [`flowkit/runners/biet_doi_gara.py`](flowkit/runners/biet_doi_gara.py) | **16:9** (Ngang) | Dòng `22` | `biet-doi-gara/output_videos/` |

---

## 🚀 Hướng Dẫn Chạy Bằng CLI (3 Bước)

### Bước 1: Bật FlowKit Server & Kết Nối Chrome Extension
Mở **Terminal 1** và khởi động FlowKit API Server (cổng `8200`):

```bash
cd /Users/iseul-a/Documents/METACREW/TikTokSeries/flowkit
./venv/bin/python -m uvicorn agent.main:app --host 127.0.0.1 --port 8200
```

> **Lưu ý trên trình duyệt Chrome:**
> 1. Mở Chrome đã cài **FlowKit Extension** (`flowkit/extension`).
> 2. Giữ mở sẵn 1 tab dự án Google Flow: `https://flow.google.com/project/<PROJECT_ID_CỦA_BẠN>`

---

### Bước 2: Đổi `PROJECT_ID` Trong Script Muốn Chạy
Mở file script tương ứng trong `flowkit/runners/` và thay giá trị `PROJECT_ID`:

```python
PROJECT_ID = "dán-project-id-google-flow-của-bạn-vào-đây"
```

---

### Bước 3: Chạy Lệnh Tự Động Render Video (Terminal 2)
Mở **Terminal 2** tại thư mục gốc dự án:

```bash
cd /Users/iseul-a/Documents/METACREW/TikTokSeries
```

Cú pháp chung:
```bash
./flowkit/venv/bin/python flowkit/runners/<tên_script>.py [tập_bắt_đầu] [tập_kết_thúc]
```

#### 1️⃣ Chạy Series **Mít và Đú 1970** (9:16)
```bash
# Chạy mặc định từ Tập 1 đến Tập 15:
./flowkit/venv/bin/python flowkit/runners/mit_va_du.py

# Chỉ chạy riêng Tập 1:
./flowkit/venv/bin/python flowkit/runners/mit_va_du.py 1 1

# Chạy từ Tập 13 đến Tập 15:
./flowkit/venv/bin/python flowkit/runners/mit_va_du.py 13 15
```

#### 2️⃣ Chạy Series **365 Ngày Việt Nam** (9:16)
```bash
# Chạy mặc định từ Tập 1 đến Tập 5:
./flowkit/venv/bin/python flowkit/runners/365ngayvietnam.py

# Chỉ chạy riêng Tập 1 (Hà Giang):
./flowkit/venv/bin/python flowkit/runners/365ngayvietnam.py 1 1
```

#### 3️⃣ Chạy Series **Mẹ và Bé** (9:16)
```bash
# Chạy mặc định từ Tập 1 đến Tập 3:
./flowkit/venv/bin/python flowkit/runners/me_va_be.py

# Chỉ chạy riêng Tập 2:
./flowkit/venv/bin/python flowkit/runners/me_va_be.py 2 2
```

#### 4️⃣ Chạy Series **365 Ngày Phèo Làm Nội Trợ** (9:16)
```bash
# Chạy mặc định Tập 9 (10 clips):
./flowkit/venv/bin/python flowkit/runners/pheo_va_no_meo.py

# Hoặc truyền phạm vi tập:
./flowkit/venv/bin/python flowkit/runners/pheo_va_no_meo.py 9 9
```

#### 5️⃣ Chạy Series **Tây Du Ký 2026** (9:16)
```bash
# Chạy mặc định từ Tập 8 đến Tập 11:
./flowkit/venv/bin/python flowkit/runners/tay_du_ky.py

# Chỉ chạy riêng Tập 8:
./flowkit/venv/bin/python flowkit/runners/tay_du_ky.py 8 8
```

#### 6️⃣ Chạy Series **Biệt Đội Gara** (16:9)
```bash
# Chạy mặc định từ Cảnh 3 đến Cảnh 5:
./flowkit/venv/bin/python flowkit/runners/biet_doi_gara.py

# Chạy từ Cảnh 1 đến Cảnh 45:
./flowkit/venv/bin/python flowkit/runners/biet_doi_gara.py 1 45
```

---

## ⚙️ Cơ Chế Hoạt Động Tự Động
1. **Clip 1 của mỗi Tập/Cảnh**: Khởi tạo bằng `POST /api/flow/generate-video-omni-text` (10s, 720p, đúng tỉ lệ `9:16` hoặc `16:9`).
2. **Tự động tải về & đổi tên**: Ngay khi Google Flow render xong, script tự tải file `.mp4` về `<series>/output_videos/<tập>/`.
3. **Nối cảnh mượt (Seamless Chaining)**: Tự động dùng `ffmpeg` trích xuất khung hình cuối cùng (`last.jpg`) lưu vào `<series>/exported_frames/`, upload lên Google Flow và gắn vào slot **[Bắt đầu] (Start Frame)** cho Clip kế tiếp (`POST /api/flow/generate-video`).
4. **Tự động làm sạch Prompt & Retry**: Nếu gặp lỗi từ khóa nhạy cảm/bản quyền, script tự động khử từ khóa và thử lại tối đa 3 lần.
