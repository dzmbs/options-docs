## Grid Trading

Grid trading works by the simple strategy of buy low and sell high.
After you set the parameters, the system automatically places orders at incrementally increasing or decreasing prices. Overall, the grid bot seeks to capitalize on normal price volatility by placing buy and sell orders at certain regular intervals above and below a predefined base price.

The API endpoints of `Grid Trading` require authentication.

### POST / Place grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/order-algo`

Request Example

```
# Place spot grid algo order
POST /api/v5/tradingBot/grid/order-algo
body
{
 "instId": "BTC-USDT",
 "algoOrdType": "grid",
 "maxPx": "5000",
 "minPx": "400",
 "gridNum": "10",
 "runType": "1",
 "quoteSz": "25",
 "triggerParams":[
 {
 "triggerAction":"stop",
 "triggerStrategy":"price",
 "triggerPx":"1000"
 }
 ]
}

# Place contract grid algo order
POST /api/v5/tradingBot/grid/order-algo
body
{
 "instId": "BTC-USDT-SWAP",
 "algoOrdType": "contract_grid",
 "maxPx": "5000",
 "minPx": "400",
 "gridNum": "10",
 "runType": "1",
 "sz": "200",
 "direction": "long",
 "lever": "2",
 "triggerParams":[
 {
 "triggerAction":"start",
 "triggerStrategy":"rsi",
 "timeframe":"30m",
 "thold":"10",
 "triggerCond":"cross",
 "timePeriod":"14"
 },
 {
 "triggerAction":"stop",
 "triggerStrategy":"price",
 "triggerPx":"1000",
 "stopType":"2"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP` |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| maxPx | String | Yes | Upper price of price range |
| minPx | String | Yes | Lower price of price range |
| gridNum | String | Yes | Grid quantity |
| runType | String | No | Grid type`1`: Arithmetic, `2`: GeometricDefault is Arithmetic |
| tpTriggerPx | String | No | TP tigger priceApplicable to `Spot grid`/`Contract grid` |
| slTriggerPx | String | No | SL tigger priceApplicable to `Spot grid`/`Contract grid` |
| algoClOrdId | String | No | Client-supplied Algo IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Order tag |
| profitSharingRatio | String | No | Profit sharing ratio, it only supports these values`0`,`0.1`,`0.2`,`0.3` 0.1 represents 10% |
| triggerParams | Array of objects | No | Trigger ParametersApplicable to `Spot grid`/`Contract grid` |
| > triggerAction | String | Yes | Trigger action`start``stop` |
| > triggerStrategy | String | Yes | Trigger strategy`instant``price``rsi`Default is `instant` |
| > delaySeconds | String | No | Delay seconds after action triggered |
| > timeframe | String | No | K-line type`3m`, `5m`, `15m`, `30m` (`m`: minute)`1H`, `4H` (`H`: hour)`1D` (`D`: day)This field is only valid when `triggerStrategy` is `rsi` |
| > thold | String | No | ThresholdThe value should be an integer between 1 to 100This field is only valid when `triggerStrategy` is `rsi` |
| > triggerCond | String | No | Trigger condition`cross_up``cross_down``above``below``cross`This field is only valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | No | Time Period`14`This field is only valid when `triggerStrategy` is `rsi` |
| > triggerPx | String | No | Trigger PriceThis field is only valid when `triggerStrategy` is `price` |
| > stopType | String | No | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positionsThis field is only valid when `triggerAction` is `stop` |

Spot Grid Order

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| quoteSz | String | Conditional | Invest amount for quote currencyEither `quoteSz` or `baseSz` is required |
| baseSz | String | Conditional | Invest amount for base currencyEither `quoteSz` or `baseSz` is required |
| tradeQuoteCcy | String | No | The quote currency for trading. Only applicable to SPOT.The default value is the quote currency of instId, e.g. USD for BTC-USD. |

Contract Grid Order

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sz | String | Yes | Used margin based on `USDT` |
| direction | String | Yes | Contract grid type`long`,`short`,`neutral` |
| lever | String | Yes | Leverage |
| basePos | Boolean | No | Whether or not open a position when the strategy activates Default is `false`Neutral contract grid should omit the parameter |
| tpRatio | String | No | Take profit ratio, 0.1 represents 10% |
| slRatio | String | No | Stop loss ratio, 0.1 represents 10% |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "447053782921515008",
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
| sCode | String | The code of the event execution result, `0` means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |
| tag | String | Order tag |

### POST / Amend grid algo order basic param

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/amend-algo-basic-param`

Request Example

```
POST /api/v5/tradingBot/grid/amend-algo-basic-param
body
 {
 "algoId": "448965992920907776",
 "maxPx": "100",
 "minPx": "10",
 "gridNum": "5"
 "topupAmount": "123.45"
 }
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| minPx | String | Yes | Minimum price range |
| maxPx | String | Yes | Maximum price range |
| gridNum | String | Yes | Grid quantity |
| topupAmount | String | No | Contract grid only. Optional client-supplied top up investment amount. If this is not supplied or explicitly supplied as "0", the required top up investment amount to edit grid parameters is topped up by default |

Response Example

```
{
 "code": "55186",
 "msg": "Due to market fluctuations, your investment amount is too large to apply these modifications.",
 "data": [
 {
 "algoId": "4283223775520665600",
 "maxTopupAmount": "12456.78",
 "requiredTopupAmount": "12.34"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| requiredTopupAmount | String | Required top up investment amount to edit grid parameters. |
| maxTopupAmount | String | Contract grid only. Max top up investment amount to edit grid parameters |

#### Error Code

| Error Code | HTTP Status code | Error Message |
| --- | --- | --- |
| 51000 | 400 | Parameter {param} error. This would also be returned when a grid bot does not support the parameter |
| 51346 | 400 | Upper limit must be greater than the lower limit price. |
| 55123 | 400 | There is insufficient balance for transfer. |
| 55124 | 200 | Due to market fluctuations, your investment amount is insufficient to apply these modifications. |
| 55186 | 200 | Due to market fluctuations, your investment amount is too large to apply these modifications. |

### POST / Amend grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/amend-order-algo`

Request Example

```
POST /api/v5/tradingBot/grid/amend-order-algo
body
{
 "algoId":"448965992920907776",
 "instId":"BTC-USDT-SWAP",
 "slTriggerPx":"1200",
 "tpTriggerPx":""
}

POST /api/v5/tradingBot/grid/amend-order-algo
body
{
 "algoId":"578963447615062016",
 "instId":"BTC-USDT",
 "triggerParams":[
 {
 "triggerAction":"stop",
 "triggerStrategy":"price",
 "triggerPx":"1000"
 }
 ]
}

POST /api/v5/tradingBot/grid/amend-order-algo
body
{
 "algoId":"578963447615062016",
 "instId":"BTC-USDT-SWAP",
 "triggerParams":[
 {
 "triggerAction":"stop",
 "triggerStrategy":"instant",
 "stopType":"1"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP` |
| slTriggerPx | String | No | New stop-loss trigger priceif slTriggerPx is set "" means stop-loss trigger price is canceled.Either `slTriggerPx` or `tpTriggerPx` is required. |
| tpTriggerPx | String | No | New take-profit trigger priceif tpTriggerPx is set "" means take-profit trigger price is canceled. |
| tpRatio | String | No | Take profit ratio, 0.1 represents 10%, only applicable to contract gridif it is set "" means take-profit ratio is canceled. |
| slRatio | String | No | Stop loss ratio, 0.1 represents 10%, only applicable to contract grid`if it is set "" means stop-loss ratio is canceled. |
| topUpAmt | String | No | Top up amount, only applicable to spot grid |
| triggerParams | Array of objects | No | Trigger Parameters |
| > triggerAction | String | Yes | Trigger action`start``stop` |
| > triggerStrategy | String | Yes | Trigger strategy`instant``price``rsi` |
| > triggerPx | String | No | Trigger PriceThis field is only valid when `triggerStrategy` is `price` |
| > stopType | String | No | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positionsThis field is only valid when `triggerAction` is `stop` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "algoClOrdId": "",
 "algoId":"448965992920907776",
 "sCode":"0",
 "sMsg":"",
 "tag": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | The code of the event execution result, `0` means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |
| tag | String | Order tag |

### POST / Stop grid algo order

A maximum of 10 orders can be stopped per request.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/stop-order-algo`

