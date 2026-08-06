> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Infrastructure, Connectivity & Best Practices

> Deployment options, commercial considerations, gateway architecture, protocols, failover, and low-latency integration guidance for Starbase.

Starbase is Deribit's high-performance matching engine and API for clients who are market making or deploying high-frequency strategies. The API provides lower-latency access through several protocols, including SBE order entry, SBE multicast market data, FIX Drop Copy, and REST. Deribit and Starbase are located in **LD4**.

<Info>
  **Existing Deribit APIs remain available.** Standard WebSocket and REST order entry continue to work for supported instruments, but they are not wire- or behavior-compatible with Starbase SBE. They use separate credentials and sessions, have different response semantics, and do not expose live open-order state for orders submitted through Starbase.
</Info>

<Note>
  To have your **Test account enabled** for Starbase, please reach out to your Account Manager or Technical Account Manager.
</Note>

## Architecture & Location

The Starbase matching engine and its gateways run in **LD4** — none of Deribit's infrastructure is deployed in the cloud. Clients on AWS can reach Starbase over **AWS Private Link** without traversing the public internet, but this is a connectivity option only, not a change in where the infrastructure runs. For server-level detail, see [Server Infrastructure](https://support.deribit.com/hc/en-us/articles/25944617582877-Server-Infrastructure).

There is no layering between Starbase protocols — SBE order entry and SBE market data talk directly to the matching engine and are not built on top of FIX or WebSocket internals (nor vice versa). SBE is the most performant option Deribit offers and is expected to remain so.

For the lowest possible network latency, run the latency-sensitive trading stack in **LD4** using hosted colocation or a cross-connect. A server in another region, including Tokyo, must still reach the matching engine in London and therefore cannot provide the same round-trip latency as an LD4 deployment. Remote infrastructure can still be used for monitoring, risk, research, and disaster recovery.

<Note>
  Per-hop latency breakdowns (network, gateway, matching engine processing time, etc.) are not published yet. Deribit is deploying Corvil monitoring in LD4 to produce these figures.
</Note>

## Deployment Options

| Option                            | Recommended use                                                   | Latency characteristics                                                                                                          |
| --------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Hosted colocation in LD4**      | Clients that want managed hosting close to Starbase               | Lowest-latency option without operating their own LD4 footprint                                                                  |
| **Cross-connect in LD4**          | Clients with their own LD4 presence                               | Lowest-latency direct connectivity from the client's LD4 infrastructure                                                          |
| **AWS Private Link**              | Clients whose trading systems run on AWS                          | Private connectivity without traversing the public internet; network latency depends on the client's AWS region and route to LD4 |
| **Remote support infrastructure** | Monitoring, risk, reconciliation, research, and disaster recovery | Suitable for non-critical-path services; not equivalent to LD4 colocation for order round trips                                  |

Starbase does **not** accept connections over the public internet. For hosted colocation, cross-connects, AWS connectivity, multicast delivery, PTP access, and network onboarding, contact <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a>.

### Commercial Costs

There is no single public price that applies to every deployment. The total cost depends on the connectivity model and the services purchased from the chosen data-center or hosting provider.

Plan for the following line items:

* Hosted-colocation fees, or rack space and power for clients operating their own LD4 footprint
* Cross-connect installation and recurring charges
* Network transit or AWS connectivity charges
* Optional managed hosting or remote-hands services
* Optional PTP service

Contact <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a> for connectivity requirements and your hosting or colocation provider for a commercial quote. Contact your Deribit Account Manager to confirm Starbase access and discuss rate-limit requirements. Higher rate limits are capacity allocations based on the strategy's technical needs and expected liquidity contribution; they should not be treated as an automatically purchasable add-on. See [API Rate Limits](/starbase/api-rate-limits).

## Getting Started

### Starbase API Key

Starbase uses a **separate API key** from your standard Deribit API key. See [Creating a Starbase API Key](/starbase/creating-api-key) for setup instructions.

