## SOL staking

By staking SOL tokens and delegating them to validators on the Solana network, you can receive equivalent OKSOL and earn extra OKSOL rewards.

Stake SOL on Solana to receive OKSOL at a 1:1 ratio for liquidity

[Learn more about OKSOL Staking](/earn/solana-staking#from=finance_crypto)

### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/product-info`

Request Example

```
GET /api/v5/finance/staking-defi/sol/product-info
```

```

```

Response Example

```
{
 "code": "0",
 "data": {
 "fastRedemptionAvail": "240",
 "fastRedemptionDailyLimit": "240",
 "rate": "5.57",
 "redemptDays": "2",
 "minAmt": "0.01"
 },
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| fastRedemptionDailyLimit | String | Fast redemption daily limitThe master account and sub-accounts share the same limit |
| fastRedemptionAvail | String | Currently fast redemption max available amount |
| rate | String | Latest OKSOL APY |
| redemptDays | String | Redemption days of OKSOL |
| minAmt | String | Minimum subscription amount of OKSOL |

### POST / Purchase

Staking SOL for OKSOL

Only the assets in the funding account can be used.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/purchase`

Request Example

```
POST /api/v5/finance/staking-defi/sol/purchase
body
{
 "amt":"100"
}
```

```
import okx.Finance.SolStaking as SolStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.sol_purchase(amt="1")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| amt | String | Yes | Investment amount |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 ]
}

```

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Redeem

Only the assets in the funding account can be used. If your OKSOL is in your trading account, you can make funding transfer first.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/redeem`

Request Example

```
POST /api/v5/finance/staking-defi/sol/redeem
body
{
 "amt": "10"
}
```

```
import okx.Finance.SolStaking as SolStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.sol_redeem(amt="1")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| amt | String | Yes | Redeeming amount |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 ]
}

```

#### Response Parameters

code = `0` means your request has been successfully handled.

### GET / Balance

The balance represents the real-time total OKSOL holdings across the entire account, including assets in the trading account, funding account, and those currently in the redeeming process.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/balance`

Request Example

```
GET /api/v5/finance/staking-defi/sol/balance
```

```
import okx.Finance.SolStaking as SolStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.sol_balance()
print(result)
```

#### Request Parameters

None

Response Example

```
{
 "code": "0",
 "data": [
 {
 "amt": "0.01100012",
 "ccy": "OKSOL",
 "latestInterestAccrual": "0.00000012",
 "totalInterestAccrual": "0.00000012"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `OKSOL` |
| amt | String | Currency amount |
| latestInterestAccrual | String | Latest interest accrual |
| totalInterestAccrual | String | Total interest accrual |

### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

Request Example

```
GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
```

```
import okx.Finance.SolStaking as SolStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.sol_purchase_redeem_history()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | String | No | Type`purchase``redeem` |
| status | String | No | Status`pending``success``failed` |
| after | String | No | Pagination of data to return records earlier than the `requestTime`. The value passed is the corresponding `timestamp` |
| before | String | No | Pagination of data to return records newer than the `requestTime`. The value passed is the corresponding `timestamp` |
| limit | String | No | Number of results per request. The default is `100`. The maximum is `100`. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "amt": "0.62666630",
 "completedTime": "1683413171000",
 "estCompletedTime": "",
 "redeemingAmt": "",
 "requestTime": "1683413171000",
 "status": "success",
 "type": "purchase"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| type | String | Type`purchase``redeem` |
| amt | String | Purchase/Redeem amount |
| redeemingAmt | String | Redeeming amount |
| status | String | Status`pending``success``failed` |
| requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/apy-history`

Request Example

```
GET /api/v5/finance/staking-defi/sol/apy-history?days=2
```

```
import okx.Finance.SolStaking as SolStaking

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = SolStaking.SolStakingAPI(flag=flag)

result = StackingAPI.sol_apy_history(days="7")
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| days | String | Yes | Get the days of APY(Annual percentage yield) history record in the pastNo more than 365 days |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "rate": "0.11280000",
 "ts": "1734192000000"
 },
 {
 "rate": "0.11270000",
 "ts": "1734105600000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| rate | String | APY(Annual percentage yield), e.g. `0.01` represents `1%` |
| ts | String | Data time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
