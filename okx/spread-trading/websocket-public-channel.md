## WebSocket Public Channel

- Production Trading URL: `wss://ws.okx.com:8443/ws/v5/business`

- Demo Trading URL: `wss://wspap.okx.com:8443/ws/v5/business`

### Order book channel

Retrieve order book data. Available channels:

- `sprd-bbo-tbt`: 1 depth level snapshot will be pushed in the initial push. Snapshot data will be pushed every 10 ms when there are changes in the 1 depth level snapshot.

- `sprd-books5`: 5 depth levels snapshot will be pushed in the initial push. Snapshot data will be pushed every 100 ms when there are changes in the 5 depth levels snapshot.

- `sprd-books-l2-tbt`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time.

- The push sequence for order book channels within the same connection and trading symbols is fixed as: sprd-bbo-tbt -> sprd-books-l2-tbt -> sprd-books5.

#### URL Path

/ws/v5/business

Request Example: sprd-books5

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-books5",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
 await ws.start()
 args = [
 {
 "channel": "sprd-books5",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

Request Example: sprd-books-l2-tbt

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-books-l2-tbt",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
 await ws.start()
 args = [
 {
 "channel": "sprd-books-l2-tbt",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
| args | Array of objects | Yes | List of subscribed channels`sprd-bbo-tbt``sprd-books5``sprd-books-l2-tbt` |
| > channel | String | Yes | Channel name |
| > sprdId | String | Yes | spread ID |

Successful Response Example: sprd-books5

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "sprd-books5",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 },
 "connId": "a4d3ae55"
}

```

Successful Response Example: sprd-books-l2-tbt

```
{
 "id": "1512",
 "event":"subscribe",
 "arg":{
 "channel":"sprd-books-l2-tbt",
 "sprdId":"BTC-USDT_BTC-USDT-SWAP"
 },
 "connId":"214fdd24"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"sprd-books5\", \"sprdId\" : \"BTC-USD_BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channels`sprd-bbo-tbt``sprd-books5``sprd-books-l2-tbt` |
| > channel | String | Yes | Channel name |
| > sprdId | String | Yes | spread ID |
| msg | String | No | Error message |
| code | String | No | Error code |
| connId | String | Yes | WebSocket connection ID |

Push Data Example: sprd-books5

```
{
 "arg": {
 "channel": "sprd-books5",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 },
 "data": [
 {
 "asks": [
 ["111.06","55154","2"],
 ["111.07","53276","2"],
 ["111.08","72435","2"],
 ["111.09","70312","2"],
 ["111.1","67272","2"]],
 "bids": [
 ["111.05","57745","2"],
 ["111.04","57109","2"],
 ["111.03","69563","2"],
 ["111.02","71248","2"],
 ["111.01","65090","2"]],
 "ts": "1670324386802",
 "seqId":1724294007352168320
 }
 ]
}

```

Push Data Example: sprd-books-l2-tbt

```
{
 "arg":{
 "channel":"sprd-books-l2-tbt",
 "sprdId":"BTC-USDT_BTC-USDT-SWAP"
 },
 "action":"snapshot",
 "data":[
 {
 "asks":[
 ["1.9","1.1","3"],
 ["2.5","0.9","1"],
 ["3.2","4.921","1"],
 ["4.8","0.165","1"],
 ["5.2","4.921","1"]
 ......
 ],
 "bids":[
 ["1.8","0.165","1"],
 ["0.6","0.2","2"],
 ["0","23.49","1"],
 ["-0.1","1","1"],
 ["-0.6","1","1"],
 ["-3.9","4.921","1"]
 ......
 ],
 "ts":"1724391380926",
 "checksum":-1285595583,
 "prevSeqId":-1,
 "seqId":1724294007352168320
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > sprdId | String | spread ID |
| action | String | Push data action, incremental data or full snapshot.`snapshot`: full`update`: incremental |
| data | Array of objects | Subscribed data |
| > asks | Array of strings | Order book on sell side |
| > bids | Array of strings | Order book on buy side |
| > ts | String | Order book generation time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| > checksum | Integer | Checksum, implementation details below. Only applicable to `sprd-books-l2-tbt`. |
| > prevSeqId | Integer | Sequence ID of the last sent message. Only applicable to `sprd-books-l2-tbt`. |
| > seqId | Integer | Sequence ID of the current message, implementation details below. |

An example of the array of asks and bids values: ["411.8", "10", "4"]

- "411.8" is the depth price

- "10" is the quantity at the price (Unit: szCcy)

- "4" is the number of orders at the price.

#### Sequence ID

`seqId` is the sequence ID of the market data published. The set of sequence ID received by users is the same if users are connecting to the same channel through multiple websocket connections. Each `sprdId` has an unique set of sequence ID. Users can use `prevSeqId` and `seqId` to build the message sequencing for incremental order book updates. Generally the value of seqId is larger than prevSeqId. The `prevSeqId` in the new message matches with `seqId` of the previous message. The smallest possible sequence ID value is 0, except in snapshot messages where the prevSeqId is always -1.

Exceptions:

1. If there are no updates to the depth for an extended period, OKX will send a message with `'asks': [], 'bids': []` to inform users that the connection is still active. `seqId` is the same as the last sent message and `prevSeqId` equals to `seqId`.
2. The sequence number may be reset due to maintenance, and in this case, users will receive an incremental message with `seqId` smaller than `prevSeqId`. However, subsequent messages will follow the regular sequencing rule.

##### Example

- Snapshot message: prevSeqId = -1, seqId = 10

- Incremental message 1 (normal update): prevSeqId = 10, seqId = 15

- Incremental message 2 (no update): prevSeqId = 15, seqId = 15

- Incremental message 3 (sequence reset): prevSeqId = 15, seqId = 3

- Incremental message 4 (normal update): prevSeqId = 3, seqId = 5

#### Checksum

This mechanism can assist users in checking the accuracy of depth data.

##### Merging incremental data into full data

After subscribing to the incremental load push (such as `books` 400 levels) of Order Book Channel, users first receive the initial full load of market depth. After the incremental load is subsequently received, update the local full load.

- If there is the same price, compare the size. If the size is 0, delete this depth data. If the size changes, replace the original data.

- If there is no same price, sort by price (bid in descending order, ask in ascending order), and insert the depth information into the full load.

##### Calculate Checksum

Use the first 25 bids and asks in the full load to form a string (where a colon connects the price and size in an ask or a bid), and then calculate the CRC32 value (32-bit signed integer).

### Public Trades channel

Retrieve the recent trades data from `sprd-public-trades`. Data will be pushed whenever there is a trade. Every update contains only one trade.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-public-trades",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
 await ws.start()
 args = [
 {
 "channel": "sprd-public-trades",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
| > channel | String | Yes | Channel name`sprd-public-trades` |
| > sprdId | String | Yes | spread ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "sprd-public-trades",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-public-trades\", \"instId\" : \"BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}
```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > sprdId | String | Yes | spread ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "sprd-public-trades",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 },
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-USDT-SWAP",
 "tradeId": "2499206329160695808",
 "px": "-10",
 "sz": "0.001",
 "side": "sell",
 "ts": "1726801105519"
 }
 ]
}
```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > sprdId | String | spread ID |
| data | Array of objects | Subscribed data |
| > sprdId | String | spread ID, e.g. |
| > tradeId | String | Trade ID |
| > px | String | Trade price |
| sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| > side | String | Trade direction, buy, sell |
| > ts | String | Filled time, Unix timestamp format in milliseconds, e.g. 1597026383085 |

### Tickers channel

Retrieve the last traded price, bid price, ask price.
The fastest rate is 1 update/100ms. There will be no update if the event is not triggered. The events which can trigger update: trade, the change on best ask/bid price

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "sprd-tickers",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
 await ws.start()
 args = [
 {
 "channel": "sprd-tickers",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
| > channel | String | Yes | Channel name`sprd-tickers` |
| > sprdId | String | Yes | spread ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "sprd-tickers",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
 "connId": "a4d3ae55"
}
```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > sprdId | String | Yes | spread ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "sprd-tickers",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 },
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-USDT-SWAP",
 "last": "4",
 "lastSz": "0.01",
 "askPx": "19.7",
 "askSz": "5.79",
 "bidPx": "5.9",
 "bidSz": "5.79",
 "open24h": "-7",
 "high24h": "19.6",
 "low24h": "-7",
 "vol24h": "9.87",
 "ts": "1715247061026"
 }
 ]
}
```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > sprdId | String | spread ID |
| data | Array of objects | Subscribed data |
| > sprdId | String | spread ID |
| > last | String | Last traded price |
| > lastSz | String | Last traded size |
| > askPx | String | Best ask price |
| > askSz | String | Best ask size |
| > bidPx | String | Best bid price |
| > bidSz | String | Best bid size |
| > open24h | String | Open price in the past 24 hours |
| > high24h | String | Highest price in the past 24 hours |
| > low24h | String | Lowest price in the past 24 hours |
| > vol24h | String | 24h trading volume, with a unit of base currency or USD |
| > ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085 |

vol24h

For Spot vs USDT-margined contracts spread and USDT-margined contracts spread, the volume is with the unit of base currency; for Crypto-margined contracts spread, the volume is with the unit of USD.

### Candlesticks channel

Retrieve the candlesticks data of an instrument. The push frequency is the fastest interval 1 second push the data.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op":"subscribe",
 "args":[
 {
 "channel":"sprd-candle1D",
 "sprdId":"BTC-USDT_BTC-USDT-SWAP"
 }
 ]
}
```

