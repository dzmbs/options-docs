> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Maintaining the order book

> Maintain order books using the Starbase Binary API including Buy Put, Sell Put, Buy Amount Reduced, Sell Amount Reduced, and Order Delete messages.

Position in the price-time priority queue is explicitly stated and can be tracked using the `sortOrderId`. Snapshots are disseminated starting with the first-to-execute order, in sequence of execution priority. Priority should *never* be inferred from message sequence and should be taken from `sortOrderId` as speed bumped orders and certain risk-checked orders will be assigned priority some time before they are disseminated.

<Info>
  Every matching engine event that changes the book — including an order that is added and then cancelled within the same instant — generates messages on this feed (e.g. a `Buy Put`/`Sell Put` followed by an `Order Delete`). Starbase publishes market-by-order (L3) data only; there is no separate Level 2 (aggregated price-level) feed.
</Info>

## Heartbeat messages

A heartbeat message will be sent as an empty packet (0 messages). The heartbeat interval is 5 seconds and will be sent when the interval has elapsed since the last send. The packet will contain the current sequence number. This ensures that the sequence number stream is alive even when there are no market data changes.

## Incremental messages

### Buy Put (20)

This message is sent when a new buy order is placed, an existing buy order is partially executed or an existing buy order is amended. The order specified by a `Buy Put` moves to the back of the price level queue.

| Field | Name         | Type             | Length | Description                                                                                               |
| ----- | ------------ | ---------------- | ------ | --------------------------------------------------------------------------------------------------------- |
| 1     | orderId      | int64            | 8      | Numeric exchange assigned order ID                                                                        |
| 2     | instrumentId | int64            | 8      | Numeric instrument ID                                                                                     |
| 3     | quantity     | QuantityMantissa | 8      | It represents the requested order's visible quantity                                                      |
| 4     | price        | Price9           | 8      | The price of the order or quote                                                                           |
| 5     | sortOrderId  | int64            | 8      | Used to indicate order priority within a price level. A smaller number has priority over a larger number. |

### Sell Put (21)

This message is sent when a new sell order is placed, an existing sell order is partially executed or an existing sell order is amended. The order specified by a `Sell Put` moves to the back of the price level queue.

| Field | Name         | Type             | Length | Description                                                                                               |
| ----- | ------------ | ---------------- | ------ | --------------------------------------------------------------------------------------------------------- |
| 1     | orderId      | int64            | 8      | Numeric exchange assigned order ID                                                                        |
| 2     | instrumentId | int64            | 8      | Numeric instrument ID                                                                                     |
| 3     | quantity     | QuantityMantissa | 8      | It represents the requested order's visible quantity                                                      |
| 4     | price        | Price9           | 8      | The price of the order or quote                                                                           |
| 5     | sortOrderId  | int64            | 8      | Used to indicate order priority within a price level. A smaller number has priority over a larger number. |

### Buy Amount Reduced (22)

This message is sent when the amount of an existing buy order is amended to be smaller. This does not affect the order's position in the price level queue.

| Field | Name         | Type             | Length | Description                        |
| ----- | ------------ | ---------------- | ------ | ---------------------------------- |
| 1     | orderId      | int64            | 8      | Numeric exchange assigned order ID |
| 2     | instrumentId | int64            | 8      | Numeric instrument ID              |
| 3     | quantity     | QuantityMantissa | 8      | New quantity                       |

### Sell Amount Reduced (23)

This message is sent when the amount of an existing sell order is amended to be smaller. This does not affect the order's position in the price level queue.

| Field | Name         | Type             | Length | Description                        |
| ----- | ------------ | ---------------- | ------ | ---------------------------------- |
| 1     | orderId      | int64            | 8      | Numeric exchange assigned order ID |
| 2     | instrumentId | int64            | 8      | Numeric instrument ID              |
| 3     | quantity     | QuantityMantissa | 8      | New quantity                       |

### Buy Order Delete (24)

This message is sent when a buy order is fully executed or cancelled.

| Field | Name         | Type  | Length | Description                        |
| ----- | ------------ | ----- | ------ | ---------------------------------- |
| 1     | orderId      | int64 | 8      | Numeric exchange assigned order ID |
| 2     | instrumentId | int64 | 8      | Numeric instrument ID              |

### Sell Order Delete (25)

This message is sent when a sell order is fully executed or cancelled.

| Field | Name         | Type  | Length | Description                        |
| ----- | ------------ | ----- | ------ | ---------------------------------- |
| 1     | orderId      | int64 | 8      | Numeric exchange assigned order ID |
| 2     | instrumentId | int64 | 8      | Numeric instrument ID              |

## Snapshot messages

Snapshots are made up of `Buy Put (21)`  and `Sell Put (21)`  messages. Each snapshot for an instruments starts with `SnapshotHeader (100)`  and ends with `SnapshotTrailer (101)`. After all snapshots have been sent, a `EndOfCycle (119)` message is sent.

### SnapshotHeader (100)

| Field | Name                 | Type  | Length | Description                                                                              |
| :---- | :------------------- | :---- | :----- | :--------------------------------------------------------------------------------------- |
| 1     | instrumentId         | int64 | 8      | Numeric instrument ID                                                                    |
| 2     | incrementalTimestamp | int64 | 8      | Nanoseconds since epoch. Timestamp of last incremental update included in this snapshot. |
| 3     | incrementalSeqNum    | int64 | 8      | Sequence number of last incremental update included in this snapshot                     |

### SnapshotTrailer (101)

| Field | Name                 | Type  | Length | Description                                                                              |
| :---- | :------------------- | :---- | :----- | :--------------------------------------------------------------------------------------- |
| 1     | instrumentId         | int64 | 8      | Numeric instrument ID                                                                    |
| 2     | incrementalTimestamp | int64 | 8      | Nanoseconds since epoch. Timestamp of last incremental update included in this snapshot. |
| 3     | incrementalSeqNum    | int64 | 8      | Sequence number of last incremental update included in this snapshot                     |

### EndOfCycle (119)

| Field | Name                  | Type  | Length | Description                        |
| :---- | :-------------------- | :---- | :----- | :--------------------------------- |
| 1     | activeInstrumentCount | int32 | 4      | Total number of active instruments |


## Related topics

- [public/get_order_book](/api-reference/market-data/public-get_order_book.md)
- [public/get_order_book_by_instrument_id](/api-reference/market-data/public-get_order_book_by_instrument_id.md)
- [Options Data Collection](/articles/options-data-collection-best-practices.md)
- [Notifications](/articles/notifications.md)
- [FIX Drop Copy API](/starbase/fix-drop-copy-api.md)
