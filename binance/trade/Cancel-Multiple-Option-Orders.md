- [](/legacy-docs/)
- Options Trading
- Trade
- Cancel Multiple Option Orders
**On this page


# Cancel Multiple Option Orders (TRADE)

## API Description​

Cancel multiple orders.

## HTTP Request​

DELETE `/eapi/v1/batchOrders`

## Request Weight​

5**

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| symbol | STRING | YES | Option trading pair, e.g BTC-200730-9000-C |
| orderIds | LIST<LONG> | NO | Order ID, e.g [4611875134427365377,4611875134427365378] |
| clientOrderIds | LIST<STRING> | NO | User-defined order ID, e.g ["my_id_1","my_id_2"] |
| recvWindow | LONG | NO | |
| timestamp | LONG | YES | |

- At least one instance of `orderId` and `clientOrderId` must be sent.

## Response Example​

```
[
 {
 "orderId": 4611875134427365377, // System order number
 "symbol": "BTC-200730-9000-C", // Option trading pair
 "price": "100", // Order Price
 "quantity": "1", // Order Quantity
 "executedQty": "0", // Number of completed quantity
 "side": "BUY", // Buy/sell direction
 "type": "LIMIT", // Order type
 "timeInForce": "GTC", // Time in force method
 "reduceOnly": false, // Order is reduce only Y/N
 "createTime": 1592465880683, // Order Time
 "updateTime": 1566818724722, // Update time
 "status": "NEW", // Order status
 "avgPrice": "0", // Average price of completed trade
 "source": "API",
 "clientOrderId": "", // Client order ID
 "priceScale": 3,
 "quantityScale": 4,
 "optionSide": "CALL",
 "quoteAsset": "USDT",
 "mmp": false,
 "selfTradePreventionMode": "EXPIRE_MAKER" //self trading prevention mode
  }
]

```
