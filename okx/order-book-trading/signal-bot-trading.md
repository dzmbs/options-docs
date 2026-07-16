## Signal bot trading

Create and customize your own signals while gaining access to a diverse selection of signals from top providers. Empower your trading strategies and stay ahead of the game with our comprehensive signal trading platform. [Learn more](/learn/signal-trading)

### POST / Create signal

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/create-signal`

Request Example

```
POST /api/v5/tradingBot/signal/create-signal
body
{
 "signalChanName": "long short",
 "signalDesc": "this is the first version"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| signalChanName | String | Yes | Signal channel name |
| signalChanDesc | String | No | Signal channel description |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "signalChanId" :"572112109",
 "signalChanToken":"dojuckew331lkx"
 }

 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| signalChanId | String | Signal channel Id |
| signalChanToken | String | User identify when placing orders via signal |

### GET / Signals

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/signals`

Request Example

```
GET /api/v5/tradingBot/signal/signals?signalSourceType=1
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| signalSourceType | String | Yes | Signal source type`1`: Created by yourself`2`: Subscribe`3`: Free signal |
| signalChanId | String | No | Signal channel id |
| after | String | No | Pagination of data to return records `signalChanId` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records `signalChanId` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "signalChanId": "623833708424069120",
 "signalChanName": "test",
 "signalChanDesc": "test",
 "signalChanToken": "test",
 "signalSourceType": "1"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| signalChanId | String | Signal channel id |
| signalChanName | String | Signal channel name |
| signalChanDesc | String | Signal channel description |
| signalChanToken | String | User identify when placing orders via signal |
| signalSourceType | String | Signal source type`1`: Created by yourself`2`: Subscribe`3`: Free signal |

