## Stable Rewards

OKX Stable Rewards automatically distributes daily rewards to holders of eligible stablecoins (e.g. `USDG`) without any action required once enrolled.

Subscribe from the funding account; rewards and redemptions settle to the trading account by default.

### GET / Product info

Retrieve product-level information for the specified stablecoin, including all currencies eligible for subscription and redemption, applicable fee rates, amount limits, daily quotas, and current redemption availability.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/stable-rewards/product-info`

Request Example

```
GET /api/v5/finance/stable-rewards/product-info?ccy=USDG
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Stablecoin, e.g. `USDG` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "details": [
 {
 "ccy": "USDG",
 "settleCcy": "USDC",
 "subFeeRate": "0.0003",
 "redemptFeeRate": "0",
 "minSubAmt": "1",
 "minRedeemAmt": "0.0000001",
 "remainingSubQuota": "1000000",
 "remainingRedemptQuota": "500000",
 "canRedeem": true
 },
 {
 "ccy": "USDG",
 "settleCcy": "USDT",
 "subFeeRate": "0.0003",
 "redemptFeeRate": "",
 "minSubAmt": "1",
 "minRedeemAmt": "",
 "remainingSubQuota": "1000000",
 "remainingRedemptQuota": "",
 "canRedeem": false
 }
 ],
 "ts": "1718035200000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| details | Array of objects | List of supported settlement currencies and their subscription/redemption details |
| > ccy | String | Subscribable stablecoin, e.g. `USDG` |
| > settleCcy | String | Settlement currency that can be used to subscribe to `ccy`, e.g. `USDC`, `USDT` |
| > subFeeRate | String | Subscription fee rate, e.g. `0.01` represents `1%` |
| > redemptFeeRate | String | Redemption fee rate, e.g. `0.01` represents `1%`Returns `""` if redemption to the given `settleCcy` is not available |
| > minSubAmt | String | Minimum subscription amount, denominated in `settleCcy` |
| > minRedeemAmt | String | Minimum redemption amount, denominated in `ccy`Returns `""` if redemption to the given `settleCcy` is not available |
| > remainingSubQuota | String | Remaining daily subscription quota per master user IDReturns `-1` if unlimited |
| > remainingRedemptQuota | String | Remaining daily redemption quota per master user IDReturns `-1` if unlimitedReturns `""` if redemption to the given `settleCcy` is not available |
| > canRedeem | Boolean | Whether redemption to the given `settleCcy` is currently available`true`: Available`false`: Unavailable |
| ts | String | Data query time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### POST / Quote