Request Example

```
POST /api/v5/tradingBot/grid/stop-order-algo
body
[
 {
 "algoId":"448965992920907776",
 "instId":"BTC-USDT",
 "stopType":"1",
 "algoOrdType":"grid"
 }
]
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| stopType | String | Yes | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positions |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "448965992920907776",
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
| sCode | String | The code of the event execution result, `0` means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |
| tag | String | Order tag |

### POST / Close position for contract grid

Close position when the contract grid stop type is 'keep position'.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/close-position`

Request Example

```
POST /api/v5/tradingBot/grid/close-position
body
{
 "algoId":"448965992920907776",
 "mktClose":true
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| mktClose | Boolean | Yes | Market close all the positions or not`true`: Market close all position, `false`: Close part of position |
| sz | String | Conditional | Close position amount, with unit of `contract`If `mktClose` is `false`, the parameter is required. |
| px | String | Conditional | Close position priceIf `mktClose` is `false`, the parameter is required. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "448965992920907776",
 "ordId": "",
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
| ordId | String | Close position order IDIf `mktClose` is `true`, the parameter will return "". |
| algoClOrdId | String | Client-supplied Algo ID |
| tag | String | Order tag |

### POST / Cancel close position order for contract grid

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/cancel-close-order`

Request Example

```
POST /api/v5/tradingBot/grid/cancel-close-order
body
{
 "algoId":"448965992920907776",
 "ordId":"570627699870375936"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| ordId | String | Yes | Close position order ID |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "algoClOrdId": "",
 "algoId": "448965992920907776",
 "ordId": "570627699870375936",
 "tag": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| ordId | String | Close position order ID |
| algoClOrdId | String | Client-supplied Algo ID |
| tag | String | Order tag |

### POST / Instant trigger grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/order-instant-trigger`

Request Example

```
POST /api/v5/tradingBot/grid/order-instant-trigger
body
{
 "algoId":"561564133246894080"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| topUpAmt | String | No | Top up amount, only applicable to spot grid |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "561564133246894080"
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

### GET / Grid algo order list

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/orders-algo-pending`

Request Example

```
GET /api/v5/tradingBot/grid/orders-algo-pending?algoOrdType=grid
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| algoId | String | No | Algo ID |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |
| instType | String | No | Instrument type`SPOT``MARGIN``FUTURES``SWAP` |
| after | String | No | Pagination of data to return records earlier than the requested `algoId`. |
| before | String | No | Pagination of data to return records newer than the requested `algoId`. |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "actualLever": "",
 "algoClOrdId": "",
 "algoId": "56802********64032",
 "algoOrdType": "grid",
 "arbitrageNum": "0",
 "availEq": "",
 "basePos": false,
 "baseSz": "0",
 "cTime": "1681700496249",
 "cancelType": "0",
 "direction": "",
 "floatProfit": "0",
 "gridNum": "10",
 "gridProfit": "0",
 "instFamily": "",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "investment": "25",
 "lever": "",
 "liqPx": "",
 "maxPx": "5000",
 "minPx": "400",
 "ordFrozen": "",
 "pnlRatio": "0",
 "quoteSz": "25",
 "rebateTrans": [
 {
 "rebate": "0",
 "rebateCcy": "BTC"
 },
 {
 "rebate": "0",
 "rebateCcy": "USDT"
 }
 ],
 "runType": "1",
 "slTriggerPx": "",
 "state": "running",
 "stopType": "",
 "sz": "",
 "tag": "",
 "totalPnl": "0",
 "tpTriggerPx": "",
 "triggerParams": [
 {
 "triggerAction": "start",
 "delaySeconds": "0",
 "triggerStrategy": "instant",
 "triggerType": "auto",
 "triggerTime": ""
 },
 {
 "triggerAction": "stop",
 "delaySeconds": "0",
 "triggerStrategy": "instant",
 "stopType": "1",
 "triggerPx": "1000",
 "triggerType": "manual",
 "triggerTime": ""
 }
 ],
 "uTime": "1682062564350",
 "uly": "BTC-USDT",
 "profitSharingRatio": "",
 "copyType": "0",
 "fee": "",
 "feeCcy": "",
 "fundingFee": "",
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
| instId | String | Instrument ID |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| state | String | Algo order state`starting``running``stopping``pending_signal``no_close_position`: stopped algo order but have not closed position yet |
| rebateTrans | Array of objects | Rebate transfer info |
| > rebate | String | Rebate amount |
| > rebateCcy | String | Rebate currency |
| triggerParams | Array of objects | Trigger Parameters |
| > triggerAction | String | Trigger action`start``stop` |
| > triggerStrategy | String | Trigger strategy`instant``price``rsi` |
| > delaySeconds | String | Delay seconds after action triggered |
| > triggerTime | String | Actual action triggered time, unix timestamp format in milliseconds, e.g. `1597026383085` |
| > triggerType | String | Actual action triggered type`manual``auto` |
| > timeframe | String | K-line type`3m`, `5m`, `15m`, `30m` (`m`: minute)`1H`, `4H` (`H`: hour)`1D` (`D`: day)This field is only valid when `triggerStrategy` is `rsi` |
| > thold | String | ThresholdThe value should be an integer between 1 to 100This field is only valid when `triggerStrategy` is `rsi` |
| > triggerCond | String | Trigger condition`cross_up``cross_down``above``below``cross`This field is only valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | Time Period`14`This field is only valid when `triggerStrategy` is `rsi` |
| > triggerPx | String | Trigger PriceThis field is only valid when `triggerStrategy` is `price` |
| > stopType | String | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positionsThis field is only valid when `triggerAction` is `stop` |
| maxPx | String | Upper price of price range |
| minPx | String | Lower price of price range |
| gridNum | String | Grid quantity |
| runType | String | Grid type`1`: Arithmetic, `2`: Geometric |
| tpTriggerPx | String | Take-profit trigger price |
| slTriggerPx | String | Stop-loss trigger price |
| arbitrageNum | String | The number of arbitrages executed |
| totalPnl | String | Total P&L |
| pnlRatio | String | P&L ratio |
| investment | String | Accumulated investment amountSpot grid investment amount calculated on quote currency |
| gridProfit | String | Grid profit |
| floatProfit | String | Variable P&L |
| cancelType | String | Algo order stop reason`0`: None`1`: Manual stop`2`: Take profit`3`: Stop loss`4`: Risk control`5`: Delivery`6`: Signal |
| stopType | String | Actual Stop typeSpot `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positions |
| quoteSz | String | Quote currency investment amountOnly applicable to `Spot grid` |
| baseSz | String | Base currency investment amountOnly applicable to `Spot grid` |
| direction | String | Contract grid type`long`,`short`,`neutral`Only applicable to `contract grid` |
| basePos | Boolean | Whether or not to open a position when the strategy is activatedOnly applicable to `contract grid` |
| sz | String | Used margin based on `USDT`Only applicable to `contract grid` |
| lever | String | LeverageOnly applicable to `contract grid` |
| actualLever | String | Actual LeverageOnly applicable to `contract grid` |
| liqPx | String | Estimated liquidation priceOnly applicable to `contract grid` |
| uly | String | UnderlyingOnly applicable to `contract grid` |
| instFamily | String | Instrument familyOnly applicable to `FUTURES`/`SWAP`/`OPTION`Only applicable to `contract grid` |
| ordFrozen | String | Margin used by pending ordersOnly applicable to `contract grid` |
| availEq | String | Available marginOnly applicable to `contract grid` |
| tag | String | Order tag |
| profitSharingRatio | String | Profit sharing ratioValue range [0, 0.3]If it is a normal order (neither copy order nor lead order), this field returns "" |
| copyType | String | Profit sharing order type`0`: Normal order`1`: Copy order without profit sharing`2`: Copy order with profit sharing`3`: Lead order |
| fee | String | Accumulated fee. Only applicable to contract grid, or it will be "" |
| feeCcy | String | Accumulated fee currency. Only applicable to contract grid, or it will be "" |
| fundingFee | String | Accumulated funding fee. Only applicable to contract grid, or it will be "" |
| tradeQuoteCcy | String | The quote currency for trading. |

