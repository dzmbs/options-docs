## Trade

All `Trade` API endpoints require authentication.

### POST / Place order

You can place an order only if you have sufficient funds.

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

#### HTTP Request

`POST /api/v5/trade/order`

**Request Example

```
place order for SPOT
 POST /api/v5/trade/order
 body
 {
 "instId":"BTC-USDT",
 "tdMode":"cash",
 "clOrdId":"b15",
 "side":"buy",
 "ordType":"limit",
 "px":"2.15",
 "sz":"2"
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

# Spot mode, limit order
result = tradeAPI.place_order(
 instId="BTC-USDT",
 tdMode="cash",
 clOrdId="b15",
 side="buy",
 ordType="limit",
 px="2.15",
 sz="2"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| tdMode | String | Yes | Trade modeMargin mode `cross` `isolated` (`isolated` is only applicable to spot margin isolated)Non-Margin mode `cash``spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)Note: `isolated` (spot margin isolated) is not available in multi-currency margin mode and portfolio margin mode. Event contracts symbols only support `isolated` |
| ccy | String | No | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`. |
| clOrdId | String | No | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.Only applicable to general order. It will not be posted to algoId when placing TP/SL order after the general order is filled completely. |
| tag | String | No | Order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| side | String | Yes | Order side, `buy` `sell` |
| posSide | String | Conditional | Position side The default is `net` in the `net` mode It is required in the `long/short` mode, and can only be `long` or `short`. Only applicable to `FUTURES`/`SWAP`. Do not send this field for `SPOT` or `MARGIN` orders. Omitting it for `FUTURES`/`SWAP` in long/short mode returns error 51000. |
| ordType | String | Yes | Order type `market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP` `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Places a limit order at the maximum buy price (upper price limit) for buy orders, or the minimum sell price (lower price limit) for sell orders, as defined by the exchange's price limit bands. Any unfilled portion is immediately cancelled (IOC). Applicable only to Expiry Futures and Perpetual Futures.`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode) `mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)`elp`: Enhanced Liquidity Program order |
| sz | String | Yes | Quantity to buy or sell |
| px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| outcome | String | Conditional | The market outcome users trade on.`yes``no`Only applicable and required for `EVENTS` |
| pxUsd | String | Conditional | Place options orders in `USD` Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100% Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| reduceOnly | Boolean | No | Whether orders can only reduce in position size. Valid options: `true` or `false`. The default value is `false`.Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode Only applicable to `Futures mode` and `Multi-currency margin` |
| tgtCcy | String | No | Whether the target currency uses the quote or base currency.`base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| banAmend | Boolean | No | Whether to disallow the system from automatically reducing the order size when account balance is insufficient for the full SPOT Market Order.Valid options: `true` or `false`. The default value is `false`.If `true`: the entire order is rejected when balance is insufficient. If `false` (default): the system reduces sz to fit the available balance and executes the smaller order.Only applicable to SPOT Market Orders |
| pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `px` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit The default value is `0` |
| tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`. The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`. |
| slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.If not specified or empty, defaults to `0.00%`.Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.Only applicable to `SPOT` and `SPOT margin` `market` orders. |
| stpMode | String | No | Self trade prevention mode. `cancel_maker`,`cancel_taker`, `cancel_both`Cancel both does not support FOK The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order. |
| isElpTakerAccess | Boolean | No | ELP taker access`true`: the request can trade with ELP orders but a speed bump will be applied`false`: the request cannot trade with ELP orders and no speed bumpThe default value is `false` while `true` is only applicable to ioc orders. |
| attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information |
| > attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > tpTriggerPx | String | Conditional | Take-profit trigger priceFor condition TP order, if you fill in this parameter, you should fill in the take-profit order price as well. |
| > tpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30% Only one of `tpTriggerPx` and `tpTriggerRatio` can be passed Only applicable to FUTURES and SWAP. If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0. |
| > tpOrdPx | String | Conditional | Take-profit order price For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well. For limit TP order, you need to fill in this parameter, but the take-profit trigger price doesn’t need to be filled. If the price is -1, take-profit will be executed at the market price. |
| > tpOrdKind | String | No | TP order kind`condition``limit` The default is `condition` |
| > slTriggerPx | String | Conditional | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > slTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30% Only one of `slTriggerPx` and `slTriggerRatio` can be passed Only applicable to FUTURES and SWAP. If the main order is a buy order, it should be between 0 and 1, and if the main order is a sell order, it must be greater than 0. |
| > slOrdPx | String | Conditional | Stop-loss order priceIf you fill in this parameter, you should fill in the stop-loss trigger price.If the price is -1, stop-loss will be executed at the market price. |
| > tpTriggerPxType | String | No | Take-profit trigger price type`last`: last price `index`: index price `mark`: mark price The default is last |
| > slTriggerPxType | String | No | Stop-loss trigger price type`last`: last price `index`: index price `mark`: mark price The default is last |
| > sz | String | Conditional | Size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs |
| > amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. Whether `slTriggerPx` will move to `avgPx` when the first TP order is triggered`0`: disable, the default value `1`: Enable |
| > callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > callbackSpread | String | Conditional | Callback spread (price distance).Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > activePx | String | No | Activation price.The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.Only applicable when `ordType` = `move_order_stop` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "clOrdId": "oktswap6",
 "ordId": "312269865356374016",
 "tag": "",
 "ts":"1695190491421",
 "sCode": "0",
 "sMsg": "",
 "subCode": ""
 }
 ],
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection or success message of event execution. |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` The time is recorded after authentication. |
| outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

tdMode
Trade Mode, when placing an order, you need to specify the trade mode.
Spot mode:****- SPOT and OPTION buyer: cash
Futures mode:****- Isolated MARGIN (spot margin isolated only): isolated
- Cross MARGIN: cross
- SPOT: cash
- Cross FUTURES/SWAP/OPTION: cross
Multi-currency margin mode:****- Cross SPOT: cross
- Cross FUTURES/SWAP/OPTION: cross
Portfolio margin:****- Cross SPOT: cross
- Cross FUTURES/SWAP/OPTION: cross

clOrdId
clOrdId is a user-defined unique order identifier at the User ID level. If provided in the request parameters, it will be included in the response and can be used as a request parameter to query, cancel, and amend orders.
clOrdId must be unique among all currently pending (live or partially_filled) orders in the account. Once an order reaches a terminal state (filled, canceled, mmp_canceled), the same clOrdId may be reused for a new order. Uniqueness is not enforced historically — GET /api/v5/trade/order returns only the latest match when multiple orders share a clOrdId. "General order" means a standard order placed via this endpoint; clOrdId is not forwarded to attached TP/SL algo orders.

posSide
Position side, this parameter is not mandatory in net** mode. If you pass it through, the only valid value is **net**.**In long/short** mode, it is mandatory. Valid values are **long** or **short**.**In long/short** mode, **side** and **posSide** need to be specified in the combinations below:**Open long: buy and open long (side: fill in buy; posSide: fill in long)
Open short: sell and open short (side: fill in sell; posSide: fill in short)
Close long: sell and close long (side: fill in sell; posSide: fill in long)
Close short: buy and close short (side: fill in buy; posSide: fill in short)
Portfolio margin mode: Expiry Futures and Perpetual Futures only support net mode
Do not send this field for SPOT or MARGIN orders. For FUTURES/SWAP in net mode, omit or explicitly pass `net`.

ordType
Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:
limit: Limit order, which requires specified sz and px.
market: Market order. For SPOT and MARGIN, market order will be filled with market price (by swiping opposite order book). For Expiry Futures and Perpetual Futures, market order will be placed to order book with most aggressive price allowed by Price Limit Mechanism. For OPTION, market order is not supported yet. As the filled price for market orders cannot be determined in advance, OKX reserves/freezes your quote currency by an additional 5% for risk check.
post_only: Post-only order, which the order can only provide liquidity to the market and be a maker. If the order would have executed on placement, it will be canceled instead.
fok: Fill or kill order. If the order cannot be fully filled, the order will be canceled. The order would not be partially filled.
ioc: Immediate or cancel order. Immediately execute the transaction at the order price, cancel the remaining unfilled quantity of the order, and the order quantity will not be displayed in the order book.
optimal_limit_ioc: Places a limit order at the maximum buy price (upper price limit) for buy orders, or the minimum sell price (lower price limit) for sell orders, as defined by the exchange's price limit bands at the time of submission. Any unfilled portion is immediately cancelled (IOC). Applicable only to Expiry Futures and Perpetual Futures. The order will not execute at a price worse than the current price limit boundary.

sz
Quantity to buy or sell.
For SPOT/MARGIN Buy and Sell Limit Orders, it refers to the quantity in base currency.
For MARGIN Buy Market Orders, it refers to the quantity in quote currency.
For MARGIN Sell Market Orders, it refers to the quantity in base currency.
For SPOT Market Orders, it is set by tgtCcy.
For FUTURES/SWAP/OPTION orders, it refers to the number of contracts. Notional value = sz × ctVal × markPx (linear contracts) or sz × ctVal (inverse contracts, USD-denominated). Retrieve ctVal and ctType from GET /api/v5/public/instruments.

reduceOnly
When placing an order with this parameter set to true, it means that the order will reduce the size of the position only
For the same MARGIN instrument, the coin quantity of all reverse direction pending orders adds `sz` of new `reduceOnly` order cannot exceed the position assets. After the debt is paid off, if there is a remaining size of orders, the position will not be opened in reverse, but will be traded in SPOT.
For the same FUTURES/SWAP instrument, the sum of the current order size and all reverse direction reduce-only pending orders which’s price-time priority is higher than the current order, cannot exceed the contract quantity of position.
Only applicable to `Futures mode` and `Multi-currency margin`
Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode
Notice: Under long/short mode of Expiry Futures and Perpetual Futures, all closing orders apply the reduce-only feature which is not affected by this parameter.
If sz exceeds the current position size, the entire order is rejected — the system does not auto-trim to the position size.

tgtCcy
This parameter is used to specify the order quantity in the order request is denominated in the quantity of base or quote currency. This is applicable to SPOT Market Orders only.
Quick reference for BTC-USDT:
- tgtCcy=`quote_ccy`, sz=100 (buy): spend 100 USDT on BTC.
- tgtCcy=`base_ccy`, sz=0.001 (buy): buy 0.001 BTC at market price.
- tgtCcy=`base_ccy`, sz=0.001 (sell, default): sell 0.001 BTC.
- tgtCcy=`quote_ccy`, sz=100 (sell): sell BTC until you receive 100 USDT.
Base currency: base_ccy
Quote currency: quote_ccy

If you use the Base Currency quantity for buy market orders or the Quote Currency for sell market orders, please note:

1. If the quantity you enter is greater than what you can buy or sell, the system will execute the order according to your maximum buyable or sellable quantity. If you want to trade according to the specified quantity, you should use Limit orders.

2. When the market price is too volatile, the locked balance may not be sufficient to buy the Base Currency quantity or sell to receive the Quote Currency that you specified. We will change the quantity of the order to execute the order based on best effort principle based on your account balance. In addition, we will try to over lock a fraction of your balance to avoid changing the order quantity.

2.1 Example of base currency buy market order:

Taking the market order to buy 10 LTCs as an example, and the user can buy 11 LTC. At this time, if 10 3,000, the user's locked balance is not sufficient to buy using the specified amount of base currency, the user's maximum locked balance of 3,000 USDT will be used to settle the trade. Final transaction quantity becomes 3,000/400 = 7.5 LTC.

2.2 Example of quote currency sell market order:

Taking the market order to sell 1,000 USDT as an example, and the user can sell 1,200 USDT, 1,000

px
The value for px must be a multiple of tickSz for OPTION orders.
If not, the system will apply the rounding rules below. Using tickSz 0.0005 as an example:
The px will be rounded up to the nearest 0.0005 when the remainder of px to 0.0005 is more than 0.00025 or `px` is less than 0.0005.
The px will be rounded down to the nearest 0.0005 when the remainder of px to 0.0005 is less than 0.00025 and `px` is more than 0.0005.

For placing order with TP/SL:
Attached TP/SL orders become active only after the parent order is filled. If the parent is cancelled before any fill, the attached TP/SL is also discarded. For TP/SL orders independent of a parent order, use POST /api/v5/trade/order-algo.
1. TP/SL algo order will be generated only when this order is filled; if the parent order is cancelled before any fill, no TP/SL algo order will be generated.
2. Attaching TP/SL is neither supported for market buy with tgtCcy is base_ccy or market sell with tgtCcy is quote_ccy
3. If tpOrdKind is limit, and there is only one conditional TP order, attachAlgoClOrdId can be used as clOrdId for retrieving on "GET / Order details" endpoint.
4. For “split TPs”, including condition TP order and limit TP order.
* TP/SL orders in Split TPs only support one-way TP/SL. You can't use slTriggerPx&slOrdPx and tpTriggerPx&tpOrdPx at the same time, or error code 51076 will be thrown.
* Take-profit trigger price types (tpTriggerPxType) must be the same in an order with Split TPs attached, or error code 51080 will be thrown.
* Take-profit trigger prices (tpTriggerPx) cannot be the same in an order with Split TPs attached, or error code 51081 will be thrown.
* The size of the TP order among split TPs attached cannot be empty, or error code 51089 will be thrown.
* The total size of TP orders with Split TPs attached in a same order should equal the size of this order, or error code 51083 will be thrown.
* The number of TP orders with Split TPs attached in a same order cannot exceed 10, or error code 51079 will be thrown.
* Setting multiple TP and cost-price SL orders isn’t supported for spot and margin trading, or error code 51077 will be thrown.
* The number of SL orders with Split TPs attached in a same order cannot exceed 1, or error code 51084 will be thrown.
* The number of TP orders cannot be less than 2 when cost-price SL is enabled (amendPxOnTriggerType set as 1) for Split TPs, or error code 51085 will be thrown.
* All TP orders in one order must be of the same type, or error code 51091 will be thrown.
* TP order prices (tpOrdPx) in one order must be different, or error code 51092 will be thrown.
* TP limit order prices (tpOrdPx) in one order can't be –1 (market price), or error code 51093 will be thrown.
* You can't place TP limit orders in spot, margin, or options trading. Otherwise, error code 51094 will be thrown.

Mandatory self trade prevention (STP)
The trading platform imposes mandatory self trade prevention at master account level, which means the accounts under the same master account, including master account itself and all its affiliated sub-accounts, will be prevented from self trade. The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.
Mandatory self trade prevention will not lead to latency.
There are three STP modes. The STP mode is always taken based on the configuration in the taker order.
1. Cancel Maker: This is the default STP mode, which cancels the maker order to prevent self-trading. Then, the taker order continues to match with the next order based on the order book priority.
2. Cancel Taker: The taker order is canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled and then canceled. FOK orders are always honored and canceled if they would result in self-trading.
3. Cancel Both: Both taker and maker orders are canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled. Then, the remaining quantity of the taker order and the first maker order are canceled. FOK orders are not supported in this mode. Combining stpMode=cancel_both with ordType=`fok` returns error 50016.

tradeQuoteCcy
For users in specific countries and regions, this parameter must be filled out for a successful order. Otherwise, the system will use the quote currency of instId as the default value, then error code 51000 will occur.
The value provided must be one of the enumerated values from tradeQuoteCcyList, which can be obtained from the endpoint Get instruments (GET /api/v5/account/instruments).

Rate limit of orders tagged as isElpTakerAccess:true
- 50 orders per 2 seconds per User ID per instrument ID.
- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket

### POST / Place multiple orders

