## REST API

### Place order

Place a new order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/sprd/order`

**Request Example

```
# place order for a spread
POST /api/v5/sprd/order
body
{
 "sprdId":"BTC-USDT_BTC-USDT-SWAP",
 "clOrdId":"b15",
 "side":"buy",
 "ordType":"limit",
 "px":"2.15",
 "sz":"2"
}
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# place order
result = spreadAPI.place_order(sprdId='BTC-USDT_BTC-USDT-SWAP',
 clOrdId='b16',side='buy',ordType='limit',
 px='2',sz='2')
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USD-SWAP |
| clOrdId | String | No | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| side | String | Yes | Order side, `buy` `sell` |
| ordType | String | Yes | Order type`market`: Market order `limit`: Limit order `post_only`: Post-only order`ioc`: Immediate-or-cancel order |
| sz | String | Yes | Quantity to buy or sell. The unit is USD for inverse spreads, and the corresponding baseCcy for linear and hybrid spreads. |
| px | String | Yes | Order price. Only applicable to `limit`, `post_only`, `ioc` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "clOrdId": "b15",
 "ordId": "312269865356374016",
 "tag": "",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| sCode | String | The code of the event execution result, 0 means success. |
| sMsg | String | Rejection or success message of event execution. |

clOrdId
clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.
clOrdId must be unique among the clOrdIds of all pending orders.

ordType
Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:
limit: Limit order, which requires specified sz and px.
post_only: Post-only order, which the order can only provide liquidity to the market and be a maker. If the order would have executed on placement, it will be canceled instead.
ioc: Immediate-or-cancel order

sz
The sz unit for inverse spreads is USD in Nitro Spread, as opposed to contract in OKX orderbook.

### Cancel order

Cancel an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/sprd/cancel-order`

Request Example

```
POST /api/v5/sprd/cancel-order
body
{
 "ordId":"2510789768709120"
}
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# cancel order
result = spreadAPI.cancel_order(ordId='1905309079888199680')
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used. |
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
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

#### Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| sCode | String | The code of the event execution result, 0 means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |

Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state.

### Cancel All orders

Cancel all pending orders.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/sprd/mass-cancel`

Request Example

```
POST /api/v5/sprd/mass-cancel
body
{
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
}
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# cancel all
result = spreadAPI.cancel_all_orders(sprdId="BTC-USDT_BTC-USDT-SWAP")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | No | spread ID |

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

#### Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| result | Boolean | Result of the request `true`, `false` |

Getting a response with result=true means your request has been successfully received and will be processed. The result of the cancellation is subject to the state pushed by the order channel or the get order state.

### Amend order

Amend an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/sprd/amend-order`

Request Example

```
POST /api/v5/sprd/amend-order
body
{
 "ordId":"2510789768709120",
 "newSz":"2"
}
```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required. If both are passed, ordId will be used. |
| clOrdId | String | Conditional | Client Order ID as assigned by the client |
| reqId | String | No | Client Request ID as assigned by the client for order amendment A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. The response will include the corresponding reqId to help you identify the request if you provide it in the request. |
| newSz | String | Conditional | New quantity after amendment Either `newSz` or `newPx` is required. When amending a partially-filled order, the newSz should include the amount that has been filled. |
| newPx | String | Conditional | New price after amendment Either `newSz` or `newPx` is required. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "clOrdId":"",
 "ordId":"12344",
 "reqId":"b12344",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client. |
| reqId | String | Client Request ID as assigned by the client for order amendment. |
| sCode | String | The code of the event execution result, 0 means success. |
| sMsg | String | Rejection message if the request is unsuccessful. |

newSz
If the new quantity of the order is less than or equal to the (accFillSz + canceledSz + pendingSettleSz), after pendingSettleSz is settled, the order status will be transitioned into filled (if canceledSz = 0), or canceled (if canceledSz > 0).

The amend order returns sCode equal to 0

It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query.

### Get order details

Retrieve order details.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/sprd/order`

Request Example

