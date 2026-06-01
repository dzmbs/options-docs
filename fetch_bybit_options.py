#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Bybit Options documentation fetcher.

Clones/pulls the bybit-exchange/docs repo and extracts all options-relevant
files into bybit/. Bybit uses a unified v5 API where options are
category=option, so we cherry-pick the relevant files.
"""

from __future__ import annotations

import hashlib
import json
import logging
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

REPO_URL = "https://github.com/bybit-exchange/docs.git"
MANIFEST_FILE = "bybit_options_manifest.json"

# ---------------------------------------------------------------------------
# Files to extract from the bybit docs repo (relative to docs/v5/)
# These are all endpoints that cover category=option
# ---------------------------------------------------------------------------

# Options-only files
OPTIONS_ONLY = [
    "market/iv.mdx",                          # Historical Volatility (option only)
    "account/coin-greeks.mdx",                # Coin Greeks (option only)
    "account/set-mmp.mdx",                    # Set MMP (market maker protection, option)
    "account/reset-mmp.mdx",                  # Reset MMP
    "account/get-mmp-state.mdx",              # Get MMP State
    "websocket/private/greek.mdx",            # Greeks websocket (option only)
]

# Shared endpoints that support category=option
SHARED_WITH_OPTIONS = [
    # General / reference
    "intro.mdx",
    "enum.mdx",
    "error.mdx",
    "guide.mdx",
    "smp.mdx",
    "acct-mode.mdx",

    # Market data
    "market/instrument.mdx",                  # Get Instruments Info
    "market/orderbook.mdx",                   # Get Orderbook
    "market/tickers.mdx",                     # Get Tickers
    "market/recent-trade.mdx",                # Get Recent Trade
    "market/delivery-price.mdx",              # Get Delivery Price
    "market/new-delivery-price.mdx",          # Get Delivery Price (new)

    # Order
    "order/create-order.mdx",                 # Place Order
    "order/amend-order.mdx",                  # Amend Order
    "order/cancel-order.mdx",                 # Cancel Order
    "order/open-order.mdx",                   # Get Open Orders
    "order/cancel-all.mdx",                   # Cancel All Orders
    "order/order-list.mdx",                   # Get Order History
    "order/execution.mdx",                    # Get Trade History
    "order/batch-place.mdx",                  # Batch Place Order
    "order/batch-amend.mdx",                  # Batch Amend Order
    "order/batch-cancel.mdx",                 # Batch Cancel Order
    "order/dcp.mdx",                          # Dead Man's Switch (DCP)
    "order/pre-check-order.mdx",              # Pre-check Order

    # Position
    "position/position.mdx",                  # Get Position Info
    "position/close-position.mdx",            # Close Position (confirm)
    "position/move-position.mdx",             # Move Position
    "position/move-position-history.mdx",     # Get Move Position History

    # Account
    "account/wallet-balance.mdx",             # Get Wallet Balance
    "account/fee-rate.mdx",                   # Get Fee Rate
    "account/account-info.mdx",               # Get Account Info
    "account/transaction-log.mdx",            # Get Transaction Log
    "account/set-margin-mode.mdx",            # Set Margin Mode
    "account/dcp-info.mdx",                   # Get DCP Info
    "account/unified-trans-amnt.mdx",         # Get Unified Account Info

    # Websocket public
    "websocket/public/orderbook.mdx",
    "websocket/public/trade.mdx",
    "websocket/public/ticker.mdx",
    "websocket/public/kline.mdx",
    "websocket/public/all-liquidation.mdx",

    # Websocket private
    "websocket/private/order.mdx",
    "websocket/private/execution.mdx",
    "websocket/private/fast-execution.mdx",
    "websocket/private/position.mdx",
    "websocket/private/wallet.mdx",
    "websocket/private/dcp.mdx",
    "websocket/wss-authentication.mdx",
    "websocket/trade/guideline.mdx",

    # Rate limits
    "rate-limit/rate-limit.mdx",

    # Pre-upgrade
    "pre-upgrade/order-list.mdx",
    "pre-upgrade/execution.mdx",
    "pre-upgrade/delivery.mdx",
    "pre-upgrade/settlement.mdx",
    "pre-upgrade/transaction-log.mdx",

    # Asset
    "asset/delivery.mdx",
]

# RFQ (block trading for options) — include entire section
RFQ_FILES = [
    "rfq/basic-workflow.mdx",
    "rfq/trade/create-rfq.mdx",
    "rfq/trade/cancel-rfq.mdx",
    "rfq/trade/cancel-all-rfq.mdx",
    "rfq/trade/rfq-realtime.mdx",
    "rfq/trade/rfq-list.mdx",
    "rfq/trade/rfq-config.mdx",
    "rfq/trade/create-quote.mdx",
    "rfq/trade/cancel-quote.mdx",
    "rfq/trade/cancel-all-quotes.mdx",
    "rfq/trade/quote-realtime.mdx",
    "rfq/trade/quote-list.mdx",
    "rfq/trade/execute-quote.mdx",
    "rfq/trade/accept-other-quote.mdx",
    "rfq/trade/trade-list.mdx",
    "rfq/trade/public-trades.mdx",
    "rfq/websocket/private/inquiry.mdx",
    "rfq/websocket/private/quote.mdx",
    "rfq/websocket/private/transaction.mdx",
    "rfq/websocket/public/public-transaction.mdx",
]

ALL_FILES = OPTIONS_ONLY + SHARED_WITH_OPTIONS + RFQ_FILES


def clone_or_pull(repo_dir: Path) -> None:
    """Clone the repo if missing, otherwise pull latest."""
    if (repo_dir / ".git").exists():
        logger.info("Pulling latest changes from bybit-exchange/docs...")
        subprocess.run(
            ["git", "-C", str(repo_dir), "pull", "--ff-only"],
            check=True, capture_output=True, text=True,
        )
    else:
        logger.info("Cloning bybit-exchange/docs (shallow)...")
        subprocess.run(
            ["git", "clone", "--depth", "1", REPO_URL, str(repo_dir)],
            check=True, capture_output=True, text=True,
        )


def main() -> None:
    start = datetime.now()
    logger.info("Starting Bybit Options documentation fetch")

    script_dir = Path(__file__).resolve().parent
    repo_dir = script_dir / ".bybit-docs-upstream"
    out_dir = script_dir / "bybit"
    out_dir.mkdir(exist_ok=True)

    # Clone/pull
    clone_or_pull(repo_dir)

    v5_dir = repo_dir / "docs" / "v5"
    if not v5_dir.exists():
        logger.error(f"Expected v5 docs at {v5_dir} — not found!")
        sys.exit(1)

    manifest: dict = {"files": {}}
    successful = 0
    failed = 0
    failed_files: list[str] = []

    for rel_path in ALL_FILES:
        src = v5_dir / rel_path
        dest = out_dir / rel_path

        if not src.exists():
            logger.warning(f"  Not found: {rel_path}")
            failed += 1
            failed_files.append(rel_path)
            continue

        content = src.read_text(encoding="utf-8")
        content_hash = hashlib.sha256(content.encode()).hexdigest()

        dest.parent.mkdir(parents=True, exist_ok=True)

        # Check if changed
        if dest.exists():
            old_content = dest.read_text(encoding="utf-8")
            old_hash = hashlib.sha256(old_content.encode()).hexdigest()
            if old_hash == content_hash:
                logger.info(f"  Unchanged: {rel_path}")
                manifest["files"][rel_path] = {
                    "hash": content_hash,
                    "last_updated": datetime.now().isoformat(),
                }
                successful += 1
                continue

        dest.write_text(content, encoding="utf-8")
        logger.info(f"  Updated: {rel_path}")
        manifest["files"][rel_path] = {
            "hash": content_hash,
            "last_updated": datetime.now().isoformat(),
        }
        successful += 1

    # Clean up files that are no longer in our list
    for md_file in out_dir.rglob("*.mdx"):
        rel = str(md_file.relative_to(out_dir))
        if rel not in ALL_FILES:
            logger.info(f"  Removing obsolete: {rel}")
            md_file.unlink()

    manifest["fetch_metadata"] = {
        "completed_at": datetime.now().isoformat(),
        "duration_seconds": (datetime.now() - start).total_seconds(),
        "source_repo": REPO_URL,
        "files_total": len(ALL_FILES),
        "files_fetched": successful,
        "files_failed": failed,
        "failed_files": failed_files,
    }
    manifest["last_updated"] = datetime.now().isoformat()

    manifest_path = out_dir / MANIFEST_FILE
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    logger.info("=" * 50)
    logger.info(f"Done in {datetime.now() - start}")
    logger.info(f"Fetched: {successful}/{len(ALL_FILES)}  |  Failed: {failed}")

    if failed_files:
        logger.warning("Missing files:")
        for f in failed_files:
            logger.warning(f"  - {f}")

    logger.info(f"Output: {out_dir}")


if __name__ == "__main__":
    main()
