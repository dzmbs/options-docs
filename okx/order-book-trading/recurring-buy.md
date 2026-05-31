## Recurring Buy

Recurring buy is a strategy for investing a fixed amount in crypto at fixed intervals.
An appropriate recurring approach in volatile markets allows you to buy crypto at lower costs. [Learn more](/help/vii-recurring-buy)

The API endpoints of `Recurring buy` require authentication.

### POST / Place recurring buy order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/order-algo`

Request Example

```
POST /api/v5/tradingBot/recurring/order-algo
body
{
 "stgyName": "BTC|ETH recurring buy monthly",
 "amt":"100",
 "recurringList":[
 {
 "ccy":"BTC",
 "ratio":"0.2"
 },
 {
 "ccy":"ETH",
 "ratio":"0.8"
 }
 ],
 "period":"monthly",
 "recurringDay":"1",
 "recurringTime":"0",
 "timeZone":"8", // UTC +8
 "tdMode":"cross",
 "investmentCcy":"USDT"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| stgyName | String | Yes | Custom name for trading bot, no more than 40 characters |
| recurringList | Array of objects | Yes | Recurring buy info |
| > ccy | String | Yes | Recurring currency, e.g. `BTC` |
| > ratio | String | Yes | Proportion of recurring currency assets, e.g. "0.2" representing 20% |
| > minPx | String | No | Minimum price of recurring currency. `""` means no limit |
| > maxPx | String | No | Maximum price of recurring currency. `""` means no limit |
| period | String | Yes | Period`monthly``weekly``daily``hourly` |
| recurringDay | String | Conditional | Recurring buy dateWhen the period is `monthly`, the value range is an integer of [1,28]When the period is `weekly`, the value range is an integer of [1,7]When the period is `daily`/`hourly`, the parameter is not required. |
| recurringHour | String | Conditional | Recurring buy by hourly`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour"When the period is `hourly`, the parameter is required. |
| recurringTime | String | Yes | Recurring buy time, the value range is an integer of [0,23]When the period is `hourly`, the parameter is the time of the first investment occurs. |
| timeZone | String | Yes | UTC time zone, the value range is an integer of [-12,14]e.g. "8" representing UTC+8 (East 8 District), Beijing Time |
| amt | String | Yes | Quantity invested per cycle |
| investmentCcy | String | Yes | The invested quantity unit, can only be `USDT`/`USDC` |
| tdMode | String | Yes | Trading modeMargin mode: `cross`Non-Margin mode: `cash` |
| algoClOrdId | String | No | Client-supplied Algo IDThere will be a value when algo order attaching algoClOrdId is triggered, or it will be "".A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| tradeQuoteCcy | String | No | The quote currency for trading. |
| source | Array | No | Funding source`1`: Trading account`2`: Funding account`3`: Simple earn accountDefault is `1` |
| recurringTimeType | String | No | Recurring buy time type`1`: Custom time`2`: Immediate triggerDefault is `1` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "algoId":"560472804207104000",
 "algoClOrdId":"",
 "sCode":"0",
 "sMsg":"",
 "tag":""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | The code of the event execution result, 0 means success |
| sMsg | String | Rejection message if the request is unsuccessful |
| tag | String | Order tag |

### POST / Amend recurring buy order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-order-algo`

Request Example

```
POST /api/v5/tradingBot/recurring/amend-order-algo
body
{
 "algoId":"448965992920907776",
 "stgyName":"stg1"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| stgyName | String | Yes | New custom name for trading bot after adjustment, no more than 40 characters |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "algoId":"448965992920907776",
 "algoClOrdId":"",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | The code of the event execution result, 0 means success |
| sMsg | String | Rejection message if the request is unsuccessful |

### POST / Stop recurring buy order

A maximum of 10 orders can be stopped per request.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/stop-order-algo`

Request Example

