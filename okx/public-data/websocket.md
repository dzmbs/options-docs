## WebSocket

### Instruments channel

The triggering scenarios for incremental data are:

1. When there is any change to the instrument’s state (such as delivery of FUTURES, exercise of OPTION, listing of new contracts / trading pairs, trading suspension, etc.)

2. When the trading parameters change (tickSz,minSz,maxMktSz)

3. When the expTime or listTime changes

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "instruments",
 "instType": "SPOT"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "instruments",
 "instType": "SPOT"
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
| > channel | String | Yes | Channel name`instruments` |
| > instType | String | Yes | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "instruments",
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"instruments\", \"instType\" : \"FUTURES\"}]}",
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
| > instType | String | Yes | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "instruments",
 "instType": "SPOT"
 },
 "data": [
 {
 "alias": "",
 "auctionEndTime": "",
 "baseCcy": "BTC",
 "category": "1",
 "ctMult": "",
 "ctType": "",
 "ctVal": "",
 "ctValCcy": "",
 "contTdSwTime": "1704876947000",
 "expTime": "",
 "futureSettlement": false,
 "groupId": "1",
 "instFamily": "",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "lever": "10",
 "listTime": "1606468572000",
 "lotSz": "0.00000001",
 "maxIcebergSz": "9999999999.0000000000000000",
 "maxLmtAmt": "1000000",
 "maxLmtSz": "9999999999",
 "maxMktAmt": "1000000",
 "maxMktSz": "",
 "maxStopSz": "",
 "maxTriggerSz": "9999999999.0000000000000000",
 "maxTwapSz": "9999999999.0000000000000000",
 "minSz": "0.00001",
 "optType": "",
 "openType": "call_auction",
 "preMktSwTime": "",
 "quoteCcy": "USDT",
 "settleCcy": "",
 "state": "live",
 "ruleType": "normal",
 "stk": "",
 "tickSz": "0.1",
 "uly": "",
 "instIdCode": 1000000000,
 "instCategory": "1",
 "upcChg": [
 {
 "param": "tickSz",
 "newValue": "0.0001",
 "effTime": "1704876947000"
 }
 ]
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Subscribed channel |
| > channel | String | Channel name |
| > instType | String | Instrument type |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`. Only applicable to `EVENTS` |
| > instId | String | Instrument ID, e.g. `BTC-UST` |
| > uly | String | Underlying, e.g. `BTC-USD` Only applicable to `FUTURES`/`SWAP`/`OPTION` |
| > groupId | String | Instrument trading fee group IDSpot:`1`: Spot USDT`2`: Spot USDC & Crypto`3`: Spot TRY`4`: Spot EUR`5`: Spot BRL`7`: Spot AED`8`: Spot AUD`9`: Spot USD`10`: Spot SGD`11`: Spot zero`12`: Spot group one`13`: Spot group two`14`: Spot group three`15`: Spot special ruleExpiry futures:`1`: Expiry futures crypto-margined`2`: Expiry futures USDT-margined`3`: Expiry futures USDC-margined`4`: Expiry futures premarket`5`: Expiry futures group one`6`: Expiry futures group twoPerpetual futures:`1`: Perpetual futures crypto-margined`2`: Perpetual futures USDT-margined`3`: Perpetual futures USDC-margined`4`: Perpetual futures group one`5`: Perpetual futures group two`6`: Stock perpetual futures Options:`1`: Options crypto-margined`2`: Options USDC-marginedinstType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with fee rates endpoint to get the trading fee of a specific symbol. Some enum values may not apply to you; the actual return values shall prevail. |
| > instFamily | String | Instrument family, e.g. `BTC-USD` Only applicable to `FUTURES`/`SWAP`/`OPTION` |
| > category | String | Currency category. Note: this parameter is already deprecated |
| > baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT` Only applicable to `SPOT`/`MARGIN` |
| > quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT` Only applicable to `SPOT`/`MARGIN` |
| > settleCcy | String | Settlement and margin currency, e.g. `BTC` Only applicable to `FUTURES`/`SWAP`/`OPTION` |
| > ctVal | String | Contract value |
| > ctMult | String | Contract multiplier |
| > ctValCcy | String | Contract value currency |
| > optType | String | Option type`C`: Call`P`: PutOnly applicable to `OPTION` |
| > stk | String | Strike priceOnly applicable to `OPTION` |
| > listTime | String | Listing timeOnly applicable to `FUTURES`/`SWAP`/`OPTION` |
| > auctionEndTime | String | The end time of call auction, Unix timestamp format in milliseconds, e.g. `1597026383085` Only applicable to `SPOT` that are listed through call auctions, return "" in other cases (deprecated, use contTdSwTime) |
| > contTdSwTime | String | Continuous trading switch time. The switch time from call auction, prequote to continuous trading, Unix timestamp format in milliseconds. e.g. `1597026383085`. Only applicable to `SPOT`/`MARGIN` that are listed through call auction or prequote, return "" in other cases. |
| > preMktSwTime | String | The time premarket swap switched to normal swap, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable premarket `SWAP` |
| > openType | String | Open type `fix_price`: fix price opening`pre_quote`: pre-quote`call_auction`: call auction Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines |
| > expTime | String | Expiry timeApplicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is the delivery/exercise time. It can also be the delisting time of the trading instrument. Update once change. |
| > lever | String | Max LeverageNot applicable to `SPOT`/`OPTION`, used to distinguish between `MARGIN` and `SPOT`. |
| > tickSz | String | Tick size, e.g. `0.0001`.For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band. |
| > lotSz | String | Lot sizeIf it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency` |
| > minSz | String | Minimum order sizeIf it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency` |
| > ctType | String | Contract type`linear`: linear contract`inverse`: inverse contractOnly applicable to `FUTURES`/`SWAP` |
| > alias | String | Contract alias (deprecated — use expTime to obtain the delivery time, will be removed by the end of April 2026)`this_week``next_week``this_month``next_month``quarter``next_quarter``this_five_years`: current 5-year contract`next_five_years`: next 5-year contractOnly applicable to `FUTURES` |
| > state | String | Instrument status`live``suspend``expired``rebase`: can't be traded during rebasing, only applicable to `SWAP``post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP``preopen`. e.g. There will be `preopen` before the Futures and Options new contracts state is live.`test`: Test pairs, can't be traded`settling`: Settling, only applicable to `EVENTS` |
| > ruleType | String | Trading rule types`normal`: normal trading`pre_market`: pre-market trading`rebase_contract`: pre-market rebase contract`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts |
| > maxLmtSz | String | The maximum order quantity of a single limit order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| > maxMktSz | String | The maximum order quantity of a single market order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`. |
| > maxTwapSz | String | The maximum order quantity of a single TWAP order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| > maxIcebergSz | String | The maximum order quantity of a single iceBerg order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| > maxTriggerSz | String | The maximum order quantity of a single trigger order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| > maxStopSz | String | The maximum order quantity of a single stop market order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`. |
| > futureSettlement | Boolean | Whether daily settlement for expiry feature is enabledApplicable to `FUTURES` `cross` |
| > instIdCode | Integer | Instrument ID code. For simple binary encoding, you must use `instIdCode` instead of `instId`.For the same `instId`, it's value may be different between production and demo trading. It is `null` when the value is not generated. |
| > instCategory | String | The asset category of the instrument’s base asset (the first segment of the instrument ID). For example, for `BTC-USDT-SWAP`, the `instCategory` represents the asset category of `BTC`. `1`: Crypto `3`: Stocks `4`: Commodities `5`: Forex `6`: Bonds `""`: Not available |
| > upcChg | Array of objects | Upcoming changes. It is [] when there is no upcoming change. |
| >> param | String | The parameter name to be updated. `tickSz` `minSz`: For `FUTURES`/`SWAP`, `lotSz` will be modified synchronously. `maxMktSz` |
| >> newValue | String | The parameter value that will replace the current one. |
| >> effTime | String | Effective time. Unix timestamp format in milliseconds, e.g. `1597026383085` |


Instrument status will trigger pushing of incremental data from instruments channel.
When a new contract is going to be listed, the instrument data of the new contract will be available with status preopen.
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument status will be changed to expired.

listTime and contTdSwTime

For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".

state

For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders. Certain symbols will now have `state:preopen` before they go live. Before going live, the instruments channel will push data for pre-listing symbols with `state:preopen`. If the listing is cancelled, the channel will send full data excluding the cancelled symbol, without additional notification. When the symbol goes live (at or shortly after `listTime` for `OPTION`), the channel will push data with `state:live`. Users can also query the corresponding data via the REST endpoint.

When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available.

### Event contract markets channel

Pushes event contract market status updates and floorStrike generation. No initial snapshot push.

#### URL Path

/ws/v5/public

Request Example

```
{
 "op": "subscribe",
 "args": [
 {
 "channel": "event-contract-markets",
 "instType": "EVENTS"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message. Provided by client. Returned in response. Alphanumeric, 1-32 characters. |
| op | String | Yes | Operation.`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name.`event-contract-markets` |
| > instType | String | Yes | Instrument type.`EVENTS` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "event-contract-markets",
 "instType": "EVENTS"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{\"channel\": \"event-contract-markets\", \"instType\": \"EVENTS\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| event | String | Event.`subscribe``unsubscribe``error` |
| arg | Object | Subscribed channel |
| > channel | String | Channel name |
| > instType | String | Instrument type |
| code | String | Error code |
| msg | String | Error message |
| connId | String | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "event-contract-markets"
 },
 "data": [
 {
 "seriesId": "BTC-ABOVE-DAILY",
 "eventId": "BTC-ABOVE-DAILY-260224-1600",
 "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
 "listTime": "1769697132335",
 "fixTime": "",
 "expTime": "1769697132335",
 "state": "live",
 "outcome": "0",
 "floorStrike": "120000",
 "settleValue": "",
 "disputed": false
 }
 ]
}

```

#### Push Data Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Subscribed channel |
| > channel | String | Channel name |
| data | Array of objects | Subscribed data |
| > seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY` |
| > eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600` |
| > instId | String | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000` |
| > listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method. |
| > expTime | String | Strike time for this event, Unix timestamp format in milliseconds, e.g. `1597026383085`. Updated once the market is settled. |
| > state | String | Market state.`preopen``live``settling``expired` |
| > outcome | String | Market outcome.`0`: Not available`1`: YES`2`: NO.`1`/`2` only applicable when state is `expired` |
| > floorStrike | String | Minimum expiration value that leads to a YES outcome |
| > settleValue | String | Settlement valueOnly return when the state is `expired` |
| > disputed | Boolean | Whether the market has been disputed.`true``false` |

### Open interest channel

Retrieve the open interest. Data will be pushed every 3 seconds when there are updates.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "open-interest",
 "instId": "LTC-USD-SWAP"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "open-interest",
 "instId": "LTC-USD-SWAP"
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
| > channel | String | Yes | Channel name`open-interest` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "open-interest",
 "instId": "LTC-USD-SWAP"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"open-interest\", \"instId\" : \"LTC-USD-SWAP\"}]}",
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
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "open-interest",
 "instId": "BTC-USDT-SWAP"
 },
 "data": [
 {
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "oi": "2216113.01000000309",
 "oiCcy": "22161.1301000000309",
 "oiUsd": "1939251795.54769270396321",
 "ts": "1743041250440"
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
| > instType | String | Instrument type |
| > instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| > oi | String | Open interest, in units of contracts. |
| > oiCcy | String | Open interest, in currency units, like BTC. |
| > oiUsd | String | Open interest in number of USD |
| > ts | String | The time when the data was updated, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Funding rate channel

Retrieve funding rate. Data will be pushed in 30s to 90s.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "funding-rate",
 "instId": "BTC-USD-SWAP"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "funding-rate",
 "instId": "BTC-USD-SWAP"
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
| > channel | String | Yes | Channel name`funding-rate` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "funding-rate",
 "instId": "BTC-USD-SWAP"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"funding-rate\", \"instId\" : \"BTC-USD-SWAP\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | yes | Channel name |
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg":{
 "channel":"funding-rate",
 "instId":"BTC-USD-SWAP"
 },
 "data":[
 {
 "formulaType": "noRate",
 "fundingRate":"0.0001875391284828",
 "fundingTime":"1700726400000",
 "impactValue": "",
 "instId":"BTC-USD-SWAP",
 "instType":"SWAP",
 "interestRate": "",
 "method": "current_period",
 "maxFundingRate":"0.00375",
 "minFundingRate":"-0.00375",
 "nextFundingRate":"",
 "nextFundingTime":"1700755200000",
 "premium": "0.0001233824646391",
 "settFundingRate":"0.0001699799259033",
 "settState":"settled",
 "ts":"1700724675402"
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
| > instType | String | Instrument type`SWAP`: Perpetual futures`FUTURES`: X-Perps futures |
| > instId | String | Instrument ID, e.g. `BTC-USD-SWAP` |
| > method | String | Funding rate mechanism `current_period` `next_period`(no longer supported) |
| > formulaType | String | Formula type`noRate`: old funding rate formula`withRate`: new funding rate formula |
| > fundingRate | String | Current funding rate |
| > nextFundingRate | String | Forecasted funding rate for the next period The nextFundingRate will be "" if the method is `current_period`(no longer supported) |
| > fundingTime | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > nextFundingTime | String | Forecasted funding time for the next period, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > minFundingRate | String | The lower limit of the predicted funding rate of the next cycle |
| > maxFundingRate | String | The upper limit of the predicted funding rate of the next cycle |
| > interestRate | String | Interest rate |
| > impactValue | String | Depth weighted amount (in the unit of quote currency) |
| > settState | String | Settlement state of funding rate `processing` `settled` |
| > settFundingRate | String | If settState = `processing`, it is the funding rate that is being used for current settlement cycle. If settState = `settled`, it is the funding rate that is being used for previous settlement cycle |
| > premium | String | Premium index formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price |
| > ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

For some altcoins perpetual swaps with significant fluctuations in funding rates, OKX will closely monitor market changes. When necessary, the funding rate collection frequency, currently set at 8 hours, may be adjusted to higher frequencies such as 6 hours, 4 hours, 2 hours, or 1 hour. Thus, users should focus on the difference between `fundingTime` and `nextFundingTime` fields to determine the funding fee interval of a contract.

### Price limit channel

Retrieve the maximum buy price and minimum sell price of instruments. Data will be pushed every 200ms when there are changes in limits, and will not be pushed when there is no changes on limit.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "price-limit",
 "instId": "LTC-USD-190628"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "price-limit",
 "instId": "LTC-USD-190628"
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
| > channel | String | Yes | Channel name`price-limit` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "price-limit",
 "instId": "LTC-USD-190628"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"price-limit\", \"instId\" : \"LTC-USD-190628\"}]}",
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
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "price-limit",
 "instId": "LTC-USD-190628"
 },
 "data": [{
 "instId": "LTC-USD-190628",
 "buyLmt": "200",
 "sellLmt": "300",
 "ts": "1597026383085",
 "enabled": true
 }]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > instId | String | Instrument ID, e.g. `BTC-USDT` |
| > buyLmt | String | Maximum buy price Return "" when enabled is false |
| > sellLmt | String | Minimum sell price Return "" when enabled is false |
| > ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > enabled | Boolean | Whether price limit is effective `true`: the price limit is effective `false`: the price limit is not effective |

### Option summary channel

Retrieve detailed pricing information of all OPTION contracts. Data will be pushed at once.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "opt-summary",
 "instFamily": "BTC-USD"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "opt-summary",
 "instFamily": "BTC-USD"
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
| > channel | String | Yes | Channel name`opt-summary` |
| > instFamily | String | Yes | Instrument family |

Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "opt-summary",
 "instFamily": "BTC-USD"
 },
 "connId": "a4d3ae55"
}

