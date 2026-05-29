## WebSocket Private Channel

- Production Trading URL: `wss://ws.okx.com:8443/ws/v5/business`

- Demo Trading URL: `wss://wspap.okx.com:8443/ws/v5/business`

### Order channel

Retrieve order information from the `sprd-order` Websocket channel. Data will not be pushed when first subscribed. Data will only be pushed when triggered by events such as placing/canceling order.

#### URL Path

/ws/v5/business (required login)

Request Example : single

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-orders",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPrivateAsync import WsPrivateAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPrivateAsync(
 apiKey = "YOUR_API_KEY",
 passphrase = "YOUR_PASSPHRASE",
 secretKey = "YOUR_SECRET_KEY",
 url = "wss://ws.okx.com:8443/ws/v5/business",
 useServerTime=False
 )
 await ws.start()
 args = [
 {
 "channel": "sprd-orders",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

Request Example:

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-orders",
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPrivateAsync import WsPrivateAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPrivateAsync(
 apiKey = "YOUR_API_KEY",
 passphrase = "YOUR_PASSPHRASE",
 secretKey = "YOUR_SECRET_KEY",
 url = "wss://ws.okx.com:8443/ws/v5/business",
 useServerTime=False
 )
 await ws.start()
 args = [
 {
 "channel": "sprd-orders",
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`sprd-orders` |
| > sprdId | String | No | Spread ID |

Successful Response Example : single

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "sprd-orders",
 "sprdId": "BTC-USDT_BTC-UST-SWAP"
 },
 "connId": "a4d3ae55"
}

```

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "sprd-orders"
 },
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-orders\", \"instType\" : \"FUTURES\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | Yes | String | Event`subscribe``unsubscribe``error` |
| arg | No | Object | Subscribed channel |
| > channel | Yes | String | Channel name |
| > sprdId | No | String | Spread ID |
| code | No | String | Error code |
| msg | No | String | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example: single

```
{
 "arg": {
 "channel": "sprd-orders",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP",
 "uid": "614488474791936"
 },
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-UST-SWAP",
 "ordId": "312269865356374016",
 "clOrdId": "b1",
 "tag": "",
 "px": "999",
 "sz": "3",
 "ordType": "limit",
 "side": "buy",
 "fillSz": "0",
 "fillPx": "",
 "tradeId": "",
 "accFillSz": "0",
 "pendingFillSz": "2",
 "pendingSettleSz": "1",
 "canceledSz": "1",
 "state": "live",
 "avgPx": "0",
 "cancelSource": "",
 "uTime": "1597026383085",
 "cTime": "1597026383085",
 "code": "0",
 "msg": "",
 "reqId": "",
 "amendResult": ""
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > sprdId | String | spread ID |
| data | Array of objects | Subscribed data |
| > sprdId | String | spread ID, e.g. |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > px | String | Order price |
| > sz | String | The original order quantity, in the unit of szCcy |
| > ordType | String | Order type`market`: Market order `limit`: limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| > side | String | Order side, buy sell |
| > fillSz | String | Last trade quantity, only applicable to order updates representing successful settlement |
| > fillPx | String | Last trade price, only applicable to order updates representing successful settlement |
| > tradeId | String | Last trade ID |
| > accFillSz | String | Accumulated fill quantity |
| > pendingFillSz | String | Quantity still remaining to be filled |
| > pendingSettleSz | String | Quantity that's pending settlement |
| > canceledSz | String | Quantity canceled due order cancellations or trade rejections |
| > avgPx | String | Average filled price. If none is filled, it will return "0". |
| > state | String | Order state: `canceled` `live` `partially_filled` `filled` |
| > cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are: `0`: Order canceled by system `1`: Order canceled by user `14`: Order canceled: IOC order was partially canceled due to incompletely filled`15`: Order canceled: The order price is beyond the limit `20`: Cancel all after triggered `31`: The post-only order will take liquidity in maker orders `32`: Self trade prevention `34`: Order failed to settle due to insufficient margin `35`: Order cancellation due to insufficient margin from another order`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit. |
| > uTime | String | Update time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| > cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| > code | String | Error Code, the default is 0 |
| > msg | String | Error Message, the default is "" |
| > reqId | String | Client Request ID as assigned by the client for order amendment. "" will be returned if there is no order amendment. |
| > amendResult | String | The result of amending the order `-1`: failure `0`: success"" will be returned if there is no order amendment. |

### Trades channel

All updates relating to User's Trades are sent through the `sprd-trades` WebSocket Notifications channel.

This is a private channel and consumable solely by the authenticated user.

Updates received through the `sprd-trades` WebSocket Notification channel can include Trades being `filled` or `rejected`.

You may receive multiple notifications if an Order of yours interacts with more than one other Order.

#### URL Path

/ws/v5/business (required login)

Request Example : single

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-trades",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPrivateAsync import WsPrivateAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPrivateAsync(
 apiKey = "YOUR_API_KEY",
 passphrase = "YOUR_PASSPHRASE",
 secretKey = "YOUR_SECRET_KEY",
 url = "wss://ws.okx.com:8443/ws/v5/business",
 useServerTime=False
 )
 await ws.start()
 args = [
 {
 "channel": "sprd-trades",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

Request Example:

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-trades",
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPrivateAsync import WsPrivateAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPrivateAsync(
 apiKey = "YOUR_API_KEY",
 passphrase = "YOUR_PASSPHRASE",
 secretKey = "YOUR_SECRET_KEY",
 url = "wss://ws.okx.com:8443/ws/v5/business",
 useServerTime=False
 )
 await ws.start()
 args = [
 {
 "channel": "sprd-trades",
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`sprd-trades` |
| > sprdId | String | No | Spread ID |

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > sprdId | String | No | Spread ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "sprd-trades",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP",
 "uid": "614488474791936"
 },
 "data":[
 {
 "sprdId":"BTC-USDT-SWAP_BTC-USDT-200329",
 "tradeId":"123",
 "ordId":"123445",
 "clOrdId": "b16",
 "tag":"",
 "fillPx":"999",
 "fillSz":"3",
 "state": "filled",
 "side":"buy",
 "execType":"M",
 "ts":"1597026383085",
 "legs": [
 {
 "instId": "BTC-USDT-SWAP",
 "px": "20000",
 "sz": "3",
 "szCont": "0.03",
 "side": "buy",
 "fillPnl": "",
 "fee": "",
 "feeCcy": "",
 "tradeId": "1232342342"
 },
 {
 "instId": "BTC-USDT-200329",
 "px": "21000",
 "sz": "3",
 "szCont": "0.03",
 "side": "sell",
 "fillPnl": "",
 "fee": "",
 "feeCcy": "",
 "tradeId": "5345646634"
 },
 ]
 "code": "",
 "msg": ""
 }
 ]
}
```

#### Push Data Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > sprdId | String | spread ID |
| data | Array of objects | Subscribed data |
| > sprdId | String | spread ID |
| > tradeId | String | Trade ID |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > fillPx | String | Last filled price |
| > fillSz | String | Last filled quantity |
| > side | String | Order side, buy sell |
| > state | String | Trade state. Valid values are filled and rejected |
| > execType | String | Liquidity taker or maker `T`: taker `M`: maker |
| >ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085. |
| > legs | Array of objects | Legs of trade |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> px | String | The price the leg executed |
| >> sz | String | Size of the leg in contracts or spot. |
| >> szCont | String | Filled amount of the contract Only applicable to contracts, return "" for spot |
| >> side | String | The direction of the leg. Valid value can be `buy` or `sell`. |
| >> fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| >> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive number represents rebate. |
| >> feeCcy | String | Fee currency |
| >> tradeId | String | Traded ID in the OKX orderbook. |
| > code | String | Error Code, the default is 0 |
| > msg | String | Error Message, the default is "" |
