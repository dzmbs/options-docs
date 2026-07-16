## On-chain earn

Only the assets in the funding account can be used for purchase. [More details](/earn/onchain-earn)

### GET / Offers

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/offers`

Request Example

```
GET /api/v5/finance/staking-defi/offers
```

```
import okx.Finance.StakingDefi as StakingDefi

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)

result = StakingAPI.get_offers(ccy="USDT")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| productId | String | No | Product ID |
| protocolType | String | No | Protocol type`defi`: on-chain earn |
| ccy | String | No | Investment currency, e.g. `BTC` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "DOT",
 "productId": "101",
 "protocol": "Polkadot",
 "protocolType": "defi",
 "term": "0",
 "apy": "0.1767",
 "earlyRedeem": false,
 "state": "purchasable",
 "investData": [
 {
 "bal": "0",
 "ccy": "DOT",
 "maxAmt": "0",
 "minAmt": "2"
 }
 ],
 "earningData": [
 {
 "ccy": "DOT",
 "earningType": "0"
 }
 ],
 "fastRedemptionDailyLimit": "",
 "redeemPeriod": [
 "28D",
 "28D"
 ]
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency type, e.g. `BTC` |
| productId | String | Product ID |
| protocol | String | Protocol |
| protocolType | String | Protocol type`defi`: on-chain earn |
| term | String | Protocol termIt will return the days of fixed term and will return `0` for flexible product |
| apy | String | Estimated annualizationIf the annualization is 7% , this field is 0.07 |
| earlyRedeem | Boolean | Whether the protocol supports early redemption |
| investData | Array of objects | Current target currency information available for investment |
| > ccy | String | Investment currency, e.g. `BTC` |
| > bal | String | Available balance to invest |
| > minAmt | String | Minimum subscription amount |
| > maxAmt | String | Maximum available subscription amount |
| earningData | Array of objects | Earning data |
| > ccy | String | Earning currency, e.g. `BTC` |
| > earningType | String | Earning type`0`: Estimated earning`1`: Cumulative earning |
| state | String | Product state`purchasable`: Purchasable`sold_out`: Sold out`Stop`: Suspension of subscription |
| redeemPeriod | Array of strings | Redemption Period, format in [min time,max time]`H`: Hour, `D`: Daye.g. ["1H","24H"] represents redemption period is between 1 Hour and 24 Hours.["14D","14D"] represents redemption period is 14 days. |
| fastRedemptionDailyLimit | String | Fast redemption daily limitIf fast redemption is not supported, it will return ''. |

### POST / Purchase

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/purchase`

Request Example

```
# Invest 100ZIL 30-day staking protocol
POST /api/v5/finance/staking-defi/purchase
body
{
 "productId":"1234",
 "investData":[
 {
 "ccy":"ZIL",
 "amt":"100"
 }
 ],
 "term":"30"
}
```

```
import okx.Finance.StakingDefi as StakingDefi

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)

result = StakingAPI.purchase(
 productId = "4005",
 investData = [{
 "ccy":"USDT",
 "amt":"100"
 }]
 )
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| productId | String | Yes | Product ID |
| investData | Array of objects | Yes | Investment data |
| > ccy | String | Yes | Investment currency, e.g. `BTC` |
| > amt | String | Yes | Investment amount |
| term | String | Conditional | Investment termInvestment term must be specified for fixed-term product |
| tag | String | No | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "754147",
 "tag": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| tag | String | Order tag |

### POST / Redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/redeem`

Request Example

```
# Early redemption of investment
POST /api/v5/finance/staking-defi/redeem
body
{
 "ordId":"754147",
 "protocolType":"defi",
 "allowEarlyRedeem":true
}
```

```
import okx.Finance.StakingDefi as StakingDefi

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)

result = StakingAPI.redeem(
 ordId = "1234",
 protocolType = "defi"
 )
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Order ID |
| protocolType | String | Yes | Protocol type`defi`: on-chain earn |
| allowEarlyRedeem | Boolean | No | Whether allows early redemptionDefault is `false` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "754147",
 "tag": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| tag | String | Order tag |

### POST / Cancel purchases/redemptions

After cancelling, returning funds will go to the funding account.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/cancel`

Request Example

```
POST /api/v5/finance/staking-defi/cancel
body
{
 "ordId":"754147",
 "protocolType":"defi"
}
```

```
import okx.Finance.StakingDefi as StakingDefi

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)

result = StakingAPI.cancel(
 ordId = "1234",
 protocolType = "defi"
 )
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Order ID |
| protocolType | String | Yes | Protocol type`defi`: on-chain earn |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "754147",
 "tag": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| tag | String | Order tag |

### GET / Active orders

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/orders-active`

Request Example

```
GET /api/v5/finance/staking-defi/orders-active
```

