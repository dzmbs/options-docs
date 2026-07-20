## OKUSD

OKUSD is OKX's stablecoin receipt issued at a 1:1 rate against USDT. Holders earn daily APR with no action required, and OKUSD can be used as trading margin to improve capital efficiency.

Subscription and redemption operate on the funding account. Use the `/limits` endpoint to check your remaining daily quota before subscribing or redeeming.

### GET / OKUSD limits

Retrieve your remaining daily OKUSD subscription quota and both fast and standard redemption quotas. All limits are calculated at the master-account level and shared across sub-accounts.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/okusd/limits`

Request Example

```
GET /api/v5/finance/okusd/limits
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
 "subLimit": {
 "maxSubAmt": "45000000",
 "personalDailyLimit": "5000000",
 "personalUsedAmt": "500000",
 "platformDailyLimit": "50000000",
 "platformUsedAmt": "5000000"
 },
 "fastRedeemLimit": {
 "personalDailyLimit": "10000",
 "personalUsedAmt": "0",
 "platformDailyLimit": "5000000",
 "platformUsedAmt": "1000000",
 "feeRate": "0.001"
 },
 "stdRedeemLimit": {
 "personalDailyLimit": "1000000",
 "personalUsedAmt": "0",
 "platformDailyLimit": "40000000",
 "platformUsedAmt": "0",
 "feeRate": "0.00025"
 },
 "ts": "1718500000000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| subLimit | Object | Subscription limit information |
| > maxSubAmt | String | Maximum subscribable amount for today (USDT). Equal to `min(personalDailyLimit - personalUsedAmt, platformDailyLimit - platformUsedAmt)`. Minimum value is `"0"` |
| > personalDailyLimit | String | Your daily subscription limit based on your VIP tier (USDT) |
| > personalUsedAmt | String | Amount you have already subscribed today (USDT) |
| > platformDailyLimit | String | Platform-wide daily subscription cap (USDT) |
| > platformUsedAmt | String | Total amount subscribed across the platform today (USDT) |
| fastRedeemLimit | Object | Fast redemption limit information (real-time settlement) |
| > personalDailyLimit | String | Your daily fast redemption limit based on your VIP tier (OKUSD) |
| > personalUsedAmt | String | Fast redemption amount you have already used today (OKUSD) |
| > platformDailyLimit | String | Platform-wide daily fast redemption cap (OKUSD) |
| > platformUsedAmt | String | Total fast redemption amount used across the platform today (OKUSD) |
| > feeRate | String | Fee rate for fast redemption |
| stdRedeemLimit | Object | Standard redemption limit information |
| > personalDailyLimit | String | Your daily standard redemption limit based on your VIP tier (OKUSD) |
| > personalUsedAmt | String | Standard redemption amount you have already used today (OKUSD) |
| > platformDailyLimit | String | Platform-wide daily standard redemption cap (OKUSD) |
| > platformUsedAmt | String | Total standard redemption amount used across the platform today (OKUSD) |
| > feeRate | String | Fee rate for standard redemption |
| ts | String | Server timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### POST / Subscribe OKUSD

