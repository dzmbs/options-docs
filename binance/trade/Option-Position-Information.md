- [](/legacy-docs/)
- Options Trading
- Trade
- Option Position Information
**On this page


# Option Position Information (USER_DATA)

## API Description​

Get current position information.

## HTTP Request​

GET `/eapi/v1/position`

## Request Weight​

5**

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | NO | Option trading pair, e.g BTC-200730-9000-C |
| recvWindow | LONG | NO | |
| timestamp | LONG | YES | |

## Response Example​

```
[
 {
 "entryPrice": "1000", // Average entry price
 "symbol": "BTC-200730-9000-C", // Option trading pair
 "side": "SHORT", // Position direction
 "quantity": "-0.1", // Number of positions (positive numbers represent long positions, negative number represent short positions)
 "markValue": "105.00138", // Current market value
 "unrealizedPNL": "-5.00138", // Unrealized profit/loss
 "markPrice": "1050.0138", // Mark price
 "strikePrice": "9000", // Strike price
 "expiryDate": 1593511200000, // Exercise time
 "priceScale": 2,
 "quantityScale": 2,
 "optionSide": "CALL", // option type
 "quoteAsset": "USDT", // quote asset
 "time": 1762872654561, // last update time
 "bidQuantity": "0.0000", // buy order qty
 "askQuantity": "0.0000" // sell order qty
 }
]

```
