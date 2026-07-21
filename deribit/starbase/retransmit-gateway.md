> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multicast Retransmit Gateway

> Reference for the UDP unicast retransmit service that lets clients recover missed incremental feed messages by sequence number.

When a client detects a gap in the incremental multicast feed's sequence numbers, it can request the missing messages from the retransmit gateway. The client sends a UDP unicast `RetransmitRequest` to the gateway; the gateway serves cached SBE messages back via UDP unicast.

<Info>
  See [Multicast Channels](/starbase/multicast-channels) for the list of available feeds and their addresses. See [Multicast Subscription Guide](/starbase/multicast-subscription-guide) for connection setup.
</Info>

***

## Wire Protocol

All multi-byte values are **little-endian**.

### Packet Header

Every packet (requests and responses) begins with a 24-byte header.

| Offset | Size | Field          | Notes                                                                                           |
| ------ | ---- | -------------- | ----------------------------------------------------------------------------------------------- |
| 0      | 8    | `sendingTime`  | `int64`, nanoseconds since Unix epoch                                                           |
| 8      | 8    | `seqNum`       | `int64`; in requests, used as a client-supplied `correlationId` echoed back in reject responses |
| 16     | 4    | `channelId`    | `int32`, identifies the multicast channel                                                       |
| 20     | 2    | `packetType`   | `uint16` bitmask (see below)                                                                    |
| 22     | 2    | `messageCount` | `uint16`, number of SBE messages in this packet                                                 |

#### `packetType` Bitmask

| Bit | Hex    | Meaning       |
| --- | ------ | ------------- |
| 0   | `0x01` | `INCREMENTAL` |
| 1   | `0x02` | `SNAPSHOT`    |
| 2   | `0x04` | `RETRANSMIT`  |

A successful retransmit response sets `packetType = 0x05` (`INCREMENTAL | RETRANSMIT`). A reject response sets `packetType = 0x00`.

### SBE Message Header

Each SBE message within a packet is prefixed by a 16-byte `mdMessageHeader`:

| Field           | Type     | Description                                                       |
| --------------- | -------- | ----------------------------------------------------------------- |
| `messageLength` | `uint16` | Length of the message including this header                       |
| `templateId`    | `uint16` | SBE template ID identifying the message type                      |
| `version`       | `uint16` | Schema version                                                    |
| `flags`         | `uint16` | Bitmask: bit 0 = `startOfTransaction`, bit 1 = `endOfTransaction` |
| `transactTime`  | `int64`  | Nanoseconds since Unix epoch                                      |

```xml theme={null}
<composite name="mdMessageHeader" description="Header for each message in a packet (16 bytes)">
    <type name="messageLength"  primitiveType="uint16" description="Length of message including this header"/>
    <type name="templateId"     primitiveType="uint16"/>
    <type name="version"        primitiveType="uint16"/>
    <set name="flags"           encodingType="uint16">
        <choice name="startOfTransaction">0</choice>
        <choice name="endOfTransaction">1</choice>
    </set>
    <type name="transactTime"   primitiveType="int64" description="Nanoseconds since Unix epoch"/>
</composite>
```

The full schema XML is available to download from the [Binary API Reference](/starbase/binary-api-reference) page.

<Note>
  The gateway validates only `templateId` (must be 200) and `messageLength` (must be 25) on incoming `RetransmitRequest` packets. Other header fields are not checked.
</Note>

***

## Messages

### RetransmitRequest (template ID 200)

Sent to the gateway as a UDP unicast packet.

| Field          | Type    | Description                                    |
| -------------- | ------- | ---------------------------------------------- |
| `beginSeqNum`  | `int64` | Sequence number of the first requested message |
| `messageCount` | `uint8` | Number of messages requested (maximum 255)     |

The packet header's `seqNum` field (offset 8) carries the client's `correlationId`. Set this to any value you want echoed back on rejection.

<Warning>
  `messageCount` is a `uint8` with a maximum value of **255**. To recover more than 255 messages, issue multiple sequential requests.
