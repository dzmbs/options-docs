> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Spot Trading: Deribit and Coinbase-Routed Instruments

> Which Deribit spot instruments are matched on Deribit and which are routed to Coinbase Exchange, and how order entry and market data differ between them.

Deribit spot instruments are matched in one of two places:

* **On the Deribit matching engine**, the same engine that matches derivatives. A small number of spot instruments continue to work this way.
* **On Coinbase Exchange (CBE)**, where Deribit routes the order for matching. Most spot instruments are routed.

Both kinds trade through the same Deribit APIs, with the same authentication, the same sessions and the same instrument names, and both return the same order and trade objects. Routed instruments accept a narrower set of order parameters and do not serve the public trade tape, which is what the rest of this article describes.

Derivatives are never affected, including derivatives on the same currency pair. A routed spot instrument does not change anything about the futures, perpetuals or options quoted in the same currencies.

For the background to the routing change, see [Spot trading routed to Coinbase Exchange](https://support.deribit.com/hc/en-us/articles/38375233938205-18-August-2026) in the Deribit knowledge base.

## Telling the two apart

[`public/get_instrument`](/api-reference/market-data/public-get_instrument) and [`public/get_instruments`](/api-reference/market-data/public-get_instruments) return `is_cbe_routed: true`, and its alias `is_csr: true`, for routed spot instruments:

```json theme={null}
{
  "instrument_name": "USDC_USDT",
  "kind": "spot",
  "is_cbe_routed": true,
  "is_csr": true,
  "...": "..."
}
```

Both fields are omitted entirely for spot instruments matched on Deribit, and for every other instrument, so test for their presence rather than for a `false` value. Routed spot instruments also omit `block_trade_commission`, `block_trade_tick_size` and `block_trade_min_trade_amount`, because block trading is not available on them.

Which pairs are routed is a configuration decision that can change, so read the flag from the instrument metadata instead of maintaining your own list.

The [`instrument.creation.{kind}.{currency}`](/subscriptions/market-data/instrumentcreationkindcurrency) and [`instrument.state.{kind}.{currency}`](/subscriptions/market-data/instrumentstatekindcurrency) notifications carry `is_csr` only; the `is_cbe_routed` alias is added by the two instrument methods above.

On FIX there is no routing flag in the reference data. [`Security List`(`y`)](/fix-api/production/security-list) returns both kinds as ordinary `FXSPOT` entries, so identify routed instruments through the JSON-RPC methods above.

## What applies to every spot instrument

These rules hold for spot regardless of where the instrument is matched, and are differences from derivatives rather than from routing:

* `good_til_day` is rejected. On FIX, `TimeInForce`(`59`)=`0` is rejected.
* `reduce_only` is not supported, and `mmp` is not available. Mass quotes are derivatives-only.
* Spot holdings are balances, not positions: [`private/get_positions`](/api-reference/account-management/private-get_positions) rejects `kind: "spot"`.

## Order entry

### JSON-RPC

The table compares [`private/buy`](/api-reference/trading/private-buy), [`private/sell`](/api-reference/trading/private-sell), [`private/edit`](/api-reference/trading/private-edit) and [`private/edit_by_label`](/api-reference/trading/private-edit_by_label) across the two venues.

| Feature                         | Matched on Deribit                                                                                           | Routed to Coinbase                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| `type`                          | `limit`, `market`, `market_limit`, `stop_limit`, `stop_market`, `take_limit`, `take_market`, `trailing_stop` | `limit`, `market` and `stop_limit` only                                   |
| `time_in_force`, limit orders   | `good_til_cancelled`, `immediate_or_cancel`, `fill_or_kill`                                                  | Same                                                                      |
| `time_in_force`, market orders  | Omit it, or send `good_til_cancelled`                                                                        | Omit it, or send `immediate_or_cancel`                                    |
| `post_only`                     | Supported. The price is adjusted into the spread unless `reject_post_only` is set                            | Supported only with `reject_post_only: true`. The price is never adjusted |
| `display_amount` (iceberg)      | Supported                                                                                                    | Not supported                                                             |
| `trigger` on stop orders        | `last_price`, `mark_price` or `index_price`                                                                  | `last_price` only                                                         |
| Linked orders (OTO, OCO, OTOCO) | Supported                                                                                                    | Not supported                                                             |
| Block trades and Block RFQ legs | Supported                                                                                                    | Not supported                                                             |

Cancelling works the same on both. [`private/cancel`](/api-reference/trading/private-cancel), [`private/cancel_all_by_instrument`](/api-reference/trading/private-cancel_all_by_instrument) and the other cancel methods accept routed spot orders, including untriggered stop-limit orders.

### FIX

The same differences apply to [`New Order Single`(`D`)](/fix-api/production/new-order-single) and [`Order Cancel/Replace Request`(`G`)](/fix-api/production/order-cancel-replace).

| Tag  | Name                            | Matched on Deribit                                                       | Routed to Coinbase                                                                                                   |
| ---- | ------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| 40   | `OrdType`                       | The same set as derivatives, resolved together with `StopPx`(`99`)       | `1` = Market, `2` = Limit and `4` = Stop Limit only                                                                  |
| 59   | `TimeInForce`                   | `1` = Good 'Til Cancelled, `3` = Immediate or Cancel, `4` = Fill or Kill | Same                                                                                                                 |
| 18   | `ExecInst`                      | `6` and `6A` are both accepted                                           | `6A` only. A bare `6` is rejected with `post_only_not_allowed`, and `E` (reduce only) with `reduce_only_not_allowed` |
| 1138 | `DisplayQty`                    | Supported                                                                | Not supported. Iceberg orders are rejected with `iceberg_not_allowed`                                                |
| 5127 | `DeribitConditionTriggerMethod` | `1` = mark price, `2` = trade or `3` = index, required on stop orders    | Required on stop limit orders, and must be `2` = trade                                                               |

### Post-only

On the Deribit matching engine, a post-only order that would match on arrival has its price adjusted by one tick into the spread, unless you set `reject_post_only: true` — `ExecInst`(`18`)=`6A` on FIX — in which case it is rejected instead.

On a routed instrument the price is never adjusted. The order is either placed unmodified or rejected, which is why the reject flag is mandatory there: post-only without it is rejected with `post_only_not_allowed` (11055). An order that would match on arrival is rejected with `post_only_reject` (11054) on both venues.

### Errors and rejections

The errors below are specific to routed instruments. On JSON-RPC they are returned in the response to the request; on FIX, rejected orders arrive as an [`Execution Report`(`8`)](/fix-api/production/execution-reports) with `OrdStatus`(`39`)=`8` and the reason in `Text`(`58`).

| Code  | Message                                        | Cause                                                                                                                          |
| ----- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 11030 | `other_reject <reason>`                        | The rejection originated at Coinbase, for example `other_reject price_band` or `other_reject not_enough_funds`                 |
| 11054 | `post_only_reject`                             | A post-only order would have matched on arrival                                                                                |
| 11055 | `post_only_not_allowed`                        | Post-only was requested without the reject flag                                                                                |
| 11059 | `iceberg_not_allowed`                          | `display_amount`, or `DisplayQty`(`1138`), was set on a routed spot instrument                                                 |
| 11060 | `not_supported_for_coinbase_routed_spot`       | The requested order type, time in force, trigger, block trade or market data call is not available on a routed spot instrument |
| 13922 | `linked_order_type_not_supported_for_csr_spot` | A linked order (OTO, OCO or OTOCO) was submitted for a routed spot instrument                                                  |

Parameters that are unavailable on spot generally, such as `reduce_only` and `good_til_day`, come back as `Invalid params` (-32602) on both venues rather than as one of the codes above. See [Error codes](/articles/errors) for the full list. Code 11060 is also returned under its legacy message `not_supported_for_csr_spot`; treat the two as equivalent.

<Note>
  On routed instruments, fills are asynchronous. `private/buy`, `private/sell`, `private/edit` and `private/edit_by_label` — and, on FIX, the first `Execution Report` for the order — acknowledge the order once Coinbase has accepted it, and do not necessarily carry any fills. Subscribe to [`user.trades.{instrument_name}.{interval}`](/subscriptions/user/usertradesinstrument_nameinterval) and [`user.orders.{instrument_name}.{interval}`](/subscriptions/user/userordersinstrument_nameinterval), or track the subsequent Execution Reports on the FIX session, to follow execution.
</Note>

## Market data

Deribit only observes a match on Coinbase when one of your own orders was a party to it, so the public trade tape it could publish for a routed instrument would be incomplete. Rather than serve partial data, trade-derived methods, channels and message types are rejected for routed instruments. Order book data is unaffected, because Deribit receives the full Coinbase book.

| Data                                                                                               | Matched on Deribit           | Routed to Coinbase                         |
| -------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------ |
| Public trade tape (`public/get_last_trades_*`)                                                     | Served                       | Rejected with 11060                        |
| `trades.*` channels                                                                                | Served                       | Rejected as invalid channels               |
| Candles (`public/get_tradingview_chart_data`, `chart.trades.*`)                                    | Served                       | Rejected                                   |
| Trade entries on FIX, `MDEntryType`(`269`)=`2`                                                     | Served                       | Rejected                                   |
| Order book methods, and the `book.*`, `quote.*` and `ticker.*` channels                            | Served from the Deribit book | Served from the Coinbase book              |
| `stats` in [`public/ticker`](/api-reference/market-data/public-ticker)                             | Full                         | `volume_notional` and `volume_usd` omitted |
| `spot_volume` in [`public/get_trade_volumes`](/api-reference/market-data/public-get_trade_volumes) | Present                      | Omitted                                    |

Your own fills are always complete on both venues: [`private/get_user_trades_by_instrument`](/api-reference/trading/private-get_user_trades_by_instrument), the `user.trades.*` channels, and on FIX both [Execution Reports](/fix-api/production/execution-reports) and [`Trade Capture Report`(`AE`)](/fix-api/production/trade-capture-report), report every trade you were a party to.

### Methods that return an error

For routed instruments these return `not_supported_for_coinbase_routed_spot` (11060):

* [`public/get_last_trades_by_instrument`](/api-reference/market-data/public-get_last_trades_by_instrument)
* [`public/get_last_trades_by_instrument_and_time`](/api-reference/market-data/public-get_last_trades_by_instrument_and_time)
* [`public/get_last_trades_by_currency`](/api-reference/market-data/public-get_last_trades_by_currency) and [`public/get_last_trades_by_currency_and_time`](/api-reference/market-data/public-get_last_trades_by_currency_and_time), when `kind` is `spot` or `any` — `any` is the default when `kind` is omitted, and a currency counts as routed when it is either the base or the quote of a routed pair
* [`public/get_tradingview_chart_data`](/api-reference/market-data/public-get_tradingview_chart_data)

Requesting a derivative `kind` on a currency that happens to have a routed spot pair is unaffected, so `kind: "future"` still returns trades for that currency.

### Subscriptions that are rejected

[`public/subscribe`](/api-reference/subscription-management/public-subscribe) refuses these channels for routed instruments, reporting them as invalid channels rather than as error 11060:

* [`trades.{instrument_name}.{interval}`](/subscriptions/trades/tradesinstrument_nameinterval)
* [`trades.{kind}.{currency}.{interval}`](/subscriptions/trades/tradeskindcurrencyinterval) for `kind` `spot` or `any`
* [`chart.trades.{instrument_name}.{resolution}`](/subscriptions/market-data/charttradesinstrument_nameresolution)

`currency: "any"` is rejected as well whenever any routed spot pair exists, so subscribe per currency, or per instrument, if you need spot trades for instruments matched on Deribit.

### FIX market data

* `MDEntryType`(`269`)=`2` (Trade) is rejected for routed spot instruments in a [`Market Data Request`(`V`)](/fix-api/production/market-data-request), which is answered with a [`Market Data Request Reject`(`Y`)](/fix-api/production/market-data-request-reject). `0` (Bid) and `1` (Offer) requested in the same message are still served.
* [`Market Data Snapshot/Full Refresh`(`W`)](/fix-api/production/market-data-snapshot) and [`Market Data Incremental Refresh`(`X`)](/fix-api/production/market-data-incremental) therefore never carry trade entries for routed spot instruments.

Bid and offer snapshots and incremental updates are fed from the full Coinbase L2 book, and [`Security List Request`(`x`)](/fix-api/production/security-list-request) and [`Security Status Request`(`e`)](/fix-api/production/security-status-request) are unaffected.

### Responses that omit fields

For routed instruments, two responses drop fields instead of returning an error:

* [`public/get_trade_volumes`](/api-reference/market-data/public-get_trade_volumes) omits `spot_volume`, and `spot_volume_7d` and `spot_volume_30d` under `extended`, for any currency that has a routed pair. The futures and options volume fields are unaffected.
* [`public/ticker`](/api-reference/market-data/public-ticker) and the [`ticker.{instrument_name}.{interval}`](/subscriptions/market-data/tickerinstrument_nameinterval) channel omit `volume_notional` and `volume_usd` from `stats`. The base currency `volume` field is still returned.

### Getting the routed data from Coinbase

For the full public trade tape, candles and venue volume of a routed instrument, query Coinbase Exchange directly:

* [Get product trades](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproducttrades)
* [Get product candles](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductcandles)
* [Get all product volume](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductvolume)
* The [`matches` WebSocket channel](https://docs.cdp.coinbase.com/exchange/websocket-feed/channels) and the [FIX Market Data API](https://docs.cdp.coinbase.com/exchange/fix-api/market-data)


## Related topics

- [Deribit Production FIX API Overview](/fix-api/production/overview.md)
- [trades.(kind).(currency).(interval) ](/subscriptions/trades/tradeskindcurrencyinterval.md)
- [public/get_tradingview_chart_data](/api-reference/market-data/public-get_tradingview_chart_data.md)
- [public/get_last_trades_by_currency](/api-reference/market-data/public-get_last_trades_by_currency.md)
- [chart.trades.(instrument_name).(resolution) ](/subscriptions/market-data/charttradesinstrument_nameresolution.md)
