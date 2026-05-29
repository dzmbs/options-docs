## REST API

### Get sub-account list

Applies to master accounts only

#### Rate limit：20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/users/subaccount/list`

Request sample

```
GET /api/v5/users/subaccount/list
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Get sub-account list
result = subAccountAPI.get_subaccount_list()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| enable | String | No | Sub-account status `true`: Normal `false`: Frozen |
| subAcct | String | No | Sub-account name |
| after | String | No | Query the data earlier than the requested subaccount creation timestamp, the value should be a Unix timestamp in millisecond format. e.g. `1597026383085` |
| before | String | No | Query the data newer than the requested subaccount creation timestamp, the value should be a Unix timestamp in millisecond format. e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Returned results

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "canTransOut": false,
 "enable": true,
 "frozenFunc": [
 ],
 "gAuth": false,
 "label": "D456DDDLx",
 "mobile": "",
 "subAcct": "D456DDDL",
 "ts": "1659334756000",
 "type": "1",
 "uid": "3400***********7413",
 "subAcctLv": "1",
 "firstLvSubAcct": "D456DDDL",
 "ifDma": false
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| type | String | Sub-account type `1`: Standard sub-account `2`: Managed trading sub-account `5`: Custody trading sub-account - Copper`9`: Managed trading sub-account - Copper `12`: Custody trading sub-account - Komainu |
| enable | Boolean | Sub-account status`true`: Normal`false`: Frozen (global) |
| subAcct | String | Sub-account name |
| uid | String | Sub-account uid |
| label | String | Sub-account note |
| mobile | String | Mobile number that linked with the sub-account. |
| gAuth | Boolean | If the sub-account switches on the Google Authenticator for login authentication. `true`: On `false`: Off |
| frozenFunc | Array of strings | Frozen functions`trading``convert``transfer``withdrawal``deposit``flexible_loan` |
| canTransOut | Boolean | Whether the sub-account has the right to transfer out. `true`: can transfer out `false`: cannot transfer out |
| ts | String | Sub-account creation time, Unix timestamp in millisecond format. e.g. `1597026383085` |
| subAcctLv | String | Sub-account level `1`: First level sub-account`2`: Second level sub-account. |
| firstLvSubAcct | String | The first level sub-account. For subAcctLv: 1, firstLvSubAcct is equal to subAcctFor subAcctLv: 2, subAcct belongs to firstLvSubAcct. |
| ifDma | Boolean | Whether it is dma broker sub-account. `true`: Dma broker sub-account `false`: It is not dma broker sub-account. |

### Create sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/create-subaccount`

Request sample

```
POST /api/v5/users/subaccount/create-subaccount
body
{
 "subAcct": "subAccount002",
 "type": "1",
 "label": "123456"
}
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Reset the API Key of a sub-account
result = subAccountAPI.reset_subaccount_apikey(
 subAcct="hahawang1",
 apiKey="",
 ip=""
)
print(result)
```

#### Request Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name |
| type | String | Yes | Sub-account type `1`: Standard sub-account `5`: Custody trading sub-account - Copper `12`: Custody trading sub-account - Komainu |
| label | String | No | Sub-account notes. 6-32 letters (case sensitive), numbers or special characters like *. |
| pwd | String | Conditional | Sub-account login password, it is required for KYB users only. Your password must contain:8 - 32 characters long.1 lowercase character (a-z).1 uppercase character (A-Z).1 number.1 special character e.g. ! @ # $ % |

Returned results

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "label": "123456 ",
 "subAcct": "subAccount002",
 "ts": "1744875304520",
 "uid": "698827017768230914"
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| subAcct | String | Sub-account name |
| label | String | Sub-account notes |
| uid | String | Sub-account ID |
| ts | String | Creation time |

### Create an API Key for a sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/apikey`

Request sample

