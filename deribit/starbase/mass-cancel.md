> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starbase Mass Cancel Messages

> Cancel many Starbase orders and quotes at once using MassCancelRequest, MassQuoteCancelRequest, and the currency_pair_id sourced from InstrumentDefinition.

### Mass Cancel Granularity

Mass cancels are scoped to an instrument or underlying currency pair and per side of the order book, using the fields in the `MassCancelRequest` below. There is no equivalent of a QuoteSetID for mass cancels.

Because Starbase applies a speed bump to aggressive orders, individual cancel requests can reach the matching engine ahead of incoming aggressor orders. This makes fine-grained cancellation with regular `CancelOrderRequest` messages practical without requiring a broader mass cancel.

Mass cancels are aligned with single cancels in their treatment of speed-bumped orders: both **convert** pending orders to IOC rather than removing them immediately. When the speed bump expires, the order attempts to fill as IOC and any unfilled remainder is cancelled. See [Cancelling Pending Orders](/starbase/speed-bumps#cancelling-pending-orders) for full details.

### MassCancelRequest (140)

Request to cancel all orders and quotes submitted via the binary SBE order gateway that meet the specified criteria.

<Note>
  At least one of `indexId` or `instrumentId` must be specified — the gateway rejects a `MassCancelRequest` that contains neither. Each mass cancel is routed to a single matching engine shard determined by the currency pair (an instrument ID implies its currency pair), so one request cannot span multiple currency pairs. To cancel every order across all currency pairs in a single call, use the REST [`cancel_all`](/api-reference/portfolio-management/mass-cancel) endpoint instead.
</Note>

| Field | Name          | Type  | Length | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----- | ------------- | ----- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | correlationId | int64 | 8      | Client-assigned ID                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2     | indexId       | int64 | 8      | Underlying index ID (`currencyPairId` in the SBE schema). Required unless `instrumentId` is specified. `0` matches no currency pair and results in zero cancellations. Take this value from `indexId` in the multicast [`InstrumentDefinition` (10)](/starbase/reference-data#instrumentdefinition-10) message — it is the same identifier as `index_id` in [`public/get_instruments`](/api-reference/market-data/public-get_instruments). |
| 3     | instrumentId  | int64 | 8      | Instrument ID. To cancel orders for a specific instrument, pass that instrument's ID. To cancel across all instruments of the currency pair given in `indexId`, pass `null` (not `0`). Required unless `indexId` is specified.                                                                                                                                                                                                             |
| 4     | productType   | int8  | 1      | `0`=ALL (ignore this filter)<br />`1`=Options<br />`2`=Futures (includes Perpetuals)<br />`3`=Combo Futures<br />`4`=Combo Options<br />`5`=Spot                                                                                                                                                                                                                                                                                           |
| 5     | side          | int8  | 1      | `0`=Both (ignore this filter)<br />`1`=BUY<br />`-1`=SELL                                                                                                                                                                                                                                                                                                                                                                                  |

### MassQuoteCancelRequest (145)

Request to cancel all active quotes for the specified MMP group.

| Field | Name          | Type  | Length | Description                          |
| ----- | ------------- | ----- | ------ | ------------------------------------ |
| 1     | correlationId | int64 | 8      | Client-assigned ID                   |
| 2     | mmpGroupId    | int64 | 8      | Identifier of MMP group              |
| 3     | side          | int8  | 1      | `0`=Both<br />`1`=BUY<br />`-1`=SELL |

### MassCancelResponse (240)

Acknowledges the successful execution of a `MassCancelRequest` or `MassQuoteCancelRequest`.

| Field | Name            | Type  | Length | Description                                                         |
| ----- | --------------- | ----- | ------ | ------------------------------------------------------------------- |
| 1     | transactTime    | int64 | 8      | Nanoseconds since epoch. Time of entry into the order book          |
| 2     | execId          | int64 | 8      | Exchange-assigned event ID                                          |
| 3     | correlationId   | int64 | 8      | Client-assigned ID                                                  |
| 4     | receiveTime     | int64 | 8      | Nanoseconds since epoch. Time of receipt of order on the gateway.   |
| 5     | totalOrderCount | int32 | 4      | Number of canceled orders included in the following repeating group |

### MassCancelReject (242)

Reject generated in case a `MassCancelRequest` or `MassQuoteCancelRequest` is unsuccessful.

| Field | Name          | Type  | Length | Description                                                                                                                     |
| ----- | ------------- | ----- | ------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 1     | transactTime  | int64 | 8      | Nanoseconds since epoch. Time of entry into the order book                                                                      |
| 2     | execId        | int64 | 8      | Exchange-assigned event ID                                                                                                      |
| 3     | correlationId | int64 | 8      | Client-assigned ID                                                                                                              |
| 4     | reason        | uint8 | 1      | Rejection reason code. See [Rejection Reason Codes](/starbase/binary-api-reference#rejection-reason-codes) for possible values. |
| 5     | details       | char  | 0-255  | ASCII-encoded string                                                                                                            |


## Related topics

- [Mass Quotes](/starbase/mass-quotes.md)
- [Mass Cancel](/api-reference/portfolio-management/mass-cancel.md)
- [Starbase Market Maker Protection (MMP)](/starbase/mmp.md)
- [Starbase API Changelog](/changelogs/starbase.md)
- [Cancel on Disconnect](/starbase/cancel-on-disconnect.md)