### Available Protocols and Interfaces

| Protocol or interface | Purpose                                                   |
| --------------------- | --------------------------------------------------------- |
| SBE — Order Entry     | Place, amend, and cancel orders via the binary protocol   |
| SBE — Market Data     | Low-latency L3 multicast market data feeds                |
| SBE — Retransmit      | Request retransmission of missed market data packets      |
| FIX Drop Copy         | Consolidated account-wide order and trade feed            |
| REST                  | Utility endpoints (order snapshot, purge, reference data) |

### Compatibility with standard Deribit APIs

“Existing APIs remain available” means clients can continue using the standard APIs alongside Starbase. It does not mean requests, responses, or private event streams are interchangeable.

| Capability                       | Standard WebSocket / JSON-RPC                                             | Starbase                                                                               |
| -------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Authentication                   | Standard Deribit API key                                                  | Separate Starbase API key                                                              |
| Order entry                      | JSON-RPC methods                                                          | SBE order-entry messages                                                               |
| Open Starbase order lifecycle    | Not returned by `private/get_open_orders*` or private order subscriptions | Originating SBE session, Starbase REST order snapshot, or Starbase FIX Drop Copy       |
| Starbase trades and positions    | Available                                                                 | Available through SBE and FIX Drop Copy                                                |
| Mass-quote validation            | Each side is validated independently                                      | The entire `MassQuoteRequest` is rejected if any quantity is invalid                   |
| Reference and configuration APIs | Used for data such as derived statistics and MMP configuration            | SBE provides latency-sensitive trading and market data; REST provides a utility subset |

Design each protocol as a separate adapter and reconcile them through exchange-assigned identifiers and trade/position records. See [Mass Quotes](/starbase/mass-quotes), [Reference Data](/starbase/reference-data), and [FIX Drop Copy](/starbase/fix-drop-copy-api) for the protocol-specific behavior.

### Recommended Production Architecture

Keep the execution path small and run order entry, book building, and strategy logic close together:

1. Subscribe to both **A and B incremental and snapshot multicast feeds** for every traded product group.
2. Reconstruct and maintain the L3 order book locally.
3. Connect to both **A and B order-entry gateways** for each traded product group.
4. Load-balance order flow across A and B while retaining automatic failover.
5. Consume **FIX Drop Copy** independently from order-entry sessions and persist its Execution Reports for reconciliation.
6. Keep slower control-plane functions, analytics, and long-term storage outside the critical execution path.

<Info>
  FIX Drop Copy is the recommended source for a consolidated order and trade audit trail. Standard WebSocket APIs continue to expose Starbase trades and positions, but they do not expose open Starbase orders or their lifecycle updates.
</Info>

### Protocol Support

| Protocol | Support                                                                                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IPv4     | Supported                                                                                                                                                                                      |
| IPv6     | Not supported                                                                                                                                                                                  |
| TLS      | REST only (HTTPS). FIX Drop Copy and SBE Market Data multicast are unencrypted — both are reachable only via hosted colocation, cross-connect, or AWS Private Link, never the public internet. |
| HTTP/3   | Not implemented                                                                                                                                                                                |
| QUIC     | Not implemented                                                                                                                                                                                |

***

## Gateway Architecture

Starbase uses a distributed gateway architecture designed for high availability and horizontal scaling:

* Gateways run in **hot-hot A/B pairs** — both gateways in a pair are fully active at all times; neither is a standby.
* Each gateway pair provides access to a specific set of order books.
* Order books for the same underlying asset are always on the same gateway pair, ensuring atomicity of MMP and implied matching.
* All sessions connected to a given gateway share a **single inbound event-loop thread** — requests from every session on that gateway are processed sequentially, in receipt order.

### Rule 1 — Connection Limits per API Key

