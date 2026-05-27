#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.32"]
# ///
"""
Derive (formerly Lyra) documentation fetcher.

Fetches all pages from docs.derive.xyz using .md endpoints.
Derive is a ReadMe.com-powered site that serves markdown at URL.md.
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

BASE_URL = "https://docs.derive.xyz"
MANIFEST_FILE = "derive_manifest.json"

HEADERS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/markdown, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
}

MAX_RETRIES = 3
RETRY_DELAY = 2
RATE_LIMIT_DELAY = 0.5

# ---------------------------------------------------------------------------
# All known pages (from sidebar navigation)
# ---------------------------------------------------------------------------

PAGES: list[str] = [
    # OVERVIEW
    "reference/overview",
    "reference/onboard-via-interface",
    "reference/ux-create-or-deposit-to-subaccount",
    "reference/create-session-keys",
    "reference/multiple-subaccounts",
    "reference/transfer",
    "reference/ux-withdraw",
    "reference/onboard-manually",
    "reference/deposit-to-lyra-chain",
    "reference/create-or-deposit-to-subaccount",
    "reference/on-chain-manage-session-keys",
    "reference/on-chain-withdraw",
    "reference/json-rpc",
    "reference/naming",
    "reference/authentication",
    "reference/session-keys",
    "reference/rate-limits",
    "reference/protocol-constants",
    "reference/fees-1",
    "reference/api-broker",
    "reference/builder-fee",
    "reference/institutional-trading-rewards-program",
    "reference/matching-algorithms",

    # REST API - Public
    "reference/post_public-build-register-session-key-tx",
    "reference/post_public-register-session-key",
    "reference/post_public-deregister-session-key",
    "reference/post_public-login",
    "reference/post_public-statistics",
    "reference/post_public-get-all-currencies",
    "reference/post_public-get-currency",
    "reference/post_public-get-instrument",
    "reference/post_public-get-all-instruments",
    "reference/post_public-get-instruments",
    "reference/post_public-get-ticker",
    "reference/post_public-get-latest-signed-feeds",
    "reference/post_public-get-option-settlement-prices",
    "reference/post_public-get-spot-feed-history",
    "reference/post_public-get-spot-feed-history-candles",
    "reference/post_public-get-funding-rate-history",
    "reference/post_public-get-trade-history",
    "reference/post_public-get-option-settlement-history",
    "reference/post_public-get-liquidation-history",
    "reference/post_public-get-interest-rate-history",
    "reference/post_public-get-transaction",
    "reference/post_public-get-margin",
    "reference/post_public-margin-watch",
    "reference/post_public-get-vault-share",
    "reference/post_public-get-vault-statistics",
    "reference/post_public-get-vault-balances",
    "reference/post_public-create-subaccount-debug",
    "reference/post_public-deposit-debug",
    "reference/post_public-withdraw-debug",
    "reference/post_public-send-quote-debug",
    "reference/post_public-execute-quote-debug",
    "reference/post_public-get-time",
    "reference/post_public-get-live-incidents",
    "reference/post_public-get-maker-programs",
    "reference/post_public-get-maker-program-scores",
    "reference/post_public-get-referral-performance",
    "reference/post_public-get-tickers",

    # REST API - Private
    "reference/post_private-get-account",
    "reference/post_private-create-subaccount",
    "reference/post_private-get-subaccount",
    "reference/post_private-get-subaccounts",
    "reference/post_private-get-all-portfolios",
    "reference/post_private-change-subaccount-label",
    "reference/post_private-get-notifications",
    "reference/post_private-update-notifications",
    "reference/post_private-deposit",
    "reference/post_private-withdraw",
    "reference/post_private-transfer-erc20",
    "reference/post_private-transfer-position",
    "reference/post_private-transfer-positions",
    "reference/post_private-order",
    "reference/post_private-replace",
    "reference/post_private-order-debug",
    "reference/post_private-get-order",
    "reference/post_private-get-orders",
    "reference/post_private-get-open-orders",
    "reference/post_private-cancel",
    "reference/post_private-cancel-by-label",
    "reference/post_private-cancel-by-nonce",
    "reference/post_private-cancel-by-instrument",
    "reference/post_private-cancel-all",
    "reference/post_private-cancel-trigger-order",
    "reference/post_private-get-order-history",
    "reference/post_private-get-trade-history",
    "reference/post_private-get-deposit-history",
    "reference/post_private-get-withdrawal-history",
    "reference/post_private-send-rfq",
    "reference/post_private-cancel-rfq",
    "reference/post_private-cancel-batch-rfqs",
    "reference/post_private-get-rfqs",
    "reference/post_private-poll-rfqs",
    "reference/post_private-send-quote",
    "reference/post_private-cancel-quote",
    "reference/post_private-cancel-batch-quotes",
    "reference/post_private-get-quotes",
    "reference/post_private-poll-quotes",
    "reference/post_private-execute-quote",
    "reference/post_private-rfq-get-best-quote",
    "reference/post_private-get-margin",
    "reference/post_private-get-collaterals",
    "reference/post_private-get-positions",
    "reference/post_private-get-option-settlement-history",
    "reference/post_private-get-subaccount-value-history",
    "reference/post_private-expired-and-cancelled-history",
    "reference/post_private-get-funding-history",
    "reference/post_private-get-interest-history",
    "reference/post_private-get-erc20-transfer-history",
    "reference/post_private-get-liquidation-history",
    "reference/post_private-liquidate",
    "reference/post_private-get-liquidator-history",
    "reference/post_private-session-keys",
    "reference/post_private-edit-session-key",
    "reference/post_private-register-scoped-session-key",
    "reference/post_private-get-mmp-config",
    "reference/post_private-set-mmp-config",
    "reference/post_private-reset-mmp",
    "reference/post_private-set-cancel-on-disconnect",
    "reference/post_private-cancel-all-trigger-orders",
    "reference/post_private-replace-quote",

    # GUIDES
    "reference/submit-order-javascript-copy",
    "reference/submit-order",
    "reference/transfer-collateral",
    "reference/rfq-quoting-and-execution-javascript-copy",
    "reference/rfq-quoting-and-execution",
    "reference/open-orders-margin",
    "reference/liquidation-api",

    # WEBSOCKET API - Public
    "reference/public-build_register_session_key_tx",
    "reference/public-register_session_key",
    "reference/public-deregister_session_key",
    "reference/public-login",
    "reference/public-statistics",
    "reference/public-get_all_currencies",
    "reference/public-get_currency",
    "reference/public-get_instrument",
    "reference/public-get_all_instruments",
    "reference/public-get_instruments",
    "reference/public-validate_invite_code",
    "reference/public-get_points",
    "reference/public-get_ticker",
    "reference/public-get_tickers",
    "reference/public-get_latest_signed_feeds",
    "reference/public-get_option_settlement_prices",
    "reference/public-get_spot_feed_history",
    "reference/public-get_spot_feed_history_candles",
    "reference/public-get_funding_rate_history",
    "reference/public-get_trade_history",
    "reference/public-get_option_settlement_history",
    "reference/public-get_liquidation_history",
    "reference/public-get_interest_rate_history",
    "reference/public-get_transaction",
    "reference/public-get_margin",
    "reference/public-margin_watch",
    "reference/public-get_vault_share",
    "reference/public-get_vault_statistics",
    "reference/public-get_vault_balances",
    "reference/public-get_all_points",
    "reference/public-get_points_leaderboard",
    "reference/public-create_subaccount_debug",
    "reference/public-get_descendant_tree",
    "reference/public-get_tree_roots",
    "reference/public-get_invite_code",
    "reference/public-deposit_debug",
    "reference/public-withdraw_debug",
    "reference/public-get_referral_code",
    "reference/public-create_account_with_secret-1",
    "reference/public-execute_quote_debug",
    "reference/public-all_statistics",
    "reference/public-all_user_statistics",
    "reference/public-change_compliance_status",
    "reference/public-check_subaccount_drift",
    "reference/public-compare_ffi_margin",
    "reference/public-create_account_with_secret",
    "reference/public-get_all_referral_codes",
    "reference/public-get_asset",
    "reference/public-get_assets",
    "reference/public-get_bridge_balances",
    "reference/public-get_detailed_maker_snapshot_history",
    "reference/public-get_live_incidents",
    "reference/public-get_maker_program_scores",
    "reference/public-get_maker_programs",
    "reference/public-get_matching_engine_monitor",
    "reference/public-get_perp_impact_twap",
    "reference/public-send_quote_debug",
    "reference/public-get_referral_performance",
    "reference/public-get_stdrv_snapshots",
    "reference/public-get_time",
    "reference/public-get_vault_assets",
    "reference/public-get_vault_pools",
    "reference/public-get_vault_rates",
    "reference/public-get_wallets_from_session_key",
    "reference/public-ob_internal_view",
    "reference/public-order_quote",
    "reference/public-register_session_key_via_secret",
    "reference/public-set_feed_data",
    "reference/public-user_statistics",

    # WEBSOCKET API - Private
    "reference/private-change_session_key_label",
    "reference/private-create_subaccount",
    "reference/private-get_account",
    "reference/private-change_subaccount_label",
    "reference/private-get_all_portfolios",
    "reference/private-deposit",
    "reference/private-cancel-all",
    "reference/private-cancel",
    "reference/private-get_notifications",
    "reference/private-cancel_by_label",
    "reference/private-get_subaccount",
    "reference/private-cancel-all_trigger_orders",
    "reference/private-get_subaccounts",
    "reference/private-cancel_by_nonce",
    "reference/private-cancel_by_instrument",
    "reference/private-cancel_trigger_order",
    "reference/private-cancel_batch_rfqs",
    "reference/private-cancel_rfq",
    "reference/private-get_order",
    "reference/private-get_open_orders",
    "reference/private-get_orders",
    "reference/private-get_deposit_history",
    "reference/private-cancel_quote",
    "reference/private-order",
    "reference/private-cancel_batch_quotes",
    "reference/private-order_debug",
    "reference/private-get_order_history",
    "reference/private-update_notifications",
    "reference/private-replace",
    "reference/private-execute_quote",
    "reference/private-transfer_erc20",
    "reference/private-withdraw",
    "reference/private-transfer_position",
    "reference/private-get_trade_history",
    "reference/private-transfer_positions",
    "reference/private-create_contact_info",
    "reference/private-get_withdrawal_history",
    "reference/private-delete_contact_info",
    "reference/private-get_rfqs",
    "reference/private-edit_session_key",
    "reference/private-get_collaterals",
    "reference/private-expired_and_cancelled_history",
    "reference/private-get_contact_info",
    "reference/private-get_erc20_transfer_history",
    "reference/private-get_quotes",
    "reference/private-poll_rfqs",
    "reference/private-get_funding_history",
    "reference/private-send_rfq",
    "reference/private-get_interest_history",
    "reference/private-get_margin",
    "reference/private-replace_quote",
    "reference/private-get_liquidation_history",
    "reference/private-send_quote",
    "reference/private-get_liquidator_history",
    "reference/private-poll_quotes",
    "reference/private-get_mmp_config",
    "reference/private-get_option_settlement_history",
    "reference/private-get_positions",
    "reference/private-get_subaccount_value_history",
    "reference/private-rfq_get_best_quote",
    "reference/private-get_trigger_orders",
    "reference/private-liquidate",
    "reference/private-order_quote",
    "reference/private-register_scoped_session_key",
    "reference/private-reset_mmp",
    "reference/private-session_keys",
    "reference/private-set_cancel_on_disconnect",
    "reference/private-set_mmp_config",
    "reference/private-transfer_position_debug",
    "reference/private-trigger_order",
    "reference/private-update_contact_info",

    # WEBSOCKET - Subscriptions
    "reference/subscribe",
    "reference/unsubscribe",

    # CHANNELS - Public
    "reference/orderbook-instrument_name-group-depth",
    "reference/ticker-instrument_name-interval",
    "reference/ticker_slim-instrument_name-interval",
    "reference/spot_feed-currency",
    "reference/trades-instrument_name",
    "reference/trades-instrument_type-currency",
    "reference/trades-instrument_type-currency-tx_status",
    "reference/margin-watch",
    "reference/auctions-watch",
    "reference/trades-instrument_type-currency-1",

    # CHANNELS - Private
    "reference/subaccount_id-quotes-1",
    "reference/subaccount_id-quotes-2",
    "reference/subaccount_id-balances",
    "reference/subaccount_id-best-quotes",
    "reference/subaccount_id-orders",
    "reference/subaccount_id-quotes",
    "reference/subaccount_id-trades-tx_status",
    "reference/subaccount_id-trades",
    "reference/wallet-rfqs",

    # ERRORS
    "reference/error-codes",
]


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def fetch_markdown(url: str, session: requests.Session) -> str:
    """Fetch markdown content by appending .md to the page URL."""
    md_url = url.rstrip("/") + ".md"

    for attempt in range(MAX_RETRIES):
        try:
            resp = session.get(md_url, headers=HEADERS, timeout=30, allow_redirects=True)

            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 60))
                logger.warning(f"Rate-limited, waiting {wait}s …")
                time.sleep(wait)
                continue

            if resp.status_code == 404:
                raise ValueError(f"Page not found: {md_url}")

            resp.raise_for_status()
            content = resp.text

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

    raise RuntimeError(f"Failed to fetch {md_url} after {MAX_RETRIES} attempts")


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
    logger.info("Starting Derive documentation fetch")

    out_dir = Path(__file__).resolve().parent / "derive"
    out_dir.mkdir(exist_ok=True)

    manifest = load_manifest(out_dir)
    new_manifest: Manifest = {"files": {}}

    successful = 0
    failed = 0
    failed_pages: list[str] = []

    with requests.Session() as session:
        total = len(PAGES)
        for i, page_path in enumerate(PAGES, 1):
            url = f"{BASE_URL}/{page_path}"
            rel_path = f"{page_path}.md"
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
