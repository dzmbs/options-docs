#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.32"]
# ///
"""
OKX documentation fetcher.

OKX docs are a single ~5MB Slate-generated HTML page. This script
downloads it, splits by section headings (h1/h2/h3), converts to
markdown, and saves each section as a separate file.

Sections are split at h2 level (REST API endpoints, WebSocket channels),
organized under h1 top-level directories.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
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

DOCS_URL = "https://www.okx.com/docs-v5/en/"
MANIFEST_FILE = "okx_manifest.json"

HEADERS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}


# ---------------------------------------------------------------------------
# HTML to Markdown (lightweight)
# ---------------------------------------------------------------------------

def html_to_markdown(html: str) -> str:
    """Convert an HTML fragment to markdown."""

    # Remove script/style
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)

    # Headings (h1-h6) — preserve heading level
    for i in range(6, 0, -1):
        html = re.sub(
            rf"<h{i}[^>]*>(.*?)</h{i}>",
            lambda m, level=i: f'\n\n{"#" * level} {_strip_tags(m.group(1)).strip()}\n\n',
            html, flags=re.DOTALL | re.IGNORECASE,
        )

    # Code blocks: <pre><code>...</code></pre>
    html = re.sub(
        r'<pre[^>]*><code[^>]*(?:class="[^"]*language-(\w+)[^"]*")?[^>]*>(.*?)</code></pre>',
        lambda m: f'\n\n```{m.group(1) or ""}\n{_decode_html(m.group(2)).strip()}\n```\n\n',
        html, flags=re.DOTALL | re.IGNORECASE,
    )
    html = re.sub(
        r'<pre[^>]*>(.*?)</pre>',
        lambda m: f'\n\n```\n{_decode_html(_strip_tags(m.group(1))).strip()}\n```\n\n',
        html, flags=re.DOTALL | re.IGNORECASE,
    )

    # Inline code
    html = re.sub(
        r'<code[^>]*>(.*?)</code>',
        lambda m: f'`{_decode_html(m.group(1)).strip()}`',
        html, flags=re.DOTALL | re.IGNORECASE,
    )

    # Tables
    html = _convert_tables(html)

    # Links
    html = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        lambda m: f'[{_strip_tags(m.group(2)).strip()}]({m.group(1)})',
        html, flags=re.DOTALL | re.IGNORECASE,
    )

    # Bold
    html = re.sub(
        r'<(?:strong|b)[^>]*>(.*?)</(?:strong|b)>',
        lambda m: f'**{_strip_tags(m.group(1)).strip()}**',
        html, flags=re.DOTALL | re.IGNORECASE,
    )

    # Italic
    html = re.sub(
        r'<(?:em|i)[^>]*>(.*?)</(?:em|i)>',
        lambda m: f'*{_strip_tags(m.group(1)).strip()}*',
        html, flags=re.DOTALL | re.IGNORECASE,
    )

    # List items
    html = re.sub(
        r'<li[^>]*>(.*?)</li>',
        lambda m: f'- {_strip_tags(m.group(1)).strip()}\n',
        html, flags=re.DOTALL | re.IGNORECASE,
    )

    # Paragraphs, divs, br, hr
    html = re.sub(r'<br\s*/?>', '\n', html, flags=re.IGNORECASE)
    html = re.sub(r'<p[^>]*>(.*?)</p>', lambda m: f'\n\n{m.group(1).strip()}\n\n', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<hr\s*/?>', '\n\n---\n\n', html, flags=re.IGNORECASE)

    # Strip remaining tags
    html = re.sub(r'<[^>]+>', '', html)

    # Decode entities
    html = _decode_html(html)

    # Clean whitespace
    html = re.sub(r'\n{3,}', '\n\n', html)
    html = re.sub(r' +', ' ', html)
    html = '\n'.join(line.rstrip() for line in html.splitlines())
    html = html.strip() + '\n'

    return html


def _strip_tags(html: str) -> str:
    return re.sub(r'<[^>]+>', '', html)


def _decode_html(text: str) -> str:
    for old, new in [
        ('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'),
        ('&quot;', '"'), ('&#39;', "'"), ('&apos;', "'"),
        ('&nbsp;', ' '), ('&#x27;', "'"), ('&#x2F;', '/'),
    ]:
        text = text.replace(old, new)
    return text


def _convert_tables(html: str) -> str:
    def _table_to_md(match: re.Match) -> str:
        table_html = match.group(0)
        rows: list[list[str]] = []
        for tr in re.finditer(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL | re.IGNORECASE):
            cells = [_strip_tags(c.group(1)).strip()
                     for c in re.finditer(r'<(?:td|th)[^>]*>(.*?)</(?:td|th)>', tr.group(1), re.DOTALL | re.IGNORECASE)]
            if cells:
                rows.append(cells)
        if not rows:
            return ''
        max_cols = max(len(r) for r in rows)
        for r in rows:
            while len(r) < max_cols:
                r.append('')
        lines = ['| ' + ' | '.join(rows[0]) + ' |',
                 '| ' + ' | '.join('---' for _ in rows[0]) + ' |']
        for row in rows[1:]:
            lines.append('| ' + ' | '.join(row) + ' |')
        return '\n\n' + '\n'.join(lines) + '\n\n'

    return re.sub(r'<table[^>]*>.*?</table>', _table_to_md, html, flags=re.DOTALL | re.IGNORECASE)


# ---------------------------------------------------------------------------
# Section splitting
# ---------------------------------------------------------------------------

def split_into_sections(html: str) -> list[dict[str, str]]:
    """Split the monolithic HTML into sections at h1/h2 boundaries.

    Returns a list of dicts with keys: id, title, level, html
    Each h2 section includes its child h3 sections.
    """
    # Extract just the content div
    content_match = re.search(r'<div class="page-wrapper">(.*)', html, re.DOTALL)
    if content_match:
        html = content_match.group(1)

    # Split on h1 and h2 headings
    # Pattern: find all <h1 id='...'> and <h2 id='...'>
    heading_pattern = re.compile(
        r"(<h([12])\s+id='([^']*)'[^>]*>([^<]*)</h\2>)",
        re.IGNORECASE,
    )

    matches = list(heading_pattern.finditer(html))
    if not matches:
        return []

    sections: list[dict[str, str]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(html)

        section_html = html[start:end]
        sections.append({
            "id": match.group(3),
            "title": match.group(4).strip(),
            "level": int(match.group(2)),
            "html": section_html,
        })

    return sections


def section_to_filepath(section: dict[str, str], current_h1: str) -> str:
    """Convert a section to a file path.

    h1 sections -> directory/README.md
    h2 sections -> directory/section-name.md
    """
    section_id = section["id"]

    if section["level"] == 1:
        return f"{section_id}/README.md"

    # h2: goes under its parent h1 directory
    # The id format is like "trading-account-rest-api-get-balance"
    # We want: trading-account/rest-api-get-balance.md
    if current_h1 and section_id.startswith(current_h1 + "-"):
        remainder = section_id[len(current_h1) + 1:]
    else:
        remainder = section_id

    return f"{current_h1}/{remainder}.md"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    start = datetime.now()
    logger.info("Starting OKX documentation fetch")

    out_dir = Path(__file__).resolve().parent / "okx"
    out_dir.mkdir(exist_ok=True)

    # Download the monolithic page
    logger.info(f"Downloading {DOCS_URL} ...")
    resp = requests.get(DOCS_URL, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    raw_html = resp.text
    logger.info(f"Downloaded {len(raw_html):,} bytes")

    # Split into sections
    sections = split_into_sections(raw_html)
    logger.info(f"Split into {len(sections)} sections")

    if not sections:
        logger.error("No sections found!")
        sys.exit(1)

    manifest: Manifest = {"files": {}}
    current_h1 = ""
    successful = 0

    for i, section in enumerate(sections, 1):
        if section["level"] == 1:
            current_h1 = section["id"]

        rel_path = section_to_filepath(section, current_h1)
        logger.info(f"[{i}/{len(sections)}] {rel_path}")

        content = html_to_markdown(section["html"])
        content_hash = hashlib.sha256(content.encode()).hexdigest()

        dest = out_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")

        manifest["files"][rel_path] = {
            "section_id": section["id"],
            "title": section["title"],
            "hash": content_hash,
            "last_updated": datetime.now().isoformat(),
        }
        successful += 1

    manifest["fetch_metadata"] = {
        "completed_at": datetime.now().isoformat(),
        "duration_seconds": (datetime.now() - start).total_seconds(),
        "source_url": DOCS_URL,
        "raw_html_bytes": len(raw_html),
        "sections_total": len(sections),
        "files_written": successful,
    }
    manifest["last_updated"] = datetime.now().isoformat()
    manifest["source"] = DOCS_URL

    manifest_path = out_dir / MANIFEST_FILE
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    logger.info("=" * 50)
    logger.info(f"Done in {datetime.now() - start}")
    logger.info(f"Wrote {successful} files from {len(sections)} sections")
    logger.info(f"Output: {out_dir}")


if __name__ == "__main__":
    main()