### GET / Grid algo order history

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/orders-algo-history`

Request Example

```
GET /api/v5/tradingBot/grid/orders-algo-history?algoOrdType=grid
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| algoId | String | No | Algo ID |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |
| instType | String | No | Instrument type`SPOT``MARGIN``FUTURES``SWAP` |
| after | String | No | Pagination of data to return records earlier than the requested `algoId`. |
| before | String | No | Pagination of data to return records newer than the requested `algoId`. |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "actualLever": "",
 "algoClOrdId": "",
 "algoId": "565849588675117056",
 "algoOrdType": "grid",
 "arbitrageNum": "0",
 "availEq": "",
 "basePos": false,
 "baseSz": "0",
 "cTime": "1681181054927",
 "cancelType": "1",
 "direction": "",
 "floatProfit": "0",
 "gridNum": "10",
 "gridProfit": "0",
 "instFamily": "",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "investment": "25",
 "lever": "0",
 "liqPx": "",
 "maxPx": "5000",
 "minPx": "400",
 "ordFrozen": "",
 "pnlRatio": "0",
 "quoteSz": "25",
 "rebateTrans": [
 {
 "rebate": "0",
 "rebateCcy": "BTC"
 },
 {
 "rebate": "0",
 "rebateCcy": "USDT"
 }
 ],
 "runType": "1",
 "slTriggerPx": "0",
 "state": "stopped",
 "stopResult": "0",
 "stopType": "1",
 "sz": "",
 "tag": "",
 "totalPnl": "0",
 "tpTriggerPx": "0",
 "triggerParams": [
 {
 "triggerAction": "start",
 "delaySeconds": "0",
 "triggerStrategy": "instant",
 "triggerType": "auto",
 "triggerTime": ""
 },
 {
 "triggerAction": "stop",
 "delaySeconds": "0",
 "triggerStrategy": "instant",
 "stopType": "1",
 "triggerPx": "1000",
 "triggerType": "manual",
 "triggerTime": "1681181186484"
 }
 ],
 "uTime": "1681181186496",
 "uly": "BTC-USDT",
 "profitSharingRatio": "",
 "copyType": "0",
 "fee": "",
 "feeCcy": "",
 "fundingFee": "",
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
| instId | String | Instrument ID |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| state | String | Algo order state`stopped` |
| rebateTrans | Array of objects | Rebate transfer info |
| > rebate | String | Rebate amount |
| > rebateCcy | String | Rebate currency |
| triggerParams | Array of objects | Trigger Parameters |
| > triggerAction | String | Trigger action`start``stop` |
| > triggerStrategy | String | Trigger strategy`instant``price``rsi` |
| > delaySeconds | String | Delay seconds after action triggered |
| > triggerTime | String | Actual action triggered time, unix timestamp format in milliseconds, e.g. `1597026383085` |
| > triggerType | String | Actual action triggered type`manual``auto` |
| > timeframe | String | K-line type`3m`, `5m`, `15m`, `30m` (`m`: minute)`1H`, `4H` (`H`: hour)`1D` (`D`: day)This field is only valid when `triggerStrategy` is `rsi` |
| > thold | String | ThresholdThe value should be an integer between 1 to 100This field is only valid when `triggerStrategy` is `rsi` |
| > triggerCond | String | Trigger condition`cross_up``cross_down``above``below``cross`This field is only valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | Time Period`14`This field is only valid when `triggerStrategy` is `rsi` |
| > triggerPx | String | Trigger PriceThis field is only valid when `triggerStrategy` is `price` |
| > stopType | String | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positionsThis field is only valid when `triggerAction` is `stop` |
| maxPx | String | Upper price of price range |
| minPx | String | Lower price of price range |
| gridNum | String | Grid quantity |
| runType | String | Grid type`1`: Arithmetic, `2`: Geometric |
| tpTriggerPx | String | Take-profit trigger price |
| slTriggerPx | String | Stop-loss trigger price |
| arbitrageNum | String | The number of arbitrages executed |
| totalPnl | String | Total P&L |
| pnlRatio | String | P&L ratio |
| investment | String | Accumulated investment amountSpot grid investment amount calculated on quote currency |
| gridProfit | String | Grid profit |
| floatProfit | String | Variable P&L |
| cancelType | String | Algo order stop reason`0`: None`1`: Manual stop`2`: Take profit`3`: Stop loss`4`: Risk control`5`: Delivery`6`: Signal |
| stopType | String | Actual Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positions |
| quoteSz | String | Quote currency investment amountOnly applicable to `Spot grid` |
| baseSz | String | Base currency investment amountOnly applicable to `Spot grid` |
| direction | String | Contract grid type`long`,`short`,`neutral`Only applicable to `contract grid` |
| basePos | Boolean | Whether or not to open a position when the strategy is activatedOnly applicable to `contract grid` |
| sz | String | Used margin based on `USDT`Only applicable to `contract grid` |
| lever | String | LeverageOnly applicable to `contract grid` |
| actualLever | String | Actual LeverageOnly applicable to `contract grid` |
| liqPx | String | Estimated liquidation priceOnly applicable to `contract grid` |
| uly | String | UnderlyingOnly applicable to `contract grid` |
| instFamily | String | Instrument familyOnly applicable to `FUTURES`/`SWAP`/`OPTION`Only applicable to `contract grid` |
| ordFrozen | String | Margin used by pending ordersOnly applicable to `contract grid` |
| availEq | String | Available marginOnly applicable to `contract grid` |
| tag | String | Order tag |
| profitSharingRatio | String | Profit sharing ratioValue range [0, 0.3]If it is a normal order (neither copy order nor lead order), this field returns "" |
| copyType | String | Profit sharing order type`0`: Normal order`1`: Copy order without profit sharing`2`: Copy order with profit sharing`3`: Lead order |
| fee | String | Accumulated fee. Only applicable to contract grid, or it will be "" |
| feeCcy | String | Accumulated fee currency. Only applicable to contract grid, or it will be "" |
| fundingFee | String | Accumulated funding fee. Only applicable to contract grid, or it will be "" |
| stopResult | String | Stop result`0`: default, `1`: Successful selling of currency at market price, `-1`: Failed to sell currency at market priceOnly applicable to `Spot grid` |
| tradeQuoteCcy | String | The quote currency for trading. |

### GET / Grid algo order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/orders-algo-details`

Request Example

