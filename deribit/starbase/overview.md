> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starbase API Overview

> High-level introduction to Deribit Starbase — the low-latency binary and FIX API stack, gateways, and how it differs from the main Deribit API.

Starbase is Deribit's high-performance matching engine designed for institutional trading and market makers. Equipped with a **Simple Binary Encoding (SBE)** API, Starbase provides direct access to the matching engine with ultra-low latency, making it ideal for high-frequency trading applications.

Standard Deribit WebSocket APIs (e.g. `private/get_user_trades_by_instrument`) also work for orders placed through Starbase. A **REST** API with utility endpoints such as an order purge or order snapshot will also be added.

<Info>
  Two versions of the API documentation are available. You can switch between them using the version selector button at the top of the page. Changes in the upcoming version will be available in the production version after the next release. For release notes and information about upcoming releases, see the [Starbase Changelog](/changelogs/starbase).
</Info>

<Info>
  Starbase is accessible exclusively via **colocated cross-connect** at Deribit's data center or via **AWS Private Link** for clients connecting from AWS infrastructure. Internet connectivity is not supported. Contact [colo-support@coinbase.com](mailto:colo-support@coinbase.com) to arrange access.
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
    * **Self Match Prevention (SMP):** A highly flexible system to avoid matching order internally.
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


## Related topics

- [Starbase API Changelog](/changelogs/starbase.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [Underlying Tiers](/starbase/underlying-tiers.md)
- [Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [Speed Bumps](/starbase/speed-bumps.md)
