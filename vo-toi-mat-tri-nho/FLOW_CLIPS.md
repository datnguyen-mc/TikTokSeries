# Clip đã render trên Flow

Project: https://flow.google.com/project/aa812909-361b-4c9b-b8f9-40d8d5de1c34
Tất cả ở 720p, 16:9. Mở clip: `.../project/aa812909-361b-4c9b-b8f9-40d8d5de1c34/edit/<id>`

## Phần 01 (15 shot, 57 giây, 171 tín dụng) — render 18/11/2026

| Shot | Tên trên Flow | Thời lượng | ID |
|---|---|---|---|
| 01-01 | P01-01 · Giày đỏ hành lang | 3s | 70a52dca-5ad2-4614-aa89-205d04c599e6 |
| 01-02 | P01-02 · Linh ngồi một mình | 3s | 4f21cebf-65bf-4f2d-8e92-fadec7ecff60 |
| 01-03 | P01-03 · Kẹp tóc hoa anh đào | 4s | d6cfb966-d1c6-48e0-927e-fab9185923ca |
| 01-04 | P01-04 · Tuấn mang hoa | 5s | 83a2457d-bad3-4b5e-8fda-7d39a58db71b |
| 01-05 | P01-05 · Thế cơ à | 3s | 403f3c37-534d-4a42-8528-53fdf037f09a |
| 01-06 | P01-06 · Tuấn ngơ ngác | 3s | 781abe6d-011c-49c0-a587-3f56b7d52992 |
| 01-07 | P01-07 · Mười năm ngày cưới | 5s | 03882415-eaa5-4b1e-944b-b4c45bb06bfb |
| 01-08 | P01-08 · Tuấn đếm hoa | 4s | 902320d0-39fb-4dc3-b837-f313fd9d2ce0 |
| 01-09 | P01-09 · Úp bó hoa | 3s | 03d13da7-39eb-4624-ba63-faa53932c9ce |
| 01-10 | P01-10 · Linh ra lan can | 4s | 8c375da0-25ad-4415-af7b-dede8365c7e9 |
| 01-11 | P01-11 · Cặp đôi dưới sảnh | 4s | 9676cb3d-0017-4006-9030-71f81ebdc121 |
| 01-12 | P01-12 · Linh nhìn xuống | 5s | 3dd821cc-1356-4afc-820e-03a3a075e9fa |
| 01-13 | P01-13 · Tuấn chắn tầm nhìn | 4s | e52044ac-9397-4136-b04d-8e96980680ec |
| 01-14 | P01-14 · Linh đi về thang máy | 4s | d0955daf-a982-4051-b018-6cfa718c4c97 |
| 01-15 | P01-15 · Rượu đổ khăn trắng | 3s | 443bfd77-e302-48ba-b2de-f9058db350e8 |

## Trailer 1 phút — giọng A (18/11/2026)

Prompt: `trailer/prompts/T1..T8.txt` (sinh bằng `trailer/build_trailer_prompts.py`). Dựng: `trailer/make_trailer2.py` → `trailer/Trailer_1phut_Vo_toi_mat_tri_nho.mp4` (71 giây, khung 2.39:1).

| Clip | Tên trên Flow | Thời lượng | ID |
|---|---|---|---|
| T1 | TRAILER-T1 · Cột ở sảnh | 12s | 83ab7bf1-1005-4c21-aa27-6716fa0717e8 |
| T2 | TRAILER-T2 · Anh là ai | 12s | f3318170-9659-4874-aba1-9cf788d103dc |
| T3 | TRAILER-T3 · Bác sĩ đồng phạm | 10s | bbe7955d-ec59-4afb-bded-2746cd77e428 |
| T4 | TRAILER-T4 · Phó tổng dưới mưa | 10s | e8ebeede-087a-455e-bb18-f3a673a96e5a |
| T5 | TRAILER-T5 · Chiếc váy trắng | 10s | 19f6844c-c55c-4138-b0be-0c793de1b1f6 |
| T6 | TRAILER-T6 · Đêm mưa | 10s | 5df67070-f8ad-4558-8ebd-c6ba7af455ab |
| T7 | TRAILER-T7 · Chủ tịch | 15s | 533a541a-b0cb-41bd-a985-fd6b51458dd1 |
| T8 | TRAILER-T8 · Hợp đồng làm chồng | 10s | 26f0df96-f6bd-4c69-9d43-36d68ba5d02c |
| test | TEST-A · Giọng tự nhiên (không preset) | 15s | df58436d-cc97-41aa-b0cb-ac79a3c978bb |
| test | TEST-B · Giọng preset Flow | 15s | b5a68e33-81ea-4053-8715-b5fb48c87d6c |

## Phần 02 (15 shot, 55 giây, 165 tín dụng) — render 18/11/2026

Omni 1.2 Flash, 720p, 16:9, x1. Tên trên Flow: `P02-01 · Váy trắng lướt sảnh` … `P02-15 · Đèn chùm loá trắng`. File: `clips/p02/`.

