## WebSocket Public Channel

### Public structure block trades channel

Retrieve the recent block trades data in OKX. All the legs in the same block trade are included in the same update. The data will be pushed 15 minutes after the block trade execution.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "public-struc-block-trades"
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
 "channel": "public-struc-block-trades"
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
| > channel | String | Yes | Channel name`public-struc-block-trades` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "public-struc-block-trades"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"public-struc-block-trades\""}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Operation`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`public-struc-block-trades` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg":{
 "channel":"public-struc-block-trades"
 },
 "data":[
 {

 "cTime":"1608267227834",
 "blockTdId":"1802896",
 "groupId":"",
 "legs":[
 {
 "px":"0.323",
 "sz":"25.0",
 "instId":"BTC-USD-20220114-13250-C",
 "side":"sell",
 "tradeId":"15102"
 },
 {
 "px":"0.666",
 "sz":"25",
 "instId":"BTC-USD-20220114-21125-C",
 "side":"buy",
 "tradeId":"15103"
 }
 ]
 }
 ]
}

```

#### Push data parameters

| Parameters | Types | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| data | Array of objects | Subscribed data |
| > cTime | String | The time the trade was executed. Unix timestamp in milliseconds. |
| > blockTdId | String | Block trade ID. |
| > groupId | String | Group RFQ IDOnly applicable to group RFQ, return "" for normal RFQ |
| > legs | Array of objects | Legs of trade |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> px | String | The price the leg executed |
| >> sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| >> side | String | The direction of the leg from the Takers perspective. Valid value can be `buy` or `sell`. |
| >> tradeId | String | Last traded ID. |

Group RFQ introduction

1. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.

2. Data return by this endpoint should be at **parent RFQ level** regardless of the subaccounts allocation. blockTdId and tradeId will be empty.

Mapping blockTdId to rfqId

For normal RFQs, each `blockTdId` has a 1:1 relationship with an `rfqId`. For Group RFQs, one `rfqId` may correspond to multiple `blockTdId`s.

This channel does not include `rfqId` directly. Users who are counterparties to the trade (taker and executing maker) can subscribe to the private [Structure block trades channel](/docs-v5/en/#block-trading-websocket-private-channel-structure-block-trades-channel), which provides both `rfqId` and `blockTdId`, enabling cross-referencing between the two channels.

### Public block trades channel

Retrieve the recent block trades data by individual legs. Each leg in a block trade is pushed in a separate update. The data will be pushed 15 minutes after the block trade execution.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "public-block-trades",
 "instId": "BTC-USDT-SWAP"
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
 "channel": "public-block-trades",
 "instId": "BTC-USDT-SWAP"
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
| > channel | String | Yes | Channel name`public-block-trades` |
| > instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP. |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "public-block-trades",
 "instId": "BTC-USDT-SWAP",
 "connId": "a4d3ae55"
 }
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"public-block-trades\""}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Operation`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`public-block-trades` |
| > instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP. |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg":{
 "channel":"public-block-trades",
 "instId":"BTC-USD-231020-5000-P"
 },
 "data":[
 {
 "fillVol":"5",
 "fwdPx":"26808.16",
 "groupId":"",
 "idxPx":"27222.5",
 "instId":"BTC-USD-231020-5000-P",
 "markPx":"0.0022406326071111",
 "px":"0.0048",
 "side":"buy",
 "sz":"1",
 "tradeId":"633971452580106242",
 "ts":"1697422572972"
 }
 ]
}

```

#### Push data parameters

| Parameters | Types | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID, e.g. BTC-USDT-SWAP. |
| data | Array of objects | Information of the public trade object. |
| > instId | String | Instrument ID, e.g. BTC-USDT-SWAP. |
| > tradeId | String | Trade ID, generated by counter. |
| > px | String | The price the leg executed. |
| > sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| > side | String | Trade direction, buy, sell, from taker perspective. |
| > fillVol | String | Implied volatility Only applicable to `OPTION` |
| > fwdPx | String | Forward price Only applicable to options |
| > idxPx | String | Index price Applicable to `FUTURES`, `SWAP`, `OPTION` |
| > markPx | String | Mark price Applicable to `FUTURES`, `SWAP`, `OPTION` |
| > groupId | String | Group RFQ ID Only applicable to group RFQ, return "" for normal RFQ |
| > ts | String | Filled time, Unix timestamp format in milliseconds, e.g. 1597026383085. |

Group RFQ introduction

1. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.

2. Data return by this endpoint should be at **child RFQ execution level** but split into a single leg. tradeId will be populated.

### Block tickers channel

Retrieve the latest block trading volume in the last 24 hours.

The data will be pushed when triggered by transaction execution event. In addition, it will also be pushed in 5 minutes interval according to subscription granularity.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "block-tickers",
 "instId": "BTC-USDT"
 }]
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
 args = [{
 "channel": "block-tickers",
 "instId": "BTC-USDT"
 }]

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
| > channel | String | Yes | Channel name`block-tickers` |
| > instId | String | Yes | Instrument ID e.g. BTC-USDT-SWAP |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "block-tickers",
 "instId": "LTC-USD-200327"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"block-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`block-tickers` |
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "block-tickers"
 },
 "data": [
 {
 "instType": "SWAP",
 "instId": "LTC-USD-SWAP",
 "volCcy24h": "0",
 "vol24h": "0",
 "ts": "1597026383085"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instId | String | Instrument ID |
| > instType | String | Instrument type |
| > volCcy24h | String | 24h trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| > vol24h | String | 24h trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| > ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
