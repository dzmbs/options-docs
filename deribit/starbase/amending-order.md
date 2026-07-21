> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amending an Order

> Amend existing orders using the Starbase Binary API including AmendOrderRequest, AmendOrderResponse, and AmendOrderReject messages.

## Amending an existing order

<Info>
  **Cross-Session Amending**: Orders can be amended from a different SBE session than the one that submitted them. For example, an order submitted on session A can be amended on session B.

  **Response Routing**: `AmendOrderResponse` is sent to both the session that sent the `AmendOrderRequest` and the session that originally submitted the order. All subsequent events (fills, further amends, cancels) route to the original submit session.

  **Event Scoping**: An SBE connection only receives events about orders submitted through that same connection.
</Info>

### AmendOrderRequest (110)

Request to change the modifiable fields of an existing order.

<Info>
  **Null values**: Some optional fields use `NULL_LONG` / `NULL_QUANTITY` (`0x8000000000000000L`) as a sentinel to indicate "not set". For example, set `displayAmount = NULL_QUANTITY` to keep the order non-iceberg.
</Info>

| Field | Name          | Type      | Length | Description                                                                                                                                                                                                                                                                                |
| ----- | ------------- | --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | clientOrderId | int64     | 8      | Numeric client order ID                                                                                                                                                                                                                                                                    |
| 2     | correlationId | int64     | 8      | Client-assigned ID                                                                                                                                                                                                                                                                         |
| 3     | instrumentId  | int64     | 8      | Numeric instrument ID                                                                                                                                                                                                                                                                      |
| 4     | limitPrice    | Price9    | 8      | New price                                                                                                                                                                                                                                                                                  |
| 5     | quantity      | Decimal72 | 9      | New quantity                                                                                                                                                                                                                                                                               |
| 6     | showQty       | Decimal72 | 9      | New visible amount for iceberg orders. Setting this field to any value (including equal to `amount`) marks the order as an iceberg order. To submit a non-iceberg order, omit this field or set it to `NULL_QUANTITY`. Iceberg orders are not supported for options and combo instruments. |
| 7     | flags         | uint16    | 2      | See the table below.                                                                                                                                                                                                                                                                       |

The table below outlines the content of field 7 (flags) of `AmendOrderRequest`.

| Bit number (from last to first) | Name                    | Description                                                                                                                                                                                                       |
| ------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                               | postOnly                | Enables post-only that amends the order to the best bid/ask if the edit would make it immediately executable. The amended price is then validated against price limits. Mutually exclusive with `postOnlyReject`. |
| 2                               | postOnlyReject          | Enables post-only that rejects the edit if it would make the order immediately executable. The original order remains in the book unchanged. Mutually exclusive with `postOnly` .                                 |
| 3                               | Reserved for future use |                                                                                                                                                                                                                   |
| 4                               | Reserved for future use |                                                                                                                                                                                                                   |
| 5                               | Reserved for future use |                                                                                                                                                                                                                   |
| 6                               | Reserved for future use |                                                                                                                                                                                                                   |
| 7                               | Reserved for future use |                                                                                                                                                                                                                   |
| 8                               | Reserved for future use |                                                                                                                                                                                                                   |
| 9-16                            | Reserved for future use |                                                                                                                                                                                                                   |

### AmendOrderResponse (210)

Response to confirm an `AmendOrderRequest` was successful, sent from the exchange to the client. Any immediate fills generated by the `AmendOrderRequest` will be included in the `AmendOrderResponse` and will NOT be sent additionally in an `OrderUpdate`.

If the amendment causes the order to aggress and it is speed bumped, the `AmendOrderResponse` is sent immediately with `orderState = 4` (queued). Once the speed bump period expires, an unsolicited `OrderPlaced` message is sent. See [Speed Bumps](/starbase/speed-bumps) for details.