```
POST /api/v5/tradingBot/recurring/stop-order-algo
body
[
 {
 "algoId":"560472804207104000"
 }
]
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "1839309556514557952",
 "sCode": "0",
 "sMsg": "",
 "tag": ""
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | The code of the event execution result, 0 means success |
| sMsg | String | Rejection message if the request is unsuccessful |
| tag | String | Order tag (Deprecated) |

### GET / Recurring buy order list

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/recurring/orders-algo-pending`

Request Example

```
GET /api/v5/tradingBot/recurring/orders-algo-pending
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | No | Algo ID |
| after | String | No | Pagination of data to return records earlier than the requested `algoId`. |
| before | String | No | Pagination of data to return records newer than the requested `algoId`. |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "644497312047435776",
 "algoOrdType": "recurring",
 "amt": "100",
 "cTime": "1699932133373",
 "cycles": "6",
 "instType": "SPOT",
 "investmentAmt": "0",
 "investmentCcy": "USDC",
 "mktCap": "0",
 "period": "hourly",
 "pnlRatio": "0",
 "recurringDay": "",
 "recurringHour": "1",
 "recurringList": [
 {
 "ccy": "BTC",
 "ratio": "0.2",
 "minPx": "",
 "maxPx": ""
 },
 {
 "ccy": "ETH",
 "ratio": "0.8",
 "minPx": "",
 "maxPx": ""
 }
 ],
 "recurringTime": "12",
 "state": "running",
 "stgyName": "stg1",
 "tag": "",
 "timeZone": "8",
 "totalAnnRate": "0",
 "totalPnl": "0",
 "uTime": "1699952473152",
 "tradeQuoteCcy": "USDT",
 "source": ["1"],
 "recurringTimeType": "1",
 "recurringTimeMinutes": "0"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| instType | String | Instrument type |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`recurring`: recurring buy |
| state | String | Algo order state`running``stopping``pause` |
| stgyName | String | Custom name for trading bot, no more than 40 characters |
| recurringList | Array of objects | Recurring buy info |
| > ccy | String | Recurring currency, e.g. `BTC` |
| > ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20% |
| > minPx | String | Minimum price of recurring currency. `""` means no limit |
| > maxPx | String | Maximum price of recurring currency. `""` means no limit |
| period | String | Period`monthly``weekly``daily``hourly` |
| recurringDay | String | Recurring buy dateWhen the period is `monthly`, the value range is an integer of [1,28]When the period is `weekly`, the value range is an integer of [1,7] |
| recurringHour | String | Recurring buy by hourly`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour" |
| recurringTime | String | Recurring buy time, the value range is an integer of [0,23] |
| timeZone | String | UTC time zone, the value range is an integer of [-12,14]e.g. "8" representing UTC+8 (East 8 District), Beijing Time |
| amt | String | Quantity invested per cycle |
| investmentAmt | String | Accumulate quantity invested |
| investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC` |
| totalPnl | String | Total P&L |
| totalAnnRate | String | Total annualized rate of yield |
| pnlRatio | String | Rate of yield |
| mktCap | String | Market value in unit of `USDT` |
| cycles | String | Accumulate recurring buy cycles |
| tag | String | Order tag |
| tradeQuoteCcy | String | The quote currency for trading. |
| source | Array | Funding source`1`: Trading account`2`: Funding account`3`: Simple earn account |
| recurringTimeType | String | Recurring buy time type`1`: Custom time`2`: Immediate trigger |
| recurringTimeMinutes | String | Recurring buy time in minutes, integer of [0,59] |

### GET / Recurring buy order history

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/recurring/orders-algo-history`

Request Example

