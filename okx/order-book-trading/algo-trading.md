## Algo Trading

### POST / Place algo order

The algo order includes `trigger` order, `oco` order, `chase` order, `conditional` order, `twap` order and trailing order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 1 request per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/order-algo`

**Request Example

```
# Place Take Profit / Stop Loss Order
POST /api/v5/trade/order-algo
body
{
 "instId":"BTC-USDT",
 "tdMode":"cross",
 "side":"buy",
 "ordType":"conditional",
 "sz":"2",
 "tpTriggerPx":"15",
 "tpOrdPx":"18"
}

# Place Trigger Order
POST /api/v5/trade/order-algo
body
{
 "instId": "BTC-USDT-SWAP",
 "side": "buy",
 "tdMode": "cross",
 "posSide": "net",
 "sz": "1",
 "ordType": "trigger",
 "triggerPx": "25920",
 "triggerPxType": "last",
 "orderPx": "-1",
 "attachAlgoOrds": [{
 "attachAlgoClOrdId": "",
 "slTriggerPx": "100",
 "slOrdPx": "600",
 "tpTriggerPx": "25921",
 "tpOrdPx": "2001"
 }]
}

# Place Trailing Stop Order
POST /api/v5/trade/order-algo
body
{
 "instId": "BTC-USDT-SWAP",
 "tdMode": "cross",
 "side": "buy",
 "ordType": "move_order_stop",
 "sz": "10",
 "posSide": "net",
 "callbackRatio": "0.05",
 "reduceOnly": true
}