```
GET /api/v5/sprd/order?ordId=2510789768709120
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get order details
result = spreadAPI.get_order_details(ordId='1905309079888199680')
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used |
| clOrdId | String | Conditional | Client Order ID as assigned by the client. The latest order will be returned. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "BTC-USD-200329",
 "ordId": "312269865356374016",
 "clOrdId": "b1",
 "tag": "",
 "px": "999",
 "sz": "3",
 "ordType": "limit",
 "side": "buy",
 "fillSz": "0",
 "fillPx": "",
 "tradeId": "",
 "accFillSz": "0",
 "pendingFillSz": "2",
 "pendingSettleSz": "1",
 "canceledSz": "1",
 "state": "live",
 "avgPx": "0",
 "cancelSource": "",
 "uTime": "1597026383085",
 "cTime": "1597026383085"
 }
 ]
}

```

#### Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | Price |
| sz | String | Quantity to buy or sell |
| ordType | String | Order type`market`: Market order `limit`: Limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| side | String | Order side |
| fillSz | String | Last fill quantity |
| fillPx | String | Last fill price |
| tradeId | String | Last trade ID |
| accFillSz | String | Accumulated fill quantity |
| pendingFillSz | String | Live quantity |
| pendingSettleSz | String | Quantity that's pending settlement |
| canceledSz | String | Quantity canceled due order cancellations or trade rejections |
| avgPx | String | Average filled price. If none is filled, it will return "0". |
| state | String | State `canceled` `live` `partially_filled` `filled` |
| cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are: `0`: Order canceled by system `1`: Order canceled by user `14`: Order canceled: IOC order was partially canceled due to incompletely filled`15`: Order canceled: The order price is beyond the limit`20`: Cancel all after triggered `31`: The post-only order will take liquidity in maker orders`32`: Self trade prevention`34`: Order failed to settle due to insufficient margin `35`: Order cancellation due to insufficient margin from another order`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit. |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

Order sizes equation: pendingFillSz + canceledSz + accFillSz = sz

### Get active orders

Retrieve all incomplete orders under the current account.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/sprd/orders-pending`

Request Example

```
GET /api/v5/sprd/orders-pending
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get active orders
result = spreadAPI.get_active_orders()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | No | spread ID, e.g. |
| ordType | String | No | Order type`market`: Market order `limit`: Limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| state | String | No | State `live` `partially_filled` |
| beginId | String | No | Start order ID the request to begin with. Pagination of data to return records newer than the requested order Id, not including beginId |
| endId | String | No | End order ID the request to end with. Pagination of data to return records earlier than the requested order Id, not including endId |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-UST-SWAP",
 "ordId": "312269865356374016",
 "clOrdId": "b1",
 "tag": "",
 "px": "999",
 "sz": "3",
 "ordType": "limit",
 "side": "buy",
 "fillSz": "0",
 "fillPx": "",
 "tradeId": "",
 "accFillSz": "0",
 "pendingFillSz": "2",
 "pendingSettleSz": "1",
 "canceledSz": "1",
 "state": "live",
 "avgPx": "0",
 "cancelSource": "",
 "uTime": "1597026383085",
 "cTime": "1597026383085"
 }
 ]
}

```

#### Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | Price |
| sz | String | Quantity to buy or sell |
| ordType | String | Order type`market`: Market order `limit`: Limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| side | String | Order side |
| fillSz | String | Last fill quantity |
| fillPx | String | Last fill price |
| tradeId | String | Last trade ID |
| accFillSz | String | Accumulated fill quantity |
| pendingFillSz | String | Quantity still remaining to be filled |
| pendingSettleSz | String | Quantity that's pending settlement |
| canceledSz | String | Quantity canceled due order cancellations or trade rejections |
| avgPx | String | Average filled price. If none is filled, it will return "0". |
| state | String | State `live` `partially_filled` |
| cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are: `0`: Order canceled by system `1`: Order canceled by user `14`: Order canceled: IOC order was partially canceled due to incompletely filled`15`: Order canceled: The order price is beyond the limit `20`: Cancel all after triggered `31`: The post-only order will take liquidity in maker orders `32`: Self trade prevention `34`: Order failed to settle due to insufficient margin `35`: Order cancellation due to insufficient margin from another order`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit. |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get orders (last 21 days)

Retrieve the completed order data for the last 21 days, and the incomplete orders (filledSz =0 & state = canceled) that have been canceled are only reserved for 2 hours. Results are returned in counter chronological order of orders creation.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/sprd/orders-history`

Request Example

