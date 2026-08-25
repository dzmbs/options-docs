> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Binary API Reference

> Complete reference for the Starbase Binary API — SBE encoding, order entry messages, market data channels, and session lifecycle handling.

## Downloads

<CardGroup cols={2}>
  <Card title="SBE Order API XML" icon="file-code">
    Schema definition for SBE order entry.

    * [Production](/specifications/deribit-sbe-xmls/deribit-sbe-order-api.xml) — latest version: 15 (semantic version 1.5)
    * [Testnet](/specifications/deribit-sbe-xmls/deribit-sbe-order-api-testnet.xml) — latest version: 14 (semantic version 1.5)
  </Card>

  <Card title="SBE Market Data API XML" icon="file-code">
    Schema definition for SBE market data.

    * [Production](/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api.xml) — latest version: 1 (semantic version 1.0)
    * [Testnet](/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api-testnet.xml) — latest version: 1 (semantic version 1.0)
  </Card>

  <Card title="Starbase SDKs" icon="box">
    Client SDKs for integrating with Starbase, built from the latest schemas.

    * [Order entry SDK](/starbase/starbase-deribit-order-sdk-14.0.zip) — schema version 14 (semantic version 1.5)
    * [Market data SDK](/starbase/starbase-deribit-md-sdk-1.0.zip) — schema version 1 (semantic version 1.0)
  </Card>

  <Card title="Market Data PCAP" icon="wave-square" href="http://statics.deribit.com/files/starbase-market-data.pcap">
    Sample packet capture for market data
  </Card>
</CardGroup>

## Historical XMLs

Previous versions of the SBE Order API schema. Each XML is the final state of that semantic version.

