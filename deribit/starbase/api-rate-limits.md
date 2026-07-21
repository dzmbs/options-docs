> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Rate Limits

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

All five product groups share the same defaults:

|                         | Orders | Mass Quotes |
| :---------------------- | :----- | :---------- |
| **R** (tokens/ms)       | 100    | 20          |
| **B** (max tokens)      | 100k   | 20k         |
| **Burst** (messages)    | 50     | 10          |
| **Steady** (messages/s) | 50     | 10          |

<Info>
  Mass quotes have separate, lower rate limits than orders. Option market makers should use mass quotes for quoting—mass quotes are lighter on the system and are allocated accordingly. High order rate limits will **not** be given out for quoting options. For quoting perpetuals, dated futures, and future spreads, higher order or mass quote rate limits can be granted based on the preference of the market maker.
</Info>

### Per-Member Overrides

Rate limits can be increased on a per-member basis at the discretion of Deribit, based on current or expected contribution to liquidity. Overrides are configured per product group and quoting type independently.

The following tables illustrate an example override:

**Bucket parameters** — R in tokens/ms, B in max tokens

| Product Group   | Orders R | Orders B | MQ R | MQ B |
| :-------------- | :------- | :------- | :--- | :--- |
| BTC             | 1k       | 1m       | 1k   | 1m   |
| ETH             | 500      | 500k     | 300k | 500k |
| Altcoin options | 100      | 300k     | 40   | 300k |
| Other crypto    | 100      | 100k     | 20   | 20k  |
| RWA             | 100      | 100k     | 20   | 20k  |

**Rate limits** — burst in messages, steady in messages/s

| Product Group   | Orders Burst | Orders Steady | MQ Burst | MQ Steady |
| :-------------- | :----------- | :------------ | :------- | :-------- |
| BTC             | 500          | 500           | 500      | 500       |
| ETH             | 250          | 250           | 250      | 150       |
| Altcoin options | 150          | 50            | 150      | 20        |
| Other crypto    | 50           | 50            | 10       | 10        |
| RWA             | 50           | 50            | 10       | 10        |

Rate limits are assigned based on the technical needs of the strategy. In practice, the majority of Starbase's total capacity is allocated to market makers who provide continuous two-way liquidity across many instruments. The spread of the instruments quoted influences the allocation: quoting a perpetual future at a bid-ask spread of less than 1 basis point will receive a much larger rate limit allocation than a dated future trading at a spread of 10 basis points.

## Rate Limit Violations

When a bucket is full, new orders, amends, and mass quotes containing non-zero quantities are rejected. The reject response indicates the rate limit was exceeded. Cancel requests (`CancelOrderRequest`, `MassQuoteCancelRequest`, `MassCancelRequest`, and `MassQuoteRequest` consisting entirely of zero quantities) are never rejected due to rate limits, though they do consume tokens from their respective buckets as described above.

<Note>
  Rate limit violations are scoped to a single gateway. Exceeding a rate limit on gateway A will not cause requests on gateway B to be rejected.
</Note>

## Gateway Redundancy

Each gateway consists of two independent gateways (A and B). Both gateways enforce identical and independent rate limits. This design encourages clients to load balance across both gateways without requiring the gateways to synchronize rate limit state.

## Review Schedule

Rate limit allocations are reviewed periodically. The contribution of trading members is assessed to ensure their performance aligns with allocated rate limits. Rate limits are not adjusted automatically and only change with prior notice.

## Other Limits

### API Key Limits

Each member has a default limit of 8 API keys, allowing 8 connections per gateway. This limit can be increased at the discretion of Deribit. Please reach out to Support if this limit is too low for your activities.

Each API key can hold exactly **one session per gateway** (see [Gateway Connectivity](/starbase/gateway-connectivity#api-keys)). There is no separate cap on the number of simultaneous clients/sessions beyond the API key limit above — each additional key can open its own set of gateway connections.

### IP-Based Limits

The rate limits described above are applied per member and per gateway, not per IP address. The only IP-based limit is on the REST `get_open_orders` endpoint, which is capped at **1 request per minute per IP**. There is no limit on the number of IP addresses a member can whitelist.

### Open Order Limits

The number of orders and quotes active at any time is limited per member. The default is 2,000 and can be increased at the discretion of Deribit. Please reach out to Support if this limit is too low for your activities.
