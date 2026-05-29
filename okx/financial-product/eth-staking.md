## ETH staking

ETH Staking, also known as Ethereum Staking, is the process of participating in the Ethereum blockchain's Proof-of-Stake (PoS) consensus mechanism.

Stake to receive BETH for liquidity at 1:1 ratio and earn daily BETH rewards

[Learn more about ETH Staking](https://www.okx.com/earn/ethereum-staking)

### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/product-info`

Request Example

```
GET /api/v5/finance/staking-defi/eth/product-info
```

```
import okx.Finance.EthStaking as EthStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.eth_product_info()
print(result)
```

Response Example

```
{
 "code": "0",
 "data": [
 {
 "fastRedemptionDailyLimit": "100"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| fastRedemptionDailyLimit | String | Fast redemption daily limitThe master account and sub-accounts share the same limit |

### POST / Purchase

Staking ETH for BETH

Only the assets in the funding account can be used.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/purchase`

Request Example

```
POST /api/v5/finance/staking-defi/eth/purchase
body
{
 "amt":"100"
}
```

```
import okx.Finance.EthStaking as EthStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.eth_purchase(amt="1")
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

Only the assets in the funding account can be used. If your BETH is in your trading account, you can make funding transfer first.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/redeem`

Request Example

```
POST /api/v5/finance/staking-defi/eth/redeem
body
{
 "amt": "10"
}
```

```
import okx.Finance.EthStaking as EthStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.eth_redeem(amt="1")
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

### POST / Cancel redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

Request Example

```
POST /api/v5/finance/staking-defi/eth/cancel-redeem
body
{
 "ordId": "1234567890"
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
 "data": [
 {
 "ordId": "1234567890"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |

### GET / Balance

The balance represents the real-time total BETH holdings across the entire account, including assets in the trading account, funding account, and those currently in the redeeming process.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/balance`

Request Example

```
GET /api/v5/finance/staking-defi/eth/balance
```

```
import okx.Finance.EthStaking as EthStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.eth_balance()
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
 "amt": "0.63926191",
 "ccy": "BETH",
 "latestInterestAccrual": "0.00006549",
 "totalInterestAccrual": "0.01490596",
 "ts": "1699257600000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BETH` |
| amt | String | Currency amount |
| latestInterestAccrual | String | Latest interest accrual |
| totalInterestAccrual | String | Total interest accrual |
| ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/purchase-redeem-history`

Request Example

```
GET /api/v5/finance/staking-defi/eth/purchase-redeem-history
```

```
import okx.Finance.EthStaking as EthStaking

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)

result = StackingAPI.eth_purchase_redeem_history()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | String | No | Type`purchase``redeem` |
| status | String | No | Status`pending``success``failed``cancelled` |
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
| status | String | Status`pending``success``failed``cancelled` |
| ordId | String | Order ID |
| requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/apy-history`

Request Example

```
GET /api/v5/finance/staking-defi/eth/apy-history?days=2
```

```
import okx.Finance.EthStaking as EthStaking

flag = "0" # Production trading:0 , demo trading:1

StackingAPI = EthStaking.EthStakingAPI(flag=flag)

result = StackingAPI.eth_apy_history(days="7")
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
 "rate": "0.02690000",
 "ts": "1734195600000"
 },
 {
 "rate": "0.02840000",
 "ts": "1734109200000"
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