```
POST /api/v5/users/subaccount/apikey
body
{
 "subAcct":"panpanBroker2",
 "label":"broker3",
 "passphrase": "******",
 "perm":"trade"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name, supports 6 to 20 characters that include numbers and letters (case sensitive, space symbol is not supported). |
| label | String | Yes | API Key note |
| passphrase | String | Yes | API Key password, supports 8 to 32 alphanumeric characters containing at least 1 number, 1 uppercase letter, 1 lowercase letter and 1 special character. |
| perm | String | No | API Key permissions `read_only`: Read only `trade`: Trade |
| ip | String | No | Link IP addresses, separate with commas if more than one. Support up to 20 addresses.For security reasons, it is recommended to bind IP addresses.API keys with trading or withdrawal permissions that are not bound to IPs will expire after 14 days of inactivity. (API keys in demo trading will not be deleted.) |

Returned result

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "subAcct": "test-1",
 "label": "v5",
 "apiKey": "******",
 "secretKey": "******",
 "passphrase": "******",
 "perm": "read_only,trade",
 "ip": "1.1.1.1,2.2.2.2",
 "ts": "1597026383085"
 }]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| subAcct | String | Sub-account name |
| label | String | API Key note |
| apiKey | String | API public key |
| secretKey | String | API private key |
| passphrase | String | API Key password |
| perm | String | API Key access `read_only` : Read only `trade` : Trade |
| ip | String | IP address that linked with API Key |
| ts | String | Creation time |

### Query the API Key of a sub-account

Applies to master accounts only

#### Rate limit：20 request per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/users/subaccount/apikey`

Request sample

```
GET /api/v5/users/subaccount/apikey?subAcct=panpanBroker2
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name |
| apiKey | String | No | API public key |

Returned results

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "label": "v5",
 "apiKey": "******",
 "perm": "read_only,trade",
 "ip": "1.1.1.1,2.2.2.2",
 "ts": "1597026383085"
 },
 {
 "label": "v5.1",
 "apiKey": "******",
 "perm": "read_only",
 "ip": "1.1.1.1,2.2.2.2",
 "ts": "1597026383085"
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| label | String | API Key note |
| apiKey | String | API public key |
| perm | String | API Key access read_only: Read only; trade: Trade |
| ip | String | IP address that linked with API Key |
| ts | String | Creation time |

### Reset the API Key of a sub-account

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/modify-apikey`

Request sample

```
POST /api/v5/users/subaccount/modify-apikey
body
{
 "subAcct":"yongxu",
 "apiKey":"******"
 "ip":"1.1.1.1"
}
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Reset the API Key of a sub-account
result = subAccountAPI.reset_subaccount_apikey(
 subAcct="hahawang1",
 apiKey="",
 ip=""
)
print(result)
```

#### Request Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name |
| apiKey | String | Yes | Sub-account APIKey |
| label | String | No | Sub-account API Key label. The label will be reset if this is passed through. |
| perm | String | No | Sub-account API Key permissions`read_only`: Read`trade`: TradeSeparate with commas if more than one. The permission will be reset if this is passed through. |
| ip | String | No | Sub-account API Key linked IP addresses, separate with commas if more than one. Support up to 20 IP addresses.The IP will be reset if this is passed through.If `ip` is set to "", then no IP addresses is linked to the APIKey. |

Returned results

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "subAcct": "yongxu",
 "label": "v5",
 "apiKey": "******",
 "perm": "read,trade",
 "ip": "1.1.1.1",
 "ts": "1597026383085"
 }]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| subAcct | String | Sub-account name |
| apiKey | String | Sub-accountAPI public key |
| label | String | Sub-account API Key label |
| perm | String | Sub-account API Key permissions`read_only`: Read`trade`: Trade |
| ip | String | Sub-account API Key IP addresses that linked with API Key |
| ts | String | Creation time |

### Delete the API Key of sub-accounts

