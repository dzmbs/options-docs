> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Placing a New Order

> Submit new orders via the Starbase Binary API — NewOrderRequest, NewOrderResponse, and NewOrderReject messages with supported order types and flags.

## Placing a new order

<Info>
  **Fill Limits**: The maximum number of fills on a single order is **2000 fills for single-leg instruments** and **400 fills for combo instruments**.
</Info>

### NewOrderRequest (100)

Request to place a new order sent by the client. The order will belong to the portfolio with which the connection was authenticated. Will be followed by a `NewOrderResponse` in case the order placement is successful or by a `NewOrderReject` in case the order placement is unsuccessful. Any immediate fills will be added to the `NewOrderResponse` and will NOT be sent in an `OrderFilled`. Any consecutive unsolicited change to the order (including fills) will be sent in an `OrderFilled`.

If the order aggresses and is subject to a speed bump, the `NewOrderResponse` is sent immediately with `orderState = 4` (queued). Once the speed bump period expires and the order is entered into the book, an unsolicited `OrderPlaced` message is sent. See [Speed Bumps](/starbase/speed-bumps) for details.

<Info>
  **Null values**: Some optional fields use `NULL_LONG` / `NULL_QUANTITY` (`0x8000000000000000L`) as a sentinel to indicate "not set". For example, set `displayAmount = NULL_QUANTITY` to place a non-iceberg order, or `limitPrice = NULL_LONG` for a market order.
</Info>

| Field | Name                  | Type      | Length | Description                                                                                                                                                                                                                                                                            |
| ----- | --------------------- | --------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | clientOrderId         | int64     | 8      | Required. Numeric client order ID. Unique per portfolio.                                                                                                                                                                                                                               |
| 2     | correlationId         | int64     | 8      | Required. Client-assigned ID. Scope: per connection.                                                                                                                                                                                                                                   |
| 3     | instrumentId          | int64     | 8      | Required. Numeric instrument ID.                                                                                                                                                                                                                                                       |
| 4     | limitPrice            | Price9    | 8      | Limit price. For market orders set to `0x8000000000000000L` and use `marketLimit` flag.                                                                                                                                                                                                |
| 5     | quantity              | Decimal72 | 9      | Required. Quantity.                                                                                                                                                                                                                                                                    |
| 6     | showQty               | Decimal72 | 9      | Visible amount for iceberg orders. Setting this field to any value (including equal to `amount`) marks the order as an iceberg order. To submit a non-iceberg order, omit this field or set it to `NULL_QUANTITY`. Iceberg orders are not supported for options and combo instruments. |
| 7     | selfMatchPreventionId | int64     | 8      | SMP token. This order cannot match with any other orders within the same portfolio with the same token. `0` /null → no SMP enforcement.                                                                                                                                                |
| 8     | side                  | int8      | 1      | Required.<br />`1`=BUY<br />`-1`=SELL                                                                                                                                                                                                                                                  |
| 9     | timeInForce           | int8      | 1      | `-2`=Immediate-or-cancel<br />`-1`=Fill-or-kill<br />`0`=Good-til-cancel<br />Any number >0 will be the number of days the order will be alive, such that an order with `1` will be cancelled at the next settlement.                                                                  |
| 10    | flags                 | uint16    | 2      | See the table below.                                                                                                                                                                                                                                                                   |
| 11    | smpMode               | int8      | 1      | Required.<br />`0`=CancelTaker<br />`1`=CancelMaker<br />**Note**: if the taker order is [speed-bumped](/starbase/speed-bumps), the mode is overridden to `CancelMaker` regardless of this field.                                                                                      |

The table below outlines the content of field 10 (flags) of `NewOrderRequest`.

| Bit number (from last to first) | Name                    | Description                                                                                                                                                                                                   |
| ------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                               | cancelOnDisconnect      | Order-level cancel-on-disconnect flag.                                                                                                                                                                        |
| 1                               | postOnly                | Enables post-only that amends the order price to the best bid/ask if it would be immediately executable. The amended price is then validated against price limits. Mutually exclusive with `postOnlyReject` . |
| 2                               | postOnlyReject          | Enables post-only that rejects the order if it would be immediately executable. Mutually exclusive with `postOnly`.                                                                                           |
| 3                               | marketLimit             | Set `limitPrice` based on the top-of-book instead of the price band.                                                                                                                                          |
| 4                               | MMP                     | The order will be subject to the default Market Maker Protection group                                                                                                                                        |
| 5                               | resetMmp                | Unfreeze orders MMP group                                                                                                                                                                                     |
| 6                               | Reserved for future use |                                                                                                                                                                                                               |
| 7                               | Reserved for future use |                                                                                                                                                                                                               |