## Bản ghép 2 phút (P01 + P02)

`tap/Vo_toi_mat_tri_nho_P01-P02_2phut.mp4` (1:53, 16:9, không phụ đề). Dựng lại: `python3 tap/make_2phut.py seg && python3 tap/make_2phut.py join`.

## Bản 3 — 3 phút đầu (P1–P3), 18/11/2026

- Kịch bản: `KICH_BAN_V3_P1-3.md`; prompt: `flow_v3/` (sinh bằng `_v2/build_v3.py`).
- Ảnh nhân vật làm lại kiểu điện ảnh ngay trên nhân vật gốc (Linh · Dạ hội xanh, Linh · Áo bệnh viện, Quân · Vest navy, Mai Anh · Váy trắng, Khang · Áo blouse, Tuấn · Vest be); lịch sử ảnh cũ vẫn còn trên Flow.
- Ảnh bối cảnh trên Flow: `Bối cảnh · Sân thượng / Sảnh khách sạn / Phòng bệnh VIP / Hành lang bệnh viện / Hành lang kính` (bản lỗi có thiết bị quay đổi tên `Cũ · …`).
- Đủ 50/50 shot, tên trên Flow `V3 NN-SS`, file `clips/v3/`. Đã làm lại: 03-13 (câu thoại đổi thành "…thì quỹ mới ký" vì bản cũ bị Flow từ chối), 01-12b (thấy rõ cặp đôi dưới cổng), 02-16b (góc từ trên xuống). Bản cũ của 01-12, 02-16 để ở `clips/v3_bo/`.
- Bản ghép: `tap/Vo_toi_mat_tri_nho_V3_3phut.mp4` (3:08). Dựng lại: `python3 tap/make_v3.py seg && python3 tap/make_v3.py join`.

## Phần 04–25 — 15s/clip, giọng A (18/11/2026)

Prompt: `flow_15s/manifest.json` + `flow_15s/_compact_p04-p25.json`. Clip tải về: `clips/full_p04_p25/Pxx-Cy.mp4`.
Dựng: `tap/make_full.py` → `tap/phan/Pxx_*.mp4` (từng phần) và `tap/Vo_toi_mat_tri_nho_FULL.mp4` (23,2 phút).
Đã sửa prompt để qua bộ lọc: 05-1, 16-1, 25-5 (bỏ cảnh trẻ em trên giường/ôm sát), 06-4, 08-4. 12-2 bị chặn 6 lần → bỏ khỏi phim.

