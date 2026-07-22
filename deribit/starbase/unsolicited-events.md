> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unsolicited Events

> Server-initiated events on the Starbase Binary API — OrderFilled notifications and MMPTrigger messages that require no client request or ack.

## Unsolicited events

Unsolicited events are sent by the exchange when activity occurs on your resting orders or quotes without you directly requesting it — for example, fills as a maker, system cancellations, or MMP triggers.

<Note>
  **Maker vs. taker fills**: `OrderFilled` unsolicited events are only sent to the **maker**. If your order or quote was the aggressor (taker), all fill information is returned directly on the acknowledgement message (`NewOrderResponse`, `AmendOrderResponse`, or `MassQuoteResponse`). You will not receive a separate `OrderFilled` event for taker fills.
</Note>

### OrderFilled (300)

Event generated when one or more resting orders are filled by a taker order. This may include orders from different instruments if the taker order was for a combo instrument and matched an implied order.

| Field | Name               | Type      | Length | Description                                                                                                                                               |
| ----- | ------------------ | --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | transactTime       | int64     | 8      | Nanoseconds since echo. Time of entry into the order book                                                                                                 |
| 2     | execId             | int64     | 8      | Exchange-assigned event ID                                                                                                                                |
| 3     | blockLengthOfFills | uint16    | 2      | 60 (bytes)                                                                                                                                                |
| 4     | numberOfFills      | uint16    | 2      | Indicates the length of the following repeating group containing all immediate fills when the order was submitted                                         |
| ->5   | clientOrderId      | int64     | 8      | Numeric client order ID. Set to the `quoteId` if the order was submitted as part of a `MassQuote`                                                         |
| ->6   | orderId            | int64     | 8      | Numeric exchange assigned order ID                                                                                                                        |
| ->7   | instrumentId       | int64     | 8      | Numeric instrument ID                                                                                                                                     |
| ->8   | matchId            | int64     | 8      | Transaction ID representing match, shared by all fills within match                                                                                       |
| ->9   | fillPrice          | Price9    | 8      | Price of fill                                                                                                                                             |
| ->10  | fillQty            | Decimal72 | 9      | Quantity of fill                                                                                                                                          |
| ->11  | totalFilled        | Decimal72 | 9      | Cumulative amount filled                                                                                                                                  |
| ->12  | side               | int8      | 1      | `1`=BUY<br />`-1`=SELL                                                                                                                                    |
| ->13  | flags              | uint8     | 1      | Defined in following table                                                                                                                                |
| 14    | blockLengthOfLegs  | uint16    | 2      | 34 (bytes)                                                                                                                                                |
| 15    | numberOfLegs       | uint16    | 2      | Indicates the length of the following repeating group containing all combo leg quantities and prices.<br />Non-zero for trades on combo instruments only. |
| ->16  | matchId            | int64     | 8      | Transaction ID representing match.                                                                                                                        |
| ->17  | instrumentId       | int64     | 8      | Numeric instrument ID.                                                                                                                                    |
| ->18  | legPrice           | Price9    | 8      | Price of this leg in the combo instrument                                                                                                                 |
| ->19  | legQuantity        | Decimal72 | 9      | Quantity of this leg in the combo instrument                                                                                                              |
| ->20  | legSide            | int8      | 1      | `1`=BUY<br />`-1`=SELL                                                                                                                                    |

The table below outlines the content of field 13 (flags).

| Bit number (from last to first) | Name                    | Description                              |
| ------------------------------- | ----------------------- | ---------------------------------------- |
| 1                               | isQuote                 | `0`=False (order)<br />`1`=True (quote)  |
| 2                               | isFullyFilled           | `0`=PartiallyFilled<br />`1`=FullyFilled |
| 3                               | Reserved for future use |                                          |
| 4                               | Reserved for future use |                                          |
| 5                               | Reserved for future use |                                          |
| 6                               | Reserved for future use |                                          |
| 7                               | Reserved for future use |                                          |
| 8                               | Reserved for future use |                                          |

### OrdersCanceled (310)

Event generated when one or more orders and/or quotes submitted via this binary API session are canceled for some reason other than in direct response to a client request (NewOrderRequest, AmendOrderRequest, CancelOrderRequest, MassQuoteRequest). For example, due to end-of-day expiries, liquidation, admin action, or as part of a mass cancel request or MMP trigger event.

