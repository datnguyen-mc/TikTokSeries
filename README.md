# 🎬 TikTokSeries — FlowKit Studio CMS & Hệ Thống Tự Động Hóa Tạo Video Google Flow

Hệ thống quản trị **FlowKit Studio CMS** và bộ Runner CLI tự động hóa toàn diện cho **6 kênh TikTok Series**:
1. **Đăng nhập bảo mật (Authentication)**: Giao diện Login quản trị viên (`admin` / `admin123`), quản lý phiên đăng nhập và đổi mật khẩu trực tiếp trên CMS.
2. **Theo dõi & Quản lý từng kênh (Multi-Channel CMS)**: Quản lý tập trung cả 6 kênh, xem tiến độ từng tập/clip, sửa kịch bản `clip-X.md`, tạo tập mới và bấm nút **Tạo Video trực tiếp ngay trên CMS**.
3. **Khóa Nhân Vật Cố Định (Character Lock)**: Tự động khóa chính xác `media_id` gốc của từng nhân vật (`@Mit`, `@Đú`, `@Nở`, `@Vy`, `@Joi`, `@Ngọc`, `@Gạo`, `@Bông`, `@Pheo`, `@No`, `@Thay`, `@DaiCa`, `@HeoLuoi`, `@UtKho`, `@Thang`, `@Lan`...) qua endpoint `/api/flow/generate-video-omni` (Ingredients R2V) kết hợp nối mượt khung hình cuối (Seamless Chaining).
4. **Lưu Log Thực Thụ (Persistent SQLite Logs & Real-time WebSocket)**: Toàn bộ nhật ký chạy CLI, API Box, trạng thái khóa nhân vật và ghép tập đều được lưu bền vững vào bảng `cms_log` trong SQLite (`flowkit/flow_agent.db`) và phát trực tiếp lên CMS.
5. **Tự Động Ghép Các Clip Nhỏ Thành 1 Tập Hoàn Chỉnh (Auto Episode Merger)**: Ngay sau khi render xong các clip nhỏ của một tập (hoặc khi bấm nút **"🎞️ Ghép Tập Hoàn Chỉnh"** trên CMS), hệ thống tự động dùng `ffmpeg` ghép nối liền mạch tất cả clip nhỏ thành 1 file tập hoàn chỉnh (`<kênh>_tap-XX_FULL.mp4`).

---

## 🖥️ 1. Truy Cập Giao Diện Quản Trị FlowKit Studio CMS

Khi FlowKit Server đang chạy ở cổng `8200`:
- **Địa chỉ CMS trực tiếp**: `http://localhost:8200/` (hoặc `http://localhost:5173/` nếu chạy thêm Vite dev)
- **Tài khoản Admin mặc định**:
  - **Username**: `admin`
  - **Password**: `admin123`

### Các tính năng chính trong CMS (`http://localhost:8200/`):
- **Quản Lý Kênh (CMS)**:
  - Theo dõi thẻ trạng thái của cả **6 kênh TikTok Series** (tổng số tập, số clip nhỏ đã render, số tập `FULL.mp4` đã ghép, nhân vật đã khóa `media_id`, log mới nhất).
  - Chọn bất kỳ kênh nào để mở **Studio Kênh**:
    - Đổi `PROJECT_ID` Google Flow & tỉ lệ khung hình (`9:16` / `16:9`) ngay trên web.
    - Tạo tập mới (`+ Tạo Tập Mới`) tự động điền sẵn khung `[CHARACTER ANCHORS]` chuẩn của kênh đó.
    - Chỉnh sửa trực tiếp nội dung prompt của từng `clip-1.md`..`clip-N.md` và bấm **💾 Lưu Kịch Bản Clip**.
    - Bấm **▶️ Tạo Video Cả Tập (& Tự Ghép FULL)**, **▶️ Tạo Video Riêng Clip Này**, hoặc **⚡ Chạy Liên Tiếp Nhiều Tập** ngay trên giao diện web.
    - Bấm **🎞️ Ghép Các Clip Nhỏ Thành 1 Tập Hoàn Chỉnh** bất kỳ lúc nào để nối các clip lẻ thành file `FULL.mp4` và xem/tải về trực tiếp trên trình phát video của CMS.
- **Nhật Ký & Log Kênh (`/logs`)**:
  - Lọc log theo từng kênh (`mit-va-du-1970`, `365ngayvietnam`, `me-va-be`, `pheo-va-no-meo`, `tay-du-ky-2026`, `biet-doi-gara`), theo mức độ (`INFO`, `SUCCESS`, `WARN`, `ERROR`), hoặc theo danh mục (`RUNNER`, `API_BOX`, `MERGE`, `JOB`, `PROMPT`, `AUTH`).