# Place TWAP Order
POST /api/v5/trade/order-algo
body
{
 "instId": "BTC-USDT-SWAP",
 "tdMode": "cross",
 "side": "buy",
 "ordType": "twap",
 "sz": "10",
 "posSide": "net",
 "szLimit": "10",
 "pxLimit": "100",
 "timeInterval": "10",
 "pxSpread": "10"
}
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# One-way stop order
result = tradeAPI.place_algo_order(
 instId="BTC-USDT",
 tdMode="cross",
 side="buy",
 ordType="conditional",
 sz="2",
 tpTriggerPx="15",
 tpOrdPx="18"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| tdMode | String | Yes | Trade modeMargin mode `cross` `isolated`Non-Margin mode `cash``spot_isolated` (only applicable to SPOT lead trading)Note: `isolated` is not available in multi-currency margin mode and portfolio margin mode. |
| ccy | String | No | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`. |
| side | String | Yes | Order side, `buy` `sell` |
| posSide | String | Conditional | Position side Required in `long/short` mode and only be `long` or `short` |
| ordType | String | Yes | Order type `conditional`: One-way stop order`oco`: One-cancels-the-other order`chase`: chase order, only applicable to FUTURES and SWAP`trigger`: Trigger order`move_order_stop`: Trailing order`twap`: TWAP order |
| sz | String | Conditional | Quantity to buy or sellEither `sz` or `closeFraction` is required. |
| tag | String | No | Order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| tgtCcy | String | No | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` traded with Market buy `conditional` orderDefault is `quote_ccy` for buy, `base_ccy` for sell |
| algoClOrdId | String | No | Client-supplied Algo IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| closeFraction | String | Conditional | Fraction of position to be closed when the algo order is triggered. Currently the system supports fully closing the position only so the only accepted value is `1`. For the same position, only one TPSL pending order for fully closing the position is supported. This is only applicable to `FUTURES` or `SWAP` instruments.If `posSide` is `net`, `reduceOnly` must be `true`.This is only applicable if `ordType` is `conditional` or `oco`.This is only applicable if the stop loss and take profit order is executed as market order.This is not supported in Portfolio Margin mode.Either `sz` or `closeFraction` is required. |
| tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`. The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`. |

Take Profit / Stop Loss Order**

Predefine the price you want the order to trigger a market order to execute immediately or it will place a limit order. **This type of order will not freeze your free margin in advance.

learn more about [Take Profit / Stop Loss Order](/help/11015447687437)

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| tpTriggerPx | String | No | Take-profit trigger priceIf you fill in this parameter, you should fill in the take-profit order price as well. |
| tpTriggerPxType | String | No | Take-profit trigger price type`last`: last price`index`: index price`mark`: mark price The default is `last` |
| tpOrdPx | String | No | Take-profit order price For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well.For limit TP order, you need to fill in this parameter, but the take-profit trigger price doesn’t need to be filled. If the price is `-1`, take-profit will be executed at the market price. |
| tpOrdKind | String | No | TP order kind`condition``limit` The default is `condition` |
| slTriggerPx | String | No | Stop-loss trigger price If you fill in this parameter, you should fill in the stop-loss order price. |
| slTriggerPxType | String | No | Stop-loss trigger price type`last`: last price`index`: index price`mark`: mark price The default is `last` |
| slOrdPx | String | No | Stop-loss order price If you fill in this parameter, you should fill in the stop-loss trigger price. If the price is `-1`, stop-loss will be executed at the market price. |
| cxlOnClosePos | Boolean | No | Whether the TP/SL order placed by the user is associated with the corresponding position of the instrument. If it is associated, the TP/SL order will be canceled when the position is fully closed; if it is not, the TP/SL order will not be affected when the position is fully closed. Valid values: `true`: Place a TP/SL order associated with the position `false`: Place a TP/SL order that is not associated with the position The default value is `false`. If `true` is passed in, users must pass reduceOnly = true as well, indicating that when placing a TP/SL order associated with a position, it must be a reduceOnly order. Only applicable to `Futures mode` and `Multi-currency margin`. |
| reduceOnly | Boolean | No | Whether the order can only reduce the position size. Valid options: `true` or `false`. The default value is `false`. |

Take Profit / Stop Loss Order
When placing net TP/SL order (ordType=conditional) and both take-profit and stop-loss parameters are sent, only stop-loss logic will be performed and take-profit logic will be ignored.

Chase order**

It will place a Post Only order immediately and amend it continuously**Chase order and corresponding Post Only order can't be amended.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| chaseType | String | No | Chase type.`distance`: distance from best bid/ask price, the default value.`ratio`: ratio. |
| chaseVal | String | No | Chase value.It represents distance from best bid/ask price when `chaseType` is distance. For USDT-margined contract, the unit is USDT. For USDC-margined contract, the unit is USDC. For Crypto-margined contract, the unit is USD. It represents ratio when `chaseType` is ratio. 0.1 represents 10%. The default value is 0. |
| maxChaseType | String | Conditional | Maximum chase type.`distance`: maximum distance from best bid/ask price`ratio`: the ratio. maxChaseTyep and maxChaseVal need to be used together or none of them. |
| maxChaseVal | String | Conditional | Maximum chase value.It represents maximum distance when `maxChaseType` is distance.It represents ratio when `maxChaseType` is ratio. 0.1 represents 10%. |
| reduceOnly | Boolean | No | Whether the order can only reduce the position size. Valid options: `true` or `false`. The default value is `false`. |

Trigger Order**

Use a trigger order to place a market or limit order when a specific price level is crossed. **When a Trigger Order is triggered, if your account balance is lower than the order amount, the system will automatically place the order based on your current balance. Trigger orders do not freeze assets when placed. Only applicable to SPOT/FUTURES/SWAP

learn more about [Trigger Order](/help/11015447687437)

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| triggerPx | String | Yes | Trigger price |
| orderPx | String | Yes | Order Price If the price is `-1`, the order will be executed at the market price. |
| advanceOrdType | String | No | Trigger order type`fok`: Fill-or-kill order`ioc`: Immediate-or-cancel orderDefault is "", limit or market (controlled by orderPx) |
| triggerPxType | String | No | Trigger price type `last`: last price`index`: index price`mark`: mark price The default is `last` |
| attachAlgoOrds | Array of objects | No | Attached SL/TP orders infoApplicable to `Futures mode/Multi-currency margin/Portfolio margin` |
| > attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order attaching TP/SL.A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to algoClOrdId when placing TP/SL order once the general order is filled completely. |
| > tpTriggerPx | String | No | Take-profit trigger priceIf you fill in this parameter, you should fill in the take-profit order price as well. |
| > tpTriggerRatio | String | No | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `tpTriggerPx` and `tpTriggerRatio` can be passed If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be bewteen -1 and 0. |
| > tpTriggerPxType | String | No | Take-profit trigger price type`last`: last price`index`: index price`mark`: mark priceThe default is `last` |
| > tpOrdPx | String | No | Take-profit order priceIf you fill in this parameter, you should fill in the take-profit trigger price as well. If the price is `-1`, take-profit will be executed at the market price. |
| > slTriggerPx | String | No | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > slTriggerRatio | String | No | Stop profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `slTriggerPx` and `slTriggerRatio` can be passed If the main order is a buy order, it must be bewteen 0 and 1, and if the main order is a sell order, it must be greater than 0. |
| > slTriggerPxType | String | No | Stop-loss trigger price type`last`: last price`index`: index price`mark`: mark price The default is `last` |
| > slOrdPx | String | No | Stop-loss order price If you fill in this parameter, you should fill in the stop-loss trigger price. If the price is `-1`, stop-loss will be executed at the market price. |

Trailing Stop Order**

A trailing stop order is a stop order that tracks the market price. Its trigger price changes with the market price. Once the trigger price is reached, a market order is placed.**Actual trigger price for sell orders and short positions = Highest price after order placement – Trail variance (Var.), or Highest price after placement × (1 – Trail variance) (Ratio).
Actual trigger price for buy orders and long positions = Lowest price after order placement + Trail variance, or Lowest price after order placement × (1 + Trail variance).
You can use the activation price to set the activation condition for a trailing stop order.

learn more about [Trailing Stop Order](/help/11015447687437)

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| callbackRatio | String | Conditional | Callback price ratio, e.g. `0.01` represents `1%`Either `callbackRatio` or `callbackSpread` is allowed to be passed. |
| callbackSpread | String | Conditional | Callback price variance |
| activePx | String | No | Active priceThe system will only start tracking the market and calculating your trigger price after the activation price is reached. If you don’t set a price, your order will be activated as soon as it’s placed. |
| reduceOnly | Boolean | No | Whether the order can only reduce the position size. Valid options: `true` or `false`. The default value is `false`.This parameter is only valid in the `FUTRUES`/`SWAP` net mode, and is ignored in the long/short mode. |

TWAP Order**

Time-weighted average price (TWAP) strategy splits your order and places smaller orders at regular time intervals.**It is a strategy that will attempt to execute an order which trades in slices of order quantity at regular intervals of time as specified by users.

learn more about [TWAP Order](/help/xiii-time-weighted-average-price-twap)

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| pxVar | String | Conditional | Price variance by percentage, range between [0.0001 ~ 0.01], e.g. `0.01` represents `1%`Take buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range. This parameter determines the range by percentage.Either `pxVar` or `pxSpread` is allowed to be passed. |
| pxSpread | String | Conditional | Price variance by constant, should be no less then 0 (no upper limit)Take buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range. This parameter determines the range by constant. |
| szLimit | String | Yes | Average amountTake buy orders as an example. When the market price is lower than the limit price, a certain amount of buy orders will be placed above the best bid price within a certain range. This parameter determines the amount. |
| pxLimit | String | Yes | Price Limit, should be no less then 0 (no upper limit)Take buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range. This parameter represents the limit price. |
| timeInterval | String | Yes | Time interval in unit of `second`ake buy orders as an example. When the market price is lower than the limit price, small buy orders will be placed above the best bid price within a certain range based on the time cycle. This parameter represents the time cycle. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "order1234",
 "algoId": "1836487817828872192",
 "clOrdId": "",
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
| clOrdId | String | Client Order ID as assigned by the client(Deprecated) |
| algoClOrdId | String | Client-supplied Algo ID |
| sCode | String | The code of the event execution result, `0` means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |
| tag | String | Order tag |

### POST / Cancel algo order

Cancel unfilled algo orders. A maximum of 10 orders can be canceled per request. Request parameters should be passed in the form of an array.

#### Rate Limit: 20 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/cancel-algos`

Request Example

```
POST /api/v5/trade/cancel-algos
body
[
 {
 "algoId":"590919993110396111",
 "instId":"BTC-USDT"
 },
 {
 "algoId":"590920138287841222",
 "instId":"BTC-USDT"
 }
]
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Cancel unfilled algo orders (not including Iceberg order, TWAP order, Trailing Stop order)
algo_orders = [
 {"instId": "BTC-USDT", "algoId": "590919993110396111"},
 {"instId": "BTC-USDT", "algoId": "590920138287841222"}
]

result = tradeAPI.cancel_algo_order(algo_orders)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| algoId | String | Conditional | Algo IDEither `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used. |
| algoClOrdId | String | Conditional | Client-supplied Algo IDEither `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "algoClOrdId": "",
 "algoId": "1836489397437468672",
 "clOrdId": "",
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
| sCode | String | The code of the event execution result, `0` means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |
| clOrdId | String | Client Order ID as assigned by the client(Deprecated) |
| algoClOrdId | String | Client-supplied Algo ID(Deprecated) |
| tag | String | Order tag (Deprecated) |

### POST / Amend algo order

Amend unfilled algo orders (Support Stop order and Trigger order only, not including Move_order_stop order, Iceberg order, TWAP order, Trailing Stop order).

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID + Instrument ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/amend-algos`

Request Example

```
POST /api/v5/trade/amend-algos
body
{
 "algoId":"2510789768709120",
 "newSz":"2",
 "instId":"BTC-USDT"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID |
| algoId | String | Conditional | Algo IDEither `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used. |
| algoClOrdId | String | Conditional | Client-supplied Algo IDEither `algoId` or `algoClOrdId` is required. If both are passed, `algoId` will be used. |
| cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails Valid options: `false` or `true`, the default is `false`. |
| reqId | String | Conditional | Client Request ID as assigned by the client for order amendment A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. The response will include the corresponding `reqId` to help you identify the request if you provide it in the request. |
| newSz | String | Conditional | New quantity after amendment and it has to be larger than 0. |

Take Profit / Stop Loss Order**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| newTpTriggerPx | String | Conditional | Take-profit trigger price. Either the take-profit trigger price or order price is 0, it means that the take-profit is deleted |
| newTpOrdPx | String | Conditional | Take-profit order price If the price is -1, take-profit will be executed at the market price. |
| newSlTriggerPx | String | Conditional | Stop-loss trigger price.Either the stop-loss trigger price or order price is 0, it means that the stop-loss is deleted |
| newSlOrdPx | String | Conditional | Stop-loss order price If the price is -1, stop-loss will be executed at the market price. |
| newTpTriggerPxType | String | Conditional | Take-profit trigger price type`last`: last price `index`: index price `mark`: mark price |
| newSlTriggerPxType | String | Conditional | Stop-loss trigger price type`last`: last price `index`: index price `mark`: mark price |

**Trigger Order**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| newTriggerPx | String | Yes | New trigger price after amendment |
| newOrdPx | String | Yes | New order price after amendmentIf the price is `-1`, the order will be executed at the market price. |
| newTriggerPxType | String | No | New trigger price type after amendment `last`: last price`index`: index price`mark`: mark price The default is `last` |
| attachAlgoOrds | Array of objects | No | Attached SL/TP orders infoApplicable to `Futures mode/Multi-currency margin/Portfolio margin` |
| > newTpTriggerPx | String | No | Take-profit trigger priceIf you fill in this parameter, you should fill in the take-profit order price as well. |
| > newTpTriggerRatio | String | No | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `newTpTriggerPx` and `newTpTriggerRatio` can be passed If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be bewteen -1 and 0. 0 means to delete the take-profit. |
| > newTpTriggerPxType | String | No | Take-profit trigger price type`last`: last price`index`: index price`mark`: mark priceThe default is `last` |
| > newTpOrdPx | String | No | Take-profit order priceIf you fill in this parameter, you should fill in the take-profit trigger price as well. If the price is `-1`, take-profit will be executed at the market price. |
| > newSlTriggerPx | String | No | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > newSlTriggerRatio | String | No | Stop profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed If the main order is a buy order, it must be bewteen 0 and 1, and if the main order is a sell order, it must be greater than 0. 0 means to delete the stop-loss. |
| > newSlTriggerPxType | String | No | Stop-loss trigger price type`last`: last price`index`: index price`mark`: mark price The default is `last` |
| > newSlOrdPx | String | No | Stop-loss order price If you fill in this parameter, you should fill in the stop-loss trigger price. If the price is `-1`, stop-loss will be executed at the market price. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "algoClOrdId":"algo_01",
 "algoId":"2510789768709120",
 "reqId":"po103ux",
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
| reqId | String | Client Request ID as assigned by the client for order amendment. |
| sCode | String | The code of the event execution result, `0` means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |

### GET / Algo order details

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/order-algo`

Request Example

```
GET /api/v5/trade/order-algo?algoId=1753184812254216192
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| algoId | String | Conditional | Algo IDEither `algoId` or `algoClOrdId` is required.If both are passed, `algoId` will be used. |
| algoClOrdId | String | Conditional | Client-supplied Algo IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "activePx": "",
 "actualPx": "",
 "actualSide": "",
 "actualSz": "0",
 "algoClOrdId": "",
 "algoId": "1753184812254216192",
 "amendPxOnTriggerType": "0",
 "attachAlgoOrds": [],
 "cTime": "1724751378980",
 "callbackRatio": "",
 "callbackSpread": "",
 "ccy": "",
 "chaseType": "",
 "chaseVal": "",
 "clOrdId": "",
 "closeFraction": "",
 "failCode": "0",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "isTradeBorrowMode": "",
 "last": "62916.5",
 "lever": "",
 "linkedOrd": {
 "ordId": ""
 },
 "maxChaseType": "",
 "maxChaseVal": "",
 "moveTriggerPx": "",
 "ordId": "",
 "ordIdList": [],
 "ordPx": "",
 "ordType": "conditional",
 "posSide": "net",
 "pxLimit": "",
 "pxSpread": "",
 "pxVar": "",
 "quickMgnType": "",
 "reduceOnly": "false",
 "side": "buy",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "",
 "state": "live",
 "sz": "10",
 "szLimit": "",
 "tag": "",
 "tdMode": "cash",
 "tgtCcy": "quote_ccy",
 "timeInterval": "",
 "tpOrdPx": "-1",
 "tpTriggerPx": "10000",
 "tpTriggerPxType": "last",
 "triggerPx": "",
 "triggerPxType": "",
 "triggerTime": "",
 "tradeQuoteCcy": "USDT",
 "uTime": "1724751378980"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| ordId | String | Latest order ID. It will be deprecated soon |
| ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order. |
| algoId | String | Algo ID |
| clOrdId | String | Client Order ID as assigned by the client |
| sz | String | Quantity to buy or sell |
| closeFraction | String | Fraction of position to be closed when the algo order is triggered |
| ordType | String | Order type |
| side | String | Order side |
| posSide | String | Position side |
| tdMode | String | Trade mode |
| tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| state | String | State `live` `pause` `partially_effective``effective` `canceled` `order_failed``partially_failed` |
| lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| tpTriggerPx | String | Take-profit trigger price. |
| tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| tpOrdPx | String | Take-profit order price. |
| slTriggerPx | String | Stop-loss trigger price. |
| slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| slOrdPx | String | Stop-loss order price. |
| triggerPx | String | trigger price. |
| triggerPxType | String | trigger price type. `last`: last price`index`: index price`mark`: mark price |
| ordPx | String | Order price for the trigger order |
| advanceOrdType | String | Trigger order type`fok`: Fill-or-kill order`ioc`: Immediate-or-cancel orderDefault is "", limit or market (controlled by orderPx) |
| actualSz | String | Actual order quantity |
| actualPx | String | Actual order price |
| tag | String | Order tag |
| actualSide | String | Actual trigger side, `tp`: take profit `sl`: stop lossOnly applicable to oco order and conditional order |
| triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| pxVar | String | Price ratio Only applicable to `iceberg` order or `twap` order |
| pxSpread | String | Price variance Only applicable to `iceberg` order or `twap` order |
| szLimit | String | Average amount Only applicable to `iceberg` order or `twap` order |
| pxLimit | String | Price Limit Only applicable to `iceberg` order or `twap` order |
| timeInterval | String | Time interval Only applicable to `twap` order |
| callbackRatio | String | Callback price ratioOnly applicable to `move_order_stop` order |
| callbackSpread | String | Callback price varianceOnly applicable to `move_order_stop` order |
| activePx | String | Active priceOnly applicable to `move_order_stop` order |
| moveTriggerPx | String | Trigger priceOnly applicable to `move_order_stop` order |
| reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false. |
| quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` |
| last | String | Last filled price while placing |
| failCode | String | It represents that the reason that algo order fails to trigger. It is "" when the state is `effective`/`canceled`. There will be value when the state is `order_failed`, e.g. 51008;Only applicable to Stop Order, Trailing Stop Order, Trigger order. |
| algoClOrdId | String | Client-supplied Algo ID |
| amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| attachAlgoOrds | Array of objects | Attached SL/TP orders infoApplicable to `Futures mode/Multi-currency margin/Portfolio margin` |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order attaching TP/SL.A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to algoClOrdId when placing TP/SL order once the general order is filled completely. |
| > tpTriggerPx | String | Take-profit trigger priceIf you fill in this parameter, you should fill in the take-profit order price as well. |
| > tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > tpTriggerPxType | String | Take-profit trigger price type`last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order priceIf you fill in this parameter, you should fill in the take-profit trigger price as well. If the price is `-1`, take-profit will be executed at the market price. |
| > slTriggerPx | String | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > slTriggerRatio | String | Stop profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > slTriggerPxType | String | Stop-loss trigger price type`last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price If you fill in this parameter, you should fill in the stop-loss trigger price. If the price is `-1`, stop-loss will be executed at the market price. |
| linkedOrd | Object | Linked TP order detail, only applicable to SL order that comes from the one-cancels-the-other (OCO) order that contains the TP limit order. |
| > ordId | String | Order ID |
| cTime | String | Creation time Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| isTradeBorrowMode | String | Whether borrowing currency automatically true falseOnly applicable to `trigger order`, `trailing order` and `twap order` |
| chaseType | String | Chase type. Only applicable to `chase` order. |
| chaseVal | String | Chase value. Only applicable to `chase` order. |
| maxChaseType | String | Maximum chase type. Only applicable to `chase` order. |
| maxChaseVal | String | Maximum chase value. Only applicable to `chase` order. |
| tradeQuoteCcy | String | The quote currency used for trading. |

### GET / Algo order list

Retrieve a list of untriggered Algo orders under the current account.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-algo-pending`

Request Example

```
GET /api/v5/trade/orders-algo-pending?ordType=conditional
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Retrieve a list of untriggered one-way stop orders
result = tradeAPI.order_algos_list(
 ordType="conditional"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordType | String | Yes | Order type`conditional`: One-way stop order `oco`: One-cancels-the-other order `chase`: chase order, only applicable to FUTURES and SWAP`trigger`: Trigger order `move_order_stop`: Trailing order `iceberg`: Iceberg order `twap`: TWAP orderFor every request, unlike other ordType which only can use one type, `conditional` and `oco` both can be used and separated with comma. |
| algoId | String | No | Algo ID |
| instType | String | No | Instrument type`SPOT``SWAP``FUTURES``MARGIN` |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |
| after | String | No | Pagination of data to return records earlier than the requested `algoId`. |
| before | String | No | Pagination of data to return records newer than the requested `algoId`. |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "activePx": "",
 "actualPx": "",
 "actualSide": "",
 "actualSz": "0",
 "algoClOrdId": "",
 "algoId": "1753184812254216192",
 "amendPxOnTriggerType": "0",
 "attachAlgoOrds": [],
 "cTime": "1724751378980",
 "callbackRatio": "",
 "callbackSpread": "",
 "ccy": "",
 "chaseType": "",
 "chaseVal": "",
 "clOrdId": "",
 "closeFraction": "",
 "failCode": "0",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "isTradeBorrowMode": "",
 "last": "62916.5",
 "lever": "",
 "linkedOrd": {
 "ordId": ""
 },
 "maxChaseType": "",
 "maxChaseVal": "",
 "moveTriggerPx": "",
 "ordId": "",
 "ordIdList": [],
 "ordPx": "",
 "ordType": "conditional",
 "posSide": "net",
 "pxLimit": "",
 "pxSpread": "",
 "pxVar": "",
 "quickMgnType": "",
 "reduceOnly": "false",
 "side": "buy",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "",
 "state": "live",
 "sz": "10",
 "szLimit": "",
 "tag": "",
 "tdMode": "cash",
 "tgtCcy": "quote_ccy",
 "timeInterval": "",
 "tpOrdPx": "-1",
 "tpTriggerPx": "10000",
 "tpTriggerPxType": "last",
 "triggerPx": "",
 "triggerPxType": "",
 "triggerTime": "",
 "tradeQuoteCcy": "USDT",
 "uTime": "1724751378980"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| ordId | String | Latest order ID. It will be deprecated soon |
| ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order. |
| algoId | String | Algo ID |
| clOrdId | String | Client Order ID as assigned by the client |
| sz | String | Quantity to buy or sell |
| closeFraction | String | Fraction of position to be closed when the algo order is triggered |
| ordType | String | Order type |
| side | String | Order side |
| posSide | String | Position side |
| tdMode | String | Trade mode |
| tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` traded with Market order |
| state | String | State`live``pause` |
| lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| tpTriggerPx | String | Take-profit trigger price |
| tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| tpOrdPx | String | Take-profit order price |
| slTriggerPx | String | Stop-loss trigger price |
| slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| slOrdPx | String | Stop-loss order price |
| triggerPx | String | Trigger price |
| triggerPxType | String | Trigger price type. `last`: last price`index`: index price`mark`: mark price |
| ordPx | String | Order price for the trigger order |
| advanceOrdType | String | Trigger order type |
| actualSz | String | Actual order quantity |
| tag | String | Order tag |
| actualPx | String | Actual order price |
| actualSide | String | Actual trigger side`tp`: take profit `sl`: stop lossOnly applicable to oco order and conditional order |
| triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| pxVar | String | Price ratio Only applicable to `iceberg` order or `twap` order |
| pxSpread | String | Price variance Only applicable to `iceberg` order or `twap` order |
| szLimit | String | Average amount Only applicable to `iceberg` order or `twap` order |
| pxLimit | String | Price Limit Only applicable to `iceberg` order or `twap` order |
| timeInterval | String | Time interval Only applicable to `twap` order |
| callbackRatio | String | Callback price ratioOnly applicable to `move_order_stop` order |
| callbackSpread | String | Callback price varianceOnly applicable to `move_order_stop` order |
| activePx | String | Active priceOnly applicable to `move_order_stop` order |
| moveTriggerPx | String | Trigger priceOnly applicable to `move_order_stop` order |
| reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false. |
| quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` |
| last | String | Last filled price while placing |
| failCode | String | It represents that the reason that algo order fails to trigger. There will be value when the state is `order_failed`, e.g. 51008;For this endpoint, it always is "". |
| algoClOrdId | String | Client-supplied Algo ID |
| amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| attachAlgoOrds | Array of objects | Attached SL/TP orders infoApplicable to `Futures mode/Multi-currency margin/Portfolio margin` |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order attaching TP/SL.A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to algoClOrdId when placing TP/SL order once the general order is filled completely. |
| > tpTriggerPx | String | Take-profit trigger priceIf you fill in this parameter, you should fill in the take-profit order price as well. |
| > tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > tpTriggerPxType | String | Take-profit trigger price type`last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order priceIf you fill in this parameter, you should fill in the take-profit trigger price as well. If the price is `-1`, take-profit will be executed at the market price. |
| > slTriggerPx | String | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > slTriggerRatio | String | Stop profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > slTriggerPxType | String | Stop-loss trigger price type`last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price If you fill in this parameter, you should fill in the stop-loss trigger price. If the price is `-1`, stop-loss will be executed at the market price. |
| linkedOrd | Object | Linked TP order detail, only applicable to SL order that comes from the one-cancels-the-other (OCO) order that contains the TP limit order. |
| > ordId | String | Order ID |
| cTime | String | Creation time Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| isTradeBorrowMode | String | Whether borrowing currency automatically true falseOnly applicable to `trigger order`, `trailing order` and `twap order` |
| chaseType | String | Chase type. Only applicable to `chase` order. |
| chaseVal | String | Chase value. Only applicable to `chase` order. |
| maxChaseType | String | Maximum chase type. Only applicable to `chase` order. |
| maxChaseVal | String | Maximum chase value. Only applicable to `chase` order. |
| tradeQuoteCcy | String | The quote currency used for trading. |

### GET / Algo order history

Retrieve a list of all algo orders under the current account in the last 3 months.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-algo-history`

Request Example

```
GET /api/v5/trade/orders-algo-history?ordType=conditional&state=effective
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Retrieve a list of all one-way stop algo orders
result = tradeAPI.order_algos_history(
 state="effective",
 ordType="conditional"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordType | String | Yes | Order type `conditional`: One-way stop order `oco`: One-cancels-the-other order `chase`: chase order, only applicable to FUTURES and SWAP`trigger`: Trigger order `move_order_stop`: Trailing order `iceberg`: Iceberg order `twap`: TWAP order For every request, unlike other ordType which only can use one type, `conditional` and `oco` both can be used and separated with comma. |
| state | String | Conditional | State`effective``canceled``order_failed`Either `state` or `algoId` is required |
| algoId | String | Conditional | Algo ID Either `state` or `algoId` is required. |
| instType | String | No | Instrument type`SPOT``SWAP``FUTURES``MARGIN` |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |
| after | String | No | Pagination of data to return records earlier than the requested `algoId` |
| before | String | No | Pagination of data to return records new than the requested `algoId` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "activePx": "",
 "actualPx": "",
 "actualSide": "tp",
 "actualSz": "100",
 "algoClOrdId": "",
 "algoId": "1880721064716505088",
 "amendPxOnTriggerType": "0",
 "attachAlgoOrds": [],
 "cTime": "1728552255493",
 "callbackRatio": "",
 "callbackSpread": "",
 "ccy": "",
 "chaseType": "",
 "chaseVal": "",
 "clOrdId": "",
 "closeFraction": "1",
 "failCode": "1",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "isTradeBorrowMode": "",
 "last": "60777.5",
 "lever": "10",
 "linkedOrd": {
 "ordId": ""
 },
 "maxChaseType": "",
 "maxChaseVal": "",
 "moveTriggerPx": "",
 "ordId": "1884789786215137280",
 "ordIdList": [
 "1884789786215137280"
 ],
 "ordPx": "",
 "ordType": "oco",
 "posSide": "long",
 "pxLimit": "",
 "pxSpread": "",
 "pxVar": "",
 "quickMgnType": "",
 "reduceOnly": "true",
 "side": "sell",
 "slOrdPx": "-1",
 "slTriggerPx": "57000",
 "slTriggerPxType": "mark",
 "state": "effective",
 "sz": "100",
 "szLimit": "",
 "tag": "",
 "tdMode": "isolated",
 "tgtCcy": "",
 "timeInterval": "",
 "tpOrdPx": "-1",
 "tpTriggerPx": "63000",
 "tpTriggerPxType": "last",
 "triggerPx": "",
 "triggerPxType": "",
 "triggerTime": "1728673513447",
 "tradeQuoteCcy": "USDT",
 "uTime": "1728673513447"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| ordId | String | Latest order ID. It will be deprecated soon |
| ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order. |
| algoId | String | Algo ID |
| clOrdId | String | Client Order ID as assigned by the client |
| sz | String | Quantity to buy or sell |
| closeFraction | String | Fraction of position to be closed when the algo order is triggered |
| ordType | String | Order type |
| side | String | Order side |
| posSide | String | Position side |
| tdMode | String | Trade mode |
| tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| state | String | State `effective` `canceled` `order_failed` `partially_failed` |
| lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| tpTriggerPx | String | Take-profit trigger price. |
| tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| tpOrdPx | String | Take-profit order price. |
| slTriggerPx | String | Stop-loss trigger price. |
| slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| slOrdPx | String | Stop-loss order price. |
| triggerPx | String | trigger price. |
| triggerPxType | String | trigger price type. `last`: last price`index`: index price`mark`: mark price |
| ordPx | String | Order price for the trigger order |
| advanceOrdType | String | Trigger order type |
| actualSz | String | Actual order quantity |
| actualPx | String | Actual order price |
| tag | String | Order tag |
| actualSide | String | Actual trigger side, `tp`: take profit `sl`: stop lossOnly applicable to oco order and conditional order |
| triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| pxVar | String | Price ratio Only applicable to `iceberg` order or `twap` order |
| pxSpread | String | Price variance Only applicable to `iceberg` order or `twap` order |
| szLimit | String | Average amount Only applicable to `iceberg` order or `twap` order |
| pxLimit | String | Price Limit Only applicable to `iceberg` order or `twap` order |
| timeInterval | String | Time interval Only applicable to `twap` order |
| callbackRatio | String | Callback price ratioOnly applicable to `move_order_stop` order |
| callbackSpread | String | Callback price varianceOnly applicable to `move_order_stop` order |
| activePx | String | Active priceOnly applicable to `move_order_stop` order |
| moveTriggerPx | String | Trigger priceOnly applicable to `move_order_stop` order |
| reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false. |
| quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` |
| last | String | Last filled price while placing |
| failCode | String | It represents that the reason that algo order fails to trigger. It is "" when the state is `effective`/`canceled`. There will be value when the state is `order_failed`, e.g. 51008;Only applicable to Stop Order, Trailing Stop Order, Trigger order. |
| algoClOrdId | String | Client Algo Order ID as assigned by the client. |
| amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| attachAlgoOrds | Array of objects | Attached SL/TP orders infoApplicable to `Futures mode/Multi-currency margin/Portfolio margin` |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order attaching TP/SL.A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to algoClOrdId when placing TP/SL order once the general order is filled completely. |
| > tpTriggerPx | String | Take-profit trigger priceIf you fill in this parameter, you should fill in the take-profit order price as well. |
| > tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > tpTriggerPxType | String | Take-profit trigger price type`last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order priceIf you fill in this parameter, you should fill in the take-profit trigger price as well. If the price is `-1`, take-profit will be executed at the market price. |
| > slTriggerPx | String | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > slTriggerRatio | String | Stop profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > slTriggerPxType | String | Stop-loss trigger price type`last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price If you fill in this parameter, you should fill in the stop-loss trigger price. If the price is `-1`, stop-loss will be executed at the market price. |
| linkedOrd | Object | Linked TP order detail, only applicable to SL order that comes from the one-cancels-the-other (OCO) order that contains the TP limit order. |
| > ordId | String | Order ID |
| cTime | String | Creation time Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| isTradeBorrowMode | String | Whether borrowing currency automatically true falseOnly applicable to `trigger order`, `trailing order` and `twap order` |
| chaseType | String | Chase type. Only applicable to `chase` order. |
| chaseVal | String | Chase value. Only applicable to `chase` order. |
| maxChaseType | String | Maximum chase type. Only applicable to `chase` order. |
| maxChaseVal | String | Maximum chase value. Only applicable to `chase` order. |
| tradeQuoteCcy | String | The quote currency used for trading. |

### WS / Algo orders channel

Retrieve algo orders (includes `trigger` order, `oco` order, `conditional` order). Data will not be pushed when first subscribed. Data will only be pushed when there are order updates.

#### URL Path

/ws/v5/business (required login)

Request Example : single

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "orders-algo",
 "instType": "FUTURES",
 "instFamily": "BTC-USD",
 "instId": "BTC-USD-200329"
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
 "channel": "orders-algo",
 "instType": "FUTURES",
 "instFamily": "BTC-USD",
 "instId": "BTC-USD-200329"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "orders-algo",
 "instType": "FUTURES",
 "instFamily": "BTC-USD"
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
 "channel": "orders-algo",
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
| > channel | String | Yes | Channel name`orders-algo` |
| > instType | String | Yes | Instrument type `SPOT``MARGIN``SWAP``FUTURES` `ANY` |
| > instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > instId | String | No | Instrument ID |

Successful Response Example : single

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "orders-algo",
 "instType": "FUTURES",
 "instFamily": "BTC-USD",
 "instId": "BTC-USD-200329"
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
 "channel": "orders-algo",
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"orders-algo\", \"instType\" : \"FUTURES\"}]}",
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
| > instType | String | Yes | Instrument type `SPOT``MARGIN``SWAP``FUTURES` `ANY` |
| > instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example: single

```
{
 "arg": {
 "channel": "orders-algo",
 "uid": "77982378738415879",
 "instType": "FUTURES",
 "instId": "BTC-USD-200329"
 },
 "data": [{
 "actualPx": "0",
 "actualSide": "",
 "actualSz": "0",
 "algoClOrdId": "",
 "algoId": "581878926302093312",
 "attachAlgoOrds": [],
 "amendResult": "",
 "cTime": "1685002746818",
 "uTime": "1708679675245",
 "ccy": "",
 "clOrdId": "",
 "closeFraction": "",
 "failCode": "",
 "instId": "BTC-USDC",
 "instType": "SPOT",
 "last": "26174.8",
 "lever": "0",
 "notionalUsd": "11.0",
 "ordId": "",
 "ordIdList": [],
 "ordPx": "",
 "ordType": "conditional",
 "posSide": "",
 "quickMgnType": "",
 "reduceOnly": "false",
 "reqId": "",
 "side": "buy",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "",
 "state": "live",
 "sz": "11",
 "tag": "",
 "tdMode": "cross",
 "tgtCcy": "quote_ccy",
 "tpOrdPx": "-1",
 "tpTriggerPx": "1",
 "tpTriggerPxType": "last",
 "triggerPx": "",
 "triggerTime": "",
 "tradeQuoteCcy": "USDT",
 "amendPxOnTriggerType": "0",
 "linkedOrd":{
 "ordId":"98192973880283"
 },
 "isTradeBorrowMode": ""
 }]
}

```

#### Response parameters when data is pushed.

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > instType | String | Instrument type |
| > instFamily | String | Instrument family |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| > ordId | String | Latest order ID, the order ID associated with the algo order. It will be deprecated soon |
| > ordIdList | Array of strings | Order ID list. There will be multiple order IDs when there is TP/SL splitting order. |
| > algoId | String | Algo ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > sz | String | Quantity to buy or sell.`SPOT`/`MARGIN`: in the unit of currency.`FUTURES`/`SWAP`/`OPTION`: in the unit of contract. |
| > ordType | String | Order type`conditional`: One-way stop order `oco`: One-cancels-the-other order `trigger`: Trigger order `chase`: Chase order |
| > side | String | Order side`buy``sell` |
| > posSide | String | Position side `net``long` or `short`Only applicable to `FUTURES`/`SWAP` |
| > tdMode | String | Trade mode`cross`: cross`isolated`: isolated`cash`: cash |
| > tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency`quote_ccy`: Quote currencyOnly applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| > lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| > state | String | Order status `live`: to be effective `effective`: effective `canceled`: canceled `order_failed`: order failed`partially_failed`: partially failed`partially_effective`: partially effective |
| > tpTriggerPx | String | Take-profit trigger price. |
| > tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order price. |
| > slTriggerPx | String | Stop-loss trigger price. |
| > slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price. |
| > triggerPx | String | Trigger price |
| > triggerPxType | String | Trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > ordPx | String | Order price for the trigger order |
| > advanceOrdType | String | Trigger order type |
| > last | String | Last filled price while placing |
| > actualSz | String | Actual order quantity |
| > actualPx | String | Actual order price |
| > notionalUsd | String | Estimated national value in `USD` of order |
| > tag | String | Order tag |
| > actualSide | String | Actual trigger sideOnly applicable to oco order and conditional order |
| > triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > reduceOnly | String | Whether the order can only reduce the position size. Valid options: `true` or `false`. |
| > failCode | String | It represents that the reason that algo order fails to trigger. It is "" when the state is `effective`/`canceled`. There will be value when the state is `order_failed`, e.g. 51008;Only applicable to Stop Order, Trailing Stop Order, Trigger order. |
| > algoClOrdId | String | Client Algo Order ID as assigned by the client. |
| > reqId | String | Client Request ID as assigned by the client for order amendment. "" will be returned if there is no order amendment. |
| > amendResult | String | The result of amending the order`-1`: failure `0`: success |
| > amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| > attachAlgoOrds | Array of objects | Attached SL/TP orders infoApplicable to `Futures mode/Multi-currency margin/Portfolio margin` |
| >> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order attaching TP/SL.A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to algoClOrdId when placing TP/SL order once the general order is filled completely. |
| >> tpTriggerPx | String | Take-profit trigger priceIf you fill in this parameter, you should fill in the take-profit order price as well. |
| >> tpTriggerRatio | String | Take-profit trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts. |
| >> tpTriggerPxType | String | Take-profit trigger price type`last`: last price`index`: index price`mark`: mark price |
| >> tpOrdPx | String | Take-profit order priceIf you fill in this parameter, you should fill in the take-profit trigger price as well. If the price is `-1`, take-profit will be executed at the market price. |
| >> slTriggerPx | String | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| >> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts. |
| >> slTriggerPxType | String | Stop-loss trigger price type`last`: last price`index`: index price`mark`: mark price |
| >> slOrdPx | String | Stop-loss order price If you fill in this parameter, you should fill in the stop-loss trigger price. If the price is `-1`, stop-loss will be executed at the market price. |
| > linkedOrd | Object | Linked TP order detail, only applicable to SL order that comes from the one-cancels-the-other (OCO) order that contains the TP limit order. |
| >> ordId | String | Order ID |
| > cTime | String | Creation time Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > uTime | String | Order updated time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| > isTradeBorrowMode | String | Whether borrowing currency automatically true falseOnly applicable to `trigger order`, `trailing order` and `twap order` |
| > chaseType | String | Chase type. Only applicable to `chase` order. |
| > chaseVal | String | Chase value. Only applicable to `chase` order. |
| > maxChaseType | String | Maximum chase type. Only applicable to `chase` order. |
| > maxChaseVal | String | Maximum chase value. Only applicable to `chase` order. |
| > tradeQuoteCcy | String | The quote currency used for trading. |

### WS / Advance algo orders channel

Retrieve advance algo orders (including Iceberg order, TWAP order, Trailing order). Data will be pushed when first subscribed. Data will be pushed when triggered by events such as placing/canceling order.

#### URL Path

/ws/v5/business (required login)

Request Example : single

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "algo-advance",
 "instType": "SPOT",
 "instId": "BTC-USDT"
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
 "channel": "algo-advance",
 "instType": "SPOT",
 "instId": "BTC-USDT"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "algo-advance",
 "instType": "SPOT"
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
 "channel": "algo-advance",
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
| > channel | String | Yes | Channel name`algo-advance` |
| > instType | String | Yes | Instrument type `SPOT``MARGIN``SWAP``FUTURES` `ANY` |
| > instId | String | No | Instrument ID |
| > algoId | String | No | Algo Order ID |

Successful Response Example : single

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "algo-advance",
 "instType": "SPOT",
 "instId": "BTC-USDT"
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
 "channel": "algo-advance",
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"algo-advance\", \"instType\" : \"FUTURES\"}]}",
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
| > instType | String | Yes | Instrument type `SPOT``MARGIN``SWAP``FUTURES` `ANY` |
| > instId | String | No | Instrument ID |
| > algoId | String | No | Algo Order ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example: single

```
{
 "arg":{
 "channel":"algo-advance",
 "uid": "77982378738415879",
 "instType":"SPOT",
 "instId":"BTC-USDT"
 },
 "data":[
 {
 "actualPx":"",
 "actualSide":"",
 "actualSz":"0",
 "algoId":"355056228680335360",
 "cTime":"1630924001545",
 "ccy":"",
 "clOrdId": "",
 "count":"1",
 "instId":"BTC-USDT",
 "instType":"SPOT",
 "lever":"0",
 "notionalUsd":"",
 "ordPx":"",
 "ordType":"iceberg",
 "pTime":"1630924295204",
 "posSide":"net",
 "pxLimit":"10",
 "pxSpread":"1",
 "pxVar":"",
 "side":"buy",
 "slOrdPx":"",
 "slTriggerPx":"",
 "state":"pause",
 "sz":"0.1",
 "szLimit":"0.1",
 "tdMode":"cash",
 "timeInterval":"",
 "tpOrdPx":"",
 "tpTriggerPx":"",
 "tag": "adadadadad",
 "triggerPx":"",
 "triggerTime":"",
 "tradeQuoteCcy": "USDT",
 "callbackRatio":"",
 "callbackSpread":"",
 "activePx":"",
 "moveTriggerPx":"",
 "failCode": "",
 "algoClOrdId": "",
 "reduceOnly": "",
 "isTradeBorrowMode": true
 }
 ]
}

```

#### Response parameters when data is pushed.

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > algoId | String | Algo Order ID |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| > ordId | String | Order ID, the order ID associated with the algo order. |
| > algoId | String | Algo ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > sz | String | Quantity to buy or sell. `SPOT`/`MARGIN`: in the unit of currency. `FUTURES`/`SWAP`/`OPTION`: in the unit of contract. |
| > ordType | String | Order type `iceberg`: Iceberg order `twap`: TWAP order `move_order_stop`: Trailing order |
| > side | String | Order side, `buy` `sell` |
| > posSide | String | Position side `net` `long` or `short` Only applicable to `FUTURES`/`SWAP` |
| > tdMode | String | Trade mode, `cross`: cross `isolated`: isolated `cash`: cash |
| > tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| > lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| > state | String | Order status `live`: to be effective `effective`: effective`partially_effective`: partially effective`canceled`: canceled `order_failed`: order failed `pause`: pause |
| > tpTriggerPx | String | Take-profit trigger price. |
| > tpOrdPx | String | Take-profit order price. |
| > slTriggerPx | String | Stop-loss trigger price. |
| > slOrdPx | String | Stop-loss order price. |
| > triggerPx | String | Trigger price |
| > ordPx | String | Order price |
| > actualSz | String | Actual order quantity |
| > actualPx | String | Actual order price |
| > notionalUsd | String | Estimated national value in `USD` of order |
| > tag | String | Order tag |
| > actualSide | String | Actual trigger side |
| > triggerTime | String | Trigger time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > pxVar | String | Price ratio Only applicable to `iceberg` order or `twap` order |
| > pxSpread | String | Price variance Only applicable to `iceberg` order or `twap` order |
| > szLimit | String | Average amount Only applicable to `iceberg` order or `twap` order |
| > pxLimit | String | Price limit Only applicable to `iceberg` order or `twap` order |
| > timeInterval | String | Time interval Only applicable to `twap` order |
| > count | String | Algo Order count Only applicable to `iceberg` order or `twap` order |
| > callbackRatio | String | Callback price ratioOnly applicable to `move_order_stop` order |
| > callbackSpread | String | Callback price varianceOnly applicable to `move_order_stop` order |
| > activePx | String | Active priceOnly applicable to `move_order_stop` order |
| > moveTriggerPx | String | Trigger priceOnly applicable to `move_order_stop` order |
| > failCode | String | It represents that the reason that algo order fails to trigger. It is "" when the state is `effective`/`canceled`. There will be value when the state is `order_failed`, e.g. 51008;Only applicable to Stop Order, Trailing Stop Order, Trigger order. |
| > algoClOrdId | String | Client Algo Order ID as assigned by the client. |
| > reduceOnly | String | Whether the order can only reduce the position size. Valid options: `true` or `false`. |
| > pTime | String | Push time of algo order information, millisecond format of Unix timestamp, e.g. `1597026383085` |
| > isTradeBorrowMode | Boolean | Whether borrowing currency automatically true falseOnly applicable to `trigger order`, `trailing order` and `twap order` |
| > tradeQuoteCcy | String | The quote currency used for trading. |
