## REST API

### Get currencies

Retrieve a list of all currencies available which are related to the current account's KYC entity.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/currencies`

**Request Example

```
GET /api/v5/asset/currencies
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get currencies
result = fundingAPI.get_currencies()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Single currency or multiple currencies separated with comma, e.g. `BTC` or `BTC,ETH`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "burningFeeRate": "",
 "canDep": true,
 "canInternal": true,
 "canWd": true,
 "ccy": "BTC",
 "chain": "BTC-Bitcoin",
 "ctAddr": "",
 "depEstOpenTime": "",
 "depQuotaFixed": "",
 "depQuoteDailyLayer2": "",
 "fee": "0.00005",
 "logoLink": "https://static.coinall.ltd/cdn/oksupport/asset/currency/icon/btc20230419112752.png",
 "mainNet": true,
 "maxFee": "0.00005",
 "maxFeeForCtAddr": "",
 "maxWd": "500",
 "minDep": "0.0005",
 "minDepArrivalConfirm": "1",
 "minFee": "0.00005",
 "minFeeForCtAddr": "",
 "minInternal": "0.0001",
 "minWd": "0.0005",
 "minWdUnlockConfirm": "2",
 "name": "Bitcoin",
 "needTag": false,
 "usedDepQuotaFixed": "",
 "usedWdQuota": "0",
 "wdEstOpenTime": "",
 "wdQuota": "10000000",
 "wdTickSz": "8"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `BTC` |
| name | String | Name of currency. There is no related name when it is not shown. |
| logoLink | String | The logo link of currency |
| chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20` |
| ctAddr | String | Contract address |
| canDep | Boolean | The availability to deposit from chain `false`: not available `true`: available |
| canWd | Boolean | The availability to withdraw to chain `false`: not available `true`: available |
| canInternal | Boolean | The availability to internal transfer `false`: not available `true`: available |
| depEstOpenTime | String | Estimated opening time for deposit, Unix timestamp format in milliseconds, e.g. `1597026383085`if `canDep` is `true`, it returns `""` |
| wdEstOpenTime | String | Estimated opening time for withdraw, Unix timestamp format in milliseconds, e.g. `1597026383085`if `canWd` is `true`, it returns `""` |
| minDep | String | The minimum deposit amount of currency in a single transaction |
| minWd | String | The minimum `on-chain withdrawal` amount of currency in a single transaction |
| minInternal | String | The minimum `internal transfer` amount of currency in a single transactionNo maximum `internal transfer` limit in a single transaction, subject to the withdrawal limit in the past 24 hours(`wdQuota`). |
| maxWd | String | The maximum amount of currency `on-chain withdrawal` in a single transaction |
| wdTickSz | String | The withdrawal precision, indicating the number of digits after the decimal point.The withdrawal fee precision kept the same as withdrawal precision.The accuracy of internal transfer withdrawal is 8 decimal places. |
| wdQuota | String | The withdrawal limit in the past 24 hours (including `on-chain withdrawal` and `internal transfer`), unit in `USD` |
| usedWdQuota | String | The amount of currency withdrawal used in the past 24 hours, unit in `USD` |
| fee | String | The fixed withdrawal feeApply to `on-chain withdrawal` |
| minFee | String | The minimum withdrawal fee for normal addressApply to `on-chain withdrawal`(Deprecated) |
| maxFee | String | The maximum withdrawal fee for normal addressApply to `on-chain withdrawal`(Deprecated) |
| minFeeForCtAddr | String | The minimum withdrawal fee for contract addressApply to `on-chain withdrawal`(Deprecated) |
| maxFeeForCtAddr | String | The maximum withdrawal fee for contract addressApply to `on-chain withdrawal`(Deprecated) |
| burningFeeRate | String | Burning fee rate, e.g "0.05" represents "5%".Some currencies may charge combustion fees. The burning fee is deducted based on the withdrawal quantity (excluding gas fee) multiplied by the burning fee rate.Apply to `on-chain withdrawal` |
| mainNet | Boolean | If current chain is main net, then it will return `true`, otherwise it will return `false` |
| needTag | Boolean | Whether tag/memo information is required for withdrawal, e.g. `EOS` will return `true` |
| minDepArrivalConfirm | String | The minimum number of blockchain confirmations to acknowledge fund deposit. The account is credited after that, but the deposit can not be withdrawn |
| minWdUnlockConfirm | String | The minimum number of blockchain confirmations required for withdrawal of a deposit |
| depQuotaFixed | String | The fixed deposit limit, unit in `USD`Return empty string if there is no deposit limit |
| usedDepQuotaFixed | String | The used amount of fixed deposit quota, unit in `USD`Return empty string if there is no deposit limit |
| depQuoteDailyLayer2 | String | The layer2 network daily deposit limit |

### Get balance

Retrieve the funding account balances of all the assets and the amount that is available or on hold.

Only asset information of a currency with a balance greater than 0 will be returned.


#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/balances`

Request Example

```
GET /api/v5/asset/balances
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get balane
result = fundingAPI.get_balances()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "availBal": "37.11827078",
 "bal": "37.11827078",
 "ccy": "ETH",
 "frozenBal": "0"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| bal | String | Balance |
| frozenBal | String | Frozen balance |
| availBal | String | Available balance |

### Get non-tradable assets

Retrieve the funding account balances of all the assets and the amount that is available or on hold.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/non-tradable-assets`

Request Example

```
GET /api/v5/asset/non-tradable-assets
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

result = fundingAPI.get_non_tradable_assets()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "bal": "989.84719571",
 "burningFeeRate": "",
 "canWd": true,
 "ccy": "CELT",
 "chain": "CELT-OKTC",
 "ctAddr": "f403fb",
 "fee": "2",
 "feeCcy": "USDT",
 "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/221/460DA8A592400393.png",
 "minWd": "0.1",
 "name": "",
 "needTag": false,
 "wdAll": false,
 "wdTickSz": "8"
 },
 {
 "bal": "0.001",
 "burningFeeRate": "",
 "canWd": true,
 "ccy": "MEME",
 "chain": "MEME-ERC20",
 "ctAddr": "09b760",
 "fee": "5",
 "feeCcy": "USDT",
 "logoLink": "https://static.coinall.ltd/cdn/assets/imgs/207/2E664E470103C613.png",
 "minWd": "0.001",
 "name": "MEME Inu",
 "needTag": false,
 "wdAll": false,
 "wdTickSz": "8"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. `CELT` |
| name | String | Chinese name of currency. There is no related name when it is not shown. |
| logoLink | String | Logo link of currency |
| bal | String | Withdrawable balance |
| canWd | Boolean | Availability to withdraw to chain. `false`: not available `true`: available |
| chain | String | Chain for withdrawal |
| minWd | String | Minimum withdrawal amount of currency in a single transaction |
| wdAll | Boolean | Whether all assets in this currency must be withdrawn at one time |
| fee | String | Fixed withdrawal fee |
| feeCcy | String | Fixed withdrawal fee unit, e.g. `USDT` |
| burningFeeRate | String | Burning fee rate, e.g "0.05" represents "5%".Some currencies may charge combustion fees. The burning fee is deducted based on the withdrawal quantity (excluding gas fee) multiplied by the burning fee rate. |
| ctAddr | String | Last 6 digits of contract address |
| wdTickSz | String | Withdrawal precision, indicating the number of digits after the decimal point |
| needTag | Boolean | Whether tag/memo information is required for withdrawal |

### Get account asset valuation

View account asset valuation

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/asset-valuation`

Request Example

```
GET /api/v5/asset/asset-valuation
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get account asset valuation
result = fundingAPI.get_asset_valuation()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Asset valuation calculation unit BTC, USDTUSD, CNY, JP, KRW, RUB, EURVND, IDR, INR, PHP, THB, TRY AUD, SGD, ARS, SAR, AED, IQD The default is the valuation in BTC. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "details": {
 "classic": "124.6",
 "earn": "1122.73",
 "funding": "0.09",
 "trading": "2544.28"
 },
 "totalBal": "3790.09",
 "ts": "1637566660769"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| totalBal | String | Valuation of total account assets |
| ts | String | Unix timestamp format in milliseconds, e.g.`1597026383085` |
| details | Object | Asset valuation details for each account |
| > funding | String | Funding account |
| > trading | String | Trading account |
| > classic | String | [Deprecated] Classic account |
| > earn | String | Earn account |

### Funds transfer

Only API keys with `Trade` privilege can call this endpoint.

This endpoint supports the transfer of funds between your funding account and trading account, and from the master account to sub-accounts.

Sub-account can transfer out to master account by default. Need to call [Set permission of transfer out](/docs-v5/en/#sub-account-rest-api-set-permission-of-transfer-out) to grant privilege first if you want sub-account transferring to another sub-account (sub-accounts need to belong to same master account.)

The success or failure of the request does not necessarily reflect the actual transfer result. Recommend checking the transfer status by calling "Get funds transfer state" to confirm the final result.

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID + Currency

#### HTTP Request

`POST /api/v5/asset/transfer`

Request Example

```
# Transfer 1.5 USDT from funding account to Trading account when current account is master-account
POST /api/v5/asset/transfer
body
{
 "ccy":"USDT",
 "amt":"1.5",
 "from":"6",
 "to":"18"
}

# Transfer 1.5 USDT from funding account to subAccount when current account is master-account
POST /api/v5/asset/transfer
body
{
 "ccy":"USDT",
 "type":"1",
 "amt":"1.5",
 "from":"6",
 "to":"6",
 "subAcct":"mini"
}

# Transfer 1.5 USDT from funding account to subAccount when current account is sub-account
POST /api/v5/asset/transfer
body
{
 "ccy":"USDT",
 "type":"4",
 "amt":"1.5",
 "from":"6",
 "to":"6",
 "subAcct":"mini"
}
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Funds transfer
result = fundingAPI.funds_transfer(
 ccy="USDT",
 amt="1.5",
 from_="6",
 to="18"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | String | No | Transfer type`0`: transfer within account`1`: master account to sub-account (Only applicable to API Key from master account)`2`: sub-account to master account (Only applicable to API Key from master account)`3`: sub-account to master account (Only applicable to APIKey from sub-account)`4`: sub-account to sub-account (Only applicable to APIKey from sub-account, and target account needs to be another sub-account which belongs to same master account. Sub-account directly transfer out permission is disabled by default, set permission please refer to Set permission of transfer out)The default is `0`.If you want to make transfer between sub-accounts by master account API key, refer to Master accounts manage the transfers between sub-accounts |
| ccy | String | Yes | Transfer currency, e.g. `USDT` |
| amt | String | Yes | Amount to be transferred |
| from | String | Yes | The remitting account`6`: Funding account`18`: Trading account |
| to | String | Yes | The beneficiary account`6`: Funding account`18`: Trading account |
| subAcct | String | Conditional | Name of the sub-accountWhen `type` is `1`/`2`/`4`, this parameter is required. |
| loanTrans | Boolean | No | Whether or not borrowed coins can be transferred out under `Spot mode`/`Multi-currency margin`/`Portfolio margin``true`: borrowed coins can be transferred out`false`: borrowed coins cannot be transferred outthe default is `false` |
| omitPosRisk | String | No | Ignore position riskDefault is `false`Applicable to `Portfolio margin` |
| clientId | String | No | Client-supplied IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "transId": "754147",
 "ccy": "USDT",
 "clientId": "",
 "from": "6",
 "amt": "0.1",
 "to": "18"
 }
 ]
}

