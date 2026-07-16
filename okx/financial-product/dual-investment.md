## Dual investment

### GET / Currency pairs

Returns available dual investment currency pairs.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/currency-pair`

Request Example

```
GET /api/v5/finance/sfp/dcd/currency-pair
```

#### Request Parameters

None

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "baseCcy": "BTC",
 "quoteCcy": "USDT",
 "optType": "C",
 "uly": "BTC-USD"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| baseCcy | String | Base currency |
| quoteCcy | String | Quote currency |
| optType | String | Option type`C`: Call`P`: Put |
| uly | String | Underlying |

### GET / Product info

Return dual investment product list.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/products`

Request Example

```
GET /api/v5/finance/sfp/dcd/products?baseCcy=BTC&quoteCcy=USDT&optType=C
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| baseCcy | String | Yes | Base currency |
| quoteCcy | String | Yes | Quote currency |
| optType | String | Yes | Option type`C`: Call`P`: Put |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "absYield": "0.00232413",
 "annualizedYield": "0.0541",
 "baseCcy": "BTC",
 "quoteCcy": "USDT",
 "expTime": "1774598400000",
 "interestAccrualTime": "1773244800000",
 "listTime": "1743150759000",
 "maxSize": "6000000",
 "minSize": "10",
 "notionalCcy": "USDT",
 "optType": "P",
 "productId": "BTC-USDT-260327-54500-P",
 "quoteTime": "1773243808703",
 "redeemEndTime": "1774594800000",
 "redeemStartTime": "1773244800000",
 "stepSz": "1",
 "tradeEndTime": "1774584000000",
 "strike": "54500",
 "uly": "BTC-USD"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| absYield | String | Absolute yield |
| annualizedYield | String | Annualized yield |
| baseCcy | String | Base currency |
| quoteCcy | String | Quote currency |
| notionalCcy | String | Investment currency. If `C`, then baseCcy; if `P`, then quoteCcy. |
| expTime | String | Expiry time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| interestAccrualTime | String | Interest accrual start time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| listTime | String | Product launch time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| minSize | String | Minimum trade size in notional currency |
| maxSize | String | Maximum trade size in notional currency |
| optType | String | Option type`C`: Call`P`: Put |
| productId | String | Product ID |
| quoteTime | String | When product was quoted, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| redeemStartTime | String | Earliest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| redeemEndTime | String | Latest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| stepSz | String | Trade step size in notional currency |
| tradeEndTime | String | Trade end time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uly | String | Underlying |
| strike | String | Strike price |

### POST / Request for quote

Requests a real-time quote for a dual investment product. The quote has a TTL and must be used before expiry.

#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/quote`

Request Example

```
POST /api/v5/finance/sfp/dcd/quote
body
{
 "productId": "BTC-USDT-260327-77000-C",
 "notionalSz": "1.5",
 "notionalCcy": "BTC"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| productId | String | Yes | Product ID |
| notionalSz | String | Yes | Investment size |
| notionalCcy | String | Yes | Investment currency |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "absYield": "0.00135182",
 "annualizedYield": "69.65",
 "interestAccrualTime": "1773241200000",
 "notionalSz": "0.001",
 "notionalCcy": "BTC",
 "productId": "BTC-USDT-260312-72000-C",
 "quoteId": "qtbcDCD-QUOTE17732395560537636",
 "validUntil": "1774584000000",
 "idxPx": "69000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| absYield | String | Absolute yield |
| annualizedYield | String | Annualized yield |
| interestAccrualTime | String | Interest accrual start time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| notionalSz | String | Investment size |
| notionalCcy | String | Investment currency |
| productId | String | Product ID |
| quoteId | String | Quote ID |
| validUntil | String | Quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| idxPx | String | Index price |

### POST / Trade

Places a dual investment order using a valid quote.

#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/trade`

Request Example

```
POST /api/v5/finance/sfp/dcd/trade
body
{
 "quoteId": "quoterbpDCD-QUOTE17732116652401234"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| quoteId | String | Yes | Quote ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "quoteId": "quoterbpDCD-QUOTE17732116652401234",
 "ordId": "987654321",
 "state": "live"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| quoteId | String | Quote ID |
| ordId | String | Order ID |
| state | String | Order state`initial`: request has been received by system, will further process`pending_book`: trade received by liquidity provider, pending further processing`live`: trade is live`rejected`: trade has been rejected |

### POST / Request for redeem quote

Requests an early redemption quote for a live dual investment order. This is step 1 of the two-step early redemption flow; call POST / Redeem to confirm.

#### Rate Limit: 10 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem-quote`

