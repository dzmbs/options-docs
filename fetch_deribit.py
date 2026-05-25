#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.32"]
# ///
"""
Deribit documentation fetcher.

Fetches all pages from docs.deribit.com using their .md endpoints
(discovered via llms.txt). Deribit is an options-first exchange so
all API docs are relevant.
"""

from __future__ import annotations

import hashlib
import json
import logging
import random
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

Manifest = dict[str, Any]

BASE_URL = "https://docs.deribit.com"
LLMS_TXT_URL = f"{BASE_URL}/llms.txt"
MANIFEST_FILE = "deribit_manifest.json"

HEADERS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/markdown, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
}

MAX_RETRIES = 3
RETRY_DELAY = 2
RATE_LIMIT_DELAY = 0.5


# ---------------------------------------------------------------------------
# URL discovery from llms.txt
# ---------------------------------------------------------------------------

def discover_pages(session: requests.Session) -> list[str]:
    """Parse llms.txt to extract all .md URLs."""
    logger.info(f"Discovering pages from {LLMS_TXT_URL}")
    resp = session.get(LLMS_TXT_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    import re
    urls = re.findall(r'https://docs\.deribit\.com/[^\s\)]+\.md', resp.text)
    # Deduplicate and sort
    urls = sorted(set(urls))
    logger.info(f"Discovered {len(urls)} pages")
    return urls


def url_to_filepath(url: str) -> str:
    """Convert a full URL to a relative file path.

    https://docs.deribit.com/api-reference/trading/private-buy.md
      -> api-reference/trading/private-buy.md
    """
    return url.replace(f"{BASE_URL}/", "")


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def fetch_markdown(url: str, session: requests.Session) -> str:
    """Fetch markdown content from a .md URL."""
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.get(url, headers=HEADERS, timeout=30, allow_redirects=True)

            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 60))
                logger.warning(f"Rate-limited, waiting {wait}s …")
                time.sleep(wait)
                continue

            if resp.status_code == 404:
                raise ValueError(f"Page not found: {url}")

            resp.raise_for_status()
            content = resp.text

            # Sanity check — should be markdown, not HTML
            if content.strip().startswith("<!DOCTYPE") or "<html" in content[:200]:
                raise ValueError("Received HTML instead of markdown")

            return content

        except requests.exceptions.RequestException as e:
            logger.warning(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                delay = min(RETRY_DELAY * (2 ** attempt), 30)
                time.sleep(delay * random.uniform(0.5, 1.0))
            else:
                raise
        except ValueError:
            raise

    raise RuntimeError(f"Failed to fetch {url} after {MAX_RETRIES} attempts")


# ---------------------------------------------------------------------------
# Manifest helpers
# ---------------------------------------------------------------------------

def load_manifest(out_dir: Path) -> Manifest:
    manifest_path = out_dir / MANIFEST_FILE
    if manifest_path.exists():
        try:
            return json.loads(manifest_path.read_text())
        except Exception:
            pass
    return {"files": {}, "last_updated": None}


def save_manifest(out_dir: Path, manifest: Manifest) -> None:
    manifest_path = out_dir / MANIFEST_FILE
    manifest["last_updated"] = datetime.now().isoformat()
    manifest["source"] = BASE_URL
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    start = datetime.now()
    logger.info("Starting Deribit documentation fetch")

    out_dir = Path(__file__).resolve().parent / "deribit"
    out_dir.mkdir(exist_ok=True)

    manifest = load_manifest(out_dir)
    new_manifest: Manifest = {"files": {}}

    successful = 0
    failed = 0
    failed_pages: list[str] = []

    with requests.Session() as session:
        pages = discover_pages(session)
        if not pages:
            logger.error("No pages discovered!")
            sys.exit(1)

        total = len(pages)
        for i, url in enumerate(pages, 1):
            rel_path = url_to_filepath(url)
            logger.info(f"[{i}/{total}] {rel_path}")

            try:
                content = fetch_markdown(url, session)

                old_hash = manifest.get("files", {}).get(rel_path, {}).get("hash", "")
                new_hash = hashlib.sha256(content.encode()).hexdigest()

                dest = out_dir / rel_path
                dest.parent.mkdir(parents=True, exist_ok=True)

                if new_hash != old_hash:
                    dest.write_text(content, encoding="utf-8")
                    logger.info(f"  Updated: {rel_path}")
                    last_updated = datetime.now().isoformat()
                else:
                    logger.info(f"  Unchanged: {rel_path}")
                    last_updated = str(
                        manifest.get("files", {}).get(rel_path, {}).get("last_updated", datetime.now().isoformat())
                    )

                new_manifest["files"][rel_path] = {
                    "source_url": url,
                    "hash": new_hash,
                    "last_updated": last_updated,
                }
                successful += 1

                if i < total:
                    time.sleep(RATE_LIMIT_DELAY)

            except Exception as e:
                logger.error(f"  Failed: {e}")
                failed += 1
                failed_pages.append(url)

    new_manifest["fetch_metadata"] = {
        "completed_at": datetime.now().isoformat(),
        "duration_seconds": (datetime.now() - start).total_seconds(),
        "pages_total": total,
        "pages_fetched": successful,
        "pages_failed": failed,
        "failed_pages": failed_pages,
    }

    save_manifest(out_dir, new_manifest)

    logger.info("=" * 50)
    logger.info(f"Done in {datetime.now() - start}")
    logger.info(f"Fetched: {successful}/{total}  |  Failed: {failed}")

    if failed_pages:
        logger.warning("Failed pages:")
        for p in failed_pages:
            logger.warning(f"  - {p}")
        if successful == 0:
            sys.exit(1)
    else:
        logger.info("All pages fetched successfully!")


if __name__ == "__main__":
    main()