Place orders in batches. Maximum 20 orders can be placed per request.
Request parameters should be passed in the form of an array. Orders will be placed in turn

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Place order`.

#### HTTP Request

`POST /api/v5/trade/batch-orders`

Request Example

```
batch place order for SPOT
 POST /api/v5/trade/batch-orders
 body
 [
 {
 "instId":"BTC-USDT",
 "tdMode":"cash",
 "clOrdId":"b15",
 "side":"buy",
 "ordType":"limit",
 "px":"2.15",
 "sz":"2"
 },
 {
 "instId":"BTC-USDT",
 "tdMode":"cash",
 "clOrdId":"b16",
 "side":"buy",
 "ordType":"limit",
 "px":"2.15",
 "sz":"2"
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

# Place multiple orders
place_orders_without_clOrdId = [
 {"instId": "BTC-USDT", "tdMode": "cash", "clOrdId": "b15", "side": "buy", "ordType": "limit", "px": "2.15", "sz": "2"},
 {"instId": "BTC-USDT", "tdMode": "cash", "clOrdId": "b16", "side": "buy", "ordType": "limit", "px": "2.15", "sz": "2"}
]

result = tradeAPI.place_multiple_orders(place_orders_without_clOrdId)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| tdMode | String | Yes | Trade modeMargin mode `cross` `isolated`Non-Margin mode `cash``spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)Note: `isolated` is not available in multi-currency margin mode and portfolio margin mode. Event contracts symbols only support `isolated` |
| ccy | String | No | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`. |
| clOrdId | String | No | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| side | String | Yes | Order side `buy` `sell` |
| posSide | String | Conditional | Position side The default is `net` in the `net` mode It is required in the `long/short` mode, and can only be `long` or `short`. Only applicable to `FUTURES`/`SWAP`. |
| ordType | String | Yes | Order type `market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP` `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures).`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `elp`: Enhanced Liquidity Program order |
| sz | String | Yes | Quantity to buy or sell |
| px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| outcome | String | Conditional | The market outcome users trade on.`yes``no`Only applicable and required for `EVENTS` |
| pxUsd | String | Conditional | Place options orders in `USD` Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100% Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| reduceOnly | Boolean | No | Whether the order can only reduce position size. Valid options: `true` or `false`. The default value is `false`.Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode Only applicable to `Futures mode` and `Multi-currency margin` |
| tgtCcy | String | No | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| banAmend | Boolean | No | Whether to disallow the system from amending the size of the SPOT Market Order.Valid options: `true` or `false`. The default value is `false`.If `true`, system will not amend and reject the market order if user does not have sufficient funds. Only applicable to SPOT Market Orders |
| pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `px` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit The default value is `0` |
| tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`. The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`. |
| slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.If not specified or empty, defaults to `0.00%`.Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.Only applicable to `SPOT` and `SPOT margin` `market` orders. |
| stpMode | String | No | Self trade prevention mode. `cancel_maker`,`cancel_taker`, `cancel_both`Cancel both does not support FOK. The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order. |
| isElpTakerAccess | Boolean | No | ELP taker access`true`: the request can trade with ELP orders but a speed bump will be applied`false`: the request cannot trade with ELP orders and no speed bumpThe default value is `false` while `true` is only applicable to ioc orders. |
| attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information |
| > attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > tpTriggerPx | String | Conditional | Take-profit trigger priceFor condition TP order, if you fill in this parameter, you should fill in the take-profit order price as well. |
| > tpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30% Only one of `tpTriggerPx` and `tpTriggerRatio` can be passed Only applicable to FUTURES and SWAP.If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0. |
| > tpOrdPx | String | Conditional | Take-profit order price For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well. For limit TP order, you need to fill in this parameter, take-profit trigger needn't to be filled.If the price is -1, take-profit will be executed at the market price. |
| > tpOrdKind | String | No | TP order kind`condition``limit` The default is `condition` |
| > slTriggerPx | String | Conditional | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > slTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30% Only one of `slTriggerPx` and `slTriggerRatio` can be passed Only applicable to FUTURES and SWAP.If the main order is a buy order, it should be between 0 and 1, and if the main order is a sell order, it must be greater than 0. |
| > slOrdPx | String | Conditional | Stop-loss order priceIf you fill in this parameter, you should fill in the stop-loss trigger price.If the price is -1, stop-loss will be executed at the market price. |
| > tpTriggerPxType | String | No | Take-profit trigger price type`last`: last price `index`: index price `mark`: mark price The default is last |
| > slTriggerPxType | String | No | Stop-loss trigger price type`last`: last price `index`: index price `mark`: mark price The default is last |
| > sz | String | Conditional | Size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs |
| > amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. Whether `slTriggerPx` will move to `avgPx` when the first TP order is triggered`0`: disable, the default value `1`: Enable |
| > callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > callbackSpread | String | Conditional | Callback spread (price distance).Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > activePx | String | No | Activation price.The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.Only applicable when `ordType` = `move_order_stop` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "clOrdId":"oktswap6",
 "ordId":"12345689",
 "tag":"",
 "ts":"1695190491421",
 "sCode":"0",
 "sMsg":"",
 "subCode": ""
 },
 {
 "clOrdId":"oktswap7",
 "ordId":"12344",
 "tag":"",
 "ts":"1695190491421",
 "sCode":"0",
 "sMsg":"",
 "subCode": ""
 }
 ],
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection or success message of event execution. |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` The time is recorded after authentication. |
| outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

In the `Portfolio Margin` account mode, either all orders are accepted by the system successfully, or all orders are rejected by the system.

clOrdId
clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.
clOrdId must be unique among all pending orders and the current request.

Rate limit of orders tagged as isElpTakerAccess:true
- 50 orders per 2 seconds per User ID per instrument ID.
- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket

### POST / Cancel order

Cancel an incomplete order.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/cancel-order`

Request Example

```
POST /api/v5/trade/cancel-order
body
{
 "ordId":"590908157585625111",
 "instId":"BTC-USD-190927"
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

# Cancel order
result = tradeAPI.cancel_order(instId="BTC-USDT", ordId="590908157585625111")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required. If both are passed, ordId will be used. |
| clOrdId | String | Conditional | Client Order ID as assigned by the client |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "clOrdId":"oktswap6",
 "ordId":"12345689",
 "ts":"1695190491421",
 "sCode":"0",
 "sMsg":""
 }
 ],
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |
| inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` The time is recorded after authentication. |
| outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state.

### POST / Cancel multiple orders

Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request. Request parameters should be passed in the form of an array.

#### Rate Limit: 300 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`.

#### HTTP Request

`POST /api/v5/trade/cancel-batch-orders`

Request Example

```
POST /api/v5/trade/cancel-batch-orders
body
[
 {
 "instId":"BTC-USDT",
 "ordId":"590908157585625111"
 },
 {
 "instId":"BTC-USDT",
 "ordId":"590908544950571222"
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

# Cancel multiple orders by ordId
cancel_orders_with_orderId = [
 {"instId": "BTC-USDT", "ordId": "590908157585625111"},
 {"instId": "BTC-USDT", "ordId": "590908544950571222"}
]

result = tradeAPI.cancel_multiple_orders(cancel_orders_with_orderId)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| ordId | String | Conditional | Order IDEither `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used. |
| clOrdId | String | Conditional | Client Order ID as assigned by the client |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "clOrdId":"oktswap6",
 "ordId":"12345689",
 "ts":"1695190491421",
 "sCode":"0",
 "sMsg":""
 },
 {
 "clOrdId":"oktswap7",
 "ordId":"12344",
 "ts":"1695190491421",
 "sCode":"0",
 "sMsg":""
 }
 ],
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |
| inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` The time is recorded after authentication. |
| outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

### POST / Amend order

Amend an incomplete order.

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

#### HTTP Request

`POST /api/v5/trade/amend-order`

Request Example

```
POST /api/v5/trade/amend-order
body
{
 "ordId":"590909145319051111",
 "newSz":"2",
 "instId":"BTC-USDT"
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

# Amend order
result = tradeAPI.amend_order(
 instId="BTC-USDT",
 ordId="590909145319051111",
 newSz="2"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID |
| cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails Valid options: `false` or `true`, the default is `false`. Amendment failure scenarios include: `newSz` not a multiple of `lotSz`, position or risk limit breach, etc. When `false` (default): the original order continues unchanged after a failed amendment. When `true`: the original order is auto-cancelled on any amendment failure. |
| ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used. |
| clOrdId | String | Conditional | Client Order ID as assigned by the client |
| reqId | String | No | Client Request ID as assigned by the client for order amendment A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. The response will include the corresponding `reqId` to help you identify the request if you provide it in the request. |
| newSz | String | Conditional | New total target quantity after amendment, must be > 0. This is the desired total order size, not the remaining unfilled portion. For a partially-filled order: if 3 contracts are already filled and you want a total of 8, pass `newSz=8` (not 5). The system will attempt to fill the remaining 5. At least one of `newSz` or `newPx` (or `newPxUsd`/`newPxVol` for options) must be provided. |
| newPx | String | Conditional | New price after amendment. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order. At least one of `newSz` or `newPx` must be provided. |
| speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| newPxUsd | String | Conditional | Modify options orders using USD prices Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100% Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit The default value is `0` |
| attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information |
| > attachAlgoId | String | Conditional | The order ID of the attached TP/SL or trailing stop order. It is required to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely. |
| > attachAlgoClOrdId | String | Conditional | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > newTpTriggerPx | String | Conditional | Take-profit trigger price. Either the take profit trigger price or order price is 0, it means that the take profit is deleted. |
| > newTpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `newTpTriggerPx` and `newTpTriggerRatio` can be passed. If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0. 0 means to delete the take-profit. |
| > newTpOrdPx | String | Conditional | Take-profit order priceIf the price is -1, take-profit will be executed at the market price. |
| > newTpOrdKind | String | No | TP order kind`condition``limit` |
| > newSlTriggerPx | String | Conditional | Stop-loss trigger priceEither the stop loss trigger price or order price is 0, it means that the stop loss is deleted. |
| > newSlTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed. If the main order is a buy order, it should be between 0 and 1, and if the main order is a sell order, it must be greater than 0. Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed, 0 means to delete the stop-loss. |
| > newSlOrdPx | String | Conditional | Stop-loss order priceIf the price is -1, stop-loss will be executed at the market price. |
| > newTpTriggerPxType | String | Conditional | Take-profit trigger price type`last`: last price `index`: index price `mark`: mark priceOnly applicable to `FUTURES`/`SWAP`If you want to add the take-profit, this parameter is required |
| > newSlTriggerPxType | String | Conditional | Stop-loss trigger price type`last`: last price `index`: index price `mark`: mark priceOnly applicable to `FUTURES`/`SWAP`If you want to add the stop-loss, this parameter is required |
| > sz | String | Conditional | New size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs |
| > amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| > newCallbackRatio | String | Conditional | New callback ratio, e.g. `0.05` represents 5%.Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > newCallbackSpread | String | Conditional | New callback spread (price distance).Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > newActivePx | String | No | New activation price.Only applicable when `ordType` = `move_order_stop` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "clOrdId":"",
 "ordId":"12344",
 "ts":"1695190491421",
 "reqId":"b12344",
 "sCode":"0",
 "sMsg":""
 "subCode": ""
 }
 ],
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > reqId | String | Client Request ID as assigned by the client for order amendment. |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` The time is recorded after authentication. |
| outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

newSz
If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled.

The amend order returns sCode equal to 0. It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query

### POST / Amend multiple orders

Amend incomplete orders in batches. Maximum 20 orders can be amended per request. Request parameters should be passed in the form of an array.

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Amend order`.

#### HTTP Request

`POST /api/v5/trade/amend-batch-orders`

Request Example

```
POST /api/v5/trade/amend-batch-orders
body
[
 {
 "ordId":"590909308792049444",
 "newSz":"2",
 "instId":"BTC-USDT"
 },
 {
 "ordId":"590909308792049555",
 "newSz":"2",
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

# Amend incomplete orders in batches by ordId
amend_orders_with_orderId = [
 {"instId": "BTC-USDT", "ordId": "590909308792049444","newSz":"2"},
 {"instId": "BTC-USDT", "ordId": "590909308792049555","newSz":"2"}
]

result = tradeAPI.amend_multiple_orders(amend_orders_with_orderId)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID |
| cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment failsValid options: `false` or `true`, the default is `false`. Amendment failure scenarios include: `newSz` not a multiple of `lotSz`, position or risk limit breach, etc. When `false` (default): the original order continues unchanged after a failed amendment. When `true`: the original order is auto-cancelled on any amendment failure. |
| ordId | String | Conditional | Order ID Either `ordId` or `clOrdId`is required, if both are passed, `ordId` will be used. |
| clOrdId | String | Conditional | Client Order ID as assigned by the client |
| reqId | String | No | Client Request ID as assigned by the client for order amendment A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. The response will include the corresponding `reqId` to help you identify the request if you provide it in the request. |
| newSz | String | Conditional | New total target quantity after amendment, must be > 0. This is the desired total order size, not the remaining unfilled portion. For a partially-filled order: if 3 contracts are already filled and you want a total of 8, pass `newSz=8` (not 5). The system will attempt to fill the remaining 5. At least one of `newSz` or `newPx` (or `newPxUsd`/`newPxVol` for options) must be provided. |
| newPx | String | Conditional | New price after amendment. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order. At least one of `newSz` or `newPx` must be provided. |
| speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| newPxUsd | String | Conditional | Modify options orders using USD prices Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100% Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit The default value is `0` |
| attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information |
| > attachAlgoId | String | Conditional | The order ID of the attached TP/SL or trailing stop order. It is required to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely. |
| > attachAlgoClOrdId | String | Conditional | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > newTpTriggerPx | String | Conditional | Take-profit trigger price. Either the take profit trigger price or order price is 0, it means that the take profit is deleted. |
| > newTpTriggerRatio | String | Conditional | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `newTpTriggerPx` and `newTpTriggerRatio` can be passed If the main order is a buy order, it must be greater than 0, and if the main order is a sell order, it must be between -1 and 0. 0 means to delete the take-profit. |
| > newTpOrdPx | String | Conditional | Take-profit order priceIf the price is -1, take-profit will be executed at the market price. |
| > newTpOrdKind | String | No | TP order kind`condition``limit` |
| > newSlTriggerPx | String | Conditional | Stop-loss trigger priceEither the stop loss trigger price or order price is 0, it means that the stop loss is deleted. |
| > newSlTriggerRatio | String | Conditional | Stop-loss trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. Only one of `newSlTriggerPx` and `newSlTriggerRatio` can be passed If the main order is a buy order, it must be between 0 and 1, and if the main order is a sell order, it must be greater than 0. 0 means to delete the stop-loss. |
| > newSlOrdPx | String | Conditional | Stop-loss order priceIf the price is -1, stop-loss will be executed at the market price. |
| > newTpTriggerPxType | String | Conditional | Take-profit trigger price type`last`: last price `index`: index price `mark`: mark priceOnly applicable to `FUTURES`/`SWAP`If you want to add the take-profit, this parameter is required |
| > newSlTriggerPxType | String | Conditional | Stop-loss trigger price type`last`: last price `index`: index price `mark`: mark priceOnly applicable to `FUTURES`/`SWAP`If you want to add the stop-loss, this parameter is required |
| > sz | String | Conditional | New size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs |
| > amendPxOnTriggerType | String | No | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| > newCallbackRatio | String | Conditional | New callback ratio, e.g. `0.05` represents 5%.Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > newCallbackSpread | String | Conditional | New callback spread (price distance).Either `newCallbackRatio` or `newCallbackSpread` can be passed. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > newActivePx | String | No | New activation price.Only applicable when `ordType` = `move_order_stop` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "clOrdId":"oktswap6",
 "ordId":"12345689",
 "ts":"1695190491421",
 "reqId":"b12344",
 "sCode":"0",
 "sMsg":"",
 "subCode": ""
 },
 {
 "clOrdId":"oktswap7",
 "ordId":"12344",
 "ts":"1695190491421",
 "reqId":"b12344",
 "sCode":"0",
 "sMsg":"",
 "subCode": ""
 }
 ],
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success |
| msg | String | The error message, empty if the code is 0 |
| data | Array of objects | Array of objects contains the response results |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > reqId | String | Client Request ID as assigned by the client for order amendment. |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at REST gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` The time is recorded after authentication. |
| outTime | String | Timestamp at REST gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

newSz
If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled.

### POST / Close positions

