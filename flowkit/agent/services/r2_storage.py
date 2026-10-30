"""Cloudflare R2 Object Storage Client (S3 AWS Signature V4 + Cloudflare API v4 fallback).

Zero external dependencies: works in both flowkit/venv and system Python.
Streams large video files (.mp4) directly from disk without loading full files into RAM.
"""

from __future__ import annotations

import datetime
import hashlib
import hmac
import json
import logging
import mimetypes
import os
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

try:
    import requests
except ImportError:
    requests = None

logger = logging.getLogger(__name__)

_FLOWKIT_DIR = Path(__file__).resolve().parent.parent.parent
_ENV_PATH = _FLOWKIT_DIR / ".env"


def load_r2_config() -> dict:
    """Load R2 & Cloudflare credentials dynamically from flowkit/.env and os.environ."""
    env_map: dict[str, str] = {}
    if _ENV_PATH.is_file():
        try:
            for line in _ENV_PATH.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env_map[k.strip()] = v.strip().strip('"').strip("'")
        except Exception:
            pass

    def _get(key: str, default: str = "") -> str:
        val = env_map.get(key)
        if val is not None and val != "":
            return val
        return os.environ.get(key, default).strip()

    cf_account_id = _get("CF_ACCOUNT_ID")
    r2_account_id = _get("R2_ACCOUNT_ID") or cf_account_id
    r2_endpoint = _get("R2_ENDPOINT_URL").rstrip("/")
    if not r2_endpoint and r2_account_id:
        r2_endpoint = f"https://{r2_account_id}.r2.cloudflarestorage.com"

    return {
        "cf_account_id": cf_account_id,
        "cf_api_token": _get("CF_API_TOKEN"),
        "r2_auto_upload": _get("R2_AUTO_UPLOAD", "1").lower() not in ("0", "false", "no"),
        "r2_account_id": r2_account_id,
        "r2_access_key_id": _get("R2_ACCESS_KEY_ID"),
        "r2_secret_access_key": _get("R2_SECRET_ACCESS_KEY"),
        "r2_bucket_name": _get("R2_BUCKET_NAME", "tiktok-series") or "tiktok-series",
        "r2_public_url": _get("R2_PUBLIC_URL").rstrip("/"),
        "r2_endpoint_url": r2_endpoint,
        "r2_key_prefix": _get("R2_KEY_PREFIX", "series").strip("/"),
    }


def is_r2_configured(cfg: Optional[dict] = None) -> bool:
    """Return True if R2 credentials (either S3 keys or CF API token) are configured."""
    c = cfg or load_r2_config()
    bucket = c.get("r2_bucket_name", "").strip()
    if not bucket:
        return False
    has_s3 = bool(
        c.get("r2_access_key_id")
        and c.get("r2_secret_access_key")
        and (c.get("r2_endpoint_url") or c.get("r2_account_id"))
    )
    has_cf_api = bool(c.get("cf_account_id") and c.get("cf_api_token"))
    return has_s3 or has_cf_api


def detect_media_info(path_or_url: str, default_category: str = "") -> dict:
    """Detect media kind ('video' | 'image' | 'audio'), MIME type, and normalized extension."""
    raw = (path_or_url or "").split("?")[0].split("#")[0].strip()
    ext = os.path.splitext(raw)[1].lower()
    cat = (default_category or "").lower()

    if not ext:
        if cat in ("frames", "images", "character_refs", "thumbnails"):
            ext = ".jpg"
        elif cat in ("audio", "tts", "music"):
            ext = ".mp3"
        else:
            ext = ".mp4"

    if ext in (".mp4", ".m4v"):
        return {"media_kind": "video", "mime_type": "video/mp4", "ext": ".mp4"}
    if ext == ".webm":
        return {"media_kind": "video", "mime_type": "video/webm", "ext": ".webm"}
    if ext == ".mov":
        return {"media_kind": "video", "mime_type": "video/quicktime", "ext": ".mov"}
    if ext in (".jpg", ".jpeg"):
        return {"media_kind": "image", "mime_type": "image/jpeg", "ext": ".jpg"}
    if ext == ".png":
        return {"media_kind": "image", "mime_type": "image/png", "ext": ".png"}
    if ext == ".webp":
        return {"media_kind": "image", "mime_type": "image/webp", "ext": ".webp"}
    if ext == ".gif":
        return {"media_kind": "image", "mime_type": "image/gif", "ext": ".gif"}
    if ext == ".mp3":
        return {"media_kind": "audio", "mime_type": "audio/mpeg", "ext": ".mp3"}
    if ext == ".wav":
        return {"media_kind": "audio", "mime_type": "audio/wav", "ext": ".wav"}
    if ext in (".m4a", ".aac"):
        return {"media_kind": "audio", "mime_type": "audio/mp4", "ext": ext}

    guessed, _ = mimetypes.guess_type(raw)
    if guessed:
        kind = guessed.split("/")[0] if "/" in guessed else "video"
        return {"media_kind": kind if kind in ("video", "image", "audio") else "video", "mime_type": guessed, "ext": ext}
    return {"media_kind": "video", "mime_type": "video/mp4", "ext": ".mp4"}