### POST / Create signal bot

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/order-algo`

Request Example

```
# Create signal bot
POST /api/v5/tradingBot/signal/order-algo
body
{
 "signalChanId": "627921182788161536",
 "instIds": [
 "BTC-USDT-SWAP",
 "ETH-USDT-SWAP",
 "LTC-USDT-SWAP"
 ],
 "lever": "10",
 "investAmt": "100",
 "subOrdType": "9",
 "entrySettingParam": {
 "allowMultipleEntry": true,
 "entryType": "1",
 "amt": "",
 "ratio": ""
 },
 "exitSettingParam": {
 "tpSlType": "2",
 "tpPct": "",
 "slPct": ""
 }
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| signalChanId | String | Yes | Signal channel Id |
| lever | String | Yes | LeverageOnly applicable to `contract signal` |
| investAmt | String | Yes | Investment amount |
| subOrdType | String | Yes | Sub order type `1`：limit order `2`：market order `9`：tradingView signal |
| includeAll | Boolean | No | Whether to include all USDT-margined contract.The default value is `false`. `true`: include `false` : exclude |
| instIds | String | No | Instrument IDs. Single currency or multiple currencies separated with comma. When `includeAll` is `true`, it is ignored |
| ratio | String | No | Price offset ratio, calculate the limit price as a percentage offset from the best bid/ask price.Only applicable to `subOrdType` is `limit` order |
| entrySettingParam | String | No | Entry setting |
| > allowMultipleEntry | String | No | Whether or not allow multiple entries in the same direction for the same trading pairs.The default value is `true`。 `true`：Allow `false`：Prohibit |
| > entryType | String | No | Entry type`1`: TradingView signal`2`: Fixed margin`3`: Contracts`4`: Percentage of free margin`5`: Percentage of the initial invested margin |
| > amt | String | No | Amount per order Only applicable to entryType in `2`/`3` |
| > ratio | Array of objects | No | Amount ratio per orderOnly applicable to entryType in `4`/`5` |
| exitSettingParam | String | No | Exit setting |
| > tpSlType | String | 是 | Type of set the take-profit and stop-loss trigger price `pnl`: Based on the estimated profit and loss percentage from the entry point `price`: Based on price increase or decrease from the crypto’s entry price |
| > tpPct | String | No | Take-profit percentage |
| > slPct | String | No | Stop-loss percentage |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "447053782921515008",
 "sCode": "0",
 "sMsg": ""
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
| sCode | String | The code of the event execution result, 0 means success. |
| sMsg | String | The code of the event execution result, 0 means success. |

### POST / Cancel signal bots

A maximum of 10 orders can be stopped per request.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/stop-order-algo`

Request Example

```
POST /api/v5/tradingBot/signal/stop-order-algo
body
[
 {
 "algoId":"448965992920907776"
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
 "algoId": "448965992920907776",
 "sCode": "0",
 "sMsg": "",
 "algoClOrdId": ""
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| sCode | String | The code of the event execution result, `0` means success. |
| sMsg | String | Rejection or success message of event execution. |
| algoClOrdId | String | Client-supplied Algo ID |

### POST / Adjust margin balance

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/margin-balance`

Request Example

```
POST /api/v5/tradingBot/signal/margin-balance
body
{
 "algoId":"123456",
 "type":"add",
 "amt":"10"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| type | String | Yes | Adjust margin balance type`add` `reduce` |
| amt | String | Yes | Adjust margin balance amountEither `amt` or `percent` is required. |
| allowReinvest | Boolean | No | Whether to reinvest with newly added margin. The default value is `false`. `false`:it will be used as passive margin to prevent liquidation and will not be used as active investment`true`:the margin added here will furthermore be accounted for in calculations of your total investment amount, and furthermore your order size。Only applicable to your signal comes in with an “investmentType” of “percentage_investment” |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "123456"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |

### POST / Amend TPSL

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/amendTPSL`

Request Example

```
POST /api/v5/tradingBot/signal/amendTPSL
body
{
 "algoId": "637039348240277504",
 "exitSettingParam": {
 "tpSlType": "pnl",
 "tpPct": "0.01",
 "slPct": "0.01"
 }
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| exitSettingParam | String | Yes | Exit setting |
| > tpSlType | String | Yes | Type of set the take-profit and stop-loss trigger price`pnl`: Based on the estimated profit and loss percentage from the entry point`price`: Based on price increase or decrease from the crypto’s entry price |
| > tpPct | String | No | Take-profit percentage |
| > slPct | String | No | Stop-loss percentage |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "637039348240277504"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |

### POST / Set instruments

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/set-instruments`

Request Example

```
POST /api/v5/tradingBot/signal/set-instruments
body
{
 "algoId": "637039348240277504",
 "instIds": [
 "SHIB-USDT-SWAP",
 "ETH-USDT-SWAP"
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| instIds | Array of strings | Yes | Instrument IDs. When `includeAll` is `true`, it is ignored |
| includeAll | Boolean | Yes | Whether to include all USDT-margined contract.The default value is `false`. `true`: include `false` : exclude |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "637039348240277504"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |

### GET / Signal bot order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/orders-algo-details`

Request Example

```
GET /api/v5/tradingBot/signal/orders-algo-details?algoId=623833708424069120&algoOrdType=contract
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`contract`: Contract signal |
| algoId | String | Yes | Algo ID |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "623833708424069120",
 "algoClOrdId": "",
 "algoOrdType": "contract",
 "availBal": "1.6561369013122267",
 "cTime": "1695005546360",
 "cancelType": "0",
 "entrySettingParam": {
 "allowMultipleEntry": true,
 "amt": "0",
 "entryType": "1",
 "ratio": ""
 },
 "exitSettingParam": {
 "slPct": "",
 "tpPct": "",
 "tpSlType": "price"
 },
 "floatPnl": "0.1279999999999927",
 "frozenBal": "25.16816",
 "instIds": [
 "BTC-USDT-SWAP",
 "ETH-USDT-SWAP"
 ],
 "instType": "SWAP",
 "investAmt": "100",
 "lever": "10",
 "ratio": "",
 "realizedPnl": "-73.303703098687766",
 "signalChanId": "623827579484770304",
 "signalChanName": "testing",
 "signalSourceType": "1",
 "state": "running",
 "subOrdType": "9",
 "totalEq": "26.824296901312227",
 "totalPnl": "-73.1757030986877733",
 "totalPnlRatio": "-0.7317570309868777",
 "uTime": "1697029422313"
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
| instIds | Array of strings | Instrument IDs |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`contract`: Contract signal |
| state | String | Algo order state`starting``running``stopping``stopped` |
| cancelType | String | Algo order stop reason`0`: None`1`: Manual stop |
| totalPnl | String | Total P&L |
| totalPnlRatio | String | Total P&L ratio |
| totalEq | String | Total equity of strategy account |
| floatPnl | String | Float P&L |
| realizedPnl | String | Realized P&L |
| frozenBal | String | Frozen balance |
| availBal | String | Avail balance |
| lever | String | LeverageOnly applicable to `contract signal` |
| investAmt | String | Investment amount |
| subOrdType | String | Sub order type`1`：limit order`2`：market order`9`：tradingView signal |
| ratio | String | Price offset ratio, calculate the limit price as a percentage offset from the best bid/ask priceOnly applicable to `subOrdType` is `limit order` |
| entrySettingParam | Object | Entry setting |
| > allowMultipleEntry | Boolean | Whether or not allow multiple entries in the same direction for the same trading pairs |
| > entryType | String | Entry type`1`: TradingView signal`2`: Fixed margin`3`: Contracts`4`: Percentage of free margin`5`: Percentage of the initial invested margin |
| > amt | String | Amount per orderOnly applicable to `entryType` in `2`/`3` |
| > ratio | String | Amount ratio per orderOnly applicable to `entryType` in `4`/`5` |
| exitSettingParam | Object | Exit setting |
| > tpSlType | String | Type of set the take-profit and stop-loss trigger price`pnl`: Based on the estimated profit and loss percentage from the entry point`price`: Based on price increase or decrease from the crypto’s entry price |
| > tpPct | String | Take-profit percentage |
| > slPct | String | Stop-loss percentage |
| signalChanId | String | Signal channel Id |
| signalChanName | String | Signal channel name |
| signalSourceType | String | Signal source type`1`: Created by yourself`2`: Subscribe`3`: Free signal |

### GET / Active signal bot

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/orders-algo-pending`

Request Example

```
GET /api/v5/tradingBot/signal/orders-algo-pending?algoOrdType=contract
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`contract`: Contract signal |
| algoId | String | No | Algo ID |
| after | String | Yes | Pagination of data to return records `algoId` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records `algoId` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "623833708424069120",
 "algoClOrdId": "",
 "algoOrdType": "contract",
 "availBal": "1.6561369013122267",
 "cTime": "1695005546360",
 "cancelType": "0",
 "entrySettingParam": {
 "allowMultipleEntry": true,
 "amt": "0",
 "entryType": "1",
 "ratio": ""
 },
 "exitSettingParam": {
 "slPct": "",
 "tpPct": "",
 "tpSlType": "price"
 },
 "floatPnl": "0.1279999999999927",
 "frozenBal": "25.16816",
 "instIds": [
 "BTC-USDT-SWAP",
 "ETH-USDT-SWAP"
 ],
 "instType": "SWAP",
 "investAmt": "100",
 "lever": "10",
 "ratio": "",
 "realizedPnl": "-73.303703098687766",
 "signalChanId": "623827579484770304",
 "signalChanName": "my signal",
 "signalSourceType": "1",
 "state": "running",
 "subOrdType": "9",
 "totalEq": "26.824296901312227",
 "totalPnl": "-73.1757030986877733",
 "totalPnlRatio": "-0.7317570309868777",
 "uTime": "1697029422313"
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
| instIds | Array of strings | Instrument IDs |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`contract`: Contract signal |
| state | String | Algo order state`starting``running``stopping` |
| cancelType | String | Algo order stop reason`0`: None |
| totalPnl | String | Total P&L |
| totalPnlRatio | String | Total P&L ratio |
| totalEq | String | Total equity of strategy account |
| floatPnl | String | Float P&L |
| realizedPnl | String | Realized P&L |
| frozenBal | String | Frozen balance |
| availBal | String | Avail balance |
| lever | String | LeverageOnly applicable to `contract signal` |
| investAmt | String | Investment amount |
| subOrdType | String | Sub order type`1`：limit order`2`：market order`9`：tradingView signal |
| ratio | String | Price offset ratio, calculate the limit price as a percentage offset from the best bid/ask priceOnly applicable to `subOrdType` is `limit order` |
| entrySettingParam | Object | Entry setting |
| > allowMultipleEntry | Boolean | Whether or not allow multiple entries in the same direction for the same trading pairs |
| > entryType | String | Entry type`1`: TradingView signal`2`: Fixed margin`3`: Contracts`4`: Percentage of free margin`5`: Percentage of the initial invested margin |
| > amt | String | Amount per orderOnly applicable to `entryType` in `2`/`3` |
| > ratio | String | Amount ratio per orderOnly applicable to `entryType` in `4`/`5` |
| exitSettingParam | Object | Exit setting |
| > tpSlType | String | Type of set the take-profit and stop-loss trigger price`pnl`: Based on the estimated profit and loss percentage from the entry point`price`: Based on price increase or decrease from the crypto’s entry price |
| > tpPct | String | Take-profit percentage |
| > slPct | String | Stop-loss percentage |
| signalChanId | String | Signal channel Id |
| signalChanName | String | Signal channel name |
| signalSourceType | String | Signal source type`1`: Created by yourself`2`: Subscribe`3`: Free signal |

### GET / Signal bot history

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/orders-algo-history`

Request Example

```
GET /api/v5/tradingBot/signal/orders-algo-history?algoId=623833708424069120&algoOrdType=contract
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`contract`: Contract signal |
| algoId | String | Yes | Algo ID |
| after | String | Yes | Pagination of data to return records `algoId` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records `algoId` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "623833708424069120",
 "algoClOrdId": "",
 "algoOrdType": "contract",
 "availBal": "1.6561369013122267",
 "cTime": "1695005546360",
 "cancelType": "1",
 "entrySettingParam": {
 "allowMultipleEntry": true,
 "amt": "0",
 "entryType": "1",
 "ratio": ""
 },
 "exitSettingParam": {
 "slPct": "",
 "tpPct": "",
 "tpSlType": "price"
 },
 "floatPnl": "0.1279999999999927",
 "frozenBal": "25.16816",
 "instIds": [
 "BTC-USDT-SWAP",
 "ETH-USDT-SWAP"
 ],
 "instType": "SWAP",
 "investAmt": "100",
 "lever": "10",
 "ratio": "",
 "realizedPnl": "-73.303703098687766",
 "signalChanId": "623827579484770304",
 "signalChanName": "my signal",
 "signalSourceType": "1",
 "state": "stopped",
 "subOrdType": "9",
 "totalEq": "26.824296901312227",
 "totalPnl": "-73.1757030986877733",
 "totalPnlRatio": "-0.7317570309868777",
 "uTime": "1697029422313"
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
| instIds | Array of strings | Instrument IDs |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`contract`: Contract signal |
| state | String | Algo order state`stopped` |
| cancelType | String | Algo order stop reason`1`: Manual stop |
| totalPnl | String | Total P&L |
| totalPnlRatio | String | Total P&L ratio |
| totalEq | String | Total equity of strategy account |
| floatPnl | String | Float P&L |
| realizedPnl | String | Realized P&L |
| frozenBal | String | Frozen balance |
| availBal | String | Avail balance |
| lever | String | LeverageOnly applicable to `contract signal` |
| investAmt | String | Investment amount |
| subOrdType | String | Sub order type`1`：limit order`2`：market order`9`：tradingView signal |
| ratio | String | Price offset ratio, calculate the limit price as a percentage offset from the best bid/ask priceOnly applicable to `subOrdType` is `limit order` |
| entrySettingParam | Object | Entry setting |
| > allowMultipleEntry | Boolean | Whether or not allow multiple entries in the same direction for the same trading pairs |
| > entryType | String | Entry type`1`: TradingView signal`2`: Fixed margin`3`: Contracts`4`: Percentage of free margin`5`: Percentage of the initial invested margin |
| > amt | String | Amount per orderOnly applicable to `entryType` in `2`/`3` |
| > ratio | String | Amount ratio per orderOnly applicable to `entryType` in `4`/`5` |
| exitSettingParam | Object | Exit setting |
| > tpSlType | String | Type of set the take-profit and stop-loss trigger price`pnl`: Based on the estimated profit and loss percentage from the entry point`price`: Based on price increase or decrease from the crypto’s entry price |
| > tpPct | String | Take-profit percentage |
| > slPct | String | Stop-loss percentage |
| signalChanId | String | Signal channel Id |
| signalChanName | String | Signal channel name |
| signalSourceType | String | Signal source type`1`: Created by yourself`2`: Subscribe`3`: Free signal |

### GET / Signal bot order positions

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/positions`

Request Example

```
GET /api/v5/tradingBot/signal/positions?algoId=623833708424069120&algoOrdType=contract
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`contract`: Contract signal |
| algoId | String | Yes | Algo ID |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "adl": "1",
 "algoClOrdId": "",
 "algoId": "623833708424069120",
 "avgPx": "1597.74",
 "cTime": "1697502301460",
 "ccy": "USDT",
 "imr": "23.76495",
 "instId": "ETH-USDT-SWAP",
 "instType": "SWAP",
 "last": "1584.34",
 "lever": "10",
 "liqPx": "1438.7380360728976",
 "markPx": "1584.33",
 "mgnMode": "cross",
 "mgnRatio": "11.719278420807477",
 "mmr": "1.9011959999999997",
 "notionalUsd": "237.75168928499997",
 "pos": "15",
 "posSide": "net",
 "uTime": "1697502301460",
 "upl": "-2.0115000000000123",
 "uplRatio": "-0.0839310526118142"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID. Used to be extended in the future. |
| instType | String | Instrument type |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| avgPx | String | Average open price |
| ccy | String | Margin currency |
| lever | String | Leverage |
| liqPx | String | Estimated liquidation price |
| posSide | String | Position side`net` |
| pos | String | Quantity of positions |
| mgnMode | String | Margin mode`cross``isolated` |
| mgnRatio | String | Maintenance margin ratio |
| imr | String | Initial margin requirement |
| mmr | String | Maintenance margin requirement |
| upl | String | Unrealized profit and loss |
| uplRatio | String | Unrealized profit and loss ratio |
| last | String | Latest traded price |
| notionalUsd | String | Notional value of positions in `USD` |
| adl | String | Automatic-Deleveraging, signal areaDivided into 5 levels, from 1 to 5, the smaller the number, the weaker the adl intensity. |
| markPx | String | Mark price |

### GET / Position history

Retrieve the updated position data for the last 3 months. Return in reverse chronological order using utime.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/positions-history`

Request Example

```
GET /api/v5/tradingBot/signal/positions-history?algoId=1234
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| instId | String | No | Instrument ID, e.g.：`BTC-USD-SWAP` |
| after | String | No | Pagination of data to return records earlier than the requested `uTime`, Unix timestamp format in milliseconds, e.g.`1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `uTime`, Unix timestamp format in milliseconds, e.g `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "cTime": "1704724451471",
 "closeAvgPx": "200",
 "direction": "net",
 "instId": "ETH-USDT-SWAP",
 "lever": "5.0",
 "mgnMode": "cross",
 "openAvgPx": "220",
 "pnl": "-2.021",
 "pnlRatio": "-0.4593181818181818",
 "uTime": "1704724456322",
 "uly": "ETH-USDT"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| mgnMode | String | Margin mode `cross` `isolated` |
| cTime | String | Created time of position |
| uTime | String | Updated time of position |
| openAvgPx | String | Average price of opening position |
| closeAvgPx | String | Average price of closing position |
| pnl | String | Profit and loss |
| pnlRatio | String | P&L ratio |
| lever | String | Leverage |
| direction | String | Direction: `long` `short` |
| uly | String | Underlying |

### POST / Close position

Close the position of an instrument via a market order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/close-position`

Request Example

```
POST /api/v5/tradingBot/signal/close-position
body
{
 "instId":"BTC-USDT-SWAP",
 "algoId":"448965992920907776"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| instId | String | Yes | Instrument ID |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "448965992920907776"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |

### POST / Place sub order

You can place an order only if you have sufficient funds.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/sub-order`

Request Example

```
POST /api/v5/tradingBot/signal/sub-order
body
{
 "algoId":"1222",
 "instId":"BTC-USDT-SWAP",
 "side":"buy",
 "ordType":"limit",
 "px":"2.15",
 "sz":"2"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP` |
| algoId | String | Yes | Algo ID |
| side | String | Yes | Order side, `buy` `sell` |
| ordType | String | Yes | Order type `market`: Market order `limit`: Limit order |
| sz | String | Yes | Quantity to buy or sell |
| px | String | Conditional | Order price. Only applicable to `limit` order. |
| reduceOnly | Boolean | No | Whether orders can only reduce in position size. Valid options: `true` or `false`. The default value is `false`. Only applicable to `Futures mode`/`Multi-currency margin` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |

ordType

Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:

`limit`: Limit order, which requires specified sz and px.

`market`: Market order. It will be filled with market price (by swiping opposite order book). Market order will be placed to order book with most aggressive price allowed by Price Limit Mechanism.

sz refers to the number of contracts。

reduceOnly

When placing an order with this parameter set to true, it means that the order will reduce the size of the position only
The sum of the current order size and all reverse direction reduce-only pending orders which's price-time priority is higher than the current order, cannot exceed the contract quantity of position.
Only applicable to `Futures mode` and `Multi-currency margin`

### POST / Cancel sub order

Cancel an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/signal/cancel-sub-order`

Request Example

```
POST /api/v5/tradingBot/signal/cancel-sub-order
body
{
 "algoId":"91664",
 "signalOrdId":"590908157585625111",
 "instId":"BTC-USDT-SWAP"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP |
| signalOrdId | String | Yes | Order ID |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "signalOrdId":"590908157585625111",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |
| > signalOrdId | String | Order ID |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection or success message of event execution. |

Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state by get sub orders endpoint.

### GET / Signal bot sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/sub-orders`

Request Example

```
# Get historical filled sub orders
GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&state=filled

# Get designated sub order
GET /api/v5/tradingBot/signal/sub-orders?algoId=623833708424069120&algoOrdType=contract&signalOrdId=O632302662327996418
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| algoOrdType | String | Yes | Algo order type`contract`: Contract signal |
| state | String | Conditional | Sub order state`live``partially_filled``filled``cancelled`Either `state` or `signalOrdId` is required, if both are passed in, only `state` is valid. |
| signalOrdId | String | Conditional | Sub order ID |
| after | String | No | Pagination of data to return records earlier than the requested `ordId` |
| before | String | No | Pagination of data to return records newer than the requested `ordId`. |
| begin | String | No | Return records of `ctime` after than the requested timestamp (include), Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | Return records of `ctime` before than the requested timestamp (include), Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |
| type | String | No | Sub order type `live``filled`Either `type` or `clOrdId` is required, if both are passed in, only `clOrdId` is valid. |
| clOrdId | String | No | Sub order client-supplied ID. `It will be deprecated soon` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "accFillSz": "18",
 "algoClOrdId": "",
 "algoId": "623833708424069120",
 "algoOrdType": "contract",
 "avgPx": "1572.81",
 "cTime": "1697024702320",
 "ccy": "",
 "clOrdId": "O632302662327996418",
 "ctVal": "0.01",
 "fee": "-0.1415529",
 "feeCcy": "USDT",
 "instId": "ETH-USDT-SWAP",
 "instType": "SWAP",
 "lever": "10",
 "ordId": "632302662351958016",
 "ordType": "market",
 "pnl": "-2.6784",
 "posSide": "net",
 "px": "",
 "side": "buy",
 "state": "filled",
 "sz": "18",
 "tag": "",
 "tdMode": "cross",
 "uTime": "1697024702322"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID. Used to be extended in the future |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| algoOrdType | String | Algo order type`contract`: Contract signal |
| ordId | String | Sub order ID |
| clOrdId | String | Sub order client-supplied ID. It is equal to `signalOrdId` |
| cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| tdMode | String | Sub order trade modeMargin mode: `cross`/`isolated`Non-Margin mode: `cash` |
| ccy | String | Margin currencyOnly applicable to cross MARGIN orders in `Futures mode`. |
| ordType | String | Sub order type`market`: Market order`limit`: Limit order`ioc`: Immediate-or-cancel order |
| sz | String | Sub order quantity to buy or sell |
| state | String | Sub order state`canceled``live``partially_filled``filled``cancelling` |
| side | String | Sub order side`buy`,`sell` |
| px | String | Sub order price |
| fee | String | Sub order fee amount |
| feeCcy | String | Sub order fee currency |
| avgPx | String | Sub order average filled price |
| accFillSz | String | Sub order accumulated fill quantity |
| posSide | String | Sub order position side`net` |
| pnl | String | Sub order profit and loss |
| ctVal | String | Contract valueOnly applicable to `FUTURES`/`SWAP` |
| lever | String | Leverage |
| tag | String | Order tag |

### GET / Signal bot event history

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/signal/event-history`

Request Example

```
GET /api/v5/tradingBot/signal/event-history?algoId=623833708424069120
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| after | String | No | Pagination of data to return records `eventCtime` earlier than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records `eventCtime` newer than the requested timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "alertMsg": "{\"marketPosition\":\"short\",\"prevMarketPosition\":\"long\",\"action\":\"sell\",\"instrument\":\"ETHUSDT.P\",\"timestamp\":\"2023-10-16T10:50:00.000Z\",\"maxLag\":\"60\",\"investmentType\":\"base\",\"amount\":\"2\"}",
 "algoId": "623833708424069120",
 "eventCtime": "1697453400959",
 "eventProcessMsg": "Processed reverse entry signal and placed ETH-USDT-SWAP order with all available balance",
 "eventStatus": "success",
 "eventType": "signal_processing",
 "eventUtime": "",
 "triggeredOrdData": [
 {
 "clOrdId": "O634100754731765763"
 },
 {
 "clOrdId": "O634100754752737282"
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
| alertMsg | String | Alert message |
| algoId | String | Algo ID |
| eventType | String | Event type`system_action``user_action``signal_processing` |
| eventCtime | String | Event timestamp of creation. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| eventUtime | String | Event timestamp of update. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| eventProcessMsg | String | Event process message |
| eventStatus | String | Event status`success``failure` |
| triggeredOrdData | Array of objects | Triggered sub order data |
| > clOrdId | String | Sub order client-supplied id |