---

## 📁 2. Danh Sách 6 Kênh & Nhân Vật Đã Khóa Cố Định (`flowkit/runners/`)

| Kênh / Series | Slug Kênh | File Runner Script | Tỉ Lệ | Nhân Vật Khóa Cố Định (`@Character`) | Thư Mục Tập Hoàn Chỉnh (`FULL.mp4`) |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **Mít Và Đú 1970** | `mit-va-du-1970` | [`flowkit/runners/mit_va_du.py`](flowkit/runners/mit_va_du.py) | **9:16** | `@Mit`, `@Đú`, `@Nở` (chó con dễ thương) | `mit-va-du-1970/output_videos/full_episodes/` |
| **365 Ngày Việt Nam** | `365ngayvietnam` | [`flowkit/runners/365ngayvietnam.py`](flowkit/runners/365ngayvietnam.py) | **9:16** | `@Vy`, `@Joi` | `365ngayvietnam/output_videos/full_episodes/` |
| **Mẹ Và Bé** | `me-va-be` | [`flowkit/runners/me_va_be.py`](flowkit/runners/me_va_be.py) | **9:16** | `@Ngọc`, `@Gạo`, `@Bông` | `me-va-be/output_videos/full_episodes/` |
| **365 Ngày Phèo Làm Nội Trợ** | `pheo-va-no-meo` | [`flowkit/runners/pheo_va_no_meo.py`](flowkit/runners/pheo_va_no_meo.py) | **9:16** | `@Pheo`, `@No`, `@My`, `@MèoTrẻ` | `pheo-va-no-meo/output_videos/full_episodes/` |
| **Tây Du Ký 2026** | `tay-du-ky-2026` | [`flowkit/runners/tay_du_ky.py`](flowkit/runners/tay_du_ky.py) | **9:16** | `@Thay`, `@DaiCa`, `@HeoLuoi`, `@UtKho` | `tay-du-ky-2026/output_videos/full_episodes/` |
| **Biệt Đội Gara** | `biet-doi-gara` | [`flowkit/runners/biet_doi_gara.py`](flowkit/runners/biet_doi_gara.py) | **16:9** | `@Thang`, `@Lan`, `@Hai`, `@Khoi`, `@Minh` | `biet-doi-gara/output_videos/full_episodes/` |

---

## 🚀 3. Hướng Dẫn Khởi Động Server & Chạy Bằng CLI

### Bước 1: Bật FlowKit CMS & API Server (Cổng `8200`)
```bash
cd /Users/iseul-a/Documents/METACREW/TikTokSeries/flowkit
GLA_RELOAD=1 ./venv/bin/python -m agent.main
```
Sau khi chạy lệnh trên:
1. Mở trình duyệt vào **`http://localhost:8200/`** và đăng nhập với `admin` / `admin123`.
2. Trên Chrome có cài **FlowKit Extension**, giữ mở 1 tab dự án Google Flow (`https://labs.google/fx/vi/tools/flow/project/<PROJECT_ID>`).

### Bước 2: Chạy Tạo Video & Tự Động Ghép Tập (Từ Web CMS hoặc Terminal)
Bạn có thể bấm nút **▶️ Tạo Video** trực tiếp trên giao diện Web CMS (`http://localhost:8200/`), hoặc chạy bằng lệnh CLI dưới đây:

```bash
cd /Users/iseul-a/Documents/METACREW/TikTokSeries

# 1. Chạy Tập 16 của Mít Và Đú 1970 (Xong 5 clips tự động ghép thành mit-va-du-1970_tap-16_FULL.mp4):
./flowkit/venv/bin/python flowkit/runners/mit_va_du.py 16 16

# 2. Chạy Tập 1 của 365 Ngày Việt Nam:
./flowkit/venv/bin/python flowkit/runners/365ngayvietnam.py 1 1

# 3. Chạy Tập 1 của Mẹ Và Bé:
./flowkit/venv/bin/python flowkit/runners/me_va_be.py 1 1

# 4. Chạy Tập 9 của 365 Ngày Phèo Làm Nội Trợ:
./flowkit/venv/bin/python flowkit/runners/pheo_va_no_meo.py 9 9

# 5. Chạy Tập 8 của Tây Du Ký 2026:
./flowkit/venv/bin/python flowkit/runners/tay_du_ky.py 8 8

# 6. Chạy Cảnh 3 đến Cảnh 5 của Biệt Đội Gara:
./flowkit/venv/bin/python flowkit/runners/biet_doi_gara.py 3 5
```