```
import asyncio
from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
 await ws.start()
 args = [
 {
 "channel":"sprd-candle1D",
 "sprdId":"BTC-USDT_BTC-USDT-SWAP"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation, subscribe unsubscribe |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name `sprd-candle3M` `sprd-candle1M` `sprd-candle1W` `sprd-candle1D` `sprd-candle2D` `sprd-candle3D` `sprd-candle5D` `sprd-candle12H` `sprd-candle6H` `sprd-candle4H` `sprd-candle2H` `sprd-candle1H` `sprd-candle30m` `sprd-candle15m` `sprd-candle5m` `sprd-candle3m` `sprd-candle1m` `sprd-candle3Mutc` `sprd-candle1Mutc` `sprd-candle1Wutc` `sprd-candle1Dutc` `sprd-candle2Dutc` `sprd-candle3Dutc` `sprd-candle5Dutc` `sprd-candle12Hutc` `sprd-candle6Hutc` |
| > sprdId | String | Yes | Spread ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "sprd-candle1D",
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event, subscribe unsubscribe error |
| arg | Object | No | Subscribed channel |
| channel | String | yes | channel name |
| sprdId | String | Yes | Spread ID |
| code | String | No | Error code |
| msg | String | No | Error message |

Push Data Example

```
{
 "arg": {
 "channel": "sprd-candle1D",
 "sprdId": "BTC-USDT_BTC-USD-SWAP"
 },
 "data": [
 [
 "1597026383085",
 "8533.02",
 "8553.74",
 "8527.17",
 "8548.26",
 "45247",
 "0"
 ]
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > sprdId | String | Spread ID |
| data | Array of Arrays | Subscribed data |
| > ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| > o | String | Open price |
| > h | String | highest price |
| > l | String | Lowest price |
| > c | String | Close price |
| > vol | String | Trading volume, in szCcy |
| > confirm | String | The state of candlesticks.0 represents that it is uncompleted, 1 represents that it is completed. |

The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,confirm]
