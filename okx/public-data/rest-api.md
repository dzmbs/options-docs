## REST API

### Get instruments

Retrieve a list of instruments with open contracts for OKX. Retrieve available instruments info of current account, please refer to [Get instruments](/docs-v5/en/#trading-account-rest-api-get-instruments).

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + Instrument Type

#### HTTP Request

`GET /api/v5/public/instruments`

**Request Example

```
GET /api/v5/public/instruments?instType=SPOT
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve a list of instruments with open contracts
result = publicDataAPI.get_instruments(
 instType="SPOT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`SPOT`: Spot`MARGIN`: Margin`SWAP`: Perpetual Futures`FUTURES`: Expiry Futures`OPTION`: Option`EVENTS`: Event Contracts |
| seriesId | String | Conditional | Series ID, e.g. `BTC-ABOVE-DAILY`. Required when instType is `EVENTS` |
| instFamily | String | Conditional | Instrument familyOnly applicable to `FUTURES`/`SWAP`/`OPTION`. If instType is `OPTION`, `instFamily` is required. |
| instId | String | No | Instrument ID |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
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
 "tradeQuoteCcyList": [
 "USDT"
 ],
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

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY`. Only applicable to `EVENTS` |
| instId | String | Instrument ID, e.g. `BTC-USD-SWAP` |
| uly | String | Underlying, e.g. `BTC-USD` Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION` |
| groupId | String | Instrument trading fee group IDSpot:`1`: Spot USDT`2`: Spot USDC & Crypto`3`: Spot TRY`4`: Spot EUR`5`: Spot BRL`7`: Spot AED`8`: Spot AUD`9`: Spot USD`10`: Spot SGD`11`: Spot zero`12`: Spot group one`13`: Spot group two`14`: Spot group three`15`: Spot special ruleExpiry futures:`1`: Expiry futures crypto-margined`2`: Expiry futures USDT-margined`3`: Expiry futures USDC-margined`4`: Expiry futures premarket`5`: Expiry futures group one`6`: Expiry futures group twoPerpetual futures:`1`: Perpetual futures crypto-margined`2`: Perpetual futures USDT-margined`3`: Perpetual futures USDC-margined`4`: Perpetual futures group one`5`: Perpetual futures group two `6`: Stock perpetual futures Options:`1`: Options crypto-margined`2`: Options USDC-marginedinstType and groupId should be used together to determine a trading fee group. Users should use this endpoint together with fee rates endpoint to get the trading fee of a specific symbol. Some enum values may not apply to you; the actual return values shall prevail. |
| instFamily | String | Instrument family, e.g. `BTC-USD` Only applicable to `MARGIN/FUTURES`/`SWAP`/`OPTION` |
| category | String | Currency category. Note: this parameter is already deprecated |
| baseCcy | String | Base currency, e.g. `BTC` in`BTC-USDT` Only applicable to `SPOT`/`MARGIN` |
| quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT` Only applicable to `SPOT`/`MARGIN` |
| settleCcy | String | Settlement and margin currency, e.g. `BTC` Only applicable to `FUTURES`/`SWAP`/`OPTION` |
| ctVal | String | Face value of one contract. Denomination depends on `ctType`: for linear contracts, `ctVal` is in the base currency (e.g., ctVal=0.01 BTC for BTC-USDT-SWAP); for inverse contracts, `ctVal` is in USD (e.g., ctVal=100 USD for BTC-USD-SWAP). Notional: linear = sz × ctVal × markPx (in quote ccy); inverse = sz × ctVal (in USD, fixed). Only applicable to `FUTURES`/`SWAP`/`OPTION` |
| ctMult | String | Contract multiplier Only applicable to `FUTURES`/`SWAP`/`OPTION` |
| ctValCcy | String | Contract value currency Only applicable to `FUTURES`/`SWAP`/`OPTION` |
| optType | String | Option type, `C`: Call `P`: put Only applicable to `OPTION` |
| stk | String | Strike price Only applicable to `OPTION` |
| listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| auctionEndTime | String | The end time of call auction, Unix timestamp format in milliseconds, e.g. `1597026383085` Only applicable to `SPOT` that are listed through call auctions, return "" in other cases (deprecated, use contTdSwTime) |
| contTdSwTime | String | Continuous trading switch time. The switch time from call auction, prequote to continuous trading, Unix timestamp format in milliseconds. e.g. `1597026383085`. Only applicable to `SPOT`/`MARGIN` that are listed through call auction or prequote, return "" in other cases. |
| preMktSwTime | String | The time premarket swap switched to normal swap, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable premarket `SWAP` |
| openType | String | Open type `fix_price`: fix price opening`pre_quote`: pre-quote`call_auction`: call auction Only applicable to `SPOT`/`MARGIN`, return "" for all other business lines |
| expTime | String | Expiry time Applicable to `SPOT`/`MARGIN`/`FUTURES`/`SWAP`/`OPTION`. For `FUTURES`/`OPTION`, it is natural delivery/exercise time. It is the instrument offline time when there is `SPOT/MARGIN/FUTURES/SWAP/` manual offline. Update once change. |
| lever | String | Exchange-defined maximum leverage ceiling for this instrument. The actual leverage available to a specific account may be lower based on VIP tier and position size. Use GET /api/v5/account/leverage-info for the user's current configured leverage. Not applicable to `SPOT`, `OPTION` |
| tickSz | String | Minimum price increment, e.g. `0.0001`.For `OPTION`/`EVENTS`, it is the minimum tickSz among tick band. Use "Get instrument tick bands" endpoint with the corresponding `instType` for accurate tickSz per price range. |
| lotSz | String | Lot size — the minimum order size increment. All order quantities (sz) must be a multiple of `lotSz`. Violation returns error 51121.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| minSz | String | Minimum order size. Order size must satisfy both: sz ≥ `minSz` AND sz is a multiple of `lotSz`.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| ctType | String | Contract type`linear`: linear contract — margin, P&L, and settlement in the quote currency (e.g., USDT for BTC-USDT-SWAP).`inverse`: inverse contract — margin, P&L, and settlement in the base currency (e.g., BTC for BTC-USD-SWAP). For inverse contracts, P&L in USD terms is non-linear: the USD value of a fixed BTC gain changes with the BTC price. Only applicable to `FUTURES`/`SWAP` |
| alias | String | Contract alias (deprecated — use expTime to obtain the delivery time, will be removed by the end of April 2026)`this_week``next_week``this_month``next_month``quarter``next_quarter``third_quarter``this_five_years`: current 5-year contract`next_five_years`: next 5-year contractOnly applicable to `FUTURES` |
| state | String | Instrument status`live` `suspend``rebase`: can’t be traded during rebasing, only applicable to `SWAP``post_only`: only post-only orders are accepted; existing post-only orders can be amended and cancelled. Other order types (market, IOC, FOK, normal limit) are rejected. Only applicable to `SWAP``preopen`. e.g. There will be `preopen` before the Futures and Options new contracts state is live.`test`: Test pairs, can’t be traded`settling`: Settling, only applicable to `EVENTS` |
| ruleType | String | Trading rule types`normal`: normal trading`pre_market`: pre-market trading`rebase_contract`: pre-market rebase contract`xperp`: perpetual-style futures, only applicable to certain `FUTURES` contracts |
| maxLmtSz | String | The maximum order quantity of a single limit order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| maxMktSz | String | The maximum order quantity of a single market order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`. |
| maxLmtAmt | String | Max USD amount for a single limit order |
| maxMktAmt | String | Max USD amount for a single market order Only applicable to `SPOT`/`MARGIN` |
| maxTwapSz | String | The maximum order quantity of a single TWAP order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. The minimum order quantity of a single TWAP order is minSz*2 |
| maxIcebergSz | String | The maximum order quantity of a single iceBerg order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| maxTriggerSz | String | The maximum order quantity of a single trigger order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `base currency`. |
| maxStopSz | String | The maximum order quantity of a single stop market order.If it is a derivatives contract, the value is the number of contracts.If it is `SPOT`/`MARGIN`, the value is the quantity in `USDT`. |
| futureSettlement | Boolean | Whether daily settlement for expiry feature is enabledApplicable to `FUTURES` `cross` |
| tradeQuoteCcyList | Array of strings | List of quote currencies available for trading, e.g. ["USD", "USDC”]. |
| instIdCode | Integer | Instrument ID code. For simple binary encoding, you must use `instIdCode` instead of `instId`.For the same `instId`, it's value may be different between production and demo trading. It is `null` when the value is not generated. |
| instCategory | String | The asset category of the instrument’s base asset (the first segment of the instrument ID). For example, for `BTC-USDT-SWAP`, the `instCategory` represents the asset category of `BTC`. `1`: Crypto `3`: Stocks `4`: Commodities `5`: Forex `6`: Bonds `""`: Not available |
| upcChg | Array of objects | Upcoming changes. It is [] when there is no upcoming change. |
| > param | String | The parameter name to be updated. `tickSz` `minSz`: For `FUTURES`/`SWAP`, `lotSz` will be modified synchronously. `maxMktSz` |
| > newValue | String | The parameter value that will replace the current one. |
| > effTime | String | Effective time. Unix timestamp format in milliseconds, e.g. `1597026383085` |

 When a new contract is going to be listed, the instrument data of the new contract will be available with status preopen.
 When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available

 listTime and contTdSwTime
For spot symbols listed through a call auction or pre-open, listTime represents the start time of the auction or pre-open, and contTdSwTime indicates the end of the auction or pre-open and the start of continuous trading. For other scenarios, listTime will mark the beginning of continuous trading, and contTdSwTime will return an empty value "".

state
For `SPOT`, `MARGIN`, `SWAP`, and `FUTURES`, the state changes from `preopen` to `live` when the `listTime` is reached. For `OPTION` contracts, the state may change to `live` slightly after `listTime` due to internal processing. It is recommended to verify that `state` is `live` before placing orders.
When a product is going to be delisted (e.g. when a FUTURES contract is settled or OPTION contract is exercised), the instrument will not be available.

Instruments REST endpoints and WebSocket channel will update `expTime` once the delisting announcement is published.
Instruments REST endpoint and WebSocket channel will update `listTime` once the listing announcement is published:

1. For `SPOT/MARGIN/SWAP`, this event is only applicable to `instType`, `instId`, `listTime`, `state`.
2. For `FUTURES`, this event is only applicable to `instType`, `instFamily`, `listTime`, `state`.
3. Other fields will be "" temporarily, but they will be updated at least 5 minutes in advance of the `listTime`, then the WebSocket subscription using related `instId`/`instFamily` can be available.

### Get series

Retrieve the list of series for OKX prediction markets.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Public

#### HTTP Request

`GET /api/v5/public/event-contract/series`

Request Example

```
GET /api/v5/public/event-contract/series?seriesId=BTC-ABOVE-DAILY
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| seriesId | String | No | Series ID, e.g. `BTC-ABOVE-DAILY`. If not passed, all series will be returned. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "seriesId": "BTC-ABOVE-DAILY",
 "freq": "daily",
 "title": "BTC price above 15k",
 "category": "Crypto",
 "settlement": {
 "method": "price_above",
 "closeEarly": false,
 "srcName": "okx_index",
 "underlying": "BTC-USDT"
 }
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY` |
| freq | String | Frequency of the series`five_min``fifteen_min``hourly``daily` |
| title | String | Series title |
| category | String | Category which this series belongs to, e.g. `Crypto` |
| settlement | Object | Settlement information |
| > method | String | Settlement method.`price_up_down`: Price up/down`price_above`: Price above |
| > closeEarly | Boolean | Whether the market can be settled earlier than the expiration time.`true``false` |
| > srcName | String | Settlement source name, e.g. `okx_index`, `cf_benchmark_index` |
| > underlying | String | Price underlying in OKX trading symbol format, e.g. `BTC-USDT`. Only applicable to price-related settlement methods. |

### Get events

Get events for a series in OKX prediction markets. Returns all event records, including expired ones. Return data in expTime and eventId descending order.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Public

#### HTTP Request

`GET /api/v5/public/event-contract/events`

Request Example

```
GET /api/v5/public/event-contract/events?seriesId=BTC-ABOVE-DAILY
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| seriesId | String | Yes | Series ID, e.g. `BTC-ABOVE-DAILY` |
| eventId | String | No | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600` |
| state | String | No | Event state filter.`preopen``live``settling``expired` |
| limit | String | No | Number of results per request. Maximum is 100. Default is 100. |
| before | String | No | Pagination. Returns records newer than the requested `expTime`, not included. |
| after | String | No | Pagination. Returns records earlier than the requested `expTime`, not included. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "seriesId": "BTC-ABOVE-DAILY",
 "eventId": "BTC-ABOVE-DAILY-260224-1600",
 "expTime": "1769697132335",
 "state": "live"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY` |
| eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600` |
| fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method. |
| expTime | String | The specific strike time this event is based on, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| state | String | Event state.`preopen``live``settling``expired` |

### Get markets

Get markets for events in OKX prediction markets. Return data in expTime and floorStrike descending order.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Public

#### HTTP Request

`GET /api/v5/public/event-contract/markets`

Request Example

```
GET /api/v5/public/event-contract/markets?seriesId=BTC-ABOVE-DAILY
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| seriesId | String | Yes | Series ID, e.g. `BTC-ABOVE-DAILY` |
| eventId | String | No | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600` |
| instId | String | No | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000` |
| state | String | No | Filter by market status.`preopen``live``settling``expired` |
| limit | String | No | Number of results per request. Maximum is 100. Default is 100. |
| before | String | No | Pagination. Returns records newer than the requested `expTime`, not included. |
| after | String | No | Pagination. Returns records earlier than the requested `expTime`, not included. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "seriesId": "BTC-ABOVE-DAILY",
 "eventId": "BTC-ABOVE-DAILY-260224-1600",
 "instId": "BTC-ABOVE-DAILY-260224-1600-65000",
 "listTime": "1769697132335",
 "expTime": "1769697132335",
 "state": "live",
 "fixTime": "",
 "outcome": "0",
 "floorStrike": "120000",
 "settleValue": "",
 "disputed": false
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| seriesId | String | Series ID, e.g. `BTC-ABOVE-DAILY` |
| eventId | String | Event ID, e.g. `BTC-ABOVE-DAILY-260224-1600` |
| instId | String | Instrument ID, e.g. `BTC-ABOVE-DAILY-260224-1600-65000` |
| listTime | String | Listing time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| fixTime | String | Strike price fixing time, Unix timestamp format in milliseconds, e.g. `1597026383085`. Only applicable to `price_up_down` settlement method. |
| expTime | String | Strike time for this event, Unix timestamp format in milliseconds, e.g. `1597026383085`. Updated once the market is settled. |
| state | String | Market state.`preopen``live``settling``expired` |
| disputed | Boolean | Whether the market has been disputed.`true``false` |
| outcome | String | Market outcome.`0`: Not available`1`: YES`2`: NO.`1`/`2` only applicable when state is `expired` |
| floorStrike | String | Minimum expiration value that leads to a YES outcome |
| settleValue | String | Settlement valueOnly return when the state is `expired` |

### Get estimated delivery/exercise price

Retrieve the estimated delivery price which will only have a return value one hour before the delivery/exercise.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/estimated-price`

Request Example

```
GET /api/v5/public/estimated-price?instId=BTC-USD-200214
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve estimated delivery/exercise price
result = publicDataAPI.get_estimated_price(
 instId = "BTC-USD-200214",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USD-200214` only applicable to `FUTURES`/`OPTION`/`EVENTS` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "instType":"FUTURES",
 "instId":"BTC-USDT-201227",
 "settlePx":"200",
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`FUTURES``OPTION` |
| instId | String | Instrument ID, e.g. `BTC-USD-200214` |
| settlePx | String | Estimated delivery/exercise price |
| ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get delivery/exercise history

Retrieve delivery records of Futures and exercise records of Options in the last 3 months.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP + (Instrument Type + instFamily)

#### HTTP Request

`GET /api/v5/public/delivery-exercise-history`

Request Example

```
GET /api/v5/public/delivery-exercise-history?instType=OPTION&instFamily=BTC-USD
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve delivery records of Futures and exercise records of Options in the last 3 months
result = publicDataAPI.get_delivery_exercise_history(
 instType="FUTURES",
 uly="BTC-USD"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`FUTURES``OPTION` |
| instFamily | String | Yes | Instrument family, only applicable to `FUTURES`/`OPTION` |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| before | String | No | Pagination of data to return records newer than the requested `ts` |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "ts":"1597026383085",
 "details":[
 {
 "type":"delivery",
 "insId":"BTC-USD-190927",
 "px":"0.016"
 }
 ]
 },
 {
 "ts":"1597026383085",
 "details":[
 {
 "insId":"BTC-USD-200529-6000-C",
 "type":"exercised",
 "px":"0.016"
 },
 {
 "insId":"BTC-USD-200529-8000-C",
 "type":"exercised",
 "px":"0.016"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Delivery/exercise time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| details | Array of objects | Delivery/exercise details |
| > insId | String | Delivery/exercise contract ID |
| > px | String | Delivery/exercise price |
| > type | String | Type `delivery` `exercised` `expired_otm`:Out of the money |

### Get estimated future settlement price

Retrieve the estimated settlement price which will only have a return value one hour before the settlement.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/estimated-settlement-info`

Request Example

```
GET /api/v5/public/estimated-settlement-info?instId=XRP-USDT-250307
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `XRP-USDT-250307` only applicable to `FUTURES` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "estSettlePx": "2.5666068562369959",
 "instId": "XRP-USDT-250307",
 "nextSettleTime": "1741248000000",
 "ts": "1741246429748"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. `XRP-USDT-250307` |
| nextSettleTime | String | Next settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| estSettlePx | String | Estimated settlement price |
| ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get futures settlement history

Retrieve settlement records of futures in the last 3 months.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP + (Instrument Family)

#### HTTP Request

`GET /api/v5/public/settlement-history`

Request Example

```
GET /api/v5/public/settlement-history?instFamily=XRP-USD
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instFamily | String | Yes | Instrument family |
| after | String | No | Pagination of data to return records earlier than (not include) the requested `ts` |
| before | String | No | Pagination of data to return records newer than (not include) the requested `ts` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "details": [
 {
 "instId": "XRP-USDT-250307",
 "settlePx": "2.5192078615298715"
 }
 ],
 "ts": "1741161600000"
 },
 {
 "details": [
 {
 "instId": "XRP-USDT-250307",
 "settlePx": "2.5551316341327384"
 }
 ],
 "ts": "1741075200000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| details | Array of objects | Settlement info |
| > instId | String | Instrument ID |
| > settlePx | String | Settlement price |

### Get funding rate

Retrieve funding rate.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/funding-rate`

Request Example

```
GET /api/v5/public/funding-rate?instId=BTC-USD-SWAP
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve funding rate
result = publicDataAPI.get_funding_rate(
 instId="BTC-USD-SWAP",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` or X-Perps futures instId, or `ANY` to return the funding rate info of all perpetual and X-Perps futures contractsApplicable to `SWAP` and X-Perps `FUTURES` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "formulaType": "noRate",
 "fundingRate": "0.0000182221218054",
 "fundingTime": "1743609600000",
 "impactValue": "",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "interestRate": "",
 "maxFundingRate": "0.00375",
 "method": "current_period",
 "minFundingRate": "-0.00375",
 "nextFundingRate": "",
 "nextFundingTime": "1743638400000",
 "premium": "0.0000910113652644",
 "settFundingRate": "0.0000145824401745",
 "settState": "settled",
 "ts": "1743588686291"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`SWAP`: Perpetual futures`FUTURES`: X-Perps futures |
| instId | String | Instrument ID, e.g. `BTC-USD-SWAP` or `ANY` |
| method | String | Funding rate mechanism `current_period` `next_period`(no longer supported) |
| formulaType | String | Formula type`noRate`: old funding rate formula`withRate`: new funding rate formula |
| fundingRate | String | Predicted funding rate for the upcoming settlement period. Sign: positive = long positions pay short positions at the next `fundingTime`; negative = short positions pay long positions. This is a forecast — the final settled rate may differ. See `settFundingRate` for the last settled rate. Note: the settlement interval is typically 8 hours but may be adjusted; use the difference between `fundingTime` and `nextFundingTime` to determine the actual interval. |
| nextFundingRate | String | Forecasted funding rate for the next period The nextFundingRate will be "" if the method is `current_period`(no longer supported) |
| fundingTime | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| nextFundingTime | String | Forecasted funding time for the next period , Unix timestamp format in milliseconds, e.g. `1597026383085` |
| minFundingRate | String | The lower limit of the funding rate |
| maxFundingRate | String | The upper limit of the funding rate |
| interestRate | String | Interest rate |
| impactValue | String | Depth weighted amount (in the unit of quote currency) |
| settState | String | Settlement state of funding rate `processing` `settled` |
| settFundingRate | String | If settState = `processing`, it is the funding rate that is being used for current settlement cycle. If settState = `settled`, it is the funding rate that is being used for previous settlement cycle |
| premium | String | Premium index formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price |
| ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

For some altcoins perpetual swaps with significant fluctuations in funding rates, OKX will closely monitor market changes. When necessary, the funding rate collection frequency, currently set at 8 hours, may be adjusted to higher frequencies such as 6 hours, 4 hours, 2 hours, or 1 hour. Thus, users should focus on the difference between `fundingTime` and `nextFundingTime` fields to determine the funding fee interval of a contract.

### Get funding rate history

Retrieve funding rate history. This endpoint can return data up to three months.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/funding-rate-history`

Request Example

```
GET /api/v5/public/funding-rate-history?instId=BTC-USD-SWAP
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve funding rate history
result = publicDataAPI.funding_rate_history(
 instId="BTC-USD-SWAP",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` or X-Perps futures instIdApplicable to `SWAP` and X-Perps `FUTURES` |
| before | String | No | Pagination of data to return records newer than the requested `fundingTime` |
| after | String | No | Pagination of data to return records earlier than the requested `fundingTime` |
| limit | String | No | Number of results per request. The maximum is `400`; The default is `400` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "formulaType": "noRate",
 "fundingRate": "0.0000746604960499",
 "fundingTime": "1703059200000",
 "instId": "BTC-USD-SWAP",
 "instType": "SWAP",
 "method": "next_period",
 "realizedRate": "0.0000746572360545"
 },
 {
 "formulaType": "noRate",
 "fundingRate": "0.000227985782722",
 "fundingTime": "1703030400000",
 "instId": "BTC-USD-SWAP",
 "instType": "SWAP",
 "method": "next_period",
 "realizedRate": "0.0002279755647389"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`SWAP`: Perpetual futures`FUTURES`: X-Perps futures |
| instId | String | Instrument ID, e.g. `BTC-USD-SWAP` |
| formulaType | String | Formula type`noRate`: old funding rate formula`withRate`: new funding rate formula |
| fundingRate | String | Predicted funding rate |
| realizedRate | String | Actual funding rate |
| fundingTime | String | Settlement time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| method | String | Funding rate mechanism `current_period` `next_period` |

For some altcoins perpetual swaps with significant fluctuations in funding rates, OKX will closely monitor market changes. When necessary, the funding rate collection frequency, currently set at 8 hours, may be adjusted to higher frequencies such as 6 hours, 4 hours, 2 hours, or 1 hour. Thus, users should focus on the difference between `fundingTime` and `nextFundingTime` fields to determine the funding fee interval of a contract.

### Get open interest

Retrieve the total open interest for contracts on OKX.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/open-interest`

Request Example

```
GET /api/v5/public/open-interest?instType=SWAP
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve the total open interest for contracts on OKX
result = publicDataAPI.get_open_interest(
 instType="SWAP",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | Conditional | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION`If instType is `OPTION`, instFamily is required. |
| instId | String | No | Instrument ID, e.g. `BTC-USDT-SWAP`Applicable to `FUTURES`/`SWAP`/`OPTION`/`EVENTS` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "instType":"SWAP",
 "instId":"BTC-USDT-SWAP",
 "oi":"5000",
 "oiCcy":"555.55",
 "oiUsd": "50000",
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| oi | String | Open interest in number of contracts |
| oiCcy | String | Open interest in number of coin |
| oiUsd | String | Open interest in number of USD |
| ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get limit price

Retrieve the highest buy limit and lowest sell limit of the instrument.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/price-limit`

Request Example

```
GET /api/v5/public/price-limit?instId=BTC-USDT-SWAP
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve the highest buy limit and lowest sell limit of the instrument
result = publicDataAPI.get_price_limit(
 instId="BTC-USD-SWAP",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "instType":"SWAP",
 "instId":"BTC-USDT-SWAP",
 "buyLmt":"17057.9",
 "sellLmt":"16388.9",
 "ts":"1597026383085",
 "enabled": true
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| buyLmt | String | Highest buy limit Return "" when enabled is false |
| sellLmt | String | Lowest sell limit Return "" when enabled is false |
| ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| enabled | Boolean | Whether price limit is effective `true`: the price limit is effective `false`: the price limit is not effective |

### Get option market data

Retrieve option market data.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP + instFamily

#### HTTP Request

`GET /api/v5/public/opt-summary`

Request Example

```
GET /api/v5/public/opt-summary?uly=BTC-USD
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve option market data
result = publicDataAPI.get_opt_summary(
 uly="BTC-USD",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instFamily | String | Yes | Instrument family, only applicable to `OPTION` |
| expTime | String | No | Contract expiry date, the format is "YYMMDD", e.g. "200527" |

Note**: This endpoint may not return data for every option listed in [`/api/v5/public/instruments`](#get-instruments). Data can be absent in two cases:
1. The option is listed but not yet tradeable (e.g. supplemental options may not become tradeable until a scheduled time; data will not be available before trading opens).
2. Implied volatility surface fitting fails due to insufficient market quotes. This is more likely to occur in demo trading; in live trading, market maker quotes are generally available to ensure fitting succeeds.

**Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "askVol": "3.7207056835937498",
 "bidVol": "0",
 "delta": "0.8310206676289528",
 "deltaBS": "0.9857332101544538",
 "fwdPx": "39016.8143629068452065",
 "gamma": "-1.1965483553276135",
 "gammaBS": "0.000011933182397798109",
 "instId": "BTC-USD-220309-33000-C",
 "instType": "OPTION",
 "lever": "0",
 "markVol": "1.5551965233045728",
 "realVol": "0",
 "volLv": "0",
 "theta": "-0.0014131955002093717",
 "thetaBS": "-66.03526900575946",
 "ts": "1646733631242",
 "uly": "BTC-USD",
 "vega": "0.000018173851073258973",
 "vegaBS": "0.7089307622132419"
 },
 {
 "askVol": "1.7968814062499998",
 "bidVol": "0",
 "delta": "-0.014668822072611904",
 "deltaBS": "-0.01426678984554619",
 "fwdPx": "39016.8143629068452065",
 "gamma": "0.49483062407551576",
 "gammaBS": "0.000011933182397798109",
 "instId": "BTC-USD-220309-33000-P",
 "instType": "OPTION",
 "lever": "0",
 "markVol": "1.5551965233045728",
 "realVol": "0",
 "volLv": "0",
 "theta": "-0.0014131955002093717",
 "thetaBS": "-54.93377294845015",
 "ts": "1646733631242",
 "uly": "BTC-USD",
 "vega": "0.000018173851073258973",
 "vegaBS": "0.7089307622132419"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`OPTION` |
| instId | String | Instrument ID, e.g. `BTC-USD-200103-5500-C` |
| uly | String | Underlying |
| delta | String | Sensitivity of option price to `uly` price |
| gamma | String | The delta is sensitivity to `uly` price |
| vega | String | Sensitivity of option price to implied volatility |
| theta | String | Sensitivity of option price to remaining maturity |
| deltaBS | String | Sensitivity of option price to `uly` price in BS mode |
| gammaBS | String | The delta is sensitivity to `uly` price in BS mode |
| vegaBS | String | Sensitivity of option price to implied volatility in BS mode |
| thetaBS | String | Sensitivity of option price to remaining maturity in BS mode |
| lever | String | Leverage |
| markVol | String | Mark volatility |
| bidVol | String | Bid volatility |
| askVol | String | Ask volatility |
| realVol | String | Realized volatility (not currently used) |
| volLv | String | Implied volatility of at-the-money options |
| fwdPx | String | Forward price |
| ts | String | Data update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get discount rate and interest-free quota

Retrieve discount rate level and interest-free quota.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/discount-rate-interest-free-quota`

Request Example

```
GET /api/v5/public/discount-rate-interest-free-quota?ccy=BTC
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve discount rate level and interest-free quota
result = publicDataAPI.discount_interest_free_quota()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency |
| discountLv | String | No | Discount level (Deprecated) |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "amt": "0",
 "ccy": "BTC",
 "collateralRestrict": false,
 "details": [
 {
 "discountRate": "0.98",
 "liqPenaltyRate": "0.02",
 "maxAmt": "20",
 "minAmt": "0",
 "tier": "1",
 "disCcyEq": "1000"
 },
 {
 "discountRate": "0.9775",
 "liqPenaltyRate": "0.0225",
 "maxAmt": "25",
 "minAmt": "20",
 "tier": "2",
 "disCcyEq": "2000"
 }
 ],
 "discountLv": "1",
 "minDiscountRate": "0"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| colRes | String | Platform level collateral restriction status `0`: The restriction is not enabled. `1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit. `2`: The restriction is enabled. This crypto can't be used as margin for your new orders. This may result in failed orders. But it will still be included in the account's adjusted equity and doesn't impact margin ratio. Refer to Introduction to the platform collateralized borrowing limit for more details. |
| collateralRestrict | Boolean | Platform level collateralized borrow restriction `true` `false`(deprecated, use colRes instead) |
| amt | String | Interest-free quota |
| discountLv | String | Discount rate level.(Deprecated) |
| minDiscountRate | String | Minimum discount rate when it exceeds the maximum amount of the last tier. |
| details | Array of objects | New discount details. |
| > discountRate | String | Discount rate |
| > maxAmt | String | Tier - upper bound. The unit is the currency like BTC. "" means positive infinity |
| > minAmt | String | Tier - lower bound. The unit is the currency like BTC. The minimum is 0 |
| > tier | String | Tiers |
| > liqPenaltyRate | String | Liquidation penalty rate |
| > disCcyEq | String | Discount equity in currency for quick calculation if your equity is the`maxAmt` |

### Get system time

Retrieve API server time.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/time`

Request Example

```
GET /api/v5/public/time
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve API server time
result = publicDataAPI.get_system_time()
print(result)
```

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | System time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get mark price

Retrieve mark price.

We set the mark price based on the SPOT index and at a reasonable basis to prevent individual users from manipulating the market and causing the contract price to fluctuate.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/public/mark-price`

Request Example

```
GET /api/v5/public/mark-price?instType=SWAP
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve mark price
result = publicDataAPI.get_mark_price(
 instType="SWAP",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instId | String | No | Instrument ID, e.g. `BTC-USD-SWAP` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "instType":"SWAP",
 "instId":"BTC-USDT-SWAP",
 "markPx":"200",
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instId | String | Instrument ID, e.g. `BTC-USD-200214` |
| markPx | String | Mark price |
| ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get position tiers

Retrieve position tiers information, maximum leverage depends on your borrowings and Maintenance margin ratio.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/position-tiers`

Request Example

```
GET /api/v5/public/position-tiers?tdMode=cross&instType=SWAP&instFamily=BTC-USDT
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve position tiers information
result = publicDataAPI.get_position_tiers(
 instType="SWAP",
 tdMode="cross",
 uly="BTC-USD"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`MARGIN``SWAP``FUTURES``OPTION` |
| tdMode | String | Yes | Trade modeMargin mode `cross` `isolated` |
| instFamily | String | Conditional | Single instrument familiy or multiple instrument families (no more than 5) separated with comma.If instType is `SWAP/FUTURES/OPTION`, `instFamily` is required. |
| instId | String | Conditional | Single instrument or multiple instruments (no more than 5) separated with comma.Either instId or ccy is required, if both are passed, instId will be used, ignore when instType is one of `SWAP`,`FUTURES`,`OPTION` |
| ccy | String | Conditional | Margin currencyOnly applicable to cross MARGIN. It will return borrowing amount for `Multi-currency margin` and `Portfolio margin` when `ccy` takes effect. |
| tier | String | No | Tiers |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "baseMaxLoan": "50",
 "imr": "0.1",
 "instId": "BTC-USDT",
 "maxLever": "10",
 "maxSz": "50",
 "minSz": "0",
 "mmr": "0.03",
 "optMgnFactor": "0",
 "quoteMaxLoan": "500000",
 "tier": "1",
 "uly": "",
 "instFamily": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| uly | String | UnderlyingApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instFamily | String | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instId | String | Instrument ID |
| tier | String | Tiers |
| minSz | String | The minimum borrowing amount or position of this gear is only applicable to margin/options/perpetual/delivery, the minimum position is 0 by defaultIt will return the minimum borrowing amount when `ccy` takes effect. |
| maxSz | String | The maximum borrowing amount or number of positions held in this position is only applicable to margin/options/perpetual/deliveryIt will return the maximum borrowing amount when `ccy` takes effect. |
| mmr | String | Position maintenance margin requirement rate |
| imr | String | Initial margin requirement rate |
| maxLever | String | Maximum available leverage |
| optMgnFactor | String | Option Margin Coefficient (only applicable to options) |
| quoteMaxLoan | String | Quote currency borrowing amount (only applicable to leverage and the case when `instId` takes effect) |
| baseMaxLoan | String | Base currency borrowing amount (only applicable to leverage and the case when `instId` takes effect) |

### Get interest rate and loan quota

Retrieve interest rate

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/interest-rate-loan-quota`

Request Example

```
GET /api/v5/public/interest-rate-loan-quota
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve interest rate and loan quota
result = publicDataAPI.get_interest_rate_loan_quota()
print(result)
```

Response Example

```
{
 "code": "0",
 "data": [
 {
 "configCcyList": [
 {
 "ccy": "USDT",
 "rate": "0.00043728",
 }
 ],
 "basic": [
 {
 "ccy": "USDT",
 "quota": "500000",
 "rate": "0.00043728"
 },
 {
 "ccy": "BTC",
 "quota": "10",
 "rate": "0.00019992"
 }
 ],
 "vip": [
 {
 "irDiscount": "",
 "loanQuotaCoef": "6",
 "level": "VIP1"
 },
 {
 "irDiscount": "",
 "loanQuotaCoef": "7",
 "level": "VIP2"
 }
 ],
 "config": [
 {
 "ccy": "USDT",
 "stgyType": "0", // normal
 "quota": "xxxxxx",
 "level": "VIP 8"
 },
 ......
 {
 "ccy": "USDT",
 "stgyType": "1", // delta neutral
 "quota": "xxxxx",
 "level": "VIP 1"
 },
 ......
 ],
 "regular": [
 {
 "irDiscount": "",
 "loanQuotaCoef": "1",
 "level": "Lv1"
 },
 {
 "irDiscount": "",
 "loanQuotaCoef": "2",
 "level": "Lv1"
 }
 ]
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| basic | Array of objects | Basic interest rate |
| > ccy | String | Currency |
| > rate | String | Daily borrowing rate |
| > quota | String | Max borrow |
| vip | Array of objects | Interest info for vip users |
| > level | String | VIP Level, e.g. `VIP1` |
| > loanQuotaCoef | String | Loan quota coefficient. Loan quota = `quota` * `level` |
| > irDiscount | String | Interest rate discount(Deprecated) |
| regular | Array of objects | Interest info for regular users |
| > level | String | Regular user Level, e.g. `Lv1` |
| > loanQuotaCoef | String | Loan quota coefficient. Loan quota = `quota` * `level` |
| > irDiscount | String | Interest rate discount(Deprecated) |
| configCcyList | Array of strings | Currencies that have loan quota configured using customized absolute value.Users should refer to config to get the loan quota of a currency which is listed in configCcyList, instead of getting it from basic/vip/regular. |
| > ccy | String | Currency |
| > rate | String | Daily rate |
| config | Array of objects | The currency details of loan quota configured using customized absolute value |
| > ccy | String | Currency |
| > stgyType | String | Strategy type`0`: general strategy`1`: delta neutral strategyIf only `0` is returned for a currency, it means the loan quota is shared between accounts in general strategy and accounts in delta neutral strategy; if both `0/1` are returned for a currency, it means accounts in delta neutral strategy have separate loan quotas. |
| > quota | String | Loan quota in absolute value |
| > level | String | VIP level |

### Get underlying

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/underlying`

Request Example

```
GET /api/v5/public/underlying?instType=FUTURES
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Get underlying
result = publicDataAPI.get_underlying(
 instType="FUTURES"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`SWAP``FUTURES``OPTION` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "LTC-USDT",
 "BTC-USDT",
 "ETC-USDT"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| uly | Array | Underlying |

### Get security fund

Get security fund balance information

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/insurance-fund`

Request Example

```
GET /api/v5/public/insurance-fund?instType=SWAP&uly=BTC-USD
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Get security fund balance information
result = publicDataAPI.get_insurance_fund(
 instType="SWAP",
 uly="BTC-USD"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`MARGIN``SWAP``FUTURES``OPTION` |
| type | String | No | Type`liquidation_balance_deposit``bankruptcy_loss``platform_revenue`(Deprecated, returns empty values. To be removed in a future update) `adl`(Deprecated, returns empty values. To be removed in a future update) The default is `all type` |
| instFamily | String | Conditional | Instrument familyRequired for `FUTURES`/`SWAP`/`OPTION` |
| ccy | String | Conditional | Currency, only applicable to `MARGIN` |
| before | String | No | Pagination of data to return records newer than the requested `ts` |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "details": [
 {
 "adlType": "",
 "amt": "1343.1308",
 "balance": "1369179138.7489",
 "ccy": "ETH",
 "maxBal": "",
 "maxBalTs": "",
 "ts": "1704883083000",
 "type": "liquidation_balance_deposit"
 }
 ],
 "instFamily": "ETH-USD",
 "instType": "OPTION",
 "total": "1369179138.7489"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| total | String | The total balance of security fund, in `USD` |
| instFamily | String | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instType | String | Instrument type |
| details | Array of objects | security fund data |
| > balance | String | The balance of security fund |
| > amt | String | The change in the balance of security fund Applicable when type is `liquidation_balance_deposit` or `bankruptcy_loss` |
| > ccy | String | The currency of security fund |
| > type | String | The type of security fund`liquidation_balance_deposit``bankruptcy_loss``platform_revenue`(Deprecated, returns empty values)`adl`(Deprecated, returns empty values) |
| > maxBal | String | Maximum security fund balance in the past eight hours Only applicable when type is `adl`(Deprecated, returns empty values) |
| > maxBalTs | String | Timestamp when security fund balance reached maximum in the past eight hours, Unix timestamp format in milliseconds, e.g. `1597026383085` Only applicable when type is `adl`(Deprecated, returns empty values) |
| > decRate | String | Real-time security fund decline rate (compare balance and maxBal) Only applicable when type is `adl`(Deprecated) |
| > adlType | String | ADL related events `rate_adl_start`: ADL begins due to high security fund decline rate `bal_adl_start`: ADL begins due to security fund balance falling `pos_adl_start`：ADL begins due to the volume of liquidation orders falls to a certain level (only applicable to premarket symbols) `adl_end`: ADL ends Only applicable when type is `adl`(Deprecated, returns empty values) |
| > ts | String | The update timestamp of security fund. Unix timestamp format in milliseconds, e.g. `1597026383085` |

The `regular_update` type has been removed. The `adl` and `platform_revenue` types are deprecated and currently return empty values; they will be removed in a future update. The `amt` field presents the difference in security fund balance when the `type` is `liquidation_balance_deposit` or `bankruptcy_loss`, which is generated once per day around 08:00 am (UTC).

### Unit convert

Convert the crypto value to the number of contracts, or vice versa

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/convert-contract-coin`

Request Example

```
GET /api/v5/public/convert-contract-coin?instId=BTC-USD-SWAP&px=35000&sz=0.888
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Convert the crypto value to the number of contracts, or vice versa
result = publicDataAPI.get_convert_contract_coin(
 instId="BTC-USD-SWAP",
 px="35000",
 sz="0.888"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | String | No | Convert type`1`: Convert currency to contract`2`: Convert contract to currencyThe default is `1` |
| instId | String | Yes | Instrument IDonly applicable to `FUTURES`/`SWAP`/`OPTION` |
| sz | String | Yes | Quantity to buy or sellIt is quantity of currency while converting currency to contract; It is quantity of contract while converting contract to currency. |
| px | String | Conditional | Order priceFor crypto-margined contracts, it is necessary while converting.For USDT-margined contracts, it is necessary while converting between usdt and contract.It is optional while converting between coin and contract. For OPTION, it is optional. |
| unit | String | No | The unit of currency`coin``usds`: USDT/USDCThe default is `coin`, only applicable to USDⓈ-margined contracts from `FUTURES`/`SWAP` |
| opType | String | No | Order type`open`: round down sz when opening positions `close`: round sz to the nearest when closing positions The default is `close` Applicable to `FUTURES` `SWAP` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "instId": "BTC-USD-SWAP",
 "px": "35000",
 "sz": "311",
 "type": "1",
 "unit": "coin"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| type | String | Convert type `1`: Convert currency to contract`2`: Convert contract to currency |
| instId | String | Instrument ID |
| px | String | Order price |
| sz | String | Quantity to buy or sellIt is quantity of contract while converting currency to contractIt is quantity of currency while contract to currency. |
| unit | String | The unit of currency`coin``usds`: USDT/USDC |

### Get instrument tick bands

Get instrument tick bands information

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/instrument-tick-bands`

Request Example

```
GET /api/v5/public/instrument-tick-bands?instType=OPTION
```

```
GET /api/v5/public/instrument-tick-bands?instType=EVENTS
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`OPTION``EVENTS` |
| instFamily | String | No | Instrument familyOnly applicable to `OPTION` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instType": "OPTION",
 "instFamily": "BTC-USD",
 "tickBand": [
 {
 "minPx": "0",
 "maxPx": "100",
 "tickSz": "0.1"
 },
 {
 "minPx": "100",
 "maxPx": "10000",
 "tickSz": "1"
 }
 ]
 },
 {
 "instType": "OPTION",
 "instFamily": "ETH-USD",
 "tickBand": [
 {
 "minPx": "0",
 "maxPx": "100",
 "tickSz": "0.1"
 },
 {
 "minPx": "100",
 "maxPx": "10000",
 "tickSz": "1"
 }
 ]
 }
 ]
}

```

Response Example: EVENTS

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instType": "EVENTS",
 "instFamily": "",
 "tickBand": [
 {
 "minPx": "0.001",
 "maxPx": "0.04",
 "tickSz": "0.001"
 },
 {
 "minPx": "0.04",
 "maxPx": "0.96",
 "tickSz": "0.01"
 },
 {
 "minPx": "0.96",
 "maxPx": "0.999",
 "tickSz": "0.001"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instFamily | String | Instrument family. Only applicable to `OPTION` |
| tickBand | Array of objects | Tick size band. For `EVENTS`, returns unified tick bands applicable to all event contracts. |
| > minPx | String | Minimum price while placing an order |
| > maxPx | String | Maximum price while placing an order |
| > tickSz | String | Tick size, e.g. `0.0001` |

### Get premium history

It will return premium data in the past 6 months.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/premium-history`

Request Example

```
GET /api/v5/public/premium-history?instId=BTC-USDT-SWAP
```

```

```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP`Applicable to `SWAP` |
| after | String | No | Pagination of data to return records earlier than the requested ts(not included) |
| before | String | No | Pagination of data to return records newer than the requested ts(not included) |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "instId": "BTC-USDT-SWAP",
 "premium": "0.0000578896878167",
 "ts": "1713925924000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| premium | String | Premium index formula: [Max (0, Impact bid price – Index price) – Max (0, Index price – Impact ask price)] / Index price |
| ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get index tickers

Retrieve index tickers.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-tickers`

Request Example

```
GET /api/v5/market/index-tickers?instId=BTC-USDT
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve index tickers
result = marketDataAPI.get_index_tickers(
 instId="BTC-USDT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| quoteCcy | String | Conditional | Quote currency Currently there is only an index with `USD/USDT/BTC/USDC` as the quote currency. |
| instId | String | Conditional | Index, e.g. `BTC-USD`Either `quoteCcy` or `instId` is required. Same as `uly`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "BTC-USDT",
 "idxPx": "43350",
 "high24h": "43649.7",
 "sodUtc0": "43444.1",
 "open24h": "43640.8",
 "low24h": "43261.9",
 "sodUtc8": "43328.7",
 "ts": "1649419644492"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Index |
| idxPx | String | Latest index price |
| high24h | String | Highest price in the past 24 hours |
| low24h | String | Lowest price in the past 24 hours |
| open24h | String | Open price in the past 24 hours |
| sodUtc0 | String | Open price in the UTC 0 |
| sodUtc8 | String | Open price in the UTC 8 |
| ts | String | Index price update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get index candlesticks

Retrieve the candlestick charts of the index. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-candles`

Request Example

```
GET /api/v5/market/index-candles?instId=BTC-USD
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the candlestick charts of the index
result = marketDataAPI.get_index_candlesticks(
 instId="BTC-USD"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Index, e.g. `BTC-USD`Same as `uly`. |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually |
| bar | String | No | Bar size, the default is `1m`e.g. [`1m`/`3m`/`5m`/`15m`/`30m`/`1H`/`2H`/`4H`] UTC+8 opening price k-line: [`6H`/`12H`/`1D`/`1W`/`1M`/`3M`]UTC+0 opening price k-line: [`6Hutc`/`12Hutc`/`1Dutc`/`1Wutc`/`1Mutc`/`3Mutc`] |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1597026383085",
 "3.721",
 "3.743",
 "3.677",
 "3.708",
 "0"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| o | String | Open price |
| h | String | highest price |
| l | String | Lowest price |
| c | String | Close price |
| confirm | String | The state of candlesticks.`0` represents that it is uncompleted, `1` represents that it is completed. |

 The candlestick data may be incomplete, and should not be polled repeatedly.

The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm].

### Get index candlesticks history

Retrieve the candlestick charts of the index from recent years.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-index-candles`

Request Example

```
GET /api/v5/market/history-index-candles?instId=BTC-USD
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Index, e.g. `BTC-USD`Same as `uly`. |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually |
| bar | String | No | Bar size, the default is `1m`e.g. [1m/3m/5m/15m/30m/1H/2H/4H] UTC+8 opening price k-line: [6H/12H/1D/1W/1M]UTC+0 opening price k-line: [/6Hutc/12Hutc/1Dutc/1Wutc/1Mutc] |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1597026383085",
 "3.721",
 "3.743",
 "3.677",
 "3.708",
 "1"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| o | String | Open price |
| h | String | highest price |
| l | String | Lowest price |
| c | String | Close price |
| confirm | String | The state of candlesticks.`0` represents that it is uncompleted, `1` represents that it is completed. |

The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm].

### Get mark price candlesticks

Retrieve the candlestick charts of mark price. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/mark-price-candles`

Request Example

```
GET /api/v5/market/mark-price-candles?instId=BTC-USD-SWAP
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the candlestick charts of mark price
result = marketDataAPI.get_mark_price_candlesticks(
 instId="BTC-USD-SWAP"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually |
| bar | String | No | Bar size, the default is `1m`e.g. [1m/3m/5m/15m/30m/1H/2H/4H] UTC+8 opening price k-line: [6H/12H/1D/1W/1M/3M]UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/1Wutc/1Mutc/3Mutc] |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1597026383085",
 "3.721",
 "3.743",
 "3.677",
 "3.708",
 "0"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| o | String | Open price |
| h | String | highest price |
| l | String | Lowest price |
| c | String | Close price |
| confirm | String | The state of candlesticks.`0` represents that it is uncompleted, `1` represents that it is completed. |

 The candlestick data may be incomplete, and should not be polled repeatedly.

The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm]

### Get mark price candlesticks history

Retrieve the candlestick charts of mark price from recent years.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-mark-price-candles`

Request Example

```
GET /api/v5/market/history-mark-price-candles?instId=BTC-USD-SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually |
| bar | String | No | Bar size, the default is `1m`e.g. [1m/3m/5m/15m/30m/1H/2H/4H] UTC+8 opening price k-line: [6H/12H/1D/1W/1M]UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/1Wutc/1Mutc] |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1597026383085",
 "3.721",
 "3.743",
 "3.677",
 "3.708",
 "1"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| o | String | Open price |
| h | String | highest price |
| l | String | Lowest price |
| c | String | Close price |
| confirm | String | The state of candlesticks.`0` represents that it is uncompleted, `1` represents that it is completed. |

The data returned will be arranged in an array like this: [ts,o,h,l,c,confirm]

### Get exchange rate

This interface provides the average exchange rate data for 2 weeks

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/exchange-rate`

Request Example

```
GET /api/v5/market/exchange-rate
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve average exchange rate data for 2 weeks
result = marketDataAPI.get_exchange_rate()
print(result)
```

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "usdCny": "7.162"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| usdCny | String | Exchange rate |

### Get index components

Get the index component information data on the market

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/index-components`

Request Example

```
GET /api/v5/market/index-components?index=BTC-USD
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Get the index component information data on the market
result = marketDataAPI.get_index_components(
 index="BTC-USD"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| index | String | Yes | index, e.g `BTC-USDT`Same as `uly`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": {
 "components": [
 {
 "symbol": "BTC/USDT",
 "symPx": "52733.2",
 "wgt": "0.25",
 "cnvPx": "52733.2",
 "exch": "OKX"
 },
 {
 "symbol": "BTC/USDT",
 "symPx": "52739.87000000",
 "wgt": "0.25",
 "cnvPx": "52739.87000000",
 "exch": "Binance"
 },
 {
 "symbol": "BTC/USDT",
 "symPx": "52729.1",
 "wgt": "0.25",
 "cnvPx": "52729.1",
 "exch": "Huobi"
 },
 {
 "symbol": "BTC/USDT",
 "symPx": "52739.47929397",
 "wgt": "0.25",
 "cnvPx": "52739.47929397",
 "exch": "Poloniex"
 }
 ],
 "last": "52735.4123234925",
 "index": "BTC-USDT",
 "ts": "1630985335599"
 }
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| index | String | Index |
| last | String | Latest Index Price |
| ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| components | Array of objects | Components |
| > exch | String | Name of Exchange |
| > symbol | String | Name of Exchange Trading Pairs |
| > symPx | String | Price of Exchange Trading Pairs |
| > wgt | String | Weights |
| > cnvPx | String | Price converted to index |

### Get economic calendar data

Authentication is required for this endpoint. This endpoint is only supported in production environment.

Get the macro-economic calendar data within 3 months. Historical data from 3 months ago is only available to users with trading fee tier VIP1 and above.

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/economic-calendar`

Request Example

```
GET /api/v5/public/economic-calendar
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| region | string | No | Country, region or entity `afghanistan`, `albania`, `algeria`, `andorra`, `angola`, `antigua_and_barbuda`, `argentina`, `armenia`, `aruba`, `australia`, `austria`, `azerbaijan`, `bahamas`, `bahrain`, `bangladesh`, `barbados`, `belarus`, `belgium`, `belize`, `benin`, `bermuda`, `bhutan`, `bolivia`, `bosnia_and_herzegovina`, `botswana`, `brazil`, `brunei`, `bulgaria`, `burkina_faso`, `burundi`, `cambodia`, `cameroon`, `canada`, `cape_verde`, `cayman_islands`, `central_african_republic`, `chad`, `chile`, `china`, `colombia`, `comoros`, `congo`, `costa_rica`, `croatia`, `cuba`, `cyprus`, `czech_republic`, `denmark`, `djibouti`, `dominica`, `dominican_republic`, `east_timor`, `ecuador`, `egypt`, `el_salvador`, `equatorial_guinea`, `eritrea`, `estonia`, `ethiopia`, `euro_area`, `european_union`, `faroe_islands`, `fiji`, `finland`, `france`, `g20`, `g7`, `gabon`, `gambia`, `georgia`, `germany`, `ghana`, `greece`, `greenland`, `grenada`, `guatemala`, `guinea`, `guinea_bissau`, `guyana`, `hungary`, `haiti`, `honduras`, `hong_kong`, `hungary`, `imf`, `indonesia`, `iceland`, `india`, `indonesia`, `iran`, `iraq`, `ireland`, `isle_of_man`, `israel`, `italy`, `ivory_coast`, `jamaica`, `japan`, `jordan`, `kazakhstan`, `kenya`, `kiribati`, `kosovo`, `kuwait`, `kyrgyzstan`, `laos`, `latvia`, `lebanon`, `lesotho`, `liberia`, `libya`, `liechtenstein`, `lithuania`, `luxembourg`, `macau`, `macedonia`, `madagascar`, `malawi`, `malaysia`, `maldives`, `mali`, `malta`, `mauritania`, `mauritius`, `mexico`, `micronesia`, `moldova`, `monaco`, `mongolia`, `montenegro`, `morocco`, `mozambique`, `myanmar`, `namibia`, `nepal`, `netherlands`, `new_caledonia`, `new_zealand`, `nicaragua`, `niger`, `nigeria`, `north_korea`, `northern_mariana_islands`, `norway`, `opec`, `oman`, `pakistan`, `palau`, `palestine`, `panama`, `papua_new_guinea`, `paraguay`, `peru`, `philippines`, `poland`, `portugal`, `puerto_rico`, `qatar`, `russia`, `republic_of_the_congo`, `romania`, `russia`, `rwanda`, `slovakia`, `samoa`, `san_marino`, `sao_tome_and_principe`, `saudi_arabia`, `senegal`, `serbia`, `seychelles`, `sierra_leone`, `singapore`, `slovakia`, `slovenia`, `solomon_islands`, `somalia`, `south_africa`, `south_korea`, `south_sudan`, `spain`, `sri_lanka`, `st_kitts_and_nevis`, `st_lucia`, `sudan`, `suriname`, `swaziland`, `sweden`, `switzerland`, `syria`, `taiwan`, `tajikistan`, `tanzania`, `thailand`, `togo`, `tonga`, `trinidad_and_tobago`, `tunisia`, `turkey`, `turkmenistan`, `uganda`, `ukraine`, `united_arab_emirates`, `united_kingdom`, `united_states`, `uruguay`, `uzbekistan`, `vanuatu`, `venezuela`, `vietnam`, `world`, `yemen`, `zambia`, `zimbabwe` |
| importance | string | No | Level of importance `1`: low `2`: medium `3`: high |
| before | String | No | Pagination of data to return records newer than the requested ts based on the date parameter. Unix timestamp format in milliseconds. |
| after | String | No | Pagination of data to return records earlier than the requested ts based on the date parameter. Unix timestamp format in milliseconds. The default is the timestamp of the request moment. |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "actual": "7.8%",
 "calendarId": "330631",
 "category": "Harmonised Inflation Rate YoY",
 "ccy": "",
 "date": "1700121600000",
 "dateSpan": "0",
 "event": "Harmonised Inflation Rate YoY",
 "forecast": "7.8%",
 "importance": "1",
 "prevInitial": "",
 "previous": "9%",
 "refDate": "1698710400000",
 "region": "Slovakia",
 "uTime": "1700121605007",
 "unit": "%"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| calendarId | string | Calendar ID |
| date | string | Estimated release time of the value of actual field, millisecond format of Unix timestamp, e.g. `1597026383085` |
| region | string | Country, region or entity |
| category | string | Category name |
| event | string | Event name |
| refDate | string | Date for which the datapoint refers to |
| actual | string | The actual value of this event |
| previous | string | Latest actual value of the previous period The value will be revised if revision is applicable |
| forecast | string | Average forecast among a representative group of economists |
| dateSpan | string | `0`: The time of the event is known`1`: we only know the date of the event, the exact time of the event is unknown. |
| importance | string | Level of importance `1`: low `2`: medium `3`: high |
| uTime | string | Update time of this record, millisecond format of Unix timestamp, e.g. `1597026383085` |
| prevInitial | string | The initial value of the previous period Only applicable when revision happens |
| ccy | string | Currency of the data |
| unit | string | Unit of the data |

### Get historical market data

Data availability****Historical data backfill is currently in progress. Data availability may vary by module, instrument, and time period. The dataset will be continuously expanded to provide more comprehensive historical coverage.

Legacy data format notice****For module 1 (trade history), some old historical files may contain column headers with both Chinese characters along with English column names. All the Chinese characters will be removed once the data backfill is done. Please account for this when parsing the data.

Data release schedule****Most data for modules 1, 2, 3, 11 is typically available on T+2; order book data is typically available on T+3.

Retrieve historical market data for OKX.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/market-data-history`

Request Example

```
GET /api/v5/public/market-data-history?module=1&instType=SWAP&instFamilyList=BTC-USDT&dateAggrType=daily&begin=1756604295000&end=1756777095000
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| module | String | Yes | Data module type`1`: Tick-by-tick trade history`2`: 1-minute candlestick`3`: Funding rate`4`: 400-level orderbook`5`: 5000-level orderbook (from Nov 1, 2025)`6`: 50-level orderbook (will gradually be deprecated, please use module = `4`,`5` instead)`11`: Borrowing rate |
| instType | String | Yes | Instrument type`SPOT``FUTURES``SWAP``OPTION` |
| instIdList | String | Conditional | List of instrument IDs, e.g. `BTC-USDT`, or `ANY` for all instruments (`ANY` is only supported for module = `1`, `2`, `3`, `11` & dateAggrType = `daily`)Multiple instrument IDs should be separated by commas, e.g. `BTC-USDT,ETH-USDT`Maximum length = 10Only applicable when instType = `SPOT` |
| instFamilyList | String | Conditional | List of instrument families, e.g. `BTC-USDT`, or `ANY` for all instruments (`ANY` is only supported for module = `1`, `2`, `3`, `11` & dateAggrType = `daily`)Multiple instrument families should be separated by commas, e.g. `BTC-USDT,ETH-USDT`Maximum length = 10 (= 1when module = `6` & instType = `OPTION`)Only applicable when instType ≠ `SPOT` |
| dateAggrType | String | Yes | Date aggregation type `daily` (not supported for module = `3` & instFamilyList ≠ `ANY`) `monthly` (not supported for module = `6`) |
| begin | String | Yes | Begin timestamp. Unix timestamp format in milliseconds (inclusive)Maximum range: 20 days for daily, 20 months for monthly |
| end | String | Yes | End timestamp. Unix timestamp format in milliseconds (inclusive)When module = `6` & instType = `OPTION`, only returns data for the day specified by `end` |

Response Example

```
{
 "code": "0",
 "data": [{
 "dateAggrType": "daily",
 "details": [{
 "dateRangeEnd": "1756656000000",
 "dateRangeStart": "1756569600000",
 "groupDetails": [{
 "dateTs": "1756656000000",
 "filename": "BTC-USDT-SWAP-trades-2025-09-01.zip",
 "sizeMB": "10.82",
 "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250901/BTC-USDT-SWAP-trades-2025-09-01.zip"
 },
 {
 "dateTs": "1756569600000",
 "filename": "BTC-USDT-SWAP-trades-2025-08-31.zip",
 "sizeMB": "4.82",
 "url": "https://static.okx.com/cdn/okex/traderecords/trades/daily/20250831/BTC-USDT-SWAP-trades-2025-08-31.zip"
 }],
 "groupSizeMB": "15.64",
 "instFamily": "BTC-USDT",
 "instId": "",
 "instType": "SWAP"
 }],
 "totalSizeMB": "15.64",
 "ts": "1756882260390"
 }],
 "msg": ""
}

```

Response Example when no data files are available

```
{
 "code": "0",
 "data": [
 {
 "dateAggrType": "monthly",
 "details": [],
 "totalSizeMB": "0",
 "ts": "1756889595507"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Response timestamp, Unix timestamp format in milliseconds |
| totalSizeMB | String | Total size of all data files in MB |
| dateAggrType | String | Date aggregation type `daily` `monthly` |
| details | Array | |
| > instId | String | Instrument ID |
| > instFamily | String | Instrument family |
| > dateRangeStart | String | Data range start date, Unix timestamp format in milliseconds (inclusive) |
| > dateRangeEnd | String | Data range end date, Unix timestamp format in milliseconds (inclusive) |
| > groupSizeMB | String | Data group size in MB |
| > groupDetails | Array | |
| >> filename | String | Data file name, e.g. `BTC-USDT-SWAP-trades-2025-05-15.zip` |
| >> dataTs | String | Data date timestamp, Unix timestamp format in milliseconds |
| >> sizeMB | String | File size in MB |
| >> url | String | Download URL |

Data query rules****• Only the date portion (yyyy-mm-dd) of timestamps is used; time components are ignored
• Both begin and end timestamps are inclusive
• Data is returned in reverse chronological order (closer to end first)
• If the query exceeds record limits, data closest to the end timestamp is returned
• Exception:** When module = 6 & instType = OPTION, only data for the day specified by the end is returned

**Timezone specifications for timestamp parsing****When converting Unix timestamps to dates, the following timezone conventions are applied to all timestamp fields (begin, end, dateRangeStart, dateRangeEnd, dataTs):
• Orderbook data** (modules 4, 5, 6): UTC+0**• All other data modules** (modules 1, 2, 3, 11): UTC+8