Subscribe USDT to receive OKUSD at a 1:1 rate with no subscription fee. OKUSD is credited immediately to your funding account. Pass a unique `clOrdId` per request; resubmitting the same `clOrdId` returns the original order without re-executing the subscription.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/okusd/subscribe`

Request Example

```
POST /api/v5/finance/okusd/subscribe
body
{
 "amt": "1000.00000000",
 "clOrdId": "my-sub-001"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| amt | String | Yes | Amount of USDT to subscribe. Minimum: `1`. Maximum 8 decimal places. Scientific notation is not supported |
| clOrdId | String | Yes | Client-defined order ID. Maximum 32 characters (letters, digits, `-`, `_`). Must be unique per UID. Used for order tracking and idempotency |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "680012345678901234",
 "clOrdId": "my-sub-001",
 "ccy": "USDT",
 "amt": "1000.00000000",
 "okusdAmt": "1000.00000000",
 "state": "success",
 "ts": "1718500000000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | System-generated order ID |
| clOrdId | String | Client-defined order ID (echoed back) |
| ccy | String | Subscription currency. Always `"USDT"` |
| amt | String | Actual USDT amount subscribed |
| okusdAmt | String | OKUSD amount credited to your funding account (equal to `amt` at 1:1 rate; no subscription fee) |
| state | String | Order status: `"success"` / `"pending"` / `"failed"` |
| ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### POST / Redeem OKUSD

Redeem OKUSD back to USDT. Choose between fast redemption (real-time settlement) or standard redemption (D+5 or D+6 calendar days, depending on submission time). Fee rates vary by redemption type — call `GET /limits` to get current rates. All fee amounts are truncated (floor) to 8 decimal places. Pass a unique `clOrdId` per request; resubmitting the same `clOrdId` returns the original order without re-executing the redemption.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/okusd/redeem`

Request Example (Fast Redemption)

```
POST /api/v5/finance/okusd/redeem
body
{
 "amt": "1000.00000000",
 "redeemType": "1",
 "clOrdId": "my-redeem-001"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| amt | String | Yes | Amount of OKUSD to redeem. Minimum: `1`. Maximum 8 decimal places. Scientific notation is not supported |
| redeemType | String | Yes | Redemption type. `"1"`: Fast redemption (real-time settlement); `"2"`: Standard redemption (D+5 calendar days if submitted before UTC+8 16:00; D+6 calendar days if submitted at or after UTC+8 16:00). See the `feeRate` fields returned by `GET /limits` for current fee rates |
| clOrdId | String | Yes | Client-defined order ID. Maximum 32 characters (letters, digits, `-`, `_`). Must be unique per UID. Used for order tracking and idempotency |

Response Example (Fast Redemption)

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "680012345678905678",
 "clOrdId": "my-redeem-001",
 "ccy": "OKUSD",
 "amt": "1000.00000000",
 "fee": "1.00000000",
 "usdtAmt": "999.00000000",
 "redeemType": "1",
 "state": "success",
 "estSettlementTime": "1718500010000",
 "ts": "1718500000000"
 }
 ]
}

```

Response Example (Standard Redemption)

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "680012345678906789",
 "clOrdId": "my-redeem-002",
 "ccy": "OKUSD",
 "amt": "50000.00000000",
 "fee": "12.50000000",
 "usdtAmt": "49987.50000000",
 "redeemType": "2",
 "state": "processing",
 "estSettlementTime": "1718932800000",
 "ts": "1718500000000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | System-generated order ID |
| clOrdId | String | Client-defined order ID (echoed back) |
| ccy | String | Redemption currency. Always `"OKUSD"` |
| amt | String | OKUSD amount redeemed |
| fee | String | Fee charged in USDT, truncated (floor) to 8 decimal places |
| usdtAmt | String | Net USDT amount credited to your funding account (`amt - fee`, truncated to 8 decimal places) |
| redeemType | String | Redemption type: `"1"` (fast) or `"2"` (standard) |
| state | String | Order status: `"processing"` / `"success"` / `"failed"` / `"cancelled"` |
| estSettlementTime | String | Estimated settlement time, Unix timestamp format in milliseconds. Fast redemption: current time. Standard redemption: D+5 calendar days if submitted before UTC+8 16:00; D+6 calendar days if submitted at or after UTC+8 16:00 |
| ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Get OKUSD Account

Retrieve your current OKUSD balance and lifetime accrued yield. All balances are aggregated at the master-account level and shared across sub-accounts.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/account`

Request Example

```
GET /api/v5/finance/okusd/account
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
 "ccy": "OKUSD",
 "amt": "10000.00000000",
 "totalEarnAccrual": "123.45678900",
 "ts": "1718500000000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency. Always `"OKUSD"` |
| amt | String | Current OKUSD balance |
| totalEarnAccrual | String | Cumulative yield accrued over the holding period, denominated in USDT |
| ts | String | Server timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Get Subscription History

Retrieve your OKUSD subscription order history. Results are returned in descending order by timestamp (newest first) and support time-range filtering.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/subscribe/history`

Request Example