Close the position of an instrument via a market order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/close-position`

Request Example

```
POST /api/v5/trade/close-position
body
{
 "instId":"BTC-USDT-SWAP",
 "mgnMode":"cross"
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

# Close the position of an instrument via a market order
result = tradeAPI.close_positions(
 instId="BTC-USDT-SWAP",
 mgnMode="cross"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID |
| posSide | String | Conditional | Position side This parameter can be omitted in `net` mode, and the default value is `net`. You can only fill with `net`.This parameter must be filled in under the `long/short` mode. Fill in `long` for close-long and `short` for close-short. |
| mgnMode | String | Yes | Margin mode`cross` `isolated` |
| ccy | String | Conditional | Margin currency, required in the case of closing `cross` `MARGIN` position for `Futures mode`. |
| autoCxl | Boolean | No | Whether any pending orders for closing out needs to be automatically canceled when close position via a market order.`false` or `true`, the default is `false`. |
| clOrdId | String | No | Client-supplied IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "clOrdId": "",
 "instId": "BTC-USDT-SWAP",
 "posSide": "long",
 "tag": ""
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| posSide | String | Position side |
| clOrdId | String | Client-supplied IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

if there are any pending orders for closing out and the orders do not need to be automatically canceled, it will return an error code and message to prompt users to cancel pending orders before closing the positions.

### GET / Order details

Retrieve order details.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/order`

Request Example

```
GET /api/v5/trade/order?ordId=1753197687182819328&instId=BTC-USDT
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Retrieve order details by ordId
result = tradeAPI.get_order(
 instId="BTC-USDT",
 ordId="680800019749904384"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT`Only applicable to live instruments |
| ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used |
| clOrdId | String | Conditional | Client Order ID as assigned by the clientIf the `clOrdId` is associated with multiple orders, only the latest one will be returned. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "accFillSz": "0.00192834",
 "algoClOrdId": "",
 "algoId": "",
 "attachAlgoClOrdId": "",
 "attachAlgoOrds": [],
 "avgPx": "51858",
 "cTime": "1708587373361",
 "cancelSource": "",
 "cancelSourceReason": "",
 "category": "normal",
 "ccy": "",
 "clOrdId": "",
 "fee": "-0.00000192834",
 "feeCcy": "BTC",
 "fillPx": "51858",
 "fillSz": "0.00192834",
 "fillTime": "1708587373361",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "isTpLimit": "false",
 "lever": "",
 "linkedAlgoOrd": {
 "algoId": ""
 },
 "ordId": "680800019749904384",
 "ordType": "market",
 "pnl": "0",
 "posSide": "net",
 "px": "",
 "pxType": "",
 "pxUsd": "",
 "pxVol": "",
 "quickMgnType": "",
 "rebate": "0",
 "rebateCcy": "USDT",
 "reduceOnly": "false",
 "side": "buy",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "",
 "source": "",
 "state": "filled",
 "stpId": "",
 "stpMode": "",
 "sz": "100",
 "tag": "",
 "tdMode": "cash",
 "tgtCcy": "quote_ccy",
 "tpOrdPx": "",
 "tpTriggerPx": "",
 "tpTriggerPxType": "",
 "tradeId": "744876980",
 "tradeQuoteCcy": "USDT",
 "uTime": "1708587373362"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instId | String | Instrument ID |
| tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | PriceFor options, use coin as unit (e.g. BTC, ETH) |
| pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types |
| pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types |
| pxType | String | Price type of options `px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH) `pxVol`: Place an order based on pxVol `pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD) |
| sz | String | Quantity to buy or sell |
| pnl | String | Profit and loss (excluding the fee). Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| ordType | String | Order type `market`: Market order `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `op_fok`: Simple options (fok)`elp`: Enhanced Liquidity Program order |
| side | String | Order side |
| posSide | String | Position side |
| tdMode | String | Trade mode |
| accFillSz | String | Running total of filled quantity since order creation. In WebSocket order channel push events, `accFillSz` always represents the cumulative total, not the increment since the last push.The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC;The unit is contract for `FUTURES`/`SWAP`/`OPTION` |
| fillPx | String | Last filled price. If none is filled, it will return "". |
| tradeId | String | Last traded ID |
| fillSz | String | Quantity of the most recent individual fill event (not cumulative). For the running total of all fills, use `accFillSz`.The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC;The unit is contract for `FUTURES`/`SWAP`/`OPTION` |
| fillTime | String | Last filled time |
| avgPx | String | Average filled price. If none is filled, it will return "". |
| state | String | Order state:`live`: on the order book, no fills yet.`partially_filled`: partially executed, still active on book.`filled`: fully executed, terminal state.`canceled`: cancelled, terminal state. For IOC orders partially filled before cancellation, `accFillSz` may be non-zero.`mmp_canceled`: automatically cancelled by Market Maker Protection, terminal state.Note: GET /api/v5/trade/orders-pending only returns `live` and `partially_filled`; GET /api/v5/trade/orders-history returns `filled`, `canceled`, and `mmp_canceled`. |
| stpId | String | Self trade prevention IDReturn "" if self trade prevention is not applicable (Deprecated) |
| stpMode | String | Self trade prevention mode |
| lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop. |
| tpTriggerPx | String | Take-profit trigger price. |
| tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| tpOrdPx | String | Take-profit order price. |
| slTriggerPx | String | Stop-loss trigger price. |
| slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| slOrdPx | String | Stop-loss order price. |
| attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information |
| > attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely. |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > tpOrdKind | String | TP order kind`condition``limit` |
| > tpTriggerPx | String | Take-profit trigger price. |
| > tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order price. |
| > slTriggerPx | String | Stop-loss trigger price. |
| > slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price. |
| > sz | String | Size. Only applicable to TP order of split TPs |
| > amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| > callbackRatio | String | Callback ratio, e.g. `0.05` represents 5% |
| > callbackSpread | String | Callback spread (price distance) |
| > activePx | String | Activation price |
| > failCode | String | The error code when failing to place TP/SL order, e.g. 51020 The default is "" |
| > failReason | String | The error reason when failing to place TP/SL order. The default is "" |
| linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order. |
| > algoId | String | Algo ID |
| feeCcy | String | Fee currencyFor maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged. |
| fee | String | Fee amount. Sign convention: negative = net fee paid to platform; positive = net rebate received from platform. The net amount reflects fee minus rebate.For Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negative.For maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin).For split accounting, use `feeCcy` + `fee` together with `rebateCcy` + `rebate`. `feeCcy` and `rebateCcy` may differ. |
| rebateCcy | String | Rebate currencyFor maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid. |
| rebate | String | Rebate amount, only applicable to Spot and MarginFor maker sell orders: Accumulated fee and rebate amount in the unit of base currency.For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate. |
| source | String | Order source (non-exhaustive — handle unknown values gracefully as new types may be added):`6`: The normal order triggered by the `trigger order``7`: The normal order triggered by the `TP/SL order` `13`: The normal order triggered by the algo order`25`: The normal order triggered by the `trailing stop order``34`: The normal order triggered by the chase order.All values represent system-generated child orders triggered by parent algo or strategy orders. |
| category | String | Category:`normal`: standard user-placed order.`twap`: forced repayment order generated by the system (not a TWAP algorithmic strategy).`adl`: auto-deleveraging, system-triggered position reduction.`full_liquidation`: forced full position close due to margin breach.`partial_liquidation`: forced partial position close.`delivery`: futures/options expiry settlement execution.`ddh`: delta dynamic hedge order placed by the options market-maker system.`auto_conversion`: system-triggered asset conversion. |
| reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false. |
| isTpLimit | String | Whether it is TP limit order. true or false |
| cancelSource | String | Code of the cancellation source. |
| cancelSourceReason | String | Reason for the cancellation. |
| quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` (Deprecated) |
| algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "". |
| algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "". |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| tradeQuoteCcy | String | The quote currency used for trading. |
| outcome | String | The market outcome the user traded on.`yes``no`Only applicable to `EVENTS` |

### GET / Order List

Retrieve all incomplete orders under the current account.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-pending`

Request Example

```
GET /api/v5/trade/orders-pending?ordType=post_only,fok,ioc&instType=SPOT
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Retrieve all incomplete orders
result = tradeAPI.get_order_list(
 instType="SPOT",
 ordType="post_only,fok,ioc"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instId | String | No | Instrument ID, e.g. `BTC-USD-200927` |
| ordType | String | No | Order type `market`: Market order `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order `mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `op_fok`: Simple options (fok)`elp`: Enhanced Liquidity Program order |
| state | String | No | State`live` `partially_filled` |
| after | String | No | Pagination of data to return records earlier than the requested `ordId` |
| before | String | No | Pagination of data to return records newer than the requested `ordId` |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "accFillSz": "0",
 "algoClOrdId": "",
 "algoId": "",
 "attachAlgoClOrdId": "",
 "attachAlgoOrds": [],
 "avgPx": "",
 "cTime": "1724733617998",
 "cancelSource": "",
 "cancelSourceReason": "",
 "category": "normal",
 "ccy": "",
 "clOrdId": "",
 "fee": "0",
 "feeCcy": "BTC",
 "fillPx": "",
 "fillSz": "0",
 "fillTime": "",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "isTpLimit": "false",
 "lever": "",
 "linkedAlgoOrd": {
 "algoId": ""
 },
 "ordId": "1752588852617379840",
 "ordType": "post_only",
 "pnl": "0",
 "posSide": "net",
 "px": "13013.5",
 "pxType": "",
 "pxUsd": "",
 "pxVol": "",
 "quickMgnType": "",
 "rebate": "0",
 "rebateCcy": "USDT",
 "reduceOnly": "false",
 "side": "buy",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "",
 "source": "",
 "state": "live",
 "stpId": "",
 "stpMode": "cancel_maker",
 "sz": "0.001",
 "tag": "",
 "tdMode": "cash",
 "tgtCcy": "",
 "tpOrdPx": "",
 "tpTriggerPx": "",
 "tpTriggerPxType": "",
 "tradeId": "",
 "tradeQuoteCcy": "USDT",
 "uTime": "1724733617998"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instId | String | Instrument ID |
| tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | Price For options, use coin as unit (e.g. BTC, ETH) |
| pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types |
| pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types |
| pxType | String | Price type of options `px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH) `pxVol`: Place an order based on pxVol `pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD) |
| sz | String | Quantity to buy or sell |
| pnl | String | Profit and loss (excluding the fee). Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| ordType | String | Order type `market`: Market order `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `op_fok`: Simple options (fok)`elp`: Enhanced Liquidity Program order |
| side | String | Order side |
| posSide | String | Position side |
| tdMode | String | Trade mode |
| accFillSz | String | Accumulated fill quantity |
| fillPx | String | Last filled price |
| tradeId | String | Last trade ID |
| fillSz | String | Last filled quantity |
| fillTime | String | Last filled time |
| avgPx | String | Average filled price. If none is filled, it will return "". |
| state | String | State`live` `partially_filled` |
| lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop. |
| tpTriggerPx | String | Take-profit trigger price. |
| tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| tpOrdPx | String | Take-profit order price. |
| slTriggerPx | String | Stop-loss trigger price. |
| slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| slOrdPx | String | Stop-loss order price. |
| attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information |
| > attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely. |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > tpOrdKind | String | TP order kind`condition``limit` |
| > tpTriggerPx | String | Take-profit trigger price. |
| > tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order price. |
| > slTriggerPx | String | Stop-loss trigger price. |
| > slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price. |
| > sz | String | Size. Only applicable to TP order of split TPs |
| > amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| > callbackRatio | String | Callback ratio, e.g. `0.05` represents 5% |
| > callbackSpread | String | Callback spread (price distance) |
| > activePx | String | Activation price |
| > failCode | String | The error code when failing to place TP/SL order, e.g. 51020 The default is "" |
| > failReason | String | The error reason when failing to place TP/SL order. The default is "" |
| linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order. |
| > algoId | String | Algo ID |
| stpId | String | Self trade prevention IDReturn "" if self trade prevention is not applicable (Deprecated) |
| stpMode | String | Self trade prevention mode |
| feeCcy | String | Fee currencyFor maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged. |
| fee | String | Fee amountFor Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negativeFor maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin) |
| rebateCcy | String | Rebate currencyFor maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid. |
| rebate | String | Rebate amount, only applicable to Spot and MarginFor maker sell orders: Accumulated fee and rebate amount in the unit of base currency.For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate. |
| source | String | Order source`6`: The normal order triggered by the `trigger order``7`: The normal order triggered by the `TP/SL order` `13`: The normal order triggered by the algo order`25`: The normal order triggered by the `trailing stop order``34`: The normal order triggered by the chase order |
| category | String | Category `normal` |
| reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false. |
| quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` (Deprecated) |
| algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "". |
| algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "". |
| isTpLimit | String | Whether it is TP limit order. true or false |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cancelSource | String | Code of the cancellation source. |
| cancelSourceReason | String | Reason for the cancellation. |
| tradeQuoteCcy | String | The quote currency used for trading. |
| outcome | String | The market outcome the user traded on.`yes``no`Only applicable to `EVENTS` |

### GET / Order history (last 7 days)

Get completed orders which are placed in the last 7 days, including those placed 7 days ago but completed in the last 7 days.

The incomplete orders that have been canceled are only reserved for 2 hours.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-history`

Request Example

```
GET /api/v5/trade/orders-history?ordType=post_only,fok,ioc&instType=SPOT
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Get completed SPOT orders which are placed in the last 7 days
# The incomplete orders that have been canceled are only reserved for 2 hours
result = tradeAPI.get_orders_history(
 instType="SPOT",
 ordType="post_only,fok,ioc"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | yes | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |
| ordType | String | No | Order type`market`: market order `limit`: limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `op_fok`: Simple options (fok) `elp`: Enhanced Liquidity Program order |
| state | String | No | State`canceled``filled``mmp_canceled`: Order canceled automatically due to Market Maker Protection |
| category | String | No | Category `twap` `adl``full_liquidation``partial_liquidation` `delivery` `ddh`: Delta dynamic hedge |
| after | String | No | Pagination of data to return records earlier than the requested `ordId` |
| before | String | No | Pagination of data to return records newer than the requested `ordId` |
| begin | String | No | Filter with a begin timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085 |
| end | String | No | Filter with an end timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085 |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "accFillSz": "0.00192834",
 "algoClOrdId": "",
 "algoId": "",
 "attachAlgoClOrdId": "",
 "attachAlgoOrds": [],
 "avgPx": "51858",
 "cTime": "1708587373361",
 "cancelSource": "",
 "cancelSourceReason": "",
 "category": "normal",
 "ccy": "",
 "clOrdId": "",
 "fee": "-0.00000192834",
 "feeCcy": "BTC",
 "fillPx": "51858",
 "fillSz": "0.00192834",
 "fillTime": "1708587373361",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "lever": "",
 "linkedAlgoOrd": {
 "algoId": ""
 },
 "ordId": "680800019749904384",
 "ordType": "market",
 "pnl": "0",
 "posSide": "",
 "px": "",
 "pxType": "",
 "pxUsd": "",
 "pxVol": "",
 "quickMgnType": "",
 "rebate": "0",
 "rebateCcy": "USDT",
 "reduceOnly": "false",
 "side": "buy",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "",
 "source": "",
 "state": "filled",
 "stpId": "",
 "stpMode": "",
 "sz": "100",
 "tag": "",
 "tdMode": "cash",
 "tgtCcy": "quote_ccy",
 "tpOrdPx": "",
 "tpTriggerPx": "",
 "tpTriggerPxType": "",
 "tradeId": "744876980",
 "tradeQuoteCcy": "USDT",
 "uTime": "1708587373362",
 "isTpLimit": "false"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instId | String | Instrument ID |
| tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | Price For options, use coin as unit (e.g. BTC, ETH) |
| pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types |
| pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types |
| pxType | String | Price type of options `px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH) `pxVol`: Place an order based on pxVol `pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD) |
| sz | String | Quantity to buy or sell |
| ordType | String | Order type `market`: market order `limit`: limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `op_fok`: Simple options (fok)`elp`: Enhanced Liquidity Program order |
| side | String | Order side |
| posSide | String | Position side |
| tdMode | String | Trade mode |
| accFillSz | String | Accumulated fill quantity |
| fillPx | String | Last filled price. If none is filled, it will return "". |
| tradeId | String | Last trade ID |
| fillSz | String | Last filled quantity |
| fillTime | String | Last filled time |
| avgPx | String | Average filled price. If none is filled, it will return "". |
| state | String | State `canceled` `filled` `mmp_canceled` |
| lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop. |
| tpTriggerPx | String | Take-profit trigger price. |
| tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| tpOrdPx | String | Take-profit order price. |
| slTriggerPx | String | Stop-loss trigger price. |
| slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| slOrdPx | String | Stop-loss order price. |
| attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information |
| > attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely. |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > tpOrdKind | String | TP order kind`condition``limit` |
| > tpTriggerPx | String | Take-profit trigger price. |
| > tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order price. |
| > slTriggerPx | String | Stop-loss trigger price. |
| > slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price. |
| > sz | String | Size. Only applicable to TP order of split TPs |
| > amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| > callbackRatio | String | Callback ratio, e.g. `0.05` represents 5% |
| > callbackSpread | String | Callback spread (price distance) |
| > activePx | String | Activation price |
| > failCode | String | The error code when failing to place TP/SL order, e.g. 51020 The default is "" |
| > failReason | String | The error reason when failing to place TP/SL order. The default is "" |
| linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order. |
| > algoId | String | Algo ID |
| stpId | String | Self trade prevention IDReturn "" if self trade prevention is not applicable (Deprecated) |
| stpMode | String | Self trade prevention mode |
| feeCcy | String | Fee currencyFor maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged. |
| fee | String | Fee amountFor Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negativeFor maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin) |
| rebateCcy | String | Rebate currencyFor maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid. |
| rebate | String | Rebate amount, only applicable to Spot and MarginFor maker sell orders: Accumulated fee and rebate amount in the unit of base currency.For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate. |
| source | String | Order source`6`: The normal order triggered by the `trigger order``7`: The normal order triggered by the `TP/SL order` `13`: The normal order triggered by the algo order`25`: The normal order triggered by the `trailing stop order``34`: The normal order triggered by the chase order |
| pnl | String | Profit and loss (excluding the fee). Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| category | String | Category `normal``twap` `adl``full_liquidation``partial_liquidation` `delivery` `ddh`: Delta dynamic hedge`auto_conversion` |
| reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false. |
| cancelSource | String | Code of the cancellation source. |
| cancelSourceReason | String | Reason for the cancellation. |
| algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "". |
| algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "". |
| isTpLimit | String | Whether it is TP limit order. true or false |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` (Deprecated) |
| tradeQuoteCcy | String | The quote currency used for trading. |
| outcome | String | The market outcome the user traded on.`yes``no`Only applicable to `EVENTS` |

### GET / Order history (last 3 months)

