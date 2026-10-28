# 🎬 FlowKit — Hướng Dẫn Chạy CLI Tự Động Cho Các Series

Toàn bộ các script chạy tự động cho từng series được đặt trong thư mục [`runners/`](runners/).

---

## 📋 Danh Sách Script Theo Series (`flowkit/runners/`)

| Series | File Script | Tỉ Lệ | Dòng Sửa `PROJECT_ID` |
| :--- | :--- | :---: | :---: |
| **365 Ngày Việt Nam** | [`runners/365ngayvietnam.py`](runners/365ngayvietnam.py) | `9:16` (Portrait) | Dòng `26` |
| **Mẹ và Bé** | [`runners/me_va_be.py`](runners/me_va_be.py) | `9:16` (Portrait) | Dòng `26` |
| **Mít và Đú 1970** | [`runners/mit_va_du.py`](runners/mit_va_du.py) | `9:16` (Portrait) | Dòng `26` |
| **365 Ngày Phèo Làm Nội Trợ** | [`runners/pheo_va_no_meo.py`](runners/pheo_va_no_meo.py) | `9:16` (Portrait) | Dòng `26` |
| **Tây Du Ký 2026** | [`runners/tay_du_ky.py`](runners/tay_du_ky.py) | `9:16` (Portrait) | Dòng `26` |
| **Biệt Đội Gara** | [`runners/biet_doi_gara.py`](runners/biet_doi_gara.py) | `16:9` (Landscape) | Dòng `22` |

---

## 🚀 Cách Chạy Nhanh

### 1. Khởi động FlowKit Server (Terminal 1)
```bash
cd /Users/iseul-a/Documents/METACREW/TikTokSeries/flowkit
./venv/bin/python -m uvicorn agent.main:app --host 127.0.0.1 --port 8200
```
*(Mở Chrome có cài FlowKit Extension và giữ mở tab `https://flow.google.com/project/<PROJECT_ID>`).*

### 2. Chạy Script Series (Terminal 2)
Đứng tại thư mục gốc `/Users/iseul-a/Documents/METACREW/TikTokSeries`:

```bash
# 1. Mít và Đú 1970 (9:16) — Tập 1 đến 15 (hoặc truyền tập bắt đầu / kết thúc)
./flowkit/venv/bin/python flowkit/runners/mit_va_du.py 1 15

# 2. 365 Ngày Việt Nam (9:16) — Tập 1 đến 5
./flowkit/venv/bin/python flowkit/runners/365ngayvietnam.py 1 5

# 3. Mẹ và Bé (9:16) — Tập 1 đến 3
./flowkit/venv/bin/python flowkit/runners/me_va_be.py 1 3

# 4. 365 Ngày Phèo Làm Nội Trợ (9:16) — Tập 9
./flowkit/venv/bin/python flowkit/runners/pheo_va_no_meo.py 9 9

# 5. Tây Du Ký 2026 (9:16) — Tập 8 đến 11
./flowkit/venv/bin/python flowkit/runners/tay_du_ky.py 8 11

# 6. Biệt Đội Gara (16:9) — Cảnh 3 đến 5
./flowkit/venv/bin/python flowkit/runners/biet_doi_gara.py 3 5
```
