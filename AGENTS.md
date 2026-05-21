# Options Docs

Community mirror of API documentation from major options/derivatives exchanges, stored as markdown for search, diffing, and AI coding agents.

## Sources

- Binance Options API: https://developers.binance.com/docs/derivatives/options-trading/general-info
- Bybit v5 docs: https://github.com/bybit-exchange/docs
- Deribit docs: https://docs.deribit.com
- Derive docs: https://docs.derive.xyz
- OKX API v5 docs: https://www.okx.com/docs-v5/en/

## Documentation structure

```
binance/  # Binance options API: market data, account, trade, websockets, market-maker endpoints
bybit/    # Bybit v5 options-relevant API: market, order, position, account, websocket, RFQ
          # block trading

deribit/  # Deribit full API reference, subscriptions, articles, FIX docs, instrument specs
derive/   # Derive/Lyra reference docs: REST, WebSocket, RFQ, margin, positions, collateral
okx/      # OKX v5 docs: overview, trading account, order-book trading, block/spread trading,
          # public data, funding/sub-account sections
```

Each exchange directory includes a manifest JSON file mapping mirrored files to source URLs and content hashes.

## Sync

Documentation is fetched daily by GitHub Actions. To update locally:

```bash
python3 fetch_binance_options.py
python3 fetch_bybit_options.py
python3 fetch_deribit.py
python3 fetch_derive.py
python3 fetch_okx.py
```

The scripts are idempotent and only rewrite files when source content changes.
