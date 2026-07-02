- [](/legacy-docs/)
- Options Trading
- Market Data
- Order Book
On this page


# Order Book

## API Description​

Check orderbook depth on specific symbol

## HTTP Request​

GET `/eapi/v1/depth`

## Request Weight​

| limit | weight |
| --- | --- |
| 5, 10, 20, 50 | 1 |
| 100 | 5 |
| 500 | 10 |
| 1000 | 20 |

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES | Option trading pair, e.g BTC-200730-9000-C |
| limit | INT | NO | Default:100 Max:1000.Optional value:[10, 20, 50, 100, 500, 1000] |

## Response Example​

```
{
 "bids": [ // Buy order
 [
 "1000.000", // Price
 "0.1000" // Quantity
 ]
 ],
 "asks": [ // Sell order
 [
 "1900.000", // Price
 "0.1000" // Quantity
 ]
 ],
 "T": 1762780909676, // transaction time
 "lastUpdateId": 361 // update id
}

```
