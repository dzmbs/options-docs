- [](/docs/)
- Options Trading
- FAQ
- Self Trade Prevention
**On this page


# Self Trade Prevention (STP) FAQ

## What is Self Trade Prevention?​

Self Trade Prevention (or STP) prevents orders of users, or the user's `tradeGroupId` to match against their own.

## What defines a self-trade?​

A self-trade can occur in either scenario:

The order traded against the same account.
The order traded against an account with the same `tradeGroupId`.

## What happens when STP is triggered?​

There are three possible modes for what the system will do if an order could create a self-trade.
`EXPIRE_TAKER` - This mode prevents a trade by immediately expiring the taker order's remaining quantity.
`EXPIRE_MAKER` - This mode prevents a trade by immediately expiring the potential maker order's remaining quantity.
`EXPIRE_BOTH` - This mode prevents a trade by immediately expiring both the taker and the potential maker orders' remaining quantities.
The STP event will occur depending on the STP mode of the taker order**. **Thus, the STP mode of an order that goes on the book is no longer relevant and will be ignored for all future order processing.

## Where do I set STP mode for an order?​

STP can only be set using field `selfTradePreventionMode` through API endpoints below:

POST `/eapi/v1/order`
POST `/eapi/v1/batchOrders`

## What is a Trade Group Id?​

Different accounts with the same `tradeGroupId` are considered part of the same "trade group". Orders submitted by members of a trade group are eligible for STP according to the taker-order's STP mode.
A user can confirm if their accounts are under the same `tradeGroupId` from the API either from `GET /eapi/v1/accountConfig` (REST API).
If the value is `-1`, then the `tradeGroupId` has not been set for that account, so the STP may only take place between orders of the same account.
Users can group sub-accounts to the same tradeGroupId via the Sub-Account API Management page.

## How do I know which symbol uses STP?​

Placing orders on all symbols in `GET /eapi/v1/exchangeInfo` can set `selfTradePreventionMode`.

## What order types support STP?​

All orders support STP when Time in Force (timeInForce) is set to `GTC`/ `IOC`/ `GTD`.
STP won't take effect for Time in force(timeInForce) `FOK` or `GTX`

## How do I know if an order expired due to STP?​

The order will have the status `EXPIRED_IN_MATCH`.
In user data stream event `ORDER_TRADE_UPDATE`, field `X` would be `EXPIRED_IN_MATCH` if order is expired due to STP

```
{ "e":"ORDER_TRADE_UPDATE", // Event Type "E":1568879465651, // Event Time "T":1568879465650, // Transaction Time "o":{ "s":"BTC-260228-70000-C", // Symbol "c":"TEST", // Client Order Id // special client order id: // starts with "autoclose-": liquidation order // "adl_autoclose": ADL auto close order // "settlement_autoclose-": settlement order for delisting or delivery "S":"SELL", // Side "o":"TRAILING_STOP_MARKET", // Order Type "f":"GTC", // Time in Force "q":"0.001", // Original Quantity "p":"0", // Original Price "ap":"0", // Average Price "sp":"7103.04", // Stop Price. Please ignore with TRAILING_STOP_MARKET order "x":"EXPIRED", // Execution Type "X":"EXPIRED_IN_MATCH", // Order Status "i":8886774, // Order Id "l":"0", // Order Last Filled Quantity "z":"0", // Order Filled Accumulated Quantity "L":"0", // Last Filled Price "N":"USDT", // Commission Asset, will not push if no commission "n":"0", // Commission, will not push if no commission "T":1568879465650, // Order Trade Time "t":0, // Trade Id "b":"0", // Bids Notional "a":"9.91", // Ask Notional "m":false, // Is this trade the maker side? "R":false, // Is this reduce only "wt":"CONTRACT_PRICE", // Stop Price Working Type "ot":"TRAILING_STOP_MARKET", // Original Order Type "ps":"LONG", // Position Side "cp":false, // If Close-All, pushed with conditional order "AP":"7476.89", // Activation Price, only pushed with TRAILING_STOP_MARKET order "cr":"5.0", // Callback Rate, only pushed with TRAILING_STOP_MARKET order "pP": false, // ignore "si": 0, // ignore "ss": 0, // ignore "rp":"0", // Realized Profit of the trade "V": "EXPIRE_MAKER", // selfTradePreventionMode "pm":"QUEUE", // price match type "gtd":1768879465650 // good till date }}
```

## STP Examples:​

For all these cases, assume that all orders for these examples are made on the same account.
Scenario A- A user sends an order with `EXPIRE_MAKER` that would match with their orders that are already on the book.**

```
Maker Order 1: symbol=BTC-260228-70000-C side=BUY type=LIMIT quantity=1 price=51 selfTradePreventionMode=EXPIRE_MAKER**Taker Order 1: symbol=BTC-260228-70000-C side=SELL type=LIMIT quantity=2 price=50 selfTradePreventionMode=EXPIRE_MAKER
```

Result**: The order that was on the book will expire due to STP, and the taker order will go on the book.

Maker Order