### NewOrderResponse (200)

Response to confirm a `NewOrderRequest` was successful, sent from the exchange to the client. Any immediate fills generated by the `NewOrderRequest` will be included in the `NewOrderResponse` and will NOT be sent additionally in an `OrderFilled`.

| Field | Name               | Type      | Length | Description                                                                                                                                               |
| ----- | ------------------ | --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | transactTime       | int64     | 8      | Nanoseconds since epoch. Time of entry into the order book                                                                                                |
| 2     | execId             | int64     | 8      | Exchange-assigned event ID                                                                                                                                |
| 3     | clientOrderId      | int64     | 8      | Numeric client order ID                                                                                                                                   |
| 4     | correlationId      | int64     | 8      | Client-assigned ID                                                                                                                                        |
| 5     | orderId            | int64     | 8      | Numeric exchange assigned order ID                                                                                                                        |
| 6     | instrumentId       | int64     | 8      | Numeric instrument ID                                                                                                                                     |
| 7     | limitPrice         | Price9    | 8      | Price. Can differ from submitted price when post-only (amend) is enabled                                                                                  |
| 8     | quantity           | Decimal72 | 9      | Decimal floating point amount. Can differ from submitted amount when reduce-only is enabled                                                               |
| 10    | totalFilled        | Decimal72 | 9      | Immediate fill total                                                                                                                                      |
| 11    | visibleQty         | Decimal72 | 9      | For iceberg orders this is the visible amount in the book.<br />For non-icebergs this is the remaining amount (amount - filledAmount).                    |
| 12    | side               | int8      | 1      | `1`=BUY<br />`-1`=SELL                                                                                                                                    |
| 13    | status             | int8      | 1      | `1`=Active<br />`2`=filled<br />`3`=cancelled<br />`4`=queued (speed bumped)                                                                              |
| 14    | cancelReason       | int8      | 1      | See [Cancel Reason Codes](/starbase/binary-api-reference#cancel-reason-codes)                                                                             |
| 15    | blockLengthOfFills | uint16    | 2      | 25 (bytes). Size in bytes of each fill record in the repeating group.                                                                                     |
| 16    | numberOfFills      | uint16    | 2      | Number of fills in the following repeating group.                                                                                                         |
| ->17  | matchId            | int64     | 8      | Transaction ID representing match.                                                                                                                        |
| ->18  | fillPrice          | Price9    | 8      | Price of fill                                                                                                                                             |
| ->19  | fillQty            | Decimal72 | 9      | Quantity of fill                                                                                                                                          |
| 20    | blockLengthOfLegs  | uint16    | 2      | 34 (bytes)                                                                                                                                                |
| 21    | numberOfLegs       | uint16    | 2      | Indicates the length of the following repeating group containing all combo leg quantities and prices.<br />Non-zero for trades on combo instruments only. |
| ->22  | matchId            | int64     | 8      | Transaction ID representing match.                                                                                                                        |
| ->23  | instrumentId       | int64     | 8      | Numeric instrument ID                                                                                                                                     |
| ->24  | legPrice           | Price9    | 8      | Price of this leg in the combo instrument                                                                                                                 |
| ->25  | legQty             | Decimal72 | 9      | Quantity of this leg in the combo instrument                                                                                                              |
| ->26  | legSide            | int8      | 1      | `1`=BUY<br />`-1`=SELL                                                                                                                                    |

### NewOrderReject (202)

Reject generated in case a `NewOrderRequest` is unsuccessful.

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


## Related topics

- [Market Maker Protection (MMP) API Configuration](/articles/market-maker-protection.md)
- [New Order Single(D)](/fix-api/production/new-order-single.md)
- [REST Order Gateway Authentication](/starbase/rest-authentication.md)
- [Market Maker Protection (MMP)](/starbase/mmp.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