Request Example

```
POST /api/v5/finance/sfp/dcd/redeem-quote
body
{
 "ordId": "987654321"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Order ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "987654321",
 "quoteId": "quoterbcDCD-REDEEM17732116652401234",
 "redeemCcy": "BTC",
 "redeemSz": "1.4856",
 "termRate": "-0.50",
 "validUntil": "1774598400000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| quoteId | String | Quote ID |
| redeemSz | String | Redeem size |
| redeemCcy | String | Redeem currency |
| termRate | String | Term rate |
| validUntil | String | Redeem quote valid until, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### POST / Redeem

Confirms early redemption using a valid redeem quote. This is step 2 of the two-step early redemption flow.

#### Rate Limit: 2 requests per 60 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/sfp/dcd/redeem`

Request Example

```
POST /api/v5/finance/sfp/dcd/redeem
body
{
 "ordId": "987654321",
 "quoteId": "quoterbcDCD-REDEEM17732116652401234"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Order ID |
| quoteId | String | Yes | Quote ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "987654321",
 "state": "pending_redeem_booking"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| state | String | order state`pending_redeem_booking`: redeem received, waiting for liquidity provider further processing`pending_redeem`: liquidity provider booked, waiting for transfer`redeeming`: redemption in progress`redeemed`: redemption completed |

### GET / Order state

Returns the current state of a dual investment order.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/order-status`

Request Example

```
GET /api/v5/finance/sfp/dcd/order-status?ordId=987654321
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Order ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "987654321",
 "state": "live"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| state | String | Order state`initial``live``pending_settle``settled``pending_redeem``redeemed``rejected` |

### GET / Order history

Return dual investment history orders

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/sfp/dcd/order-history`

Request Example

```
GET /api/v5/finance/sfp/dcd/order-history
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | No | Order ID. When provided, returns that specific order directly (ignores other filters) |
| productId | String | No | Product ID, e.g. `BTC-USDT-260327-77000-C` |
| uly | String | No | Underlying index, e.g. `BTC-USD` |
| state | String | No | Order state filter`initial``live``pending_settle``settled``pending_redeem``redeemed``rejected` |
| beginId | String | No | Return records newer than this order ID |
| endId | String | No | Return records earlier than this order ID |
| begin | String | No | Begin timestamp filter, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | End timestamp filter, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request, max 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "987654321",
 "quoteId": "quoterbpDCD-QUOTE17732116652401234",
 "state": "settled",
 "productId": "BTC-USDT-260327-77000-C",
 "baseCcy": "BTC",
 "quoteCcy": "USDT",
 "uly": "BTC-USD",
 "strike": "77000",
 "notionalSz": "1.5",
 "notionalCcy": "BTC",
 "absYield": "0.00806038",
 "annualizedYield": "0.1834",
 "yieldSz": "0.01209057",
 "yieldCcy": "BTC",
 "settleSz": "1.51209057",
 "settleCcy": "BTC",
 "settlePx": "76500",
 "settleTime": "1774598400000",
 "expTime": "1774598400000",
 "redeemStartTime" : "1774598400000",
 "redeemEndime": "1774598400000",
 "cTime": "1773212400000",
 "uTime": "1773212400000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| quoteId | String | Quote ID |
| state | String | Order state`initial``live``pending_settle``settled``pending_redeem``redeemed``rejected` |
| productId | String | Product ID, e.g. `BTC-USDT-260327-77000-C` |
| baseCcy | String | Base currency, e.g. `BTC` |
| quoteCcy | String | Quote currency, e.g. `USDT` |
| uly | String | Underlying index, e.g. `BTC-USD` |
| strike | String | Strike price |
| notionalSz | String | Notional size |
| notionalCcy | String | Notional currency |
| absYield | String | Absolute yield rate |
| annualizedYield | String | Annual yield rate |
| yieldSz | String | Yield size |
| yieldCcy | String | Yield currency |
| settleSz | String | Settlement size ("" if not yet settled) |
| settleCcy | String | Settlement currency ("" if not yet settled) |
| settlePx | String | Settlement price ("" if not yet settled) |
| expTime | String | Product expiration time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| settleTime | String | Actual settled time, Unix timestamp format in milliseconds, e.g. `1597026383085` ("" if not yet settled) |
| redeemStartTime | String | Earliest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| redeemEndTime | String | Latest time to request early redemption, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| cTime | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Last update time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
