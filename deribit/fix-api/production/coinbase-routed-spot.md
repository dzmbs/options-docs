> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Coinbase-Routed Spot — Production FIX API

> How the Deribit production FIX API behaves for spot instruments matched on Coinbase Exchange: accepted order tags, market data limits, and rejections.

Selected spot instruments are matched on Coinbase Exchange (CBE) instead of the
Deribit matching engine. They trade over the same FIX session as every other
instrument, but order entry accepts a narrower set of tag values and the public
trade tape is not served for them. Derivatives are unaffected, including
derivatives on the same currency pair.

## Identifying routed instruments

Routing is flagged in the instrument metadata returned by the JSON-RPC methods
`public/get_instrument` and `public/get_instruments`, which set
`is_cbe_routed` to `true` (and its alias `is_csr` to `true`) for routed spot
instruments. Both fields are omitted entirely for every other instrument, so
test for presence rather than for a `false` value. Routed spot instruments also
omit `block_trade_commission`, `block_trade_tick_size` and
`block_trade_min_trade_amount`.

## Order entry

These restrictions apply to [`New Order Single`(`D`)](/fix-api/production/new-order-single)
and [`Order Cancel/Replace Request`(`G`)](/fix-api/production/order-cancel-replace).

| Tag  | Name                            | Accepted on routed spot                                                                                                                              |
| ---- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 40   | `OrdType`                       | `1` = Market, `2` = Limit and `4` = Stop Limit only                                                                                                  |
| 59   | `TimeInForce`                   | `1` = Good 'Til Cancelled, `3` = Immediate or Cancel and `4` = Fill or Kill. `0` = Good 'Til Day is rejected on every spot instrument, routed or not |
| 18   | `ExecInst`                      | `6A` only. A bare `6` is rejected with `post_only_not_allowed`, and `E` (reduce only) with `reduce_only_not_allowed`                                 |
| 1138 | `DisplayQty`                    | Not supported. Iceberg orders are rejected with `iceberg_not_allowed`                                                                                |
| 5127 | `DeribitConditionTriggerMethod` | Required on stop limit orders, and must be `2` = trade                                                                                               |

Post-only works differently from native Deribit post-only: the price of a routed
post-only order is never adjusted into the spread, so the order is either placed
unmodified or rejected. That is why `A` ("no cross") must always accompany `6`.

Linked orders (OTO, OCO and OTOCO), block trades and Block RFQ legs are not
available on routed spot instruments.

<Note>
  Fills are asynchronous. The [`Execution Report`(`8`)](/fix-api/production/execution-reports)
  that acknowledges a routed order confirms that Coinbase accepted it, and it
  does not necessarily carry any fills. Track execution through the subsequent
  Execution Reports on the same session.
</Note>

## Market data

Deribit only observes a Coinbase match when one of your own orders was a party
to it, so the public trade tape it could publish for a routed instrument would
be incomplete. Rather than serve partial data, the trade entry type is rejected:

* `MDEntryType`(`269`)=`2` (Trade) is rejected for routed spot instruments in a [`Market Data Request`(`V`)](/fix-api/production/market-data-request), which is answered with a [`Market Data Request Reject`(`Y`)](/fix-api/production/market-data-request-reject). `0` (Bid) and `1` (Offer) requested in the same message are still served.
* [`Market Data Snapshot/Full Refresh`(`W`)](/fix-api/production/market-data-snapshot) and [`Market Data Incremental Refresh`(`X`)](/fix-api/production/market-data-incremental) therefore never carry trade entries for routed spot instruments.

Everything else in the market data set behaves normally. Bid and offer snapshots
and incremental updates are fed from the full Coinbase L2 book, and
[`Security List Request`(`x`)](/fix-api/production/security-list-request) and
[`Security Status Request`(`e`)](/fix-api/production/security-status-request)
are unaffected.

Your own fills are always complete. Both
[Execution Reports](/fix-api/production/execution-reports) and
[`Trade Capture Report`(`AE`)](/fix-api/production/trade-capture-report)
include every trade you were a party to.

For the full public trade tape, query Coinbase Exchange directly through its
[FIX Market Data API](https://docs.cdp.coinbase.com/exchange/fix-api/market-data),
the [`matches` WebSocket channel](https://docs.cdp.coinbase.com/exchange/websocket-feed/channels),
or the [Get product trades](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproducttrades)
and [Get product candles](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductcandles)
REST endpoints.

## Rejections

Rejected orders arrive as an [`Execution Report`(`8`)](/fix-api/production/execution-reports)
with `OrdStatus`(`39`)=`8` and the reason in `Text`(`58`). Rejected market data
requests arrive as a [`Market Data Request Reject`(`Y`)](/fix-api/production/market-data-request-reject).

| Code  | Message                                        | Meaning                                                                                                        |
| ----- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 11030 | `other_reject <reason>`                        | The rejection originated at Coinbase, for example `other_reject price_band` or `other_reject not_enough_funds` |
| 11055 | `post_only_not_allowed`                        | `ExecInst`(`18`)=`6` was sent without `A`                                                                      |
| 11059 | `iceberg_not_allowed`                          | `DisplayQty`(`1138`) was set on a routed spot instrument                                                       |
| 11060 | `not_supported_for_coinbase_routed_spot`       | The requested feature is not available on a routed spot instrument                                             |
| 13922 | `linked_order_type_not_supported_for_csr_spot` | A linked order (OTO, OCO or OTOCO) was submitted for a routed spot instrument                                  |
|       | `reduce_only_not_allowed`                      | `ExecInst`(`18`)=`E` was sent for a routed spot instrument                                                     |

See [Error codes](/articles/errors) for the full list.


## Related topics

- [Deribit Production FIX API Overview](/fix-api/production/overview.md)
- [Market Data Snapshot (W) — Production FIX API](/fix-api/production/market-data-snapshot.md)
- [New Order Single(D) — Production FIX API](/fix-api/production/new-order-single.md)
- [Market Data Incremental Refresh(X) — Production FIX API](/fix-api/production/market-data-incremental.md)
- [Security List(y) — Production FIX API](/fix-api/production/security-list.md)