```
GET /api/v5/tradingBot/grid/orders-algo-details?algoId=448965992920907776&algoOrdType=grid
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| algoId | String | Yes | Algo ID |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "actualLever": "",
 "activeOrdNum": "0",
 "algoClOrdId": "",
 "algoId": "448965992920907776",
 "algoOrdType": "grid",
 "annualizedRate": "0",
 "arbitrageNum": "0",
 "availEq": "",
 "basePos": false,
 "baseSz": "0",
 "cTime": "1681181054927",
 "cancelType": "1",
 "curBaseSz": "0",
 "curQuoteSz": "0",
 "direction": "",
 "eq": "",
 "floatProfit": "0",
 "gridNum": "10",
 "gridProfit": "0",
 "instFamily": "",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "investment": "25",
 "lever": "0",
 "liqPx": "",
 "maxPx": "5000",
 "minPx": "400",
 "ordFrozen": "",
 "perMaxProfitRate": "1.14570215",
 "perMinProfitRate": "0.0991200440528634356837",
 "pnlRatio": "0",
 "profit": "0.00000000",
 "quoteSz": "25",
 "rebateTrans": [
 {
 "rebate": "0",
 "rebateCcy": "BTC"
 },
 {
 "rebate": "0",
 "rebateCcy": "USDT"
 }
 ],
 "runType": "1",
 "runPx": "30089.7",
 "singleAmt": "0.00101214",
 "slTriggerPx": "0",
 "state": "stopped",
 "stopResult": "0",
 "stopType": "1",
 "sz": "",
 "tag": "",
 "totalAnnualizedRate": "0",
 "totalPnl": "0",
 "tpTriggerPx": "0",
 "tradeNum": "0",
 "triggerParams": [
 {
 "triggerAction": "start",
 "delaySeconds": "0",
 "triggerStrategy": "instant",
 "triggerType": "auto",
 "triggerTime": ""
 },
 {
 "triggerAction": "stop",
 "delaySeconds": "0",
 "triggerStrategy": "instant",
 "stopType": "1",
 "triggerType": "manual",
 "triggerTime": "1681181186484"
 }
 ],
 "uTime": "1681181186496",
 "uly": "",
 "profitSharingRatio": "",
 "copyType": "0",
 "tpRatio": "",
 "slRatio": "",
 "fee": "",
 "feeCcy": "",
 "fundingFee": "",
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
| instId | String | Instrument ID |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| algoOrdType | String | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| state | String | Algo order state`starting``running``stopping``no_close_position`: stopped algo order but have not closed position yet`stopped` |
| rebateTrans | Array of objects | Rebate transfer info |
| > rebate | String | Rebate amount |
| > rebateCcy | String | Rebate currency |
| triggerParams | Array of objects | Trigger Parameters |
| > triggerAction | String | Trigger action`start``stop` |
| > triggerStrategy | String | Trigger strategy`instant``price``rsi` |
| > delaySeconds | String | Delay seconds after action triggered |
| > triggerTime | String | Actual action triggered time, unix timestamp format in milliseconds, e.g. `1597026383085` |
| > triggerType | String | Actual action triggered type`manual``auto` |
| > timeframe | String | K-line type`3m`, `5m`, `15m`, `30m` (`m`: minute)`1H`, `4H` (`H`: hour)`1D` (`D`: day)This field is only valid when `triggerStrategy` is `rsi` |
| > thold | String | ThresholdThe value should be an integer between 1 to 100This field is only valid when `triggerStrategy` is `rsi` |
| > triggerCond | String | Trigger condition`cross_up``cross_down``above``below``cross`This field is only valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | Time Period`14`This field is only valid when `triggerStrategy` is `rsi` |
| > triggerPx | String | Trigger PriceThis field is only valid when `triggerStrategy` is `price` |
| > stopType | String | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positionsThis field is only valid when `triggerAction` is `stop` |
| maxPx | String | Upper price of price range |
| minPx | String | Lower price of price range |
| gridNum | String | Grid quantity |
| runType | String | Grid type`1`: Arithmetic, `2`: Geometric |
| tpTriggerPx | String | Take-profit trigger price |
| slTriggerPx | String | Stop-loss trigger price |
| tradeNum | String | The number of trades executed |
| arbitrageNum | String | The number of arbitrages executed |
| singleAmt | String | Amount per grid |
| perMinProfitRate | String | Estimated minimum Profit margin per grid |
| perMaxProfitRate | String | Estimated maximum Profit margin per grid |
| runPx | String | Price at launch |
| totalPnl | String | Total P&L |
| pnlRatio | String | P&L ratio |
| investment | String | Accumulated investment amountSpot grid investment amount calculated on quote currency |
| gridProfit | String | Grid profit |
| floatProfit | String | Variable P&L |
| totalAnnualizedRate | String | Total annualized rate |
| annualizedRate | String | Grid annualized rate |
| cancelType | String | Algo order stop reason`0`: None`1`: Manual stop`2`: Take profit`3`: Stop loss`4`: Risk control`5`: Delivery`6`: Signal |
| stopType | String | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positions |
| activeOrdNum | String | Total count of pending sub orders |
| quoteSz | String | Quote currency investment amountOnly applicable to `Spot grid` |
| baseSz | String | Base currency investment amountOnly applicable to `Spot grid` |
| curQuoteSz | String | Assets of quote currency currently heldOnly applicable to `Spot grid` |
| curBaseSz | String | Assets of base currency currently heldOnly applicable to `Spot grid` |
| profit | String | Current available profit based on quote currencyOnly applicable to `Spot grid` |
| stopResult | String | Stop result`0`: default, `1`: Successful selling of currency at market price, `-1`: Failed to sell currency at market priceOnly applicable to `Spot grid` |
| direction | String | Contract grid type`long`,`short`,`neutral`Only applicable to `contract grid` |
| basePos | Boolean | Whether or not to open a position when the strategy is activatedOnly applicable to `contract grid` |
| sz | String | Used margin based on `USDT`Only applicable to `contract grid` |
| lever | String | LeverageOnly applicable to `contract grid` |
| actualLever | String | Actual LeverageOnly applicable to `contract grid` |
| liqPx | String | Estimated liquidation priceOnly applicable to `contract grid` |
| uly | String | UnderlyingOnly applicable to `contract grid` |
| instFamily | String | Instrument familyOnly applicable to `FUTURES`/`SWAP`/`OPTION`Only applicable to `contract grid` |
| ordFrozen | String | Margin used by pending ordersOnly applicable to `contract grid` |
| availEq | String | Available marginOnly applicable to `contract grid` |
| eq | String | Total equity of strategy accountOnly applicable to `contract grid` |
| tag | String | Order tag |
| profitSharingRatio | String | Profit sharing ratioValue range [0, 0.3]If it is a normal order (neither copy order nor lead order), this field returns "" |
| copyType | String | Profit sharing order type`0`: Normal order`1`: Copy order without profit sharing`2`: Copy order with profit sharing`3`: Lead order |
| tpRatio | String | Take profit ratio, 0.1 represents 10% |
| slRatio | String | Stop loss ratio, 0.1 represents 10% |
| fee | String | Accumulated fee. Only applicable to contract grid, or it will be "" |
| feeCcy | String | Accumulated fee currency. Only applicable to contract grid, or it will be "" |
| fundingFee | String | Accumulated funding fee. Only applicable to contract grid, or it will be "" |
| tradeQuoteCcy | String | The quote currency for trading. |

### GET / Grid algo sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/sub-orders`

Request Example

