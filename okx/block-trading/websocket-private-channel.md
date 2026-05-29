## WebSocket Private Channel

### Rfqs channel

Retrieve the RFQs sent or received by the user. Data will be pushed whenever the user sends or receives an RFQ.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "rfqs"
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
 "channel": "rfqs"
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
| > channel | String | Yes | Channel name`rfqs` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "rfqs"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"rfqs\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Operation`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`rfqs` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg":{
 "channel":"rfqs",
 "uid": "77982378738415879"
 },
 "data":[
 {
 "cTime":"1611033737572",
 "uTime":"1611033737572",
 "traderCode":"DSK2",
 "rfqId":"22534",
 "clRfqId":"",
 "tag":"123456",
 "state":"active",
 "flowType":"",
 "validUntil":"1611033857557",
 "allowPartialExecution": false,
 "counterparties":[
 "DSK4",
 "DSK5"
 ],
 "legs":[
 {
 "instId":"BTCUSD-211208-36000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "sz":"25.0",
 "side":"buy",
 "posSide": "long",
 "tgtCcy":""
 },
 {
 "instId":"ETHUSD-211208-45000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "sz":"25.0",
 "side":"sell",
 "posSide": "long",
 "tgtCcy":""
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
| > uid | String | User Identifier |
| data | Array of objects | Subscribed data |
| > cTime | String | The timestamp the RFQ was created, Unix timestamp format in milliseconds. |
| > uTime | String | The timestamp the RFQ was updated latest, Unix timestamp format in milliseconds. |
| > state | String | The status of the RFQ. Valid values can be `active`, `canceled`, `filled`, `expired` `traded_away` or `failed`. `traded_away` only applies to Maker. |
| > counterparties | Array of Strings | The list of counterparties traderCode the RFQ was broadcasted to. |
| > validUntil | String | The timestamp the RFQ expires. Unix timestamp format in milliseconds. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker. Return empty for Maker, eg. "". |
| > tag | String | RFQ tag. The block trade associated with the RFQ will have the same tag. |
| > flowType | String | Identify the type of the RFQ. Only applicable to Makers, return "" for Takers |
| > traderCode | String | A unique identifier of taker. Empty If anonymous mode is `True`. |
| > rfqId | String | RFQ ID |
| > allowPartialExecution | Boolean | Whether the RFQ can be partially filled provided that the shape of legs stays the same. Valid value is `true` or `false`. `false` by default. |
| > legs | Array of objects | An Array of objects containing each leg of the RFQ. |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> tdMode | String | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| >> ccy | String | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| >> sz | String | Size of the leg. |
| >> side | String | The direction of the leg. Valid values can be buy or sell. |
| >> posSide | String | Position side. The default is `net` in the net mode. If not specified, return "", which is equivalent to net. It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short). Only applicable to `FUTURES`/`SWAP`. |
| >> tgtCcy | String | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default. |
| >> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |
| > groupId | String | Group RFQ ID Only applicable to group RFQ, return "" for normal RFQ |
| > acctAlloc | Array of objects | Account level allocation of the RFQ This is only applicable to the taker. |
| >> acct | String | The name of the allocated account of the RFQ. |
| >> legs | Array of objects | The allocated legs of the account. |
| >>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP" |
| >>> sz | String | The allocated size of each leg. |
| >>> tdMode | String | Trade mode |
| >>> ccy | String | Margin currency |
| >>> posSide | String | Position side |

state: pending_fill is a kind of moment state, and this channel doesn't update it.

Group RFQ introduction

1. allowPartialExecution field is always true for group RFQ for taker and maker.

2. Add a new response parameter acctAlloc with all account allocation the same as the initial request, but it is only applicable to takers.

3. Add a new response parameter groupId, applicable to both takers and makers.

4. For group RFQ state,

 1. if any allocated account is pending execution, then pending_fill

 2. otherwise,

 1. if any allocated account is filled, then filled

 2. if all allocated accounts are failed, then failed

### Quotes channel

Retrieve the Quotes sent or received by the user. Data will be pushed whenever the user sends or receives a Quote.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "quotes"
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
 "channel": "quotes"
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
| > channel | String | Yes | Channel name`quotes` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "quotes"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"quotes\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Operation`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`quotes` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg":{
 "channel":"quotes",
 "uid": "77982378738415879"
 },
 "data":[
 {
 "validUntil":"1608997227854",
 "uTime":"1608267227834",
 "cTime":"1608267227834",
 "legs":[
 {
 "px":"0.0023",
 "sz":"25.0",
 "instId":"BTC-USD-220114-25000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"sell",
 "posSide": "long",
 "tgtCcy":""

 },
 {
 "px":"0.0045",
 "sz":"25",
 "instId":"BTC-USD-220114-35000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"buy",
 "posSide": "long",
 "tgtCcy":""

 }
 ],
 "quoteId":"25092",
 "rfqId":"18753",
 "tag":"123456",
 "traderCode":"SATS",
 "quoteSide":"sell",
 "state":"canceled",
 "reason":"mmp_canceled",
 "clQuoteId":""
 }
 ]
}

```

#### Push data parameters

| Parameters | Types | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| data | Array of objects | Subscribed data |
| > cTime | String | The timestamp the Quote was created, Unix timestamp format in milliseconds. |
| > uTime | String | The timestamp the Quote was updated latest, Unix timestamp format in milliseconds. |
| > state | String | The status of the quote. Valid values can be `active` `canceled` `filled` `expired` or `failed`. |
| > reason | String | Reasons of state. Valid values can be mmp_canceled. |
| > validUntil | String | The timestamp the Quote expires. Unix timestamp format in milliseconds. |
| > rfqId | String | RFQ ID. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, just return empty string "" for Maker. |
| > quoteId | String | Quote ID |
| > clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, just return empty string "" for Taker. |
| > tag | String | Quote tag. The block trade associated with the Quote will have the same tag. |
| > traderCode | String | A unique identifier of maker. Empty If anonymous mode of Quote is `True`. |
| > quoteSide | String | Top level side of Quote. Its value can be buy or sell. |
| > legs | Array of objects | The legs of the Quote. |
| >> instId | String | The instrument name of quoted leg. |
| >> tdMode | String | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| >> ccy | String | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| >> sz | String | The size of the quoted leg in contracts or spot. |
| >> px | String | The price of the leg. |
| >> side | String | The direction of the leg. Valid values can be buy or sell. |
| >> posSide | String | Position side. The default is `net` in the net mode. If not specified, return "", which is equivalent to net. It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short). Only applicable to `FUTURES`/`SWAP`. |
| >> tgtCcy | String | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default. |
| >> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |

### Structure block trades channel

Retrieve user's block trades data. All the legs in the same block trade are included in the same update. Data will be pushed whenever there is a block trade that the user is a counterparty for.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "struc-block-trades"
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
 "channel": "struc-block-trades"
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
| > channel | String | Yes | Channel name`struc-block-trades` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "struc-block-trades"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"struc-block-trades\""}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Operation`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`struc-block-trades` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg":{
 "channel":"struc-block-trades",
 "uid": "77982378738415879"
 },
 "data":[
 {
 "cTime":"1608267227834",
 "rfqId":"18753",
 "clRfqId":"",
 "quoteId":"25092",
 "clQuoteId":"",
 "blockTdId":"180184",
 "tag":"123456",
 "tTraderCode":"ANAND",
 "mTraderCode":"WAGMI",
 "isSuccessful": true,
 "errorCode": "",
 "legs":[
 {
 "px":"0.0023",
 "sz":"25.0",
 "instId":"BTC-USD-20220630-60000-C",
 "side":"sell",
 "fee":"0.1001",
 "feeCcy":"BTC",
 "tradeId":"10211",
 "tgtCcy":""

 },
 {
 "px":"0.0033",
 "sz":"25",
 "instId":"BTC-USD-20220630-50000-C",
 "side":"buy",
 "fee":"0.1001",
 "feeCcy":"BTC",
 "tradeId":"10212",
 "tgtCcy":""

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
| > uid | String | User Identifier |
| data | Array of objects | Subscribed data |
| > cTime | String | The time the trade was executed. Unix timestamp in milliseconds. |
| > rfqId | String | RFQ ID. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, just return empty string "" for Maker. |
| > quoteId | String | Quote ID. |
| > clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, just return empty string "" for Taker. |
| > blockTdId | String | Block trade ID. |
| > tag | String | Trade tag. The block trade will have the tag of the RFQ or Quote it corresponds to. |
| > tTraderCode | String | A unique identifier of the Taker. Empty If anonymous mode of RFQ is `True`. |
| > mTraderCode | String | A unique identifier of the Maker. Empty If anonymous mode of Quote is `True`. |
| > isSuccessful | Boolean | Whether the trade is filled successfully |
| > errorCode | String | Error code for unsuccessful trades. It is "" for successful trade. |
| > legs | Array of objects | Legs of trade |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> px | String | The price the leg executed |
| >> sz | String | Size of the leg. |
| >> side | String | The direction of the leg. Valid value can be buy or sell. |
| >> tgtCcy | String | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default. |
| >> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive fee represents rebate. |
| >> feeCcy | String | Fee currency |
| >> tradeId | String | Last traded ID. |
| > acctAlloc | Array of objects | Applicable to both taker, maker |
| >> blockTdId | String | Block trade ID |
| >> errorCode | String | Error code for unsuccessful trades.It is "0" for successful trade. |
| >> acct | String | The name of the allocated account of the RFQOnly applicable to taker, return "" to makers |
| >> legs | Array of objects | The allocated legs of the account. |
| >>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP" |
| >>> sz | String | Filled size |
| >>> tradeId | String | Trade ID |
| >>> fee | String | Fee |
| >>> feeCcy | String | Fee currency |

Group RFQ introduction

1. This endpoint is at parent RFQ level and contains account allocation. For parent RFQ, we should return the actual executed size, i.e. failed execution size should not be included in the parent RFQ level.

2. For account allocation, we should include both filled and failed child RFQ but add an errorCode to indicate whether a child RFQ is filled.

3. Trade results will only be returned to group RFQ creator. Allocated subaccounts and MSAs will not see trade results. Allocated accounts are expected to get these trades through trading bills.

4. Trades data will only be returned after all child RFQs are execuated.

5. For parent RFQ isSuccessful field,

 1. it will return true if any child RFQs are filled

 2. otherwise, if all child RFQ fails, it will return false

6. Parent RFQ blockTdId or legs tradeId will be empty. However, account allocation breakdown will be offered and tradeId will be attached.