Request a quote before subscribing or redeeming. Only the assets in the funding account can be used. The returned `quoteId` must be submitted via `POST /trade` before `ttlMs` expires.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/stable-rewards/quote`

Request Example

```
POST /api/v5/finance/stable-rewards/quote
body
{
 "ccy": "USDG",
 "settleCcy": "USDT",
 "action": "subscribe",
 "amt": "1000"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Stablecoin to subscribe or redeem, e.g. `USDG` |
| settleCcy | String | Yes | Settlement currency, e.g. `USDC`, `USDT` |
| action | String | Yes | Action type`subscribe``redeem` |
| amt | String | Yes | Transaction amountFor `subscribe`: denominated in `settleCcy`For `redeem`: denominated in `ccy` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "quoteId": "1234567890",
 "quoteAmt": "998.88",
 "quoteCcy": "USDG",
 "exchRate": "0.99888110",
 "feeRate": "0.0003",
 "quoteTime": "1620282889345",
 "ttlMs": "10000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| quoteId | String | Quote ID. Submit this value via `POST /trade` before `ttlMs` expires to execute the transaction |
| quoteAmt | String | Target amount denominated in `quoteCcy` |
| quoteCcy | String | Currency of `quoteAmt`For `subscribe`: returns `ccy` (the stablecoin received)For `redeem`: returns `settleCcy` (the settlement currency received) |
| exchRate | String | Exchange rate, 8 decimalsFor `subscribe`: units of `ccy` received per unit of `settleCcy`For `redeem`: units of `settleCcy` received per unit of `ccy` |
| feeRate | String | Fee rate applied to this quote, e.g. `0.0003` represents `0.03%` |
| quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| ttlMs | String | Quotation validity period in milliseconds, e.g. `10000` means the quote is valid for 10 seconds |

### POST / Trade

Execute a subscription or redemption using a valid `quoteId` obtained from `POST /quote`.

Subscription: assets are deducted from the funding account; on success, the stablecoin is credited to the trading account by default.

Redemption: the stablecoin is deducted from the funding account by default; the settlement currency is credited to the trading account by default.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/stable-rewards/trade`

Request Example

```
POST /api/v5/finance/stable-rewards/trade
body
{
 "quoteId": "1234567890"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| quoteId | String | Yes | Quote ID returned by `POST /quote`. The quote must not have expired |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "quoteId": "1234567890",
 "ordId": "987654321"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| quoteId | String | Quote ID |
| ordId | String | Order ID |

### GET / Balance

Retrieve the real-time Stable Rewards balance across the account (trading account, funding account, and in-progress redemptions combined), along with lifetime earnings and the current earning state for each stablecoin.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/stable-rewards/balance`

Request Example

```
GET /api/v5/finance/stable-rewards/balance?ccy=USDG
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Stablecoin, e.g. `USDG`Returns all supported stablecoins if not specified |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "details": [
 {
 "ccy": "USDG",
 "amt": "100",
 "totalEarnAccrual": "0.0003",
 "state": "earning"
 }
 ],
 "ts": "1718035200000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| details | Array of objects | Real-time balance details per stablecoin |
| > ccy | String | Stablecoin, e.g. `USDG` |
| > amt | String | Currency amount held across the entire account |
| > totalEarnAccrual | String | Total interest accrued over the lifetime of the holding |
| > state | String | Earning state`earning`: The balance is currently accruing rewards`pending`: The balance is not currently accruing (e.g. auto-earn is off, or the balance is below the activation threshold) |
| ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / APY history

Retrieve the historical daily APY of the specified stablecoin. The returned rate reflects the user's current VIP level.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/stable-rewards/apy-history`

Request Example

```
GET /api/v5/finance/stable-rewards/apy-history?ccy=USDG
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Stablecoin, e.g. `USDG` |
| days | String | No | Number of historical days to return. The default is `100`. The maximum is `100` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "rate": "0.004",
 "ts": "1718035200000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| rate | String | Daily APY for the user's current VIP level, e.g. `0.041` represents `4.1%` |
| ts | String | Snapshot time (UTC+0), Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Subscribe redeem history

Retrieve subscription and redemption records. Results are returned in reverse chronological order.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/stable-rewards/subscribe-redeem-history`

Request Example

```
GET /api/v5/finance/stable-rewards/subscribe-redeem-history?ccy=USDG
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Stablecoin, e.g. `USDG` |
| type | String | No | Record type`subscribe``redeem`Returns both types if not specified |
| status | String | No | Order status`pending``success``failed`Returns all statuses if not specified |
| after | String | No | Pagination of data to return records earlier than the requested `ordId` |
| before | String | No | Pagination of data to return records newer than the requested `ordId` |
| limit | String | No | Number of results per request. The default is `100`. The maximum is `100` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "type": "subscribe",
 "status": "success",
 "ccy": "USDG",
 "settleCcy": "USDT",
 "ccyAmt": "998.88",
 "settleCcyAmt": "1000",
 "fee": "0.3",
 "quoteId": "1234567890",
 "ordId": "987654321",
 "ts": "1718035200000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| type | String | Record type`subscribe``redeem` |
| status | String | Order status`pending``success``failed` |
| ccy | String | Stablecoin subscribed or redeemed, e.g. `USDG` |
| settleCcy | String | Settlement currency, e.g. `USDC`, `USDT` |
| ccyAmt | String | Amount denominated in `ccy` |
| settleCcyAmt | String | Amount denominated in `settleCcy` |
| fee | String | Fee charged, denominated in `settleCcy` |
| quoteId | String | Quote ID |
| ordId | String | Order ID |
| ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