```
GET /api/v5/tradingBot/grid/sub-orders?algoId=123456&type=live&algoOrdType=grid
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| algoId | String | Yes | Algo ID |
| type | String | Yes | Sub order state`live``filled` |
| groupId | String | No | Group ID |
| after | String | No | Pagination of data to return records earlier than the requested `ordId`. |
| before | String | No | Pagination of data to return records newer than the requested `ordId`. |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "accFillSz": "0",
 "algoClOrdId": "",
 "algoId": "448965992920907776",
 "algoOrdType": "grid",
 "avgPx": "0",
 "cTime": "1653347949771",
 "ccy": "",
 "ctVal": "",
 "fee": "0",
 "feeCcy": "USDC",
 "groupId": "3",
 "instId": "BTC-USDC",
 "instType": "SPOT",
 "lever": "0",
 "ordId": "449109084439187456",
 "ordType": "limit",
 "pnl": "0",
 "posSide": "net",
 "px": "30404.3",
 "rebate": "0",
 "rebateCcy": "USDT",
 "side": "sell",
 "state": "live",
 "sz": "0.00059213",
 "tag": "",
 "tdMode": "cash",
 "uTime": "1653347949831"
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
| instId | String | Instrument ID |
| algoOrdType | String | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| groupId | String | Group ID |
| ordId | String | Sub order ID |
| cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| tdMode | String | Sub order trade modeMargin mode: `cross`/`isolated`Non-Margin mode: `cash` |
| ccy | String | Margin currencyOnly applicable to cross MARGIN orders in `Futures mode`. |
| ordType | String | Sub order type`market`: Market order`limit`: Limit order`ioc`: Immediate-or-cancel order |
| sz | String | Sub order quantity to buy or sell |
| state | String | Sub order state`canceled``live``partially_filled``filled``cancelling` |
| side | String | Sub order side`buy` `sell` |
| px | String | Sub order price |
| fee | String | Sub order fee amount |
| feeCcy | String | Sub order fee currency |
| rebate | String | Sub order rebate amount |
| rebateCcy | String | Sub order rebate currency |
| avgPx | String | Sub order average filled price |
| accFillSz | String | Sub order accumulated fill quantity |
| posSide | String | Sub order position side`net` |
| pnl | String | Sub order profit and loss |
| ctVal | String | Contract valueOnly applicable to `FUTURES`/`SWAP` |
| lever | String | Leverage |
| tag | String | Order tag |

### GET / Grid algo order positions

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/positions`

Request Example

```
GET /api/v5/tradingBot/grid/positions?algoId=448965992920907776&algoOrdType=contract_grid
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`contract_grid`: Contract grid |
| algoId | String | Yes | Algo ID |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "adl": "1",
 "algoClOrdId": "",
 "algoId": "449327675342323712",
 "avgPx": "29215.0142857142857149",
 "cTime": "1653400065917",
 "ccy": "USDT",
 "imr": "2045.386",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "last": "29206.7",
 "lever": "5",
 "liqPx": "661.1684795867162",
 "markPx": "29213.9",
 "mgnMode": "cross",
 "mgnRatio": "217.19370606167573",
 "mmr": "40.907720000000005",
 "notionalUsd": "10216.70307",
 "pos": "35",
 "posSide": "net",
 "uTime": "1653400066938",
 "upl": "1.674999999999818",
 "uplRatio": "0.0008190504784478"
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

### POST / Spot grid withdraw income

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/withdraw-income`

Request Example

```
POST /api/v5/tradingBot/grid/withdraw-income
body
{
 "algoId":"448965992920907776"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "algoClOrdId": "",
 "algoId":"448965992920907776",
 "profit":"100"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| profit | String | Withdraw profit |

### POST / Compute margin balance

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/compute-margin-balance`

Request Example

```
POST /api/v5/tradingBot/grid/compute-margin-balance
body {
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
| amt | String | No | Adjust margin balance amountDefault is zero. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "lever": "0.3877200981166066",
 "maxAmt": "1.8309562403342999"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| maxAmt | String | Maximum adjustable margin balance amount |
| lever | String | Leverage after adjustment of margin balance |

### POST / Adjust margin balance

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/margin-balance`

Request Example

```
POST /api/v5/tradingBot/grid/margin-balance
body {
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
| amt | String | Conditional | Adjust margin balance amountEither `amt` or `percent` is required. |
| percent | String | Conditional | Adjust margin balance percentage |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
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
| algoClOrdId | String | Client-supplied Algo ID |

### POST / Add investment

It is used to add investment and only applicable to contract gird.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/adjust-investment`

Request Example

```
POST /api/v5/tradingBot/grid/adjust-investment
body
{
 "algoId":"448965992920907776",
 "amt":"12"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| amt | String | Yes | The amount is going to be added |
| allowReinvestProfit | String | No | Whether reinvesting profits, only applicable to spot grid.`true` or `false`. The default is true. |

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

### GET / Grid AI parameter (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/ai-param`

Request Example