```
GET /api/v5/sprd/orders-history
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get orders history
result = spreadAPI.get_orders()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | No | spread ID, e.g. |
| ordType | String | No | Order type`market`: Market order `limit`: limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| state | String | No | State `canceled` `filled` |
| beginId | String | No | Start order ID the request to begin with. Pagination of data to return records newer than the requested order Id, not including beginId |
| endId | String | No | End order ID the request to end with. Pagination of data to return records earlier than the requested order Id, not including endId |
| begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`. Date older than 7 days will be truncated. |
| end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-UST-SWAP",
 "ordId": "312269865356374016",
 "clOrdId": "b1",
 "tag": "",
 "px": "999",
 "sz": "3",
 "ordType": "limit",
 "side": "buy",
 "fillSz": "0",
 "fillPx": "",
 "tradeId": "",
 "accFillSz": "0",
 "pendingFillSz": "2",
 "pendingSettleSz": "1",
 "canceledSz": "1",
 "state": "live",
 "avgPx": "0",
 "cancelSource": "",
 "uTime": "1597026383085",
 "cTime": "1597026383085"
 }
 ]
}

```

#### Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | Price |
| sz | String | Quantity to buy or sell |
| ordType | String | Order type`market`: Market order `limit`: limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| side | String | Order side |
| fillSz | String | Last fill quantity |
| fillPx | String | Last fill price |
| tradeId | String | Last trade ID |
| accFillSz | String | Accumulated fill quantity |
| pendingFillSz | String | Quantity still remaining to be filled, inluding pendingSettleSz |
| pendingSettleSz | String | Quantity that's pending settlement |
| canceledSz | String | Quantity canceled due order cancellations or trade rejections |
| avgPx | String | Average filled price. If none is filled, it will return "0". |
| state | String | State `canceled` `filled` |
| cancelSource | String | Source of the order cancellation. Valid values and the corresponding meanings are: `0`: Order canceled by system `1`: Order canceled by user `14`: Order canceled: IOC order was partially canceled due to incompletely filled`15`: Order canceled: The order price is beyond the limit `20`: Cancel all after triggered `31`: The post-only order will take liquidity in maker orders `32`: Self trade prevention`34`: Order failed to settle due to insufficient margin `35`: Order cancellation due to insufficient margin from another order`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit. |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get orders history (last 3 months)

Retrieve the completed order data for the last 3 months, including those placed 3 months ago but completed in the last 3 months. Results are returned in counter chronological order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/sprd/orders-history-archive`

Request Example

```
GET /api/v5/sprd/orders-history-archive
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | No | spread ID, e.g. |
| ordType | String | No | Order type`market`: Market order `limit`: limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| state | String | No | State `canceled` `filled` |
| instType | String | No | Instrument type`SPOT``FUTURES``SWAP` Any orders with spreads containing the specified instrument type in any legs will be returned |
| instFamily | String | No | Instrument family, e.g. BTC-USDT. Any orders with spreads containing the specified instrument family in any legs will be returned |
| beginId | String | No | Start order ID the request to begin with. Pagination of data to return records newer than the requested order Id, not including beginId |
| endId | String | No | End order ID the request to end with. Pagination of data to return records earlier than the requested order Id, not including endId |
| begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-UST-SWAP",
 "ordId": "312269865356374016",
 "clOrdId": "b1",
 "tag": "",
 "px": "999",
 "sz": "3",
 "ordType": "limit",
 "side": "buy",
 "fillSz": "0",
 "fillPx": "",
 "tradeId": "",
 "accFillSz": "0",
 "pendingFillSz": "2",
 "pendingSettleSz": "1",
 "canceledSz": "1",
 "state": "canceled",
 "avgPx": "0",
 "cancelSource": "",
 "uTime": "1597026383085",
 "cTime": "1597026383085"
 }
 ]
}

