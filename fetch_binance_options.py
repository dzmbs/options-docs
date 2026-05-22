#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.32"]
# ///
"""
Binance Options Trading documentation fetcher.

Scrapes all pages from the Binance developer docs Options Trading section,
converts HTML to clean markdown, and saves locally.
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
from urllib.parse import urlparse

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

Manifest = dict[str, Any]

BASE_URL = "https://developers.binance.com"
DOCS_PREFIX = "/docs/derivatives/options-trading"

HEADERS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

MAX_RETRIES = 3
RETRY_DELAY = 2
RATE_LIMIT_DELAY = 1.0

MANIFEST_FILE = "binance_options_manifest.json"

# ---------------------------------------------------------------------------
# All known pages in the Options Trading section
# ---------------------------------------------------------------------------

PAGES: list[str] = [
    # Top-level
    "general-info",
    "common-definition",
    # Market Data
    "market-data",
    "market-data/Check-Server-Time",
    "market-data/Test-Connectivity",
    "market-data/24hr-Ticker-Price-Change-Statistics",
    "market-data/Exchange-Information",
    "market-data/Historical-Exercise-Records",
    "market-data/Open-Interest",
    "market-data/Order-Book",
    "market-data/Recent-Trades-List",
    "market-data/Recent-Block-Trade-List",
    "market-data/Symbol-Price-Ticker",
    "market-data/Kline-Candlestick-Data",
    "market-data/Option-Mark-Price",
    # Account
    "account",
    "account/Account-Funding-Flow",
    "account/Funds-Transfer",
    # Trade
    "trade",
    "trade/Place-Multiple-Orders",
    "trade/Cancel-Option-Order",
    "trade/Cancel-Multiple-Option-Orders",
    "trade/Cancel-All-Option-Orders-By-Underlying",
    "trade/Cancel-all-Option-orders-on-specific-symbol",
    "trade/Query-Single-Order",
    "trade/Query-Option-Order-History",
    "trade/Query-Current-Open-Option-Orders",
    "trade/Option-Position-Information",
    "trade/User-Exercise-Record",
    "trade/Account-Trade-List",
    "trade/User-Commission",
    # Websocket Market Streams
    "websocket-market-streams",
    "websocket-market-streams/Live-Subscribing-Unsubscribing-to-streams",
    "websocket-market-streams/New-Symbol-Info",
    "websocket-market-streams/Open-Interest",
    "websocket-market-streams/Mark-Price",
    "websocket-market-streams/Kline-Candlestick-Streams",
    "websocket-market-streams/Index-Price-Streams",
    "websocket-market-streams/Bookticker",
    "websocket-market-streams/24-hour-TICKER",
    "websocket-market-streams/Trade-Streams",
    "websocket-market-streams/Partial-Book-Depth-Streams",
    "websocket-market-streams/Diff-Book-Depth-Streams",
    "websocket-market-streams/How-to-manage-a-local-order-book-correctly",
    # User Data Streams
    "user-data-streams",
    "user-data-streams/Start-User-Data-Stream",
    "user-data-streams/Keepalive-User-Data-Stream",
    "user-data-streams/Close-User-Data-Stream",
    "user-data-streams/Event-User-Data-Stream-Expired",
    "user-data-streams/Event-Risk-level-change",
    "user-data-streams/Event-Order-update",
    "user-data-streams/Event-Account-data",
    "user-data-streams/Event-Balance-and-Position-Update",
    "user-data-streams/Event-Greek-Update",
    # Market Maker Endpoints
    "market-maker-endpoints",
    "market-maker-endpoints/Get-Auto-Cancel-All-Open-Orders-Config",
    "market-maker-endpoints/Set-Market-Maker-Protection-Config",
    "market-maker-endpoints/Auto-Cancel-All-Open-Orders-Heartbeat",
    "market-maker-endpoints/Reset-Market-Maker-Protection-Config",
    "market-maker-endpoints/Set-Auto-Cancel-All-Open-Orders-Config",
    # Market Maker Block Trade
    "market-maker-block-trade",
    "market-maker-block-trade/New-Block-Trade-Order",
    "market-maker-block-trade/Cancel-Block-Trade-Order",
    "market-maker-block-trade/Extend-Block-Trade-Order",
    "market-maker-block-trade/Query-Block-Trade-Order",
    "market-maker-block-trade/Accept-Block-Trade-Order",
    "market-maker-block-trade/Query-Block-Trade-Detail",
    "market-maker-block-trade/Account-Block-Trade-List",
    # FAQ
    "faq/stp-faq",
    # Error Code
    "error-code",
]


# ---------------------------------------------------------------------------
# HTML to Markdown conversion (lightweight, no extra deps)
# ---------------------------------------------------------------------------

def html_to_markdown(html: str) -> str:
    """Extract main content from Binance docs HTML and convert to markdown.

    This is a pragmatic converter — it handles the common elements found in
    Binance API docs (headings, tables, code blocks, lists, links, bold/italic)
    without requiring beautifulsoup or other heavy dependencies.
    """
    import re

    # Try to extract just the main content area
    # Binance docs typically have a main content div
    main_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html, re.DOTALL | re.IGNORECASE,
    )
    if not main_match:
        main_match = re.search(
            r'<main[^>]*>(.*?)</main>',
            html, re.DOTALL | re.IGNORECASE,
        )
    if not main_match:
        # Try the content div pattern common in Binance docs
        main_match = re.search(
            r'class="[^"]*content[^"]*"[^>]*>(.*?)(?=<footer|<nav\s)',
            html, re.DOTALL | re.IGNORECASE,
        )

    content = main_match.group(1) if main_match else html

    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Convert headings
    for i in range(6, 0, -1):
        content = re.sub(
            rf'<h{i}[^>]*>(.*?)</h{i}>',
            lambda m, level=i: f'\n\n{"#" * level} {_strip_tags(m.group(1)).strip()}\n\n',
            content, flags=re.DOTALL | re.IGNORECASE,
        )

    # Convert code blocks
    content = re.sub(
        r'<pre[^>]*><code[^>]*(?:class="[^"]*language-(\w+)[^"]*")?[^>]*>(.*?)</code></pre>',
        lambda m: f'\n\n```{m.group(1) or ""}\n{_decode_html(m.group(2)).strip()}\n```\n\n',
        content, flags=re.DOTALL | re.IGNORECASE,
    )
    content = re.sub(
        r'<pre[^>]*>(.*?)</pre>',
        lambda m: f'\n\n```\n{_decode_html(_strip_tags(m.group(1))).strip()}\n```\n\n',
        content, flags=re.DOTALL | re.IGNORECASE,
    )

    # Convert inline code
    content = re.sub(
        r'<code[^>]*>(.*?)</code>',
        lambda m: f'`{_decode_html(m.group(1)).strip()}`',
        content, flags=re.DOTALL | re.IGNORECASE,
    )

    # Convert tables
    content = _convert_tables(content)

    # Convert links
    content = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        lambda m: f'[{_strip_tags(m.group(2)).strip()}]({m.group(1)})',
        content, flags=re.DOTALL | re.IGNORECASE,
    )

    # Convert bold/strong
    content = re.sub(
        r'<(?:strong|b)[^>]*>(.*?)</(?:strong|b)>',
        lambda m: f'**{_strip_tags(m.group(1)).strip()}**',
        content, flags=re.DOTALL | re.IGNORECASE,
    )

    # Convert italic/em
    content = re.sub(
        r'<(?:em|i)[^>]*>(.*?)</(?:em|i)>',
        lambda m: f'*{_strip_tags(m.group(1)).strip()}*',
        content, flags=re.DOTALL | re.IGNORECASE,
    )

    # Convert list items
    content = re.sub(
        r'<li[^>]*>(.*?)</li>',
        lambda m: f'- {_strip_tags(m.group(1)).strip()}\n',
        content, flags=re.DOTALL | re.IGNORECASE,
    )

    # Convert <br> to newlines
    content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)

    # Convert <p> to double newlines
    content = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: f'\n\n{m.group(1).strip()}\n\n', content, flags=re.DOTALL | re.IGNORECASE)

    # Convert <hr> to ---
    content = re.sub(r'<hr\s*/?>', '\n\n---\n\n', content, flags=re.IGNORECASE)

    # Strip remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode HTML entities
    content = _decode_html(content)

    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r' +', ' ', content)
    content = '\n'.join(line.rstrip() for line in content.splitlines())
    content = content.strip() + '\n'

    return content


def _strip_tags(html: str) -> str:
    import re
    return re.sub(r'<[^>]+>', '', html)


def _decode_html(text: str) -> str:
    """Decode common HTML entities."""
    replacements = [
        ('&amp;', '&'),
        ('&lt;', '<'),
        ('&gt;', '>'),
        ('&quot;', '"'),
        ('&#39;', "'"),
        ('&apos;', "'"),
        ('&nbsp;', ' '),
        ('&#x27;', "'"),
        ('&#x2F;', '/'),
        ('&#47;', '/'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def _convert_tables(html: str) -> str:
    """Convert HTML tables to markdown tables."""
    import re

    def _table_to_md(match: re.Match) -> str:  # type: ignore[type-arg]
        table_html = match.group(0)
        rows: list[list[str]] = []

        for tr_match in re.finditer(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL | re.IGNORECASE):
            cells: list[str] = []
            for cell_match in re.finditer(r'<(?:td|th)[^>]*>(.*?)</(?:td|th)>', tr_match.group(1), re.DOTALL | re.IGNORECASE):
                cells.append(_strip_tags(cell_match.group(1)).strip())
            if cells:
                rows.append(cells)

        if not rows:
            return ''

        # Normalize column count
        max_cols = max(len(r) for r in rows)
        for r in rows:
            while len(r) < max_cols:
                r.append('')

        lines: list[str] = []
        # Header row
        lines.append('| ' + ' | '.join(rows[0]) + ' |')
        lines.append('| ' + ' | '.join('---' for _ in rows[0]) + ' |')
        # Data rows
        for row in rows[1:]:
            lines.append('| ' + ' | '.join(row) + ' |')

        return '\n\n' + '\n'.join(lines) + '\n\n'

    return re.sub(r'<table[^>]*>.*?</table>', _table_to_md, html, flags=re.DOTALL | re.IGNORECASE)


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
    manifest["source"] = f"{BASE_URL}{DOCS_PREFIX}"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def fetch_page(url: str, session: requests.Session) -> str:
    """Fetch a page and return its HTML content."""
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
            return resp.text

        except requests.exceptions.RequestException as e:
            logger.warning(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                delay = min(RETRY_DELAY * (2 ** attempt), 30)
                time.sleep(delay * random.uniform(0.5, 1.0))
            else:
                raise

    raise RuntimeError(f"Failed to fetch {url} after {MAX_RETRIES} attempts")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    start = datetime.now()
    logger.info("Starting Binance Options Trading documentation fetch")

    out_dir = Path(__file__).resolve().parent / "binance"
    out_dir.mkdir(exist_ok=True)

    manifest = load_manifest(out_dir)
    new_manifest: Manifest = {"files": {}}

    successful = 0
    failed = 0
    failed_pages: list[str] = []

    with requests.Session() as session:
        total = len(PAGES)
        for i, page_path in enumerate(PAGES, 1):
            url = f"{BASE_URL}{DOCS_PREFIX}/{page_path}"
            rel_path = f"{page_path}.md"
            logger.info(f"[{i}/{total}] {url}  →  {rel_path}")

            try:
                html = fetch_page(url, session)
                content = html_to_markdown(html)

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
        "pages_total": len(PAGES),
        "pages_fetched": successful,
        "pages_failed": failed,
        "failed_pages": failed_pages,
    }

    save_manifest(out_dir, new_manifest)

    logger.info("=" * 50)
    logger.info(f"Done in {datetime.now() - start}")
    logger.info(f"Fetched: {successful}/{len(PAGES)}  |  Failed: {failed}")

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