```
GET /api/v5/tradingBot/recurring/orders-algo-history
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | No | Algo ID |
| after | String | No | Pagination of data to return records earlier than the requested `algoId`. |
| before | String | No | Pagination of data to return records newer than the requested `algoId`. |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "644496098429767680",
 "algoOrdType": "recurring",
 "amt": "100",
 "cTime": "1699931844050",
 "cycles": "0",
 "instType": "SPOT",
 "investmentAmt": "0",
 "investmentCcy": "USDC",
 "mktCap": "0",
 "period": "hourly",
 "pnlRatio": "0",
 "recurringDay": "",
 "recurringHour": "1",
 "recurringList": [
 {
 "ccy": "BTC",
 "ratio": "0.2",
 "minPx": "",
 "maxPx": ""
 },
 {
 "ccy": "ETH",
 "ratio": "0.8",
 "minPx": "",
 "maxPx": ""
 }
 ],
 "recurringTime": "0",
 "state": "stopped",
 "stgyName": "stg1",
 "tag": "",
 "timeZone": "8",
 "totalAnnRate": "0",
 "totalPnl": "0",
 "uTime": "1699932177659",
 "tradeQuoteCcy": "USDT"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| instType | String | Instrument type |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`recurring`: recurring buy |
| state | String | Algo order state`stopped` |
| stgyName | String | Custom name for trading bot, no more than 40 characters |
| recurringList | Array of objects | Recurring buy info |
| > ccy | String | Recurring currency, e.g. `BTC` |
| > ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20% |
| > minPx | String | Minimum price of recurring currency. `""` means no limit |
| > maxPx | String | Maximum price of recurring currency. `""` means no limit |
| period | String | Period`monthly``weekly``daily``hourly` |
| recurringDay | String | Recurring buy dateWhen the period is `monthly`, the value range is an integer of [1,28]When the period is `weekly`, the value range is an integer of [1,7] |
| recurringHour | String | Recurring buy by hourly`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour" |
| recurringTime | String | Recurring buy time, the value range is an integer of [0,23] |
| timeZone | String | UTC time zone, the value range is an integer of [-12,14]e.g. "8" representing UTC+8 (East 8 District), Beijing Time |
| amt | String | Quantity invested per cycle |
| investmentAmt | String | Accumulate quantity invested |
| investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC` |
| totalPnl | String | Total P&L |
| totalAnnRate | String | Total annualized rate of yield |
| pnlRatio | String | Rate of yield |
| mktCap | String | Market value in unit of `USDT` |
| cycles | String | Accumulate recurring buy cycles |
| tag | String | Order tag |
| tradeQuoteCcy | String | The quote currency for trading. |
| source | Array | Funding source`1`: Trading account`2`: Funding account`3`: Simple earn account |
| recurringTimeType | String | Recurring buy time type`1`: Custom time`2`: Immediate trigger |
| recurringTimeMinutes | String | Recurring buy time in minutes, integer of [0,59] |

### GET / Recurring buy order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/recurring/orders-algo-details`

Request Example