| Semantic version | Schema version | Release date                                                          | Download                                                                                                     |
| ---------------- | -------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1.0              | 1              | [2026-05-06](/changelogs/starbase#starbase-release-06-05-2026-—-v1-0) | [deribit-sbe-order-api-v1.0.xml](/specifications/deribit-sbe-xmls/historical/deribit-sbe-order-api-v1.0.xml) |
| 1.1              | 7              | [2026-06-26](/changelogs/starbase#starbase-release-26-06-2026-—-v1-1) | [deribit-sbe-order-api-v1.1.xml](/specifications/deribit-sbe-xmls/historical/deribit-sbe-order-api-v1.1.xml) |
| 1.2              | 9              | [2026-07-15](/changelogs/starbase#starbase-release-15-07-2026-—-v1-2) | [deribit-sbe-order-api-v1.2.xml](/specifications/deribit-sbe-xmls/historical/deribit-sbe-order-api-v1.2.xml) |
| 1.3              | 11             | [2026-07-21](/changelogs/starbase#starbase-release-21-07-2026-—-v1-3) | [deribit-sbe-order-api-v1.3.xml](/specifications/deribit-sbe-xmls/historical/deribit-sbe-order-api-v1.3.xml) |
| 1.4              | 12             | [2026-08-04](/changelogs/starbase#starbase-release-04-08-2026-—-v1-4) | [deribit-sbe-order-api-v1.4.xml](/specifications/deribit-sbe-xmls/historical/deribit-sbe-order-api-v1.4.xml) |

# What is SBE?

SBE is a compact binary encoding format with fixed-width fields at fixed offsets, in contrast to standard FIX with ASCII-encoded human-readable tag=value pairs. SBE provides:

* **Minimizes latency**: Binary encoding eliminates text parsing overhead
* **Reduces bandwidth**: Compact binary representation uses less network bandwidth than text-based protocols
* **Provides type safety**: Strong typing ensures data integrity
* **Fixed offsets**: Fields are at fixed positions within each message

## Message Structure

### TCP messages

All SBE messages sent over TCP follow a consistent structure:

1. **Message Header** (32 bytes): Contains protocol identification, message type, sequence numbers, and timing information
2. **Message Body**: Contains the specific message data fields

Messages are sent over TCP connections and can be bidirectional - clients send requests and receive responses/updates on the same connection.

Each message starts with the following 32-byte header:

| Field | Name                | Type   | Length | Description                                                                                                                                                                                                                                                             |
| ----- | ------------------- | ------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | protocolId          | uint8  | 1      | Constant (= `0xDB`)                                                                                                                                                                                                                                                     |
| 2     | flags               | uint8  | 1      | Bitset of flags:<br />`0x01` = resend                                                                                                                                                                                                                                   |
| 3     | messageLength       | uint16 | 2      | Total length of message including this header and body                                                                                                                                                                                                                  |
| 4     | messageTypeId       | uint16 | 2      | Message type ID (e.g., `100` for `NewOrderRequest`)                                                                                                                                                                                                                     |
| 5     | version             | uint16 | 2      | Per-message version stamp: the newest schema version at which this message type last changed, capped at the schema version negotiated at logon. May be lower than the negotiated version — see [schema version negotiation](/starbase/session-messages#logonresponse-2) |
| 6     | sequenceNum         | int64  | 8      | Message sequence number                                                                                                                                                                                                                                                 |
| 7     | lastProcessedSeqNum | int64  | 8      | Sequence number of last message received from client when this message was sent                                                                                                                                                                                         |
| 8     | sendTime            | int64  | 8      | Time when this message was sent in nanoseconds since epoch                                                                                                                                                                                                              |

### UDP messages

Incremental, snapshot and retransmit channels share the same basic packet and message structure. Each UDP packet will start with a packet header followed by zero or more messages. Each message within the packet will start with a message header.

All messages have a sequence number, although only the sequence number of the first message in the packet is specified (in the packet header). Thus the next expected sequence number in the next packet is packet sequenceNum plus messageCount. \
Heartbeat packets will have a messageCount of 0 with the next expected sequence number. This same sequence number will be repeated with the first real message.

Each UDP packet starts with the following 24-byte packet header:

| Field | Name         | Type   | Length | Description                                                         |
| ----- | ------------ | ------ | ------ | ------------------------------------------------------------------- |
| 1     | sendTime     | int64  | 8      | Time when this message was sent in nanoseconds since epoch          |
| 2     | sequenceNum  | int64  | 8      | Message sequence number                                             |
| 3     | channelId    | int32  | 4      | Channel identifier for product group                                |
| 4     | type         | uint16 | 2      | Bitset: `1`=IncrementalUpdate<br />`2`=Snapshot<br />`4`=Retransmit |
| 5     | messageCount | uint16 | 2      | Number of messages in packet. 0 for heartbeats                      |

Each message within a packet starts with the following 16-byte header:

| Field | Name          | Type   | Length | Description                                                        |
| ----- | ------------- | ------ | ------ | ------------------------------------------------------------------ |
| 1     | messageLength | uint16 | 2      | Total length of message including this header and body             |
| 2     | messageTypeId | uint16 | 2      | Message type ID                                                    |
| 3     | version       | uint16 | 2      | Message version number                                             |
| 4     | flags         | uint16 | 2      | Bitset of flags:<br />0=startOfTransaction<br />1=endOfTransaction |
| 5     | transactTime  | int64  | 8      | Timestamp of event in matching engine. Nanoseconds since epoch     |

### Key Concepts

**Message Type ID**: Each message type has a unique `messageTypeId` (uint16) that identifies its purpose. The `messageTypeId` is located in field 4 of the message header and is used to determine how to parse and process the message body.

For example, a `NewOrderRequest` message has `messageTypeId = 100`. When the gateway receives a message with `messageTypeId = 100` in the header, it knows to parse the message body as a `NewOrderRequest` containing fields such as `clientOrderId`, `correlationId`, `limitPrice`, `amount`, etc.

**Message Types**: Each message type has a unique `messageTypeId` that identifies its purpose (e.g., `NewOrderRequest` (100), `NewOrderResponse` (200), `OrderFilled` (300)).

**Sequence Numbers**: Sequence numbers are assigned and validated like FIX sequence numbers. Every message includes sequence numbers for:

* **sequenceNum**: Sequence number of the current message
* **lastProcessedSeqNum**: Sequence number of the last message received from the client (in responses)

Sequence numbers enable:

* Message ordering verification
* Gap detection for missing messages
* Resend requests when gaps are detected (using the resend flag in the message header)

**Correlation IDs**: Order entry messages (requests, responses, rejects, and `OrderFilled`) contain an 8-byte integer `correlationId`. Clients can assign any value to `correlationId`, which is not validated by the server. However, Deribit recommends monotonically increasing the value. `correlationId` is used for matching responses to requests and for indirectly correlated messages, such as order fill and system cancel notifications. Messages from server to client use the `correlationId` of either the **corresponding request message from the client** or of the **last related request**. Market data messages (order book updates, trades, reference data) do not contain correlation IDs.

**Protocol ID**: All messages start with `protocolId = 0xDB` to identify the Deribit Starbase protocol.

### Data Types

All multi-byte fields are encoded in **little-endian** byte order.

SBE uses standard binary data types:

* **int8/int16/int32/int64**: Signed integers of various sizes
* **uint8/uint16**: Unsigned integers
* **double**: 64-bit floating point (used for prices)
* **char**: Fixed-length character arrays

In addition, Starbase uses the following custom composite types:

* **Decimal72** (also referred to as **DFP**, or Decimal Floating Point): A 9-byte variable-precision quantity encoding defined as an SBE composite of a 64-bit signed integer mantissa and an 8-bit signed integer exponent, where `value = mantissa × 10^exponent`. The variable exponent provides a wide range of precision across different underlying assets. It is used for quantities throughout the protocol.
* **QuantityMantissa**: A 64-bit signed integer (int64) representing the mantissa component of a Decimal72 quantity. Used in market data messages where only the mantissa is transmitted (8 bytes).

### Byte Alignment and Message Padding

The frame length of all outbound messages to the client is rounded up to the nearest multiple of 8. Clients are encouraged to do the same with inbound messages, although this is not required.

### Clock Synchronization

Deribit exposes **PTP (Precision Time Protocol)** to clients colocated in LD4, allowing `sendTime` and `transactTime` (both nanoseconds since epoch) to be correlated against a client's own clock. Contact <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a> for the PTP service agreement.

### Usage Workflow

1. **Connect**: Establish a TCP connection to the gateway
2. **Authenticate**: Authenticate using your API credentials
3. **Send Requests**: Send binary-encoded request messages
4. **Receive Responses**: Process binary-encoded response and update messages
5. **Handle Sequence**: Monitor sequence numbers and request resends if gaps are detected

### Order Expiration

When an order expires (e.g., a day order at the close of a trading day or when an instrument expires), an `OrderCanceled` message is sent via the unsolicited events channel.

<Note>
  **Fill Limits**: The maximum number of fills on a single order or mass quote is **2000 fills for single-leg instruments** and **400 fills for combo instruments**.
</Note>

## Rejection Reason Codes

Reject messages in the Starbase Binary API include a `reason` field that indicates why the request was rejected. The following table lists all possible rejection reason codes:

| Value | Name                               | Description                                                                                                                                                                                |
| ----- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `0`   | `SYSTEM_ERROR`                     |                                                                                                                                                                                            |
| `1`   | `INVALID_INSTRUMENT`               |                                                                                                                                                                                            |
| `2`   | `INVALID_FIELD`                    |                                                                                                                                                                                            |
| `3`   | `INSUFFICIENT_MARGIN`              |                                                                                                                                                                                            |
| `4`   | `DUPLICATE_CLIENT_ORDER_ID`        |                                                                                                                                                                                            |
| `5`   | `INVALID_QUANTITY`                 |                                                                                                                                                                                            |
| `6`   | `INVALID_PRICE`                    |                                                                                                                                                                                            |
| `7`   | `NOT_ALLOWED_BY_MARKET_STATE`      |                                                                                                                                                                                            |
| `8`   | `POST_ONLY`                        |                                                                                                                                                                                            |
| `9`   | `TOO_MANY_OPEN_ORDERS`             | Exceeded max open orders for instrument/side                                                                                                                                               |
| `10`  | `PERMISSION_ERROR`                 |                                                                                                                                                                                            |
| `11`  | `PORTFOLIO_NOT_FOUND`              |                                                                                                                                                                                            |
| `12`  | `ORDER_NOT_FOUND`                  | For replaces and engine responses                                                                                                                                                          |
| `13`  | `MMP_NOT_CONFIGURED`               |                                                                                                                                                                                            |
| `14`  | `MMP_MAX_QUOTE_QTY_EXCEEDED`       |                                                                                                                                                                                            |
| `15`  | `MMP_GROUP_FROZEN`                 |                                                                                                                                                                                            |
| `16`  | `INVALID_MARGIN_MODE`              | E.g. an options order or quote submitted against a Standard Margin (SM) portfolio, which does not support options positions                                                                |
| `17`  | `IN_LIQUIDATION`                   | Portfolio is in liquidation                                                                                                                                                                |
| `18`  | `RISK_CHECK_TIMED_OUT`             |                                                                                                                                                                                            |
| `19`  | `TOO_MANY_PENDING_REPLACES`        | Exceeded the per-order cap on unacknowledged amends: max 4 pending amends per order, 1 for OCO / reduce-only orders. See [Amending an Order](/starbase/amending-order#pending-amend-limit) |
| `20`  | `ICEBERG_NOT_ALLOWED`              |                                                                                                                                                                                            |
| `21`  | `INVALID_ALLOCATIONS`              | Block trade error                                                                                                                                                                          |
| `22`  | `PRICE_TOO_HIGH`                   | Price exceeds upper price band limit                                                                                                                                                       |
| `23`  | `PRICE_TOO_LOW`                    | Price exceeds lower price band limit                                                                                                                                                       |
| `24`  | `PRICE_BAND_UNAVAILABLE`           | No price band or mark price available                                                                                                                                                      |
| `25`  | `RATE_LIMIT`                       | Gateway rate limit exceeded                                                                                                                                                                |
| `26`  | `PORTFOLIO_LOCKED`                 | Portfolio is locked                                                                                                                                                                        |
| `27`  | `POSITION_LIMIT_EXCEEDED`          | Future or options position size limit exceeded                                                                                                                                             |
| `28`  | `ORDER_SIZE_LIMIT_EXCEEDED`        | Open order aggregate size limit exceeded                                                                                                                                                   |
| `29`  | `MEMBER_SPEED_BUMP_LIMIT_EXCEEDED` | Member has too many live speed-bumped orders                                                                                                                                               |
| `30`  | `MMP_MIN_FREEZE_TIME_NOT_ELAPSED`  | MMP minimum freeze duration not yet elapsed                                                                                                                                                |

These rejection reason codes are used in the following reject messages:

* [`NewOrderReject`](/starbase/placing-new-order#neworderreject) - Field 7 (`reason`)
* [`AmendOrderReject`](/starbase/amending-order#amendorderreject) - Field 7 (`reason`)
* [`MassQuoteResponse`](/starbase/mass-quotes#massquoteresponse) - Fields 20 (`bidRejectReason`) and 21 (`askRejectReason`)

<Note>
  `CancelOrderReject` and `MassCancelReject` use separate enumeration types with their own reason codes, documented inline in their respective message tables.
</Note>

## Cancel Reason Codes

The `cancelReason` field uses a single enumeration across all contexts, indicating why an order was (partially) canceled.

| Value | Name                      | Description                                                                                                                                                                                           |
| ----- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | `UNKNOWN`                 |                                                                                                                                                                                                       |
| `1`   | `SELF_MATCH_PREVENTION`   | Canceled due to self-match prevention                                                                                                                                                                 |
| `2`   | `TIME_IN_FORCE`           | Canceled because time-in-force condition was not met                                                                                                                                                  |
| `3`   | `ADMIN`                   | Canceled by exchange administration                                                                                                                                                                   |
| `4`   | `MM_PROTECTION`           | Canceled because MMP was triggered                                                                                                                                                                    |
| `5`   | `LIQUIDATION`             | Canceled as part of a liquidation                                                                                                                                                                     |
| `6`   | `MARKET_STATE_TRANSITION` |                                                                                                                                                                                                       |
| `7`   | `CLIENT_DISCONNECT`       |                                                                                                                                                                                                       |
| `8`   | `REDUCE_ONLY`             | The portfolio is restricted to reduce-only trading and the order would have increased a position. Reduce-only is a portfolio-level restriction applied by Deribit — it cannot be set per order in SBE |
| `9`   | `DELIVERED`               | Instrument status changed to `DELIVERED`                                                                                                                                                              |
| `10`  | `SETTLEMENT`              | Instrument entered settlement                                                                                                                                                                         |
| `11`  | `BOOK_DEACTIVATED`        | Instrument status changed to `INACTIVE`                                                                                                                                                               |
| `12`  | `BY_REQUEST`              | Canceled in response to a client mass cancel request or MMP reset                                                                                                                                     |
| `13`  | `RISK_CHECK_TIMED_OUT`    |                                                                                                                                                                                                       |
| `14`  | `MMP_GROUP_DELETED`       |                                                                                                                                                                                                       |
| `15`  | `PORTFOLIO_LOCKED`        | Order canceled because the portfolio is locked                                                                                                                                                        |
| `16`  | `POST_ONLY`               | Post-only order would have crossed                                                                                                                                                                    |
| `17`  | `QTY_TICK_SIZE_RESCALE`   | Instrument `qtyTickSize` changed and this order's quantity is not exactly representable under the new tick                                                                                            |

Used in:

* [`NewOrderResponse`](/starbase/placing-new-order#neworderresponse), Field 14 (`cancelReason`)
* [`AmendOrderResponse`](/starbase/amending-order#amendorderresponse), Field 13 (`cancelReason`)
* [`OrderPlaced`](/starbase/unsolicited-events#orderplaced-312), `cancelReason` field
* [`OrdersCanceled`](/starbase/unsolicited-events#orderscanceled-310), Field 3 (`cancelReason`)
* [`MassQuoteOrdersPlaced`](/starbase/unsolicited-events#massquoteordersplaced-314), `cancelReason` field (per quote entry)


## Related topics

- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [Multicast Retransmit Gateway](/starbase/retransmit-gateway.md)
- [Starbase Market Maker Protection (MMP)](/starbase/mmp.md)
- [Starbase Reference Data and Instrument Definitions](/starbase/reference-data.md)