```

#### Response Parameters

Response Example

| Parameter | Type | Description |
| --- | --- | --- |
| transId | String | Transfer ID |
| clientId | String | Client-supplied ID |
| ccy | String | Currency |
| from | String | The remitting account |
| amt | String | Transfer amount |
| to | String | The beneficiary account |

### Get funds transfer state

Retrieve the transfer state data of the last 2 weeks.

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/transfer-state`

Request Example

```
GET /api/v5/asset/transfer-state?transId=1&type=1
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get funds transfer state
result = fundingAPI.transfer_state(
 transId="248424899",
 type="0"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| transId | String | Conditional | Transfer IDEither transId or clientId is required. If both are passed, transId will be used. |
| clientId | String | Conditional | Client-supplied IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| type | String | No | Transfer type`0`: transfer within account `1`: master account to sub-account (Only applicable to API Key from master account) `2`: sub-account to master account (Only applicable to API Key from master account)`3`: sub-account to master account (Only applicable to APIKey from sub-account)`4`: sub-account to sub-account (Only applicable to APIKey from sub-account, and target account needs to be another sub-account which belongs to same master account)The default is `0`.For Custody accounts, can choose not to pass this parameter or pass `0`. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "amt": "1.5",
 "ccy": "USDT",
 "clientId": "",
 "from": "18",
 "instId": "", //deprecated
 "state": "success",
 "subAcct": "test",
 "to": "6",
 "toInstId": "", //deprecated
 "transId": "1",
 "type": "1"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| transId | String | Transfer ID |
| clientId | String | Client-supplied ID |
| ccy | String | Currency, e.g. `USDT` |
| amt | String | Amount to be transferred |
| type | String | Transfer type`0`: transfer within account`1`: master account to sub-account (Only applicable to API Key from master account) `2`: sub-account to master account (Only applicable to APIKey from master account)`3`: sub-account to master account (Only applicable to APIKey from sub-account)`4`: sub-account to sub-account (Only applicable to APIKey from sub-account, and target account needs to be another sub-account which belongs to same master account) |
| from | String | The remitting account`6`: Funding account`18`: Trading account |
| to | String | The beneficiary account`6`: Funding account`18`: Trading account |
| subAcct | String | Name of the sub-account |
| instId | String | deprecated |
| toInstId | String | deprecated |
| state | String | Transfer state`success``pending``failed` |

### Asset bills details

Query the billing record in the past month.

#### Rate Limit: 6 Requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/bills`

Request Example

```
GET /api/v5/asset/bills
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get asset bills details
result = fundingAPI.get_bills()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency |
| type | String | No | Bill type`1`: Deposit`2`: Withdrawal`13`: Canceled withdrawal`20`: Transfer to sub account (for master account)`21`: Transfer from sub account (for master account)`22`: Transfer out from sub to master account (for sub-account)`23`: Transfer in from master to sub account (for sub-account)`28`: Manually claimed Airdrop`47`: System reversal`48`: Event Reward`49`: Event Giveaway`68`: Fee rebate (by rebate card)`72`: Token received`73`: Token given away`74`: Token refunded`75`: [Simple earn flexible] Subscription`76`: [Simple earn flexible] Redemption`77`: Jumpstart distribute`78`: Jumpstart lock up`80`: DEFI/Staking subscription`82`: DEFI/Staking redemption`83`: Staking yield`84`: Violation fee`89`: Deposit yield`116`: [Fiat] Place an order`117`: [Fiat] Fulfill an order`118`: [Fiat] Cancel an order`124`: Jumpstart unlocking`130`: Transferred from Trading account`131`: Transferred to Trading account`132`: [P2P] Frozen by customer service`133`: [P2P] Unfrozen by customer service`134`: [P2P] Transferred by customer service`135`: Cross chain exchange`137`: [ETH Staking] Subscription`138`: [ETH Staking] Swapping`139`: [ETH Staking] Earnings`146`: Customer feedback`150`: Affiliate commission`151`: Referral reward`152`: Broker reward`160`: Dual Investment subscribe`161`: Dual Investment collection`162`: Dual Investment profit`163`: Dual Investment refund`172`: [Affiliate] Sub-affiliate commission`173`: [Affiliate] Fee rebate (by trading fee)`174`: Jumpstart Pay`175`: Locked collateral`176`: Loan`177`: Added collateral`178`: Returned collateral`179`: Repayment`180`: Unlocked collateral`181`: Airdrop payment`185`: [Broker] Convert reward`187`: [Broker] Convert transfer`189`: Mystery box bonus`195`: Untradable asset withdrawal`196`: Untradable asset withdrawal revoked`197`: Untradable asset deposit`198`: Untradable asset collection reduce`199`: Untradable asset collection increase`200`: Buy`202`: Price Lock Subscribe`203`: Price Lock Collection`204`: Price Lock Profit`205`: Price Lock Refund`207`: Dual Investment Lite Subscribe`208`: Dual Investment Lite Collection`209`: Dual Investment Lite Profit`210`: Dual Investment Lite Refund`212`: [Flexible loan] Multi-collateral loan collateral locked`215`: [Flexible loan] Multi-collateral loan collateral released`217`: [Flexible loan] Multi-collateral loan borrowed`218`: [Flexible loan] Multi-collateral loan repaid`232`: [Flexible loan] Subsidized interest received`220`: Delisted crypto`221`: Blockchain's withdrawal fee`222`: Withdrawal fee refund`223`: SWAP lead trading profit share`225`: Shark Fin subscribe`226`: Shark Fin collection`227`: Shark Fin profit`228`: Shark Fin refund`229`: Airdrop`232`: Subsidized interest received`233`: Broker rebate compensation`240`: Snowball subscribe`241`: Snowball refund`242`: Snowball profit`243`: Snowball trading failed`249`: Seagull subscribe`250`: Seagull collection`251`: Seagull profit`252`: Seagull refund`263`: Strategy bots profit share`265`: Signal revenue`266`: SPOT lead trading profit share`270`: DCD broker transfer`271`: DCD broker rebate`272`: [Convert] Buy Crypto/Fiat`273`: [Convert] Sell Crypto/Fiat`284`: [Custody] Transfer out trading sub-account`285`: [Custody] Transfer in trading sub-account`286`: [Custody] Transfer out custody funding account`287`: [Custody] Transfer in custody funding account`288`: [Custody] Fund delegation `289`: [Custody] Fund undelegation`299`: Affiliate recommendation commission`300`: Fee discount rebate`303`: Snowball market maker transfer`304`: [Simple Earn Fixed] Order submission`305`: [Simple Earn Fixed] Order redemption`306`: [Simple Earn Fixed] Principal distribution`307`: [Simple Earn Fixed] Interest distribution (early termination compensation)`308`: [Simple Earn Fixed] Interest distribution`309`: [Simple Earn Fixed] Interest distribution (extension compensation) `311`: Crypto dust auto-transfer in`313`: Sent by gift`314`: Received from gift`315`: Refunded from gift`328`: [SOL staking] Send Liquidity Staking Token reward`329`: [SOL staking] Subscribe Liquidity Staking Token staking`330`: [SOL staking] Mint Liquidity Staking Token`331`: [SOL staking] Redeem Liquidity Staking Token order`332`: [SOL staking] Settle Liquidity Staking Token order`333`: Trial fund reward`339`: [Simple Earn Fixed] Order submission`340`: [Simple Earn Fixed] Order failure refund`341`: [Simple Earn Fixed] Redemption`342`: [Simple Earn Fixed] Principal`343`: [Simple Earn Fixed] Interest`344`: [Simple Earn Fixed] Compensatory interest`345`: [Institutional Loan] Principal repayment`346`: [Institutional Loan] Interest repayment`347`: [Institutional Loan] Overdue penalty`348`: [BTC staking] Subscription`349`: [BTC staking] Redemption`350`: [BTC staking] Earnings`351`: [Institutional Loan] Loan disbursement`354`: Copy and bot rewards`361`: Deposit from closed sub-account`372`: Asset segregation`373`: Asset release `400`: Auto lend interest `408`: Auto earn USDG interest`476`: Transferred out to Cloud Exchange`477`: Transferred in from Cloud Exchange`509`: [OKUSD] Subscription`511`: [OKUSD] Redemption`516`: [OKUSD] Earnings |
| thirdPartyType | String | No | Third-party custody type. If not specified, defaults to `1` (for backward compatibility).`1`: Copper`2`: Komainu`5`: SCBWhen a master account is bound to multiple custody providers, use this parameter to filter bills by the specified custody provider. Applicable to bill types `284`–`289`. |
| clientId | String | No | Client-supplied ID for transfer or withdrawalA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "billId": "12344",
 "ccy": "BTC",
 "clientId": "",
 "balChg": "2",
 "bal": "12",
 "type": "1",
 "ts": "1597026383085",
 "notes": ""
 }]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| billId | String | Bill ID |
| ccy | String | Account balance currency |
| clientId | String | Client-supplied ID for transfer or withdrawal |
| balChg | String | Change in balance at the account level |
| bal | String | Balance at the account level |
| type | String | Bill type |
| notes | String | Notes |
| ts | String | Creation time, Unix timestamp format in milliseconds, e.g.`1597026383085` |

### Asset bills history

Query the billing records of all time since 1 February, 2021.

⚠️ IMPORTANT**: Data updates occur every 30 seconds. Update frequency may vary based on data volume - please be aware of potential delays during high-traffic periods.

#### Rate Limit: 1 Requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/bills-history`

**Request Example

