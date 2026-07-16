## Stable Rewards

OKX Stable Rewards automatically distributes daily rewards to holders of eligible stablecoins (e.g. `USDG`) without any action required once enrolled.**Subscribe from the funding account; rewards and redemptions settle to the trading account by default.

Deprecation Notice**

`POST /api/v5/finance/stable-rewards/quote`, `POST /api/v5/finance/stable-rewards/trade`, and `GET /api/v5/finance/stable-rewards/subscribe-redeem-history` have been decommissioned. Please use the standard [order book trading APIs](/docs-v5/en/#order-book-trading) to trade USDG and other stablecoins.

### GET / Product info

Retrieve product-level information for the specified stablecoin, including all currencies eligible for subscription and redemption, applicable fee rates, amount limits, daily quotas, and current redemption availability.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

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

### GET / Balance

Retrieve the real-time Stable Rewards balance across the account (trading account, funding account, and in-progress redemptions combined), along with lifetime earnings and the current earning state for each stablecoin.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

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