| Rule                                   | Detail                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------- |
| One connection per gateway per API key | Each API key can establish exactly **one** connection to each gateway instance              |
| Multi-gateway connections allowed      | The same API key can connect to **all** gateway pairs simultaneously                        |
| Duplicate connection handling          | A second connection attempt with the same key to the same gateway **disconnects the first** |

<Note>
  With 4 gateway pairs, a single API key can establish up to **8 simultaneous connections** — one to each instance: 1A, 1B, 2A, 2B, 3A, 3B, 4A, 4B.
</Note>

### Rule 2 — Event Scoping

| Rule                           | Detail                                                                                                            |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Session-scoped events          | An SBE connection only receives events for orders sent by that API key on that specific gateway                   |
| No cross-session event sharing | Orders on Gateway A with API Key X will **not** generate events on Gateway B or on any connection using API Key Y |
| Per-key isolation              | Orders submitted with API Key A will not generate events on connections using API Key B                           |

<Note>
  This design allows multiple API keys to be assigned to a single portfolio without creating portfolio-level bottlenecks.
</Note>

### Rule 3 — Rate Limits

| Rule                    | Detail                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| Independent rate limits | Rate limits on Gateway A and B are completely independent                                         |
| Effective combined rate | A rate limit of 100 req/s per gateway yields an effective combined rate of **200 req/s** per pair |

***

## Gateway-to-Product Mapping

* **Order Entry Gateways:** See [Gateway Connectivity](/starbase/gateway-connectivity)
* **Multicast Market Data Channels:** See [Multicast Channels](/starbase/multicast-channels)

### Quick Reference

| Trading Focus | Order Entry Gateways | Market Data Channels          |
| ------------- | -------------------- | ----------------------------- |
| BTC only      | 1A + 1B              | BTC Perps + BTC Options (A+B) |
| ETH only      | 2A + 2B              | ETH Perps + ETH Options (A+B) |
| BTC + ETH     | 1A + 1B + 2A + 2B    | BTC + ETH channels (A+B)      |
| Tier 2 Alts   | 3A + 3B              | Tier 2 channels (A+B)         |
| Tier 3 Alts   | 4A + 4B              | Tier 3 channels (A+B)         |
| All products  | All 8 gateways       | All multicast channels        |

***

## Failover Scenarios

### Scenario 1 — Single Gateway Failure (A or B)

| Situation       | Action                                       |
| --------------- | -------------------------------------------- |
| Gateway A fails | Continue trading on Gateway B                |
| Gateway B fails | Continue trading on Gateway A                |
| Impact          | No service interruption if connected to both |

<Tip>
  Always connect to **both A and B** gateways in each pair, send orders to both for optimal latency, and implement automatic failover logic in your client.
</Tip>

### Scenario 2 — Connection Loss & Cancel on Disconnect (CoD)

Cancel on Disconnect is **always enabled** on Starbase and cannot be disabled or configured.

| Behavior                 | Detail                                                             |
| ------------------------ | ------------------------------------------------------------------ |
| Scope                    | Session-scoped — only cancels orders from the disconnected session |
| Trigger                  | Immediate upon connection loss                                     |
| Impact on other sessions | Losing Gateway A does **not** affect orders open on Gateway B      |

**Connection loss is detected via:**

* TCP connection closure
* Missing heartbeats (heartbeats cannot be disabled)
* Explicit logout

### Scenario 3 — Reconnection After Disconnect

| Rule                  | Detail                                                                            |
| --------------------- | --------------------------------------------------------------------------------- |
| Orders not restored   | Previously cancelled orders are **not** automatically restored after reconnection |
| Resubmission required | Clients must resubmit orders to re-establish their order book                     |
| CoD remains enabled   | The new session also has CoD always enabled                                       |

### Scenario 4 — Cross-Session Amends and CoD

| Rule                                    | Detail                                                                                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CoD is bound to the originating session | CoD tracks whichever session originally submitted the order                                                                                             |
| No rebinding on amend                   | If an order submitted on Session A is amended from Session B, disconnecting Session A will still cancel the order — even if Session B remains connected |

***

## Consolidated View: FIX Drop Copy

Because SBE connections are session-scoped, use [FIX Drop Copy](/starbase/fix-drop-copy-api) for:

* A consolidated view of all activity across a single portfolio
* Reconciliation across all gateways
* Aggregated trade feed
* Durable order/trade record-keeping — order history endpoints don't retroactively return rejected or zero-fill orders, so persist Execution Reports from Drop Copy as they arrive (see the note on rejected orders in [FIX Drop Copy](/starbase/fix-drop-copy-api))

Trades placed through Starbase also appear on the standard WebSocket/FIX feeds, but **open Starbase orders do not** — those are only visible via Starbase FIX Drop Copy or an SBE session.

***

## Best Practices Summary

### Connection Management

* Connect to **both A and B** gateways in each pair
* Implement robust connection monitoring and automatic reconnection
* Handle `OrdersCanceled` messages to maintain accurate order state
* Re-evaluate and resubmit orders after reconnection based on current market conditions
* Use graceful logout when intentionally disconnecting

### Order Management

* Remember each SBE session is fully independent
* Orders submitted on one session only generate events on that session
* Avoid cross-session amends when CoD behavior is critical
* Use the same API key across gateways for a simpler audit trail

### Market Data

* Subscribe to **both A and B** multicast feeds — they have similar latency profiles
* Subscribe to both **Snapshot** and **Incremental** channels
* Implement full order book reconstruction from L3 data

### Protocol Selection

* Use **SBE order entry** for the lowest-latency placement, amendment, and cancellation path.
* Use **SBE multicast market data** for the lowest-latency L3 book.
* Use **FIX Drop Copy** for consolidated order lifecycle events, fills, and durable reconciliation. Persist events as they arrive: rejected and zero-fill orders cannot always be recovered later from order-history endpoints.
* Use **REST** for utility and recovery workflows, not as the primary execution or live order-state path. In particular, `get_open_orders` is limited to one request per minute per IP.
* Use the standard **WebSocket API** where its additional latency is acceptable or for data not yet available in the Starbase feed. Do not rely on it for open Starbase order updates.

### Access and Capacity Planning

* Create a dedicated Starbase API key; standard Deribit API keys cannot authenticate to Starbase.
* Allowlist all source IP addresses that will establish Starbase connections.
* Size connections by product gateway and resilience requirements, not to multiply throughput. Rate limits are shared per Member, per gateway, and per quoting type across all keys, sessions, and portfolios.
* Use both sides of a gateway pair: A and B have independent rate-limit buckets.
* Use mass quotes for option quoting rather than sending equivalent batches of single orders.
* Discuss non-default rate-limit requirements with your Account Manager before production rollout.

## Network Troubleshooting Checklist

When reporting a connectivity or latency issue, include enough detail to identify the route and reproduce the problem:

* Environment: test or production
* Connectivity type: LD4 cross-connect, managed colocation, or AWS Private Link
* Account UID and Starbase ClientID
* Affected protocol or interface, gateway side, destination address, and port
* Source IP address and, for colocated clients, hosting provider and cross-connect identifier
* UTC timestamps with nanosecond precision where available
* Whether the issue affects side A, side B, or both
* TCP connection and application-session status, including the last successful heartbeat or sequence number
* Ping and TCP-connectivity results where supported by the network path
* A short packet capture covering the incident, with credentials and sensitive payloads removed
* Expected and observed behavior, including relevant reject codes or sequence gaps

For persistent network or multicast issues, send this information to <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a>. For protocol-level rejects or account configuration, contact your Technical Account Manager or Deribit Support.


## Related topics

- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Order Management](/articles/order-management-best-practices.md)
- [API Usage Policy](/articles/api-usage-policy.md)
- [Market Data Collection](/articles/market-data-collection-best-practices.md)
- [Connection Management](/articles/connection-management-best-practices.md)
