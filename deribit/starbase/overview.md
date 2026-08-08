> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starbase API Overview

> Introduction to Deribit Starbase covering the low-latency binary and FIX API stack, gateway architecture, product scope, and migration from legacy SBE.

Starbase is Deribit's high-performance matching engine designed for institutional trading and market makers. Equipped with a **Simple Binary Encoding (SBE)** API, Starbase provides direct access to the matching engine with ultra-low latency, making it ideal for high-frequency trading applications.

Starbase and the standard Deribit APIs are separate order-entry protocols with different credentials, sessions, responses, and order-state visibility. Trades and positions resulting from Starbase orders are available through the standard WebSocket API, but standard JSON-RPC `private/get_open_orders*` methods and private order subscriptions do not return open Starbase orders or their lifecycle updates. Use an SBE order-entry session, the Starbase REST order snapshot, or [FIX Drop Copy](/starbase/fix-drop-copy-api) for Starbase order state. The Starbase **REST** gateway also provides utility endpoints such as portfolio-wide cancellation.

<Info>
  Two versions of the API documentation are available. You can switch between them using the version selector button at the top of the page. Changes in the upcoming version will be available in the production version after the next release. For release notes and information about upcoming releases, see the [Starbase Changelog](/changelogs/starbase).
</Info>

<Card title="Starbase Changelog" icon="clock-rotate-left" href="/changelogs/starbase">
  Review dated schema releases, gateway changes, rollout announcements, and compatibility notes before upgrading or deploying to production.
</Card>

<Info>
  Starbase is accessible exclusively through **hosted colocation** or a **cross-connect** in LD4, or through **AWS Private Link** for clients connecting from AWS infrastructure. Internet connectivity is not supported. Contact <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a> to arrange access.
</Info>

<Warning>
  **Open orders placed via Starbase are not visible in the Deribit web UI.** Due to Starbase's performance characteristics, the feed that powers the UI cannot keep up with the matching engine. Trades and positions will appear in the UI as expected — only open orders are affected.
</Warning>

**The main components of the Starbase API:**

<CardGroup cols={2}>
  <Card title="Binary Order Entry API" icon="book" href="/starbase/binary-api-reference">
    The Binary Order Entry API provides **direct access to the matching engine** using a high-performance binary protocol optimized for ultra-low latency trading.

    * **Order Entry**: Place, amend, and cancel orders with minimal latency. Supports single orders, [mass quotes](/articles/mass-quotes-specifications) (up to 15 double-sided quotes), and mass cancellation.
    * **Market Maker Protection (MMP)**: Built-in protection against adverse selection. See [Market Maker Protection](/articles/market-maker-protection) for details.
    * **Self Match Prevention (SMP):** A highly flexible system to avoid matching orders internally.
  </Card>

  <Card title="Multicast Market Data" icon="network-wired" href="/starbase/multicast-channels">
    Market data is distributed via **multicast channels** organized by product type (BTC perpetuals/futures, BTC options, ETH perpetuals/futures, ETH options, etc.). The multicast channels have:

    * **Market-by-order data**: Market data is sent as L3 data, allowing for full reconstruction of the order book.
    * **A/B Redundancy**: Duplicate feeds (A and B) for high availability.
    * **Snapshot and Incremental Updates**: Snapshot feeds provide the full order book state, while incremental feeds provide real-time updates.
  </Card>

  <Card title="FIX Drop Copy" icon="copy" href="/starbase/fix-drop-copy-api">
    The **FIX Drop Copy** feed provides a consolidated view of all orders and trades across an entire account, regardless of which gateway they were submitted through.

    * **Full order visibility**: Captures all order lifecycle events — new, amended, filled, and cancelled.
    * **FIX 5.0 SP2**: Standard FIX protocol for easy integration with existing OMS/EMS systems.
    * **Account-wide scope**: Unlike per-gateway SBE connections, a single Drop Copy session covers the full portfolio.
  </Card>

  <Card title="Gateway Connectivity" icon="server" href="/starbase/gateway-connectivity">
    Starbase gateways run in **hot-hot A/B pairs** for resilience, with independent rate limits on each side. Clients are expected to connect to both gateways in a pair simultaneously for optimal throughput and redundancy.

    * **Colocated cross-connect**: Lowest latency option for clients physically present in Deribit's data center.
    * **AWS Private Link**: Secure private connectivity for clients on AWS without routing traffic over the public internet.
    * **Multiple gateway pairs**: Gateways are partitioned by underlying asset (BTC, ETH, Tier 2/3) to allow horizontal scaling.
  </Card>
</CardGroup>

<Tip>
  **Recommended order-entry path:** Utilizing the [MMP risk bypass](/starbase/risk-bypass) is the lowest-latency method for market access in Starbase. It works for both orders (via the `MMP` flag) and mass quotes (MMP-enforced by default), reduces load on the risk and margin engines, and most integrating clients should prefer it for all order entry and quoting.
</Tip>

## Scope and migration

* **No spot trading on Starbase.** Spot order books are not available on Starbase; spot trading will migrate to a brokered solution via Coinbase Exchange (CBE). Existing spot APIs remain unchanged in the meantime — see the [spot announcement](/changelogs/starbase) for details.
* **Standard APIs are not going away.** The standard WebSocket API will be supported indefinitely. The legacy SBE feed is scheduled for deprecation at the end of 2026. One exception: portfolios added to a [Member](/starbase/account-model) can no longer use the legacy mass quotes API and must quote through the [Starbase Binary API](/starbase/mass-quotes) — all other standard API access, including regular order entry, is unaffected.

## Integration resources

<CardGroup cols={2}>
  <Card title="Connectivity Quickstart" icon="rocket" href="/starbase/quickstart">
    Validate network access, sessions, market data, recovery, and production readiness.
  </Card>

  <Card title="Reference Data" icon="database" href="/starbase/reference-data">
    Identify the authoritative source for instrument units, tick sizes, tiers, and other metadata.
  </Card>
</CardGroup>


## Related topics

- [Starbase API Rate Limits](/starbase/api-rate-limits.md)
- [Starbase Market Maker Protection (MMP)](/starbase/mmp.md)
- [Starbase API Changelog](/changelogs/starbase.md)
- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