```
import okx.Finance.StakingDefi as StakingDefi

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)

result = StakingAPI.get_activity_orders()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| productId | String | No | Product ID |
| protocolType | String | No | Protocol type`defi`: on-chain earn |
| ccy | String | No | Investment currency, e.g. `BTC` |
| state | String | No | Order state`8`: Pending `13`: Cancelling `9`: Onchain `1`: Earning `2`: Redeeming |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "ordId": "2413499",
 "ccy": "DOT",
 "productId": "101",
 "state": "1",
 "protocol": "Polkadot",
 "protocolType": "defi",
 "term": "0",
 "apy": "0.1014",
 "investData": [
 {
 "ccy": "DOT",
 "amt": "2"
 }
 ],
 "earningData": [
 {
 "ccy": "DOT",
 "earningType": "0",
 "earnings": "0.10615025"
 }
 ],
 "purchasedTime": "1729839328000",
 "tag": "",
 "estSettlementTime": "",
 "cancelRedemptionDeadline": "",
 "fastRedemptionData": []
 },
 {
 "ordId": "2213257",
 "ccy": "USDT",
 "productId": "4005",
 "state": "1",
 "protocol": "On-Chain Defi",
 "protocolType": "defi",
 "term": "0",
 "apy": "0.0323",
 "investData": [
 {
 "ccy": "USDT",
 "amt": "1"
 }
 ],
 "earningData": [
 {
 "ccy": "USDT",
 "earningType": "0",
 "earnings": "0.02886582"
 },
 {
 "ccy": "COMP",
 "earningType": "1",
 "earnings": "0.0000627"
 }
 ],
 "purchasedTime": "1725345790000",
 "tag": "",
 "estSettlementTime": "",
 "cancelRedemptionDeadline": "",
 "fastRedemptionData": []
 },
 {
 "ordId": "2210943",
 "ccy": "USDT",
 "productId": "4005",
 "state": "1",
 "protocol": "On-Chain Defi",
 "protocolType": "defi",
 "term": "0",
 "apy": "0.0323",
 "investData": [
 {
 "ccy": "USDT",
 "amt": "1"
 }
 ],
 "earningData": [
 {
 "ccy": "USDT",
 "earningType": "0",
 "earnings": "0.02891823"
 },
 {
 "ccy": "COMP",
 "earningType": "1",
 "earnings": "0.0000632"
 }
 ],
 "purchasedTime": "1725280801000",
 "tag": "",
 "estSettlementTime": "",
 "cancelRedemptionDeadline": "",
 "fastRedemptionData": []
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BTC` |
| ordId | String | Order ID |
| productId | String | Product ID |
| state | String | Order state`8`: Pending `13`: Cancelling `9`: Onchain `1`: Earning `2`: Redeeming |
| protocol | String | Protocol |
| protocolType | String | Protocol type`defi`: on-chain earn |
| term | String | Protocol termIt will return the days of fixed term and will return `0` for flexible product |
| apy | String | Estimated APYIf the estimated APY is 7% , this field is 0.07Retain to 4 decimal places (truncated) |
| investData | Array of objects | Investment data |
| > ccy | String | Investment currency, e.g. `BTC` |
| > amt | String | Invested amount |
| earningData | Array of objects | Earning data |
| > ccy | String | Earning currency, e.g. `BTC` |
| > earningType | String | Earning type`0`: Estimated earning`1`: Cumulative earning |
| > earnings | String | Earning amount |
| fastRedemptionData | Array of objects | Fast redemption data |
| > ccy | String | Currency, e.g. `BTC` |
| > redeemingAmt | String | Redeeming amount |
| purchasedTime | String | Order purchased time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| estSettlementTime | String | Estimated redemption settlement time |
| cancelRedemptionDeadline | String | Deadline for cancellation of redemption application |
| tag | String | Order tag |

### GET / Order history

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/orders-history`

Request Example

```
GET /api/v5/finance/staking-defi/orders-history
```

```
import okx.Finance.StakingDefi as StakingDefi

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)

result = StakingAPI.get_orders_history()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| productId | String | No | Product ID |
| protocolType | String | No | Protocol type`defi`: on-chain earn |
| ccy | String | No | Investment currency, e.g. `BTC` |
| after | String | No | Pagination of data to return records earlier than the requested ID. The value passed is the corresponding `ordId` |
| before | String | No | Pagination of data to return records newer than the requested ID. The value passed is the corresponding `ordId` |
| limit | String | No | Number of results per request. The default is `100`. The maximum is `100`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "1579252",
 "ccy": "DOT",
 "productId": "101",
 "state": "3",
 "protocol": "Polkadot",
 "protocolType": "defi",
 "term": "0",
 "apy": "0.1704",
 "investData": [
 {
 "ccy": "DOT",
 "amt": "2"
 }
 ],
 "earningData": [
 {
 "ccy": "DOT",
 "earningType": "0",
 "realizedEarnings": "0"
 }
 ],
 "purchasedTime": "1712908001000",
 "redeemedTime": "1712914294000",
 "tag": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BTC` |
| ordId | String | Order ID |
| productId | String | Product ID |
| state | String | Order state`3`: Completed (including canceled and redeemed) |
| protocol | String | Protocol |
| protocolType | String | Protocol type`defi`: on-chain earn |
| term | String | Protocol termIt will return the days of fixed term and will return `0` for flexible product |
| apy | String | Estimated APYIf the estimated APY is 7% , this field is `0.07`Retain to 4 decimal places (truncated) |
| investData | Array of objects | Investment data |
| > ccy | String | Investment currency, e.g. `BTC` |
| > amt | String | Invested amount |
| earningData | Array of objects | Earning data |
| > ccy | String | Earning currency, e.g. `BTC` |
| > earningType | String | Earning type`0`: Estimated earning`1`: Cumulative earning |
| > realizedEarnings | String | Cumulative earning of redeemed ordersThis field is just valid when the order is in redemption state |
| purchasedTime | String | Order purchased time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| redeemedTime | String | Order redeemed time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| tag | String | Order tag |
