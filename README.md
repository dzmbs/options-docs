# Options Docs

[![docs updated](https://img.shields.io/github/last-commit/dzmbs/options-docs/main?label=docs%20updated&color=brightgreen)](https://github.com/dzmbs/options-docs/commits/main)
[![sync](https://img.shields.io/badge/sync-daily%20at%2012%3A00%20CET-orange)](.github/workflows/update-docs.yml)
[![exchanges](https://img.shields.io/badge/exchanges-5-blue)](#whats-in-here)

Community mirror of API documentation from major crypto options/derivatives exchanges, stored as markdown for easy search, diffing, and AI consumption.

## What's in here

| Exchange | Files | Format | Source |
|---|---|---|---|
| **Binance** | 70 | `.md` | [Binance Options API](https://developers.binance.com/docs/derivatives/options-trading/general-info) |
| **Bybit** | 81 | `.mdx` | [bybit-exchange/docs](https://github.com/bybit-exchange/docs) (v5 options subset) |
| **Deribit** | 279 | `.md` | [docs.deribit.com](https://docs.deribit.com) (full API — options-first exchange) |
| **Derive** | 291 | `.md` | [docs.derive.xyz](https://docs.derive.xyz/reference/overview) (formerly Lyra) |
| **OKX** | 65 | `.md` | [OKX API v5](https://www.okx.com/docs-v5/en/) (full API, split from single page) |

## How to use

**Browse directly** — each exchange has its own folder with markdown files organized by topic (market data, trading, websockets, etc.). Open any `.md` file to read endpoint docs with parameters, examples, and response schemas.

**Search across exchanges** — use grep/ripgrep to compare how different exchanges handle the same concept:

```bash
# How does each exchange handle mark price?
rg -l "mark.price" --type md

# Compare order placement across exchanges
rg "place.order|create.order|private.buy|private-order" --type md -l

# Find all MMP (market maker protection) docs
rg -l "mmp|market.maker.protection" -i
```

**Feed to AI** — the repo is structured so you can point Claude, ChatGPT, or Cursor at any exchange folder for context when building trading systems.

## Updating

Each exchange has a standalone Python script (only requires `requests`):

```bash
python3 fetch_binance_options.py   # scrapes HTML → markdown
python3 fetch_bybit_options.py     # git pulls from GitHub repo
python3 fetch_deribit.py           # fetches .md via llms.txt sitemap
python3 fetch_derive.py            # fetches .md from ReadMe.com
python3 fetch_okx.py               # downloads single HTML page, splits by section
```

Scripts are idempotent — they track content hashes and only overwrite files that changed.

A [GitHub Action](.github/workflows/update-docs.yml) runs the same fetch scripts once per day at 12:00 CET and commits any documentation changes.

## Repo structure

```
options-docs/
├── binance/                    # Binance options trading API
│   ├── market-data/            # Ticker, orderbook, kline, OI, mark price
│   ├── trade/                  # Orders, positions, exercise, commissions
│   ├── account/                # Account info, funding, transfers
│   ├── websocket-market-streams/
│   ├── user-data-streams/
│   ├── market-maker-endpoints/
│   └── market-maker-block-trade/
├── bybit/                      # Bybit v5 API (options-relevant subset)
│   ├── market/                 # Instruments, orderbook, tickers, IV
│   ├── order/                  # Place/amend/cancel, batch ops
│   ├── position/               # Positions, move positions
│   ├── account/                # Wallet, fees, greeks, MMP
│   ├── websocket/              # Public + private streams
│   └── rfq/                    # Block trading (options-specific)
├── deribit/                    # Deribit full API (options-first exchange)
│   ├── api-reference/          # All JSON-RPC methods by category
│   ├── articles/               # Guides and best practices
│   ├── fix-api/                # FIX protocol
│   ├── instrument-specifications/ # Contract specs from support.deribit.com
│   └── subscriptions/          # WebSocket channels
├── derive/                     # Derive/Lyra full API
│   └── reference/              # REST, WebSocket, channels, guides
├── okx/                        # OKX full API (split from single page)
│   ├── overview/               # Auth, websocket, rate limits
│   ├── order-book-trading/     # Trade, algo, market data
│   ├── block-trading/          # Block trade workflow
│   ├── trading-account/        # Account, positions, margin
│   └── public-data/            # Instruments, funding, statistics
├── fetch_binance_options.py
├── fetch_bybit_options.py
├── fetch_deribit.py
├── fetch_derive.py
└── fetch_okx.py
```