def build_r2_key(
    channel_slug: str,
    category: str,
    filename: str,
    subfolder: str = "",
    cfg: Optional[dict] = None,
) -> str:
    """Build normalized R2 object key: e.g. series/biet-doi-gara/episodes/canh-01/canh-01_clip-01.mp4."""
    c = cfg or load_r2_config()
    parts = []
    prefix = c.get("r2_key_prefix", "series").strip("/")
    if prefix:
        parts.append(prefix)
    if channel_slug:
        parts.append(channel_slug.strip("/"))
    if category:
        parts.append(category.strip("/"))
    if subfolder:
        parts.append(subfolder.strip("/"))

    base_name = os.path.basename(filename)
    _, ext = os.path.splitext(base_name)
    if not ext:
        info = detect_media_info(base_name, default_category=category)
        base_name = f"{base_name}{info['ext']}"
    parts.append(base_name)
    return "/".join(parts)


def build_r2_public_url(object_key: str, cfg: Optional[dict] = None) -> str:
    """Return public URL for an R2 object key, ensuring proper bucket domain and extension."""
    c = cfg or load_r2_config()
    bucket = c.get("r2_bucket_name", "flowkit").strip("/")
    clean_key = object_key.lstrip("/")
    if clean_key.startswith(f"{bucket}/series/"):
        clean_key = clean_key[len(bucket) + 1 :]
    pub = c.get("r2_public_url", "").rstrip("/")
    if pub:
        # Strip accidental /<bucket> suffix on r2.dev public domain
        if ".r2.dev/" in f"{pub}/" and pub.endswith(f"/{bucket}"):
            pub = pub[: -(len(bucket) + 1)]
        # Auto-correct if pub is still set to the 'tiktok' bucket domain while bucket is 'flowkit'
        if bucket == "flowkit" and "pub-31538b394ab64f96ba3dff5f02ecab44.r2.dev" in pub:
            pub = "https://pub-53dae622644845c09c48558d8a42fe29.r2.dev"
        return f"{pub}/{clean_key}"
    endpoint = c.get("r2_endpoint_url", "").rstrip("/")
    if endpoint:
        return f"{endpoint}/{bucket}/{clean_key}"
    return f"r2://{bucket}/{clean_key}"


def normalize_r2_media_url(
    url: Optional[str],
    r2_key: Optional[str] = None,
    default_category: str = "episodes",
    cfg: Optional[dict] = None,
) -> Optional[str]:
    """Normalize any stored R2 URL or key into a direct playable .mp4 / .jpg public R2 URL."""
    c = cfg or load_r2_config()
    bucket = c.get("r2_bucket_name", "flowkit").strip("/")

    key_cand = (r2_key or "").strip().lstrip("/")
    if not key_cand and url:
        u_clean = url.strip()
        if "://" in u_clean:
            parsed = urllib.parse.urlparse(u_clean)
            key_cand = parsed.path.lstrip("/")
        else:
            key_cand = u_clean.lstrip("/")

    if not key_cand:
        return url

    if key_cand.startswith(f"{bucket}/"):
        key_cand = key_cand[len(bucket) + 1 :]

    _, ext = os.path.splitext(key_cand)
    if not ext:
        info = detect_media_info(key_cand, default_category=default_category)
        key_cand = f"{key_cand}{info['ext']}"

    return build_r2_public_url(key_cand, c)