```

#### Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| px | String | Price |
| sz | String | Quantity to buy or sell |
| ordType | String | Order type`market`: Market order `limit`: limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| side | String | Order side |
| fillSz | String | Last fill quantity |
| fillPx | String | Last fill price |
| tradeId | String | Last trade ID |
| accFillSz | String | Accumulated fill quantity |
| pendingFillSz | String | Quantity still remaining to be filled, inluding pendingSettleSz |
| pendingSettleSz | String | Quantity that's pending settlement |
| canceledSz | String | Quantity canceled due order cancellations or trade rejections |
| avgPx | String | Average filled price. If none is filled, it will return "0". |
| state | String | State `canceled` `filled` |
| cancelSource | String | Source of the order cancellation. Valid values and the corresponding meanings are: `0`: Order canceled by system `1`: Order canceled by user `14`: Order canceled: IOC order was partially canceled due to incompletely filled`15`: Order canceled: The order price is beyond the limit `20`: Cancel all after triggered `31`: The post-only order will take liquidity in maker orders `32`: Self trade prevention`34`: Order failed to settle due to insufficient margin `35`: Order cancellation due to insufficient margin from another order`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit. |
| uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get trades (last 7 days)

Retrieve historical transaction details for the last 7 days**. Results are returned in counter chronological order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/sprd/trades`

Request Example

```
GET /api/v5/sprd/trades
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get private trades
result = spreadAPI.get_trades()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | No | spread ID, e.g. |
| tradeId | String | No | Trade ID |
| ordId | String | No | Order ID |
| beginId | String | No | Start trade ID the request to begin with. Pagination of data to return records newer than the requested tradeId, not including beginId |
| endId | String | No | End trade ID the request to end with. Pagination of data to return records earlier than the requested tradeId, not including endId |
| begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "sprdId": "BTC-USDT-SWAP_BTC-USDT-200329",
 "tradeId": "123",
 "ordId": "123445",
 "clOrdId": "b16",
 "tag": "",
 "fillPx": "999",
 "fillSz": "3",
 "state": "filled",
 "side": "buy",
 "execType": "M",
 "ts": "1597026383085",
 "legs": [
 {
 "instId": "BTC-USDT-SWAP",
 "px": "20000",
 "sz": "3",
 "szCont": "0.03",
 "side": "buy",
 "fillPnl": "",
 "fee": "",
 "feeCcy": "",
 "tradeId": "1232342342"
 },
 {
 "instId": "BTC-USDT-200329",
 "px": "21000",
 "sz": "3",
 "szCont": "0.03",
 "side": "sell",
 "fillPnl": "",
 "fee": "",
 "feeCcy": "",
 "tradeId": "5345646634"
 }
 ],
 "code": "",
 "msg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| tradeId | String | Trade ID |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| tag | String | Order tag |
| fillPx | String | Filled price |
| fillSz | String | Filled quantity |
| side | String | Order side, `buy` `sell` |
| state | String | Trade state. Valid values are `filled` and `rejected` |
| execType | String | Liquidity taker or maker, `T`: taker `M`: maker |
| ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |
| legs | Array of objects | Legs of trade |
| > instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| > px | String | The price the leg executed |
| > sz | String | The size of each leg |
| > szCont | String | Filled amount of the contract Only applicable to contracts, return "" for spot |
| > side | String | The direction of the leg. Valid value can be `buy` or `sell`. |
| > fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions |
| > fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive number represents rebate. |
| > feeCcy | String | Fee currency |
| > tradeId | String | Traded ID in the OKX orderbook. |
| code | String | Error Code, the default is 0 |
| msg | String | Error Message, the default is "" |

### Get Spreads (Public)