```
GET /api/v5/asset/bills-history
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get asset bills details
result = fundingAPI.get_bills_history()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency |
| type | String | No | Bill type`1`: Deposit`2`: Withdrawal`13`: Canceled withdrawal`20`: Transfer to sub account (for master account)`21`: Transfer from sub account (for master account)`22`: Transfer out from sub to master account (for sub-account)`23`: Transfer in from master to sub account (for sub-account)`28`: Manually claimed Airdrop`47`: System reversal`48`: Event Reward`49`: Event Giveaway`68`: Fee rebate (by rebate card)`72`: Token received`73`: Token given away`74`: Token refunded`75`: [Simple earn flexible] Subscription`76`: [Simple earn flexible] Redemption`77`: Jumpstart distribute`78`: Jumpstart lock up`80`: DEFI/Staking subscription`82`: DEFI/Staking redemption`83`: Staking yield`84`: Violation fee`89`: Deposit yield`116`: [Fiat] Place an order`117`: [Fiat] Fulfill an order`118`: [Fiat] Cancel an order`124`: Jumpstart unlocking`130`: Transferred from Trading account`131`: Transferred to Trading account`132`: [P2P] Frozen by customer service`133`: [P2P] Unfrozen by customer service`134`: [P2P] Transferred by customer service`135`: Cross chain exchange`137`: [ETH Staking] Subscription`138`: [ETH Staking] Swapping`139`: [ETH Staking] Earnings`146`: Customer feedback`150`: Affiliate commission`151`: Referral reward`152`: Broker reward`160`: Dual Investment subscribe`161`: Dual Investment collection`162`: Dual Investment profit`163`: Dual Investment refund`172`: [Affiliate] Sub-affiliate commission`173`: [Affiliate] Fee rebate (by trading fee)`174`: Jumpstart Pay`175`: Locked collateral`176`: Loan`177`: Added collateral`178`: Returned collateral`179`: Repayment`180`: Unlocked collateral`181`: Airdrop payment`185`: [Broker] Convert reward`187`: [Broker] Convert transfer`189`: Mystery box bonus`195`: Untradable asset withdrawal`196`: Untradable asset withdrawal revoked`197`: Untradable asset deposit`198`: Untradable asset collection reduce`199`: Untradable asset collection increase`200`: Buy`202`: Price Lock Subscribe`203`: Price Lock Collection`204`: Price Lock Profit`205`: Price Lock Refund`207`: Dual Investment Lite Subscribe`208`: Dual Investment Lite Collection`209`: Dual Investment Lite Profit`210`: Dual Investment Lite Refund`212`: [Flexible loan] Multi-collateral loan collateral locked`215`: [Flexible loan] Multi-collateral loan collateral released`217`: [Flexible loan] Multi-collateral loan borrowed`218`: [Flexible loan] Multi-collateral loan repaid`232`: [Flexible loan] Subsidized interest received`220`: Delisted crypto`221`: Blockchain's withdrawal fee`222`: Withdrawal fee refund`223`: SWAP lead trading profit share`225`: Shark Fin subscribe`226`: Shark Fin collection`227`: Shark Fin profit`228`: Shark Fin refund`229`: Airdrop`232`: Subsidized interest received`233`: Broker rebate compensation`240`: Snowball subscribe`241`: Snowball refund`242`: Snowball profit`243`: Snowball trading failed`249`: Seagull subscribe`250`: Seagull collection`251`: Seagull profit`252`: Seagull refund`263`: Strategy bots profit share`265`: Signal revenue`266`: SPOT lead trading profit share`270`: DCD broker transfer`271`: DCD broker rebate`272`: [Convert] Buy Crypto/Fiat`273`: [Convert] Sell Crypto/Fiat`284`: [Custody] Transfer out trading sub-account`285`: [Custody] Transfer in trading sub-account`286`: [Custody] Transfer out custody funding account`287`: [Custody] Transfer in custody funding account`288`: [Custody] Fund delegation `289`: [Custody] Fund undelegation`299`: Affiliate recommendation commission`300`: Fee discount rebate`303`: Snowball market maker transfer`304`: [Simple Earn Fixed] Order submission`305`: [Simple Earn Fixed] Order redemption`306`: [Simple Earn Fixed] Principal distribution`307`: [Simple Earn Fixed] Interest distribution (early termination compensation)`308`: [Simple Earn Fixed] Interest distribution`309`: [Simple Earn Fixed] Interest distribution (extension compensation) `311`: Crypto dust auto-transfer in`313`: Sent by gift`314`: Received from gift`315`: Refunded from gift`328`: [SOL staking] Send Liquidity Staking Token reward`329`: [SOL staking] Subscribe Liquidity Staking Token staking`330`: [SOL staking] Mint Liquidity Staking Token`331`: [SOL staking] Redeem Liquidity Staking Token order`332`: [SOL staking] Settle Liquidity Staking Token order`333`: Trial fund reward`339`: [Simple Earn Fixed] Order submission`340`: [Simple Earn Fixed] Order failure refund`341`: [Simple Earn Fixed] Redemption`342`: [Simple Earn Fixed] Principal`343`: [Simple Earn Fixed] Interest`344`: [Simple Earn Fixed] Compensatory interest`345`: [Institutional Loan] Principal repayment`346`: [Institutional Loan] Interest repayment`347`: [Institutional Loan] Overdue penalty`348`: [BTC staking] Subscription`349`: [BTC staking] Redemption`350`: [BTC staking] Earnings`351`: [Institutional Loan] Loan disbursement`354`: Copy and bot rewards`361`: Deposit from closed sub-account`372`: Asset segregation`373`: Asset release`400`: auto lend interest`408`: Auto earn interest (USDG earn)`476`: Transferred out to Cloud Exchange`477`: Transferred in from Cloud Exchange`509`: [OKUSD] Subscription`511`: [OKUSD] Redemption`516`: [OKUSD] Earnings |
| thirdPartyType | String | No | Third-party custody type. If not specified, defaults to `1` (for backward compatibility).`1`: Copper`2`: Komainu`5`: SCBWhen a master account is bound to multiple custody providers, use this parameter to filter bills by the specified custody provider. Applicable to bill types `284`–`289`. |
| clientId | String | No | Client-supplied ID for transfer or withdrawalA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| after | String | No | Pagination of data to return records earlier than the requested `ts` or `billId`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |
| pagingType | String | No | PagingType`1`: Timestamp of the bill record`2`: Bill ID of the bill recordThe default is `1` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "billId": "12344",
 "ccy": "BTC",
 "clientId": "",
 "balChg": "2",
 "bal": "12",
 "type": "1",
 "ts": "1597026383085",
 "notes": ""
 }]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| billId | String | Bill ID |
| ccy | String | Account balance currency |
| clientId | String | Client-supplied ID for transfer or withdrawal |
| balChg | String | Change in balance at the account level |
| bal | String | Balance at the account level |
| type | String | Bill type |
| notes | String | Notes |
| ts | String | Creation time, Unix timestamp format in milliseconds, e.g.`1597026383085` |

### Get deposit address

Retrieve the deposit addresses of currencies, including previously-used addresses.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/deposit-address`

Request Example

```
GET /api/v5/asset/deposit-address?ccy=BTC
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get deposit address
result = fundingAPI.get_deposit_address(
 ccy="USDT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency, e.g. `BTC` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "chain": "BTC-Bitcoin",
 "ctAddr": "",
 "ccy": "BTC",
 "to": "6",
 "addr": "39XNxK1Ryqgg3Bsyn6HzoqV4Xji25pNkv6",
 "verifiedName":"John Corner",
 "selected": true
 },
 {
 "chain": "BTC-OKC",
 "ctAddr": "",
 "ccy": "BTC",
 "to": "6",
 "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
 "verifiedName":"John Corner",
 "selected": true
 },
 {
 "chain": "BTC-ERC20",
 "ctAddr": "5807cf",
 "ccy": "BTC",
 "to": "6",
 "addr": "0x66d0edc2e63b6b992381ee668fbcb01f20ae0428",
 "verifiedName":"John Corner",
 "selected": true
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| addr | String | Deposit address |
| tag | String | Deposit tag (This will not be returned if the currency does not require a tag for deposit) |
| memo | String | Deposit memo (This will not be returned if the currency does not require a memo for deposit) |
| pmtId | String | Deposit payment ID (This will not be returned if the currency does not require a payment_id for deposit) |
| addrEx | Object | Deposit address attachment (This will not be returned if the currency does not require this)e.g. `TONCOIN` attached tag name is `comment`, the return will be `{'comment':'123456'}` |
| ccy | String | Currency, e.g. `BTC` |
| chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20` |
| to | String | The beneficiary account`6`: Funding account `18`: Trading accountThe users under some entity (e.g. Brazil) only support deposit to trading account. |
| verifiedName | String | Verified name (for recipient) |
| selected | Boolean | Return `true` if the current deposit address is selected by the website page |
| ctAddr | String | Last 6 digits of contract address |

### Get deposit history

