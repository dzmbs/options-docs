> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trades

> Trade messages on the Starbase Binary API — Trade Summary, Trade, and Block Trade feeds with execution details and counterparty data for reporting.

## Trades

### Trade Summary (30)

This message is sent when a taker order matches against one or more maker/resting orders, followed by one or more Trade messages.

| Field | Name                | Type             | Length | Description                                            |
| ----- | ------------------- | ---------------- | ------ | ------------------------------------------------------ |
| 1     | instrumentId        | int64            | 8      | Numeric instrument ID                                  |
| 2     | takerOrderId        | int64            | 8      | Unique identifier for the taker order                  |
| 3     | totalFilledMantissa | QuantityMantissa | 8      | Total amount filled (by the taker order)               |
| 4     | deepestPrice        | Price9           | 8      | Deepest price in book matched by taker order           |
| 5     | markPrice           | Price9           | 8      | Mark price at the time of the block trade              |
| 6     | indexPrice          | Price9           | 8      | Index price at the time of the block trade             |
| 7     | tradeCount          | int32            | 4      | Number of Trade messages that will follow this message |
| 8     | takerFlags          | uint32           | 4      | Attributes of taker order, defined below               |

The table below outlines the content of field 7 (takerFlags) and field 8 (makerFlags) in Trade message:

| Bit number (from last to first) | Name                    | Description                                      |
| ------------------------------- | ----------------------- | ------------------------------------------------ |
| 1                               | isSell                  | `0`=Buy<br />`1`=Sell                            |
| 2                               | isLiquidation           | `0`=Not a liquidation<br />`1`=Liquidation trade |
| 3                               | Reserved for future use |                                                  |
| 4                               | Reserved for future use |                                                  |
| 5                               | Reserved for future use |                                                  |
| 6                               | Reserved for future use |                                                  |
| 7                               | Reserved for future use |                                                  |
| 8                               | Reserved for future use |                                                  |

### Trade (31)

This message is sent for each matched order (including implied orders) and synthetic leg for trades on combo instruments.

| Field | Name         | Type             | Length | Description                                                                                                                          |
| ----- | ------------ | ---------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | matchId      | int64            | 8      | Unique identifier of the trade                                                                                                       |
| 2     | instrumentId | int64            | 8      | Numeric instrument ID                                                                                                                |
| 3     | makerOrderId | int64            | 8      | Unique identifier for the resting order. In case of implied order or synthetic leg of a combo trade, encoded as `0x8000000000000000` |
| 4     | amount       | QuantityMantissa | 8      | Amount that was matched                                                                                                              |
| 5     | price        | Price9           | 8      | Price at which the match occurred                                                                                                    |
| 6     | makerFlags   | uint32           | 4      | See table above                                                                                                                      |

## Block Trades

### Block Trade (33)

This message is sent for each individual trade in a block trade. Multiple `Block Trade` messages belonging to the same block trade event are grouped as a transaction via the `startOfTransaction` and `endOfTransaction` flags in the message header. A block trade event is per instrument: a multi-leg block trade generates one transaction per leg. For example, a Block RFQ with 3 legs where the taker trades against 2 makers produces 3 transactions, each containing 2 `Block Trade` messages. Block RFQ trades include a `blockRfqId`; standard block trades omit it.

| Field | Name              | Type             | Length | Description                                                                                       |
| ----- | ----------------- | ---------------- | ------ | ------------------------------------------------------------------------------------------------- |
| 1     | matchId           | int64            | 8      | Unique identifier of the block trade fill                                                         |
| 2     | instrumentId      | int64            | 8      | Numeric instrument ID                                                                             |
| 3     | blockTradeId      | int64            | 8      | Per-fill block trade identifier assigned by the matching engine                                   |
| 4     | blockRfqId        | int64            | 8      | Block RFQ identifier; absent (null value) for standard block trades, present for Block RFQ trades |
| 5     | fillQtyMantissa   | QuantityMantissa | 8      | Fill quantity                                                                                     |
| 6     | fillPrice         | Price9           | 8      | Price at which the block trade occurred                                                           |
| 7     | markPrice         | Price9           | 8      | Mark price at the time of the block trade                                                         |
| 8     | indexPrice        | Price9           | 8      | Index price at the time of the block trade                                                        |
| 9     | impliedVolatility | double           | 8      | Implied volatility; absent (null value) for non-option instruments                                |
| 10    | takerFlags        | uint32           | 4      | Attributes of the taker side; see flags table in [Trades](#trades) section above                  |
| 11    | numberOfLegs      | uint16           | 2      | Total number of legs in the block trade structure                                                 |


## Related topics

- [block_trade_confirmations ](/subscriptions/block-trade/block_trade_confirmations.md)
- [private/get_block_trade](/api-reference/block-trade/private-get_block_trade.md)
- [private/execute_block_trade](/api-reference/block-trade/private-execute_block_trade.md)
- [private/get_block_trades](/api-reference/block-trade/private-get_block_trades.md)
- [private/reject_block_trade](/api-reference/block-trade/private-reject_block_trade.md)
