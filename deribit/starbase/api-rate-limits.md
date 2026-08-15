> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starbase API Rate Limits

> Rate limiting rules for the Starbase order entry gateways. Covers per-subaccount key quotas, burst-equals-refill defaults, and gateway throttling behavior.

## Overview

Rate limits are applied per member, per gateway, and per quoting type (order entry or mass quoting). Each gateway enforces its limits independently; violating a rate limit on gateway A does not affect gateway B.

Orders and mass quotes consume tokens from separate buckets, allowing you to manage order and quoting activity independently. Order cancels count toward the order bucket, and mass quote cancels count toward the mass quote bucket.

## Leaky Bucket Algorithm

Starbase uses a leaky bucket algorithm. Each bucket has two parameters:

| Parameter | Description                                |
| :-------- | :----------------------------------------- |
| **B**     | Bucket capacity (maximum number of tokens) |
| **R**     | Leak rate (tokens drained per millisecond) |

Every request adds tokens to the bucket, up to the bucket capacity B. The bucket cannot exceed B — tokens that would push it past capacity are discarded. When the bucket is full, subsequent requests are rejected until enough tokens have drained. The bucket drains at a constant rate of R tokens per millisecond.

This translates to two intuitive limits:

1. **Burst** — The maximum number of messages you can send instantaneously: `B / (tokens per request)`
2. **Steady state** — The maximum sustained throughput: `R / (tokens per request) × 1000` messages per second

### Token Cost per Request

Each request type consumes a fixed number of tokens:

| Request                  | Tokens |
| :----------------------- | :----- |
| `NewOrderRequest`        | 2000   |
| `AmendOrderRequest`      | 2000   |
| `CancelOrderRequest`     | 2000   |
| `MassQuoteRequest`       | 2000   |
| `MassQuoteCancelRequest` | 100    |
| `MassCancelRequest`      | 0      |

<Note>
  Cancel requests are unconditionally accepted and never rejected due to rate limits, even when the bucket is full. `CancelOrderRequest` consumes 2000 tokens from the order bucket — the same cost as a new order. `MassQuoteCancelRequest` consumes 100 tokens from the mass quote bucket — 1/20th the cost of a `MassQuoteRequest`. This reflects the fact that mass quote rate limits are lower than order limits because one mass quote can be equivalent to roughly 20 orders. `MassCancelRequest` (mass order cancel) consumes no tokens. Amends consume from the same order bucket as new orders.
</Note>

### Mass Quote Cancels

In mass quotes, quotes are cancelled by setting their quantity to zero (`bidQty = 0` or `askQty = 0`). A `MassQuoteRequest` where **all** quantities are zero is treated as a cancel: it adds **100 tokens** (1/20th of a normal `MassQuoteRequest`) to the mass quote bucket but is **never rejected due to rate limits**, even when the bucket is full. Token addition is capped at the bucket capacity B — a cancel-only mass quote cannot push the bucket past full. The same 100-token cost applies to a dedicated `MassQuoteCancelRequest`.

A `MassQuoteRequest` that contains any non-zero quantity is subject to normal rate limiting and will be rejected if the bucket is full.

## Default Rate Limits

The table below shows the default rate limits. These defaults apply to all members unless overridden. See [Underlying Tiers](/starbase/underlying-tiers) for the full tier classification.

<Warning>
  **Default limits are a baseline, not a ceiling.** Per-member overrides are common — any firm that represents a large part of the market will typically receive higher limits than the defaults. Do not assume the defaults apply to your firm, regardless of size; confirm your actual allocation with your Account Manager before sizing infrastructure or strategies around these numbers.
</Warning>

All five product tiers share the same defaults:

|                         | Orders | Mass Quotes |
| :---------------------- | :----- | :---------- |
| **R** (tokens/ms)       | 100    | 20          |
| **B** (max tokens)      | 100k   | 20k         |
| **Burst** (messages)    | 50     | 10          |
| **Steady** (messages/s) | 50     | 10          |

By default, the burst rate and the steady-state refill rate are identical. Custom per-member overrides can decouple the two — for example, a Tier 2 override may allow a burst of 150 messages with a steady refill of only 50 messages/s (see the example override below).

<Info>
  Mass quotes have separate, lower rate limits than orders. Option market makers should use mass quotes for quoting—mass quotes are lighter on the system and are allocated accordingly. Within a product tier, options and futures share the same rate-limit buckets; there are no separate options vs futures allocations. High order rate-limit overrides are generally not granted for option-quoting strategies. For strategies quoting perpetuals, dated futures, and future spreads, higher order or mass quote rate limits can be granted based on the preference of the market maker.
</Info>

### Per-Member Overrides

Rate limits can be increased on a per-member basis at the discretion of Deribit, based on current or expected contribution to liquidity. In practice, firms that constitute a large part of the market receive overrides above the defaults. Overrides are configured per product tier and quoting type independently.