Retrieve the deposit records according to the currency, deposit status, and time range in reverse chronological order. The 100 most recent records are returned by default.
Websocket API is also available, refer to [Deposit info channel](/docs-v5/en/#funding-account-websocket-deposit-info-channel).

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/deposit-history`

Request Example

```
GET /api/v5/asset/deposit-history

# Query deposit history from 2022-06-01 to 2022-07-01
GET /api/v5/asset/deposit-history?ccy=BTC&after=1654041600000&before=1656633600000
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Get deposit history
result = fundingAPI.get_deposit_history()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, e.g. `BTC` |
| depId | String | No | Deposit ID |
| fromWdId | String | No | Internal transfer initiator's withdrawal IDIf the deposit comes from internal transfer, this field displays the withdrawal ID of the internal transfer initiator |
| txId | String | No | Hash record of the deposit |
| type | String | No | Deposit Type`3`: internal transfer`4`: deposit from chain |
| state | String | No | Status of deposit `0`: waiting for confirmation`1`: deposit credited `2`: deposit successful `8`: pending due to temporary deposit suspension on this crypto currency`11`: match the address blacklist`12`: account or deposit is frozen`13`: sub-account deposit interception`14`: KYC limit `17`: Pending response from Travel Rule vendor |
| after | String | No | Pagination of data to return records earlier than the requested ts, Unix timestamp format in milliseconds, e.g. `1654041600000` |
| before | String | No | Pagination of data to return records newer than the requested ts, Unix timestamp format in milliseconds, e.g. `1656633600000` |
| limit | string | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "actualDepBlkConfirm": "2",
 "amt": "1",
 "areaCodeFrom": "",
 "ccy": "USDT",
 "chain": "USDT-TRC20",
 "depId": "88****33",
 "from": "",
 "fromWdId": "",
 "state": "2",
 "to": "TN4hGjVXMzy*********9b4N1aGizqs",
 "ts": "1674038705000",
 "txId": "fee235b3e812********857d36bb0426917f0df1802"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| chain | String | Chain name |
| amt | String | Deposit amount |
| from | String | Deposit accountIf the deposit comes from an internal transfer, this field displays the account information of the internal transfer initiator, which can be a mobile phone number or email address (masked), and will return "" in other cases |
| areaCodeFrom | String | If `from` is a phone number, this parameter return area code of the phone number |
| to | String | Deposit addressIf the deposit comes from the on-chain, this field displays the on-chain address, and will return "" in other cases |
| txId | String | Hash record of the deposit |
| ts | String | The timestamp that the deposit record is created, Unix timestamp format in milliseconds, e.g. `1655251200000` |
| state | String | Status of deposit`0`: Waiting for confirmation`1`: Deposit credited `2`: Deposit successful `8`: Pending due to temporary deposit suspension on this crypto currency`11`: Match the address blacklist`12`: Account or deposit is frozen`13`: Sub-account deposit interception`14`: KYC limit |
| depId | String | Deposit ID |
| fromWdId | String | Internal transfer initiator's withdrawal IDIf the deposit comes from internal transfer, this field displays the withdrawal ID of the internal transfer initiator, and will return "" in other cases |
| actualDepBlkConfirm | String | The actual amount of blockchain confirmed in a single deposit |

About deposit state
Waiting for confirmation** is that the required number of blockchain confirmations has not been reached. **Deposit credited** is that there is sufficient number of blockchain confirmations for the currency to be credited to the account, but it cannot be withdrawn yet. **Deposit successful** means the crypto has been credited to the account and it can be withdrawn.

### Withdrawal

Only supported withdrawal of assets from funding account. Common sub-account does not support withdrawal.

The API can only make withdrawal to verified addresses/account, and verified addresses can be set by WEB/APP.

About tag

Some token deposits require a deposit address and a tag (e.g. Memo/Payment ID), which is a string that guarantees the uniqueness of your deposit address. Follow the deposit procedure carefully, or you may risk losing your assets.

For currencies with labels, if it is a withdrawal between OKX users, please use internal transfer instead of online withdrawal

The following content only applies to users residing in the United Arab Emirates

Due to local laws and regulations in your country or region, a certain ratio of user assets must be stored in cold wallets. We will perform cold-to-hot wallet asset transfers from time to time. However, if assets in hot wallets are not sufficient to meet user withdrawal demands, an extra step is needed to transfer cold wallet assets to the hot wallet. This may cause delays of up to 24 hours to receive withdrawals.

Learn more (https://www.okx.com/help/what-is-a-segregated-wallet-and-why-is-my-withdrawal-delayed)

Users under certain entities need to provide additional information for withdrawal

Bahamas entity users refer to https://www.okx.com/docs-v5/log_en/#2024-08-08-withdrawal-api-adjustment-for-bahama-entity-users

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/asset/withdrawal`

Request Example

```
# on-chain withdrawal
POST /api/v5/asset/withdrawal
body
{
 "amt":"1",
 "dest":"4",
 "ccy":"BTC",
 "chain":"BTC-Bitcoin",
 "toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw"
}

# internal withdrawal
POST /api/v5/asset/withdrawal
body
{
 "amt":"10",
 "dest":"3",
 "ccy":"USDT",
 "areaCode":"86",
 "toAddr":"15651000000"
}

# Specific entity users need to provide receiver's info
POST /api/v5/asset/withdrawal
body
{
 "amt":"1",
 "dest":"4",
 "ccy":"BTC",
 "chain":"BTC-Bitcoin",
 "toAddr":"17DKe3kkkkiiiiTvAKKi2vMPbm1Bz3CMKw",
 "rcvrInfo":{
 "walletType":"exchange",
 "exchId":"did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
 "rcvrFirstName":"Bruce",
 "rcvrLastName":"Wayne"
 }
}
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Withdrawal
result = fundingAPI.withdrawal(
 ccy="USDT",
 toAddr="TXtvfb7cdrn6VX9H49mgio8bUxZ3DGfvYF",
 amt="100",
 dest="4",
 chain="USDT-TRC20"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency, e.g. `USDT` |
| amt | String | Yes | Withdrawal amountWithdrawal fee is not included in withdrawal amount. Please reserve sufficient transaction fees when withdrawing.You can get fee amount by Get currencies.For `internal transfer`, transaction fee is always `0`. |
| dest | String | Yes | Withdrawal method`3`: internal transfer`4`: on-chain withdrawal |
| toAddr | String | Yes | `toAddr` should be a trusted address/account. If your `dest` is `4`, some crypto currency addresses are formatted as `'address:tag'`, e.g. `'ARDOR-7JF3-8F2E-QUWZ-CAN7F:123456'`If your `dest` is `3`,`toAddr` should be a recipient address which can be UID, email, phone or login account name (account name is only for sub-account). |
| toAddrType | String | No | Address type`1`: wallet address, email, phone, or login account name`2`: UID (applicable only when dest=`3`) |
| chain | String | Conditional | Chain nameThere are multiple chains under some currencies, such as `USDT` has `USDT-ERC20`, `USDT-TRC20`If the parameter is not filled in, the default will be the main chain.When you withdrawal the non-tradable asset, if the parameter is not filled in, the default will be the unique withdrawal chain.Apply to `on-chain withdrawal`.You can get supported chain name by the endpoint of Get currencies. |
| areaCode | String | Conditional | Area code for the phone number, e.g. `86`If `toAddr` is a phone number, this parameter is required.Apply to `internal transfer` |
| rcvrInfo | Object | Conditional | Recipient informationFor the specific entity users to do on-chain withdrawal/lightning withdrawal, this information is required. |
| > walletType | String | Yes | Wallet Type`exchange`: Withdraw to exchange wallet`private`: Withdraw to private walletFor the wallet belongs to business recipient, `rcvrFirstName` may input the company name, `rcvrLastName` may input "N/A", location info may input the registered address of the company. |
| > exchId | String | Conditional | Exchange IDYou can query supported exchanges through the endpoint of Get exchange list (public)If the exchange is not in the exchange list, fill in '0' in this field. Apply to walletType = `exchange` |
| > rcvrFirstName | String | Conditional | Receiver's first name, e.g. `Bruce` |
| > rcvrLastName | String | Conditional | Receiver's last name, e.g. `Wayne` |
| > rcvrCountry | String | Conditional | The recipient's country, e.g. `United States`You must enter an English country name or a two letter country code (ISO 3166-1). Please refer to the `Country Name` and `Country Code` in the country information table below. |
| > rcvrCountrySubDivision | String | Conditional | State/Province of the recipient, e.g. `California` |
| > rcvrTownName | String | Conditional | The town/city where the recipient is located, e.g. `San Jose` |
| > rcvrStreetName | String | Conditional | Recipient's street address, e.g. `Clementi Avenue 1` |
| clientId | String | No | Client-supplied IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "amt": "0.1",
 "wdId": "67485",
 "ccy": "BTC",
 "clientId": "",
 "chain": "BTC-Bitcoin"
 }]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20` |
| amt | String | Withdrawal amount |
| wdId | String | Withdrawal ID |
| clientId | String | Client-supplied IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

#### Country information

| Country name | Country code |
| --- | --- |
| Afghanistan | AF |
| Albania | AL |
| Algeria | DZ |
| Andorra | AD |
| Angola | AO |
| Anguilla | AI |
| Antigua and Barbuda | AG |
| Argentina | AR |
| Armenia | AM |
| Australia | AU |
| Austria | AT |
| Azerbaijan | AZ |
| Bahamas | BS |
| Bahrain | BH |
| Bangladesh | BD |
| Barbados | BB |
| Belarus | BY |
| Belgium | BE |
| Belize | BZ |
| Benin | BJ |
| Bermuda | BM |
| Bhutan | BT |
| Bolivia | BO |
| Bosnia and Herzegovina | BA |
| Botswana | BW |
| Brazil | BR |
| British Virgin Islands | VG |
| Brunei | BN |
| Bulgaria | BG |
| Burkina Faso | BF |
| Burundi | BI |
| Cambodia | KH |
| Cameroon | CM |
| Canada | CA |
| Cape Verde | CV |
| Cayman Islands | KY |
| Central African Republic | CF |
| Chad | TD |
| Chile | CL |
| Colombia | CO |
| Comoros | KM |
| Congo (Republic) | CG |
| Congo (Democratic Republic) | CD |
| Costa Rica | CR |
| Cote d´Ivoire (Ivory Coast) | CI |
| Croatia | HR |
| Cuba | CU |
| Cyprus | CY |
| Czech Republic | CZ |
| Denmark | DK |
| Djibouti | DJ |
| Dominica | DM |
| Dominican Republic | DO |
| Ecuador | EC |
| Egypt | EG |
| El Salvador | SV |
| Equatorial Guinea | GQ |
| Eritrea | ER |
| Estonia | EE |
| Ethiopia | ET |
| Fiji | FJ |
| Finland | FI |
| France | FR |
| Gabon | GA |
| Gambia | GM |
| Georgia | GE |
| Germany | DE |
| Ghana | GH |
| Greece | GR |
| Grenada | GD |
| Guatemala | GT |
| Guinea | GN |
| Guinea-Bissau | GW |
| Guyana | GY |
| Haiti | HT |
| Honduras | HN |
| Hong Kong | HK |
| Hungary | HU |
| Iceland | IS |
| India | IN |
| Indonesia | ID |
| Iran | IR |
| Iraq | IQ |
| Ireland | IE |
| Israel | IL |
| Italy | IT |
| Jamaica | JM |
| Japan | JP |
| Jordan | JO |
| Kazakhstan | KZ |
| Kenya | KE |
| Kiribati | KI |
| North Korea | KP |
| South Korea | KR |
| Kuwait | KW |
| Kyrgyzstan | KG |
| Laos | LA |
| Latvia | LV |
| Lebanon | LB |
| Lesotho | LS |
| Liberia | LR |
| Libya | LY |
| Liechtenstein | LI |
| Lithuania | LT |
| Luxembourg | LU |
| Macau | MO |
| Macedonia | MK |
| Madagascar | MG |
| Malawi | MW |
| Malaysia | MY |
| Maldives | MV |
| Mali | ML |
| Malta | MT |
| Marshall Islands | MH |
| Mauritania | MR |
| Mauritius | MU |
| Mexico | MX |
| Micronesia | FM |
| Moldova | MD |
| Monaco | MC |
| Mongolia | MN |
| Montenegro | ME |
| Morocco | MA |
| Mozambique | MZ |
| Myanmar (Burma) | MM |
| Namibia | NA |
| Nauru | NR |
| Nepal | NP |
| Netherlands | NL |
| New Zealand | NZ |
| Nicaragua | NI |
| Niger | NE |
| Nigeria | NG |
| Norway | NO |
| Oman | OM |
| Pakistan | PK |
| Palau | PW |
| Panama | PA |
| Papua New Guinea | PG |
| Paraguay | PY |
| Peru | PE |
| Philippines | PH |
| Poland | PL |
| Portugal | PT |
| Qatar | QA |
| Romania | RO |
| Russia | RU |
| Rwanda | RW |
| Saint Kitts and Nevis | KN |
| Saint Lucia | LC |
| Saint Vincent and the Grenadines | VC |
| Samoa | WS |
| San Marino | SM |
| Sao Tome and Principe | ST |
| Saudi Arabia | SA |
| Senegal | SN |
| Serbia | RS |
| Seychelles | SC |
| Sierra Leone | SL |
| Singapore | SG |
| Slovakia | SK |
| Slovenia | SI |
| Solomon Islands | SB |
| Somalia | SO |
| South Africa | ZA |
| Spain | ES |
| Sri Lanka | LK |
| Sudan | SD |
| Suriname | SR |
| Swaziland | SZ |
| Sweden | SE |
| Switzerland | CH |
| Syria | SY |
| Taiwan | TW |
| Tajikistan | TJ |
| Tanzania | TZ |
| Thailand | TH |
| Timor-Leste (East Timor) | TL |
| Togo | TG |
| Tonga | TO |
| Trinidad and Tobago | TT |
| Tunisia | TN |
| Turkey | TR |
| Turkmenistan | TM |
| Tuvalu | TV |
| U.S. Virgin Islands | VI |
| Uganda | UG |
| Ukraine | UA |
| United Arab Emirates | AE |
| United Kingdom | GB |
| United States | US |
| Uruguay | UY |
| Uzbekistan | UZ |
| Vanuatu | VU |
| Vatican City | VA |
| Venezuela | VE |
| Vietnam | VN |
| Yemen | YE |
| Zambia | ZM |
| Zimbabwe | ZW |
| Kosovo | XK |
| South Sudan | SS |
| China | CN |
| Palestine | PS |
| Curacao | CW |
| Dominican Republic | DO |
| Dominican Republic | DO |
| Gibraltar | GI |
| New Caledonia | NC |
| Cook Islands | CK |
| Reunion | RE |
| Guernsey | GG |
| Guadeloupe | GP |
| Martinique | MQ |
| French Polynesia | PF |
| Faroe Islands | FO |
| Greenland | GL |
| Jersey | JE |
| Aruba | AW |
| Puerto Rico | PR |
| Isle of Man | IM |
| Guam | GU |
| Sint Maarten | SX |
| Turks and Caicos | TC |
| Åland Islands | AX |
| Caribbean Netherlands | BQ |
| British Indian Ocean Territory | IO |
| Christmas as Island | CX |
| Cocos (Keeling) Islands | CC |
| Falkland Islands (Islas Malvinas) | FK |
| Mayotte | YT |
| Niue | NU |
| Norfolk Island | NF |
| Northern Mariana Islands | MP |
| Pitcairn Islands | PN |
| Saint Helena, Ascension and Tristan da Cunha | SH |
| Collectivity of Saint Martin | MF |
| Saint Pierre and Miquelon | PM |
| Tokelau | TK |
| Wallis and Futuna | WF |
| American Samoa | AS |

### Cancel withdrawal

You can cancel normal withdrawal requests, but you cannot cancel withdrawal requests on Lightning.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/asset/cancel-withdrawal`

Request Example

```
POST /api/v5/asset/cancel-withdrawal
body {
 "wdId":"1123456"
}
```

```
import okx.Funding as Funding

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading: 0, Demo trading: 1

fundingAPI = Funding.FundingAPI(apikey, secretkey, passphrase, False, flag)

# Cancel withdrawal
result = fundingAPI.cancel_withdrawal(
 wdId="123456"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| wdId | String | Yes | Withdrawal ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "wdId": "1123456"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| wdId | String | Withdrawal ID |

If the code is equal to 0, it cannot be strictly considered that the withdrawal has been revoked. It only means that your request is accepted by the server. The actual result is subject to the status in the withdrawal history.

### Get withdrawal history

Retrieve the withdrawal records according to the currency, withdrawal status, and time range in reverse chronological order. The 100 most recent records are returned by default.

Websocket API is also available, refer to [Withdrawal info channel](/docs-v5/en/#funding-account-websocket-withdrawal-info-channel).

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/withdrawal-history`

Request Example

```
GET /api/v5/asset/withdrawal-history

# Query withdrawal history from 2022-06-01 to 2022-07-01
GET /api/v5/asset/withdrawal-history?ccy=BTC&after=1654041600000&before=1656633600000
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, e.g. `BTC` |
| wdId | String | No | Withdrawal ID |
| clientId | String | No | Client-supplied IDA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| txId | String | No | Hash record of the deposit |
| type | String | No | Withdrawal type`3`: Internal transfer`4`: On-chain withdrawal |
| state | String | No | Status of withdrawalStage 1 : Pending withdrawal`19`: insufficient balance in the hot wallet`17`: Pending response from Travel Rule vendor`10`: Waiting transfer`0`: Waiting withdrawal`4`/`5`/`6`/`8`/`9`/`12`: Waiting manual review`7`: Approved> `0`, `17`, `19` can be cancelled, other statuses cannot be cancelledStage 2 : Withdrawal in progress (Applicable to on-chain withdrawals, internal transfers do not have this stage)`1`: Broadcasting your transaction to chain`15`: Pending transaction validation`16`: Due to local laws and regulations, your withdrawal may take up to 24 hours to arrive`-3`: Canceling Final stage`-2`: Canceled `-1`: Failed`2`: Success |
| after | String | No | Pagination of data to return records earlier than the requested ts, Unix timestamp format in milliseconds, e.g. `1654041600000` |
| before | String | No | Pagination of data to return records newer than the requested ts, Unix timestamp format in milliseconds, e.g. `1656633600000` |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "note": "",
 "chain": "ETH-Ethereum",
 "fee": "0.007",
 "feeCcy": "ETH",
 "ccy": "ETH",
 "clientId": "",
 "toAddrType": "1",
 "amt": "0.029809",
 "txId": "0x35c******b360a174d",
 "from": "156****359",
 "areaCodeFrom": "86",
 "to": "0xa30d1fab********7CF18C7B6C579",
 "areaCodeTo": "",
 "state": "2",
 "ts": "1655251200000",
 "nonTradableAsset": false,
 "wdId": "15447421"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20` |
| nonTradableAsset | Boolean | Whether it is a non-tradable asset or not`true`: non-tradable asset, `false`: tradable asset |
| amt | String | Withdrawal amount |
| ts | String | Time the withdrawal request was submitted, Unix timestamp format in milliseconds, e.g. `1655251200000`. |
| from | String | Withdrawal account It can be `email`/`phone`/`sub-account name` |
| areaCodeFrom | String | Area code for the phone numberIf `from` is a phone number, this parameter returns the area code for the phone number |
| to | String | Receiving address |
| areaCodeTo | String | Area code for the phone numberIf `to` is a phone number, this parameter returns the area code for the phone number |
| toAddrType | String | Address type`1`: wallet address, email, phone, or login account name`2`: UID |
| tag | String | Some currencies require a tag for withdrawals. This is not returned if not required. |
| pmtId | String | Some currencies require a payment ID for withdrawals. This is not returned if not required. |
| memo | String | Some currencies require this parameter for withdrawals. This is not returned if not required. |
| addrEx | Object | Withdrawal address attachment (This will not be returned if the currency does not require this) e.g. TONCOIN attached tag name is comment, the return will be {'comment':'123456'} |
| txId | String | Hash record of the withdrawalThis parameter will return "" for internal transfers. |
| fee | String | Withdrawal fee amount |
| feeCcy | String | Withdrawal fee currency, e.g. `USDT` |
| state | String | Status of withdrawal |
| wdId | String | Withdrawal ID |
| clientId | String | Client-supplied ID |
| note | String | Withdrawal note |

### Get deposit withdraw status

Retrieve deposit's and withdrawal's detailed status and estimated complete time.

#### Rate Limit: 1 request per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/deposit-withdraw-status`

Request Example

```
# For deposit
GET /api/v5/asset/deposit-withdraw-status?txId=xxxxxx&to=1672734730284&ccy=USDT&chain=USDT-ERC20

# For withdrawal
GET /api/v5/asset/deposit-withdraw-status?wdId=200045249
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| wdId | String | Conditional | Withdrawal ID, use to retrieve withdrawal status Required to input one and only one of `wdId` and `txId` |
| txId | String | Conditional | Hash record of the deposit, use to retrieve deposit status Required to input one and only one of `wdId` and `txId` |
| ccy | String | Conditional | Currency type, e.g. `USDT` Required when retrieving deposit status with `txId` |
| to | String | Conditional | To address, the destination address in deposit Required when retrieving deposit status with `txId` |
| chain | String | Conditional | Currency chain information, e.g. USDT-ERC20 Required when retrieving deposit status with `txId` |

Response Example

```
{
 "code":"0",
 "data":[
 {
 "wdId": "200045249",
 "txId": "16f3638329xxxxxx42d988f97",
 "state": "Pending withdrawal: Wallet is under maintenance, please wait.",
 "estCompleteTime": "01/09/2023, 8:10:48 PM"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| estCompleteTime | String | Estimated complete timeThe timezone is `UTC+8`. The format is MM/dd/yyyy, h:mm:ss AM/PM estCompleteTime is only an approximate estimated time, for reference only. |
| state | String | The detailed stage and status of the deposit/withdrawal The message in front of the colon is the stage; the message after the colon is the ongoing status. |
| txId | String | Hash record on-chainFor withdrawal, if the `txId` has already been generated, it will return the value, otherwise, it will return "". |
| wdId | String | Withdrawal IDWhen retrieving deposit status, wdId returns blank "". |

Stage References

Deposit

Stage 1: On-chain transaction detection

Stage 2: Push deposit data to associated account

Stage 3: Receiving account credit

Final stage: Deposit complete

Withdrawal

Stage 1: Pending withdrawal

Stage 2: Withdrawal in progress

Final stage: Withdrawal complete / cancellation complete



### Get exchange list (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/asset/exchange-list`

Request Example

```
GET /api/v5/asset/exchange-list
```

```

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
 "exchId": "did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
 "exchName": "1xbet"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| exchName | String | Exchange name, e.g. `1xbet` |
| exchId | String | Exchange ID, e.g. `did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1` |

### Apply for monthly statement (last year)

Apply for monthly statement in the past year.

#### Rate Limit: 20 requests per month

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/asset/monthly-statement`

Request Example

```
POST /api/v5/asset/monthly-statement
body
{
 "month":"Jan"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| month | String | No | Month,last month by default. Valid value is `Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "ts": "1646892328000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Download link generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get monthly statement (last year)

Retrieve monthly statement in the past year.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/monthly-statement`

Request Example

```
GET /api/v5/asset/monthly-statement?month=Jan
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| month | String | Yes | Month, valid value is `Jan`, `Feb`, `Mar`, `Apr`,`May`, `Jun`, `Jul`,`Aug`, `Sep`,`Oct`,`Nov`,`Dec` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "fileHref": "http://xxx",
 "state": "finished",
 "ts": 1646892328000
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| fileHref | String | Download file link |
| ts | Int | Download link generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| state | String | Download link status "finished" "ongoing" |

### Get convert currencies

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/convert/currencies`

Request Example

```
GET /api/v5/asset/convert/currencies
```

#### Response parameters

none

Response Example

```
{
 "code": "0",
 "data": [
 {
 "min": "", // Deprecated
 "max": "", // Deprecated
 "ccy": "BTC"
 },
 {
 "min": "",
 "max": "",
 "ccy": "ETH"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency, e.g. BTC |
| min | String | Minimum amount to convert ( Deprecated ) |
| max | String | Maximum amount to convert ( Deprecated ) |

### Get convert currency pair

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/convert/currency-pair`

Request Example

```
GET /api/v5/asset/convert/currency-pair?fromCcy=USDT&toCcy=BTC
```

#### Response parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| fromCcy | String | Yes | Currency to convert from, e.g. `USDT` |
| toCcy | String | Yes | Currency to convert to, e.g. `BTC` |
| convertMode | String | No | `0`: standard convert (default) `1`: large order convert for VIP |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "baseCcy": "BTC",
 "baseCcyMax": "0.5",
 "baseCcyMin": "0.0001",
 "instId": "BTC-USDT",
 "quoteCcy": "USDT",
 "quoteCcyMax": "10000",
 "quoteCcyMin": "1"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Currency pair, e.g. `BTC-USDT` |
| baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT` |
| baseCcyMax | String | Maximum amount of base currency |
| baseCcyMin | String | Minimum amount of base currency |
| quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT` |
| quoteCcyMax | String | Maximum amount of quote currency |
| quoteCcyMin | String | Minimum amount of quote currency |

### Estimate quote

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: Instrument ID

#### HTTP Request

`POST /api/v5/asset/convert/estimate-quote`

Request Example

```
POST /api/v5/asset/convert/estimate-quote
body
{
 "baseCcy": "ETH",
 "quoteCcy": "USDT",
 "side": "buy",
 "rfqSz": "30",
 "rfqSzCcy": "USDT"
}
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| baseCcy | String | Yes | Base currency, e.g. `BTC` in `BTC-USDT` |
| quoteCcy | String | Yes | Quote currency, e.g. `USDT` in `BTC-USDT` |
| side | String | Yes | Trade side based on `baseCcy``buy` `sell` |
| rfqSz | String | Yes | RFQ amount |
| rfqSzCcy | String | Yes | RFQ currency |
| clQReqId | String | No | Client Order ID as assigned by the clientA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Order tagApplicable to broker user |
| convertMode | String | No | `0`: standard convert (default) `1`: large order convert for VIP |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "baseCcy": "ETH",
 "baseSz": "0.01023052",
 "clQReqId": "",
 "cnvtPx": "2932.40104429",
 "origRfqSz": "30",
 "quoteCcy": "USDT",
 "quoteId": "quoterETH-USDT16461885104612381",
 "quoteSz": "30",
 "quoteTime": "1646188510461",
 "rfqSz": "30",
 "rfqSzCcy": "USDT",
 "side": "buy",
 "ttlMs": "10000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| ttlMs | String | Validity period of quotation in milliseconds |
| clQReqId | String | Client Order ID as assigned by the client |
| quoteId | String | Quote ID |
| baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT` |
| quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT` |
| side | String | Trade side based on `baseCcy` |
| origRfqSz | String | Original RFQ amount |
| rfqSz | String | Real RFQ amount |
| rfqSzCcy | String | RFQ currency |
| cnvtPx | String | Convert price based on quote currency |
| baseSz | String | Convert amount of base currency |
| quoteSz | String | Convert amount of quote currency |

### Convert trade

You should make [estimate quote](/docs-v5/en/#funding-account-rest-api-estimate-quote) before convert trade.

Only assets in the trading account supported convert.

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

For the same side (buy/sell), there's a trading limit of 1 request per 5 seconds.

#### HTTP Request

`POST /api/v5/asset/convert/trade`

Request Example

```
POST /api/v5/asset/convert/trade
body
{
 "baseCcy": "ETH",
 "quoteCcy": "USDT",
 "side": "buy",
 "sz": "30",
 "szCcy": "USDT",
 "quoteId": "quoterETH-USDT16461885104612381"
}
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| quoteId | String | Yes | Quote ID |
| baseCcy | String | Yes | Base currency, e.g. `BTC` in `BTC-USDT` |
| quoteCcy | String | Yes | Quote currency, e.g. `USDT` in `BTC-USDT` |
| side | String | Yes | Trade side based on `baseCcy``buy` `sell` |
| sz | String | Yes | Quote amountThe quote amount should no more then RFQ amount |
| szCcy | String | Yes | Quote currency |
| clTReqId | String | No | Client Order ID as assigned by the clientA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Order tagApplicable to broker user |
| convertMode | String | No | `0`: standard convert (default) `1`: large order convert for VIP |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "baseCcy": "ETH",
 "clTReqId": "",
 "fillBaseSz": "0.01023052",
 "fillPx": "2932.40104429",
 "fillQuoteSz": "30",
 "instId": "ETH-USDT",
 "quoteCcy": "USDT",
 "quoteId": "quoterETH-USDT16461885104612381",
 "side": "buy",
 "state": "fullyFilled",
 "tradeId": "trader16461885203381437",
 "ts": "1646188520338"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| tradeId | String | Trade ID |
| quoteId | String | Quote ID |
| clTReqId | String | Client Order ID as assigned by the client |
| state | String | Trade state`fullyFilled`: success`rejected`: failed |
| instId | String | Currency pair, e.g. `BTC-USDT` |
| baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT` |
| quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT` |
| side | String | Trade side based on `baseCcy``buy``sell` |
| fillPx | String | Filled price based on quote currency |
| fillBaseSz | String | Filled amount for base currency |
| fillQuoteSz | String | Filled amount for quote currency |
| ts | String | Convert trade time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get convert history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/asset/convert/history`

Request Example

```
GET /api/v5/asset/convert/history
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| clTReqId | String | No | Client Order ID as assigned by the clientA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |
| tag | String | No | Order tagApplicable to broker userIf the convert trading used `tag`, this parameter is also required. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "clTReqId": "",
 "instId": "ETH-USDT",
 "side": "buy",
 "fillPx": "2932.401044",
 "baseCcy": "ETH",
 "quoteCcy": "USDT",
 "fillBaseSz": "0.01023052",
 "state": "fullyFilled",
 "tradeId": "trader16461885203381437",
 "fillQuoteSz": "30",
 "ts": "1646188520000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| tradeId | String | Trade ID |
| clTReqId | String | Client Order ID as assigned by the client |
| state | String | Trade state`fullyFilled` : success `rejected` : failed |
| instId | String | Currency pair, e.g. `BTC-USDT` |
| baseCcy | String | Base currency, e.g. `BTC` in `BTC-USDT` |
| quoteCcy | String | Quote currency, e.g. `USDT` in `BTC-USDT` |
| side | String | Trade side based on `baseCcy``buy` `sell` |
| fillPx | String | Filled price based on quote currency |
| fillBaseSz | String | Filled amount for base currency |
| fillQuoteSz | String | Filled amount for quote currency |
| ts | String | Convert trade time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get deposit payment methods

To display all the available fiat deposit payment methods

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/deposit-payment-methods`

Request Example

```
GET /api/v5/fiat/deposit-payment-methods?ccy=TRY
body
{
 "ccy" : "TRY",
}
```

```

```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Fiat currency, ISO-4217 3 digit currency code, e.g. `TRY` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ccy": "TRY",
 "paymentMethod": "TR_BANKS",
 "feeRate": "0",
 "minFee": "0",
 "limits": {
 "dailyLimit": "2147483647",
 "dailyLimitRemaining": "2147483647",
 "weeklyLimit": "2147483647",
 "weeklyLimitRemaining": "2147483647",
 "monthlyLimit": "",
 "monthlyLimitRemaining": "",
 "maxAmt": "1000000",
 "minAmt": "1",
 "lifetimeLimit": "2147483647"
 },
 "accounts": [
 {
 "paymentAcctId": "1",
 "acctNum": "TR740001592093703829602611",
 "recipientName": "John Doe",
 "bankName": "VakıfBank",
 "bankCode": "TVBATR2AXXX",
 "state": "active"
 },
 {
 "paymentAcctId": "2",
 "acctNum": "TR740001592093703829602622",
 "recipientName": "John Doe",
 "bankName": "FBHLTRISXXX",
 "bankCode": "",
 "state": "active"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Fiat currency |
| paymentMethod | String | The payment method associated with the currency`TR_BANKS``PIX``SEPA``XPULSE``NPP``US_WIRE` |
| feeRate | String | The fee rate for each deposit, expressed as a percentagee.g. `0.02` represents 2 percent fee for each transaction. |
| minFee | String | The minimum fee for each deposit |
| limits | Object | An object containing limits for various transaction intervals |
| > dailyLimit | String | The daily transaction limit |
| > dailyLimitRemaining | String | The remaining daily transaction limit |
| > weeklyLimit | String | The weekly transaction limit |
| > weeklyLimitRemaining | String | The remaining weekly transaction limit |
| > monthlyLimit | String | The monthly transaction limit |
| > monthlyLimitRemaining | String | The remaining monthly transaction limit |
| > maxAmt | String | The maximum amount allowed per transaction |
| > minAmt | String | The minimum amount allowed per transaction |
| > lifetimeLimit | String | The lifetime transaction limit. Return the configured value, "" if not configured |
| accounts | Array of Object | An array containing information about payment accounts associated with the currency and method. |
| > paymentAcctId | String | The account ID for withdrawal |
| > acctNum | String | The account number, which can be an IBAN or other bank account number. |
| > recipientName | String | The name of the recipient |
| > bankName | String | The name of the bank associated with the account |
| > bankCode | String | The SWIFT code / BIC / bank code associated with the account |
| > state | String | The state of the account`active` |

### Get withdrawal payment methods

To display all the available fiat withdrawal payment methods

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/withdrawal-payment-methods`

Request Example

```
GET /api/v5/fiat/withdrawal-payment-methods?ccy=TRY
```

```

```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Fiat currency, ISO-4217 3 digit currency code. e.g. `TRY` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ccy": "TRY",
 "paymentMethod": "TR_BANKS",
 "feeRate": "0.02",
 "minFee": "1",
 "limits": {
 "dailyLimit": "",
 "dailyLimitRemaining": "",
 "weeklyLimit": "",
 "weeklyLimitRemaining": "",
 "monthlyLimit": "",
 "monthlyLimitRemaining": "",
 "maxAmt": "",
 "minAmt": "",
 "lifetimeLimit": ""
 },
 "accounts": [
 {
 "paymentAcctId": "1",
 "acctNum": "TR740001592093703829602668",
 "recipientName": "John Doe",
 "bankName": "VakıfBank",
 "bankCode": "TVBATR2AXXX",
 "state": "active"
 },
 {
 "paymentAcctId": "2",
 "acctNum": "TR740001592093703829603024",
 "recipientName": "John Doe",
 "bankName": "Şekerbank",
 "bankCode": "SEKETR2AXXX",
 "state": "active"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Fiat currency |
| paymentMethod | String | The payment method associated with the currency`TR_BANKS``PIX``SEPA``XPULSE``NPP``US_WIRE``SG_FAST` |
| feeRate | String | The fee rate for each deposit, expressed as a percentage e.g. `0.02` represents 2 percent fee for each transaction. |
| minFee | String | The minimum fee for each deposit |
| limits | Object | An object containing limits for various transaction intervals |
| > dailyLimit | String | The daily transaction limit |
| > dailyLimitRemaining | String | The remaining daily transaction limit |
| > weeklyLimit | String | The weekly transaction limit |
| > weeklyLimitRemaining | String | The remaining weekly transaction limit |
| > monthlyLimit | String | The monthly transaction limit |
| > monthlyLimitRemaining | String | The remaining monthly transaction limit |
| > minAmt | String | The minimum amount allowed per transaction |
| > maxAmt | String | The maximum amount allowed per transaction |
| > lifetimeLimit | String | The lifetime transaction limit. Return the configured value, "" if not configured |
| accounts | Array of Object | An array containing information about payment accounts associated with the currency and method. |
| > paymentAcctId | String | The account ID for withdrawal |
| > acctNum | String | The account number, which can be an IBAN or other bank account number. |
| > recipientName | String | The name of the recipient |
| > bankName | String | The name of the bank associated with the account |
| > bankCode | String | The SWIFT code / BIC / bank code associated with the account |
| > state | String | The state of the account`active` |

### Create withdrawal order

Initiate a fiat withdrawal request (Authenticated endpoint, Only for API keys with "Withdrawal" access)

Only supported withdrawal of assets from funding account.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/fiat/create-withdrawal`

Request Example

```
POST /api/v5/fiat/create-withdrawal
 body
 {
 "paymentAcctId": "412323",
 "ccy": "TRY",
 "amt": "10000",
 "paymentMethod": "TR_BANKS",
 "clientId": "194a6975e98246538faeb0fab0d502df"
 }
```

```

```

#### Request Parameters

| Parameters | Type | Required | Description |
| --- | --- | --- | --- |
| paymentAcctId | String | Yes | Payment account id to withdraw to, retrieved from get withdrawal payment methods API |
| ccy | String | Yes | Currency for withdrawal, must match currency allowed for paymentMethod |
| amt | String | Yes | Requested withdrawal amount before fees. Has to be less than or equal to 2 decimal points double |
| paymentMethod | String | Yes | Payment method to use for withdrawal`TR_BANKS``PIX``SEPA``XPULSE``NPP``US_WIRE``SG_FAST` |
| clientId | String | Yes | Client-supplied ID, A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters e.g. `194a6975e98246538faeb0fab0d502df` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "cTime": "1707429385000",
 "uTime": "1707429385000",
 "ordId": "124041201450544699",
 "paymentMethod": "TR_BANKS",
 "paymentAcctId": "20",
 "fee": "0",
 "amt": "100",
 "ccy": "TRY",
 "state": "completed",
 "clientId": "194a6975e98246538faeb0fab0d502df"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | The unique order Id |
| clientId | String | The client ID associated with the transaction |
| amt | String | The requested amount for the transaction |
| ccy | String | The currency of the transaction |
| fee | String | The transaction fee |
| paymentAcctId | String | The Id of the payment account used |
| paymentMethod | String | Payment Method`TR_BANKS``PIX``SEPA` |
| state | String | The State of the transaction`processing``completed` |
| cTime | String | The creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | The update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Cancel withdrawal order

Cancel a pending fiat withdrawal order, currently only applicable to TRY

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/fiat/cancel-withdrawal`

Request Example

```
POST /api/v5/fiat/cancel-withdrawal
 body
 {
 "ordId": "124041201450544699"
 }
```

```

```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Payment Order Id |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "ordId": "124041201450544699",
 "state": "canceled"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Payment Order ID |
| state | String | The state of the transaction, e.g.`canceled` |

### Get withdrawal order history

Get fiat withdrawal order history

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/withdrawal-order-history`

Request Example

```
GET /api/v5/fiat/withdrawal-order-history
```

```

```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Fiat currency, ISO-4217 3 digit currency code, e.g. `TRY` |
| paymentMethod | String | No | Payment Method`TR_BANKS``PIX``SEPA``XPULSE``NPP``US_WIRE``SG_FAST` |
| state | String | No | State of the order`completed``failed``pending``canceled``inqueue``processing` |
| after | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085` |
| before | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085` |
| limit | String | No | Number of results per request. Maximum and default is `100` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "cTime": "1707429385000",
 "uTime": "1707429385000",
 "ordId": "124041201450544699",
 "paymentMethod": "TR_BANKS",
 "paymentAcctId": "20",
 "amt": "10000",
 "fee": "0",
 "ccy": "TRY",
 "state": "completed",
 "clientId": "194a6975e98246538faeb0fab0d502df"
 },
 {
 "cTime": "1707429385000",
 "uTime": "1707429385000",
 "ordId": "124041201450544690",
 "paymentMethod": "TR_BANKS",
 "paymentAcctId": "20",
 "amt": "5000",
 "fee": "0",
 "ccy": "TRY",
 "state": "completed",
 "clientId": "164a6975e48946538faeb0fab0d414fg"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Unique Order Id |
| clientId | String | Client Id of the transaction |
| amt | String | Final amount of the transaction |
| ccy | String | Currency of the transaction |
| fee | String | Transaction fee |
| paymentAcctId | String | ID of the payment account used |
| paymentMethod | String | Payment method type |
| state | String | State of the transaction`completed``failed``pending``canceled``inqueue``processing` |
| cTime | String | Creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get withdrawal order detail

Get fiat withdraw order detail

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/withdrawal`

Request Example

```
GET /api/v5/fiat/withdrawal?ordId=024041201450544699
 body
 {
 "ordId": "024041201450544699"
 }
```

```

```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Order ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "cTime": "1707429385000",
 "uTime": "1707429385000",
 "ordId": "024041201450544699",
 "paymentMethod": "TR_BANKS",
 "paymentAcctId": "20",
 "amt": "100",
 "fee": "0",
 "ccy": "TRY",
 "state": "completed",
 "clientId": "194a6975e98246538faeb0fab0d502df"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| clientId | String | The original request ID associated with the transaction |
| ccy | String | The currency of the transaction |
| amt | String | Amount of the transaction |
| fee | String | The transaction fee |
| paymentAcctId | String | The ID of the payment account used |
| paymentMethod | String | Payment method, e.g. `TR_BANKS``PIX``SEPA``XPULSE``NPP``US_WIRE``SG_FAST` |
| state | String | The state of the transaction`completed``failed``pending``canceled``inqueue``processing` |
| cTime | String | The creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | The update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get deposit order history

Get fiat deposit order history

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/deposit-order-history`

Request Example

```
GET /api/v5/fiat/deposit-order-history
```

```

```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | ISO-4217 3 digit currency code |
| paymentMethod | String | No | Payment Method`TR_BANKS``PIX``SEPA``XPULSE``NPP``US_WIRE` |
| state | String | No | State of the order`completed``failed``pending``canceled``inqueue``processing` |
| after | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085` |
| before | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds (inclusive), e.g. `1597026383085` |
| limit | String | No | Number of results per request. Maximum and default is 100 |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "cTime": "1707429385000",
 "uTime": "1707429385000",
 "ordId": "024041201450544699",
 "paymentMethod": "TR_BANKS",
 "paymentAcctId": "20",
 "amt": "10000",
 "fee": "0",
 "ccy": "TRY",
 "state": "completed",
 "clientId": ""
 },
 {
 "cTime": "1707429385000",
 "uTime": "1707429385000",
 "ordId": "024041201450544690",
 "paymentMethod": "TR_BANKS",
 "paymentAcctId": "20",
 "amt": "50000",
 "fee": "0",
 "ccy": "TRY",
 "state": "completed",
 "clientId": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Unique Order ID |
| clientId | String | Client Id of the transaction |
| ccy | String | Currency of the transaction |
| amt | String | Final amount of the transaction |
| fee | String | Transaction fee |
| paymentAcctId | String | ID of the payment account used |
| paymentMethod | String | Payment Method, e.g. `TR_BANKS` |
| state | String | State of the transaction`completed``failed``pending``canceled``inqueue` |
| cTime | String | Creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get deposit order detail

Get fiat deposit order detail

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/deposit`

Request Example

```
GET /api/v5/fiat/deposit?ordId=024041201450544699
body
{
 "ordId": "024041201450544699",
}
```

```

```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ordId | String | Yes | Order ID |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "cTime": "1707429385000",
 "uTime": "1707429385000",
 "ordId": "024041201450544699",
 "paymentMethod": "TR_BANKS",
 "paymentAcctId": "20",
 "amt": "100",
 "fee": "0",
 "ccy": "TRY",
 "state": "completed",
 "clientId": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| clientId | String | The original request ID associated with the transaction. If it's a deposit, it's most likely an empty string (""). |
| amt | String | Amount of the transaction |
| ccy | String | The currency of the transaction |
| fee | String | The transaction fee |
| paymentAcctId | String | The ID of the payment account used |
| paymentMethod | String | Payment method, e.g.`TR_BANKS``PIX``SEPA``XPULSE``NPP``US_WIRE` |
| state | String | The state of the transaction`completed``failed``pending``canceled``inqueue``processing` |
| cTime | String | The creation time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | The update time of the transaction, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get buy/sell currencies

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/buy-sell/currencies`

Request Example

```
GET /api/v5/fiat/buy-sell/currencies
```

Response Example

```
{
 "code": "0",
 "data": [
 {
 "fiatCcyList":[
 {
 "ccy": "USD"
 },
 {
 "ccy": "EUR"
 },
 ...
 ],
 "cryptoCcyList":[
 {
 "ccy": "BTC"
 },
 ...
 ],
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| fiatCcyList | Array of objects | Fiat currency list |
| >ccy | String | Currency, e.g. `BTC` |
| cryptoCcyList | Array of objects | Crypto currency list |
| >ccy | String | Currency, e.g. `USD` |

 This feature is only available to Bahamas institutional users at the moment.


### Get buy/sell currency pair

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/buy-sell/currency-pair`

Request Example

```
GET /api/v5/fiat/buy-sell/currency-pair?fromCcy=USD&toCcy=BTC
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| fromCcy | String | Yes | Currency to sell, e.g. `USD` |
| toCcy | String | Yes | Currency to buy, e.g. `BTC` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "side": "buy",
 "fromCcy": "USD",
 "toCcy": "BTC",
 "singleTradeMax": "1",
 "singleTradeMin": "0.01",
 "fixedPxRemainingDailyQuota": "",
 "fixedPxDailyLimit": "",
 "paymentMethods":["balance"]
 }
 ],
 "msg": ""
}

{
 "code": "0",
 "data": [
 {
 "side": "sell",
 "fromCcy": "BTC",
 "toCcy": "USD",
 "singleTradeMax": "1",
 "singleTradeMin": "0.01",
 "fixedPxRemainingDailyQuota": "",
 "fixedPxDailyLimit": "",
 "paymentMethods":["balance"]
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| side | String | Side`buy`: Fiat to crypto`sell`: Crypto to fiatMay support both sides in the future, separated with a comma, e.g. `buy,sell`. |
| fromCcy | String | Currency to sell, e.g. `USD` |
| toCcy | String | Currency to buy, e.g. `BTC` |
| singleTradeMax | String | The maximum amount of currency for a single trade, unit in `fromCcy` |
| singleTradeMin | String | The minimum amount of currency for a single trade, unit in `fromCcy` |
| fixedPxDailyLimit | String | Fixed price daily limitApplicable to Fiat to Fiat trade, else return ''.If `side` = `buy`, unit in `fromCcy`If `side` = `sell`, unit in `toCcy` |
| fixedPxRemainingDailyQuota | String | Fixed price remaining daily quotaApplicable to Fiat to Fiat trade, else return ''.If `side` = `buy`, unit in `fromCcy`If `side` = `sell`, unit in `toCcy` |
| paymentMethods | Array of strings | Supported payment methods`balance`e.g. ["balance"] |

 This feature is only available to Bahamas institutional users at the moment.


### Get buy/sell quote

#### Rate Limit: 10 requests per second

#### Rate limit rule: User ID

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: Instrument ID

#### HTTP Request

`POST /api/v5/fiat/buy-sell/quote`

Request Example

```
# Sell USD to buy 0.1 BTC
POST /api/v5/fiat/buy-sell/quote
body
{
 "side":"buy",
 "fromCcy": "USD",
 "toCcy": "BTC",
 "rfqAmt": "0.1",
 "rfqCcy": "BTC"
}

# Sell 30 USD to buy BTC
POST /api/v5/fiat/buy-sell/quote
body
{
 "side":"buy",
 "fromCcy": "USD",
 "toCcy": "BTC",
 "rfqAmt": "30",
 "rfqCcy": "USD"
}

# Sell BTC to buy 30 USD
POST /api/v5/fiat/buy-sell/quote
body
{
 "side":"sell",
 "fromCcy": "BTC",
 "toCcy": "USD",
 "rfqAmt": "30",
 "rfqCcy": "USD"
}

# Sell 0.1 BTC to buy USD
POST /api/v5/fiat/buy-sell/quote
body
{
 "side":"sell",
 "fromCcy": "BTC",
 "toCcy": "USD",
 "rfqAmt": "0.1",
 "rfqCcy": "BTC"
}
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| side | String | Yes | Side `buy`: Buy Crypto / Fiat with Fiat `sell`: Sell Crypto to Crypto / Fiat |
| fromCcy | String | Yes | Currency to sell |
| toCcy | String | Yes | Currency to buy |
| rfqAmt | String | Yes | RFQ amount |
| rfqCcy | String | Yes | RFQ currency |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "quoteId": "quoterBTC-USD16461885104612381",
 "fromCcy": "USD",
 "toCcy": "BTC",
 "rfqAmt": "30",
 "rfqCcy": "USD",
 "quotePx": "2932.40104429",
 "quoteCcy": "USD",
 "quoteFromAmt": "30",
 "quoteToAmt": "30",
 "quoteTime": "1646188510461",
 "ttlMs": "10000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| quoteId | String | Quote ID |
| side | String | Side `buy`: Buy Crypto / Fiat with Fiat `sell`: Sell Crypto to Crypto / Fiat |
| fromCcy | String | Currency to sell, e.g. `USD` |
| toCcy | String | Currency to buy, e.g. `BTC` |
| rfqAmt | String | RFQ amount |
| rfqCcy | String | RFQ currency |
| quotePx | String | Quote price |
| quoteCcy | String | Quote price unit e.g. `USD` |
| quoteFromAmt | String | Quote amount, unit in `fromCcy` |
| quoteToAmt | String | Quote amount, unit in `toCcy` |
| quoteTime | String | Quotation generation time, Unix timestamp format in milliseconds, e.g. 1597026383085 |
| ttlMs | String | The validity period of quotation in milliseconds e.g. `10000` represents the quotation only valid for 10 seconds |

 This feature is only available to Bahamas institutional users at the moment.


### Buy/sell trade

#### Rate Limit: 1 request per 5 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/fiat/buy-sell/trade`

Request Example

```
# Sell 30 USD to buy BTC
POST /api/v5/fiat/buy-sell/trade
body
{
 "clOrdId":"123456",
 "side":"sell",
 "fromCcy": "USD",
 "toCcy": "BTC",
 "rfqAmt": "30",
 "rfqCcy": "USD",
 "paymentMethod":"balance",
 "quoteId": "quoterETH-USDT16461885104612381"
}
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| quoteId | String | Yes | Quote IDGet from Buy/Sell quote API |
| side | String | Yes | Side `buy`: Buy Crypto / Fiat with Fiat `sell`: Sell Crypto to Crypto / Fiat Should be the same as the Quote request |
| fromCcy | String | Yes | Currency to sell Should be the same as the Quote request |
| toCcy | String | Yes | Currency to buy Should be the same as the Quote request |
| rfqAmt | String | Yes | RFQ amount Should be the same as the Quote request |
| rfqCcy | String | Yes | RFQ currency Should be the same as the Quote request |
| paymentMethod | String | Yes | paymentMethod `balance` |
| clOrdId | String | Yes | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "ordId": "1234",
 "clOrdId": "",
 "quoteId": "quoterBTC-USD16461885104612381",
 "side":"buy",
 "fromCcy": "USD",
 "toCcy": "BTC",
 "rfqAmt": "30",
 "rfqCcy": "USD",
 "fillPx": "2932.40104429",
 "fillQuoteCcy": "USD",
 "fillFromAmt": "30",
 "fillToAmt": "0.01",
 "cTime": "1646188510461"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| quoteId | String | Quote ID |
| state | String | Trade state `processing` `completed` `failed` |
| side | String | Side `buy`: Buy Crypto / Fiat with Fiat `sell`: Sell Crypto to Crypto / Fiat |
| fromCcy | String | Currency to sell |
| toCcy | String | Currency to buy |
| rfqAmt | String | RFQ amount |
| rfqCcy | String | RFQ currency |
| fillPx | String | Filled price based on quote currency |
| fillQuoteCcy | String | Filled price quote currency e.g. `USD` |
| fillFromAmt | String | Sold amount, unit in `fromCcy` |
| fillToAmt | String | Bought amount, unit in `toCcy` |
| cTime | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

 This feature is only available to Bahamas institutional users at the moment.


### Get buy/sell trade history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/fiat/buy-sell/history`

Request Example

```
GET /api/v5/fiat/buy-sell/history
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ordId | String | No | Order ID |
| clOrdId | String | No | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| state | String | No | Trade state `processing` `completed` `failed` |
| begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "ordId": "1234",
 "clOrdId": "",
 "quoteId": "quoterBTC-USD16461885104612381",
 "state":"completed",
 "side":"buy",
 "fromCcy": "USD",
 "toCcy": "BTC",
 "rfqAmt": "30",
 "rfqCcy": "USD",
 "fillPx": "2932.40104429",
 "fillQuoteCcy": "USD",
 "fillFromAmt": "30",
 "fillToAmt": "0.01",
 "cTime": "1646188510461",
 "uTime": "1646188510461"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ordId | String | Order ID |
| clOrdId | String | Client Order ID as assigned by the client |
| quoteId | String | Quote ID |
| state | String | Trade state `processing` `completed` `failed` |
| fromCcy | String | Currency to sell |
| toCcy | String | Currency to buy |
| rfqAmt | String | RFQ amount |
| rfqCcy | String | RFQ currency |
| fillPx | String | Filled price based on quote currency |
| fillQuoteCcy | String | Filled price quote currency e.g. `USD` |
| fillFromAmt | String | Filled amount unit in fromCcy |
| fillToAmt | String | Filled amount unit in toCcy |
| cTime | String | Request time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| uTime | String | Updated time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

 This feature is only available to Bahamas institutional users at the moment.