</Warning>

### RetransmitReject (template ID 202)

Returned when the request cannot be fulfilled.

| Field             | Type       | Description                                                |
| ----------------- | ---------- | ---------------------------------------------------------- |
| `retryDelayNanos` | `int64`    | Minimum wait before sending the next request (nanoseconds) |
| `details`         | `char[40]` | Human-readable description                                 |
| `reason`          | `int8`     | Reject reason code (see below)                             |

#### Reject Reason Codes

| Code | Name                  | Meaning                                           |
| ---- | --------------------- | ------------------------------------------------- |
| 1    | `SEQ_TOO_LOW`         | Requested sequence is older than the cache window |
| 2    | `SEQ_TOO_HIGH`        | Requested sequence has not yet been published     |
| 3    | `RATE_LIMIT_EXCEEDED` | Client exceeded the per-IP request rate           |
| 4    | `OTHER_ERROR`         | Service not yet warmed up or other internal error |

### Successful Response

There is no separate response message type. A successful retransmit response is a normal incremental packet with `packetType = 0x05`, containing one or more SBE market data messages starting at `beginSeqNum`. The packet header's `seqNum` is set to `beginSeqNum`.

<Note>
  The gateway caps response size at **1400 bytes** (MTU limit). If the requested `messageCount` would exceed this, fewer messages are returned. Always read `messageCount` from the response packet header and issue follow-up requests for any remainder.
</Note>

***

## Correlation ID Semantics

| Scenario | `seqNum` in response header                                             |
| -------- | ----------------------------------------------------------------------- |
| Reject   | Gateway echoes the client's `correlationId` back                        |
| Success  | Set to `beginSeqNum`. The client's `correlationId` is **not** preserved |

Do not use `correlationId` to identify successful responses. Match success responses by `beginSeqNum` instead.

***

## Cache Behavior

The retransmit cache stores individual SBE message frames. Older entries are evicted as new messages arrive.

A request for a `beginSeqNum` that has been evicted receives `SEQ_TOO_LOW`.

<Note>
  `SEQ_TOO_LOW` can be returned even for a `beginSeqNum` that appears to fall within the cached range. Treat it as unrecoverable regardless of cause, as the messages are not available in the cache.
</Note>

***

## Rate Limiting

* Throttled per **source IPv4 address** (not per connection or per channel)
* Subject to a per-IP request rate limit
* Rate-limited requests receive `RetransmitReject` with `reason = RATE_LIMIT_EXCEEDED`
* The `retryDelayNanos` field in the reject specifies exactly how long to wait before retrying

<Warning>
  Rate limiting applies to the **source IP**, not individual channels. A single host sending retransmit requests across multiple channels shares one quota. Factor this in when designing multi-channel gap-fill logic.
</Warning>

***

## Client Implementation Notes

**Paging large gaps.** `messageCount` in the request is `uint8` (max 255). For gaps larger than 255, send sequential requests incrementing `beginSeqNum` by the number of messages actually received in each response.

**Check response `messageCount`.** The response may contain fewer messages than requested due to the 1400-byte MTU cap. Always read `messageCount` from the response packet header to know how many messages were returned before issuing a follow-up request.

**Match success responses by `beginSeqNum`.** Successful responses do not echo `correlationId`. If you need to correlate requests with responses, match on the `beginSeqNum` value from the response packet header's `seqNum` field.

**Handle `SEQ_TOO_LOW` as unrecoverable.** Whether the sequence is genuinely older than the cache window or the byte ring has wrapped, the result is the same: the messages are gone. Fall back to the snapshot feed to re-synchronize.

**Respect `retryDelayNanos`.** On any reject, wait at least the specified delay before retrying. For `OTHER_ERROR`, apply a backoff because the service may be warming up.

**Retransmits are best-effort UDP.** Both the request and the response may be lost in transit. Implement a timeout and retry loop in your client. If no response arrives within your timeout, resend the request (subject to `retryDelayNanos` constraints).
