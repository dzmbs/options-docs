> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Options Data Collection

> Collect Deribit options market data efficiently — order books, ticker greeks, mark prices, implied volatility, combos, trades, and settlement data.

This guide is for anyone building a market data pipeline against Deribit options —
quants backfilling historical IV surfaces, market makers streaming live order books,
or risk teams tracking greeks and mark prices across an option chain. It focuses on
what's specific to **options**: which channel or method covers greeks, IV, combos,
and settlement, and how option instruments behave differently from futures and
perpetuals when collecting data. For general WebSocket/REST tradeoffs, subscription
patterns, and connection handling that apply across all instrument kinds, see the
articles linked throughout this guide.

<Info>
  This guide assumes familiarity with the general data-collection patterns covered in
  [Market Data Collection - Best Practices](/articles/market-data-collection-best-practices)
  and [Notifications](/articles/notifications). Read those first if you haven't already.
</Info>

<Note>
  All examples use `BTC` options. The same patterns apply to `ETH` and any other
  currency with a listed options market — swap the `currency` / `instrument_name`
  parameter and (for `book.{instrument_name}.{group}.{depth}.{interval}`) the
  allowed `group` values.
</Note>

## Discover and track the option chain

Don't rebuild the instrument list from scratch on every run:

1. On startup, call [`public/get_instruments`](/api-reference/market-data/public-get_instruments)
   with `currency=BTC` and `kind=option` once to seed your local instrument set.