The following tables illustrate an example override:

**Bucket parameters** — R in tokens/ms, B in max tokens

| Product Tier  | Orders R | Orders B | MQ R | MQ B |
| :------------ | :------- | :------- | :--- | :--- |
| BTC           | 400      | 400k     | 200  | 200k |
| ETH           | 400      | 400k     | 200  | 200k |
| Tier 2        | 100      | 300k     | 40   | 300k |
| Tier 3        | 100      | 100k     | 20   | 20k  |
| RWA + Pre-IPO | 100      | 100k     | 20   | 20k  |

**Rate limits** — burst in messages, steady in messages/s

| Product Tier  | Orders Burst | Orders Steady | MQ Burst | MQ Steady |
| :------------ | :----------- | :------------ | :------- | :-------- |
| BTC           | 200          | 200           | 100      | 100       |
| ETH           | 200          | 200           | 100      | 100       |
| Tier 2        | 150          | 50            | 150      | 20        |
| Tier 3        | 50           | 50            | 10       | 10        |
| RWA + Pre-IPO | 50           | 50            | 10       | 10        |

Rate limits are assigned based on the technical needs of the strategy. In practice, the majority of Starbase's total capacity is allocated to market makers who provide continuous two-way liquidity across many instruments. The spread of the instruments quoted influences the allocation: quoting a perpetual future at a bid-ask spread of less than 1 basis point will receive a much larger rate limit allocation than a dated future trading at a spread of 10 basis points.

## Rate Limit Violations

When a bucket is full, new orders, amends, and mass quotes containing non-zero quantities are rejected. The reject response indicates the rate limit was exceeded. Cancel requests (`CancelOrderRequest`, `MassQuoteCancelRequest`, `MassCancelRequest`, and `MassQuoteRequest` consisting entirely of zero quantities) are never rejected due to rate limits, though they do consume tokens from their respective buckets as described above.

<Note>
  Rate limit violations are scoped to a single gateway. Exceeding a rate limit on gateway A will not cause requests on gateway B to be rejected.
</Note>

## Gateway Redundancy

Each gateway pair consists of two independent gateways (A and B). Both gateways enforce identical and independent rate limits. This design encourages clients to load balance across both gateways without requiring the gateways to synchronize rate limit state.

## Review Schedule

Rate limit allocations are reviewed periodically. The contribution of trading members is assessed to ensure their performance aligns with allocated rate limits. Rate limits are not adjusted automatically and only change with prior notice.

### Change notifications

* Changes to default limits, token costs, or rate-limit behavior are recorded in the [Starbase Changelog](/changelogs/starbase).
* Member-specific allocation changes are communicated to the affected member before they take effect. Confirm your production allocation with your Account Manager rather than assuming that the defaults on this page apply.
* Changes to underlying tiers follow the separate [Tier Change Policy](/starbase/underlying-tiers#tier-change-policy).

Review the changelog and the upcoming documentation version before deploying a new schema or changing production capacity assumptions.

## Other Limits

### API Key Limits

Each subaccount can have up to **8 Starbase API keys** by default. This limit can be increased at the discretion of Deribit. Please reach out to Support if this limit is too low for your activities.

Each API key can hold exactly **one session per gateway** (see [Gateway Connectivity](/starbase/gateway-connectivity#api-keys)) — with 4 gateway pairs, one key can hold up to 8 simultaneous connections. Reconnecting the same key to the same gateway terminates the existing session. There is no separate cap on the number of simultaneous clients/sessions beyond the API key limit above — each additional key can open its own set of gateway connections.

### REST Gateway Limits

The rate limits described above are applied per member and per gateway, not per IP address. Starbase REST endpoints are rate-limited **per portfolio, per endpoint** — for example, `get_open_orders` is capped at **1 request per minute per portfolio**, and exceeding the limit returns HTTP 429. There is no limit on the number of IP addresses a member can whitelist.

### Open Order Limits

The number of orders and quotes active at any time is limited per member. The default is 2,000 and can be increased at the discretion of Deribit. Please reach out to Support if this limit is too low for your activities.

### Pending Amend Limits

Separate from gateway rate limits, each order can have at most **4 unacknowledged amend (replace) requests** in flight at once — **1 for OCO / reduce-only orders**. Once the cap is reached, further amends on that order are rejected with `TOO_MANY_PENDING_REPLACES` until a pending amend is acknowledged. This cap applies per order rather than per connection and is independent of the gateway rate limit buckets. See [Amending an Order](/starbase/amending-order#pending-amend-limit).


## Related topics

- [Order Management](/articles/order-management-best-practices.md)
- [Rate Limits](/articles/rate-limits.md)
- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Multicast Retransmit Gateway](/starbase/retransmit-gateway.md)
- [Infrastructure, Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
