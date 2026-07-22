> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gateway Connectivity

> Starbase gateway endpoints, host lists, connection credentials, and network requirements for reaching the order entry and market data servers.

## Connectivity

### Test Environment

| Gateway                    | Side | Address                                                | Port        | Protocol                      | AWS Port        |
| -------------------------- | ---- | ------------------------------------------------------ | ----------- | ----------------------------- | --------------- |
| sbe-order                  | A    | 195.138.37.137                                         | 4210        | TCP                           | 14210           |
| sbe-order                  | B    | 195.138.37.138                                         | 4210        | TCP                           | 24210           |
| fix-drop-copy              | A    | 195.138.37.139                                         | 4130        | TCP                           | 14130           |
| sbe-marketdata-retransmit  | A    | 195.138.37.139                                         | 4240 – 4247 | UDP Unicast<br />+ UDP Return |                 |
| sbe-marketdata-incremental | A    | [See Multicast Channels](/starbase/multicast-channels) | 4220        | UDP Multicast                 | Multicast Relay |
| sbe-marketdata-snapshot    | A    | [See Multicast Channels](/starbase/multicast-channels) | 4230        | UDP Multicast                 | Multicast Relay |
| REST                       | A    | 195.138.37.137                                         | 4410        | HTTPS                         | 14410           |
| REST                       | B    | 195.138.37.138                                         | 4410        | HTTPS                         | 24410           |

### Production Environment

| Gateway                    | Side | Address                                                | Port        | Protocol                      | AWS Port        |
| -------------------------- | ---- | ------------------------------------------------------ | ----------- | ----------------------------- | --------------- |
| sbe-order (BTC)            | A    | 195.138.37.1                                           | 4210        | TCP                           | 34210           |
| sbe-order (ETH)            | A    | 195.138.37.3                                           | 4211        | TCP                           | 34211           |
| sbe-order (Tier 2)         | A    | 195.138.37.5                                           | 4212        | TCP                           | 34212           |
| sbe-order (Tier 3)         | A    | 195.138.37.7                                           | 4213        | TCP                           | 34213           |
| sbe-order (BTC)            | B    | 195.138.37.2                                           | 4210        | TCP                           | 44210           |
| sbe-order (ETH)            | B    | 195.138.37.4                                           | 4211        | TCP                           | 44211           |
| sbe-order (Tier 2)         | B    | 195.138.37.6                                           | 4212        | TCP                           | 44212           |
| sbe-order (Tier 3)         | B    | 195.138.37.8                                           | 4213        | TCP                           | 44213           |
| fix-drop-copy              | A    | 195.138.37.7                                           | 4130        | TCP                           | 34130           |
| fix-drop-copy              | B    | 195.138.37.8                                           | 4130        | TCP                           | 44130           |
| sbe-marketdata-retransmit  | A    | 195.138.37.9                                           | 4240 – 4247 | UDP Unicast<br />+ UDP Return |                 |
| sbe-marketdata-retransmit  | B    | 195.138.37.10                                          | 4240 – 4247 | UDP Unicast<br />+ UDP Return |                 |
| sbe-marketdata-incremental | A    | [See Multicast Channels](/starbase/multicast-channels) | 4220        | UDP Multicast                 | Multicast Relay |
| sbe-marketdata-incremental | B    | [See Multicast Channels](/starbase/multicast-channels) | 4220        | UDP Multicast                 | Multicast Relay |
| sbe-marketdata-snapshot    | A    | [See Multicast Channels](/starbase/multicast-channels) | 4230        | UDP Multicast                 | Multicast Relay |
| sbe-marketdata-snapshot    | B    | [See Multicast Channels](/starbase/multicast-channels) | 4230        | UDP Multicast                 | Multicast Relay |
| REST                       | A    | 195.138.37.5                                           | 4410        | HTTPS                         | 34410           |
| REST                       | B    | 195.138.37.6                                           | 4410        | HTTPS                         | 44410           |

## Gateway Architecture

Starbase will have multiple gateways available for order entry. Gateways will always be run in pairs, A and B, for resilience. Both gateways run in a **hot-hot** configuration, meaning they are both fully active at all times and neither should be treated as a backup. For optimal latency you should connect to and use both gateways in a pair simultaneously.

**Rate limits on A and B are independent.** For example, a rate limit of 100 requests/s means you can send 100 requests/s on Gateway A *and* 100 requests/s on Gateway B, for an effective combined rate of 200 requests/s per pair.

Each pair of gateways will provide access to a set of order books, to allow for horizontal scaling. The available set of order books per gateway might change depending on the distribution of throughput per order book. Order books belonging to the same underlying asset will always appear on the same gateway to ensure the atomicity of MMP and implied matching. See below for an example order book layout of the gateways.

| Gateway     | Order Books                                                 |
| ----------- | ----------------------------------------------------------- |
| Gateway 1 A | All BTC\_USD and BTC\_USDC derivatives                      |
| Gateway 1 B | All BTC\_USD and BTC\_USDC derivatives                      |
| Gateway 2 A | All ETH\_USD and ETH\_USDC derivatives                      |
| Gateway 2 B | All ETH\_USD and ETH\_USDC derivatives                      |
| Gateway 3 A | All [Tier 2](/starbase/underlying-tiers#tier-2) derivatives |
| Gateway 3 B | All [Tier 2](/starbase/underlying-tiers#tier-2) derivatives |
| Gateway 4 A | All [Tier 3](/starbase/underlying-tiers#tier-3) derivatives |
| Gateway 4 B | All [Tier 3](/starbase/underlying-tiers#tier-3) derivatives |

## API Keys

Each API key can establish exactly one connection to each gateway. For example, if there are 4 gateway pairs, one API key can be used to establish 8 connections. This ensures a clear audit trail for messages to help both Deribit and the client to debug and eliminates the need for gateways to communicate with each other.

Trying to establish a second connection with the same key to the same gateway will result in a disconnection of the first connection.

### Connecting to multiple gateways

**Connection Rules**:

* Clients can have only **one connection per gateway instance per API key**
* Clients can use the **same API key on every gateway**

This means you can connect to different gateway instances using the same API credentials, but you cannot maintain multiple simultaneous connections to the same gateway instance with the same credentials.

**Event Scoping**: An SBE connection only receives events about orders sent by the API key on that gateway. This means:

* Orders submitted on Gateway A with API Key X will only generate events on the Gateway A connection using API Key X
* Orders submitted on Gateway B with API Key X will only generate events on the Gateway B connection using API Key X
* Orders submitted with API Key A will not generate events on a connections established with API Key B.

This is done to ensure many API Keys can be given out to a single Portfolio without Portfolio-level bottlenecks becoming an issue.

For a consolidated view of all activity on a single Portfolio, the [FIX Drop Copy API](/starbase/fix-drop-copy-api) is available. Standard Deribit WebSocket APIs also work for orders placed through Starbase.


## Related topics

- [Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [REST Order Gateway Authentication](/starbase/rest-authentication.md)
- [Starbase API Overview](/starbase/overview.md)
- [API Rate Limits](/starbase/api-rate-limits.md)
- [Cancel on Disconnect](/starbase/cancel-on-disconnect.md)