```
GET /api/v5/tradingBot/recurring/orders-algo-details?algoId=644497312047435776
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "644497312047435776",
 "algoOrdType": "recurring",
 "amt": "100",
 "cTime": "1699932133373",
 "cycles": "6",
 "instType": "SPOT",
 "investmentAmt": "0",
 "investmentCcy": "USDC",
 "mktCap": "0",
 "nextInvestTime": "1699956005500",
 "period": "hourly",
 "pnlRatio": "0",
 "recurringDay": "",
 "recurringHour": "1",
 "recurringList": [
 {
 "avgPx": "0",
 "ccy": "BTC",
 "profit": "0",
 "px": "36683.2",
 "ratio": "0.2",
 "minPx": "",
 "maxPx": "",
 "totalAmt": "0"
 },
 {
 "avgPx": "0",
 "ccy": "ETH",
 "profit": "0",
 "px": "2058.36",
 "ratio": "0.8",
 "minPx": "",
 "maxPx": "",
 "totalAmt": "0"
 }
 ],
 "recurringTime": "12",
 "state": "running",
 "stgyName": "stg1",
 "tag": "",
 "timeZone": "8",
 "totalAnnRate": "0",
 "totalPnl": "0",
 "uTime": "1699952485451",
 "tradeQuoteCcy": "USDT"，
 "source": ["1"],
 "recurringTimeType": "1",
 "recurringTimeMinutes": "0"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| instType | String | Instrument type |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`recurring`: recurring buy |
| state | String | Algo order state`running``stopping``stopped``pause` |
| stgyName | String | Custom name for trading bot, no more than 40 characters |
| recurringList | Array of objects | Recurring buy info |
| > ccy | String | Recurring buy currency, e.g. `BTC` |
| > ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20% |
| > minPx | String | Minimum price of recurring currency. `""` means no limit |
| > maxPx | String | Maximum price of recurring currency. `""` means no limit |
| > totalAmt | String | Accumulated quantity in unit of recurring buy currency |
| > profit | String | Profit in unit of `investmentCcy` |
| > avgPx | String | Average price of recurring buy, quote currency is `investmentCcy` |
| > px | String | Current market price, quote currency is `investmentCcy` |
| period | String | Period`monthly``weekly``daily``hourly` |
| recurringDay | String | Recurring buy dateWhen the period is `monthly`, the value range is an integer of [1,28]When the period is `weekly`, the value range is an integer of [1,7] |
| recurringHour | String | Recurring buy by hourly`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour" |
| recurringTime | String | Recurring buy time, the value range is an integer of [0,23] |
| timeZone | String | UTC time zone, the value range is an integer of [-12,14]e.g. "8" representing UTC+8 (East 8 District), Beijing Time |
| amt | String | Quantity invested per cycle |
| investmentAmt | String | Accumulate quantity invested |
| investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC` |
| nextInvestTime | String | Next invest time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| totalPnl | String | Total P&L |
| totalAnnRate | String | Total annualized rate of yield |
| pnlRatio | String | Rate of yield |
| mktCap | String | Market value in unit of `USDT` |
| cycles | String | Accumulate recurring buy cycles |
| tag | String | Order tag |
| tradeQuoteCcy | String | The quote currency for trading. |
| source | Array | Funding source`1`: Trading account`2`: Funding account`3`: Simple earn account |
| recurringTimeType | String | Recurring buy time type`1`: Custom time`2`: Immediate trigger |
| recurringTimeMinutes | String | Recurring buy time in minutes, integer of [0,59] |

### GET / Recurring buy sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/recurring/sub-orders`

Request Example

