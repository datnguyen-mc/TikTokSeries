#!/usr/bin/env python3
"""
Công cụ CLI Đồng Bộ Toàn Bộ Dữ Liệu (Database -> Cloudflare D1 SQL & Video .mp4 -> Cloudflare R2 Storage).

Cách chạy:
  ./flowkit/venv/bin/python flowkit/runners/sync_cloud.py            # Đồng bộ cả D1 SQL + R2 Storage
  ./flowkit/venv/bin/python flowkit/runners/sync_cloud.py --d1-only  # Chỉ đồng bộ Database lên D1 SQL
  ./flowkit/venv/bin/python flowkit/runners/sync_cloud.py --r2-only  # Chỉ upload Video .mp4 lên R2 Storage
  ./flowkit/venv/bin/python flowkit/runners/sync_cloud.py --channel biet-doi-gara
"""

import argparse
import asyncio
import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
FLOWKIT_DIR = os.path.dirname(THIS_DIR)
if FLOWKIT_DIR not in sys.path:
    sys.path.insert(0, FLOWKIT_DIR)
if THIS_DIR not in sys.path:
    sys.path.insert(0, THIS_DIR)

from agent.config import get_cloud_config  # noqa: E402
from agent.db.schema import init_db, get_db, close_db, SCHEMA  # noqa: E402
from agent.db.d1_client import is_d1_configured, test_d1_connection, sync_sqlite_to_d1  # noqa: E402
from agent.services.r2_storage import is_r2_configured, test_r2_connection  # noqa: E402
from agent.api.cms import _populate_all_channels_into_db, sync_videos_to_r2, SyncR2BatchRequest  # noqa: E402


async def main():
    parser = argparse.ArgumentParser(description="Đồng bộ dữ liệu FlowKit lên Cloudflare D1 SQL & R2 Storage")
    parser.add_argument("--d1-only", action="store_true", help="Chỉ đồng bộ Database lên Cloudflare D1 SQL")
    parser.add_argument("--r2-only", action="store_true", help="Chỉ upload video .mp4 lên Cloudflare R2 Storage")
    parser.add_argument("--channel", type=str, default=None, help="Chỉ đồng bộ R2 cho 1 kênh cụ thể (vd: biet-doi-gara)")
    parser.add_argument("--force", action="store_true", help="Upload lại toàn bộ video lên R2 kể cả các video đã có link")
    args = parser.parse_args()

    print("═" * 74)
    print("☁️  ĐỒNG BỘ DỮ LIỆU CLOUDFLARE D1 SQL & R2 OBJECT STORAGE — FLOWKIT STUDIO")
    print("═" * 74)

    await init_db()
    db = await get_db()
    try:
        print("📂 [1/3] Đang quét & lập chỉ mục toàn bộ 6 kênh Series, Tập, Kịch bản Prompt & Video...")
        idx_res = await _populate_all_channels_into_db(db)
        print(
            f"   ✅ Đã lập chỉ mục: {idx_res['episodes_indexed']} Tập/Cảnh & "
            f"{idx_res['clips_indexed']} Kịch bản Clip vào bảng cms_episode / cms_clip."
        )

        cfg = get_cloud_config()

        # 2. Upload videos to R2 if requested
        if not args.d1_only:
            print("\n🎬 [2/3] Kiểm tra kết nối & đồng bộ Video (.mp4) lên Cloudflare R2 Storage...")
            if not is_r2_configured(cfg):
                print("   ⚠️ Chưa cấu hình R2 trong flowkit/.env (R2_ACCESS_KEY_ID / R2_SECRET_ACCESS_KEY hoặc CF_API_TOKEN).")
            else:
                r2_check = test_r2_connection(cfg)
                if not r2_check.get("ok"):
                    print(f"   ❌ Kết nối R2 thất bại: {r2_check.get('error')}")
                else:
                    print(f"   ✅ {r2_check.get('message')}")
                    r2_res = await sync_videos_to_r2(
                        SyncR2BatchRequest(channel_slug=args.channel, force=args.force)
                    )
                    print(
                        f"   🎉 Đã upload lên R2: {r2_res['uploaded_clips_count']} video clips & "
                        f"{r2_res['uploaded_episodes_count']} tập FULL!"
                    )
                    if r2_res.get("errors"):
                        for e in r2_res["errors"][:5]:
                            print(f"      • Lỗi: {e}")

        # 3. Sync database to Cloudflare D1 SQL
        if not args.r2_only:
            print("\n🗄️  [3/3] Kiểm tra kết nối & đồng bộ toàn bộ Database sang Cloudflare D1 SQL...")
            if not is_d1_configured(cfg):
                print("   ⚠️ Chưa cấu hình D1 SQL trong flowkit/.env (CF_ACCOUNT_ID, CF_D1_DATABASE_ID, CF_API_TOKEN).")
            else:
                d1_check = await test_d1_connection(cfg)
                if not d1_check.get("ok"):
                    print(f"   ❌ Kết nối D1 SQL thất bại: {d1_check.get('error')}")
                else:
                    print(f"   ✅ {d1_check.get('message')}")
                    sync_res = await sync_sqlite_to_d1(db, SCHEMA)
                    print(f"   🎉 Đã đồng bộ tổng cộng {sync_res.get('total_rows_synced', 0)} bản ghi lên Cloudflare D1 SQL!")
                    for tbl, cnt in (sync_res.get("tables") or {}).items():
                        print(f"      • Bảng {tbl:<18}: {cnt} dòng")
    finally:
        await close_db()

    print("═" * 74)


if __name__ == "__main__":
    asyncio.run(main())