| Field | Name                | Type      | Length | Description                                                                   |
| ----- | ------------------- | --------- | ------ | ----------------------------------------------------------------------------- |
| 1     | transactTime        | int64     | 8      | Nanoseconds since epoch. Time of entry into the order book                    |
| 2     | execId              | int64     | 8      | Exchange-assigned event ID                                                    |
| 3     | flags               | uint8     | 1      | `0`=isLastMessage                                                             |
| 4     | blockLengthOfOrders | uint16    | 2      | 35 (bytes)                                                                    |
| 5     | numberOfOrders      | uint16    | 2      | Length of the following repeating group of canceled orders                    |
| ->6   | clientOrderId       | int64     | 8      | Numeric client order ID                                                       |
| ->7   | orderId             | int64     | 8      | Numeric exchange assigned order ID                                            |
| ->8   | instrumentId        | int64     | 8      | Numeric instrument ID                                                         |
| ->9   | totalFilled         | Decimal72 | 9      | Filled quantity of canceled order                                             |
| ->10  | cancelReason        | int8      | 1      | See [Cancel Reason Codes](/starbase/binary-api-reference#cancel-reason-codes) |
| ->11  | flags               | uint8     | 1      | `1`=isQuote                                                                   |

### OrderPlaced (312)

Unsolicited event sent when a speed-bumped order completes the speed bump period and is entered into the book. Sent to the session that originally submitted the order. When the order matches immediately upon book entry, `numberOfFills` is greater than 0 and the fills repeating group is populated.

| Field | Name               | Type      | Length | Description                                                                                                                                               |
| ----- | ------------------ | --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | transactTime       | int64     | 8      | Nanoseconds since epoch. Time of entry into the order book                                                                                                |
| 2     | execId             | int64     | 8      | Exchange-assigned event ID                                                                                                                                |
| 3     | clientOrderId      | int64     | 8      | Numeric client order ID                                                                                                                                   |
| 4     | orderId            | int64     | 8      | Numeric exchange assigned order ID                                                                                                                        |
| 5     | instrumentId       | int64     | 8      | Numeric instrument ID                                                                                                                                     |
| 6     | limitPrice         | Price9    | 8      | Price at which the order was placed in the book                                                                                                           |
| 7     | quantity           | Decimal72 | 9      | Quantity                                                                                                                                                  |
| 8     | totalFilled        | Decimal72 | 9      | Total quantity filled upon book entry. `0` if no immediate fills                                                                                          |
| 9     | visibleQty         | Decimal72 | 9      | Amount currently visible in market data                                                                                                                   |
| 10    | status             | int8      | 1      | `1`=Active<br />`2`=Filled<br />`3`=Cancelled (if cancelled during the speed bump period)                                                                 |
| 11    | cancelReason       | int8      | 1      | See [Cancel Reason Codes](/starbase/binary-api-reference#cancel-reason-codes)                                                                             |
| 12    | correlationId      | int64     | 8      | `correlationId` from the originating `NewOrderRequest`                                                                                                    |
| 13    | blockLengthOfFills | uint16    | 2      | 25 (bytes)                                                                                                                                                |
| 14    | numberOfFills      | uint16    | 2      | Number of fills. `0` if the order entered the book without immediately matching                                                                           |
| ->15  | matchId            | int64     | 8      | Transaction ID representing match                                                                                                                         |
| ->16  | fillPrice          | Price9    | 8      | Price of fill                                                                                                                                             |
| ->17  | fillQty            | Decimal72 | 9      | Quantity of fill                                                                                                                                          |
| 18    | blockLengthOfLegs  | uint16    | 2      | 34 (bytes)                                                                                                                                                |
| 19    | numberOfLegs       | uint16    | 2      | Indicates the length of the following repeating group containing all combo leg quantities and prices.<br />Non-zero for trades on combo instruments only. |
| ->20  | matchId            | int64     | 8      | Transaction ID representing match.                                                                                                                        |
| ->21  | instrumentId       | int64     | 8      | Numeric instrument ID                                                                                                                                     |
| ->22  | legPrice           | Price9    | 8      | Price of this leg in the combo instrument                                                                                                                 |
| ->23  | legQty             | Decimal72 | 9      | Quantity of this leg in the combo instrument                                                                                                              |
| ->24  | legSide            | int8      | 1      | `1`=BUY<br />`-1`=SELL                                                                                                                                    |

<Note>
  `correlationId` (field 12) and the 3-byte alignment padding preceding it were added in schema version `8`; earlier versions of this message did not carry a `correlationId`.
</Note>

### MassQuoteOrdersPlaced (314)

Unsolicited event sent when one or more speed-bumped quote sides complete the speed bump period and are entered into the book. Sent to the session that originally submitted the `MassQuoteRequest`.

| Field | Name                | Type      | Length | Description                                                                                                                                                               |
| ----- | ------------------- | --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | transactTime        | int64     | 8      | Nanoseconds since epoch. Time of entry into the order book                                                                                                                |
| 2     | execId              | int64     | 8      | Exchange-assigned event ID                                                                                                                                                |
| 3     | quoteId             | int64     | 8      | Numeric client quote ID from the originating `MassQuoteRequest`                                                                                                           |
| 4     | mmpGroupId          | int64     | 8      | Identifier of MMP group                                                                                                                                                   |
| 5     | blockLengthOfQuotes | uint16    | 2      | 44 (bytes)                                                                                                                                                                |
| 6     | numberOfQuotes      | uint16    | 2      | Number of placed quote entries in this message                                                                                                                            |
| ->7   | instrumentId        | int64     | 8      | Numeric instrument ID                                                                                                                                                     |
| ->8   | buyOrderId          | int64     | 8      | Numeric exchange assigned order ID for buy side, or `0` if not placed                                                                                                     |
| ->9   | sellOrderId         | int64     | 8      | Numeric exchange assigned order ID for sell side, or `0` if not placed                                                                                                    |
| ->10  | buyPrice            | Price9    | 8      | Limit price of buy side                                                                                                                                                   |
| ->11  | sellPrice           | Price9    | 8      | Limit price of sell side                                                                                                                                                  |
| ->12  | buyAmount           | Decimal72 | 9      | Remaining buy amount                                                                                                                                                      |
| ->13  | sellAmount          | Decimal72 | 9      | Remaining sell amount                                                                                                                                                     |
| ->14  | buyQuoteStatus      | int8      | 1      | `0`=Inactive<br />`1`=Unmodified<br />`2`=QuantityReduced<br />`3`=Updated<br />`4`=Filled<br />`5`=CanceledByRequest<br />`6`=CanceledByMmp<br />`7`=CanceledBySelfMatch |
| ->15  | sellQuoteStatus     | int8      | 1      | Refer to buyQuoteStatus for possible values                                                                                                                               |

### MassQuoteMmpTriggered (320)

Event generated when a mass quote Market Maker Protection limit is triggered. Followed by one or more OrderCanceled messages..

| Field | Name          | Type   | Length | Description                                                                     |
| ----- | ------------- | ------ | ------ | ------------------------------------------------------------------------------- |
| 1     | transactTime  | int64  | 8      | Nanoseconds since echo. Time of trigger in the order book                       |
| 2     | execId        | int64  | 8      | Exchange-assigned event ID                                                      |
| 3     | mmpGroupId    | int64  | 8      | Identifier of MMP group                                                         |
| 4     | frozenUntil   | int64  | 8      | Nanoseconds since epoch                                                         |
| 5     | quantityLevel | double | 8      | The total traded quantity, within a given interval, at the time of the trigger  |
| 6     | vegaLevel     | double | 8      | The change in vega exposure within a given interval, at the time of the trigger |
| 7     | deltaLevel    | double | 8      | The change in delta within a given interval, at the time of the trigger         |
| 8     | trigger       | int8   | 1      | 0=quantity<br />1=delta<br />2=vega                                             |

### OrdersMmpTriggered (322)

Event generated when an orders Market Maker Protection limit is triggered. Followed by one or OrderCanceled messages.

| Field | Name          | Type   | Length | Description                                                                                           |
| ----- | ------------- | ------ | ------ | ----------------------------------------------------------------------------------------------------- |
| 1     | transactTime  | int64  | 8      | Nanoseconds since echo. Time of trigger in the order book                                             |
| 2     | execId        | int64  | 8      | Exchange-assigned event ID                                                                            |
| 3     | indexId       | int64  | 8      | Numeric [index ID](https://deribit-jy-patch1.mintlify.app/api-reference/market-data/list-instruments) |
| 4     | frozenUntil   | int64  | 8      | Nanoseconds since epoch                                                                               |
| 5     | quantityLevel | double | 8      | The total traded quantity, within a given interval, at the time of the trigger                        |
| 6     | vegaLevel     | double | 8      | The change in vega exposure within a given interval, at the time of the trigger                       |
| 7     | deltaLevel    | double | 8      | The change in delta within a given interval                                                           |
| 8     | trigger       | int8   | 1      | 0=quantity<br />1=delta<br />2=vega                                                                   |

### MassQuoteMmpUnfrozen (324)

Event generated when a mass quote Market Maker Protection group is unfrozen, either in response to a reset request or because the `frozenUntil` timer elapsed.

| Field | Name          | Type  | Length | Description                                                                |
| ----- | ------------- | ----- | ------ | -------------------------------------------------------------------------- |
| 1     | transactTime  | int64 | 8      | Nanoseconds since epoch. Time of trigger in the order book                 |
| 2     | execId        | int64 | 8      | Exchange-assigned event ID                                                 |
| 3     | mmpGroupId    | int64 | 8      | Identifier of MMP group                                                    |
| 4     | correlationId | int64 | 8      | Client-assigned ID, or `0x8000000000000000` if unsolicited (timer elapsed) |

### OrdersMmpUnfrozen (326)

Event generated when an orders Market Maker Protection group is unfrozen, either in response to a reset request or because the `frozenUntil` timer elapsed.

| Field | Name          | Type  | Length | Description                                                                                           |
| ----- | ------------- | ----- | ------ | ----------------------------------------------------------------------------------------------------- |
| 1     | transactTime  | int64 | 8      | Nanoseconds since epoch. Time of trigger in the order book                                            |
| 2     | execId        | int64 | 8      | Exchange-assigned event ID                                                                            |
| 3     | indexId       | int64 | 8      | Numeric [index ID](https://deribit-jy-patch1.mintlify.app/api-reference/market-data/list-instruments) |
| 4     | correlationId | int64 | 8      | Client-assigned ID, or `0x8000000000000000` if unsolicited (timer elapsed)                            |


## Related topics

- [Speed Bumps](/starbase/speed-bumps.md)
- [Binary API Reference](/starbase/binary-api-reference.md)
- [Market Maker Protection (MMP)](/starbase/mmp.md)
- [Cancel on Disconnect](/starbase/cancel-on-disconnect.md)
- [Cancelling an Order](/starbase/cancelling-order.md)