```

Failure example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"opt-summary\", \"uly\" : \"BTC-USD\"}]}",
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
| > instFamily | String | Yes | Instrument family |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "opt-summary",
 "instFamily": "BTC-USD"
 },
 "data": [
 {
 "instType": "OPTION",
 "instId": "BTC-USD-241013-70000-P",
 "uly": "BTC-USD",
 "delta": "-1.1180902625",
 "gamma": "2.2361957091",
 "vega": "0.0000000001",
 "theta": "0.0000032334",
 "lever": "8.465747567",
 "markVol": "0.3675503331",
 "bidVol": "0",
 "askVol": "1.1669998535",
 "realVol": "",
 "deltaBS": "-0.9999672034",
 "gammaBS": "0.0000000002",
 "thetaBS": "28.2649858387",
 "vegaBS": "0.0000114332",
 "ts": "1728703155650",
 "fwdPx": "62604.6993093463",
 "volLv": "0.2044711229"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instFamily | String | Instrument family |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type, `OPTION` |
| > instId | String | Instrument ID |
| > uly | String | Underlying |
| > delta | String | Sensitivity of option price to `uly` price |
| > gamma | String | The delta is sensitivity to `uly` price |
| > vega | String | Sensitivity of option price to implied volatility |
| > theta | String | Sensitivity of option priceo remaining maturity |
| > deltaBS | String | Sensitivity of option price to `uly` price in BS mode |
| > gammaBS | String | The delta is sensitivity to `uly` price in BS mode |
| > vegaBS | String | Sensitivity of option price to implied volatility in BS mode |
| > thetaBS | String | Sensitivity of option price to remaining maturity in BS mode |
| > lever | String | Leverage |
| > markVol | String | Mark volatility |
| > bidVol | String | Bid volatility |
| > askVol | String | Ask Volatility |
| > realVol | String | Realized volatility (not currently used) |
| > volLv | String | Implied volatility of at-the-money options |
| > fwdPx | String | Forward price |
| > ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Estimated delivery/exercise/settlement price channel

Retrieve the estimated delivery/exercise/settlement price of `FUTURES`, `OPTION` and `SWAP` contracts.

The estimated price, calculated based on index price during the one-hour period prior to delivery, excerise, or settlement, with updates pushed approximately every 200ms.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "estimated-price",
 "instType": "FUTURES",
 "instFamily": "BTC-USD"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "estimated-price",
 "instType": "FUTURES",
 "instFamily": "BTC-USD"
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
| > channel | String | Yes | Channel name`estimated-price` |
| > instType | String | Yes | Instrument type`OPTION``FUTURES``SWAP``EVENTS` |
| > instFamily | String | Conditional | Instrument familyEither `instFamily` or `instId` is required. |
| > instId | String | Conditional | Instrument IDEither `instFamily` or `instId` is required. |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "estimated-price",
 "instType": "FUTURES",
 "instFamily": "BTC-USD"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"estimated-price\", \"instId\" : \"FUTURES\",\"uly\" :\"BTC-USD\"}]}",
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
| > instType | String | Yes | Instrument type`OPTION``FUTURES``SWAP``EVENTS` |
| > instFamily | String | Conditional | Instrument family |
| > instId | String | Conditional | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "estimated-price",
 "instType": "FUTURES",
 "instFamily": "XRP-USDT"
 },
 "data": [{
 "instId": "XRP-USDT-250307",
 "instType": "FUTURES",
 "settlePx": "2.4230631578947368",
 "settleType": "settlement",
 "ts": "1741244598708"
 }]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instType | String | Instrument type`FUTURES``OPTION``SWAP``EVENTS` |
| > instFamily | String | Instrument family |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > instId | String | Instrument ID, e.g. `BTC-USD-170310` |
| > settleType | String | Type`settlement`: Futures settlement`delivery`: Futures delivery`exercise`: Option exercise |
| > settlePx | String | Estimated price |
| > ts | String | Data update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Mark price channel

Retrieve the mark price. Data will be pushed every 200 ms when the mark price changes, and will be pushed every 10 seconds when the mark price does not change.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "mark-price",
 "instId": "LTC-USD-190628"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [{
 "channel": "mark-price",
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
| > channel | String | Yes | Channel name`mark-price` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "mark-price",
 "instId": "LTC-USD-190628"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price\", \"instId\" : \"LTC-USD-190628\"}]}",
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
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "mark-price",
 "instId": "LTC-USD-190628"
 },
 "data": [
 {
 "instType": "FUTURES",
 "instId": "LTC-USD-190628",
 "markPx": "0.1",
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
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > markPx | String | Mark price |
| > ts | String | Price update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Index tickers channel

Retrieve index tickers data. Push data every 100ms if there are any changes, otherwise push once a minute.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "index-tickers",
 "instId": "BTC-USDT"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "index-tickers",
 "instId": "BTC-USDT"
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
| op | String | Yes | `subscribe` `unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`index-tickers` |
| > instId | String | Yes | Index with USD, USDT, BTC, USDC as the quote currency, e.g. `BTC-USDT`Same as `uly`. |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "index-tickers",
 "instId": "BTC-USDT"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-tickers\", \"instId\" : \"BTC-USDT\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | `subscribe` `unsubscribe` `error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`index-tickers` |
