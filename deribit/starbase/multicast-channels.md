> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multicast Channels

> Starbase SBE market data over UDP multicast — A and B redundant channels sharded by product type for low-latency market data feed consumption.

<Info>
  **Multicast & networking support**: For detailed multicast or networking questions, contact [colo-support@coinbase.com](mailto:colo-support@coinbase.com).
</Info>

<Warning>
  **Test environment**: Only instruments actively running on Starbase in the test environment have live market data. If you subscribe to a test channel for an instrument that is not yet active on Starbase, you will not receive any data.
</Warning>

<Note>
  Market data will only be sent by the **active** switch and duplicate data will not be received. The secondary connection will begin to receive market data during a failover scenario.
</Note>

## Cross-Connects & Non-Colocated Access

Cross-connects are available in LD4. Deribit is running a cable-length equalization process so that latency does not depend on a client's rack placement within the data center. Contact [colo-support@coinbase.com](mailto:colo-support@coinbase.com) to arrange a cross-connect.

Clients who are not colocated or cross-connected can still receive multicast market data over AWS via the [Deribit AWS Multicast Service](https://support.deribit.com/hc/en-us/articles/25944617728285-Deribit-AWS-Multicast-Service-Instruction).

## Feed Characteristics

* Each gateway publishes market data from a **single event-loop thread**, so sequence numbers within a channel are strictly increasing and monotonic.
* Updates are **batched**: a single UDP packet can contain multiple messages (see `messageCount` in the [packet header](/starbase/binary-api-reference#udp-messages)).
* This is a **Level 3 (market-by-order)** feed — every matching engine event that affects the book is reflected here, including an order that is added and then immediately removed, which still produces both the add (`Buy Put`/`Sell Put`) and the subsequent `Order Delete` message. There is no separate Level 2 (aggregated price-level) feed on Starbase.

| Product Type                                      | Feed | Type        | IP Address   | Port |
| ------------------------------------------------- | ---- | ----------- | ------------ | ---- |
| **BTC Perpetuals, Futures and Future Spreads**    | A    | Snapshot    | 224.0.12.192 | 4230 |
|                                                   |      | Incremental | 224.0.12.193 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.208 | 4230 |
|                                                   |      | Incremental | 224.0.12.209 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.224 | 4230 |
|                                                   |      | Incremental | 224.0.12.225 | 4220 |
| **BTC Options and Option Combinations**           | A    | Snapshot    | 224.0.12.194 | 4230 |
|                                                   |      | Incremental | 224.0.12.195 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.210 | 4230 |
|                                                   |      | Incremental | 224.0.12.211 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.226 | 4230 |
|                                                   |      | Incremental | 224.0.12.227 | 4220 |
| **ETH Perpetuals, Futures and Future Spreads**    | A    | Snapshot    | 224.0.12.196 | 4230 |
|                                                   |      | Incremental | 224.0.12.197 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.212 | 4230 |
|                                                   |      | Incremental | 224.0.12.213 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.228 | 4230 |
|                                                   |      | Incremental | 224.0.12.229 | 4220 |
| **ETH Options and Option Combinations**           | A    | Snapshot    | 224.0.12.198 | 4230 |
|                                                   |      | Incremental | 224.0.12.199 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.214 | 4230 |
|                                                   |      | Incremental | 224.0.12.215 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.230 | 4230 |
|                                                   |      | Incremental | 224.0.12.231 | 4220 |
| **Tier 2 Futures, Perpetuals and Future Spreads** | A    | Snapshot    | 224.0.12.200 | 4230 |
|                                                   |      | Incremental | 224.0.12.201 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.216 | 4230 |
|                                                   |      | Incremental | 224.0.12.217 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.232 | 4230 |
|                                                   |      | Incremental | 224.0.12.233 | 4220 |
| **Tier 2 Options and Option Combinations**        | A    | Snapshot    | 224.0.12.202 | 4230 |
|                                                   |      | Incremental | 224.0.12.203 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.218 | 4230 |
|                                                   |      | Incremental | 224.0.12.219 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.234 | 4230 |
|                                                   |      | Incremental | 224.0.12.235 | 4220 |
| **Tier 3 Futures, Perpetuals and Future Spreads** | A    | Snapshot    | 224.0.12.204 | 4230 |
|                                                   |      | Incremental | 224.0.12.205 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.220 | 4230 |
|                                                   |      | Incremental | 224.0.12.221 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.236 | 4230 |
|                                                   |      | Incremental | 224.0.12.237 | 4220 |
| **Equity perpetuals and pre-launch tokens**       | A    | Snapshot    | 224.0.12.206 | 4230 |
|                                                   |      | Incremental | 224.0.12.207 | 4220 |
|                                                   | B    | Snapshot    | 224.0.12.222 | 4230 |
|                                                   |      | Incremental | 224.0.12.223 | 4220 |
|                                                   | Test | Snapshot    | 224.0.12.238 | 4230 |
|                                                   |      | Incremental | 224.0.12.239 | 4220 |

Retransmit:

| Product Type                                      | Feed | IP Address     | Port |
| :------------------------------------------------ | ---- | :------------- | :--- |
| **BTC Perpetuals, Futures and Future Spreads**    | Test | 195.138.37.139 | 4240 |
| **BTC Options and Option Combinations**           | Test | 195.138.37.139 | 4241 |
| **ETH Perpetuals, Futures and Future Spreads**    | Test | 195.138.37.139 | 4242 |
| **ETH Options and Option Combinations**           | Test | 195.138.37.139 | 4243 |
| **Tier 2 Futures, Perpetuals and Future Spreads** | Test | 195.138.37.139 | 4244 |
| **Tier 2 Options and Option Combinations**        | Test | 195.138.37.139 | 4245 |
| **Tier 3 Futures, Perpetuals and Future Spreads** | Test | 195.138.37.139 | 4246 |
| **Equity perpetuals and pre-launch tokens**       | Test | 195.138.37.139 | 4247 |


## Related topics

- [Multicast Subscription Guide](/starbase/multicast-subscription-guide.md)
- [Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [Gateway Connectivity](/starbase/gateway-connectivity.md)
- [Starbase API Changelog](/changelogs/starbase.md)
- [Underlying Tiers](/starbase/underlying-tiers.md)