2. From then on, track changes via the
   [`instrument.creation.{kind}.{currency}`](/subscriptions/market-data/instrumentcreationkindcurrency)
   and [`instrument.state.{kind}.{currency}`](/subscriptions/market-data/instrumentstatekindcurrency)
   channels instead of re-polling — see [Market Data Collection - Best Practices](/articles/market-data-collection-best-practices#instrument-lifecycle-feed)
   for how the lifecycle states work.

<Warning>
  `public/get_instruments` has a **distinct, much lower rate limit** than other
  market-data endpoints (see [Rate Limits](/articles/rate-limits) for the full table).
  Polling it on a timer to detect new expiries or check `is_active` will exhaust your
  budget quickly — use the `instrument.state` / `instrument.creation` channels for that
  instead, and only call `get_instruments` again when you need a fresh full listing
  (e.g. on reconnect after an extended outage).
</Warning>

Each option instrument also carries an `expiration_timestamp`. Precompute expiries
locally from the seeded instrument list rather than deriving them by parsing
instrument names — the `option_type` (`call`/`put`) and `strike` fields are also
provided directly on each instrument record.

## Order books

Two channels cover order book depth, with a real bandwidth/completeness tradeoff:

| Channel                                                                                                               | Depth                                          | Use when                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [`book.{instrument_name}.{interval}`](/subscriptions/orderbook/bookinstrument_nameinterval)                           | Full book, all price levels                    | You need the complete book (e.g. reconstructing liquidity at any level, feeding a local matching simulation) |
| [`book.{instrument_name}.{group}.{depth}.{interval}`](/subscriptions/orderbook/bookinstrument_namegroupdepthinterval) | Grouped/rounded, capped depth (1/10/20 levels) | You only need top-of-book or a coarse depth view across many instruments — much lower message volume         |

For a full option chain (dozens to hundreds of instruments per expiry), the grouped
channel is usually the right default — subscribing to full-depth raw books on every
strike/expiry combination multiplies message volume unnecessarily, and the
[narrow-vs-wide subscription tradeoffs](/articles/market-data-collection-best-practices#subscribe-only-to-what-you-need-narrow-vs-wide-subscriptions)
apply just as much across strikes as they do across currencies.

<Note>
  **Amount units differ for options.** On both book channels, `amount` for options is
  denominated in the underlying cryptocurrency (BTC or ETH contracts), not USD as it
  is for perpetuals/futures. Normalize this at ingestion time if your storage schema
  assumes USD-denominated size.
</Note>

For how to maintain book state correctly across snapshots, incremental updates, and
`change_id`/`prev_change_id` gap detection, see
[Notifications - Order Book Notifications](/articles/notifications#order-book-notifications).
The same mechanics apply to option order books; option instrument names just look
like `BTC-27JUL26-70000-C` instead of `BTC-PERPETUAL`. As with other instruments, the
`raw` interval is only available on authenticated connections — use `100ms` or
`agg2` on public connections.

## Ticker, greeks, and implied volatility

[`ticker.{instrument_name}.{interval}`](/subscriptions/market-data/tickerinstrument_nameinterval)
streams the full ticker payload per instrument — including `mark_price`, `mark_iv`,
`bid_iv`, `ask_iv`, and the full `greeks` object (`delta`, `gamma`, `theta`, `vega`,
`rho`) for options. For a chain with many strikes, prefer
[`incremental_ticker.{instrument_name}`](/subscriptions/market-data/incremental_tickerinstrument_name)
where available — it only pushes fields that changed since the last update,
reducing bandwidth versus the full-payload channel when you're tracking many
instruments at once.

`incremental_ticker` is capped at one update per second per instrument, so if you
need sub-second ticker precision on a small number of instruments, use the
full `ticker.{instrument_name}.{interval}` channel instead.

If all you need is the current spread — best bid/ask price and size, no greeks,
no full book — [`quote.{instrument_name}`](/subscriptions/market-data/quoteinstrument_name)
is lighter than either ticker channel and avoids the cost of tracking book state
entirely.

For a **whole-chain** view of mark prices and IV without subscribing to every
instrument individually, use
[`markprice.options.{index_name}`](/subscriptions/market-data/markpriceoptionsindex_name) —
it streams mark price and mark IV updates for every option under that index in one
channel. This is the most efficient way to track valuation across an entire option
chain in real time (portfolio marking, P\&L, risk dashboards).

If you only need a periodic full-chain snapshot rather than a continuous stream —
for example to validate your WebSocket-derived state, or to seed a new pipeline —
[`public/get_book_summary_by_currency`](/api-reference/market-data/public-get_book_summary_by_currency)
with `kind=option` returns mark price, IV, volume, and open interest for every
option in one REST call. Use it for point-in-time reconciliation, not as a
substitute for the streaming channels.

## Historical and realized/implied volatility

* [`public/get_historical_volatility`](/api-reference/market-data/public-get_historical_volatility) —
  realized volatility time series for a currency, useful as a model input or a
  sanity check against streamed `mark_iv`.
* [`deribit_volatility_index.{index_name}`](/subscriptions/market-data/deribit_volatility_indexindex_name)
  (WebSocket) and
  [`public/get_volatility_index_data`](/api-reference/market-data/public-get_volatility_index_data)
  (REST, candle-formatted) — Deribit's DVOL index, an expectation of forward
  volatility analogous to VIX. Use the WebSocket channel for live DVOL, the REST
  method for backfilling DVOL history.

## Trades

| Need                                                            | Method / Channel                                                                                                                                                                                                                         |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Live trade prints for one instrument                            | [`trades.{instrument_name}.{interval}`](/subscriptions/trades/tradesinstrument_nameinterval)                                                                                                                                             |
| Live trade prints across an entire chain (e.g. all BTC options) | [`trades.{kind}.{currency}.{interval}`](/subscriptions/trades/tradeskindcurrencyinterval)                                                                                                                                                |
| Historical backfill by time range                               | [`public/get_last_trades_by_instrument_and_time`](/api-reference/market-data/public-get_last_trades_by_instrument_and_time)                                                                                                              |
| Historical backfill by trade sequence range                     | [`public/get_last_trades_by_instrument`](/api-reference/market-data/public-get_last_trades_by_instrument) with `start_seq`/`end_seq`                                                                                                     |
| OHLC candles for charting                                       | [`chart.trades.{instrument_name}.{resolution}`](/subscriptions/market-data/charttradesinstrument_nameresolution) (live) / [`public/get_tradingview_chart_data`](/api-reference/market-data/public-get_tradingview_chart_data) (backfill) |

As with order books, prefer the per-currency+kind channel
(`trades.option.BTC.raw`, for example) over one subscription per instrument when
you're covering a full chain — see
[Subscription Strategies and Filters](/articles/market-data-collection-best-practices#subscription-strategies-and-filters)
for the general tradeoff. It scales far better as new strikes and expiries are
listed, since you don't need to manage per-instrument subscriptions as the chain
changes.

For REST backfill, `count` is capped at **1000** per call on both trade-history
methods — see [Pagination patterns at a glance](#pagination-patterns-at-a-glance)
below for how to page through a full history without gaps or duplicates.
Sequence-based pagination (`start_seq`/`end_seq`) is preferable when you need a
gapless history, since it isn't affected by multiple trades sharing a timestamp.

## Multi-leg strategies (combos)

Combo (multi-leg option spread) books are a separate object from individual option
instruments:

* [`public/get_combo_ids`](/api-reference/combo-books/public-get_combo_ids) —
  list combo IDs for a currency (optionally filtered by state).
* [`public/get_combos`](/api-reference/combo-books/public-get_combos) — active
  combos with full leg structure for a currency.
* [`public/get_combo_details`](/api-reference/combo-books/public-get_combo_details) —
  full detail for one combo ID.
* [`user.combo_trades.{instrument_name}.{interval}`](/subscriptions/user/usercombo_tradesinstrument_nameinterval) /
  [`user.combo_trades.{kind}.{currency}.{interval}`](/subscriptions/user/usercombo_tradeskindcurrencyinterval) —
  trade prints for combo instruments (requires the private/authenticated
  connection scope, since these are user-trade channels).

If your pipeline needs to track combo books alongside single-leg instruments,
treat combo IDs as their own instrument namespace — they aren't returned by
`public/get_instruments` with `kind=option`.

## Settlement and expiration data

* [`public/get_delivery_prices`](/api-reference/market-data/public-get_delivery_prices) —
  historical settlement/delivery prices for an index, paginated via
  `offset`/`count` (max 1000 per page). Use this for backtesting how options
  actually settled.
* [`estimated_expiration_price.{index_name}`](/subscriptions/market-data/estimated_expiration_priceindex_name)
  (WebSocket) — live estimate of the price that will be used at the next
  settlement, useful for monitoring expected settlement levels intraday as
  expiry approaches.

## Pagination patterns at a glance

Different endpoints paginate differently — matching the right pattern to the right
endpoint avoids gaps or duplicate records in backfilled data:

| Pattern                             | Endpoints                                                             | Notes                                                                                        |
| ----------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `offset` + `count`                  | `get_delivery_prices`                                                 | Simple page cursor; fine for data that doesn't mutate between pages                          |
| `start_seq` / `end_seq`             | `get_last_trades_by_instrument`                                       | Sequence-based — safe when several trades share a timestamp                                  |
| `start_timestamp` / `end_timestamp` | `get_last_trades_by_instrument_and_time`, `get_volatility_index_data` | Window-based; page by advancing the timestamp boundary                                       |
| `continuation` token                | order/Block RFQ history endpoints                                     | Opaque cursor returned by the previous call; keep requesting until omitted from the response |

`count` parameters across these methods cap at **1000** per request — always loop
until a page returns fewer than the requested count (or an empty continuation)
rather than assuming one call is exhaustive.

## Summary checklist

<CardGroup cols={2}>
  <Card title="Discovery">
    Seed instruments once via `get_instruments` (mind its tight rate limit);
    track changes via `instrument.creation`/`instrument.state` channels, not polling.
  </Card>

  <Card title="Order books">
    Use grouped/depth-limited books for chain-wide views; remember option
    `amount` is denominated in the underlying, not USD.
  </Card>

  <Card title="Valuation">
    Prefer `markprice.options.{index_name}` for chain-wide mark price/IV over
    per-instrument ticker polling.
  </Card>

  <Card title="Trades">
    Subscribe per-currency (`trades.{kind}.{currency}.{interval}`) instead of
    per-instrument when covering a full chain.
  </Card>

  <Card title="Combos & settlement">
    Treat combo IDs as a separate namespace from single-leg options; use
    `get_delivery_prices` and `estimated_expiration_price` for settlement data.
  </Card>

  <Card title="Backfill">
    Paginate historical calls with the right cursor for the endpoint
    (`offset`/`count`, `start_seq`/`end_seq`, or timestamp windows).
  </Card>
</CardGroup>


## Related topics

- [Market Data Collection](/articles/market-data-collection-best-practices.md)
- [private/subscribe](/api-reference/subscription-management/private-subscribe.md)
- [public/subscribe](/api-reference/subscription-management/public-subscribe.md)
- [Reference Data](/starbase/reference-data.md)
- [markprice.options.(index_name) ](/subscriptions/market-data/markpriceoptionsindex_name.md)
