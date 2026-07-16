## DCA Trading

A Martingale bot is a trading strategy that automatically adds to positions in batches as the market falls, thereby lowering the average holding cost. Users set the initial order amount, maximum number of safety orders, the price drop percentage that triggers each safety order, and the take-profit target. The bot will automatically place a buy order each time the price reaches a safety order condition, and close the position for profit once the price rebounds to the take-profit target.

The API endpoints of `DCA Trading` require authentication.

### POST / Place dca algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/create`

Request Example

```
POST /api/v5/tradingBot/dca/create
body
{
 "instId": "BTC-USDT",
 "algoOrdType": "contract_dca",
 "direction": "long",
 "lever": "2",
 "initOrdAmt": "50",
 "maxSafetyOrds": "0",
 "safetyOrdAmt": "10",
 "pxSteps": "0.01",
 "tpPct": "0.05",
 "triggerParams": [
 {
 "triggerAction": "start",
 "triggerStrategy": "rsi",
 "timeframe": "30m",
 "thold": "10",
 "triggerCond": "cross",
 "timePeriod": "14"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| initOrdAmt | String | Yes | Initial order amount |
| allowReinvest | String | No | Whether to reinvest profit. Only applicable to Contract DCA`true` or `false`, default is `true` |
| safetyOrdAmt | String | No | Safety order amountWhen `maxSafetyOrds` >= 1, `safetyOrdAmt` is required |
| maxSafetyOrds | String | Yes | Max number of safety orders |
| pxSteps | String | No | Safety order price stepWhen `maxSafetyOrds` >= 1, `pxSteps` is required |
| pxStepsMult | String | No | Price step multiplierWhen `maxSafetyOrds` >= 1, `pxStepsMult` is required |
| volMult | String | No | Safety order amount multiplierWhen `maxSafetyOrds` >= 1, `volMult` is required |
| tpPct | String | Yes | Take-profit target per cycle0.05 represents 5% |
| slPct | String | No | Stop-loss target0.05 represents 5% |
| slMode | String | No | Stop-loss mode`limit`: Limit order`market`: Market order |
| direction | String | No | Contract DCA type. Only applicable to `contract_dca``long`: Long position, `short`: Short position |
| lever | String | Yes | LeverageOnly applicable to `contract_dca` |
| triggerParams | Array of objects | Yes | Trigger parameters |
| > triggerAction | String | Yes | Trigger actionContract DCA: `start`: Start botSpot DCA: `start`: Start bot |
| > triggerStrategy | String | Yes | Trigger strategyContract DCA: `instant`: Instant trigger, `price`: Price trigger, `rsi`: RSI indicator trigger, default is `instant`Spot DCA: `instant`: Instant trigger, `rsi`: RSI indicator trigger, default is `instant` |
| > timeframe | String | No | K-line type`3m`, `5m`, `15m`, `30m` (m: minute)`1H`, `4H` (H: hour)`1D` (D: day)This field is only valid when `triggerStrategy` is `rsi` |
| > thold | String | No | ThresholdInteger between [1, 100]This field is only valid when `triggerStrategy` is `rsi` |
| > triggerCond | String | No | Trigger condition`cross_up`: Cross up`cross_down`: Cross down`above`: Above`below`: Below`cross`: CrossThis field is only valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | No | Time period`14`This field is only valid when `triggerStrategy` is `rsi` |
| > triggerPx | String | No | Trigger priceThis field is only valid when `triggerStrategy` is `price`Only applicable to `contract_dca` |
| profitSharingRatio | String | No | Lead trader profit sharing ratio. Only fixed profit sharing is supported. Only applicable to `contract_dca``0`, `0.1`, `0.2`, `0.3` |
| trackingMode | String | No | Tracking mode. Only applicable to `contract_dca``sync`: Synchronous, `async`: Asynchronous |
| tag | String | No | Order tag |
| algoClOrdId | String | No | Client-supplied Algo ID |
| tradeQuoteCcy | String | No | Quote currency for trading. Only applicable to `spot_dca` |

Response Example

```
{
 "code": "0",
 "data": [
 {
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
| tag | String | Order tag |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | The code of the event execution result, 0 means success |
| sMsg | String | Rejection message if the request is unsuccessful |

### POST / Amend spot dca basic param

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/amend-order-algo`

Request Example

```
POST /api/v5/tradingBot/dca/amend-order-algo
body
{
 "algoId": "532177187189760000",
 "pxSteps": "0.02",
 "pxStepsMult": "2.0",
 "volMult": "2.0",
 "tpPct": "0.05",
 "slPct": "0.20",
 "initOrdAmt": "100",
 "safetyOrdAmt": "50",
 "maxSafetyOrds": "5",
 "reserveFunds": true,
 "triggerParams": [
 {
 "triggerAction": "start",
 "triggerStrategy": "instant"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| pxSteps | String | Yes | Price step ratio (price gap to trigger the first safety order) |
| pxStepsMult | String | Yes | Price step multiplier |
| volMult | String | Yes | Amount multiplier |
| tpPct | String | Yes | Take-profit target, e.g. `0.05` represents 5% |
| slPct | String | Yes | Stop-loss target, e.g. `0.05` represents 5% |
| initOrdAmt | String | Yes | Initial order amount (in quote currency) |
| safetyOrdAmt | String | Yes | Safety order amount (in quote currency) |
| maxSafetyOrds | String | Yes | Maximum number of safety orders |
| reserveFunds | Boolean | Yes | Whether to reserve all funds`true`: reserve funds`false`: do not reserve funds |
| triggerParams | Array of objects | Yes | Signal trigger parameters |
| > triggerAction | String | No | Trigger action`start`: start the DCA bot |
| > triggerStrategy | String | No | Trigger strategy`instant`: trigger immediately`rsi`: RSI indicator trigger |
| > timeframe | String | No | Candlestick type`3m`, `5m`, `15m`, `30m` (`m` = minutes)`1H`, `4H` (`H` = hours)`1D` (`D` = days)Only valid when `triggerStrategy` is `rsi` |
| > thold | String | No | Threshold, integer in range [1, 100]Only valid when `triggerStrategy` is `rsi` |
| > triggerCond | String | No | Trigger condition`cross_up`: cross upward`cross_down`: cross downward`above`: above`below`: below`cross`: crossOnly valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | No | Period, e.g. `14`Only valid when `triggerStrategy` is `rsi` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "532177187189760000",
 "algoClOrdId": "",
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
| algoClOrdId | String | Client-supplied algo order ID |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### POST / Stop dca algo order

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/stop`

Request Example

```
POST /api/v5/tradingBot/dca/stop
body
{
 "algoOrdType": "contract_dca",
 "algoId": "448965992920907776",
 "stopType": "1"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| stopType | String | Yes | Stop type`contract_dca`: `1`: Market close all positions, `2`: Keep positions`spot_dca`: `1`: Sell base currency, `2`: Keep base currency |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "448965992920907776",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| tag | String | Order tag |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | The code of the event execution result, 0 means success |
| sMsg | String | Rejection message if the request is unsuccessful |

### GET / DCA algo order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/dca/ongoing-list`

Request Example

```
GET /api/v5/tradingBot/dca/ongoing-list?algoOrdType=contract_dca&limit=20
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| algoId | String | No | Algo ID |
| after | String | No | Pagination of data to return records earlier than the requested `algoId` |
| before | String | No | Pagination of data to return records newer than the requested `algoId` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "565849588675117056",
 "algoOrdType": "contract_dca",
 "instId": "BTC-USDT-SWAP",
 "copyType": "0",
 "state": "running",
 "direction": "long",
 "lever": "3",
 "initOrdAmt": "100",
 "safetyOrdAmt": "200",
 "maxSafetyOrds": "5",
 "pxSteps": "0.02",
 "pxStepsMult": "1",
 "volMult": "1",
 "tpPxRange": "",
 "slPct": "",
 "slMode": "",
 "allowReinvest": true,
 "totalPnl": "12.5",
 "pnlRatio": "0.05",
 "totalFundingFee": "-0.5",
 "investmentAmt": "500",
 "investmentCcy": "USDT",
 "arbitragePnL": "2.1",
 "profitSharingRatio": "",
 "trackingMode": "",
 "triggerParams": [
 {
 "triggerAction": "start",
 "triggerStrategy": "instant"
 }
 ],
 "cTime": "1597026383085",
 "uTime": "1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| copyType | String | Profit sharing order type`0`: Normal order`1`: Copy order without profit sharing`2`: Copy order with profit sharing`3`: Lead order |
| state | String | Algo order state`starting``running``stopping``pending_signal``no_close_position`: Stopped algo order but have not closed position yet |
| direction | String | Contract DCA: `long`: Long position, `short`: Short positionSpot DCA: `long`: Long position |
| lever | String | LeverageOnly applicable to `contract_dca` |
| initOrdAmt | String | Initial order amount |
| safetyOrdAmt | String | Safety order amount |
| maxSafetyOrds | String | Max number of safety orders |
| pxSteps | String | Safety order price step |
| pxStepsMult | String | Price step multiplier |
| volMult | String | Safety order amount multiplier |
| tpPxRange | String | Take-profit price limitFor Long DCA, the take-profit price must not be lower than the minimum threshold; for Short DCA, the take-profit price must not exceed the maximum thresholdOnly applicable to `contract_dca` |
| slPct | String | Stop-loss target, e.g. `0.05` represents 5% |
| slMode | String | Stop-loss mode`limit`: Limit order`market`: Market order |
| allowReinvest | Boolean | Whether to reinvest profit`true` or `false` |
| totalPnl | String | Total PnL |
| pnlRatio | String | PnL ratio |
| totalFundingFee | String | Total funding feeOnly applicable to `contract_dca` |
| investmentAmt | String | Total investment amount |
| investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC` |
| arbitragePnL | String | Arbitrage PnL |
| transferInMargin | String | Net transfer in margin, including margin and manually added investmentOnly applicable to `contract_dca` |
| profitSharingRatio | String | Profit sharing ratio, range [0, 0.3]Returns `""` for normal ordersOnly applicable to `contract_dca` |
| trackingMode | String | Tracking mode`sync`: Synchronous`async`: AsynchronousOnly applicable to `contract_dca` |
| triggerParams | Array of objects | Trigger parameters |
| > triggerAction | String | Trigger action`start`: Start bot`stop`: Stop bot |
| > triggerStrategy | String | Trigger strategyContract DCA: `instant`: Instant trigger, `price`: Price trigger, `rsi`: RSI indicator trigger, `webhook`: WebSocket signal triggerSpot DCA: `instant`: Instant trigger, `rsi`: RSI indicator trigger |
| > triggerPx | String | Trigger priceThis field is only valid when `triggerStrategy` is `price`Only applicable to `contract_dca` |
| > triggerCond | String | Trigger condition`cross_up`: Cross up`cross_down`: Cross down`above`: Above`below`: Below`cross`: CrossThis field is only valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | Time period, e.g. `14`This field is only valid when `triggerStrategy` is `rsi` |
| > thold | String | ThresholdInteger between [1, 100]This field is only valid when `triggerStrategy` is `rsi` |
| > timeframe | String | K-line type`3m`, `5m`, `15m`, `30m` (m: minute)`1H`, `4H` (H: hour)`1D` (D: day)This field is only valid when `triggerStrategy` is `rsi` |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| ctVal | String | Contract valueOnly applicable to `contract_dca` |
| tradeQuoteCcy | String | Quote currency for tradingOnly applicable to `spot_dca` |

### GET / DCA algo order history

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/dca/history-list`

Request Example

```
GET /api/v5/tradingBot/dca/history-list?algoOrdType=contract_dca
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| algoId | String | No | Algo ID |
| after | String | No | Pagination of data to return records earlier than the requested `algoId` |
| before | String | No | Pagination of data to return records newer than the requested `algoId` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "12345689",
 "algoOrdType": "contract_dca",
 "instId": "BTC-USDT-SWAP",
 "copyType": "0",
 "state": "stopped",
 "cancelType": "1",
 "direction": "long",
 "lever": "3",
 "initOrdAmt": "100",
 "safetyOrdAmt": "200",
 "maxSafetyOrds": "5",
 "pxSteps": "0.02",
 "pxStepsMult": "1",
 "volMult": "1",
 "slPct": "",
 "slMode": "",
 "allowReinvest": true,
 "totalPnl": "12.5",
 "pnlRatio": "0.05",
 "fundingFee": "-0.5",
 "investmentAmt": "500",
 "investmentCcy": "USDT",
 "arbitragePnL": "2.1",
 "transferInMargin": "500",
 "profitSharingRatio": "",
 "trackingMode": "",
 "triggerParams": [
 {
 "triggerAction": "start",
 "triggerStrategy": "instant"
 }
 ],
 "ctVal": "0.01",
 "cTime": "1597026383085",
 "uTime": "1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| copyType | String | Profit sharing order type`0`: Normal order`1`: Copy order without profit sharing`2`: Copy order with profit sharing`3`: Lead order |
| state | String | Algo order state`starting``running``stopping``pending_signal``no_close_position`: Stopped algo order but have not closed position yet |
| cancelType | String | Algo order stop reason`0`: None`1`: Manual stop`2`: Take profit`3`: Stop loss`4`: Risk control`5`: Delivery |
| direction | String | Contract DCA: `long`: Long position, `short`: Short positionSpot DCA: `long`: Long position |
| lever | String | LeverageOnly applicable to `contract_dca` |
| initOrdAmt | String | Initial order amount |
| safetyOrdAmt | String | Safety order amount |
| maxSafetyOrds | String | Max number of safety orders |
| pxSteps | String | Safety order price step |
| pxStepsMult | String | Price step multiplier |
| volMult | String | Safety order amount multiplier |
| slPct | String | Stop-loss target, e.g. `0.05` represents 5% |
| slMode | String | Stop-loss mode`limit`: Limit order`market`: Market order |
| allowReinvest | Boolean | Whether to reinvest profit`true` or `false` |
| totalPnl | String | Total PnL |
| pnlRatio | String | PnL ratio |
| fundingFee | String | Total funding feeOnly applicable to `contract_dca` |
| investmentAmt | String | Total investment amount |
| investmentCcy | String | The invested quantity unit, can only be `USDT`/`USDC` |
| arbitragePnL | String | Arbitrage PnL |
| transferInMargin | String | Net transfer in margin, including margin and manually added investmentOnly applicable to `contract_dca` |
| profitSharingRatio | String | Profit sharing ratio, range [0, 0.3]Returns `""` for normal ordersOnly applicable to `contract_dca` |
| trackingMode | String | Tracking mode`sync`: Synchronous`async`: AsynchronousOnly applicable to `contract_dca` |
| triggerParams | Array of objects | Trigger parameters |
| > triggerAction | String | Trigger action`start`: Start bot`stop`: Stop bot |
| > triggerStrategy | String | Trigger strategyContract DCA: `instant`: Instant trigger, `price`: Price trigger, `rsi`: RSI indicator trigger, `webhook`: WebSocket signal triggerSpot DCA: `instant`: Instant trigger, `rsi`: RSI indicator trigger |
| > triggerPx | String | Trigger priceThis field is only valid when `triggerStrategy` is `price`Only applicable to `contract_dca` |
| > triggerCond | String | Trigger condition`cross_up`: Cross up`cross_down`: Cross down`above`: Above`below`: Below`cross`: CrossThis field is only valid when `triggerStrategy` is `rsi` |
| > timePeriod | String | Time period, e.g. `14`This field is only valid when `triggerStrategy` is `rsi` |
| > thold | String | ThresholdInteger between [1, 100]This field is only valid when `triggerStrategy` is `rsi` |
| > timeframe | String | K-line type`3m`, `5m`, `15m`, `30m` (m: minute)`1H`, `4H` (H: hour)`1D` (D: day)This field is only valid when `triggerStrategy` is `rsi` |
| ctVal | String | Contract valueOnly applicable to `contract_dca` |
| cTime | String | Algo order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Algo order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| tradeQuoteCcy | String | Quote currency for tradingOnly applicable to `spot_dca` |

### GET / DCA sub orders

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/dca/orders`

Request Example

```
GET /api/v5/tradingBot/dca/orders?algoId=2833925189933756416&algoOrdType=contract_dca
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| cycleId | String | No | Cycle ID |
| after | String | No | Pagination of data to return records earlier than the requested `ordId` |
| before | String | No | Pagination of data to return records newer than the requested `ordId` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "cycleId": "9876543",
 "ordId": "570627699870375936",
 "avgFillPx": "41500",
 "direction": "long",
 "side": "buy",
 "ordType": "init_order",
 "px": "41000",
 "sz": "10",
 "filledSz": "10",
 "state": "filled",
 "fee": "-0.2",
 "rebate": "0",
 "rebateCcy": "USDT",
 "lever": "3",
 "instId": "BTC-USDT-SWAP",
 "ctVal": "0.01",
 "fillTime": "1597026383085",
 "cTime": "1597026383085",
 "uTime": "1597026383085",
 "tradeQuoteCcy": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| cycleId | String | Cycle ID |
| ordId | String | Sub order ID |
| avgFillPx | String | Average filled price |
| direction | String | Position directionContract DCA: `long`: Long position, `short`: Short positionSpot DCA: `long`: Long position |
| side | String | Order side`buy``sell` |
| ordType | String | Sub order type`init_order`: Initial order`safety_order`: Safety order`tp_order`: Take-profit order`sl_order`: Stop-loss order`manual_add_order`: Manually added order`close_position`: Close position order`manual_close_position`: Manual close position order |
| px | String | Order price |
| sz | String | Order size |
| filledSz | String | Filled size |
| state | String | Order status`live`: Pending fill`partially_filled`: Partially filled`filled`: Fully filled`canceled`: Canceled`cancelling`: Cancelling |
| fee | String | Accumulated feeNegative number represents the user transaction fee charged by the platform. Positive number represents rebate. |
| rebate | String | Rebate amount |
| rebateCcy | String | Rebate currency |
| lever | String | LeverageOnly applicable to `contract_dca` |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| ctVal | String | Contract valueOnly applicable to `contract_dca` |
| fillTime | String | Last filled time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Order created time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| tradeQuoteCcy | String | Quote currency for tradingOnly applicable to `spot_dca` |

### POST / Add investment

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/orders/manual-buy`

Request Example

```
POST /api/v5/tradingBot/dca/orders/manual-buy
body
{
 "algoId": "2833925189933756416",
 "algoOrdType": "contract_dca",
 "price": "41000",
 "amt": "100"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| price | String | Yes | Manual added order limit price |
| amt | String | Yes | Amount |
| ordType | String | No | Order type`limit`: Limit order`market`: Market orderOnly applicable to `spot_dca` |
| tradeQuoteCcy | String | No | Quote currency for tradingOnly applicable to `spot_dca` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2833925189933756416",
 "algoClOrdId": "",
 "algoOrdType": "contract_dca",
 "tag": "",
 "diffAmount": "100",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| tag | String | Order tag |
| diffAmount | String | Extra amount transferred from trading accountOnly applicable to `contract_dca` |
| sCode | String | The code of the event execution result, 0 means success |
| sMsg | String | Rejection message if the request is unsuccessful |

### POST / Amend dca reinvestment

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/settings/reinvestment`

Request Example

```
POST /api/v5/tradingBot/dca/settings/reinvestment
body
{
 "algoId": "2833925189933756416",
 "algoOrdType": "contract_dca",
 "allowReinvest": true
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order |
| allowReinvest | Boolean | Yes | Whether to reinvest profit`true` or `false` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2833925189933756416",
 "algoOrdType": "contract_dca",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order |
| sCode | String | The code of the event execution result, 0 means success |
| sMsg | String | Rejection message if the request is unsuccessful |

### POST / Amend dca take profit settings

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/settings/take-profit`

Request Example

```
POST /api/v5/tradingBot/dca/settings/take-profit
body
{
 "algoId": "2833925189933756416",
 "algoOrdType": "contract_dca",
 "tpPrice": "43500"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order |
| tpPrice | String | Yes | Take-profit price |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2833925189933756416",
 "algoOrdType": "contract_dca",
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
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### Get / DCA algo order position details

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/dca/position-details`

Request Example

```
GET /api/v5/tradingBot/dca/position-details?algoId=2833925189933756416&algoOrdType=contract_dca
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2833925189933756416",
 "algoClOrdId": "",
 "algoOrdType": "contract_dca",
 "instId": "BTC-USDT-SWAP",
 "curCycleld": "3",
 "startTime": "1597026383085",
 "fillManualOrds": "0",
 "fillSafetyOrds": "2",
 "fundingFee": "-0.05",
 "initPx": "43200",
 "notionalUsd": "5000",
 "avgPx": "43000",
 "upl": "12.5",
 "liqPx": "38000",
 "sz": "2",
 "baseSz": "",
 "quoteSz": "",
 "slPx": "40000",
 "tpPx": "45000",
 "fee": "-0.2",
 "tradeQuoteCcy": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo order ID |
| algoClOrdId | String | Client-supplied algo order ID |
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| curCycleld | String | The cycle ID for the current cycle |
| startTime | String | Start time of the current cycle, Unix timestamp in milliseconds, e.g. `1597026383085` |
| fillManualOrds | String | Number of filled manually added orders in the current cycle |
| fillSafetyOrds | String | Number of filled safety orders in the current cycle |
| fundingFee | String | Accumulated funding fee for the current cycleOnly applicable to `contract_dca` |
| initPx | String | Initial order average open price |
| notionalUsd | String | Notional value of positions in USDOnly applicable to `contract_dca` |
| avgPx | String | Average open price |
| upl | String | Unrealized PnL |
| liqPx | String | Estimated liquidation priceOnly applicable to `contract_dca` |
| sz | String | Position size in number of contractsOnly applicable to `contract_dca` |
| baseSz | String | Amount of base currency held in the current cycleOnly applicable to `spot_dca` |
| quoteSz | String | Amount of quote currency held in the current cycleOnly applicable to `spot_dca` |
| slPx | String | Stop-loss price |
| tpPx | String | Take-profit price |
| fee | String | Accumulated fee. Negative number represents the transaction fee charged by the platform. Positive number represents rebate. |
| tradeQuoteCcy | String | The quote currency for tradingOnly applicable to `spot_dca` |

### GET / DCA cycle list

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`GET /api/v5/tradingBot/dca/cycle-list`

Request Example

```
GET /api/v5/tradingBot/dca/cycle-list?algoId=2833925189933756416&algoOrdType=contract_dca
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo ID |
| algoOrdType | String | Yes | Algo order type`contract_dca`: Contract DCA order`spot_dca`: Spot DCA order |
| instId | String | No | Instrument ID |
| after | String | No | Pagination of data to return records earlier than the requested `cycleId` |
| before | String | No | Pagination of data to return records newer than the requested `cycleId` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2833925189933756416",
 "algoClOrdId": "",
 "cycleId": "9876543",
 "currentCycle": true,
 "realizedPnl": "12.5",
 "startTime": "1597026383085",
 "endTime": "",
 "fee": "-0.3",
 "avgPx": "41500",
 "tpPx": "43000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| algoId | String | Algo ID |
| algoClOrdId | String | Client-supplied Algo ID |
| cycleId | String | Cycle ID |
| currentCycle | Boolean | Whether it is the current cycle`true` or `false` |
| realizedPnl | String | Realized PnL |
| startTime | String | Cycle start time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| endTime | String | Cycle end time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| fee | String | Accumulated fee in the cycleNegative number represents the user transaction fee charged by the platform. Positive number represents rebate. |
| avgPx | String | Average open price |
| tpPx | String | Take-profit price |

### POST / Add dca margin

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/margin/add`

Request Example

```
POST /api/v5/tradingBot/dca/margin/add
body
{
 "algoId": "2833925189933756416",
 "amt": "50"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| amt | String | Yes | Margin add amount |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2833925189933756416",
 "algoOrdType": "contract_dca",
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
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |

### POST / Reduce dca margin

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit Rule: User ID

#### HTTP Request

`POST /api/v5/tradingBot/dca/margin/reduce`

Request Example

```
POST /api/v5/tradingBot/dca/margin/reduce
body
{
 "algoId": "2833925189933756416",
 "amt": "50"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Yes | Algo order ID |
| amt | String | Yes | Margin reduction amount |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "algoId": "2833925189933756416",
 "algoOrdType": "contract_dca",
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
| algoOrdType | String | Algo order type`contract_dca`: Contract DCA order |
| sCode | String | Event execution status code, `0` indicates success |
| sMsg | String | Error message if the event execution failed |
