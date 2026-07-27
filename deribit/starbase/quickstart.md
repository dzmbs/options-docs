> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectivity Quickstart

> Plan and validate Starbase network access, connect to the test gateways and market data feeds, and prepare a resilient production deployment.

This quickstart takes you from network planning to a validated Starbase connection. It focuses on connectivity and session readiness; message schemas and order workflows are covered in the [Binary API Reference](/starbase/binary-api-reference).

<Info>
  Starbase is not available over the public internet. You must connect through **hosted colocation** or a **cross-connect** in LD4, or through **AWS Private Link**. Contact <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a> to arrange network access.
</Info>

## 1. Choose a Deployment Model

The Starbase matching engine and its gateways run in **Equinix LD4 in London**. The Starbase API is exposed through several protocols, including SBE order entry, SBE multicast market data, FIX Drop Copy, and REST.

| Requirement                                      | Recommended deployment                                                   |
| ------------------------------------------------ | ------------------------------------------------------------------------ |
| Lowest possible order-entry latency              | Use hosted colocation or a cross-connect in LD4                          |
| Private connectivity from an AWS-hosted stack    | Use AWS Private Link; latency depends on the AWS region and route to LD4 |
| Monitoring, reconciliation, or disaster recovery | Run remotely, outside the critical execution path                        |

A server in Tokyo or another remote region cannot match the round-trip latency of LD4 colocation because every order must reach the matching engine in London.