Retrieve all available spreads based on the request parameters.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/sprd/spreads`

Request Example

```
GET /api/v5/sprd/spreads?instId=BTC-USDT
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get spreads
result = spreadAPI.get_spreads()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| baseCcy | string | No | Currency instrument is based in, e.g. BTC, ETH |
| instId | String | No | The instrument ID to be included in the spread. |
| sprdId | String | No | The spread ID |
| state | string | No | Spreads which are available to trade, suspened or expired. Valid values include `live`, `suspend` and `expired`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "sprdId": "ETH-USD-SWAP_ETH-USD-231229",
 "sprdType": "inverse",
 "state": "live",
 "baseCcy": "ETH",
 "szCcy": "USD",
 "quoteCcy": "USD",
 "tickSz": "0.01",
 "minSz": "10",
 "lotSz": "10",
 "listTime": "1686903000159",
 "legs": [{
 "instId": "ETH-USD-SWAP",
 "side": "sell"
 },
 {
 "instId": "ETH-USD-231229",
 "side": "buy"
 }
 ],
 "expTime": "1703836800000",
 "uTime": "1691376905595"
 },
 {
 "sprdId": "BTC-USDT_BTC-USDT-SWAP",
 "sprdType": "linear",
 "state": "live",
 "baseCcy": "BTC",
 "szCcy": "BTC",
 "quoteCcy": "USDT",
 "tickSz": "0.0001",
 "minSz": "0.001",
 "lotSz": "1",
 "listTime": "1597026383085",
 "expTime": "1597029999085",
 "uTime": "1597028888085",
 "legs": [{
 "instId": "BTC-USDT",
 "side": "sell"
 },
 {
 "instId": "BTC-USDT-SWAP",
 "side": "buy"
 }
 ]
 },
 {
 "sprdId": "BTC-USDT_BTC-USDT-230317",
 "sprdType": "linear",
 "state": "live",
 "baseCcy": "BTC",
 "szCcy": "BTC",
 "quoteCcy": "USDT",
 "tickSz": "0.0001",
 "minSz": "0.001",
 "lotSz": "1",
 "listTime": "1597026383085",
 "expTime": "1597029999085",
 "uTime": "1597028888085",
 "legs": [{
 "instId": "BTC-USDT",
 "side": "sell"
 },
 {
 "instId": "BTC-USDT-230317",
 "side": "buy"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| sprdType | String | spread Type. Valid values are `linear`, `inverse`, `hybrid` |
| state | String | Current state of the spread. Valid values include `live`, `expired`, `suspend`. |
| baseCcy | String | Currency instrument is based in. Valid values include BTC, ETH |
| szCcy | String | The currency the spread order size is submitted to the underlying venue in, e.g. USD, BTC, ETH. |
| quoteCcy | String | The currency the spread is priced in, e.g. USDT, USD |
| tickSz | String | Tick size, e.g. 0.0001 in the quoteCcy of the spread. |
| minSz | String | Minimum order size in the szCcy of the spread. |
| lotSz | String | The minimum order size increment the spread can be traded in the szCcy of the spread. |
| listTime | String | The timestamp the spread was created. Unix timestamp format in milliseconds, , e.g. `1597026383085` |
| expTime | String | Expiry time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | The timestamp the spread was last updated. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| legs | array of objects | |
| > instId | String | Instrument ID, e.g. BTC-USD-SWAP |
| > side | String | The direction of the leg of the spread. Valid Values include `buy` and `sell`. |

### Get order book (Public)

Retrieve the order book of the spread.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/sprd/books`

Request Example

```
GET /api/v5/sprd/books?sprdId=BTC-USDT_BTC-USDT-SWAP
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get order book
result = spreadAPI.get_order_book(sprdId="BTC-USDT_BTC-USDT-SWAP", sz=20)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USDT-SWAP |
| sz | String | No | Order book depth per side. Maximum value is 400. Default value is 5. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "asks": [
 [
 "41006.8", // price
 "0.60038921", // quantity
 "1" // number of orders at the price
 ]
 ],
 "bids": [
 [
 "41006.3",
 "0.30178218",
 "2"
 ]
 ],
 "ts": "1629966436396"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| asks | Array of arrays | Order book on sell side |
| bids | Array of arrays | Order book on buy side |
| ts | String | Order book generation time |

An example of the array of asks and bids values: ["411.8", "10", "4"]

- "411.8" is the depth price

- "10" is the quantity at the price (Unit: szCcy)

- "4" is the number of orders at the price.

### Get ticker (Public)

Retrieve the latest price snapshot, best bid/ask price and quantity.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/sprd-ticker`

Request Example

```
GET /api/v5/market/sprd-ticker?sprdId=BTC-USDT_BTC-USDT-SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USDT-SWAP |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-USDT-SWAP",
 "last": "14.5",
 "lastSz": "0.5",
 "askPx": "8.5",
 "askSz": "12.0",
 "bidPx": "0.5",
 "bidSz": "12.0",
 "open24h": "4",
 "high24h": "14.5",
 "low24h": "-2.2",
 "vol24h": "6.67",
 "ts": "1715331406485"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| last | String | Last traded price |
| lastSz | String | Last traded size |
| askPx | String | Best ask price |
| askSz | String | Best ask size |
| bidPx | String | Best bid price |
| bidSz | String | Best bid size |
| open24h | String | Open price in the past 24 hours |
| high24h | String | Highest price in the past 24 hours |
| low24h | String | Lowest price in the past 24 hours |
| vol24h | String | 24h trading volume The unit is USD for inverse spreads, and the corresponding baseCcy for linear and hybrid spreads. |
| ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085. |

### Get public trades (Public)

Retrieve the recent transactions of an instrument (at most 500 records per request). Results are returned in counter chronological order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/sprd/public-trades`

Request Example

```
GET /api/v5/sprd/public-trades?sprdId=BTC-USDT_BTC-USDT-SWAP
```

```
import okx.SpreadTrading as SpreadTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)

# get public trades
result = spreadAPI.get_public_trades(sprdId='ETH-USDT-SWAP_ETH-USDT-230929')
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | No | Spread ID, e.g. BTC-USDT_BTC-USDT-SWAP |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "sprdId": "BTC-USDT_BTC-USDC-SWAP",
 "side": "sell",
 "sz": "0.1",
 "px": "964.1",
 "tradeId": "242720719",
 "ts": "1654161641568"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| sprdId | String | spread ID |
| tradeId | String | Trade ID |
| px | String | Trade price |
| sz | String | Trade quantity |
| side | String | Trade side of the taker. `buy` `sell` |
| ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |

### Get candlesticks

Retrieve the candlestick charts. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/sprd-candles`

Request Example

```
GET /api/v5/market/sprd-candles?sprdId=BTC-USDT_BTC-USDT-SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | Yes | Spread ID |
| bar | String | No | Bar size, the default is 1m, e.g. [1m/3m/5m/15m/30m/1H/2H/4H] UTC+8 opening price k-line:[6H/12H/1D/2D/3D/1W/1M/3M] UTC+0 opening price k-line:[/6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc] |
| after | String | No | Pagination of data to return records earlier than the requested ts |
| before | String | No | Pagination of data to return records newer than the requested ts. The latest data will be returned when using before individually |
| limit | String | No | Number of results per request. The maximum is 300. The default is 100. |

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
 "8422410",
 "0"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "24912403",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| o | String | Open price |
| h | String | highest price |
| l | String | Lowest price |
| c | String | Close price |
| vol | String | Trading volume |
| confirm | String | The state of candlesticks. `0` represents that it is uncompleted `1` represents that it is completed. |

The first candlestick data may be incomplete, and should not be polled repeatedly.

The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,confirm].

### Get candlesticks history

Retrieve history candlestick charts from recent years.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/sprd-history-candles`

Request Example

```
GET /api/v5/market/sprd-history-candles?sprdId=BTC-USDT_BTC-USDT-SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| sprdId | String | Yes | Spread ID |
| after | String | No | Pagination of data to return records earlier than the requested ts |
| before | String | No | Pagination of data to return records newer than the requested ts. The latest data will be returned when using before individually |
| bar | String | No | Bar size, the default is 1m, e.g. [1m/3m/5m/15m/30m/1H/2H/4H] UTC+8 opening price k-line:[6H/12H/1D/2D/3D/1W/1M/3M] UTC+0 opening price k-line:[6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc] |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

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
 "8422410",
 "1"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "24912403",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| o | String | Open price |
| h | String | Highest price |
| l | String | Lowest price |
| c | String | Close price |
| vol | String | Trading volume |
| confirm | String | The state of candlesticks. `0` represents that it is uncompleted `1` represents that it is completed. |

The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,confirm]

### Cancel All After

Cancel all pending orders after the countdown timeout. Only applicable to spread trading.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/sprd/cancel-all-after`

Request Example

```
POST /api/v5/sprd/cancel-all-after
{
 "timeOut":"30"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| timeOut | String | Yes | The countdown for order cancellation, with second as the unit.Range of value can be 0, [10, 120]. Setting timeOut to 0 disables Cancel All After. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "triggerTime":"1587971460",
 "ts":"1587971400"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| triggerTime | String | The time the cancellation is triggered.triggerTime=0 means Cancel All After is disabled. |
| ts | String | The time the request is received. |

Users are recommended to send a request to the exchange every second. When the cancel all after is triggered, the trading engine will cancel orders on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies.
