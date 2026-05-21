# Options Docs

Local mirror of API documentation from major options/derivatives exchanges. Each exchange has a fetch script and its own directory of markdown docs.

## Exchanges

### Binance (`binance/`)
Options trading API from https://developers.binance.com/docs/derivatives/options-trading/general-info

- `market-data/` — Market data endpoints (ticker, orderbook, kline, open interest, mark price)
- `account/` — Account info, funding flow, transfers
- `trade/` — Order placement, cancellation, position info, trade history
- `websocket-market-streams/` — Public WS streams (depth, ticker, trades, kline)
- `user-data-streams/` — Private WS streams (order updates, balance, greeks)
- `market-maker-endpoints/` — MMP config, auto-cancel
- `market-maker-block-trade/` — Block trade RFQ endpoints

### Bybit (`bybit/`)
Options-relevant subset of Bybit v5 API, sourced from https://github.com/bybit-exchange/docs

- Top-level (`intro.mdx`, `enum.mdx`, `error.mdx`, `guide.mdx`) — General reference
- `market/` — Instruments, orderbook, tickers, trades, IV, delivery prices
- `order/` — Place/amend/cancel orders, batch operations, DCP
- `position/` — Position info, move positions
- `account/` — Wallet, fee rates, greeks, MMP, margin mode
- `websocket/` — Public (orderbook, ticker, trades) and private (orders, execution, greeks) streams
- `rfq/` — Block trading / RFQ system (entire section, options-specific)
- `rate-limit/`, `pre-upgrade/`, `asset/`

### Deribit (`deribit/`)
Full API reference from https://docs.deribit.com (options-first exchange, all docs relevant)

- `api-reference/` — JSON-RPC methods organized by category:
  - `account-management/` — Positions, account summary, subaccounts, API keys
  - `authentication/` — OAuth, token exchange
  - `block-rfq/` — Block RFQ create/quote/accept
  - `block-trade/` — Block trade verify/execute/approve
  - `combo-books/` — Combo instruments
  - `market-data/` — Orderbook, ticker, trades, volatility, settlements, instruments
  - `trading/` — Buy/sell, cancel, MMP, mass quote, order history
  - `wallet/` — Deposits, withdrawals, transfers
  - `session-management/`, `subscription-management/`, `supporting/`
- `instrument-specifications/` — Instrument spec sheets from support.deribit.com (manually cloned, not in llms.txt)
  - `inverse-options.md` — BTC/ETH inverse (coin-settled) options contract specs
  - `linear-usdc-options.md` — USDC-linear options (BTC, ETH, SOL, AVAX, TRX, XRP) contract specs
- `articles/` — Guides (quickstart, auth, block trading, MMP, rate limits, best practices)
- `fix-api/production/` — FIX protocol docs
- `subscriptions/` — WebSocket subscription channels (market data, orderbook, trades, user)

### Derive (`derive/`)
Full API reference from https://docs.derive.xyz (formerly Lyra, self-custodial options exchange)

- `reference/` — All docs in flat structure:
  - Overview pages (onboarding, JSON-RPC, auth, session keys, fees, naming)
  - `post_public-*` — REST public endpoints (instruments, tickers, settlements, margin)
  - `post_private-*` — REST private endpoints (orders, RFQ, positions, collateral, MMP)
  - `public-*` / `private-*` — WebSocket API endpoints
  - Channel docs (orderbook, ticker, trades, quotes, balances)
  - Guides (submit order, RFQ execution, margin, liquidation)

### OKX (`okx/`)
Full API reference from https://www.okx.com/docs-v5/en/ (single-page Slate docs, split by section)

- `overview/` — Auth, WebSocket, rate limits, account modes
- `trading-account/` — REST + WS for account, positions, leverage, margin, greeks
- `order-book-trading/` — Trade, algo trading, grid, copy trading, market data
- `block-trading/` — Block trade workflow, REST + WS
- `spread-trading/` — Spread instruments REST + WS
- `public-data/` — Instruments, tickers, funding, mark price, open interest
- `trading-statistics/` — Volume, margin ratio, taker flow
- `funding-account/`, `sub-account/`, `financial-product/`
- `error-code/` — REST and WS error codes

## Source tracking

Each exchange directory contains a manifest JSON file tracking content hashes and source URLs.

## Updating docs

```bash
python3 fetch_binance_options.py   # ~2 min, scrapes HTML
python3 fetch_bybit_options.py     # ~3 sec, git pull
python3 fetch_deribit.py           # ~3 min, .md endpoints via llms.txt
python3 fetch_derive.py            # ~5 min, .md endpoints
python3 fetch_okx.py               # ~1 sec, downloads single HTML page and splits
```
