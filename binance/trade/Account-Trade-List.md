- [](/legacy-docs/)
- Options Trading
- Trade
- Account Trade List
**On this page


# Account Trade List (USER_DATA)

## API Description​

Get trades for a specific account and symbol.

## HTTP Request​

`GET /eapi/v1/userTrades (HMAC SHA256)`

## Request Weight​

5**

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES | Option symbol, e.g BTC-200730-9000-C |
| fromId | LONG | NO | Trade id to fetch from. Default gets most recent trades, e.g 4611875134427365376 |
| startTime | LONG | NO | Start time, e.g 1593511200000 |
| endTime | LONG | NO | End time, e.g 1593512200000 |
| limit | INT | NO | Default 100; max 1000 |
| recvWindow | LONG | NO | |
| timestamp | LONG | YES | |

- Only support querying trades in the past 3 months

## Response Example​

```
[
 {
 "id": 4611875134427365377, // unique id
 "tradeId": 239, // trade id
 "orderId": 4611875134427365377, // order id
 "symbol": "BTC-200730-9000-C", // option symbol
 "price": "100", // trade price
 "quantity": "1", // trade quantity
 "fee": "0", // fee(negative is fee deduction)
 "realizedProfit": "0.00000000",     // realized profit/loss
 "side": "BUY", // order side
 "type": "LIMIT", // order type
 "liquidity": "TAKER", // TAKER or MAKER
 "time": 1592465880683 // trade time
 "priceScale": 2,
 "quantityScale": 2,
 "optionSide": "CALL",
 "quoteAsset": "USDT"
 }
]

```