```
{**"orderId":4611875134427365378, "symbol": "BTC-260228-70000-C", "status": "EXPIRED_IN_MATCH", "clientOrderId": "testMaker1", "price": "51", "avgPrice": "0.0000", "origQty": "1", "executedQty": "0", "cumQuote": "0", "timeInForce": "GTC", "type": "LIMIT", "reduceOnly": false, "closePosition": false, "side": "BUY", "positionSide": "BOTH", "stopPrice": "0", "workingType": "CONTRACT_PRICE", "priceMatch": "NONE", "selfTradePreventionMode": "EXPIRE_MAKER", "goodTillDate": "null", "priceProtect": false, "origType": "LIMIT", "time": 1692849639460, "updateTime": 1692849639460}
```

Output of the Taker Order

```
{ "orderId":4611875134427365379, "symbol": "BTC-260228-70000-C", "status": "FILLED", "clientOrderId": "testTaker1", "price": "50", "avgPrice": "50", "origQty": "2", "executedQty": "2", "cumQuote": "50", "timeInForce": "GTC", "type": "LIMIT", "reduceOnly": false, "closePosition": false, "side": "SELL", "positionSide": "BOTH", "stopPrice": "0", "workingType": "CONTRACT_PRICE", "priceMatch": "NONE", "selfTradePreventionMode": "EXPIRE_MAKER", "goodTillDate": "null", "priceProtect": false, "origType": "LIMIT", "time": 1692849639460, "updateTime": 1692849639460}
```

Scenario B - A user sends an order with `EXPIRE_TAKER` that would match with their orders already on the book.**

```
Maker Order 1: symbol=BTC-260228-70000-C side=BUY type=LIMIT quantity=1 price=51 selfTradePreventionMode=EXPIRE_TAKER**Taker Order 1: symbol=BTC-260228-70000-C side=SELL type=LIMIT quantity=2 price=50 selfTradePreventionMode=EXPIRE_TAKER
```

Result**: The orders already on the book will remain, while the taker order will expire.

Maker Order

```
{**"orderId":4611875134427365378, "symbol": "BTC-260228-70000-C", "status": "NEW", "clientOrderId": "testMaker1", "price": "51", "avgPrice": "0.0000", "origQty": "1", "executedQty": "0", "cumQuote": "0", "timeInForce": "GTC", "type": "LIMIT", "reduceOnly": false, "closePosition": false, "side": "BUY", "positionSide": "BOTH", "stopPrice": "0", "workingType": "CONTRACT_PRICE", "priceMatch": "NONE", "selfTradePreventionMode": "EXPIRE_TAKER", "goodTillDate": "null", "priceProtect": false, "origType": "LIMIT", "time": 1692849639460, "updateTime": 1692849639460}
```

Output of the Taker order

```
{ "orderId":4611875134427365379, "symbol": "BTC-260228-70000-C", "status": "EXPIRED_IN_MATCH", "clientOrderId": "testTaker1", "price": "50", "avgPrice": "0.0000", "origQty": "2", "executedQty": "0", "cumQuote": "0", "timeInForce": "GTC", "type": "LIMIT", "reduceOnly": false, "closePosition": false, "side": "SELL", "positionSide": "BOTH", "stopPrice": "0", "workingType": "CONTRACT_PRICE", "priceMatch": "NONE", "selfTradePreventionMode": "EXPIRE_TAKER", "goodTillDate": "null", "priceProtect": false, "origType": "LIMIT", "time": 1692849639460, "updateTime": 1692849639460}
```

Scenario C- A user has an order on the book, and then sends an order with `EXPIRE_BOTH` that would match with the existing order.**

```
Maker Order: symbol=BTC-260228-70000-C side=BUY type=LIMIT quantity=1 price=51 selfTradePreventionMode=EXPIRE_BOTH**Taker Order: symbol=BTC-260228-70000-C side=SELL type=LIMIT quantity=3 price=50 selfTradePreventionMode=EXPIRE_BOTH
```

Result**: Both orders will expire.

Maker Order

```
{
 "orderId":4611875134427365378,
 "symbol": "BTC-260228-70000-C",
 "status": "EXPIRED_IN_MATCH",
 "clientOrderId": "testMaker1",
 "price": "51",
 "avgPrice": "0.0000",
 "origQty": "1",
 "executedQty": "0",
 "cumQuote": "0",
 "timeInForce": "GTC",
 "type": "LIMIT",
 "reduceOnly": false,
 "closePosition": false,
 "side": "BUY",
 "positionSide": "BOTH",
 "stopPrice": "0",
 "workingType": "CONTRACT_PRICE",
 "priceMatch": "NONE",
 "selfTradePreventionMode": "EXPIRE_BOTH",
 "goodTillDate": "null",
 "priceProtect": false,
 "origType": "LIMIT",
 "time": 1692849639460,
 "updateTime": 1692849639460
}

```

Taker Order

```
{
 "orderId":4611875134427365379,
 "symbol": "BTC-260228-70000-C",
 "status": "EXPIRED_IN_MATCH",
 "clientOrderId": "testTaker1",
 "price": "50",
 "avgPrice": "0.0000",
 "origQty": "3",
 "executedQty": "0",
 "cumQuote": "0",
 "timeInForce": "GTC",
 "type": "LIMIT",
 "reduceOnly": false,
 "closePosition": false,
 "side": "SELL",
 "positionSide": "BOTH",
 "stopPrice": "0",
 "workingType": "CONTRACT_PRICE",
 "priceMatch": "NONE",
 "selfTradePreventionMode": "EXPIRE_BOTH",
 "goodTillDate": "null",
 "priceProtect": false,
 "origType": "LIMIT",
 "time": 1692849639460,
 "updateTime": 1692849639460
}

```