| Clip | Media ID |
|---|---|
| 04-1 | a798fee8-0897-4d1c-a46d-2fd6fc28060b |
| 04-2 | 9aa2b1f3-ac8a-4b65-8e7f-f65bada30c57 |
| 04-3 | 97818eb1-537b-4dce-b42a-427596293b50 |
| 04-4 | 89b56aa8-2a60-4ae5-b37d-3aee5a0564c6 |
| 05-1 | aa66dfa7-bbf4-4646-a162-4002959f849e |
| 05-2 | ca0fe41d-bfdc-4302-9f87-b31081ac43c1 |
| 05-3 | 73aebd0a-e9b3-4722-95d4-e5ea9be46d89 |
| 05-4 | f536ec22-dd20-4c2b-990b-097f07ad9a64 |
| 06-1 | 54f5b87f-25ea-4c34-8b10-ac62c99a8cb4 |
| 06-2 | a593aa75-8927-4ab1-a8cb-124664789d78 |
| 06-3 | edaf01da-90a1-461b-ab21-e76e0a44ec31 |
| 06-4 | 964f71f2-2177-4096-ae9e-ca0c1c4265ec |
| 07-1 | 81db761e-3729-4943-a696-e7d5e4251fd1 |
| 07-2 | a228b1dc-2117-48e9-a8f0-433fbfd60912 |
| 07-3 | e4322c3f-53fb-403d-a0f6-9dddd97d8f97 |
| 07-4 | e4dbd2af-dbbb-4388-98ed-d42a12639a95 |
| 08-1 | 5e80f36f-860c-4d84-bf37-8c1bbe965774 |
| 08-2 | f36067c5-17f4-45e3-862b-8c748d050964 |
| 08-3 | c876f546-790e-4555-b9e2-a57a03fe6da5 |
| 08-4 | 29368f4e-9d88-49c6-ac9b-302447c39a1f |
| 09-1 | cd955068-18df-4897-9be0-bd12284559c2 |
| 09-2 | d4737699-5124-412d-aff8-3bd69fe9b298 |
| 09-3 | 66ece5e2-346e-4bfb-bd2a-f69e394e066f |
| 09-4 | f1e5c423-4b77-47eb-8e20-c74a70f5ee7f |
| 10-1 | a49e4c97-2957-4352-ad56-a8cf93fbd60a |
| 10-2 | ccb3af76-9b7a-4d5b-921f-7ea43590042e |
| 10-3 | 52b2f0f5-26cd-487b-84fc-c580dd5ff8e4 |
| 10-4 | f32abaee-6704-4885-8892-d1b1926ba24a |
| 11-1 | b022a861-025c-45b6-a690-73866367c037 |
| 11-2 | 60c0e6a3-9501-4334-908e-b24b581654d0 |
| 11-3 | 7be22659-9bee-4bc7-bd5d-f249a797e750 |
| 12-1 | 06e97158-b18d-4cbe-b087-3ce07b17c862 |
| 12-3 | f645fa58-8ebd-4ec3-b4f5-1ae70ab56791 |
| 12-4 | 6d8f2c94-6890-45cd-a29e-665371f2a2da |
| 13-1 | 68abd650-a4df-4cc5-9031-19bd91a4aa46 |
| 13-2 | 2bc73b9c-dd68-4d92-8eff-c4edebfb9c3b |
| 13-3 | 3a239270-8477-455d-a794-2c8a03b53eb2 |
| 14-1 | acf4fab3-84f9-4f4c-806a-048effaea800 |
| 14-2 | f9ca1543-80f0-4d8a-9383-9957b810c621 |
| 14-3 | 49aeeac8-49f6-4abd-b123-65928d18e1e3 |
| 14-4 | f3317787-3d05-487d-839a-4ec1b7a1b1f4 |
| 15-1 | ac1daacb-55db-46ce-8032-58d96469f695 |
| 15-2 | 7cbbc07c-6612-42a7-a237-cb124aacce90 |
| 15-3 | ef98e926-0367-4cf2-8a8a-dab38f485a3d |
| 16-1 | a1c33e60-3dae-4686-a5ce-d6a9379427fc |
| 16-2 | edffb8cc-e763-41a4-8ebb-60b7f4c3bf14 |
| 16-3 | f772bb8c-022d-43bc-9807-c3e5aedcb882 |
| 17-1 | c843357a-d260-43b9-998a-fb60d5da592c |
| 17-2 | 6b2b5e91-02a7-4f20-94a4-03178bdfde83 |
| 17-3 | 1ce1979d-d7cc-418a-befc-210e98fb6553 |
| 17-4 | d0c779d3-dd95-4a5d-b1bc-8810f8371323 |
| 18-1 | 5faf780a-bc51-4647-8840-eec493bdb9e5 |
| 18-2 | bce37b4b-ffff-49f7-80c2-063ddd477adf |
| 18-3 | d45f401c-a58d-4b45-9cb5-9b22d391abeb |
| 19-1 | 85d47b0c-edd3-443d-91d9-26fc881729bc |
| 19-2 | 8e146e3a-af3e-48de-8681-e7ac9adaccad |
| 19-3 | ead0ca92-7d20-4de2-80c7-2b2b3ada1104 |
| 20-1 | 61f3bc8c-8c6a-42b1-9672-c4383cb557fc |
| 20-2 | 8c717814-8b88-4804-9991-847da5441397 |
| 20-3 | 0d7571fb-6f8f-4140-87b5-ccc5151cf70c |
| 20-4 | 4b29a78f-c8f8-4dfe-b2c9-731c07fa1bdd |
| 21-1 | faee1d5c-fcd8-42ae-a0e3-eb4ac207a785 |
| 21-2 | dbb92df9-92ca-4271-b88c-4c883fa7b6aa |
| 21-3 | 4d6be4ab-8bca-4a14-a849-e7003a2eeed4 |
| 21-4 | a6b387a2-e2b4-42b7-b2d4-4596666aa7d6 |
| 22-1 | 8eadcf04-e299-4662-ac93-2b268553e60b |
| 22-2 | a5db8a01-f888-4f2d-b4dc-583cfdf96fd0 |
| 22-3 | ac4c2a39-4b19-49e4-b9bf-ebc73179ed82 |
| 23-1 | 694b0bde-658d-49d6-b26d-a8a36a53e562 |
| 23-2 | fdc8e69a-89b3-4941-a549-107ec854a958 |
| 23-3 | df1c3569-256e-446f-92ef-bb84c42ff1a2 |
| 23-4 | 77d51d2b-d959-448e-9d42-0c15e2a62284 |
| 24-1 | e07a2d36-94a3-47e7-ac47-5e993ac37197 |
| 24-2 | 57f1c553-ab5d-43b6-a0b8-5f3c72891a7c |
| 24-3 | 6d4f226c-7ff5-427b-bd36-99525ec82da7 |
| 25-1 | 17e2a79c-fbbf-4359-92f0-7bc172cc6125 |
| 25-2 | fbbf32c0-b23e-4ff5-bc32-d1af9a6f57b1 |
| 25-3 | 65685bf3-a46e-4b90-ab48-7992bec0a5ac |
| 25-4 | 4657d9e4-29a6-4f69-889d-7aee17026f11 |
| 25-5 | 0deb1fcc-1fc9-4db8-82bf-f17694aab1b5 |