Get completed orders which are placed in the last 3 months, including those placed 3 months ago but completed in the last 3 months.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/orders-history-archive`

Request Example

```
GET /api/v5/trade/orders-history-archive?ordType=post_only,fok,ioc&instType=SPOT
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Get completed SPOT orders which are placed in the last 3 months
result = tradeAPI.get_orders_history_archive(
 instType="SPOT",
 ordType="post_only,fok,ioc"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | yes | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instId | String | No | Instrument ID, e.g. `BTC-USD-200927` |
| ordType | String | No | Order type `market`: Market order `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `op_fok`: Simple options (fok) `elp`: Enhanced Liquidity Program order |
| state | String | No | State`canceled` `filled``mmp_canceled`: Order canceled automatically due to Market Maker Protection |
| category | String | No | Category `twap` `adl``full_liquidation``partial_liquidation``delivery` `ddh`: Delta dynamic hedge |
| after | String | No | Pagination of data to return records earlier than the requested `ordId` |
| before | String | No | Pagination of data to return records newer than the requested `ordId` |
| begin | String | No | Filter with a begin timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085 |
| end | String | No | Filter with an end timestamp `cTime`. Unix timestamp format in milliseconds, e.g. 1597026383085 |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "accFillSz": "0.00192834",
 "algoClOrdId": "",
 "algoId": "",
 "attachAlgoClOrdId": "",
 "attachAlgoOrds": [],
 "avgPx": "51858",
 "cTime": "1708587373361",
 "cancelSource": "",
 "cancelSourceReason": "",
 "category": "normal",
 "ccy": "",
 "clOrdId": "",
 "fee": "-0.00000192834",
 "feeCcy": "BTC",
 "fillPx": "51858",
 "fillSz": "0.00192834",
 "fillTime": "1708587373361",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "lever": "",
 "ordId": "680800019749904384",
 "ordType": "market",
 "pnl": "0",
 "posSide": "",
 "px": "",
 "pxType": "",
 "pxUsd": "",
 "pxVol": "",
 "quickMgnType": "",
 "rebate": "0",
 "rebateCcy": "USDT",
 "reduceOnly": "false",
 "side": "buy",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "",
 "source": "",
 "state": "filled",
 "stpId": "",
 "stpMode": "",
 "sz": "100",
 "tag": "",
 "tdMode": "cash",
 "tgtCcy": "quote_ccy",
 "tpOrdPx": "",
 "tpTriggerPx": "",
 "tpTriggerPxType": "",
 "tradeId": "744876980",
 "tradeQuoteCcy": "USDT",
 "uTime": "1708587373362",
 "isTpLimit": "false",
 "linkedAlgoOrd": {
 "algoId": ""
 }
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instId | String | Instrument ID |
| tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | Price For options, use coin as unit (e.g. BTC, ETH) |
| pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types |
| pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types |
| pxType | String | Price type of options `px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH) `pxVol`: Place an order based on pxVol `pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD) |
| sz | String | Quantity to buy or sell |
| ordType | String | Order type `market`: Market order `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode) `op_fok`: Simple options (fok) `elp`: Enhanced Liquidity Program order |
| side | String | Order side |
| posSide | String | Position side |
| tdMode | String | Trade mode |
| accFillSz | String | Accumulated fill quantity |
| fillPx | String | Last filled price. If none is filled, it will return "". |
| tradeId | String | Last trade ID |
| fillSz | String | Last filled quantity |
| fillTime | String | Last filled time |
| avgPx | String | Average filled price. If none is filled, it will return "". |
| state | String | State `canceled` `filled` `mmp_canceled` |
| lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop. |
| tpTriggerPx | String | Take-profit trigger price. |
| tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| tpOrdPx | String | Take-profit order price. |
| slTriggerPx | String | Stop-loss trigger price. |
| slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| slOrdPx | String | Stop-loss order price. |
| attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information |
| > attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely. |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > tpOrdKind | String | TP order kind`condition``limit` |
| > tpTriggerPx | String | Take-profit trigger price. |
| > tpTriggerRatio | String | Take profit trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order price. |
| > slTriggerPx | String | Stop-loss trigger price. |
| > slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30% Only applicable to FUTURES and SWAP. |
| > slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price. |
| > sz | String | Size. Only applicable to TP order of split TPs |
| > amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| > callbackRatio | String | Callback ratio, e.g. `0.05` represents 5% |
| > callbackSpread | String | Callback spread (price distance) |
| > activePx | String | Activation price |
| > failCode | String | The error code when failing to place TP/SL order, e.g. 51020 The default is "" |
| > failReason | String | The error reason when failing to place TP/SL order. The default is "" |
| linkedAlgoOrd | Object | Linked SL order detail, only applicable to the order that is placed by one-cancels-the-other (OCO) order that contains the TP limit order. |
| > algoId | String | Algo ID |
| stpId | String | Self trade prevention IDReturn "" if self trade prevention is not applicable (Deprecated) |
| stpMode | String | Self trade prevention mode |
| feeCcy | String | Fee currencyFor maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged. |
| fee | String | Fee amountFor Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negativeFor maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin) |
| rebateCcy | String | Rebate currencyFor maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid. |
| rebate | String | Rebate amount, only applicable to Spot and MarginFor maker sell orders: Accumulated fee and rebate amount in the unit of base currency.For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate. |
| source | String | Order source`6`: The normal order triggered by the `trigger order``7`:The normal order triggered by the `TP/SL order` `13`: The normal order triggered by the algo order`25`:The normal order triggered by the `trailing stop order``34`: The normal order triggered by the `chase order` |
| pnl | String | Profit and loss (excluding the fee). Applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| category | String | Category `normal``twap` `adl``full_liquidation``partial_liquidation` `delivery` `ddh`: Delta dynamic hedge`auto_conversion` |
| reduceOnly | String | Whether the order can only reduce the position size. Valid options: true or false. |
| cancelSource | String | Code of the cancellation source. |
| cancelSourceReason | String | Reason for the cancellation. |
| algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "". |
| algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "". |
| isTpLimit | String | Whether it is TP limit order. true or false |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` (Deprecated) |
| tradeQuoteCcy | String | The quote currency used for trading. |
| outcome | String | The market outcome the user traded on.`yes``no`Only applicable to `EVENTS` |

This interface does not contain the order data of the `Canceled orders without any fills` type, which can be obtained through the `Get Order History (last 7 days)` interface.

As far as OPTION orders that are complete, pxVol and pxUsd will update in time for px order, pxVol will update in time for pxUsd order, pxUsd will update in time for pxVol order.

### GET / Transaction details (last 3 days)

Retrieve recently-filled transaction details in the last 3 day.

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/fills`

Request Example

```
GET /api/v5/trade/fills
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Retrieve recently-filled transaction details
result = tradeAPI.get_fills()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |
| ordId | String | No | Order ID |
| subType | String | No | Transaction type `1`: Buy`2`: Sell`3`: Open long`4`: Open short`5`: Close long`6`: Close short `100`: Partial liquidation close long`101`: Partial liquidation close short`102`: Partial liquidation buy`103`: Partial liquidation sell`104`: Liquidation long`105`: Liquidation short`106`: Liquidation buy `107`: Liquidation sell `110`: Liquidation transfer in`111`: Liquidation transfer out `118`: System token conversion transfer in`119`: System token conversion transfer out `112`: Delivery long `113`: Delivery short `125`: ADL close long`126`: ADL close short`127`: ADL buy`128`: ADL sell `212`: Auto borrow of quick margin`213`: Auto repay of quick margin `204`: block trade buy`205`: block trade sell`206`: block trade open long`207`: block trade open short`208`: block trade close long`209`: block trade close short`236`: Easy convert in`237`: Easy convert out`270`: Spread trading buy`271`: Spread trading sell`272`: Spread trading open long`273`: Spread trading open short`274`: Spread trading close long`275`: Spread trading close short `324`: Move position buy `325`: Move position sell `326`: Move position open long `327`: Move position open short `328`: Move position close long `329`: Move position close short `376`: Collateralized borrowing auto conversion buy`377`: Collateralized borrowing auto conversion sell`410`: Buy yes`411`: Buy no`412`: Sell yes`413`: Sell no`414`: Yes expiry`415`: No expiry |
| after | String | No | Pagination of data to return records earlier than the requested `billId` |
| before | String | No | Pagination of data to return records newer than the requested `billId` |
| begin | String | No | Filter with a begin timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | Filter with an end timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "side": "buy",
 "fillSz": "0.00192834",
 "fillPx": "51858",
 "fillPxVol": "",
 "fillFwdPx": "",
 "fee": "-0.00000192834",
 "fillPnl": "0",
 "ordId": "680800019749904384",
 "feeRate": "-0.001",
 "instType": "SPOT",
 "fillPxUsd": "",
 "instId": "BTC-USDT",
 "clOrdId": "",
 "posSide": "net",
 "billId": "680800019754098688",
 "subType": "1",
 "fillMarkVol": "",
 "tag": "",
 "fillTime": "1708587373361",
 "execType": "T",
 "fillIdxPx": "",
 "tradeId": "744876980",
 "fillMarkPx": "",
 "feeCcy": "BTC",
 "ts": "1708587373362",
 "tradeQuoteCcy": "USDT"
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
| tradeId | String | Last trade ID |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| billId | String | Bill ID |
| subType | String | Transaction type |
| tag | String | Order tag |
| fillPx | String | Last filled price. It is the same as the px from "Get bills details". |
| fillSz | String | Last filled quantity |
| fillIdxPx | String | Index price at the moment of trade execution For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT. |
| fillPnl | String | Realised P&L from this fill for close-position trades, denominated in the settlement currency (see `feeCcy`). Positive = realised gain; negative = realised loss. Formula: (fillPx − avgPx) × fillSz × ctVal (linear) or (1/avgPx − 1/fillPx) × fillSz × ctVal (inverse). Returns 0 for opening trades. |
| fillPxVol | String | Implied volatility when filled Only applicable to options; return "" for other instrument types |
| fillPxUsd | String | Options price when filled, in the unit of USD Only applicable to options; return "" for other instrument types |
| fillMarkVol | String | Mark volatility when filled Only applicable to options; return "" for other instrument types |
| fillFwdPx | String | Forward price when filled Only applicable to options; return "" for other instrument types |
| fillMarkPx | String | Mark price when filled Applicable to `FUTURES`, `SWAP`, `OPTION` |
| side | String | Order side, `buy` `sell` |
| posSide | String | Position side `long` `short` it returns `net` in`net` mode. |
| execType | String | Liquidity taker or maker`T`: taker`M`: makerNot applicable to system orders such as ADL and liquidation |
| feeCcy | String | Trading fee or rebate currency |
| fee | String | The amount of trading fee or rebate. The trading fee deduction is negative, such as '-0.01'; the rebate is positive, such as '0.01'. |
| ts | String | Timestamp when this fill record was generated by the system, in Unix milliseconds (UTC). Note: this differs from `fillTime`, which is the actual trade execution time. For chronological ordering of trades, sort by `fillTime`, not `ts`. |
| fillTime | String | Trade time which is the same as `fillTime` for the order channel. |
| feeRate | String | Fee rate. This field is returned for `SPOT` and `MARGIN` only |
| tradeQuoteCcy | String | The quote currency for trading. |

tradeId
For partial_liquidation, full_liquidation, or adl, when it comes to fill information, this field will be assigned a negative value to distinguish it from other matching transaction scenarios, when it comes to order information, this field will be 0.

ordId
Order ID, always "" for block trading.

clOrdId
Client-supplied order ID, always "" for block trading.

### GET / Transaction details (last 3 months)

This endpoint can retrieve data from the last 3 months.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/fills-history`

Request Example

```
GET /api/v5/trade/fills-history?instType=SPOT
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Retrieve SPOT transaction details in the last 3 months.
result = tradeAPI.get_fills_history(
 instType="SPOT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | YES | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |
| ordId | String | No | Order ID |
| subType | String | No | Transaction type `1`: Buy`2`: Sell`3`: Open long`4`: Open short`5`: Close long`6`: Close short `100`: Partial liquidation close long`101`: Partial liquidation close short`102`: Partial liquidation buy`103`: Partial liquidation sell`104`: Liquidation long`105`: Liquidation short`106`: Liquidation buy `107`: Liquidation sell `110`: Liquidation transfer in`111`: Liquidation transfer out `118`: System token conversion transfer in`119`: System token conversion transfer out `112`: Delivery long `113`: Delivery short `125`: ADL close long`126`: ADL close short`127`: ADL buy`128`: ADL sell `212`: Auto borrow of quick margin`213`: Auto repay of quick margin `204`: block trade buy`205`: block trade sell`206`: block trade open long`207`: block trade open short`208`: block trade close long`209`: block trade close short`236`: Easy convert in`237`: Easy convert out`270`: Spread trading buy`271`: Spread trading sell`272`: Spread trading open long`273`: Spread trading open short`274`: Spread trading close long`275`: Spread trading close short `324`: Move position buy `325`: Move position sell `326`: Move position open long `327`: Move position open short `328`: Move position close long `329`: Move position close short `376`: Collateralized borrowing auto conversion buy`377`: Collateralized borrowing auto conversion sell`410`: Buy yes`411`: Buy no`412`: Sell yes`413`: Sell no`414`: Yes expiry`415`: No expiry |
| after | String | No | Pagination of data to return records earlier than the requested `billId` |
| before | String | No | Pagination of data to return records newer than the requested `billId` |
| begin | String | No | Filter with a begin timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | Filter with an end timestamp `ts`. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "side": "buy",
 "fillSz": "0.00192834",
 "fillPx": "51858",
 "fillPxVol": "",
 "fillFwdPx": "",
 "fee": "-0.00000192834",
 "fillPnl": "0",
 "ordId": "680800019749904384",
 "feeRate": "-0.001",
 "instType": "SPOT",
 "fillPxUsd": "",
 "instId": "BTC-USDT",
 "clOrdId": "",
 "posSide": "net",
 "billId": "680800019754098688",
 "subType": "1",
 "fillMarkVol": "",
 "tag": "",
 "fillTime": "1708587373361",
 "execType": "T",
 "fillIdxPx": "",
 "tradeId": "744876980",
 "fillMarkPx": "",
 "feeCcy": "BTC",
 "ts": "1708587373362",
 "tradeQuoteCcy": "USDT"
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
| tradeId | String | Last trade ID |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| billId | String | Bill ID |
| subType | String | Transaction type |
| tag | String | Order tag |
| fillPx | String | Last filled price |
| fillSz | String | Last filled quantity |
| fillIdxPx | String | Index price at the moment of trade execution For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT. |
| fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| fillPxVol | String | Implied volatility when filled Only applicable to options; return "" for other instrument types |
| fillPxUsd | String | Options price when filled, in the unit of USD Only applicable to options; return "" for other instrument types |
| fillMarkVol | String | Mark volatility when filled Only applicable to options; return "" for other instrument types |
| fillFwdPx | String | Forward price when filled Only applicable to options; return "" for other instrument types |
| fillMarkPx | String | Mark price when filled Applicable to `FUTURES`, `SWAP`, `OPTION` |
| side | String | Order side`buy``sell` |
| posSide | String | Position side`long``short`it returns `net` in`net` mode. |
| execType | String | Liquidity taker or maker`T`: taker`M`: makerNot applicable to system orders such as ADL and liquidation |
| feeCcy | String | Trading fee or rebate currency |
| fee | String | The amount of trading fee or rebate. The trading fee deduction is negative, such as '-0.01'; the rebate is positive, such as '0.01'. |
| ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |
| fillTime | String | Trade time which is the same as `fillTime` for the order channel. |
| feeRate | String | Fee rate. This field is returned for `SPOT` and `MARGIN` only |
| tradeQuoteCcy | String | The quote currency for trading. |

tradeId
When the order category to which the transaction details belong is partial_liquidation, full_liquidation, or adl, this field will be assigned a negative value to distinguish it from other matching transaction scenarios.

ordId
Order ID, always "" for block trading.

clOrdId
Client-supplied order ID, always "" for block trading.

We advise you to use Get Transaction details (last 3 days)when you request data for recent 3 days.

### GET / Easy convert currency list

Get list of small convertibles and mainstream currencies. Only applicable to the crypto balance less than $10.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/easy-convert-currency-list`

Request Example

```
GET /api/v5/trade/easy-convert-currency-list
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Get list of small convertibles and mainstream currencies
result = tradeAPI.get_easy_convert_currency_list()
print(result)
```

#### Request Parameters

| Parameters | Type | Required | Description |
| --- | --- | --- | --- |
| source | String | No | Funding source`1`: Trading account`2`: Funding accountThe default is `1`. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "fromData": [
 {
 "fromAmt": "6.580712708344864",
 "fromCcy": "ADA"
 },
 {
 "fromAmt": "2.9970000013055097",
 "fromCcy": "USDC"
 }
 ],
 "toCcy": [
 "USDT",
 "BTC",
 "ETH",
 "OKB"
 ]
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| fromData | Array of objects | Currently owned and convertible small currency list |
| > fromCcy | String | Type of small payment currency convert from, e.g. `BTC` |
| > fromAmt | String | Amount of small payment currency convert from |
| toCcy | Array of strings | Type of mainstream currency convert to, e.g. `USDT` |

### POST / Place easy convert

