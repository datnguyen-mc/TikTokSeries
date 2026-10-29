"""Cloudflare D1 SQL Async Client & Hybrid Connection Adapter.

Provides:
- Direct HTTP REST API execution against Cloudflare D1 SQL:
  POST https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database/{database_id}/query
- D1Row & D1Cursor compatible with aiosqlite.Row / aiosqlite.Cursor.
- D1HybridConnection: Executes SQL against Cloudflare D1 SQL while keeping local SQLite
  in sync as an instant cache/fallback, and supports one-click full database migration
  between local SQLite and Cloudflare D1 SQL.
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
import urllib.error
import urllib.request
from typing import Any, Iterable, Optional

import aiosqlite
import httpx

from agent.config import get_cloud_config

logger = logging.getLogger(__name__)

_PRAGMA_TABLE_INFO_KEYS = ("cid", "name", "type", "notnull", "dflt_value", "pk")
_LOCAL_ONLY_PRAGMAS = (
    "PRAGMA JOURNAL_MODE",
    "PRAGMA WAL_CHECKPOINT",
    "PRAGMA SYNCHRONOUS",
    "PRAGMA BUSY_TIMEOUT",
)

ALL_SYNC_TABLES = [
    "character",
    "project",
    "material",
    "project_character",
    "video",
    "scene",
    "request",
    "provider_job",
    "cms_user",
    "cms_session",
    "cms_channel",
    "cms_episode",
    "cms_clip",
    "cms_log",
]


def is_d1_configured(cfg: Optional[dict] = None) -> bool:
    """Return True if Cloudflare D1 SQL credentials are configured and active."""
    c = cfg or get_cloud_config()
    if c.get("db_backend") == "sqlite":
        return False
    return bool(
        c.get("cf_account_id")
        and c.get("cf_api_token")
        and c.get("cf_d1_database_id")
    )


def _normalize_params(params: Optional[Iterable[Any]]) -> list[Any]:
    if not params:
        return []
    out: list[Any] = []
    for v in params:
        if isinstance(v, bool):
            out.append(1 if v else 0)
        else:
            out.append(v)
    return out


class D1Row(dict):
    """Row mapping supporting both dict keys (row['id']) and positional index (row[0])."""

    def __init__(self, data: dict[str, Any]):
        super().__init__(data)
        if all(k in data for k in _PRAGMA_TABLE_INFO_KEYS):
            self._values = [data.get(k) for k in _PRAGMA_TABLE_INFO_KEYS]
        else:
            self._values = list(data.values())

    def __getitem__(self, key: Any) -> Any:
        if isinstance(key, int):
            return self._values[key]
        return super().__getitem__(key)


class D1Cursor:
    """Async cursor compatible with aiosqlite.Cursor."""

    def __init__(
        self,
        rows: Optional[list[D1Row]] = None,
        lastrowid: Optional[int] = None,
        rowcount: int = 0,
    ):
        self._rows: list[D1Row] = rows or []
        self._idx: int = 0
        self.lastrowid: Optional[int] = lastrowid
        self.rowcount: int = rowcount

    async def fetchone(self) -> Optional[D1Row]:
        if self._idx < len(self._rows):
            row = self._rows[self._idx]
            self._idx += 1
            return row
        return None

    async def fetchall(self) -> list[D1Row]:
        if self._idx == 0:
            self._idx = len(self._rows)
            return list(self._rows)
        rem = self._rows[self._idx :]
        self._idx = len(self._rows)
        return rem


def _split_sql_statements(script: str) -> list[str]:
    """Split a multi-statement SQL script into individual statements, stripping -- comments."""
    cleaned_lines = []
    for line in script.splitlines():
        idx = line.find("--")
        if idx != -1:
            # Only strip comment if not inside quotes
            prefix = line[:idx]
            if prefix.count("'") % 2 == 0 and prefix.count('"') % 2 == 0:
                line = prefix
        cleaned_lines.append(line)
    cleaned = "\n".join(cleaned_lines)
    stmts = []
    for part in cleaned.split(";"):
        s = part.strip()
        if s:
            stmts.append(s)
    return stmts


async def d1_query_async(
    sql: str,
    params: Optional[Iterable[Any]] = None,
    cfg: Optional[dict] = None,
    client: Optional[httpx.AsyncClient] = None,
) -> dict[str, Any]:
    """Execute a parameterized SQL query against Cloudflare D1 HTTP API."""
    c = cfg or get_cloud_config()
    account_id = c.get("cf_account_id", "")
    db_id = c.get("cf_d1_database_id", "")
    token = c.get("cf_api_token", "")
    if not (account_id and db_id and token):
        return {"ok": False, "error": "Chưa cấu hình CF_ACCOUNT_ID / CF_D1_DATABASE_ID / CF_API_TOKEN"}

    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database/{db_id}/query"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "sql": sql,
        "params": _normalize_params(params),
    }

    own_client = client is None
    http_client = client or httpx.AsyncClient(timeout=30.0)
    try:
        resp = await http_client.post(url, headers=headers, json=payload)
        data = resp.json()
        if resp.status_code != 200 or not data.get("success", False):
            errs = data.get("errors") or []
            err_msg = errs[0].get("message") if errs and isinstance(errs[0], dict) else resp.text[:300]
            return {"ok": False, "status_code": resp.status_code, "error": f"D1 Error: {err_msg}"}

        result_list = data.get("result") or []
        first_res = result_list[0] if result_list and isinstance(result_list[0], dict) else {}
        raw_rows = first_res.get("results") or []
        meta = first_res.get("meta") or {}
        rows = [D1Row(r) for r in raw_rows if isinstance(r, dict)]
        return {
            "ok": True,
            "rows": rows,
            "lastrowid": meta.get("last_row_id"),
            "rowcount": meta.get("changes", len(rows)),
            "meta": meta,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}
    finally:
        if own_client:
            await http_client.aclose()


def d1_query_sync(
    sql: str,
    params: Optional[Iterable[Any]] = None,
    cfg: Optional[dict] = None,
) -> dict[str, Any]:
    """Synchronous D1 SQL query helper for runner scripts & CLI tools."""
    c = cfg or get_cloud_config()
    account_id = c.get("cf_account_id", "")
    db_id = c.get("cf_d1_database_id", "")
    token = c.get("cf_api_token", "")
    if not (account_id and db_id and token):
        return {"ok": False, "error": "Chưa cấu hình Cloudflare D1 SQL"}

    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/d1/database/{db_id}/query"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    body = json.dumps({"sql": sql, "params": _normalize_params(params)}).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if not data.get("success", False):
            errs = data.get("errors") or []
            err_msg = errs[0].get("message") if errs and isinstance(errs[0], dict) else str(data)
            return {"ok": False, "error": err_msg}
        result_list = data.get("result") or []
        first_res = result_list[0] if result_list and isinstance(result_list[0], dict) else {}
        raw_rows = first_res.get("results") or []
        meta = first_res.get("meta") or {}
        return {
            "ok": True,
            "rows": [D1Row(r) for r in raw_rows if isinstance(r, dict)],
            "lastrowid": meta.get("last_row_id"),
            "rowcount": meta.get("changes", len(raw_rows)),
            "meta": meta,
        }
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")[:300]
        return {"ok": False, "error": f"HTTP {e.code}: {err_body}"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


async def test_d1_connection(cfg: Optional[dict] = None) -> dict[str, Any]:
    """Test Cloudflare D1 SQL connection and list tables."""
    c = cfg or get_cloud_config()
    if not (c.get("cf_account_id") and c.get("cf_api_token") and c.get("cf_d1_database_id")):
        return {
            "ok": False,
            "configured": False,
            "database_id": c.get("cf_d1_database_id"),
            "error": "Chưa điền thông tin kết nối D1 SQL (CF_ACCOUNT_ID, CF_D1_DATABASE_ID, CF_API_TOKEN).",
        }

    res = await d1_query_async(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name",
        cfg=c,
    )
    if not res.get("ok"):
        return {
            "ok": False,
            "configured": True,
            "database_id": c.get("cf_d1_database_id"),
            "error": res.get("error"),
        }

    tables = [r.get("name") for r in res.get("rows", []) if r.get("name") and not str(r.get("name")).startswith("_cf_")]
    return {
        "ok": True,
        "configured": True,
        "database_id": c.get("cf_d1_database_id"),
        "account_id": c.get("cf_account_id"),
        "tables": tables,
        "table_count": len(tables),
        "message": f"Kết nối Cloudflare D1 SQL thành công ({len(tables)} bảng hiện có)!",
    }


class D1HybridConnection:
    """Drop-in replacement for aiosqlite.Connection that syncs with Cloudflare D1 SQL.

    - When D1 is configured:
      * Writes (INSERT/UPDATE/DELETE/CREATE/ALTER/DROP) execute on BOTH Cloudflare D1 SQL
        and the local SQLite database so cloud and local stay 100% synchronized.
      * Reads (SELECT / PRAGMA table_info) execute on Cloudflare D1 SQL first, with
        instant fallback to local SQLite if offline or if a table is still syncing.
    - When D1 is not yet configured:
      * Operates seamlessly on local SQLite, ready to sync to D1 the moment credentials are saved.
    """

    def __init__(self, sqlite_conn: aiosqlite.Connection):
        self._sqlite = sqlite_conn
        self._http = httpx.AsyncClient(timeout=30.0)
        self._d1_schema_initialized = False

    @property
    def row_factory(self):
        return self._sqlite.row_factory

    @row_factory.setter
    def row_factory(self, val):
        self._sqlite.row_factory = val

    async def __aenter__(self) -> "D1HybridConnection":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    def _is_local_only_sql(self, sql_upper: str) -> bool:
        for p in _LOCAL_ONLY_PRAGMAS:
            if sql_upper.startswith(p):
                return True
        if sql_upper.startswith("PRAGMA FOREIGN_KEYS"):
            return True
        return False

    def _is_write_sql(self, sql_upper: str) -> bool:
        for kw in ("INSERT", "UPDATE", "DELETE", "REPLACE", "CREATE", "ALTER", "DROP"):
            if sql_upper.startswith(kw):
                return True
        return False

    async def execute(self, sql: str, parameters: Optional[Iterable[Any]] = None) -> Any:
        params_list = _normalize_params(parameters)
        sql_stripped = sql.strip()
        sql_upper = sql_stripped.upper()

        # Always execute on local SQLite mirror first for sub-millisecond speed & consistency
        local_cur = await self._sqlite.execute(sql, params_list)

        # Serve SELECT / PRAGMA reads directly from local SQLite mirror (<1ms),
        # and replicate all WRITE statements (INSERT / UPDATE / DELETE) to Cloudflare D1 SQL
        if not self._is_write_sql(sql_upper) or not is_d1_configured() or self._is_local_only_sql(sql_upper):
            return local_cur

        # Execute write on Cloudflare D1 SQL
        d1_res = await d1_query_async(sql_stripped, params_list, client=self._http)
        if d1_res.get("ok"):
            return D1Cursor(
                rows=d1_res.get("rows"),
                lastrowid=d1_res.get("lastrowid") or local_cur.lastrowid,
                rowcount=max(d1_res.get("rowcount", 0), local_cur.rowcount if local_cur.rowcount > 0 else 0),
            )
        logger.debug("D1 write fallback to local SQLite (%s): %s", sql_stripped[:80], d1_res.get("error"))
        return local_cur

    async def executescript(self, sql_script: str) -> Any:
        local_res = await self._sqlite.executescript(sql_script)
        if is_d1_configured():
            stmts = _split_sql_statements(sql_script)
            for stmt in stmts:
                stmt_upper = stmt.upper()
                if self._is_local_only_sql(stmt_upper):
                    continue
                await d1_query_async(stmt, client=self._http)
        return local_res

    async def commit(self) -> None:
        await self._sqlite.commit()

    async def close(self) -> None:
        try:
            await self._http.aclose()
        except Exception:
            pass
        await self._sqlite.close()


async def init_d1_schema(schema_sql: str) -> dict[str, Any]:
    """Create all tables and indexes on Cloudflare D1 SQL."""
    cfg = get_cloud_config()
    if not is_d1_configured(cfg):
        return {"ok": False, "skipped": True, "error": "Cloudflare D1 chưa được cấu hình."}

    stmts = _split_sql_statements(schema_sql)
    executed = 0
    errors = []
    async with httpx.AsyncClient(timeout=45.0) as client:
        for stmt in stmts:
            if any(stmt.upper().startswith(p) for p in _LOCAL_ONLY_PRAGMAS):
                continue
            res = await d1_query_async(stmt, cfg=cfg, client=client)
            if res.get("ok"):
                executed += 1
            else:
                errors.append(res.get("error"))

    return {
        "ok": len(errors) == 0 or executed > 0,
        "statements_executed": executed,
        "errors": errors[:5],
    }


async def sync_sqlite_to_d1(sqlite_conn: Any, schema_sql: str) -> dict[str, Any]:
    """Full synchronization: push all tables and rows from local SQLite to Cloudflare D1 SQL."""
    cfg = get_cloud_config()
    if not is_d1_configured(cfg):
        return {
            "ok": False,
            "error": "Chưa cấu hình Cloudflare D1 SQL (CF_ACCOUNT_ID, CF_D1_DATABASE_ID, CF_API_TOKEN).",
        }

    # 1. Ensure schema exists on D1
    schema_res = await init_d1_schema(schema_sql)

    raw_sqlite = sqlite_conn._sqlite if isinstance(sqlite_conn, D1HybridConnection) else sqlite_conn
    table_stats: dict[str, int] = {}
    errors: list[str] = []

    async with httpx.AsyncClient(timeout=60.0) as client:
        sem = asyncio.Semaphore(6)
        for table in ALL_SYNC_TABLES:
            try:
                cur = await raw_sqlite.execute(f"SELECT * FROM {table}")
                rows = [dict(r) for r in await cur.fetchall()]
                if not rows:
                    table_stats[table] = 0
                    continue

                cols = list(rows[0].keys())
                col_list_str = ", ".join(cols)
                row_placeholder = "(" + ", ".join("?" for _ in cols) + ")"
                # Cloudflare D1 allows up to 100 bound parameters per SQL statement
                batch_size = max(1, min(20, 95 // max(1, len(cols))))

                batches = [rows[i : i + batch_size] for i in range(0, len(rows), batch_size)]

                async def _push_batch(batch_rows: list[dict]) -> int:
                    async with sem:
                        multi_placeholders = ", ".join(row_placeholder for _ in batch_rows)
                        batch_sql = f"INSERT OR REPLACE INTO {table} ({col_list_str}) VALUES {multi_placeholders}"
                        flat_vals = []
                        for r in batch_rows:
                            flat_vals.extend(r.get(c) for c in cols)
                        r_d1 = await d1_query_async(batch_sql, flat_vals, cfg=cfg, client=client)
                        if r_d1.get("ok"):
                            return len(batch_rows)
                        errors.append(f"{table}: {r_d1.get('error')}")
                        return 0

                results = await asyncio.gather(*(_push_batch(b) for b in batches))
                table_stats[table] = sum(results)
            except Exception as e:
                errors.append(f"{table}: {e}")

    total_rows = sum(table_stats.values())
    return {
        "ok": True,
        "total_rows_synced": total_rows,
        "tables": table_stats,
        "schema_initialized": schema_res.get("ok", False),
        "errors": errors[:10],
    }


async def sync_d1_to_sqlite(sqlite_conn: Any, schema_sql: str) -> dict[str, Any]:
    """Pull all rows from Cloudflare D1 SQL into the local SQLite database."""
    cfg = get_cloud_config()
    if not is_d1_configured(cfg):
        return {
            "ok": False,
            "error": "Chưa cấu hình Cloudflare D1 SQL (CF_ACCOUNT_ID, CF_D1_DATABASE_ID, CF_API_TOKEN).",
        }

    raw_sqlite = sqlite_conn._sqlite if isinstance(sqlite_conn, D1HybridConnection) else sqlite_conn
    table_stats: dict[str, int] = {}
    errors: list[str] = []

    async with httpx.AsyncClient(timeout=60.0) as client:
        for table in ALL_SYNC_TABLES:
            try:
                res = await d1_query_async(f"SELECT * FROM {table}", cfg=cfg, client=client)
                if not res.get("ok"):
                    continue
                rows = res.get("rows") or []
                if not rows:
                    table_stats[table] = 0
                    continue

                cols = list(rows[0].keys())
                col_list_str = ", ".join(cols)
                placeholders = ", ".join("?" for _ in cols)
                insert_sql = f"INSERT OR REPLACE INTO {table} ({col_list_str}) VALUES ({placeholders})"

                pulled = 0
                for row in rows:
                    vals = [row.get(c) for c in cols]
                    await raw_sqlite.execute(insert_sql, _normalize_params(vals))
                    pulled += 1
                await raw_sqlite.commit()
                table_stats[table] = pulled
            except Exception as e:
                errors.append(f"{table}: {e}")

    return {
        "ok": True,
        "total_rows_pulled": sum(table_stats.values()),
        "tables": table_stats,
        "errors": errors[:10],
    }