Applies to master accounts only and master accounts API Key must be linked to IP addresses.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/users/subaccount/delete-apikey`

Request sample

```
POST /api/v5/users/subaccount/delete-apikey
body
{
 "subAcct":"test00001",
 "apiKey":"******"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name |
| apiKey | String | Yes | API public key |

Returned results

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "subAcct": "test00001"
 }]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| subAcct | String | Sub-account name |

### Get sub-account trading balance

Query detailed balance info of Trading Account of a sub-account via the master account (applies to master accounts only)

#### Rate limit：6 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/account/subaccount/balances`

Request sample

```
GET /api/v5/account/subaccount/balances?subAcct=test1
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Get sub-account trading balance
result = subAccountAPI.get_account_balance(
 subAcct="hahawang1"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name |

Returned result

```
{
 "code": "0",
 "data": [
 {
 "adjEq": "101.46752000000001",
 "availEq": "624719833286",
 "borrowFroz": "0",
 "delta": "0",
 "deltaLever": "0",
 "deltaNeutralStatus": "0",
 "details": [
 {
 "autoLendStatus": "off",
 "autoLendMtAmt": "0",
 "accAvgPx": "",
 "availBal": "101.5",
 "availEq": "101.5",
 "borrowFroz": "0",
 "cashBal": "101.5",
 "ccy": "USDT",
 "clSpotInUseAmt": "",
 "crossLiab": "0",
 "colRes": "0",
 "collateralEnabled": false,
 "collateralRestrict": false,
 "colBorrAutoConversion": "0",
 "disEq": "101.46752000000001",
 "eq": "101.5",
 "eqUsd": "101.46752000000001",
 "fixedBal": "0",
 "frozenBal": "0",
 "frpType": "0",
 "imr": "",
 "interest": "0",
 "isoEq": "0",
 "isoLiab": "0",
 "isoUpl": "0",
 "liab": "0",
 "maxLoan": "1015.0000000000001",
 "maxSpotInUse": "",
 "mgnRatio": "",
 "mmr": "",
 "notionalLever": "",
 "openAvgPx": "",
 "ordFrozen": "0",
 "rewardBal": "",
 "smtSyncEq": "0",
 "spotBal": "",
 "spotCopyTradingEq": "0",
 "spotInUseAmt": "",
 "spotIsoBal": "0",
 "spotUpl": "",
 "spotUplRatio": "",
 "stgyEq": "0",
 "totalPnl": "",
 "totalPnlRatio": "",
 "twap": "0",
 "uTime": "1663854334734",
 "upl": "0",
 "uplLiab": "0"
 }
 ],
 "imr": "0",
 "isoEq": "0",
 "mgnRatio": "",
 "mmr": "0",
 "notionalUsd": "0",
 "notionalUsdForBorrow": "0",
 "notionalUsdForFutures": "0",
 "notionalUsdForOption": "0",
 "notionalUsdForSwap": "0",
 "ordFroz": "0",
 "totalEq": "101.46752000000001",
 "uTime": "1739332269934",
 "upl": "0"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameters | Types | Description |
| --- | --- | --- |
| uTime | String | Update time of account information, millisecond format of Unix timestamp, e.g. `1597026383085` |
| totalEq | String | The total amount of equity in `USD` |
| isoEq | String | Isolated margin equity in `USD`Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin` |
| adjEq | String | Adjusted / Effective equity in `USD` The net fiat value of the assets in the account that can provide margins for spot, expiry futures, perpetual futures and options under the cross-margin mode. In multi-ccy or PM mode, the asset and margin requirement will all be converted to USD value to process the order check or liquidation. Due to the volatility of each currency market, our platform calculates the actual USD value of each currency based on discount rates to balance market risks. Applicable to `Spot mode`/`Multi-currency margin` and `Portfolio margin` |
| availEq | String | Account level available equity, excluding currencies that are restricted due to the collateralized borrowing limit. Applicable to `Multi-currency margin`/`Portfolio margin` |
| ordFroz | String | Cross margin frozen for pending orders in `USD` Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| imr | String | Initial margin requirement in `USD` The sum of initial margins of all open positions and pending orders under cross-margin mode in `USD`. Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| mmr | String | Maintenance margin requirement in `USD` The sum of maintenance margins of all open positions and pending orders under cross-margin mode in `USD`. Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| borrowFroz | String | Potential borrowing IMR of the account in `USD` Only applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes. |
| mgnRatio | String | Maintenance margin ratio in `USD` Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| notionalUsd | String | Notional value of positions in `USD` Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| notionalUsdForBorrow | String | Notional value for `Borrow` in USDApplicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| notionalUsdForSwap | String | Notional value of positions for `Perpetual Futures` in USDApplicable to `Multi-currency margin`/`Portfolio margin` |
| notionalUsdForFutures | String | Notional value of positions for `Expiry Futures` in USDApplicable to `Multi-currency margin`/`Portfolio margin` |
| notionalUsdForOption | String | Notional value of positions for `Option` in USDApplicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| upl | String | Cross-margin info of unrealized profit and loss at the account level in `USD`Applicable to `Multi-currency margin`/`Portfolio margin` |
| delta | String | Delta (USD) |
| deltaLever | String | Delta neutral strategy account level delta leveragedeltaLever = delta / totalEq |
| deltaNeutralStatus | String | Delta risk status`0`: normal`1`: transfer restricted`2`: delta reducing - cancel all pending orders if delta is greater than 5000 USD, only one delta reducing order allowed per index (spot, futures, swap) |
| details | Array of objects | Detailed asset information in all currencies |
| > ccy | String | Currency |
| > eq | String | Equity of currency |
| > cashBal | String | Cash balance |
| > uTime | String | Update time of currency balance information, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > isoEq | String | Isolated margin equity of currencyApplicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin` |
| > availEq | String | Available equity of currencyApplicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin` |
| > disEq | String | Discount equity of currency in `USD`. |
| > fixedBal | String | Frozen balance for `Dip Sniper` and `Peak Sniper` |
| > availBal | String | Available balance of currency |
| > frozenBal | String | Frozen balance of currency |
| > ordFrozen | String | Margin frozen for open orders Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin` |
| > liab | String | Liabilities of currencyIt is a positive value, e.g. `21625.64`Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| > upl | String | The sum of the unrealized profit & loss of all margin and derivatives positions of currency. Applicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin` |
| > uplLiab | String | Liabilities due to Unrealized loss of currencyApplicable to `Multi-currency margin`/`Portfolio margin` |
| > crossLiab | String | Cross liabilities of currencyApplicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| > rewardBal | String | Trial fund balance |
| > isoLiab | String | Isolated liabilities of currencyApplicable to `Multi-currency margin`/`Portfolio margin` |
| > mgnRatio | String | Cross Maintenance margin ratio of currency The index for measuring the risk of a certain asset in the account. Applicable to `Futures mode` and when there is cross position |
| > imr | String | Cross initial margin requirement at the currency levelApplicable to `Futures mode` and when there is cross position |
| > mmr | String | Cross maintenance margin requirement at the currency levelApplicable to `Futures mode` and when there is cross position |
| > interest | String | Accrued interest of currencyIt is a positive value, e.g. `9.01`Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| > twap | String | Risk indicator of forced repaymentDivided into multiple levels from 0 to 5, the larger the number, the more likely the forced repayment will be triggered. Applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| > frpType | String | Forced repayment (FRP) type `0`: no FRP `1`: user based FRP `2`: platform based FRP Return `1`/`2` when twap is >= 1, applicable to `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| > maxLoan | String | Max loan of currencyApplicable to `cross` of `Spot mode`/`Multi-currency margin`/`Portfolio margin` |
| > eqUsd | String | Equity in `USD` of currency |
| > borrowFroz | String | Potential borrowing IMR of currency in `USD` Applicable to `Multi-currency margin`/`Portfolio margin`. It is "" for other margin modes. |
| > notionalLever | String | Leverage of currencyApplicable to `Futures mode` |
| > stgyEq | String | Strategy equity |
| > isoUpl | String | Isolated unrealized profit and loss of currencyApplicable to `Futures mode`/`Multi-currency margin`/`Portfolio margin` |
| > spotInUseAmt | String | Spot in use amountApplicable to `Portfolio margin` |
| > clSpotInUseAmt | String | User-defined spot risk offset amountApplicable to `Portfolio margin` |
| > maxSpotInUse | String | Max possible spot risk offset amountApplicable to `Portfolio margin` |
| > spotIsoBal | String | Spot isolated balanceApplicable to copy tradingApplicable to `Spot mode`/`Futures mode`. |
| > smtSyncEq | String | Smart sync equityThe default is "0", only applicable to copy trader. |
| > spotCopyTradingEq | String | Spot smart sync equity. The default is "0", only applicable to copy trader. |
| > spotBal | String | Spot balance. The unit is currency, e.g. BTC. More details |
| > openAvgPx | String | Spot average cost price. The unit is USD. More details |
| > accAvgPx | String | Spot accumulated cost price. The unit is USD. More details |
| > spotUpl | String | Spot unrealized profit and loss. The unit is USD. More details |
| > spotUplRatio | String | Spot unrealized profit and loss ratio. More details |
| > totalPnl | String | Spot accumulated profit and loss. The unit is USD. More details |
| > totalPnlRatio | String | Spot accumulated profit and loss ratio. More details |
| > colRes | String | Platform level collateral restriction status `0`: The restriction is not enabled. `1`: The restriction is not enabled. But the crypto is close to the platform's collateral limit. `2`: The restriction is enabled. This crypto can't be used as margin for your new orders. This may result in failed orders. But it will still be included in the account's adjusted equity and doesn't impact margin ratio. Refer to Introduction to the platform collateralized borrowing limit for more details. |
| > colBorrAutoConversion | String | Risk indicator of auto conversion. Divided into multiple levels from 1-5, the larger the number, the more likely the repayment will be triggered. The default will be 0, indicating there is no risk currently. 5 means this user is undergoing auto conversion now, 4 means this user will undergo auto conversion soon whereas 1/2/3 indicates there is a risk for auto conversion. Applicable to `Spot mode`/`Futures mode`/`Multi-currency margin`/`Portfolio margin` When the total liability for each crypto set as collateral exceeds a certain percentage of the platform's total limit, the auto-conversion mechanism may be triggered. This may result in the automatic sale of excess collateral crypto if you've set this crypto as collateral and have large borrowings. To lower this risk, consider reducing your use of the crypto as collateral or reducing your liabilities. Refer to Introduction to the platform collateralized borrowing limit for more details. |
| > collateralRestrict | Boolean | Platform level collateralized borrow restriction `true` `false`(deprecated, use colRes instead) |
| > collateralEnabled | Boolean | `true`: Collateral enabled`false`: Collateral disabledApplicable to `Multi-currency margin` |
| > autoLendStatus | String | Auto lend status `unsupported`: auto lend is not supported by this currency `off`: auto lend is supported but turned off `pending`: auto lend is turned on but pending matching `active`: auto lend is turned on and matched |
| > autoLendMtAmt | String | Auto lend currency matched amount Return "0" when autoLendStatus is `unsupported/off/pending`. Return matched amount when autoLendStatus is `active` |

 "" will be returned for inapplicable fields with the current account level.

### Get sub-account funding balance

Query detailed balance info of Funding Account of a sub-account via the master account (applies to master accounts only)

#### Rate limit：6 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/asset/subaccount/balances`

Request sample

```
GET /api/v5/asset/subaccount/balances?subAcct=test1
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Get sub-account funding balance
result = subAccountAPI.get_funding_balance(
 subAcct="hahawang1"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name |
| ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`. |

Returned result

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "availBal": "37.11827078",
 "bal": "37.11827078",
 "ccy": "ETH",
 "frozenBal": "0"
 }
 ]
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| bal | String | Balance |
| frozenBal | String | Frozen balance |
| availBal | String | Available balance |

### Get sub-account maximum withdrawals

Retrieve the maximum withdrawal information of a sub-account via the master account (applies to master accounts only). If no currency is specified, the transferable amount of all owned currencies will be returned.

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/account/subaccount/max-withdrawal`

Request Example

```
GET /api/v5/account/subaccount/max-withdrawal?subAcct=test1
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Sub-account name |
| ccy | String | No | Single currency or multiple currencies (no more than 20) separated with comma, e.g. `BTC` or `BTC,ETH`. |

Response Example

```
{
 "code":"0",
 "data":[
 {
 "ccy":"BTC",
 "maxWd":"3",
 "maxWdEx":"",
 "spotOffsetMaxWd":"3",
 "spotOffsetMaxWdEx":""
 },
 {
 "ccy":"ETH",
 "maxWd":"15",
 "maxWdEx":"",
 "spotOffsetMaxWd":"15",
 "spotOffsetMaxWdEx":""
 },
 {
 "ccy":"USDT",
 "maxWd":"10600",
 "maxWdEx":"",
 "spotOffsetMaxWd":"10600",
 "spotOffsetMaxWdEx":""
 }
 ],
 "msg":""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| maxWd | String | Max withdrawal (excluding borrowed assets under `Multi-currency margin`) |
| maxWdEx | String | Max withdrawal (including borrowed assets under `Multi-currency margin`) |
| spotOffsetMaxWd | String | Max withdrawal under Spot-Derivatives risk offset mode (excluding borrowed assets under `Portfolio margin`) Applicable to `Portfolio margin` |
| spotOffsetMaxWdEx | String | Max withdrawal under Spot-Derivatives risk offset mode (including borrowed assets under `Portfolio margin`) Applicable to `Portfolio margin` |

### Get history of sub-account transfer

This endpoint is only available for master accounts. Transfer records are available from September 28, 2022 onwards.

#### Rate limit：6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/asset/subaccount/bills`

Request sample

```
GET /api/v5/asset/subaccount/bills
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Get history of sub-account transfer
result = subAccountAPI.bills()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, such as BTC |
| type | String | No | Transfer type`0`: Transfers from master account to sub-account`1` : Transfers from sub-account to master account. |
| subAcct | String | No | Sub-account name |
| after | String | No | Query the data prior to the requested bill ID creation time (exclude), the value should be a Unix timestamp in millisecond format. e.g. `1597026383085` |
| before | String | No | Query the data after the requested bill ID creation time (exclude), the value should be a Unix timestamp in millisecond format. e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Returned results

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "amt": "1.1",
 "billId": "89887685",
 "ccy": "USDT",
 "subAcct": "hahatest1",
 "ts": "1712560959000",
 "type": "0"
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| billId | String | Bill ID |
| ccy | String | Transfer currency |
| amt | String | Transfer amount |
| type | String | Bill type |
| subAcct | String | Sub-account name |
| ts | String | Bill ID creation time, Unix timestamp in millisecond format, e.g. `1597026383085` |

### Get history of managed sub-account transfer

Only applicable to the trading team's master account to getting transfer records of managed sub accounts entrusted to oneself.

#### Rate limit：6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/asset/subaccount/managed-subaccount-bills`

Request sample

```
GET /api/v5/asset/subaccount/managed-subaccount-bills
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Currency, e.g `BTC` |
| type | String | No | Transfer type`0`: Transfers from master account to sub-account`1`: Transfers from sub-account to master account |
| subAcct | String | No | Sub-account name |
| subUid | String | No | Sub-account UID |
| after | String | No | Query the data prior to the requested bill ID creation time (exclude), Unix timestamp in millisecond format, e.g. `1597026383085` |
| before | String | No | Query the data after the requested bill ID creation time (exclude), Unix timestamp in millisecond format, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is 100. The default is 100. |

Returned results

```
{
 "code": "0",
 "msg": "",
 "data": [{
 "billId": "12344",
 "type": "1",
 "ccy": "BTC",
 "amt": "2",
 "subAcct": "test-1",
 "subUid": "xxxxxx",
 "ts": "1597026383085"
 }]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| billId | String | Bill ID |
| ccy | String | Transfer currency |
| amt | String | Transfer amount |
| type | String | Bill type |
| subAcct | String | Sub-account name |
| subUid | String | Sub-account UID |
| ts | String | Bill ID creation time, Unix timestamp in millisecond format, e.g. `1597026383085` |

### Master accounts manage the transfers between sub-accounts

Applies to master accounts only.

Only API keys with `Trade` privilege can call this endpoint.

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP request

`POST /api/v5/asset/subaccount/transfer`

Request sample

```
POST /api/v5/asset/subaccount/transfer
body
{
 "ccy":"USDT",
 "amt":"1.5",
 "from":"6",
 "to":"6",
 "fromSubAccount":"test-1",
 "toSubAccount":"test-2"
}
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Master accounts manage the transfers between sub-accounts
result = subAccountAPI.subAccount_transfer(
 ccy="USDT",
 amt="10",
 froms="6",
 to="6",
 fromSubAccount="test-1",
 toSubAccount="test-2"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| amt | String | Yes | Transfer amount |
| from | String | Yes | Account type of transfer from sub-account`6`: Funding Account`18`: Trading account |
| to | String | Yes | Account type of transfer to sub-account`6`: Funding Account`18`: Trading account |
| fromSubAccount | String | Yes | Sub-account name of the account that transfers funds out. |
| toSubAccount | String | Yes | Sub-account name of the account that transfers funds in. |
| loanTrans | Boolean | No | Whether or not borrowed coins can be transferred out under `Multi-currency margin`/`Portfolio margin`The default is `false` |
| omitPosRisk | String | No | Ignore position riskDefault is `false`Applicable to `Portfolio margin` |

Returned results

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "transId":"12345",
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| transId | String | Transfer ID |

### Set permission of transfer out

Set permission of transfer out for sub-account (only applicable to master account API key). Sub-account can transfer out to master account by default.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/users/subaccount/set-transfer-out`

Request Example

```
POST /api/v5/users/subaccount/set-transfer-out
body
{
 "subAcct": "Test001,Test002",
 "canTransOut": true
}
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Set permission of transfer out for sub-account
result = subAccountAPI.set_permission_transfer_out(
 subAcct="hahawang1",
 canTransOut=False
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | Yes | Name of the sub-account. Single sub-account or multiple sub-account (no more than 20) separated with comma. |
| canTransOut | Boolean | No | Whether the sub-account has the right to transfer out. The default is `true`.`false`: cannot transfer out `true`: can transfer out |

Returned result

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "subAcct": "Test001",
 "canTransOut": true
 },
 {
 "subAcct": "Test002",
 "canTransOut": true
 }
 ]
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| subAcct | String | Name of the sub-account |
| canTransOut | Boolean | Whether the sub-account has the right to transfer out. `false`: cannot transfer out `true`: can transfer out |

### Get custody trading sub-account list

The trading team uses this interface to view the list of sub-accounts currently under escrow

#### Rate limit：1 request per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP request

`GET /api/v5/users/entrust-subaccount-list`

Request sample

```
GET /api/v5/users/entrust-subaccount-list
```

```
import okx.SubAccount as SubAccount

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

subAccountAPI = SubAccount.SubAccountAPI(apikey, secretkey, passphrase, False, flag)

# Get custody trading sub-account list
result = subAccountAPI.get_entrust_subaccount_list()
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| subAcct | String | No | Sub-account name |

Returned results

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "subAcct":"test-1"
 },
 {
 "subAcct":"test-2"
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| subAcct | String | Sub-account name |
