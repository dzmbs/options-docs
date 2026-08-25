> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Underlying Tiers

> Assets on Starbase are classified into three tiers based on liquidity. Tier assignments determine rate limits and multicast channel assignments.

## Overview

Assets are classified into three tiers based on their liquidity. Tier assignments follow [Coinbase International Exchange's perpetual futures tier classification](https://help.coinbase.com/en/international-exchange/perpetual-futures-basics/perpetual-futures-tiers) and determine:

* **Rate limits** — see [API Rate Limits](/starbase/api-rate-limits)
* **Multicast channel assignments** — see [Multicast Channels](/starbase/multicast-channels)

Tier classification is based on the **base currency** of the underlying index. All underlyings sharing the same base currency belong to the same tier — for example, both `BTC_USD` and `BTC_USDC` are Tier 1.

<Note>
  PAXG is classified as **Tier 2** on Starbase, differing from its Tier 3 classification on Coinbase International Exchange.
</Note>

### Programmatic lookup

The `product_group` field on [`public/get_instruments`](/api-reference/market-data/public-get_instruments) reports this classification per instrument (values such as `BTC`, `ETH`, `TIER_2`, and `TIER_3`), so clients can drive gateway and channel routing from the live response instead of hard-coding the tables below. The field is documented on both the standard JSON-RPC and Starbase REST versions of the endpoint.

`product_group` is a per-instrument routing classification used for gateway and multicast-channel assignment. [Rate-limit](/starbase/api-rate-limits#default-rate-limits) overrides use five product tiers (BTC, ETH, Tier 2, Tier 3, and RWA + Pre-IPO). Within a product tier, options and futures share the same rate-limit buckets.

## Tier 1

The most liquid assets. Tier 1 instruments have dedicated multicast channels and the highest allocated rate limits.

| Underlying |
| ---------- |
| BTC\_USD   |
| BTC\_USDC  |
| ETH\_USD   |
| ETH\_USDC  |

## Tier 2

Established assets with moderate liquidity. All altcoin options are Tier 2 regardless of the underlying's tier.

| Underlying |
| ---------- |
| ADA\_USDC  |
| AVAX\_USDC |
| BCH\_USDC  |
| BNB\_USDC  |
| DOGE\_USDC |
| DOT\_USDC  |
| HYPE\_USDC |
| LINK\_USDC |
| LTC\_USDC  |
| NEAR\_USDC |
| PAXG\_USDC |
| SOL\_USDC  |
| TRX\_USDC  |
| UNI\_USDC  |
| XRP\_USDC  |

## Tier 3

Lower-liquidity assets.

| Underlying    |
| ------------- |
| ALGO\_USDC    |
| BTCDVOL\_USDC |
| TRUMP\_USDC   |

## Tier Change Policy

Tier assignments determine which multicast channel an instrument belongs to, so changing a tier has operational consequences for trading clients. To give clients time to adjust:

* Tier changes are made **only during planned deployments**.
* Affected clients receive **at least one week's prior notice** before any tier change takes effect.


## Related topics

- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Starbase API Rate Limits](/starbase/api-rate-limits.md)
- [public/get_instrument](/api-reference/market-data/public-get_instrument.md)
- [public/get_instruments](/api-reference/market-data/public-get_instruments.md)
- [Liquidity Support Program (LSP) API Guide](/articles/lsp-api-guide.md)
