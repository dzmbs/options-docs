> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancelling an Order

> Cancel a working order with the Starbase Binary API — CancelOrderRequest, CancelOrderResponse, and CancelOrderReject message flow and error codes.

## Cancelling an order

<Info>
  **Cross-Session Cancelling**: Orders can be cancelled from a different SBE session than the one that submitted them. For example, an order submitted on session A can be cancelled on session B.

  **Response Routing**: `CancelOrderResponse` is sent to the session that sent the `CancelOrderRequest`. The original submit session receives a cancellation notification via an unsolicited [`OrdersCanceled`](/starbase/unsolicited-events#orderscanceled-310) message.

  **Event Scoping**: An SBE connection only receives events about orders submitted through that same connection.
</Info>

### CancelOrderRequest (120)

Request to cancel an existing order by its client order ID. This message cannot cancel quotes.

| Field | Name          | Type  | Length | Description             |
| ----- | ------------- | ----- | ------ | ----------------------- |
| 1     | clientOrderId | int64 | 8      | Numeric client order ID |
| 2     | correlationId | int64 | 8      | Client-assigned ID      |
| 3     | instrumentId  | int64 | 8      | Instrument identifier   |

### CancelOrderByIdRequest (125)

Request to cancel an existing order by its exchange-assigned order ID. Use this when the `clientOrderId` is not known. This message cannot cancel quotes. Responses are the same as for `CancelOrderRequest`: a `CancelOrderResponse` (220) on success or a `CancelOrderReject` (222) on failure.

| Field | Name          | Type  | Length | Description                        |
| ----- | ------------- | ----- | ------ | ---------------------------------- |
| 1     | orderId       | int64 | 8      | Numeric exchange-assigned order ID |
| 2     | correlationId | int64 | 8      | Client-assigned ID                 |
| 3     | instrumentId  | int64 | 8      | Instrument identifier              |

### CancelOrderResponse (220)

Response to confirm a `CancelOrderRequest` was successful, sent from the exchange to the client.

| Field | Name          | Type  | Length | Description                                                              |
| ----- | ------------- | ----- | ------ | ------------------------------------------------------------------------ |
| 1     | transactTime  | int64 | 8      | Nanoseconds since epoch. Time of exit out of the order book              |
| 2     | execId        | int64 | 8      | Exchange-assigned event ID                                               |
| 3     | clientOrderId | int64 | 8      | Numeric client order ID                                                  |
| 4     | correlationId | int64 | 8      | Client-assigned ID                                                       |
| 5     | orderId       | int64 | 8      | Numeric exchange assigned order ID                                       |
| 6     | instrumentId  | int64 | 8      | Numeric instrument ID                                                    |
| 7     | receiveTime   | int64 | 8      | Nanoseconds since epoch. Time of receipt of cancellation on the gateway. |

### CancelOrderReject (222)

Reject generated in case a `CancelOrderRequest` is unsuccessful.

| Field | Name          | Type  | Length | Description                                                                                                                                                                                                                    |
| ----- | ------------- | ----- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | transactTime  | int64 | 8      | Nanoseconds since epoch. Time of entry into the order book                                                                                                                                                                     |
| 2     | execId        | int64 | 8      | Exchange-assigned event ID                                                                                                                                                                                                     |
| 3     | clientOrderId | int64 | 8      | Numeric client order ID                                                                                                                                                                                                        |
| 4     | correlationId | int64 | 8      | Client-assigned ID                                                                                                                                                                                                             |
| 5     | orderId       | int64 | 8      | Numeric exchange assigned order ID                                                                                                                                                                                             |
| 6     | instrumentId  | int64 | 8      | Numeric instrument ID                                                                                                                                                                                                          |
| 7     | reason        | int8  | 1      | `0`=Error<br />`1`=UnknownOrder<br />`2`=ClientPermissionError<br />`3`=NotAllowedByMarketState<br />`4`=CancelPending<br />`5`=InLiquidation<br />`6`=InvalidInstrument<br />`7`=TimeInForce<br />`8`=SpeedBumpConvertedToIoc |
| 8     | details       | char  | 0-255  | ASCII-encoded string                                                                                                                                                                                                           |


## Related topics

- [Order Management](/articles/order-management-best-practices.md)
- [Speed Bumps](/starbase/speed-bumps.md)
- [Order Cancel/Replace Request(G)](/fix-api/production/order-cancel-replace.md)
- [Mass Quotes Specifications](/articles/mass-quotes-specifications.md)
- [Market Maker Protection (MMP)](/starbase/mmp.md)