```
GET /api/v5/tradingBot/recurring/sub-orders?algoId=560516615079727104
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| ordId | String | No | Sub order ID |
| after | String | No | Pagination of data to return records earlier than the requested `algoId`. |
| before | String | No | Pagination of data to return records newer than the requested `algoId`. |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "accFillSz": "0.045315",
 "algoClOrdId": "",
 "algoId": "560516615079727104",
 "algoOrdType": "recurring",
 "avgPx": "1765.4",
 "cTime": "1679911222200",
 "fee": "-0.0000317205",
 "feeCcy": "ETH",
 "instId": "ETH-USDC",
 "instType": "SPOT",
 "ordId": "560523524230717440",
 "ordType": "market",
 "px": "-1",
 "side": "buy",
 "state": "filled",
 "sz": "80",
 "tag": "",
 "tdMode": "",
 "uTime": "1679911222207"
 },
 {
 "accFillSz": "0.00071526",
 "algoClOrdId": "",
 "algoId": "560516615079727104",
 "algoOrdType": "recurring",
 "avgPx": "27961.6",
 "cTime": "1679911222189",
 "fee": "-0.000000500682",
 "feeCcy": "BTC",
 "instId": "BTC-USDC",
 "instType": "SPOT",
 "ordId": "560523524184580096",
 "ordType": "market",
 "px": "-1",
 "side": "buy",
 "state": "filled",
 "sz": "20",
 "tag": "",
 "tdMode": "",
 "uTime": "1679911222194"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| algoOrdType | String | Algo order type`recurring`: recurring buy |
| ordId | String | Sub order ID |
| cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| tdMode | String | Sub order trade modeMargin mode : `cross`Non-Margin mode : `cash` |
| ordType | String | Sub order type`market`: Market order`manual_add_order`: Manual add investment order |
| sz | String | Sub order quantity to buy or sell |
| state | String | Sub order state`canceled``live``partially_filled``filled``cancelling` |
| side | String | Sub order side`buy` `sell` |
| px | String | Sub order limit priceIf it is a market order, "-1" will be return |
| fee | String | Sub order fee |
| feeCcy | String | Sub order fee currency |
| avgPx | String | Sub order average filled price |
| accFillSz | String | Sub order accumulated fill quantity |
| tag | String | Order tag |
| algoClOrdId | String | Client-supplied Algo ID |

### WS / Recurring buy orders channel

Retrieve recurring buy orders. Data will be pushed when triggered by events. It will also be pushed in regular interval according to subscription granularity.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "algo-recurring-buy",
 "instType": "SPOT"
 }]
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
 args = [{
 "channel": "algo-recurring-buy",
 "instType": "SPOT"
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
| > channel | String | Yes | Channel name`algo-recurring-buy` |
| > instType | String | Yes | Instrument type`SPOT``ANY` |
| > algoId | String | No | Algo Order ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "algo-recurring-buy",
 "instType": "SPOT"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"algo-recurring-buy\", \"instType\" : \"FUTURES\"}]}",
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
| > instType | String | Yes | Instrument type |
| > algoId | String | No | Algo Order ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example:

```
{
 "arg": {
 "channel": "algo-recurring-buy",
 "instType": "SPOT",
 "uid": "447*******584"
 },
 "data": [{
 "algoClOrdId": "",
 "algoId": "644497312047435776",
 "algoOrdType": "recurring",
 "amt": "100",
 "cTime": "1699932133373",
 "cycles": "0",
 "instType": "SPOT",
 "investmentAmt": "0",
 "investmentCcy": "USDC",
 "mktCap": "0",
 "nextInvestTime": "1699934415300",
 "pTime": "1699933314691",
 "period": "hourly",
 "pnlRatio": "0",
 "recurringDay": "",
 "recurringHour": "1",
 "recurringList": [{
 "avgPx": "0",
 "ccy": "BTC",
 "profit": "0",
 "px": "36482",
 "ratio": "0.2",
 "minPx": "30000",
 "maxPx": "50000"
 "totalAmt": "0"
 }, {
 "avgPx": "0",
 "ccy": "ETH",
 "profit": "0",
 "px": "2057.54",
 "ratio": "0.8",
 "minPx": "",
 "maxPx": "",
 "totalAmt": "0"
 }],
 "recurringTime": "12",
 "state": "running",
 "stgyName": "stg1",
 "tag": "",
 "timeZone": "8",
 "totalAnnRate": "0",
 "totalPnl": "0",
 "uTime": "1699932136249",
 "tradeQuoteCcy": "USDT"
 }]
}

```

#### Response parameters when data is pushed.

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instType | String | Instrument type |
| > algoId | String | Algo Order ID |
| > uid | String | User ID |
| data | Array of objects | Subscribed data |
| > algoId | String | Algo ID |
| > algoClOrdId | String | Client-supplied Algo ID |
| > instType | String | Instrument type |
| > cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > algoOrdType | String | Algo order type`recurring`: recurring buy |
| > state | String | Algo order state`running``stopping``stopped``pause` |
| > stgyName | String | Custom name for trading bot, no more than 40 characters |
| > recurringList | Array of objects | Recurring buy info |
| >> ccy | String | Recurring buy currency, e.g. `BTC` |
| >> ratio | String | Proportion of recurring currency assets, e.g. "0.2" representing 20% |
| >> minPx | String | Minimum price of price range. `""` means no limit |
| >> maxPx | String | Maximum price of price range. `""` means no limit |
| >> totalAmt | String | Accumulated quantity in unit of recurring buy currency |
| >> profit | String | Profit in unit of `investmentCcy` |
| >> avgPx | String | Average price of recurring buy, quote currency is `investmentCcy` |
| >> px | String | Current market price, quote currency is `investmentCcy` |
| > period | String | Period`monthly``weekly``daily``hourly` |
| > recurringDay | String | Recurring buy dateWhen the period is `monthly`, the value range is an integer of [1,28]When the period is `weekly`, the value range is an integer of [1,7] |
| > recurringHour | String | Recurring buy by hourly`1`/`4`/`8`/`12`, e.g. `4` represents "recurring buy every 4 hour" |
| > recurringTime | String | Recurring buy time, the value range is an integer of [0,23] |
| > timeZone | String | UTC time zone, the value range is an integer of [-12,14]e.g. "8" representing UTC+8 (East 8 District), Beijing Time |
| > amt | String | Quantity invested per cycle |
| > investmentAmt | String | Accumulate quantity invested |
| > investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC` |
| > nextInvestTime | String | Next invest time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > totalPnl | String | Total P&L |
| > totalAnnRate | String | Total annualized rate of yield |
| > pnlRatio | String | Rate of yield |
| > mktCap | String | Market value in unit of `USDT` |
| > cycles | String | Accumulate recurring buy cycles |
| > tag | String | Order tag |
| > pTime | String | Push time of algo order information, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > tradeQuoteCcy | String | The quote currency for trading. |
| > recurringTimeType | String | Recurring buy time type |
| > recurringTimeMinutes | String | Custom recurring buy minutes |
| > source | Array | Source of recurring buy |

