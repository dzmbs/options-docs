## Simple earn flexible

Simple earn flexible (saving) is earned by lending to leveraged trading users in the lending market. [learn more](/earn/simple-earn)

### GET / Saving balance

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/savings/balance`

Request Example

```
GET /api/v5/finance/savings/balance?ccy=USDT
```

```
import okx.Finance.Savings as Savings

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)

result = SavingsAPI.get_saving_balance(ccy="USDT")
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, e.g. `BTC` |

Response Example

```
{
 "code": "0",
 "msg":"",
 "data": [
 {
 "earnings": "0.0010737388791526",
 "redemptAmt": "",
 "rate": "0.0100000000000000",
 "ccy": "USDT",
 "amt": "11.0010737453457821",
 "loanAmt": "11.0010630707982819",
 "pendingAmt": "0.0000106745475002"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| amt | String | Currency amount |
| earnings | String | Currency earnings |
| rate | String | Minimum annual lending rate configured by users |
| loanAmt | String | Lending amount |
| pendingAmt | String | Pending amount |
| redemptAmt | String | Redempting amount (Deprecated) |

### POST / Savings purchase/redemption

Only the assets in the funding account can be used for saving.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/savings/purchase-redempt`

Request Example

```
POST /api/v5/finance/savings/purchase-redempt
body
{
 "ccy":"BTC",
 "amt":"1",
 "side":"purchase",
 "rate":"0.01"
}
```

```
import okx.Finance.Savings as Savings

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)

result = SavingsAPI.savings_purchase_redemption(ccy='USDT',amt="0.1",side="purchase",rate="1")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency, e.g. `BTC` |
| amt | String | Yes | Purchase/redemption amount |
| side | String | Yes | Action type. `purchase`: purchase saving shares `redempt`: redeem saving shares |
| rate | String | Conditional | Annual purchase rate, e.g. `0.1` represents `10%`Only applicable to purchase saving sharesThe interest rate of the new subscription will cover the interest rate of the last subscriptionThe rate value range is between 1% and 365% |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "ccy":"BTC",
 "amt":"1",
 "side":"purchase",
 "rate": "0.01"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| amt | String | Purchase/Redemption amount |
| side | String | Action type |
| rate | String | Annual purchase rate, e.g. `0.1` represents `10%` |

### POST / Set lending rate

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/savings/set-lending-rate`

Request Example

```
POST /api/v5/finance/savings/set-lending-rate
body
{
 "ccy":"BTC",
 "rate":"0.02"
}
```

```
import okx.Finance.Savings as Savings

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)

result = SavingsAPI.set_lending_rate(ccy='USDT',rate="1")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency, e.g. `BTC` |
| rate | String | Yes | Annual lending rateThe rate value range is between 1% and 365% |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "ccy": "BTC",
 "rate": "0.02"
 }]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BTC` |
| rate | String | Annual lending rate |

### GET / Lending history

Return data in the past month.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/savings/lending-history`

Request Example

```
GET /api/v5/finance/savings/lending-history
```

```
import okx.Finance.Savings as Savings

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)

result = SavingsAPI.get_lending_history()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, e.g. `BTC` |
| after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "ccy": "BTC",
 "amt": "0.01",
 "earnings": "0.001",
 "rate": "0.01",
 "ts": "1597026383085"
 },
 {
 "ccy": "ETH",
 "amt": "0.2",
 "earnings": "0.001",
 "rate": "0.01",
 "ts": "1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BTC` |
| amt | String | Lending amount |
| earnings | String | Currency earnings |
| rate | String | Lending annual interest rate |
| ts | String | Lending time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Public borrow info (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-summary`

Request Example

```
GET /api/v5/finance/savings/lending-rate-summary
```

```
import okx.Finance.Savings as Savings

flag = "0" # Production trading:0 , demo trading:1

SavingsAPI = Savings.SavingsAPI(flag=flag)

result = SavingsAPI.get_public_borrow_info()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, e.g. `BTC` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "ccy": "BTC",
 "avgAmt": "10000",
 "avgAmtUsd": "10000000000",
 "avgRate": "0.03",
 "preRate": "0.02",
 "estRate": "0.01"
 }]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BTC` |
| avgAmt | String | 24H average borrowing amount(deprecated) |
| avgAmtUsd | String | 24H average borrowing amount in `USD` value(deprecated) |
| avgRate | String | 24-hours average annual borrowing rate |
| preRate | String | Last annual borrowing interest rate |
| estRate | String | Next estimate annual borrowing interest rate |

### GET / Public borrow history (public)

Authentication is not required for this public endpoint.

Only returned records after December 14, 2021.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-history`

Request Example

```
GET /api/v5/finance/savings/lending-rate-history
```

```
import okx.Finance.Savings as Savings

flag = "0" # Production trading:0 , demo trading:1

SavingsAPI = Savings.SavingsAPI(flag=flag)

result = SavingsAPI.get_public_borrow_history()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, e.g. `BTC` |
| after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.If `ccy` is not specified, all data under the same `ts` will be returned, not limited by `limit` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "ccy": "BTC",
 "amt": "0.01",
 "rate": "0.001",
 "lendingRate": "0.001",
 "ts": "1597026383085"
 }]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BTC` |
| amt | String | Lending amount(deprecated) |
| rate | String | Annual borrowing interest rate |
| lendingRate | String | Annual lending interest rate |
| ts | String | Time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