```
GET /api/v5/tradingBot/grid/ai-param?instId=BTC-USDT&algoOrdType=grid
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| direction | String | Conditional | Contract grid type`long`,`short`,`neutral`Required in the case of `contract_grid` |
| duration | String | No | Back testing duration in number of daysSpot grid default is `7D` with available durations of `7D`, `30D` and `180D`Contract grid default is `14D` with available durations of `7D`, `14D` and `30D` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoOrdType": "grid",
 "annualizedRate": "1.5849",
 "ccy": "USDT",
 "direction": "",
 "duration": "7D",
 "gridNum": "5",
 "instId": "BTC-USDT",
 "lever": "0",
 "maxPx": "21373.3",
 "minInvestment": "0.89557758",
 "minPx": "15544.2",
 "perGridProfitRatio": "4.566226200302574",
 "perMaxProfitRate": "0.0733865364573281",
 "perMinProfitRate": "0.0561101403446263",
 "runType": "1",
 "sourceCcy": ""
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| algoOrdType | String | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| duration | String | Back testing duration`7D`: 7 Days, `30D`: 30 Days, `180D`: 180 Days |
| gridNum | String | Grid quantity |
| maxPx | String | Upper price of price range |
| minPx | String | Lower price of price range |
| perMaxProfitRate | String | Estimated maximum Profit margin per grid |
| perMinProfitRate | String | Estimated minimum Profit margin per grid |
| perGridProfitRatio | String | Per grid profit ratio |
| annualizedRate | String | Grid annualized rate |
| minInvestment | String | The minimum invest amount |
| ccy | String | The invest currency |
| runType | String | Grid type`1`: Arithmetic, `2`: Geometric |
| direction | String | Contract grid type`long`,`short`,`neutral`Only applicable to contract grid |
| lever | String | LeverageOnly applicable to contract grid |
| sourceCcy | String | Source currency |

### POST / Compute min investment (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`POST /api/v5/tradingBot/grid/min-investment`

Request Example

```
POST /api/v5/tradingBot/grid/min-investment
body
{
 "instId": "ETH-USDT",
 "algoOrdType":"grid",
 "gridNum": "50",
 "maxPx":"5000",
 "minPx":"3000",
 "runType":"1",
 "investmentData":[
 {
 "amt":"0.01",
 "ccy":"ETH"
 },
 {
 "amt":"100",
 "ccy":"USDT"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT-SWAP` |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| maxPx | String | Yes | Upper price of price range |
| minPx | String | Yes | Lower price of price range |
| gridNum | String | Yes | Grid quantity |
| runType | String | Yes | Grid type`1`: Arithmetic, `2`: Geometric |
| direction | String | Conditional | Contract grid type`long`,`short`,`neutral`Only applicable to `contract grid` |
| lever | String | Conditional | LeverageOnly applicable to `contract grid` |
| basePos | Boolean | No | Whether or not open a position when the strategy activatesDefault is `false`Neutral contract grid should omit the parameterOnly applicable to `contract grid` |
| investmentType | String | No | Investment type, only applicable to `grid` `quote``base``dual` |
| triggerStrategy | String | No | Trigger stragety, `instant``price``rsi` |
| topUpAmt | String | No | Top up amount, only applicable to spot grid |
| investmentData | Array of objects | No | Invest Data |
| > amt | String | Yes | Invest amount |
| > ccy | String | Yes | Invest currency |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "minInvestmentData": [
 {
 "amt":"0.1",
 "ccy":"ETH"
 },
 {
 "amt":"100",
 "ccy":"USDT"
 }
 ],
 "singleAmt":"10"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| minInvestmentData | Array of objects | Minimum invest Data |
| > amt | String | Minimum invest amount |
| > ccy | String | Minimum Invest currency |
| singleAmt | String | Single grid trading amountIn terms of `spot grid`, the unit is `quote currency`In terms of `contract grid`, the unit is `contract` |

### GET / RSI back testing (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/public/rsi-back-testing`

Request Example

```
GET /api/v5/tradingBot/public/rsi-back-testing?instId=BTC-USDT&thold=30&timeframe=3m&timePeriod=14
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT`Only applicable to `SPOT` |
| timeframe | String | Yes | K-line type`3m`, `5m`, `15m`, `30m` (`m`: minute)`1H`, `4H` (`H`: hour)`1D` (`D`: day) |
| thold | String | Yes | ThresholdThe value should be an integer between 1 to 100 |
| timePeriod | String | Yes | Time Period`14` |
| triggerCond | String | No | Trigger condition`cross_up``cross_down``above``below``cross`Default is `cross_down` |
| duration | String | No | Back testing duration`1M` (`M`: month)Default is `1M` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "triggerNum": "164"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| triggerNum | String | Trigger number |

### GET / Max grid quantity (public)

Authentication is not required for this public endpoint.

Maximum grid quantity can be retrieved from this endpoint. Minimum grid quantity always is 2.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/tradingBot/grid/grid-quantity`

Request Example

```
GET /api/v5/tradingBot/grid/grid-quantity?instId=BTC-USDT-SWAP&runType=1&algoOrdType=contract_grid&maxPx=70000&minPx=50000&lever=5
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| runType | String | Yes | Grid type`1`: Arithmetic `2`: Geometric |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| maxPx | String | Yes | Upper price of price range |
| minPx | String | Yes | Lower price of price range |
| lever | String | Conditional | Leverage, it is required for contract grid |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "maxGridQty": "285"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| maxGridQty | String | Maximum grid quantity |

### POST / Copy grid algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID + Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/tradingBot/grid/copy-order-algo`

Request Example

```
# Spot grid copy
POST /api/v5/tradingBot/grid/copy-order-algo
body
{
 "instId": "BTC-USDT",
 "algoOrdType": "grid",
 "sourceAlgoId": "580007082221121536",
 "quoteSz": "1000"
}
```

```
# Contract grid copy
POST /api/v5/tradingBot/grid/copy-order-algo
body
{
 "instId": "BTC-USDT-SWAP",
 "algoOrdType": "contract_grid",
 "sourceAlgoId": "580007082221121536",
 "lever": "3",
 "autoReserve": true,
 "sz": "5000"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| algoOrdType | String | Yes | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| sourceAlgoId | String | Yes | Lead algo order ID to follow and copy from |
| quoteSz | String | No | Quote currency investment amountOnly applicable to `grid` |
| lever | String | No | LeverageOnly applicable to `contract_grid` |
| autoReserve | Boolean | No | Whether to auto-reserve margin. Only applicable to `contract_grid``true`: Actual margin and extra margin are automatically calculated based on `sz``false`: Manually specify `actualMarginSz` and `extraMarginSz` |
| sz | String | No | Total investment amount in USDT. Required when `autoReserve` is `true`Only applicable to `contract_grid` |
| actualMarginSz | String | No | Actual margin. Required when `autoReserve` is `false`Only applicable to `contract_grid` |
| extraMarginSz | String | No | Extra margin reserved. Defaults to `0` when unspecifiedOnly applicable to `contract_grid` |
| algoClOrdId | String | No | Client-supplied Algo ID |
| tag | String | No | Order tag |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "581234567890123456",
 "algoClOrdId": "",
 "sCode": "0",
 "sMsg": "",
 "tag": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |
| tag | String | Order tag |

### WS / Spot grid algo orders channel

Retrieve spot grid algo orders. Data will be pushed when triggered by events such as placing/canceling order. It will also be pushed in regular interval according to subscription granularity.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "grid-orders-spot",
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
 "channel": "grid-orders-spot",
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
| > channel | String | Yes | Channel name`grid-orders-spot` |
| > instType | String | Yes | Instrument type`SPOT``ANY` |
| > instId | String | No | Instrument ID |
| > algoId | String | No | Algo Order ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "grid-orders-spot",
 "instType": "ANY"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-orders-spot\", \"instType\" : \"FUTURES\"}]}",
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
| > instId | String | No | Instrument ID |
| > algoId | String | No | Algo Order ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example:

```
{
 "arg": {
 "channel": "grid-orders-spot",
 "instType": "ANY",
 "uid": "44705892343619584"
 },
 "data": [{
 "algoClOrdId": "",
 "algoId": "568028283477164032",
 "activeOrdNum" : "10",
 "algoOrdType": "grid",
 "annualizedRate": "0",
 "arbitrageNum": "0",
 "baseSz": "0",
 "cTime": "1681700496249",
 "cancelType": "0",
 "curBaseSz": "0",
 "curQuoteSz": "25",
 "floatProfit": "0",
 "gridNum": "10",
 "gridProfit": "0",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "investment": "25",
 "maxPx": "5000",
 "minPx": "400",
 "pTime": "1682416738467",
 "perMaxProfitRate": "1.14570215",
 "perMinProfitRate": "0.0991200440528634356837",
 "pnlRatio": "0",
 "profit": "0",
 "quoteSz": "25",
 "rebateTrans": [{
 "rebate": "0",
 "rebateCcy": "BTC"
 }, {
 "rebate": "0",
 "rebateCcy": "USDT"
 }],
 "runPx": "30031.7",
 "runType": "1",
 "triggerParams": [{
 "triggerAction": "start",
 "triggerStrategy": "instant",
 "delaySeconds": "0",
 "triggerType": "auto",
 "triggerTime": ""
 }, {
 "triggerAction": "stop",
 "triggerStrategy": "instant",
 "delaySeconds": "0",
 "stopType": "1",
 "triggerType": "manual",
 "triggerTime": ""
 }],
 "singleAmt": "0.00101214",
 "slTriggerPx": "",
 "state": "running",
 "stopResult": "0",
 "stopType": "2",
 "tag": "",
 "totalAnnualizedRate": "0",
 "totalPnl": "0",
 "tpTriggerPx": "",
 "tradeNum": "0",
 "uTime": "1682406665527",
 "profitSharingRatio": "",
 "copyType": "0",
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
| > uid | String | User ID |
| data | Array of objects | Subscribed data |
| > algoId | String | Algo ID |
| > algoClOrdId | String | Client-supplied Algo ID |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > algoOrdType | String | Algo order type`grid`: Spot grid |
| > state | String | Algo order state`starting``running``stopping``stopped` |
| > rebateTrans | Array of objects | Rebate transfer info |
| >> rebate | String | Rebate amount |
| >> rebateCcy | String | Rebate currency |
| > triggerParams | Array of objects | Trigger Parameters |
| >> triggerAction | String | Trigger action`start``stop` |
| >> triggerStrategy | String | Trigger strategy`instant``price``rsi` |
| >> delaySeconds | String | Delay seconds after action triggered |
| >> triggerTime | String | Actual action triggered time, unix timestamp format in milliseconds, e.g. `1597026383085` |
| >> triggerType | String | Actual action triggered type`manual``auto` |
| >> timeframe | String | K-line type`3m`, `5m`, `15m`, `30m` (`m`: minute)`1H`, `4H` (`H`: hour)`1D` (`D`: day)This field is only valid when `triggerStrategy` is `rsi` |
| >> thold | String | ThresholdThe value should be an integer between 1 to 100This field is only valid when `triggerStrategy` is `rsi` |
| >> triggerCond | String | Trigger condition`cross_up``cross_down``above``below``cross`This field is only valid when `triggerStrategy` is `rsi` |
| >> timePeriod | String | Time Period`14`This field is only valid when `triggerStrategy` is `rsi` |
| >> triggerPx | String | Trigger PriceThis field is only valid when `triggerStrategy` is `price` |
| >> stopType | String | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positionsThis field is only valid when `triggerAction` is `stop` |
| > maxPx | String | Upper price of price range |
| > minPx | String | Lower price of price range |
| > gridNum | String | Grid quantity |
| > runType | String | Grid type`1`: Arithmetic, `2`: Geometric |
| > tpTriggerPx | String | Take-profit trigger price |
| > slTriggerPx | String | Stop-loss trigger price |
| > tradeNum | String | The number of trades executed |
| > arbitrageNum | String | The number of arbitrages executed |
| > singleAmt | String | Amount per grid |
| > perMinProfitRate | String | Estimated minimum Profit margin per grid |
| > perMaxProfitRate | String | Estimated maximum Profit margin per grid |
| > runPx | String | Price at launch |
| > totalPnl | String | Total P&L |
| > pnlRatio | String | P&L ratio |
| > investment | String | Investment amountSpot grid investment amount calculated on quote currency |
| > gridProfit | String | Grid profit |
| > floatProfit | String | Variable P&L |
| > totalAnnualizedRate | String | Total annualized rate |
| > annualizedRate | String | Grid annualized rate |
| > cancelType | String | Algo order stop reason`0`: None`1`: Manual stop`2`: Take profit`3`: Stop loss`4`: Risk control`5`: Delivery`6`: Signal |
| > stopType | String | Stop type`1`: Sell base currency `2`: Keep base currency |
| > quoteSz | String | Quote currency investment amountOnly applicable to `Spot grid` |
| > baseSz | String | Base currency investment amountOnly applicable to `Spot grid` |
| > curQuoteSz | String | Assets of quote currency currently heldOnly applicable to `Spot grid` |
| > curBaseSz | String | Assets of base currency currently heldOnly applicable to `Spot grid` |
| > profit | String | Current available profit based on quote currencyOnly applicable to `Spot grid` |
| > stopResult | String | Stop result`0`: default, `1`: Successful selling of currency at market price, `-1`: Failed to sell currency at market priceOnly applicable to `Spot grid` |
| > activeOrdNum | String | Total count of pending sub orders |
| > tag | String | Order tag |
| > profitSharingRatio | String | Profit sharing ratioValue range [0, 0.3]If it is a normal order (neither copy order nor lead order), this field returns "" |
| > copyType | String | Profit sharing order type`0`: Normal order`1`: Copy order without profit sharing`2`: Copy order with profit sharing`3`: Lead order |
| > pTime | String | Push time of algo grid information, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > tradeQuoteCcy | String | The quote currency for trading. |

### WS / Contract grid algo orders channel

Retrieve contract grid algo orders. Data will be pushed when triggered by events such as placing/canceling order. It will also be pushed in regular interval according to subscription granularity.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "grid-orders-contract",
 "instType": "SWAP"
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
 "channel": "grid-orders-contract",
 "instType": "SWAP"
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
| > channel | String | Yes | Channel name`grid-orders-contract` |
| > instType | String | Yes | Instrument type`SWAP``FUTURES``ANY` |
| > instId | String | No | Instrument ID |
| > algoId | String | No | Algo Order ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "grid-orders-contract",
 "instType": "ANY"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-orders-contract\", \"instType\" : \"FUTURES\"}]}",
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
| > instId | String | No | Instrument ID |
| > algoId | String | No | Algo Order ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example:

```
{
 "arg": {
 "channel": "grid-orders-contract",
 "instType": "ANY",
 "uid": "4470****9584"
 },
 "data": [{
 "actualLever": "2.3481494635276649",
 "activeOrdNum": "10",
 "algoClOrdId": "",
 "algoId": "571039869070475264",
 "algoOrdType": "contract_grid",
 "annualizedRate": "0",
 "arbitrageNum": "0",
 "availEq": "52.3015392887089673",
 "basePos": true,
 "cTime": "1682418514204",
 "cancelType": "0",
 "direction": "long",
 "eq": "108.7945652387089673",
 "floatProfit": "8.7945652387089673",
 "gridNum": "10",
 "gridProfit": "0",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "investment": "100",
 "lever": "5",
 "liqPx": "16370.482143120824",
 "maxPx": "36437.3",
 "minPx": "26931.9",
 "ordFrozen": "5.38638",
 "pTime": "1682492574068",
 "perMaxProfitRate": "0.1687494513302446",
 "perMinProfitRate": "0.1263869357706788",
 "pnlRatio": "0.0879456523870897",
 "rebateTrans": [{
 "rebate": "0",
 "rebateCcy": "USDT"
 }],
 "runPx": "27306.9",
 "runType": "1",
 "singleAmt": "1",
 "slTriggerPx": "",
 "state": "running",
 "stopType": "0",
 "sz": "100",
 "tag": "",
 "totalAnnualizedRate": "38.52019574554529",
 "totalPnl": "8.7945652387089673",
 "tpTriggerPx": "",
 "tradeNum": "9",
 "triggerParams": [{
 "triggerAction": "start",
 "delaySeconds": "0",
 "triggerStrategy": "price",
 "triggerPx": "1",
 "triggerType": "manual",
 "triggerTime": "1682418561497"
 }, {
 "triggerAction": "stop",
 "delaySeconds": "0",
 "triggerStrategy": "instant",
 "stopType": "1",
 "triggerType": "manual",
 "triggerTime": "0"
 }],
 "uTime": "1682492552257",
 "profitSharingRatio": "",
 "copyType": "0",
 "tpRatio": "",
 "slRatio": "",
 "fee": "",
 "fundingFee": ""
 }]
}

```

#### Response parameters when data is pushed.

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instType | String | Instrument type |
| > uid | String | User ID |
| data | Array of objects | Subscribed data |
| > algoId | String | Algo ID |
| > algoClOrdId | String | Client-supplied Algo ID |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > algoOrdType | String | Algo order type`contract_grid`: Contract grid |
| > state | String | Algo order state`starting``running``stopping``no_close_position`: stopped algo order but hadn't close position yet`stopped` |
| > rebateTrans | Array of objects | Rebate transfer info |
| >> rebate | String | Rebate amount |
| >> rebateCcy | String | Rebate currency |
| > triggerParams | Array of objects | Trigger Parameters |
| >> triggerAction | String | Trigger action`start``stop` |
| >> triggerStrategy | String | Trigger strategy`instant``price``rsi` |
| >> delaySeconds | String | Delay seconds after action triggered |
| >> triggerTime | String | Actual action triggered time, unix timestamp format in milliseconds, e.g. `1597026383085` |
| >> triggerType | String | Actual action triggered type`manual``auto` |
| >> timeframe | String | K-line type`3m`, `5m`, `15m`, `30m` (`m`: minute)`1H`, `4H` (`H`: hour)`1D` (`D`: day)This field is only valid when `triggerStrategy` is `rsi` |
| >> thold | String | ThresholdThe value should be an integer between 1 to 100This field is only valid when `triggerStrategy` is `rsi` |
| >> triggerCond | String | Trigger condition`cross_up``cross_down``above``below``cross`This field is only valid when `triggerStrategy` is `rsi` |
| >> timePeriod | String | Time Period`14`This field is only valid when `triggerStrategy` is `rsi` |
| >> triggerPx | String | Trigger PriceThis field is only valid when `triggerStrategy` is `price` |
| >> stopType | String | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positionsThis field is only valid when `triggerAction` is `stop` |
| > maxPx | String | Upper price of price range |
| > minPx | String | Lower price of price range |
| > gridNum | String | Grid quantity |
| > runType | String | Grid type`1`: Arithmetic, `2`: Geometric |
| > tpTriggerPx | String | Take-profit trigger price |
| > slTriggerPx | String | Stop-loss trigger price |
| > tradeNum | String | The number of trades executed |
| > arbitrageNum | String | The number of arbitrages executed |
| > singleAmt | String | Amount per grid |
| > perMinProfitRate | String | Estimated minimum Profit margin per grid |
| > perMaxProfitRate | String | Estimated maximum Profit margin per grid |
| > runPx | String | Price at launch |
| > totalPnl | String | Total P&L |
| > pnlRatio | String | P&L ratio |
| > investment | String | Accumulated investment amountSpot grid investment amount calculated on quote currency |
| > gridProfit | String | Grid profit |
| > floatProfit | String | Variable P&L |
| > totalAnnualizedRate | String | Total annualized rate |
| > annualizedRate | String | Grid annualized rate |
| > cancelType | String | Algo order stop reason`0`: None`1`: Manual stop`2`: Take profit`3`: Stop loss`4`: Risk control`5`: Delivery`6`: Signal |
| > stopType | String | Stop typeSpot grid `1`: Sell base currency `2`: Keep base currencyContract grid `1`: Market Close All positions `2`: Keep positions |
| > direction | String | Contract grid type`long`,`short`,`neutral`Only applicable to `contract grid` |
| > basePos | Boolean | Whether or not to open a position when the strategy is activatedOnly applicable to `contract grid` |
| > sz | String | Used margin based on `USDT`Only applicable to `contract grid` |
| > lever | String | LeverageOnly applicable to `contract grid` |
| > actualLever | String | Actual LeverageOnly applicable to `contract grid` |
| > liqPx | String | Estimated liquidation priceOnly applicable to `contract grid` |
| > ordFrozen | String | Margin used by pending ordersOnly applicable to `contract grid` |
| > availEq | String | Available marginOnly applicable to `contract grid` |
| > eq | String | Total equity of strategy accountOnly applicable to `contract grid` |
| > activeOrdNum | String | Total count of pending sub orders |
| > tag | String | Order tag |
| > profitSharingRatio | String | Profit sharing ratioValue range [0, 0.3]If it is a normal order (neither copy order nor lead order), this field returns "" |
| > copyType | String | Profit sharing order type`0`: Normal order`1`: Copy order without profit sharing`2`: Copy order with profit sharing`3`: Lead order |
| > tpRatio | String | Take profit ratio, 0.1 represents 10% |
| > slRatio | String | Stop loss ratio, 0.1 represents 10% |
| > fee | String | Accumulated fee. Only applicable to contract grid, or it will be "" |
| > fundingFee | String | Accumulated funding fee. Only applicable to contract grid, or it will be "" |
| > pTime | String | Push time of algo grid information, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### WS / Grid positions channel

Retrieve contract grid positions. Data will be pushed when triggered by events such as placing/canceling order.

Please ignore the empty data.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "grid-positions",
 "algoId": "449327675342323712"
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
 "channel": "grid-positions",
 "algoId": "449327675342323712"
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
| > channel | String | Yes | Channel name`grid-positions` |
| > algoId | String | Yes | Algo Order ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "grid-positions",
 "algoId": "449327675342323712"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-positions\", \"instType\" : \"FUTURES\"}]}",
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
| > algoId | String | Yes | Algo Order ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example:

```
{
 "arg": {
 "channel": "grid-positions",
 "uid": "4470****9584",
 "algoId": "449327675342323712"
 },
 "data": [{
 "adl": "1",
 "algoClOrdId": "",
 "algoId": "449327675342323712",
 "avgPx": "29181.4638888888888895",
 "cTime": "1653400065917",
 "ccy": "USDT",
 "imr": "2089.2690000000002",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "last": "29852.7",
 "lever": "5",
 "liqPx": "604.7617536513744",
 "markPx": "29849.7",
 "mgnMode": "cross",
 "mgnRatio": "217.71740878394456",
 "mmr": "41.78538",
 "notionalUsd": "10435.794191550001",
 "pTime": "1653536068723",
 "pos": "35",
 "posSide": "net",
 "uTime": "1653445498682",
 "upl": "232.83263888888962",
 "uplRatio": "0.1139826489932205"
 }]
}

```

#### Response parameters when data is pushed.

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > algoId | String | Algo Order ID |
| data | Array of objects | Subscribed data |
| > algoId | String | Algo ID |
| > algoClOrdId | String | Client-supplied Algo ID |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > avgPx | String | Average open price |
| > ccy | String | Margin currency |
| > lever | String | Leverage |
| > liqPx | String | Estimated liquidation price |
| > posSide | String | Position side`net` |
| > pos | String | Quantity of positions |
| > mgnMode | String | Margin mode`cross``isolated` |
| > mgnRatio | String | Maintenance margin ratio |
| > imr | String | Initial margin requirement |
| > mmr | String | Maintenance margin requirement |
| > upl | String | Unrealized profit and loss |
| > uplRatio | String | Unrealized profit and loss ratio |
| > last | String | Latest traded price |
| > notionalUsd | String | Notional value of positions in `USD` |
| > adl | String | Automatic-Deleveraging, signal areaDivided into 5 levels, from 1 to 5, the smaller the number, the weaker the adl intensity. |
| > markPx | String | Mark price |
| > pTime | String | Push time of positions information, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### WS / Grid sub orders channel

Retrieve grid sub orders. Data will be pushed when triggered by events such as placing order.

Please ignore the empty data.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "grid-sub-orders",
 "algoId": "449327675342323712"
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
 "channel": "grid-sub-orders",
 "algoId": "449327675342323712"
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
| > channel | String | Yes | Channel name`grid-sub-orders` |
| > algoId | String | Yes | Algo Order ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "grid-sub-orders",
 "algoId": "449327675342323712"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"grid-sub-orders\", \"instType\" : \"FUTURES\"}]}",
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
| > algoId | String | Yes | Algo Order ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example:

```
{
 "arg": {
 "channel": "grid-sub-orders",
 "uid": "44705892343619584",
 "algoId": "449327675342323712"
 },
 "data": [{
 "accFillSz": "0",
 "algoClOrdId": "",
 "algoId": "449327675342323712",
 "algoOrdType": "contract_grid",
 "avgPx": "0",
 "cTime": "1653445498664",
 "ctVal": "0.01",
 "fee": "0",
 "feeCcy": "USDT",
 "groupId": "-1",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "lever": "5",
 "ordId": "449518234142904321",
 "ordType": "limit",
 "pTime": "1653486524502",
 "pnl": "",
 "posSide": "net",
 "px": "28007.2",
 "rebate": "0",
 "rebateCcy": "USDT",
 "side": "buy",
 "state": "live",
 "sz": "1",
 "tag":"",
 "tdMode": "cross",
 "uTime": "1653445498674"
 }]
}

```

#### Response parameters when data is pushed.

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > algoId | String | Algo Order ID |
| data | Array of objects | Subscribed data |
| > algoId | String | Algo ID |
| > algoClOrdId | String | Client-supplied Algo ID |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > algoOrdType | String | Algo order type`grid`: Spot grid`contract_grid`: Contract grid |
| > groupId | String | Group ID |
| > ordId | String | Sub order ID |
| > cTime | String | Sub order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > uTime | String | Sub order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > tdMode | String | Sub order trade modeMargin mode `cross` `isolated`Non-Margin mode `cash` |
| > tag | String | Order tag |
| > ordType | String | Sub order type`market`: Market order`limit`: Limit order`ioc`: Immediate-or-cancel order |
| > sz | String | Sub order quantity to buy or sell |
| > state | String | Sub order state`canceled``live``partially_filled``filled``cancelling` |
| > side | String | Sub order side`buy` `sell` |
| > px | String | Sub order price |
| > fee | String | Sub order fee amount |
| > feeCcy | String | Sub order fee currency |
| > rebate | String | Sub order rebate amount |
| > rebateCcy | String | Sub order rebate currency |
| > avgPx | String | Sub order average filled price |
| > accFillSz | String | Sub order accumulated fill quantity |
| > posSide | String | Sub order position side`net` |
| > pnl | String | Sub order profit and loss |
| > ctVal | String | Contract valueOnly applicable to `FUTURES`/`SWAP`/`OPTION` |
| > lever | String | Leverage |
| > pTime | String | Push time of orders information, Unix timestamp format in milliseconds, e.g. `1597026383085` |