```
GET /api/v5/finance/okusd/subscribe/history?limit=2
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| limit | String | No | Number of results per page. Default `"100"`. Maximum `"100"` |
| begin | String | No | Start time filter (order creation time `ts`, Unix ms, inclusive) |
| end | String | No | End time filter (order creation time `ts`, Unix ms, inclusive) |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "680012345678901234",
 "clOrdId": "my-sub-001",
 "ccy": "USDT",
 "amt": "1000.00000000",
 "settleCcy": "OKUSD",
 "settleCcyAmt": "1000.00000000",
 "status": "success",
 "ts": "1718500000000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | System-generated order ID |
| clOrdId | String | Client-defined order ID (echoed back; empty string if not provided) |
| ccy | String | Subscription currency. Always `"USDT"` |
| amt | String | USDT amount subscribed |
| settleCcy | String | Settlement currency. Always `"OKUSD"` |
| settleCcyAmt | String | OKUSD amount credited (equal to `amt` at 1:1 rate) |
| status | String | Terminal order status: `"success"` / `"failed"` |
| ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Get Redemption History

Retrieve your OKUSD redemption order history. Results are returned in descending order by timestamp (newest first) and support time-range filtering and redemption-type filtering.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/redeem/history`

Request Example

```
GET /api/v5/finance/okusd/redeem/history?type=fast
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| limit | String | No | Number of results per page. Default `"100"`. Maximum `"100"` |
| begin | String | No | Start time filter (order creation time `ts`, Unix ms, inclusive) |
| end | String | No | End time filter (order creation time `ts`, Unix ms, inclusive) |
| type | String | No | Redemption type filter: `"fast"` for fast redemption only; `"standard"` for standard redemption only. Defaults to standard redemption if not specified |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "680012345678905678",
 "clOrdId": "my-rdm-fast-001",
 "ccy": "OKUSD",
 "amt": "1000.00000000",
 "fee": "1.00000000",
 "settleCcy": "USDT",
 "settleCcyAmt": "999.00000000",
 "type": "fast",
 "status": "success",
 "estSettlementTime": "1718500010000",
 "ts": "1718500000000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | System-generated order ID |
| clOrdId | String | Client-defined order ID (echoed back; empty string if not provided) |
| ccy | String | Redemption currency. Always `"OKUSD"` |
| amt | String | OKUSD amount redeemed |
| fee | String | Fee charged in USDT, truncated (floor) to 8 decimal places |
| settleCcy | String | Settlement currency. Always `"USDT"` |
| settleCcyAmt | String | Net USDT amount credited (`amt - fee`, truncated to 8 decimal places) |
| type | String | Redemption type: `"fast"` (real-time settlement) or `"standard"` (D+5/D+6 calendar days) |
| status | String | Order status: `"pending"` / `"success"` / `"failed"` / `"canceled"` |
| estSettlementTime | String | Estimated settlement time, Unix timestamp format in milliseconds. Empty string for settled fast redemption orders |
| ts | String | Order creation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Get Rewards History

Retrieve your daily OKUSD yield distribution history. Results are returned in descending order by timestamp (newest first).

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/rewards/history`

Request Example

```
GET /api/v5/finance/okusd/rewards/history?limit=7
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| limit | String | No | Number of results per page. Default `"30"`. Maximum `"100"` |
| begin | String | No | Start time filter (`ts`, Unix ms, inclusive). Maximum query span is 6 months |
| end | String | No | End time filter (`ts`, Unix ms, inclusive). Defaults to the current time if not provided |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ccy": "USDT",
 "earnAmt": "1.14246575",
 "amt": "10000.00000000",
 "apr": "0.0418",
 "ts": "1718500000000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Yield currency. Always `"USDT"` |
| earnAmt | String | USDT yield distributed in this event |
| amt | String | Your USDT principal balance at the time of distribution |
| apr | String | APR applied for this distribution, e.g. `"0.0418"` represents 4.18% |
| ts | String | Distribution timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Get APR History

Retrieve the historical APR snapshots for OKUSD. Results are returned in descending order by timestamp (newest first). This endpoint requires API Key authentication even though the data is product-level and not user-specific.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/okusd/rate/history`

Request Example

```
GET /api/v5/finance/okusd/rate/history?limit=10
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| limit | String | No | Number of results per page. Default `"30"`. Maximum `"100"` |
| begin | String | No | Start time filter (`ts`, Unix ms, inclusive). Maximum query span is 6 months |
| end | String | No | End time filter (`ts`, Unix ms, inclusive). Defaults to the current time if not provided |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 { "apr": "0.0418", "ts": "1718500000000" },
 { "apr": "0.0395", "ts": "1718413600000" }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| apr | String | OKUSD APR at this snapshot, e.g. `"0.0418"` represents 4.18% |
| ts | String | Snapshot timestamp, Unix timestamp format in milliseconds, e.g. `1597026383085` |