For detailed trade-offs and cost categories, see [Infrastructure, Connectivity & Best Practices](/starbase/connectivity-best-practices#deployment-options).

## 2. Request Starbase Access

Before connecting:

1. Ask your Account Manager or Technical Account Manager to enable Starbase on your **test account**.
2. Confirm which main account and subaccounts will trade through Starbase.
3. Configure a [Member and its portfolios](/starbase/account-model).
4. Arrange hosted colocation, a cross-connect, or AWS Private Link with <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a>.
5. Provide the source IP addresses that Deribit should allowlist.

<Note>
  Starbase API keys are separate from standard Deribit API keys. A subaccount must belong to a Member before it can authenticate to Starbase.
</Note>

## 3. Create a Starbase API Key

Create the key from the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the **main account**. Select the Member and portfolio permissions required by the trading application.

See [Creating a Starbase API Key](/starbase/creating-api-key) for the full UI and API workflow.

Keep credentials out of source code, logs, packet captures, and support tickets. Store them in your organization's secret-management system.

## 4. Prepare the Client

Download the integration resources:

* [SBE XML schemas](https://statics.deribit.com/files/deribit-sbe-xmls.zip) — schema definitions for order entry and market data
* [Starbase SDK](https://statics.deribit.com/files/starbase-deribit-sdk.zip) — client SDK for integrating with Starbase
* [Market data PCAP](http://statics.deribit.com/files/starbase-market-data.pcap) — sample multicast packet capture

Then implement:

* [SBE framing, encoding, and decoding](/starbase/binary-api-reference#message-structure)
* [TCP session establishment, authentication, heartbeats, and sequence tracking](/starbase/session-messages)
* Automatic reconnect and state recovery
* [Cancel on Disconnect handling](/starbase/cancel-on-disconnect)
* [UDP multicast reception, packet sequencing, and gap detection](/starbase/multicast-subscription-guide)
* [Snapshot plus incremental L3 order-book reconstruction](/starbase/order-book-maintenance)

Use **IPv4**. SBE order entry uses TCP, multicast market data uses UDP, and REST utility endpoints use HTTPS. FIX Drop Copy and multicast traffic are not TLS-encrypted because they are available only on private connectivity.

## 5. Validate Test Connectivity

Use the addresses and ports in [Gateway Connectivity](/starbase/gateway-connectivity#test-environment). Validate each service separately:

1. Establish TCP connectivity to the test SBE order-entry gateway.
2. Authenticate and maintain a healthy heartbeat exchange.
3. Connect to [FIX Drop Copy](/starbase/fix-drop-copy-api) and complete its session logon.
4. Receive both snapshot and incremental traffic from the required [multicast channels](/starbase/multicast-channels).
5. Verify that [retransmit requests](/starbase/retransmit-gateway) can recover an intentional market-data gap.
6. Connect to the [REST portfolio-management endpoints](/starbase/portfolio-management) over HTTPS.

Do not treat a successful TCP connection as a complete test. Authentication, heartbeats, sequence handling, multicast group membership, and recovery must all work.

## 6. Build a Resilient Session Layout

Production order-entry gateways are organized into hot-hot **A/B pairs** according to the instrument's [underlying tier](/starbase/underlying-tiers):

| Product group                                     | Order-entry connections |
| ------------------------------------------------- | ----------------------- |
| [BTC (Tier 1)](/starbase/underlying-tiers#tier-1) | BTC A and BTC B         |
| [ETH (Tier 1)](/starbase/underlying-tiers#tier-1) | ETH A and ETH B         |
| [Tier 2](/starbase/underlying-tiers#tier-2)       | Tier 2 A and Tier 2 B   |
| [Tier 3](/starbase/underlying-tiers#tier-3)       | Tier 3 A and Tier 3 B   |

Connect only to the product groups you trade, but always connect to **both A and B** within each required pair. Both sides are active, and their rate-limit buckets are independent.

Each API key can establish one connection to each gateway instance. A second connection using the same key on the same gateway disconnects the first. Order events are scoped to the API key and gateway session that originated the order.

## 7. Validate End-to-End Behavior

On test, verify the complete lifecycle before requesting production access:

* [Submit](/starbase/placing-new-order), [amend](/starbase/amending-order), and [cancel](/starbase/cancelling-order) a single order.
* Send a [mass quote](/starbase/mass-quotes) if your strategy uses option quoting.
* Confirm responses on the originating SBE session.
* Confirm lifecycle events and fills on [FIX Drop Copy](/starbase/fix-drop-copy-api).
* Confirm trades through the standard private WebSocket API.
* Confirm that open Starbase orders do **not** appear in the web UI or private WebSocket order feed.
* Disconnect a session and verify [Cancel on Disconnect](/starbase/cancel-on-disconnect) behavior.
* Reconnect, rebuild state, and resubmit only after reviewing current market conditions.
* Exercise A/B failover without losing the local view of orders or the book.

<Warning>
  Cancel on Disconnect is always enabled and session-scoped. Orders from a disconnected session are cancelled immediately and are not restored when the session reconnects.
</Warning>

Before production, also review behavior that can change order acceptance or timing: [speed bumps](/starbase/speed-bumps), [Market Maker Protection](/starbase/mmp), [Self Match Prevention](/starbase/smp), and [risk bypass](/starbase/risk-bypass).

## 8. Review Capacity

Starbase rate limits are applied **per Member, per gateway, and per quoting type**. API keys and sessions within the same Member do not each receive a fresh allocation.

Before production:

* Estimate steady-state and burst order rates by product group.
* Separate single-order traffic from [mass-quote](/starbase/mass-quotes) traffic.
* Use both A and B gateways where appropriate.
* Confirm the number of API keys and active orders required.
* Discuss non-default allocations with your Account Manager.

See [API Rate Limits](/starbase/api-rate-limits) for bucket behavior, defaults, and other limits.

## 9. Prepare for Production

Production readiness should include:

* Redundant client hosts, network interfaces, and power where applicable
* Active connections to both sides of every required gateway pair
* Both A and B [multicast feeds](/starbase/multicast-channels), including snapshot and [retransmit recovery](/starbase/retransmit-gateway)
* Independent [FIX Drop Copy](/starbase/fix-drop-copy-api) ingestion and durable event persistence
* [Clock synchronization](/starbase/binary-api-reference#clock-synchronization); colocated clients can request PTP
* Metrics and alerts for session state, heartbeats, sequence gaps, rejects, and recovery
* A tested runbook for disconnects, stale books, failover, and reconciliation

Use the production endpoints only after Deribit confirms that account, credentials, source IPs, and network access are ready.

## Troubleshooting

If connectivity fails, record:

* Test or production environment
* Connectivity type and hosting provider
* Account UID and Starbase ClientID
* Source IP, destination IP, port, protocol, gateway, and side
* UTC timestamps and the last successful heartbeat or sequence number
* Whether side A, side B, or both are affected
* TCP-connectivity results and a short sanitized packet capture
* Expected behavior, observed behavior, and any reject code

Send network and multicast issues to <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a>. Send protocol rejects and account-configuration questions to your Technical Account Manager or Deribit Support.

## Next Steps

<CardGroup cols={2}>
  <Card title="Infrastructure & Best Practices" icon="server" href="/starbase/connectivity-best-practices">
    Review deployment costs, gateway architecture, failover, and protocol selection.
  </Card>

  <Card title="Gateway Connectivity" icon="network-wired" href="/starbase/gateway-connectivity">
    Find test and production addresses, ports, and gateway mappings.
  </Card>

  <Card title="Binary API Reference" icon="code" href="/starbase/binary-api-reference">
    Implement session and order-entry messages.
  </Card>

  <Card title="Multicast Subscription Guide" icon="wave-pulse" href="/starbase/multicast-subscription-guide">
    Configure multicast reception and local book maintenance.
  </Card>
</CardGroup>


## Related topics

- [Quickstart Guide](/articles/deribit-quickstart.md)
- [Gateway Connectivity](/starbase/gateway-connectivity.md)
- [Infrastructure, Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [Welcome to Deribit API](/index.md)
- [Starbase API Overview](/starbase/overview.md)