### POST / Amend recurring buy time

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-recurring-time`

Request Example

```
POST /api/v5/tradingBot/recurring/amend-recurring-time
body
{
 "algoId": "2837428373700509696",
 "recurringTimeType": "1",
 "period": "hourly",
 "recurringHour": "8",
 "recurringDay": "1",
 "recurringTime": "11",
 "timeZone": "8"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| recurringTimeType | String | Yes | Recurring buy time type`1`: Custom time`2`: Immediate trigger |
| timeZone | String | Yes | UTC time zone, the value range is an integer of [-12,14]e.g. `8` representing UTC+8 (East 8 District), Beijing Time |
| period | String | Yes | Period`monthly``weekly``daily``hourly` |
| recurringHour | String | Conditional | Recurring buy by hourly`1`/`4`/`8`/`12`, e.g. `1` represents "recurring buy every 1 hour"Required when `period` is `hourly` |
| recurringDay | String | Conditional | Recurring buy dateWhen the period is `monthly`, the value range is an integer of [1,28]When the period is `weekly`, the value range is an integer of [1,7]When the period is `daily`/`hourly`, the parameter is not requiredOnly required when `recurringTimeType` is `1` |
| recurringTime | String | Conditional | Recurring buy time, the value range is an integer of [0,23]Only required when `recurringTimeType` is `1` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### POST / Amend recurring buy amount

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-recurring-amount`

Request Example

```
POST /api/v5/tradingBot/recurring/amend-recurring-amount
body
{
 "algoId": "2837428373700509696",
 "amount": "20"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| amount | String | Yes | Amended recurring buy amount. Only the investment currency used when the strategy was created is supported |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2837428373700509696",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### POST / Add investment

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/add-investment`

Request Example

```
POST /api/v5/tradingBot/recurring/add-investment
body
{
 "algoId": "2837428373700509696",
 "amount": "20"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| amount | String | Yes | Additional investment amount. Only the investment currency used when the strategy was created is supported |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2837428373700509696",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### POST / Pause recurring buy

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/pause`

Request Example

```
POST /api/v5/tradingBot/recurring/pause
body
{
 "algoId": "2837428373700509696"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2837428373700509696",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### POST / Restart recurring buy

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/restart`

Request Example

```
POST /api/v5/tradingBot/recurring/restart
body
{
 "algoId": "2837428373700509696"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2837428373700509696",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### POST / Amend price range

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/recurring/amend-price-range`

Request Example

```
POST /api/v5/tradingBot/recurring/amend-price-range
body
{
 "algoId": "2837428373700509696",
 "recurringList": [
 {
 "ccy": "BTC",
 "minPx": "80000",
 "maxPx": "120000"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| recurringList | Array | Yes | Price range settings. The currency must be within the scope of the recurring buy currencies |
| >ccy | String | Yes | Recurring buy currency |
| >minPx | String | Yes | Minimum price of price range. `""` means no limit |
| >maxPx | String | Yes | Maximum price of price range. `""` means no limit |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2837428373700509696",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |
