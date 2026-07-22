> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Speed Bumps

> Speed bumps in Starbase API for options trading, including how aggressive orders are delayed and how market makers are protected from latency arbitrage.

## Overview

Speed Bumps will apply to all instruments, except the top 5 crypto perpetuals by volume (BTC, ETH, SOL, XRP, and HYPE, including BTC/ETH inverse perps). All other instruments (options, dated futures, other perps, and related multi-leg instruments) will have a fixed-length speed bump, configured to be in the 1-10 millisecond range. Any aggressive order or quote, that is, an order or quote that would immediately match, will be made pending by a fixed duration before being entered into the order book. No other member except the owner of the order or quote is informed that this order or quote is pending. Pending orders and quotes are stored in a FIFO queue. Any jitter on speed bump timing will not cause pending orders or quotes to overtake each other.

## Purpose

In the presence of a speed bump, any liquidity providing member has a fixed period of time to detect if their orders or quotes are stale due to newly available information and to send in cancellations of those orders or quotes. In other words, latency arbitrage that prices in information on sub-millisecond timescales is avoided. Market makers can tighten their bid-ask spreads as a result.

As Deribit's market will go from a sub-second latency exchange to a sub-millisecond exchange, we have deemed it necessary to protect our option market makers with a speed bump to make sure our liquidity can transition and deepen.

## How Speed Bumps Work

New orders and quotes will be speed bumped if they aggress. Cancellations will never be speed bumped. For amendments, see the table below:

|                               | **Resting**                                   | **Pending**                                   |
| ----------------------------- | --------------------------------------------- | --------------------------------------------- |
| **Order amended to aggress**  | Removed from book and made pending            | Made pending for speed bump duration again    |
| **Order amended to rest**     | Immediately amended                           | Immediately added to book                     |
| **Quote replaced to aggress** | Old quote removed and new quote made pending  | Old quote removed and new quote made pending  |
| **Quote replaced to rest**    | Old quote removed and new quote added to book | Old quote removed and new quote added to book |

## Mass Quotes

Quotes can only be entered via `MassQuoteRequest`. Each quote in such a batch would be speed bumped individually, per side. This means that one side of the quote can immediately be added to the book, while the other side is pending.

## Cancelling Pending Orders

Cancelling a speed-bumped order **converts it to IOC** rather than removing it immediately. When the speed bump period expires, the order enters the book with an IOC time-in-force and attempts to fill against available liquidity. Any unfilled remainder is cancelled automatically.

The following triggers all produce this IOC conversion:

* Single cancel (`CancelOrderRequest`) and mass cancels (`MassCancelRequest`, `MassQuoteCancelRequest`)
* Market Maker Protection (MMP) trigger
* Cancel on Disconnect (CoD)
* User-initiated portfolio lock

### Message flow

The exchange responds to the cancel immediately with a `CancelOrderReject` carrying reason `convertedToIOC`. The order remains in the queue with `orderState = 4` (queued).

Once the speed bump elapses:

* **Order still matches**: an `OrderPlaced` message is sent with any fills, followed by a cancellation of the unfilled remainder.
* **Order no longer matches** (opposing liquidity has since moved): a standard cancel confirmation is sent.

If the order is already IOC — either submitted with IOC time-in-force or already converted by a prior cancel — a subsequent cancel request is rejected normally.

### Cancel arriving before the order

If a cancel reaches the matching engine before the order it targets (for example, when the order is still awaiting its risk check in the pre-trade risk (PTR) layer), the order is also treated as **IOC** upon release, matching the behavior above.

## Additional Behavior

**Applies to all API interfaces**: The speed bump applies regardless of which gateway or protocol is used. Orders and quotes submitted via the SBE gateway, REST API, or FIX gateway are all subject to the same speed bump.

**Full duration always runs**: The speed bump duration is always served in full based on market conditions at the time of submission. If the opposing liquidity that triggered the speed bump is cancelled before the bumped order is released, the order still completes its full bump period before entering the book. The matching engine does not re-evaluate pending orders when the order book changes.

**Event-driven release**: The speed bump is not a precise hardware timer. Pending orders are checked for release on every incoming message. In practice this means the delay is very close to the configured duration, but may be marginally longer during quiet periods. This has no effect on execution outcomes — any message that would allow the order to release would itself have triggered the evaluation.

## Self Match Prevention and Speed Bumps

When a self-match is detected on a taker order that is currently speed-bumped and was submitted via the SBE gateway, the SMP mode is overridden to `CANCEL_MAKER` regardless of the value in the request. Orders submitted via the WebSocket API may use `CANCEL_TAKER` regardless of speed-bump state.

See [Self Match Prevention](/starbase/smp) for details.

## Post-Only Attributes

To guarantee that trading members aiming to provide passive liquidity are not encumbered by the speed bump, Starbase has post-only-reject and post-only-amend order and quote attributes. These attributes guarantee an avoidance of the speed bump.

## Message Flow During Speed Bump

### SBE Gateway

When a new order or quote aggresses and is speed bumped, the gateway immediately acknowledges the request with a queued status. A follow-up unsolicited message is sent once the speed bump period expires and the order or quote is entered into the book.

| Event                         | Immediate response                                                          | Follow-up unsolicited message |
| ----------------------------- | --------------------------------------------------------------------------- | ----------------------------- |
| New order speed bumped        | `NewOrderResponse (200)` with `orderState = 4` (queued)                     | `OrderPlaced`                 |
| Amend causes order to aggress | `AmendOrderResponse (210)` with `orderState = 4` (queued)                   | `OrderPlaced`                 |
| Quote side speed bumped       | `MassQuoteResponse (230)` with `quoteStatus = 8` (Queued) per affected side | `MassQuoteOrdersPlaced`       |

`OrderPlaced` includes a fills repeating group (`numberOfFills > 0`) when the order matches immediately upon book entry. See [Unsolicited Events](/starbase/unsolicited-events) for the full message specifications.

### FIX Gateway

For speed bumped orders, the FIX gateway sends an `ExecutionReport (8)` for every state transition, including the queued state.

| Event                       | First ExecutionReport (`OrdStatus`) | Second ExecutionReport (`OrdStatus`)           |
| --------------------------- | ----------------------------------- | ---------------------------------------------- |
| New order speed bumped      | `A` (Pending New)                   | `0` (New) upon placement, or `1`/`2` if filled |
| Cancel/Replace speed bumped | `E` (Pending Replace)               | `0` (New) upon placement, or `1`/`2` if filled |

See [Execution Reports](/fix-api/production/execution-reports) for the full field specifications including the `OrdStatus` values.


## Related topics

- [Market Maker Protection (MMP)](/starbase/mmp.md)
- [Starbase API Changelog](/changelogs/starbase.md)
- [Self Match Prevention (SMP)](/starbase/smp.md)
- [Mass Cancel](/starbase/mass-cancel.md)
- [Cancel on Disconnect](/starbase/cancel-on-disconnect.md)