| Field | Name               | Type      | Length | Description                                                                                                                                               |   |                                           |                                           |
| ----- | ------------------ | --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ----------------------------------------- | ----------------------------------------- |
| 1     | transactTime       | int64     | 8      | Nanoseconds since epoch. Time of entry into the order book                                                                                                |   |                                           |                                           |
| 2     | execId             | int64     | 8      | Exchange-assigned event ID                                                                                                                                |   |                                           |                                           |
| 3     | clientOrderId      | int64     | 8      | Numeric client order ID                                                                                                                                   |   |                                           |                                           |
| 4     | correlationId      | int64     | 8      | Client-assigned ID                                                                                                                                        |   |                                           |                                           |
| 5     | orderId            | int64     | 8      | Numeric exchange assigned order ID                                                                                                                        |   |                                           |                                           |
| 6     | instrumentId       | int64     | 8      | Numeric instrument ID                                                                                                                                     |   |                                           |                                           |
| 7     | limitPrice         | Price9    | 8      | Price. Can differ from submitted price when post-only (amend) is enabled                                                                                  |   |                                           |                                           |
| 8     | quantity           | Decimal72 | 9      | Quantity. Can differ from submitted quantity when reduce-only is enabled                                                                                  |   |                                           |                                           |
| 9     | totalFilled        | Decimal72 | 9      | Filled quantity                                                                                                                                           |   |                                           |                                           |
| 10    | visibleQty         | Decimal72 | 9      | Currently visible in market data                                                                                                                          |   |                                           |                                           |
| 9     | totalFilled        | Decimal72 | 9      | Filled quantity                                                                                                                                           |   |                                           |                                           |
| 10    | visibleQty         | Decimal72 | 9      | Currently visible in market data                                                                                                                          |   |                                           |                                           |
| 11    | receiveTime        | int64     | 8      | Nanoseconds since epoch. Time of receipt of order on the gateway.                                                                                         |   |                                           |                                           |
| 12    | status             | int8      | 1      | `1`=Active<br />`2`=filled<br />`3`=cancelled<br />`4`=queued (speed bumped)                                                                              |   |                                           |                                           |
| 13    | cancelReason       | int8      | 1      | See [Cancel Reason Codes](/starbase/binary-api-reference#cancel-reason-codes)                                                                             |   |                                           |                                           |
| 14    | blockLengthOfFills | uint16    | 2      | 24 (bytes)                                                                                                                                                |   |                                           |                                           |
| 15    | numberOfFills      | uint16    | 2      | Indicates the length of the following repeating group containing all immediate fills when the order was submitted                                         |   |                                           |                                           |
| ->16  | matchId            | int64     | 8      | Transaction ID representing match, shared by all fills within match                                                                                       |   |                                           |                                           |
| ->17  | fillPrice          | Price9    | 8      | Price of fill                                                                                                                                             |   |                                           |                                           |
| ->18  | fillQty            | Decimal72 | 9      | Quantity of fill                                                                                                                                          |   |                                           |                                           |
| 19    | blockLengthOfLegs  | uint16    | 2      | 33 (bytes)                                                                                                                                                |   |                                           |                                           |
| 20    | numberOfLegs       | uint16    | 2      | Indicates the length of the following repeating group containing all combo leg quantities and prices.<br />Non-zero for trades on combo instruments only. |   |                                           |                                           |
| ->21  | matchId            | int64     | 8      | Transaction ID representing match.                                                                                                                        |   |                                           |                                           |
| ->22  | instrumentId       | int64     | 8      | Numeric instrument ID.                                                                                                                                    |   |                                           |                                           |
| ->23  | legPrice           | Price9    | 8      | Price9                                                                                                                                                    | 8 | Price of this leg in the combo instrument | Price of this leg in the combo instrument |
| ->24  | legQty             | Decimal72 | 9      | Quantity of this leg in the combo instrument                                                                                                              |   |                                           |                                           |
| ->25  | legSide            | int8      | 1      | `1`=BUY<br />`-1`=SELL                                                                                                                                    |   |                                           |                                           |

### AmendOrderReject (212)

Reject generated in case an `AmendOrderRequest` is unsuccessful.

| Field | Name          | Type  | Length | Description                                                                                                                     |
| ----- | ------------- | ----- | ------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 1     | transactTime  | int64 | 8      | Nanoseconds since epoch. Time of entry into the order book                                                                      |
| 2     | execId        | int64 | 8      | Exchange-assigned event ID                                                                                                      |
| 3     | clientOrderId | int64 | 8      | Numeric client order ID                                                                                                         |
| 4     | correlationId | int64 | 8      | Client-assigned ID                                                                                                              |
| 5     | orderId       | int64 | 8      | Numeric exchange assigned order ID                                                                                              |
| 6     | instrumentId  | int64 | 8      | Numeric instrument ID                                                                                                           |
| 7     | reason        | int8  | 1      | Rejection reason code. See [Rejection Reason Codes](/starbase/binary-api-reference#rejection-reason-codes) for possible values. |
| 8     | details       | char  | 0-255  | ASCII-encoded string                                                                                                            |