| > instId | String | Yes | Index with USD, USDT, BTC, USDC as the quote currency, e.g. `BTC-USDT` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "index-tickers",
 "instId": "BTC-USDT"
 },
 "data": [
 {
 "instId": "BTC-USDT",
 "idxPx": "0.1",
 "high24h": "0.5",
 "low24h": "0.1",
 "open24h": "0.1",
 "sodUtc0": "0.1",
 "sodUtc8": "0.1",
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
| > instId | String | Index with USD, USDT, or BTC as quote currency, e.g. `BTC-USDT`. |
| data | Array of objects | Subscribed data |
| > instId | String | Index |
| > idxPx | String | Latest Index Price |
| > open24h | String | Open price in the past 24 hours |
| > high24h | String | Highest price in the past 24 hours |
| > low24h | String | Lowest price in the past 24 hours |
| > sodUtc0 | String | Open price in the UTC 0 |
| > sodUtc8 | String | Open price in the UTC 8 |
| > ts | String | Update time of the index ticker, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Mark price candlesticks channel

Retrieve the candlesticks data of the mark price. The push frequency is the fastest interval 1 second push the data.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "mark-price-candle1D",
 "instId": "BTC-USD-190628"
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
 "channel": "mark-price-candle1D",
 "instId": "BTC-USD-190628"
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
| op | String | Yes | Operation`subscribe` `unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name `mark-price-candle3M` `mark-price-candle1M` `mark-price-candle1W` `mark-price-candle1D` `mark-price-candle2D` `mark-price-candle3D` `mark-price-candle5D` `mark-price-candle12H` `mark-price-candle6H` `mark-price-candle4H` `mark-price-candle2H` `mark-price-candle1H` `mark-price-candle30m` `mark-price-candle15m` `mark-price-candle5m` `mark-price-candle3m` `mark-price-candle1m` `mark-price-candle1Yutc` `mark-price-candle3Mutc` `mark-price-candle1Mutc` `mark-price-candle1Wutc` `mark-price-candle1Dutc` `mark-price-candle2Dutc` `mark-price-candle3Dutc` `mark-price-candle5Dutc` `mark-price-candle12Hutc` `mark-price-candle6Hutc` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "mark-price-candle1D",
 "instId": "BTC-USD-190628"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"mark-price-candle1D\", \"instId\" : \"BTC-USD-190628\"}]}",
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
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "mark-price-candle1D",
 "instId": "BTC-USD-190628"
 },
 "data": [
 ["1597026383085", "3.721", "3.743", "3.677", "3.708","0"],
 ["1597026383085", "3.731", "3.799", "3.494", "3.72","1"]
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of Arrays | Subscribed data |
| > ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > o | String | Open price |
| > h | String | Highest price |
| > l | String | Lowest price |
| > c | String | Close price |
| > confirm | String | The state of candlesticks.`0` represents that it is uncompleted, `1` represents that it is completed. |

### Index candlesticks channel

Retrieve the candlesticks data of the index. The push frequency is the fastest interval 1 second push the data. .

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "index-candle30m",
 "instId": "BTC-USD"
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
 "channel": "index-candle30m",
 "instId": "BTC-USD"
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
| > channel | String | Yes | Channel name `index-candle3M` `index-candle1M` `index-candle1W` `index-candle1D` `index-candle2D` `index-candle3D` `index-candle5D` `index-candle12H` `index-candle6H` `index-candle4H` `index -candle2H` `index-candle1H` `index-candle30m` `index-candle15m` `index-candle5m` `index-candle3m` `index-candle1m` `index-candle3Mutc` `index-candle1Mutc` `index-candle1Wutc` `index-candle1Dutc` `index-candle2Dutc` `index-candle3Dutc` `index-candle5Dutc` `index-candle12Hutc` `index-candle6Hutc` |
| > instId | String | Yes | Index, e.g. `BTC-USD`Same as `uly`. |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "index-candle30m",
 "instId": "BTC-USD"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"index-candle30m\", \"instId\" : \"BTC-USD\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | `subscribe` `unsubscribe` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instId | String | No | Index, e.g. `BTC-USD` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "index-candle30m",
 "instId": "BTC-USD"
 },
 "data": [["1597026383085", "3811.31", "3811.31", "3811.31", "3811.31", "0"]]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Index |
| data | Array of Arrays | Subscribed data |
| > ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > o | String | Open price |
| > h | String | Highest price |
| > l | String | Lowest price |
| > c | String | Close price |
| > confirm | String | The state of candlesticks.`0` represents that it is uncompleted, `1` represents that it is completed. |

The order of the returned values is: [ts,o,h,l,c,confirm]

### Liquidation orders channel

Retrieve the recent liquidation orders. This data doesn’t represent the total number of liquidations on OKX.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "liquidation-orders",
 "instType": "SWAP"
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
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "liquidation-orders",
 "instType": "SWAP"
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
| > channel | String | Yes | Channel name`liquidation-orders` |
| > instType | String | Yes | Instrument type`SWAP``FUTURES``MARGIN``OPTION` |

Response Example

```
{
 "id": "1512",
 "arg": {
 "channel": "liquidation-orders",
 "instType": "SWAP"
 },
 "data": [
 {
 "details": [
 {
 "bkLoss": "0",
 "bkPx": "0.007831",
 "ccy": "",
 "posSide": "short",
 "side": "buy",
 "sz": "13",
 "ts": "1692266434010"
 }
 ],
 "instFamily": "IOST-USDT",
 "instId": "IOST-USDT-SWAP",
 "instType": "SWAP",
 "uly": "IOST-USDT"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > instId | String | Instrument ID, e.g. `BTC-USD-SWAP` |
| > uly | String | UnderlyingApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > details | Array of objects | Liquidation details |
| >> side | String | Order side`buy``sell`Applicable to `FUTURES`/`SWAP` |
| >> posSide | String | Position mode side`long`: Hedge mode long`short`: Hedge mode short`net`: Net mode |
| >> bkPx | String | Bankruptcy price. The price of the transaction with the system's liquidation account, only applicable to `FUTURES`/`SWAP` |
| >> sz | String | Quantity of liquidation, only applicable to `MARGIN`/`FUTURES`/`SWAP`. For `MARGIN`, the unit is base currency. For `FUTURES/SWAP`, the unit is contract. |
| >> bkLoss | String | Bankruptcy loss |
| >> ccy | String | Liquidation currency, only applicable to `MARGIN` |
| >> ts | String | Liquidation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

Liquidation data comes from different data sources, so the updated data is not necessarily in chronological order.

### ADL warning channel

Auto-deleveraging warning channel.

Data is only pushed in the `warning` or `adl` state, once every second, displaying the security fund balance and related risk information. No data is pushed in the `normal` state.

For more ADL details, please refer to [Introduction to Auto-deleveraging](https://www.okx.com/help/iv-introduction-to-auto-deleveraging-adl)

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "adl-warning",
 "instType": "FUTURES",
 "instFamily": "BTC-USDT"
 }]
}
```

```
import asyncio
from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [{
 "channel": "adl-warning",
 "instType": "FUTURES",
 "instFamily": "BTC-USDT"
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
| > channel | String | Yes | Channel name`adl-warning` |
| > instType | String | Yes | Instrument type`SWAP``FUTURES``OPTION` |
| > instFamily | String | No | Instrument family |

Successful Response Example

```
{
 "id": "1512",
 "event":"subscribe",
 "arg":{
 "channel":"adl-warning",
 "instType":"FUTURES",
 "instFamily":"BTC-USDT"
 },
 "connId":"48d8960a"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event":"error",
 "msg":"Illegal request: { \"event\": \"subscribe\", \"arg\": { \"channel\": \"adl-warning\", \"instType\": \"FUTURES\", \"instFamily\": \"BTC-USDT\" } }",
 "code":"60012",
 "connId":"48d8960a"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`adl-warning` |
| > instType | String | Yes | Instrument type |
| > instFamily | String | No | Instrument family |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg":{
 "channel":"adl-warning",
 "instType":"FUTURES",
 "instFamily":"BTC-USDT"
 },
 "data":[
 {
 "instType":"FUTURES",
 "instFamily":"BTC-USDT",
 "state":"warning",
 "bal":"280784384.9564228289548144",
 "ccy":"",
 "maxBal":"",
 "maxBalTs":"",
 "adlType":"",
 "adlBal":"",
 "adlRecBal":"",
 "ts":"1700210763001",
 "decRate":"",
 "adlRate":"",
 "adlRecRate":""
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Subscribed channel |
| > channel | String | Channel name`adl-warning` |
| > instType | String | Instrument type |
| > instFamily | String | Instrument family |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > instFamily | String | Instrument family |
| > state | String | state `warning` `adl` |
| > bal | String | Real-time security fund balance |
| > ccy | String | The corresponding currency of security fund balance(Deprecated, returns `""`. To be removed in a future update) |
| > maxBal | String | Maximum security fund balance in the past eight hours Applicable when state is `warning` or `adl`(Deprecated, returns `""`. To be removed in a future update) |
| > maxBalTs | String | Timestamp when security fund balance reached maximum in the past eight hours, Unix timestamp format in milliseconds, e.g. `1597026383085`(Deprecated, returns `""`. To be removed in a future update) |
| > adlType | String | ADL related events `rate_adl_start`: ADL begins due to high security fund decline rate `bal_adl_start`: ADL begins due to security fund balance falling `pos_adl_start`：ADL begins due to the volume of liquidation orders falls to a certain level (only applicable to premarket symbols) `adl_end`: ADL ends(Deprecated, returns `""`. To be removed in a future update) |
| > adlBal | String | security fund balance that triggers ADL(Deprecated, returns `""`. To be removed in a future update) |
| > adlRecBal | String | security fund balance that turns off ADL(Deprecated, returns `""`. To be removed in a future update) |
| > ts | String | Data push time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > decRate | String | Real-time security fund decline rate (compare bal and maxBal) Applicable when state is `warning` or `adl`(Deprecated) |
| > adlRate | String | security fund decline rate that triggers ADL(Deprecated) |
| > adlRecRate | String | security fund decline rate that turns off ADL(Deprecated) |

### Economic calendar channel

This endpoint is only supported in production environment.

Retrieve the most up-to-date economic calendar data. This endpoint is only applicable to VIP 1 and above users in the trading fee tier.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "economic-calendar"
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
 "channel": "economic-calendar"
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
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`economic-calendar` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "economic-calendar"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"economic-calendar\", \"instId\" : \"LTC-USD-190628\"}]}",
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
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "economic-calendar"
 },
 "data": [
 {
 "calendarId": "319275",
 "date": "1597026383085",
 "region": "United States",
 "category": "Manufacturing PMI",
 "event": "S&P Global Manufacturing PMI Final",
 "refDate": "1597026383085",
 "actual": "49.2",
 "previous": "47.3",
 "forecast": "49.3",
 "importance": "2",
 "prevInitial": "",
 "ccy": "",
 "unit": "",
 "ts": "1698648096590"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name`economic-calendar` |
| data | Array of objects | Subscribed data |
| > event | string | Event name |
| > region | string | Country, region or entity |
| > category | string | Category name |
| > actual | string | The actual value of this event |
| > previous | string | Latest actual value of the previous period The value will be revised if revision is applicable |
| > forecast | string | Average forecast among a representative group of economists |
| > prevInitial | string | The initial value of the previous period Only applicable when revision happens |
| > date | string | Estimated release time of the value of actual field, millisecond format of Unix timestamp, e.g. `1597026383085` |
| > refDate | string | Date for which the datapoint refers to |
| > calendarId | string | Calendar ID |
| > unit | string | Unit of the data |
| > ccy | string | Currency of the data |
| > importance | string | Level of importance`1`: low `2`: medium `3`: high |
| > ts | string | The time of the latest update |
