> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectivity & Best Practices

> Overview of Starbase connectivity, gateway architecture, failover scenarios, and best practices for market makers and high-frequency trading clients.

Starbase is Deribit's high-performance matching engine offering a new set of APIs targeted at clients who are market making or deploying high-frequency strategies. These APIs provide lower latency access to the matching engine with new connectivity options, networking requirements, and protocols. Deribit and Starbase are colocated in **LD4**.

<Info>
  **Existing Deribit APIs are unaffected.** Standard WebSocket and REST APIs continue to work for all instruments, but will not offer the same latency as the Starbase-native APIs.
</Info>

<Note>
  To have your **Test account enabled** for Starbase, please reach out to your Account Manager or Technical Account Manager.
</Note>

## Architecture & Location

All Starbase matching engines and gateways run in **LD4** — none of Deribit's infrastructure is deployed in the cloud. Clients on AWS can reach Starbase over **AWS Private Link** without traversing the public internet, but this is a connectivity option only, not a change in where the infrastructure runs. For server-level detail, see [Server Infrastructure](https://support.deribit.com/hc/en-us/articles/25944617582877-Server-Infrastructure).

There is no layering between Starbase APIs — SBE order entry and SBE market data talk directly to the matching engine and are not built on top of FIX or WebSocket internals (nor vice versa). SBE is the most performant option Deribit offers and is expected to remain so.

<Note>
  Per-hop latency breakdowns (network, gateway, matching engine processing time, etc.) are not published yet. Deribit is deploying Corvil monitoring in LD4 to produce these figures.
</Note>

## Getting Started

### Starbase API Key

Starbase uses a **separate API key** from your standard Deribit API key. See [Creating a Starbase API Key](/starbase/creating-api-key) for setup instructions.

### Available APIs

| API               | Purpose                                                   |
| ----------------- | --------------------------------------------------------- |
| SBE — Order Entry | Place, amend, and cancel orders via the binary protocol   |
| SBE — Market Data | Low-latency L3 multicast market data feeds                |
| SBE — Retransmit  | Request retransmission of missed market data packets      |
| FIX Drop Copy     | Consolidated account-wide order and trade feed            |
| REST              | Utility endpoints (order snapshot, purge, reference data) |

### Protocol Support

| Protocol | Support                                                                                                                                                                              |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| IPv4     | Supported                                                                                                                                                                            |
| IPv6     | Not supported                                                                                                                                                                        |
| TLS      | REST only (HTTPS). FIX Drop Copy and SBE Market Data multicast are unencrypted — both are reachable only via colocated cross-connect or AWS Private Link, never the public internet. |
| HTTP/3   | Not implemented                                                                                                                                                                      |
| QUIC     | Not implemented                                                                                                                                                                      |

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