Convert small currencies to mainstream currencies.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/easy-convert`

Request Example

```
POST /api/v5/trade/easy-convert
body
{
 "fromCcy": ["ADA","USDC"], //Seperated by commas
 "toCcy": "OKB"
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

# Convert small currencies to mainstream currencies
result = tradeAPI.easy_convert(
 fromCcy=["ADA", "USDC"],
 toCcy="OKB"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| fromCcy | Array of strings | Yes | Type of small payment currency convert from Maximum 5 currencies can be selected in one order. If there are multiple currencies, separate them with commas. |
| toCcy | String | Yes | Type of mainstream currency convert to Only one receiving currency type can be selected in one order and cannot be the same as the small payment currencies. |
| source | String | No | Funding source`1`: Trading account`2`: Funding accountThe default is `1`. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "fillFromSz": "6.5807127",
 "fillToSz": "0.17171580105126",
 "fromCcy": "ADA",
 "status": "running",
 "toCcy": "OKB",
 "uTime": "1661419684687"
 },
 {
 "fillFromSz": "2.997",
 "fillToSz": "0.1683755161661844",
 "fromCcy": "USDC",
 "status": "running",
 "toCcy": "OKB",
 "uTime": "1661419684687"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| status | String | Current status of easy convert `running`: Running `filled`: Filled `failed`: Failed |
| fromCcy | String | Type of small payment currency convert from |
| toCcy | String | Type of mainstream currency convert to |
| fillFromSz | String | Filled amount of small payment currency convert from |
| fillToSz | String | Filled amount of mainstream currency convert to |
| uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085 |

### GET / Easy convert history

Get the history and status of easy convert trades in the past 7 days.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/easy-convert-history`

Request Example

```
GET /api/v5/trade/easy-convert-history
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Get the history of easy convert trades
result = tradeAPI.get_easy_convert_history()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| after | String | No | Pagination of data to return records earlier than the requested time (exclude), Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested time (exclude), Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "fillFromSz": "0.1761712511667539",
 "fillToSz": "6.7342205900000000",
 "fromCcy": "OKB",
 "status": "filled",
 "toCcy": "ADA",
 "acct": "18",
 "uTime": "1661313307979"
 },
 {
 "fillFromSz": "0.1722106121112177",
 "fillToSz": "2.9971018300000000",
 "fromCcy": "OKB",
 "status": "filled",
 "toCcy": "USDC",
 "acct": "18",
 "uTime": "1661313307979"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| fromCcy | String | Type of small payment currency convert from |
| fillFromSz | String | Amount of small payment currency convert from |
| toCcy | String | Type of mainstream currency convert to |
| fillToSz | String | Amount of mainstream currency convert to |
| acct | String | The account where the mainstream currency is located`6`: Funding account `18`: Trading account |
| status | String | Current status of easy convert `running`: Running `filled`: Filled `failed`: Failed |
| uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / One-click repay currency list

Get list of debt currency data and repay currencies. Debt currencies include both cross and isolated debts. Only applicable to `Multi-currency margin`/`Portfolio margin`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-currency-list`

Request Example

```
GET /api/v5/trade/one-click-repay-currency-list
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Get list of debt currency data and repay currencies
result = tradeAPI.get_oneclick_repay_list()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| debtType | String | No | Debt type `cross`: cross `isolated`: isolated |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "debtData": [
 {
 "debtAmt": "29.653478",
 "debtCcy": "LTC"
 },
 {
 "debtAmt": "237803.6828295906051002",
 "debtCcy": "USDT"
 }
 ],
 "debtType": "cross",
 "repayData": [
 {
 "repayAmt": "0.4978335419825104",
 "repayCcy": "ETH"
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
| debtData | Array of objects | Debt currency data list |
| > debtCcy | String | Debt currency |
| > debtAmt | String | Debt currency amount Including principal and interest |
| debtType | String | Debt type `cross`: cross `isolated`: isolated |
| repayData | Array of objects | Repay currency data list |
| > repayCcy | String | Repay currency |
| > repayAmt | String | Repay currency's available balance amount |

### POST / Trade one-click repay

Trade one-click repay to repay cross debts. Isolated debts are not applicable.
The maximum repayment amount is based on the remaining available balance of funding and trading accounts.
Only applicable to `Multi-currency margin`/`Portfolio margin`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/one-click-repay`

Request Example

```
POST /api/v5/trade/one-click-repay
body
{
 "debtCcy": ["ETH","BTC"],
 "repayCcy": "USDT"
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

# Trade one-click repay to repay cross debts
result = tradeAPI.oneclick_repay(
 debtCcy=["ETH", "BTC"],
 repayCcy="USDT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| debtCcy | Array of strings | Yes | Debt currency type Maximum 5 currencies can be selected in one order. If there are multiple currencies, separate them with commas. |
| repayCcy | String | Yes | Repay currency type Only one receiving currency type can be selected in one order and cannot be the same as the small payment currencies. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "debtCcy": "ETH",
 "fillDebtSz": "0.01023052",
 "fillRepaySz": "30",
 "repayCcy": "USDT",
 "status": "filled",
 "uTime": "1646188520338"
 },
 {
 "debtCcy": "BTC",
 "fillFromSz": "3",
 "fillToSz": "60,221.15910001",
 "repayCcy": "USDT",
 "status": "filled",
 "uTime": "1646188520338"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| status | String | Current status of one-click repay `running`: Running `filled`: Filled `failed`: Failed |
| debtCcy | String | Debt currency type |
| repayCcy | String | Repay currency type |
| fillDebtSz | String | Filled amount of debt currency |
| fillRepaySz | String | Filled amount of repay currency |
| uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085 |

### GET / One-click repay history

Get the history and status of one-click repay trades in the past 7 days. Only applicable to `Multi-currency margin`/`Portfolio margin`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-history`

Request Example

```
GET /api/v5/trade/one-click-repay-history
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)

# Get the history of one-click repay trades
result = tradeAPI.oneclick_repay_history()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| after | String | No | Pagination of data to return records earlier than the requested time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| before | String | No | Pagination of data to return records newer than the requested time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "debtCcy": "USDC",
 "fillDebtSz": "6950.4865447900000000",
 "fillRepaySz": "4.3067975995094930",
 "repayCcy": "ETH",
 "status": "filled",
 "uTime": "1661256148746"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| debtCcy | String | Debt currency type |
| fillDebtSz | String | Amount of debt currency transacted |
| repayCcy | String | Repay currency type |
| fillRepaySz | String | Amount of repay currency transacted |
| status | String | Current status of one-click repay `running`: Running `filled`: Filled `failed`: Failed |
| uTime | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085 |

### GET / One-click repay currency list (New)

Get list of debt currency data and repay currencies. Only applicable to `SPOT mode`/`Multi-currency margin mode`/`Portfolio margin mode`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-currency-list-v2`

Request Example

```
GET /api/v5/trade/one-click-repay-currency-list-v2
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"
flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True)
result = tradeAPI.get_oneclick_repay_list_v2()
print(result)
```

Response Example

```
{
 "code": "0",
 "data": [
 {
 "debtData": [
 {
 "debtAmt": "100",
 "debtCcy": "USDC"
 }
 ],
 "repayData": [
 {
 "repayAmt": "1.000022977",
 "repayCcy": "BTC"
 },
 {
 "repayAmt": "4998.0002397",
 "repayCcy": "USDT"
 },
 {
 "repayAmt": "100",
 "repayCcy": "OKB"
 },
 {
 "repayAmt": "1",
 "repayCcy": "ETH"
 },
 {
 "repayAmt": "100",
 "repayCcy": "USDC"
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
| debtData | Array of objects | Debt currency data list |
| > debtCcy | String | Debt currency |
| > debtAmt | String | Debt currency amountIncluding principal and interest |
| repayData | Array of objects | Repay currency data list |
| > repayCcy | String | Repay currency |
| > repayAmt | String | Repay currency's available balance amount |

### POST / Trade one-click repay (New)

Trade one-click repay to repay debts. Only applicable to `SPOT mode`/`Multi-currency margin mode`/`Portfolio margin mode`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/one-click-repay-v2`

Request Example

```
POST /api/v5/trade/one-click-repay-v2
body
{
 "debtCcy": "USDC",
 "repayCcyList": ["USDC","BTC"]
}
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"
flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag,debug=True)
result = tradeAPI.oneclick_repay_v2("USDC",["USDC","BTC"])
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| debtCcy | String | Yes | Debt currency |
| repayCcyList | Array of strings | Yes | Repay currency list, e.g. ["USDC","BTC"]The priority of currency to repay is consistent with the order in the array. (The first item has the highest priority) |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "debtCcy": "USDC",
 "repayCcyList": [
 "USDC",
 "BTC"
 ],
 "ts": "1742192217514"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| debtCcy | String | Debt currency |
| repayCcyList | Array of strings | Repay currency list, e.g. ["USDC","BTC"] |
| ts | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / One-click repay history (New)

Get the history and status of one-click repay trades in the past 7 days. Only applicable to `SPOT mode`.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/trade/one-click-repay-history-v2`

Request Example

```
GET /api/v5/trade/one-click-repay-history-v2
```

```
import okx.Trade as Trade

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"
flag = "1" # Production trading: 0, Demo trading: 1

tradeAPI = Trade.TradeAPI(apikey, secretkey, passphrase, False, flag)
result = tradeAPI.oneclick_repay_history_v2()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| after | String | No | Pagination of data to return records earlier than (included) the requested time `ts` , Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than (included) the requested time `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "debtCcy": "USDC",
 "fillDebtSz": "9.079631989",
 "ordIdInfo": [
 {
 "cTime": "1742194485439",
 "fillPx": "1",
 "fillSz": "9.088651",
 "instId": "USDC-USDT",
 "ordId": "2338478342062235648",
 "ordType": "ioc",
 "px": "1.0049",
 "side": "buy",
 "state": "filled",
 "sz": "9.0886514537313433"
 },
 {
 "cTime": "1742194482326",
 "fillPx": "83271.9",
 "fillSz": "0.00010969",
 "instId": "BTC-USDT",
 "ordId": "2338478237607288832",
 "ordType": "ioc",
 "px": "82856.7",
 "side": "sell",
 "state": "filled",
 "sz": "0.000109696512171"
 }
 ],
 "repayCcyList": [
 "USDC",
 "BTC"
 ],
 "status": "filled",
 "ts": "1742194481852"
 },
 {
 "debtCcy": "USDC",
 "fillDebtSz": "100",
 "ordIdInfo": [],
 "repayCcyList": [
 "USDC",
 "BTC"
 ],
 "status": "filled",
 "ts": "1742192217511"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| debtCcy | String | Debt currency |
| repayCcyList | Array of strings | Repay currency list, e.g. ["USDC","BTC"] |
| fillDebtSz | String | Amount of debt currency transacted |
| status | String | Current status of one-click repay `running`: Running `filled`: Filled `failed`: Failed |
| ordIdInfo | Array of objects | Order info |
| > ordId | String | Order ID |
| > instId | String | Instrument ID, e.g. `BTC-USDT` |
| > ordType | String | Order type`ioc`: Immediate-or-cancel order |
| > side | String | Side`buy``sell` |
| > px | String | Price |
| > sz | String | Quantity to buy or sell |
| > fillPx | String | Last filled price.If none is filled, it will return "". |
| > fillSz | String | Last filled quantity |
| > state | String | State`filled``canceled` |
| > cTime | String | Creation time for order, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| ts | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### POST / Mass cancel order

Cancel all the MMP pending orders of an instrument family.

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/mass-cancel`

Request Example

```
POST /api/v5/trade/mass-cancel
body
{
 "instType":"OPTION",
 "instFamily":"BTC-USD"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`OPTION` |
| instFamily | String | Yes | Instrument family |
| lockInterval | String | No | Lock interval(ms) The range should be [0, 10 000] The default is 0. You can set it as "0" if you want to unlock it immediately. Error 54008 will be returned when placing order during lock interval, it is different from 51034 which is thrown when MMP is triggered |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "result":true
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| result | Boolean | Result of the request `true`, `false` |

### POST / Cancel All After

Cancel all pending orders after the countdown timeout. Applicable to all trading symbols through order book (except Spread trading)

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID + tag

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/cancel-all-after`

Request Example

```
POST /api/v5/trade/cancel-all-after
{
 "timeOut":"60"
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

# Set cancel all after
result = tradeAPI.cancel_all_after(
 timeOut="10"
)

print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| timeOut | String | Yes | The countdown for order cancellation, with second as the unit.Range of value can be 0, [10, 120]. Setting timeOut to 0 disables Cancel All After. |
| tag | String | No | CAA order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "triggerTime":"1587971460",
 "tag":"",
 "ts":"1587971400"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| triggerTime | String | The time the cancellation is triggered.triggerTime=0 means Cancel All After is disabled. |
| tag | String | CAA order tag |
| ts | String | The time the request is received. |

Users are recommended to send heartbeat to the exchange every second. When the cancel all after is triggered, the trading engine will cancel orders on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies.

To use tag level CAA, first, users need to set tags for their orders using the `tag` request parameter in the placing orders endpoint. When calling the CAA endpoint, if the `tag` request parameter is not provided, the default will be to set CAA at the account level. In this case, all pending orders for all order book trading symbols under that sub-account will be cancelled when CAA triggers, consistent with the existing logic. If the `tag` request parameter is provided, CAA will be set at the order tag level. When triggered, only pending orders of order book trading symbols with the specified tag will be canceled, while orders with other tags or no tags will remain unaffected.

Users can run a maximum of 20 tag level CAAs simultaneously under the same sub-account. The system will only count live tag level CAAs. CAAs that have been triggered or revoked by the user will not be counted. The user will receive error code 51071 when exceeding the limit.

### GET / Account rate limit

Get account rate limit related information.

Only new order requests and amendment order requests will be counted towards this limit. For batch order requests consisting of multiple orders, each order will be counted individually.

For details, please refer to [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit)

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/account-rate-limit`

Request Example

```
# Get the account rate limit
GET /api/v5/trade/account-rate-limit
```

#### Request Parameters

None

Response Example

```
{
 "code":"0",
 "data":[
 {
 "accRateLimit":"2000",
 "fillRatio":"0.1234",
 "mainFillRatio":"0.1234",
 "nextAccRateLimit":"2000",
 "ts":"123456789000"
 }
 ],
 "msg":""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| fillRatio | String | Sub account fill ratio during the monitoring period. Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.If there has been no trading activity on the account in the past 7 days, `""` will be returned.If there is no executed volume during the monitoring period, `"0"` will be returned.If there is executed volume but no order operation count during the monitoring period, `"9999"` will be returned. |
| mainFillRatio | String | Master account aggregated fill ratio during the monitoring period. Applicable to users with trading fee tier >= VIP 5; other users will receive `""`.If there has been no trading activity on the account in the past 7 days, `""` will be returned.If there is no executed volume during the monitoring period, `"0"` will be returned. |
| accRateLimit | String | Current sub-account rate limit per 2 seconds |
| nextAccRateLimit | String | Expected sub-account rate limit (per 2 seconds) in the next monitoring period. Applicable to users with trading fee tier >= VIP 5; other users will receive `""`. |
| ts | String | Data update timestamp For users with trading fee tier >= VIP 5, the data will be generated daily at 08:00 am (UTC) For users with trading fee tier < VIP 5, the current timestamp will be returned. |

### POST / Order precheck

This endpoint is used to precheck the account information before and after placing the order.
Only applicable to `Multi-currency margin mode`, and `Portfolio margin mode`.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/trade/order-precheck`

Request Example

```
# place order for SPOT
POST /api/v5/trade/order-precheck
 body
 {
 "instId":"BTC-USDT",
 "tdMode":"cash",
 "clOrdId":"b15",
 "side":"buy",
 "ordType":"limit",
 "px":"2.15",
 "sz":"2"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| tdMode | String | Yes | Trade modeMargin mode `cross` `isolated`Non-Margin mode `cash``spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.) |
| side | String | Yes | Order side, `buy` `sell` |
| posSide | String | Conditional | Position side The default is `net` in the `net` mode It is required in the `long/short` mode, and can only be `long` or `short`. Only applicable to `FUTURES`/`SWAP`. |
| ordType | String | Yes | Order type `market`: Market order `limit`: Limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures). `elp`: Enhanced Liquidity Program order |
| sz | String | Yes | Quantity to buy or sell |
| px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order. |
| outcome | String | Conditional | The market outcome users trade on.`yes``no`Only applicable and required for `EVENTS` |
| reduceOnly | Boolean | No | Whether orders can only reduce in position size. Valid options: `true` or `false`. The default value is `false`.Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode Only applicable to `Futures mode` and `Multi-currency margin` |
| tgtCcy | String | No | Whether the target currency uses the quote or base currency.`base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| attachAlgoOrds | Array of objects | No | Attached TP/SL or trailing stop order information |
| > attachAlgoClOrdId | String | No | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| > tpTriggerPx | String | Conditional | Take-profit trigger priceFor condition TP order, if you fill in this parameter, you should fill in the take-profit order price as well. |
| > tpOrdPx | String | Conditional | Take-profit order price For condition TP order, if you fill in this parameter, you should fill in the take-profit trigger price as well. For limit TP order, you need to fill in this parameter, take-profit trigger needn‘t to be filled. If the price is -1, take-profit will be executed at the market price. |
| > tpOrdKind | String | No | TP order kind`condition``limit` The default is `condition` |
| > slTriggerPx | String | Conditional | Stop-loss trigger priceIf you fill in this parameter, you should fill in the stop-loss order price. |
| > slOrdPx | String | Conditional | Stop-loss order priceIf you fill in this parameter, you should fill in the stop-loss trigger price.If the price is -1, stop-loss will be executed at the market price. |
| > tpTriggerPxType | String | No | Take-profit trigger price type`last`: last price `index`: index price `mark`: mark price The default is last |
| > slTriggerPxType | String | No | Stop-loss trigger price type`last`: last price `index`: index price `mark`: mark price The default is last |
| > sz | String | Conditional | Size. Only applicable to TP order of split TPs, and it is required for TP order of split TPs |
| > callbackRatio | String | Conditional | Callback ratio, e.g. `0.05` represents 5%.Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > callbackSpread | String | Conditional | Callback spread (price distance).Either `callbackRatio` or `callbackSpread` is required. Only one can be passed.Only applicable when `ordType` = `move_order_stop` |
| > activePx | String | No | Activation price.The trailing stop is activated when the market price reaches the activation price. After activation, the system starts calculating the actual trigger price. If not provided, the trailing stop is activated immediately upon order placement.Only applicable when `ordType` = `move_order_stop` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "adjEq": "41.94347460746277",
 "adjEqChg": "-226.05616481626",
 "availBal": "0",
 "availBalChg": "0",
 "imr": "0",
 "imrChg": "57.74709688430927",
 "liab": "0",
 "liabChg": "0",
 "liabChgCcy": "",
 "liqPx": "6764.8556232031115",
 "liqPxDiff": "-57693.044376796888536773622035980224609375",
 "liqPxDiffRatio": "-0.8950500152315991",
 "mgnRatio": "0",
 "mgnRatioChg": "0",
 "mmr": "0",
 "mmrChg": "0",
 "posBal": "",
 "posBalChg": "",
 "type": ""
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| adjEq | String | Current adjusted / Effective equity in `USD` |
| adjEqChg | String | After placing order, changed quantity of adjusted / Effective equity in `USD` |
| imr | String | Current initial margin requirement in `USD` |
| imrChg | String | After placing order, changed quantity of initial margin requirement in `USD` |
| mmr | String | Current Maintenance margin requirement in `USD` |
| mmrChg | String | After placing order, changed quantity of maintenance margin requirement in `USD` |
| mgnRatio | String | Current Maintenance margin ratio in `USD` |
| mgnRatioChg | String | After placing order, changed quantity of Maintenance margin ratio in `USD` |
| availBal | String | Current available balance in margin coin currency, only applicable to turn auto borrow off |
| availBalChg | String | After placing order, changed quantity of available balance after placing order, only applicable to turn auto borrow off |
| liqPx | String | Current estimated liquidation price |
| liqPxDiff | String | After placing order, the distance between estimated liquidation price and mark price |
| liqPxDiffRatio | String | After placing order, the distance rate between estimated liquidation price and mark price |
| posBal | String | Current positive asset, only applicable to margin isolated position |
| posBalChg | String | After placing order, positive asset of margin isolated, only applicable to margin isolated position |
| liab | String | Current liabilities of currency For cross, it is cross liabilitiesFor isolated position, it is isolated liabilities |
| liabChg | String | After placing order, changed quantity of liabilities For cross, it is cross liabilitiesFor isolated position, it is isolated liabilities |
| liabChgCcy | String | After placing order, the unit of changed liabilities quantity only applicable cross and in auto borrow |
| type | String | Unit type of positive asset, only applicable to margin isolated position`1`: it is both base currency before and after placing order `2`: before plaing order, it is base currency. after placing order, it is quota currency.`3`: before plaing order, it is quota currency. after placing order, it is base currency `4`: it is both quota currency before and after placing order |

### WS / Order channel

Retrieve order information. Data will not be pushed when first subscribed. Data will only be pushed when there are new orders or order updates.

Concurrent connection to this channel will be restricted by the following rules: [WebSocket connection count limit](/docs-v5/en/#overview-websocket-connection-count-limit).

#### URL Path

/ws/v5/private (required login)

Request Example : single

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "orders",
 "instType": "FUTURES",
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
 url = "wss://ws.okx.com:8443/ws/v5/private",
 useServerTime=False
 )
 await ws.start()
 args = [
 {
 "channel": "orders",
 "instType": "FUTURES",
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
 "channel": "orders",
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
 url = "wss://ws.okx.com:8443/ws/v5/private",
 useServerTime=False
 )
 await ws.start()
 args =[
 {
 "channel": "orders",
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
| > channel | String | Yes | Channel name`orders` |
| > instType | String | Yes | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS``ANY` |
| > instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > instId | String | No | Instrument ID |

Successful Response Example : single

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "orders",
 "instType": "FUTURES",
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
 "channel": "orders",
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"orders\", \"instType\" : \"FUTURES\"}]}",
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
| > instType | String | Yes | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS``ANY` |
| > instFamily | String | No | Instrument family |
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "orders",
 "instType": "SPOT",
 "instId": "BTC-USDT",
 "uid": "614488474791936"
 },
 "data": [
 {
 "accFillSz": "0.001",
 "algoClOrdId": "",
 "algoId": "",
 "amendResult": "",
 "amendSource": "",
 "avgPx": "31527.1",
 "cancelSource": "",
 "category": "normal",
 "ccy": "",
 "clOrdId": "",
 "code": "0",
 "cTime": "1654084334977",
 "execType": "M",
 "fee": "-0.02522168",
 "feeCcy": "USDT",
 "fillFee": "-0.02522168",
 "fillFeeCcy": "USDT",
 "fillNotionalUsd": "31.50818374",
 "fillPx": "31527.1",
 "fillSz": "0.001",
 "fillPnl": "0.01",
 "fillTime": "1654084353263",
 "fillPxVol": "",
 "fillPxUsd": "",
 "fillMarkVol": "",
 "fillFwdPx": "",
 "fillMarkPx": "",
 "fillIdxPx": "",
 "instId": "BTC-USDT",
 "instType": "SPOT",
 "lever": "0",
 "msg": "",
 "notionalUsd": "31.50818374",
 "ordId": "452197707845865472",
 "ordType": "limit",
 "pnl": "0",
 "posSide": "",
 "px": "31527.1",
 "pxUsd":"",
 "pxVol":"",
 "pxType":"",
 "quickMgnType": "",
 "rebate": "0",
 "rebateCcy": "BTC",
 "reduceOnly": "false",
 "reqId": "",
 "side": "sell",
 "attachAlgoClOrdId": "",
 "slOrdPx": "",
 "slTriggerPx": "",
 "slTriggerPxType": "last",
 "source": "",
 "state": "filled",
 "stpId": "",
 "stpMode": "",
 "sz": "0.001",
 "tag": "",
 "tdMode": "cash",
 "tgtCcy": "",
 "tpOrdPx": "",
 "tpTriggerPx": "",
 "tpTriggerPxType": "last",
 "attachAlgoOrds": [],
 "tradeId": "242589207",
 "tradeQuoteCcy": "USDT",
 "lastPx": "38892.2",
 "uTime": "1654084353264",
 "isTpLimit": "false",
 "linkedAlgoOrd": {
 "algoId": ""
 }
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > instType | String | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| > instFamily | String | Instrument family |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``EVENTS` |
| > instId | String | Instrument ID |
| > tgtCcy | String | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market orders. Default is `quote_ccy` for buy, `base_ccy` for sell |
| > ccy | String | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`, `FUTURES` and `SWAP` contracts. |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > px | String | Price For options, use coin as unit (e.g. BTC, ETH) |
| > pxUsd | String | Options price in USDOnly applicable to options; return "" for other instrument types |
| > pxVol | String | Implied volatility of the options orderOnly applicable to options; return "" for other instrument types |
| > pxType | String | Price type of options `px`: Place an order based on price, in the unit of coin (the unit for the request parameter px is BTC or ETH) `pxVol`: Place an order based on pxVol `pxUsd`: Place an order based on pxUsd, in the unit of USD (the unit for the request parameter px is USD) |
| > sz | String | Quantity to buy or sell |
| > notionalUsd | String | Estimated national value in `USD` of order |
| > ordType | String | Order type `market`: market order `limit`: limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures)`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode). `op_fok`: Simple options (fok) `elp`: Enhanced Liquidity Program order |
| > side | String | Order side, `buy` `sell` |
| > posSide | String | Position side `net` `long` or `short` Only applicable to `FUTURES`/`SWAP` |
| > tdMode | String | Trade mode, `cross`: cross `isolated`: isolated `cash`: cash |
| > fillPx | String | Filled price for the current update. |
| > tradeId | String | Trade ID for the current update. |
| > fillSz | String | Filled quantity for the current udpate. The unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC; For market orders, the unit both is `base_ccy` when the tgtCcy is `base_ccy` or `quote_ccy`;The unit is contract for `FUTURES`/`SWAP`/`OPTION` |
| > fillPnl | String | Filled profit and loss for the current udpate, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| > fillTime | String | Filled time for the current udpate. |
| > fillFee | String | Filled fee amount or rebate amount for the current udpate. : Negative number represents the user transaction fee charged by the platform; Positive number represents rebate |
| > fillFeeCcy | String | Filled fee currency or rebate currency for the current udpate..It is fee currency when fillFee is less than 0; It is rebate currency when fillFee>=0. |
| > fillPxVol | String | Implied volatility when filled Only applicable to options; return "" for other instrument types |
| > fillPxUsd | String | Options price when filled, in the unit of USD Only applicable to options; return "" for other instrument types |
| > fillMarkVol | String | Mark volatility when filled Only applicable to options; return "" for other instrument types |
| > fillFwdPx | String | Forward price when filled Only applicable to options; return "" for other instrument types |
| > fillMarkPx | String | Mark price when filled Applicable to `FUTURES`, `SWAP`, `OPTION` |
| > fillIdxPx | String | Index price at the moment of trade execution For cross currency spot pairs, it returns baseCcy-USDT index price. For example, for LTC-ETH, this field returns the index price of LTC-USDT. |
| > execType | String | Liquidity taker or maker for the current update, T: taker M: maker |
| > accFillSz | String | Accumulated fill quantityThe unit is `base_ccy` for SPOT and MARGIN, e.g. BTC-USDT, the unit is BTC; For market orders, the unit both is `base_ccy` when the tgtCcy is `base_ccy` or `quote_ccy`;The unit is contract for `FUTURES`/`SWAP`/`OPTION` |
| > fillNotionalUsd | String | Filled notional value in `USD` of order |
| > avgPx | String | Average filled price. If none is filled, it will return `0`. |
| > state | String | Order state `canceled``live` `partially_filled` `filled``mmp_canceled` |
| > lever | String | Leverage, from `0.01` to `125`. Only applicable to `MARGIN/FUTURES/SWAP` |
| > attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stop. |
| > tpTriggerPx | String | Take-profit trigger price, it |
| > tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > tpOrdPx | String | Take-profit order price, it |
| > slTriggerPx | String | Stop-loss trigger price, it |
| > slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| > slOrdPx | String | Stop-loss order price, it |
| > attachAlgoOrds | Array of objects | Attached TP/SL or trailing stop order information |
| >> attachAlgoId | String | The order ID of the attached TP/SL or trailing stop order. It can be used to identify the attached order when amending. It will not be posted to algoId when placing the attached algo order after the general order is filled completely. |
| >> attachAlgoClOrdId | String | Client-supplied Algo ID when placing order with attached TP/SL or trailing stopA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.It will be posted to `algoClOrdId` when placing the attached algo order once the general order is filled completely. |
| >> tpOrdKind | String | TP order kind`condition``limit` |
| >> tpTriggerPx | String | Take-profit trigger price. |
| >> tpTriggerRatio | String | Take-profit trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts. |
| >> tpTriggerPxType | String | Take-profit trigger price type. `last`: last price`index`: index price`mark`: mark price |
| >> tpOrdPx | String | Take-profit order price. |
| >> slTriggerPx | String | Stop-loss trigger price. |
| >> slTriggerRatio | String | Stop-loss trigger ratio, 0.3 represents 30%. Only applicable to `FUTURES`/`SWAP` contracts. |
| >> slTriggerPxType | String | Stop-loss trigger price type. `last`: last price`index`: index price`mark`: mark price |
| >> slOrdPx | String | Stop-loss order price. |
| >> sz | String | Size. Only applicable to TP order of split TPs |
| >> amendPxOnTriggerType | String | Whether to enable Cost-price SL. Only applicable to SL order of split TPs. `0`: disable, the default value `1`: Enable |
| >> callbackRatio | String | Callback ratio, e.g. `0.05` represents 5% |
| >> callbackSpread | String | Callback spread (price distance) |
| >> activePx | String | Activation price |
| > linkedAlgoOrd | Object | Linked SL order detail, only applicable to TP limit order of one-cancels-the-other order(oco) |
| >> algoId | Object | Algo ID |
| > stpId | String | Self trade prevention IDReturn "" if self trade prevention is not applicable (Deprecated) |
| > stpMode | String | Self trade prevention mode |
| > feeCcy | String | Fee currencyFor maker sell orders of Spot and Margin, this represents the quote currency. For all other cases, it represents the currency in which fees are charged. |
| > fee | String | Fee amountFor Spot and Margin (excluding maker sell orders): accumulated fee charged by the platform, always negativeFor maker sell orders in Spot and Margin, Expiry Futures, Perpetual Futures and Options: accumulated fee and rebate (always in quote currency for maker sell orders in Spot and Margin) |
| > rebateCcy | String | Rebate currencyFor maker sell orders of Spot and Margin, this represents the base currency. For all other cases, it represents the currency in which rebates are paid. |
| > rebate | String | Rebate amount, only applicable to Spot and MarginFor maker sell orders: Accumulated fee and rebate amount in the unit of base currency.For all other cases, it represents the maker rebate amount, always positive, return "" if no rebate. |
| > pnl | String | Profit and loss (excluding the fee). applicable to orders which have a trade and aim to close position. It always is 0 in other conditions. For liquidation under cross margin mode, it will include liquidation penalties. |
| > source | String | Order source`6`: The normal order triggered by the `trigger order``7`:The normal order triggered by the `TP/SL order` `13`: The normal order triggered by the algo order`25`:The normal order triggered by the `trailing stop order``34`: The normal order triggered by the chase order |
| > cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are:`0`: Order canceled by system`1`: Order canceled by user`2`: Order canceled: Pre reduce-only order canceled, due to insufficient margin in user position`3`: Order canceled: Risk cancellation was triggered. Pending order was canceled due to insufficient maintenance margin ratio and forced-liquidation risk.`4`: Order canceled: Borrowings of crypto reached hard cap, order was canceled by system.`6`: Order canceled: ADL order cancellation was triggered. Pending order was canceled due to a low margin ratio and forced-liquidation risk. `7`: Order canceled: Futures contract delivery. `9`: Order canceled: Insufficient balance after funding fees deducted. `10`: Order canceled: Option contract expiration.`13`: Order canceled: FOK order was canceled due to incompletely filled.`14`: Order canceled: IOC order was partially canceled due to incompletely filled.`15`: Order canceled: The order price is beyond the limit`17`: Order canceled: Close order was canceled, due to the position was already closed at market price.`20`: Cancel all after triggered`21`: Order canceled: The TP/SL order was canceled because the position had been closed`22` Order canceled: Due to a better price was available for the order in the same direction, the current operation reduce-only order was automatically canceled `23` Order canceled: Due to a better price was available for the order in the same direction, the existing reduce-only order was automatically canceled`27`: Order canceled: Price limit verification failed because the price difference between counterparties exceeds 5% `31`: The post-only order will take liquidity in taker orders `32`: Self trade prevention `33`: The order exceeds the maximum number of order matches per taker order`36`: Your TP limit order was canceled because the corresponding SL order was triggered. `37`: Your TP limit order was canceled because the corresponding SL order was canceled. `38`: You have canceled market maker protection (MMP) orders. `39`: Your order was canceled because market maker protection (MMP) was triggered. `42`: Your order was canceled because the difference between the initial and current best bid or ask prices reached the maximum chase difference.`43`: Order cancelled because the buy order price is higher than the index price or the sell order price is lower than the index price.`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit. `45`: Order cancelled because ELP order price verification failed`46`: delta reducing cancel orders |
| > amendSource | String | Source of the order amendation. `1`: Order amended by user`2`: Order amended by user, but the order quantity is overriden by system due to reduce-only`3`: New order placed by user, but the order quantity is overriden by system due to reduce-only`4`: Order amended by system due to other pending orders`5`: Order modification due to changes in options px, pxVol, or pxUsd as a result of following variations. For example, when iv = 60, USD and px are anchored at iv = 60, the changes in USD or px lead to modification. |
| > category | String | Category `normal` `twap` `adl` `full_liquidation` `partial_liquidation``delivery` `ddh`: Delta dynamic hedge`auto_conversion` |
| > isTpLimit | String | Whether it is TP limit order. true or false |
| > uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > reqId | String | Client Request ID as assigned by the client for order amendment. "" will be returned if there is no order amendment. |
| > amendResult | String | The result of amending the order `-1`: failure `0`: success `1`: Automatic cancel (amendment request returned success but amendment subsequently failed then automatically canceled by the system) `2`: Automatic amendation successfully, only applicable to pxVol and pxUsd orders of Option.When amending the order through API and `cxlOnFail` is set to `true` in the order amendment request but the amendment is rejected, "" is returned. When amending the order through API, the order amendment acknowledgement returns success and the amendment subsequently failed, `-1` will be returned if `cxlOnFail` is set to `false`, `1` will be returned if `cxlOnFail` is set to `true`. When amending the order through Web/APP and the amendment failed, `-1` will be returned. |
| > reduceOnly | String | Whether the order can only reduce the position size. Valid options: `true` or `false`. |
| > quickMgnType | String | Quick Margin type, Only applicable to Quick Margin Mode of isolated margin`manual`, `auto_borrow`, `auto_repay` (Deprecated) |
| > algoClOrdId | String | Client-supplied Algo ID. There will be a value when algo order attaching `algoClOrdId` is triggered, or it will be "". |
| > algoId | String | Algo ID. There will be a value when algo order is triggered, or it will be "". |
| > lastPx | String | Last price |
| > code | String | Error Code, the default is 0 |
| > msg | String | Error Message, The default is "" |
| > tradeQuoteCcy | String | The quote currency used for trading. |
| > outcome | String | The market outcome the user traded on.`yes``no`Only applicable to `EVENTS` |


 For market orders, it's likely the orders channel will show order state as "filled" while showing the "last filled quantity (fillSz)" as 0.

In exceptional cases, the same message may be sent multiple times (perhaps with the different uTime) . The following guidelines are advised:

1. If a `tradeId` is present, it means a fill. Each `tradeId` should only be returned once per instrument ID, and the later messages that have the same `tradeId` should be discarded.
2. If `tradeId` is absent and the `state` is "filled," it means that the `SPOT`/`MARGIN` market order is fully filled. For messages with the same `ordId`, process only the first filled message and discard any subsequent messages. State = filled is the terminal state of an order.
3. If the state is `canceled` or `mmp_canceled`, it indicates that the order has been canceled. For cancellation messages with the same `ordId`, process the first one and discard later messages. State = canceled / mmp_canceled is the terminal state of an order.
4. If `reqId` is present, it indicates a response to a user-requested order modification. It is recommended to use a unique `reqId` for each modification request. For modification messages with the same `reqId`, process only the first message received and discard subsequent messages.

The definitions for fillPx, tradeId, fillSz, fillPnl, fillTime, fillFee, fillFeeCcy, and execType differ between the REST order information endpoints and the orders channel.

The definitions for fillPx, tradeId, fillSz, fillPnl, fillTime, fillFee, fillFeeCcy, and execType differ between the REST order information endpoints and the orders channel.

Unlike futures contracts, option positions are automatically exercised or expire at maturity. The rights then terminate and no closing orders are generated. Therefore, this channel will not push any closing-order updates for expired options.

### WS / Fills channel

Retrieve transaction information. Data will not be pushed when first subscribed. Data will only be pushed when there are order book fill events, where tradeId > 0.

The channel is exclusively available to users with trading fee tier VIP4 or above. Other users will receive error code 64003. For other users, please use [WS / Order channel](/docs-v5/en/#order-book-trading-trade-ws-order-channel).

For `EVENTS`, only data for the YES side is returned regardless of whether the actual order was placed on YES or NO.

#### URL Path

/ws/v5/private (required login)

Request Example: single

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "fills",
 "instId": "BTC-USDT-SWAP"
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
 url = "wss://ws.okx.com:8443/ws/v5/private",
 useServerTime=False
 )
 await ws.start()
 args = [
 {
 "channel": "fills",
 "instId": "BTC-USDT-SWAP"
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
 "channel": "fills"
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
 url = "wss://ws.okx.com:8443/ws/v5/private",
 useServerTime=False
 )
 await ws.start()
 args = [
 {
 "channel": "fills"
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
| > channel | String | Yes | Channel name `fills` |
| > instId | String | No | Instrument ID |

Successful Response Example: single

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "fills",
 "instId": "BTC-USDT-SWAP"
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
 "channel": "fills"
 },
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event `subscribe` `unsubscribe` `error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example: single

```
{
 "arg": {
 "channel": "fills",
 "instId": "BTC-USDT-SWAP",
 "uid": "614488474791111"
 },
 "data":[
 {
 "instId": "BTC-USDT-SWAP",
 "fillSz": "100",
 "fillPx": "70000",
 "side": "buy",
 "ts": "1705449605015",
 "ordId": "680800019749904384",
 "clOrdId": "1234567890",
 "tradeId": "12345",
 "execType": "T",
 "count": "10"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instId | String | Instrument ID |
| > fillSz | String | Filled quantity. If the trade is aggregated, the filled quantity will also be aggregated. |
| > fillPx | String | Last filled price |
| > side | String | Trade direction `buy` `sell` |
| > ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tradeId | String | The last trade ID in the trades aggregation |
| > execType | String | Liquidity taker or maker, `T`: taker `M`: maker |
| > count | String | The count of trades aggregated |


- The channel is exclusively available to users with trading fee tier VIP4 or above. Others will receive error code 64003 when subscribing to it.
- The channel only pushes partial information of the orders channel. Fill events of block trading, nitro spread, liquidation, ADL, and some other non order book events will not be pushed through this channel. Users should also subscribe to the orders channel for order confirmation.
- When a fill event is received by this channel, the account balance, margin, and position information might not have changed yet.
- Taker orders will be aggregated based on different fill prices. When aggregation occurs, the count field indicates the number of orders matched, and the tradeId represents the tradeId of the last trade in the aggregation. Maker orders will not be aggregated.
- The channel returns clOrdId. The field will be returned upon trade execution. Note that the fills channel will only return this field if the user-provided clOrdId conforms to the signed int64 positive integer format (1-9223372036854775807, 2^63-1); if the user does not provide this field or if clOrdId does not meet the format requirements, the field will return "0". The order endpoints and channel will continue to return the user-provided clOrdId as usual. All request and response parameters are of string type.
- In the future, connection limits will be imposed on this channel. The maximum number of connections subscribing to this channel per subaccount will be 20. We recommend users always use this channel within this limit to avoid any impact on their strategies when the limit is enforced.


### WS / Place order

You can place an order only if you have sufficient funds.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Rate limit is shared with the `Place order` REST API endpoints

Request Example

```
{
 "id": "1512",
 "op": "order",
 "args": [
 {
 "side": "buy",
 "instIdCode": 123456,
 "tdMode": "isolated",
 "ordType": "market",
 "sz": "100"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`order` |
| args | Array of objects | Yes | Request parameters |
| > instIdCode | Integer | 是 | Instrument ID code. |
| > tdMode | String | Yes | Trade mode Margin mode `isolated` `cross` Non-Margin mode `cash``spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.) Event contracts symbols only support `isolated` |
| > ccy | String | No | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`. |
| > clOrdId | String | No | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| > tag | String | No | Order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| > side | String | Yes | Order side, `buy` `sell` |
| > posSide | String | Conditional | Position side The default is `net` in the `net` mode It is required in the `long/short` mode, and can only be `long` or `short`. Only applicable to `FUTURES`/`SWAP`. |
| > ordType | String | Yes | Order type `market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP` `limit`: limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode)`elp`: Enhanced Liquidity Program order |
| > sz | String | Yes | Quantity to buy or sell. |
| > px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| > speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| > outcome | String | Conditional | The market outcome users trade on.`yes``no`Only applicable and required for `EVENTS` |
| > pxUsd | String | Conditional | Place options orders in `USD` Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| > pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100% Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| > reduceOnly | Boolean | No | Whether the order can only reduce the position size. Valid options: `true` or `false`. The default value is `false`.Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode Only applicable to `Futures mode` and `Multi-currency margin` |
| > tgtCcy | String | No | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| > banAmend | Boolean | No | Whether to disallow the system from amending the size of the SPOT Market Order.Valid options: `true` or `false`. The default value is `false`.If `true`, system will not amend and reject the market order if user does not have sufficient funds. Only applicable to SPOT Market Orders |
| > pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `px` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit The default value is `0` |
| > tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`. The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`. |
| > slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.If not specified or empty, defaults to `0.00%`.Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.Only applicable to `SPOT` and `SPOT margin` `market` orders. |
| > stpMode | String | No | Self trade prevention mode. `cancel_maker`,`cancel_taker`, `cancel_both`.Cancel both does not support FOK The account-level acctStpMode will be used to place orders. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order. |
| > isElpTakerAccess | Boolean | No | ELP taker access`true`: the request can trade with ELP orders but a speed bump will be applied`false`: the request cannot trade with ELP orders and no speed bumpThe default value is `false` while `true` is only applicable to ioc orders. |
| expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085` |

Successful Response Example

```
{
 "id": "1512",
 "op": "order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "12345689",
 "tag": "",
 "ts":"1695190491421",
 "sCode": "0",
 "sMsg": ""
 }
 ],
 "code": "0",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Failure Response Example

```
{
 "id": "1512",
 "op": "order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "",
 "tag": "",
 "ts":"1695190491421",
 "sCode": "5XXXX",
 "sMsg": "not exist"
 }
 ],
 "code": "1",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Format Error

```
{
 "id": "1512",
 "op": "order",
 "data": [],
 "code": "60013",
 "msg": "Invalid args",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Rejection or success message of event execution. |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` |
| outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

tdMode
Trade Mode, when placing an order, you need to specify the trade mode.
Spot mode:****- SPOT and OPTION buyer: cash
Futures mode:****- Isolated MARGIN: isolated
- Cross MARGIN: cross
- SPOT: cash
- Cross FUTURES/SWAP/OPTION: cross
- Isolated FUTURES/SWAP/OPTION: isolated
Multi-currency margin:****- Isolated MARGIN: isolated
- Cross SPOT: cross
- Cross FUTURES/SWAP/OPTION: cross
- Isolated FUTURES/SWAP/OPTION: isolated
Portfolio margin:****- Isolated MARGIN: isolated
- Cross SPOT: cross
- Cross FUTURES/SWAP/OPTION: cross
- Isolated FUTURES/SWAP/OPTION: isolated

clOrdId
clOrdId is a user-defined unique order identifier at the User ID level. If provided in the request parameters, it will be included in the response and can be used as a request parameter to query, cancel, and amend orders.
clOrdId cannot duplicate any existing clOrdId of all current pending orders.

posSide
Position side, this parameter is not mandatory in net** mode. If you pass it through, the only valid value is **net**.**In long/short** mode, it is mandatory. Valid values are **long** or **short**.**In long/short** mode, **side** and **posSide** need to be specified in the combinations below:

Open long: buy and open long (side: fill in buy; posSide: fill in long)

Open short: sell and open short (side: fill in sell; posSide: fill in short)

Close long: sell and close long (side: fill in sell; posSide: fill in long)

Close short: buy and close short (side: fill in buy; posSide: fill in short)

Portfolio margin mode: Expiry Futures and Perpetual Futures only support net mode

ordType

Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:

limit: Limit order, which requires specified sz and px.

market: Market order. For SPOT and MARGIN, market order will be filled with market price (by swiping opposite order book). For Expiry Futures and Perpetual Futures, market order will be placed to order book with most aggressive price allowed by Price Limit Mechanism. For OPTION, market order is not supported yet. As the filled price for market orders cannot be determined in advance, OKX reserves/freezes your quote currency by an additional 5% for risk check.

post_only: Post-only order, which the order can only provide liquidity to the market and be a maker. If the order would have executed on placement, it will be canceled instead.

fok: Fill or kill order. If the order cannot be fully filled, the order will be canceled. The order would not be partially filled.

ioc: Immediate or cancel order. Immediately execute the transaction at the order price, cancel the remaining unfilled quantity of the order, and the order quantity will not be displayed in the order book.

optimal_limit_ioc: Market order with ioc (immediate or cancel). Immediately execute the transaction of this market order, cancel the remaining unfilled quantity of the order, and the order quantity will not be displayed in the order book. Only applicable to Expiry Futures and Perpetual Futures.

sz

Quantity to buy or sell.

For SPOT/MARGIN Buy and Sell Limit Orders, it refers to the quantity in base currency.

For MARGIN Buy Market Orders, it refers to the quantity in quote currency.

For MARGIN Sell Market Orders, it refers to the quantity in base currency.

For SPOT Market Orders, it is set by tgtCcy.

For FUTURES/SWAP/OPTION orders, it refers to the number of contracts.

reduceOnly

When placing an order with this parameter set to true, it means that the order will reduce the size of the position only

For the same MARGIN instrument, the coin quantity of all reverse direction pending orders adds `sz` of new `reduceOnly` order cannot exceed the position assets. After the debt is paid off, if there is a remaining size of orders, the position will not be opened in reverse, but will be traded in SPOT.

For the same FUTURES/SWAP instrument, the sum of the current order size and all reverse direction reduce-only pending orders which's price-time priority is higher than the current order, cannot exceed the contract quantity of position.

Only applicable to `Futures mode` and `Multi-currency margin`

Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode

Notice: Under long/short mode of Expiry Futures and Perpetual Futures, all closing orders apply the reduce-only feature which is not affected by this parameter.

tgtCcy

This parameter is used to specify the order quantity in the order request is denominated in the quantity of base or quote currency. This is applicable to SPOT Market Orders only.

Base currency: base_ccy

Quote currency: quote_ccy

If you use the Base Currency quantity for buy market orders or the Quote Currency for sell market orders, please note:

1. If the quantity you enter is greater than what you can buy or sell, the system will execute the order according to your maximum buyable or sellable quantity. If you want to trade according to the specified quantity, you should use Limit orders.

2. When the market price is too volatile, the locked balance may not be sufficient to buy the Base Currency quantity or sell to receive the Quote Currency that you specified. We will change the quantity of the order to execute the order based on best effort principle based on your account balance. In addition, we will try to over lock a fraction of your balance to avoid changing the order quantity.

2.1 Example of base currency buy market order:

Taking the market order to buy 10 LTCs as an example, and the user can buy 11 LTC. At this time, if 10 3,000, the user's locked balance is not sufficient to buy using the specified amount of base currency, the user's maximum locked balance of 3,000 USDT will be used to settle the trade. Final transaction quantity becomes 3,000/400 = 7.5 LTC.

2.2 Example of quote currency sell market order:

Taking the market order to sell 1,000 USDT as an example, and the user can sell 1,200 USDT, 1,000

px

The value for px must be a multiple of tickSz for OPTION orders.

If not, the system will apply the rounding rules below. Using tickSz 0.0005 as an example:

The px will be rounded up to the nearest 0.0005 when the remainder of px to 0.0005 is more than 0.00025 or `px` is less than 0.0005.

The px will be rounded down to the nearest 0.0005 when the remainder of px to 0.0005 is less than 0.00025 and `px` is more than 0.0005.

Mandatory self trade prevention (STP)

The trading platform imposes mandatory self trade prevention at master account level, which means the accounts under the same master account, including master account itself and all its affiliated sub-accounts, will be prevented from self trade. The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order.

Mandatory self trade prevention will not lead to latency.

There are three STP modes. The STP mode is always taken based on the configuration in the taker order.

1. Cancel Maker: This is the default STP mode, which cancels the maker order to prevent self-trading. Then, the taker order continues to match with the next order based on the order book priority.

2. Cancel Taker: The taker order is canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled and then canceled. FOK orders are always honored and canceled if they would result in self-trading.

3. Cancel Both: Both taker and maker orders are canceled to prevent self-trading. If the user's own maker order is lower in the order book priority, the taker order is partially filled. Then, the remaining quantity of the taker order and the first maker order are canceled. FOK orders are not supported in this mode.

Rate limit of orders tagged as isElpTakerAccess:true

- 50 orders per 2 seconds per User ID per instrument ID.

- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket

### WS / Place multiple orders

Place orders in a batch. Maximum 20 orders can be placed per request

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Place order`.

Rate limit is shared with the `Place multiple orders` REST API endpoints

Request Example

```
{
 "id": "1513",
 "op": "batch-orders",
 "args": [
 {
 "side": "buy",
 "instIdCode": 123456,
 "tdMode": "cash",
 "ordType": "market",
 "sz": "100"
 },
 {
 "side": "buy",
 "instIdCode": 654321,
 "tdMode": "cash",
 "ordType": "market",
 "sz": "1"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`batch-orders` |
| args | Array of objects | Yes | Request Parameters |
| > instIdCode | Integer | Yes | Instrument ID code. |
| > tdMode | String | Yes | Trade mode Margin mode `isolated` `cross` Non-Margin mode `cash``spot_isolated` (only applicable to SPOT lead trading, `tdMode` should be `spot_isolated` for `SPOT` lead trading.)Note: `isolated` is not available in multi-currency margin mode and portfolio margin mode. Event contracts symbols only support `isolated` |
| > ccy | String | No | Margin currency Applicable to all `isolated` `MARGIN` orders and `cross` `MARGIN` orders in `Futures mode`. |
| > clOrdId | String | No | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| > tag | String | No | Order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| > side | String | Yes | Order side, `buy` `sell` |
| > posSide | String | Conditional | Position side The default `net` in the `net` mode It is required in the `long/short` mode, and only be `long` or `short`. Only applicable to `FUTURES`/`SWAP`. |
| > ordType | String | Yes | Order type `market`: Market order, only applicable to `SPOT/MARGIN/FUTURES/SWAP` `limit`: limit order `post_only`: Post-only order `fok`: Fill-or-kill order `ioc`: Immediate-or-cancel order `optimal_limit_ioc`: Market order with immediate-or-cancel order (applicable only to Expiry Futures and Perpetual Futures)`mmp`: Market Maker Protection (only applicable to Option in Portfolio Margin mode)`mmp_and_post_only`: Market Maker Protection and Post-only order(only applicable to Option in Portfolio Margin mode). `elp`: Enhanced Liquidity Program order |
| > sz | String | Yes | Quantity to buy or sell. |
| > px | String | Conditional | Order price. Only applicable to `limit`,`post_only`,`fok`,`ioc`,`mmp`,`mmp_and_post_only` order.When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| > speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| > outcome | String | Conditional | The market outcome users trade on.`yes``no`Only applicable and required for `EVENTS` |
| > pxUsd | String | Conditional | Place options orders in `USD` Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| > pxVol | String | Conditional | Place options orders based on implied volatility, where 1 represents 100% Only applicable to options When placing an option order, one of px/pxUsd/pxVol must be filled in, and only one can be filled in |
| > reduceOnly | Boolean | No | Whether the order can only reduce the position size. Valid options: `true` or `false`. The default value is `false`.Only applicable to `MARGIN` orders, and `FUTURES`/`SWAP` orders in `net` mode Only applicable to `Futures mode` and `Multi-currency margin` |
| > tgtCcy | String | No | Order quantity unit setting for `sz``base_ccy`: Base currency ,`quote_ccy`: Quote currency Only applicable to `SPOT` Market OrdersDefault is `quote_ccy` for buy, `base_ccy` for sell |
| > banAmend | Boolean | No | Whether to disallow the system from amending the size of the SPOT Market Order.Valid options: `true` or `false`. The default value is `false`.If `true`, system will not amend and reject the market order if user does not have sufficient funds. Only applicable to SPOT Market Orders |
| > pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `px` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `px` exceeds the price limit The default value is `0` |
| > tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to `SPOT`. The default value is the quote currency of the `instId`, for example: for `BTC-USD`, the default is `USD`. |
| > slippagePct | String | No | Maximum acceptable slippage for spot and spot margin market-side orders, where `tgtCcy` is the received currency (`base_ccy` for buy, `quote_ccy` for sell).Range: `0` to `0.05` (0% to 5%, inclusive). Up to 2 decimal places of the percentage, e.g., `0.01` (1%) and `0.0123` (1.23%) are accepted; `0.01234` (1.234%) is rejected.If not specified or empty, defaults to `0.00%`.Slippage cannot be modified on an existing order. Cancel and resubmit to change the slippage setting.Only applicable to `SPOT` and `SPOT margin` `market` orders. |
| > isElpTakerAccess | Boolean | No | ELP taker access`true`: the request can trade with ELP orders but a speed bump will be applied`false`: the request cannot trade with ELP orders and no speed bumpThe default value is `false` while `true` is only applicable to ioc orders. |
| > stpMode | String | No | Self trade prevention mode. `cancel_maker`,`cancel_taker`, `cancel_both`Cancel both does not support FOK. The account-level acctStpMode will be used to place orders by default. The default value of this field is `cancel_maker`. Users can log in to the webpage through the master account to modify this configuration. Users can also utilize the stpMode request parameter of the placing order endpoint to determine the stpMode of a certain order. |
| expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085` |

Response Example When All Succeed

```
{
 "id": "1513",
 "op": "batch-orders",
 "data": [
 {
 "clOrdId": "",
 "ordId": "12345689",
 "tag": "",
 "ts": "1695190491421",
 "sCode": "0",
 "sMsg": "",
 "subCode": ""
 },
 {
 "clOrdId": "",
 "ordId": "12344",
 "tag": "",
 "ts": "1695190491421",
 "sCode": "0",
 "sMsg": "",
 "subCode": ""
 }
 ],
 "code": "0",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Partially Successful

```
{
 "id": "1513",
 "op": "batch-orders",
 "data": [
 {
 "clOrdId": "",
 "ordId": "12345689",
 "tag": "",
 "ts": "1695190491421",
 "sCode": "0",
 "sMsg": "",
 "subCode": ""
 },
 {
 "clOrdId": "",
 "ordId": "",
 "tag": "",
 "ts": "1695190491421",
 "sCode": "51008",
 "sMsg": "Order failed. Insufficient USDT balance in account",
 "subCode": "1000"
 }
 ],
 "code": "2",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When All Failed

```
{
 "id": "1513",
 "op": "batch-orders",
 "data": [
 {
 "clOrdId": "oktswap6",
 "ordId": "",
 "tag": "",
 "ts": "1695190491421",
 "sCode": "51008",
 "sMsg": "Order failed. Insufficient USDT balance in account",
 "subCode": "1000"
 },
 {
 "clOrdId": "oktswap7",
 "ordId": "",
 "tag": "",
 "ts": "1695190491421",
 "sCode": "51008",
 "sMsg": "Order failed. Insufficient USDT balance in account",
 "subCode": "1000"
 }
 ],
 "code": "1",
 "msg": "",
 "subCode": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Format Error

```
{
 "id": "1513",
 "op": "batch-orders",
 "data": [],
 "code": "60013",
 "msg": "Invalid args",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Rejection or success message of event execution. |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` |
| outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

In the `Portfolio Margin` account mode, either all orders are accepted by the system successfully, or all orders are rejected by the system.

clOrdId

clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.

clOrdId must be unique among all pending orders and the current request.

Rate limit of orders tagged as isElpTakerAccess:true

- 50 orders per 2 seconds per User ID per instrument ID.

- This rate limit is shared in Place order/Place multiple orders endpoints in REST/WebSocket

### WS / Cancel order

Cancel an incomplete order

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit is shared with the `Cancel order` REST API endpoints

Request Example

```
{
 "id": "1514",
 "op": "cancel-order",
 "args": [
 {
 "instIdCode": 123456,
 "ordId": "2510789768709120"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`cancel-order` |
| args | Array of objects | Yes | Request Parameters |
| > instIdCode | Integer | Yes | Instrument ID code |
| > ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required, if both are passed, ordId will be used |
| > clOrdId | String | Conditional | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

Successful Response Example

```
{
 "id": "1514",
 "op": "cancel-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "ts": "1695190491421",
 "sCode": "0",
 "sMsg": ""
 }
 ],
 "code": "0",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Failure Response Example

```
{
 "id": "1514",
 "op": "cancel-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "ts": "1695190491421",
 "sCode": "5XXXX",
 "sMsg": "Order not exist"
 }
 ],
 "code": "1",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Format Error

```
{
 "id": "1514",
 "op": "cancel-order",
 "data": [],
 "code": "60013",
 "msg": "Invalid args",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Order status message |
| inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` |
| outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state.

### WS / Cancel multiple orders

Cancel incomplete orders in batches. Maximum 20 orders can be canceled per request.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 300 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Cancel order`.

Rate limit is shared with the `Cancel multiple orders` REST API endpoints

Request Example

```
{
 "id": "1515",
 "op": "batch-cancel-orders",
 "args": [
 {
 "instIdCode": 123456,
 "ordId": "2517748157541376"
 },
 {
 "instIdCode": 654321,
 "ordId": "2517748155771904"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`batch-cancel-orders` |
| args | Array of objects | Yes | Request Parameters |
| > instIdCode | Integer | Yes | Instrument ID code |
| > ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required, if both are passed, ordId will be used |
| > clOrdId | String | Conditional | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

Response Example When All Succeed

```
{
 "id": "1515",
 "op": "batch-cancel-orders",
 "data": [
 {
 "clOrdId": "oktswap6",
 "ordId": "2517748157541376",
 "ts": "1695190491421",
 "sCode": "0",
 "sMsg": ""
 },
 {
 "clOrdId": "oktswap7",
 "ordId": "2517748155771904",
 "ts": "1695190491421",
 "sCode": "0",
 "sMsg": ""
 }
 ],
 "code": "0",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When partially successfully

```
{
 "id": "1515",
 "op": "batch-cancel-orders",
 "data": [
 {
 "clOrdId": "oktswap6",
 "ordId": "2517748157541376",
 "ts": "1695190491421",
 "sCode": "0",
 "sMsg": ""
 },
 {
 "clOrdId": "oktswap7",
 "ordId": "2517748155771904",
 "ts": "1695190491421",
 "sCode": "5XXXX",
 "sMsg": "order not exist"
 }
 ],
 "code": "2",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When All Failed

```
{
 "id": "1515",
 "op": "batch-cancel-orders",
 "data": [
 {
 "clOrdId": "oktswap6",
 "ordId": "2517748157541376",
 "ts": "1695190491421",
 "sCode": "5XXXX",
 "sMsg": "order not exist"
 },
 {
 "clOrdId": "oktswap7",
 "ordId": "2517748155771904",
 "ts": "1695190491421",
 "sCode": "5XXXX",
 "sMsg": "order not exist"
 }
 ],
 "code": "1",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Format Error

```
{
 "id": "1515",
 "op": "batch-cancel-orders",
 "data": [],
 "code": "60013",
 "msg": "Invalid args",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Order status message |
| inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` |
| outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

### WS / Amend order

Amend an incomplete order.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 60 requests per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 requests per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Rate limit is shared with the `Amend order` REST API endpoints

Request Example

```
{
 "id": "1512",
 "op": "amend-order",
 "args": [
 {
 "instIdCode": 123456,
 "ordId": "2510789768709120",
 "newSz": "2"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`amend-order` |
| args | Array of objects | Yes | Request Parameters |
| > instIdCode | Integer | Yes | Instrument ID code |
| > cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails Valid options: `false` or `true`, the default is `false`. |
| > ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used. |
| > clOrdId | String | Conditional | Client Order ID as assigned by the client |
| > reqId | String | No | Client Request ID as assigned by the client for order amendment A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| > newSz | String | Conditional | New quantity after amendment and it has to be larger than 0. Either `newSz` or `newPx` is required. When amending a partially-filled order, the `newSz` should include the amount that has been filled. |
| > newPx | String | Conditional | New price after amendment. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order. |
| > speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| > newPxUsd | String | Conditional | Modify options orders using USD prices Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| > newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100% Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| > pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit The default value is `0` |
| expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085` |

Successful Response Example

```
{
 "id": "1512",
 "op": "amend-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "0",
 "sMsg": "",
 "subCode": ""
 }
 ],
 "code": "0",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Failure Response Example

```
{
 "id": "1512",
 "op": "amend-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "51008",
 "sMsg": "Order failed. Insufficient USDT balance in account",
 "subCode": "10000"
 }
 ],
 "code": "1",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Format Error

```
{
 "id": "1512",
 "op": "amend-order",
 "data": [],
 "code": "60013",
 "msg": "Invalid args",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > reqId | String | Client Request ID as assigned by the client for order amendment |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Order status message |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` |
| outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

newSz

If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled.

The amend order returns sCode equal to 0. It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query

### WS / Amend multiple orders

Amend incomplete orders in batches. Maximum 20 orders can be amended per request.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 300 orders per 2 seconds

#### Rate Limit of lead trader lead instruments for Copy Trading: 4 orders per 2 seconds

#### Rate limit rule (except Options): User ID + Instrument ID

#### Rate limit rule (Options only): User ID + Instrument Family

Rate limit of this endpoint will also be affected by the rules [Sub-account rate limit](/docs-v5/en/#overview-rate-limits-sub-account-rate-limit) and [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit).

Unlike other endpoints, the rate limit of this endpoint is determined by the number of orders. If there is only one order in the request, it will consume the rate limit of `Amend order`.

Rate limit is shared with the `Amend multiple orders` REST API endpoints

Request Example

```
{
 "id": "1513",
 "op": "batch-amend-orders",
 "args": [
 {
 "instIdCode": 123456,
 "ordId": "12345689",
 "newSz": "2"
 },
 {
 "instIdCode": 123456,
 "ordId": "12344",
 "newSz": "2"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`batch-amend-orders` |
| args | Array of objects | Yes | Request Parameters |
| > instIdCode | Integer | Yes | Instrument ID code |
| > cxlOnFail | Boolean | No | Whether the order needs to be automatically canceled when the order amendment fails Valid options: `false` or `true`, the default is `false`. |
| > ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used. |
| > clOrdId | String | Conditional | Client Order ID as assigned by the client |
| > reqId | String | No | Client Request ID as assigned by the client for order amendment A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| > newSz | String | Conditional | New quantity after amendment and it has to be larger than 0. Either `newSz` or `newPx` is required. When amending a partially-filled order, the `newSz` should include the amount that has been filled. |
| > newPx | String | Conditional | New price after amendment. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. It must be consistent with parameters when placing orders. For example, if users placed the order using px, they should use newPx when modifying the order. |
| > speedBump | String | Conditional | Speed bump`1`: Event contract speed bumps (the delay duration will be changed subject to adjustment without prior notice). Required for non-post-only orders of `EVENTS` symbols. |
| > newPxUsd | String | Conditional | Modify options orders using USD prices Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| > newPxVol | String | Conditional | Modify options orders based on implied volatility, where 1 represents 100% Only applicable to options. When modifying options orders, users can only fill in one of the following: newPx, newPxUsd, or newPxVol. |
| > pxAmendType | String | No | The price amendment type for orders`0`: Do not allow the system to amend to order price if `newPx` exceeds the price limit `1`: Allow the system to amend the price to the best available value within the price limit if `newPx` exceeds the price limit The default value is `0` |
| expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085` |

Response Example When All Succeed

```
{
 "id": "1513",
 "op": "batch-amend-orders",
 "data": [
 {
 "clOrdId": "oktswap6",
 "ordId": "12345689",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "0",
 "sMsg": "",
 "subCode": ""
 },
 {
 "clOrdId": "oktswap7",
 "ordId": "12344",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "0",
 "sMsg": "",
 "subCode": ""
 }
 ],
 "code": "0",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When All Failed

```
{
 "id": "1513",
 "op": "batch-amend-orders",
 "data": [
 {
 "clOrdId": "",
 "ordId": "12345689",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "5XXXX",
 "sMsg": "order not exist"
 },
 {
 "clOrdId": "oktswap7",
 "ordId": "",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "51008",
 "sMsg": "Order failed. Insufficient USDT balance in account",
 "subCode": "1000"
 }
 ],
 "code": "1",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Partially Successful

```
{
 "id": "1513",
 "op": "batch-amend-orders",
 "data": [
 {
 "clOrdId": "",
 "ordId": "12345689",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "0",
 "sMsg": ""
 },
 {
 "clOrdId": "",
 "ordId": "oktswap7",
 "ts": "1695190491421",
 "reqId": "b12344",
 "sCode": "51063",
 "sMsg": "OrdId does not exist"
 "subCode": ""
 }
 ],
 "code": "2",
 "msg": "",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

Response Example When Format Error

```
{
 "id": "1513",
 "op": "batch-amend-orders",
 "data": [],
 "code": "60013",
 "msg": "Invalid args",
 "inTime": "1695190491421339",
 "outTime": "1695190491423240"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > ts | String | Timestamp when the order request processing is finished by our system, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > reqId | String | Client Request ID as assigned by the client for order amendment If the user provides reqId in the request, the corresponding reqId will be returned |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Order status message |
| > subCode | String | Sub-code of sCode. Returns `""` when sCode is 0 (request successful). When sCode is not 0 (request failed), returns the sub-code if available; otherwise returns `""`. |
| inTime | String | Timestamp at Websocket gateway when the request is received, Unix timestamp format in microseconds, e.g. `1597026383085123` |
| outTime | String | Timestamp at Websocket gateway when the response is sent, Unix timestamp format in microseconds, e.g. `1597026383085123` |

newSz

If the new quantity of the order is less than or equal to the filled quantity when you are amending a partially-filled order, the order status will be changed to filled.

### WS / Mass cancel order

Cancel all the MMP pending orders of an instrument family.

Only applicable to Option in Portfolio Margin mode, and MMP privilege is required.

#### URL Path

/ws/v5/private (required login)

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the `Mass Cancel Order` REST API endpoints

Request Example

```
{
 "id": "1512",
 "op": "mass-cancel",
 "args": [{
 "instType":"OPTION",
 "instFamily":"BTC-USD"
 }]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`mass-cancel` |
| args | Array of objects | Yes | Request parameters |
| > instType | String | Yes | Instrument type`OPTION` |
| > instFamily | String | Yes | Instrument family |
| > lockInterval | String | No | Lock interval(ms) The range should be [0, 10 000] The default is 0. You can set it as "0" if you want to unlock it immediately. Error 54008 will be returned when placing order during lock interval, it is different from 51034 which is thrown when MMP is triggered |

##### Successful Response Example

```
{
 "id": "1512",
 "op": "mass-cancel",
 "data": [
 {
 "result": true
 }
 ],
 "code": "0",
 "msg": ""
}

```

Response Example When Format Error

```
{
 "id": "1512",
 "op": "mass-cancel",
 "data": [],
 "code": "60013",
 "msg": "Invalid args"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > result | Boolean | Result of the request `true`, `false` |