def _sha256_file_hex(file_path: str) -> str:
    """Compute SHA-256 hex digest of a file in 4 MB chunks."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4 * 1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _sign_hmac(key: bytes, msg: str) -> bytes:
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def _get_signature_key(secret_key: str, date_stamp: str, region_name: str, service_name: str) -> bytes:
    k_date = _sign_hmac(("AWS4" + secret_key).encode("utf-8"), date_stamp)
    k_region = _sign_hmac(k_date, region_name)
    k_service = _sign_hmac(k_region, service_name)
    k_signing = _sign_hmac(k_service, "aws4_request")
    return k_signing


def _build_s3_sigv4_headers(
    method: str,
    endpoint_url: str,
    bucket: str,
    object_key: str,
    access_key: str,
    secret_key: str,
    payload_hash: str,
    content_type: Optional[str] = None,
    content_length: Optional[int] = None,
    query_params: Optional[dict[str, str]] = None,
) -> tuple[str, dict[str, str]]:
    """Build target URL and AWS Signature V4 headers for Cloudflare R2 S3 API."""
    parsed = urllib.parse.urlparse(endpoint_url)
    host = parsed.netloc
    base_path = parsed.path.rstrip("/")

    quoted_bucket = urllib.parse.quote(bucket.strip("/"), safe="")
    if quoted_bucket and base_path.endswith(f"/{quoted_bucket}"):
        base_path = base_path[: -(len(quoted_bucket) + 1)]
    if object_key:
        quoted_key = "/".join(urllib.parse.quote(seg, safe="-_.~") for seg in object_key.lstrip("/").split("/"))
        canonical_uri = f"{base_path}/{quoted_bucket}/{quoted_key}"
    elif quoted_bucket:
        canonical_uri = f"{base_path}/{quoted_bucket}"
    else:
        canonical_uri = base_path or "/"

    canonical_querystring = ""
    if query_params:
        sorted_q = sorted(query_params.items(), key=lambda x: x[0])
        canonical_querystring = "&".join(
            f"{urllib.parse.quote(str(k), safe='-_.~')}={urllib.parse.quote(str(v), safe='-_.~')}"
            for k, v in sorted_q
        )

    now = datetime.datetime.now(datetime.timezone.utc)
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = now.strftime("%Y%m%d")
    region = "auto"
    service = "s3"

    headers_to_sign = {
        "host": host,
        "x-amz-content-sha256": payload_hash,
        "x-amz-date": amz_date,
    }
    if content_type:
        headers_to_sign["content-type"] = content_type

    sorted_header_keys = sorted(headers_to_sign.keys())
    canonical_headers = "".join(f"{k}:{headers_to_sign[k]}\n" for k in sorted_header_keys)
    signed_headers = ";".join(sorted_header_keys)

    canonical_request = "\n".join(
        [
            method.upper(),
            canonical_uri,
            canonical_querystring,
            canonical_headers,
            signed_headers,
            payload_hash,
        ]
    )

    algorithm = "AWS4-HMAC-SHA256"
    credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"
    string_to_sign = "\n".join(
        [
            algorithm,
            amz_date,
            credential_scope,
            hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
        ]
    )

    signing_key = _get_signature_key(secret_key, date_stamp, region, service)
    signature = hmac.new(signing_key, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()

    authorization_header = (
        f"{algorithm} Credential={access_key}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, Signature={signature}"
    )

    req_headers = {
        "Host": host,
        "x-amz-date": amz_date,
        "x-amz-content-sha256": payload_hash,
        "Authorization": authorization_header,
    }
    if content_type:
        req_headers["Content-Type"] = content_type
    if content_length is not None:
        req_headers["Content-Length"] = str(content_length)

    target_url = f"{parsed.scheme}://{host}{canonical_uri}"
    if canonical_querystring:
        target_url = f"{target_url}?{canonical_querystring}"

    return target_url, req_headers


def upload_file_to_r2(
    local_path: str,
    object_key: str,
    content_type: Optional[str] = None,
    cfg: Optional[dict] = None,
) -> dict:
    """Upload a local file (e.g. .mp4 clip or merged episode) to Cloudflare R2 Storage."""
    c = cfg or load_r2_config()
    if not os.path.isfile(local_path) or os.path.getsize(local_path) == 0:
        return {"ok": False, "error": f"File không tồn tại hoặc rỗng: {local_path}"}

    if not is_r2_configured(c):
        return {
            "ok": False,
            "skipped": True,
            "error": "Chưa cấu hình thông tin xác thực Cloudflare R2 (R2_ACCESS_KEY_ID / CF_API_TOKEN).",
        }

    file_size = os.path.getsize(local_path)
    size_mb = round(file_size / (1024 * 1024), 2)
    media_info = detect_media_info(local_path or object_key)
    if not content_type:
        content_type = media_info["mime_type"]

    bucket = c["r2_bucket_name"]
    clean_key = object_key.lstrip("/")
    if not os.path.splitext(clean_key)[1]:
        clean_key = f"{clean_key}{media_info['ext']}"
    public_url = build_r2_public_url(clean_key, c)
    last_error = ""

    # 1. Try S3-compatible endpoint with AWS Signature V4 if S3 keys are configured
    if c.get("r2_access_key_id") and c.get("r2_secret_access_key") and c.get("r2_endpoint_url"):
        try:
            payload_hash = _sha256_file_hex(local_path)
            target_url, headers = _build_s3_sigv4_headers(
                method="PUT",
                endpoint_url=c["r2_endpoint_url"],
                bucket=bucket,
                object_key=clean_key,
                access_key=c["r2_access_key_id"],
                secret_key=c["r2_secret_access_key"],
                payload_hash=payload_hash,
                content_type=content_type,
                content_length=file_size,
            )
            with open(local_path, "rb") as f:
                if requests is not None:
                    resp = requests.put(target_url, data=f, headers=headers, timeout=600)
                    status_code = resp.status_code
                    resp_text = resp.text[:300]
                else:
                    req = urllib.request.Request(target_url, data=f.read(), headers=headers, method="PUT")
                    with urllib.request.urlopen(req, timeout=600) as r:
                        status_code = r.status
                        resp_text = ""

            if status_code in (200, 201, 204):
                return {
                    "ok": True,
                    "r2_key": clean_key,
                    "r2_url": public_url,
                    "bucket": bucket,
                    "size_bytes": file_size,
                    "size_mb": size_mb,
                    "method": "s3_sigv4",
                }
            last_error = f"R2 S3 PUT HTTP {status_code}: {resp_text}"
        except Exception as e:
            last_error = f"R2 S3 PUT exception: {e}"

    # 2. Fallback to Cloudflare API v4 R2 Objects endpoint if CF_ACCOUNT_ID + CF_API_TOKEN are present
    if c.get("cf_account_id") and c.get("cf_api_token"):
        try:
            quoted_key = "/".join(urllib.parse.quote(seg, safe="-_.~") for seg in clean_key.split("/"))
            cf_url = (
                f"https://api.cloudflare.com/client/v4/accounts/{c['cf_account_id']}"
                f"/r2/buckets/{urllib.parse.quote(bucket, safe='')}/objects/{quoted_key}"
            )
            cf_headers = {
                "Authorization": f"Bearer {c['cf_api_token']}",
                "Content-Type": content_type,
                "Content-Length": str(file_size),
            }
            with open(local_path, "rb") as f:
                if requests is not None:
                    resp = requests.put(cf_url, data=f, headers=cf_headers, timeout=600)
                    status_code = resp.status_code
                    resp_text = resp.text[:300]
                else:
                    req = urllib.request.Request(cf_url, data=f.read(), headers=cf_headers, method="PUT")
                    with urllib.request.urlopen(req, timeout=600) as r:
                        status_code = r.status
                        resp_text = ""

            if status_code in (200, 201, 204):
                return {
                    "ok": True,
                    "r2_key": clean_key,
                    "r2_url": public_url,
                    "bucket": bucket,
                    "size_bytes": file_size,
                    "size_mb": size_mb,
                    "method": "cf_api_v4",
                }
            last_error = f"CF API v4 R2 PUT HTTP {status_code}: {resp_text}"
        except Exception as e:
            last_error = f"CF API v4 R2 PUT exception: {e}"

    return {"ok": False, "error": last_error or "Upload lên R2 thất bại"}


def test_r2_connection(cfg: Optional[dict] = None) -> dict:
    """Verify Cloudflare R2 credentials & bucket access."""
    c = cfg or load_r2_config()
    if not is_r2_configured(c):
        return {
            "ok": False,
            "configured": False,
            "bucket": c.get("r2_bucket_name"),
            "error": "Chưa điền thông tin kết nối R2 (R2_ACCESS_KEY_ID + R2_SECRET_ACCESS_KEY hoặc CF_API_TOKEN).",
        }

    bucket = c["r2_bucket_name"]
    last_err = ""

    if c.get("r2_access_key_id") and c.get("r2_secret_access_key") and c.get("r2_endpoint_url"):
        try:
            empty_hash = hashlib.sha256(b"").hexdigest()
            target_url, headers = _build_s3_sigv4_headers(
                method="GET",
                endpoint_url=c["r2_endpoint_url"],
                bucket=bucket,
                object_key="",
                access_key=c["r2_access_key_id"],
                secret_key=c["r2_secret_access_key"],
                payload_hash=empty_hash,
                query_params={"list-type": "2", "max-keys": "1"},
            )
            if requests is not None:
                resp = requests.get(target_url, headers=headers, timeout=15)
                code = resp.status_code
                text = resp.text[:300]
            else:
                req = urllib.request.Request(target_url, headers=headers, method="GET")
                with urllib.request.urlopen(req, timeout=15) as r:
                    code = r.status
                    text = ""

            if code == 200:
                return {
                    "ok": True,
                    "configured": True,
                    "bucket": bucket,
                    "endpoint": c["r2_endpoint_url"],
                    "public_url": c.get("r2_public_url") or f"{c['r2_endpoint_url']}/{bucket}",
                    "method": "s3_sigv4",
                    "message": f"Kết nối Cloudflare R2 Bucket '{bucket}' thành công (S3 API)!",
                }
            last_err = f"S3 HTTP {code}: {text}"
        except Exception as e:
            last_err = str(e)

    if c.get("cf_account_id") and c.get("cf_api_token"):
        try:
            cf_url = (
                f"https://api.cloudflare.com/client/v4/accounts/{c['cf_account_id']}"
                f"/r2/buckets/{urllib.parse.quote(bucket, safe='')}"
            )
            cf_headers = {"Authorization": f"Bearer {c['cf_api_token']}"}
            if requests is not None:
                resp = requests.get(cf_url, headers=cf_headers, timeout=15)
                code = resp.status_code
                text = resp.text[:300]
            else:
                req = urllib.request.Request(cf_url, headers=cf_headers, method="GET")
                with urllib.request.urlopen(req, timeout=15) as r:
                    code = r.status
                    text = ""

            if code == 200:
                return {
                    "ok": True,
                    "configured": True,
                    "bucket": bucket,
                    "public_url": c.get("r2_public_url") or f"https://{c['cf_account_id']}.r2.cloudflarestorage.com/{bucket}",
                    "method": "cf_api_v4",
                    "message": f"Kết nối Cloudflare R2 Bucket '{bucket}' thành công (Cloudflare API v4)!",
                }
            last_err = f"CF API HTTP {code}: {text}"
        except Exception as e:
            last_err = str(e)

    return {
        "ok": False,
        "configured": True,
        "bucket": bucket,
        "error": f"Không thể kết nối R2 Bucket '{bucket}': {last_err}",
    }


def list_r2_bucket_objects(prefix: str = "", cfg: Optional[dict] = None) -> list[dict]:
    """List objects in the configured R2 bucket via S3 ListObjectsV2, returning keys, sizes, public URLs, and media types."""
    import xml.etree.ElementTree as ET

    c = cfg or load_r2_config()
    if not (c.get("r2_access_key_id") and c.get("r2_secret_access_key") and c.get("r2_endpoint_url")):
        return []

    bucket = c["r2_bucket_name"]
    empty_hash = hashlib.sha256(b"").hexdigest()
    items: list[dict] = []
    cont_token: Optional[str] = None
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}

    while True:
        qp: dict[str, str] = {"list-type": "2", "max-keys": "1000"}
        if prefix:
            qp["prefix"] = prefix.lstrip("/")
        if cont_token:
            qp["continuation-token"] = cont_token

        target_url, headers = _build_s3_sigv4_headers(
            method="GET",
            endpoint_url=c["r2_endpoint_url"],
            bucket=bucket,
            object_key="",
            access_key=c["r2_access_key_id"],
            secret_key=c["r2_secret_access_key"],
            payload_hash=empty_hash,
            query_params=qp,
        )
        try:
            if requests is not None:
                resp = requests.get(target_url, headers=headers, timeout=20)
                if resp.status_code != 200:
                    break
                xml_data = resp.text
            else:
                req = urllib.request.Request(target_url, headers=headers, method="GET")
                with urllib.request.urlopen(req, timeout=20) as r:
                    xml_data = r.read().decode("utf-8")

            root = ET.fromstring(xml_data)
            for node in root.findall("s3:Contents", ns):
                k_el = node.find("s3:Key", ns)
                s_el = node.find("s3:Size", ns)
                if k_el is None or not k_el.text:
                    continue
                k = k_el.text
                sz = int(s_el.text or 0) if s_el is not None else 0
                minfo = detect_media_info(k)
                items.append(
                    {
                        "r2_key": k,
                        "r2_url": build_r2_public_url(k, c),
                        "size_bytes": sz,
                        "size_mb": round(sz / (1024 * 1024), 2),
                        "media_kind": minfo["media_kind"],
                        "mime_type": minfo["mime_type"],
                        "ext": minfo["ext"],
                    }
                )
            is_trunc = root.find("s3:IsTruncated", ns)
            if is_trunc is not None and is_trunc.text == "true":
                nxt = root.find("s3:NextContinuationToken", ns)
                cont_token = nxt.text if nxt is not None else None
                if not cont_token:
                    break
            else:
                break
        except Exception:
            break

    return items


