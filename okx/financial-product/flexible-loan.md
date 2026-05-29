## Flexible loan

OKX Flexible Loan is a high-end loan product that allows users to increase cash flow without selling off their crypto. [More details](/loan)

### GET / Borrowable currencies

Get borrowable currencies

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/borrow-currencies`

Request Example

```
GET /api/v5/finance/flexible-loan/borrow-currencies
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.borrow_currencies()
print(result)
```

Response Example

```
{
 "code": "0",
 "data": [
 {
 "borrowCcy": "USDT"
 },
 {
 "borrowCcy": "USDC"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| borrowCcy | String | Borrowable currency, e.g. `BTC` |

### GET / Collateral assets

Get collateral assets in funding account.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/collateral-assets`

Request Example

```
GET /api/v5/finance/flexible-loan/collateral-assets
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.collateral_assets()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Collateral currency, e.g. `BTC` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "assets": [
 {
 "amt": "1.7921483143067599",
 "ccy": "BTC",
 "notionalUsd": "158292.621793314105231"
 },
 {
 "amt": "1.9400755578876945",
 "ccy": "ETH",
 "notionalUsd": "6325.6652712507628946"
 },
 {
 "amt": "63.9795959720319628",
 "ccy": "USDT",
 "notionalUsd": "64.3650372635940345"
 }
 ]
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| assets | Array of objects | Collateral assets data |
| > ccy | String | Currency, e.g. `BTC` |
| > amt | String | Available amount |
| > notionalUsd | String | Notional value in `USD` |

### POST / Maximum loan amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/finance/flexible-loan/max-loan`

Request Example

```
POST /api/v5/finance/flexible-loan/max-loan
body
{
 "borrowCcy": "USDT"
}
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.max_loan(borrowCcy="USDT")
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| borrowCcy | String | Yes | Currency to borrow, e.g. `USDT` |
| supCollateral | Array of objects | No | Supplementary collateral assets |
| > ccy | String | Yes | Currency, e.g. `BTC` |
| > amt | String | Yes | Amount |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "borrowCcy": "USDT",
 "maxLoan": "0.01113",
 "notionalUsd": "0.01113356",
 "remainingQuota": "3395000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| borrowCcy | String | Currency to borrow, e.g. `USDT` |
| maxLoan | String | Maximum available loan |
| notionalUsd | String | Maximum available loan notional value, unit in `USD` |
| remainingQuota | String | Remaining quota, unit in `borrowCcy` |

### GET / Maximum collateral redeem amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

Request Example

```
GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.max_collateral_redeem_amount("USDT")
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Collateral currency, e.g. `USDT` |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "maxRedeemAmt": "1"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Collateral currency, e.g. `USDT` |
| maxRedeemAmt | String | Maximum collateral redeem amount |

### POST / Adjust collateral

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/flexible-loan/adjust-collateral`

Request Example

```
POST /api/v5/finance/flexible-loan/adjust-collateral
body
{
 "type":"add",
 "collateralCcy": "BTC",
 "collateralAmt": "0.1"
}
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.adjust_collateral(type="add", collateralCcy="USDT", collateralAmt="1")
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| type | String | Yes | Operation type`add`: Add collateral`reduce`: Reduce collateral |
| collateralCcy | String | Yes | Collateral currency, e.g. `BTC` |
| collateralAmt | String | Yes | Collateral amount |

Response Example

```
{
 "code": "0",
 "data": [
 ],
 "msg": ""
}

```

#### Response Parameters

code = `0` means your request has been accepted (It doesn't mean the request has been successfully handled.)

### GET / Loan info

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-info`

Request Example

```
GET /api/v5/finance/flexible-loan/loan-info
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.loan_info()
print(result)
```

Response Example

```
{
 "code": "0",
 "data": [
 {
 "collateralData": [
 {
 "amt": "0.0000097",
 "ccy": "COMP"
 },
 {
 "amt": "0.78",
 "ccy": "STX"
 },
 {
 "amt": "0.001",
 "ccy": "DOT"
 },
 {
 "amt": "0.05357864",
 "ccy": "LUNA"
 }
 ],
 "collateralNotionalUsd": "1.5078763",
 "curLTV": "0.5742",
 "liqLTV": "0.8374",
 "loanData": [
 {
 "amt": "0.86590608",
 "ccy": "USDC"
 }
 ],
 "loanNotionalUsd": "0.8661285",
 "marginCallLTV": "0.7374",
 "riskWarningData": {
 "instId": "",
 "liqPx": ""
 }
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| loanNotionalUsd | String | Loan value in `USD` |
| loanData | Array of objects | Loan data |
| > ccy | String | Loan currency, e.g. `USDT` |
| > amt | String | Loan amount |
| collateralNotionalUsd | String | Collateral value in `USD` |
| collateralData | Array of objects | Collateral data |
| > ccy | String | Collateral currency, e.g. `BTC` |
| > amt | String | Collateral amount |
| riskWarningData | Object | Risk warning data |
| > instId | String | Liquidation instrument ID, e.g. `BTC-USDT`This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "". |
| > liqPx | String | Liquidation priceThe unit of the liquidation price is the quote currency of the instrument, e.g. `USDT` in `BTC-USDT`.This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "". |
| curLTV | String | Current LTV, e.g. `0.1` represents `10%`Note: LTV = Loan to Value |
| marginCallLTV | String | Margin call LTV, e.g. `0.1` represents `10%`If your loan hits the margin call LTV, our system will automatically warn you that your loan is getting close to forced liquidation. |
| liqLTV | String | Liquidation LTV, e.g. `0.1` represents `10%`If your loan reaches liquidation LTV, it'll trigger forced liquidation. When this happens, you'll lose access to your collateral and any repayments made. |

### GET / Loan history

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-history`

Request Example

```
GET /api/v5/finance/flexible-loan/loan-history
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.loan_history()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| type | String | No | Action type`borrowed``repaid``collateral_locked``collateral_released``forced_repayment_buy``forced_repayment_sell``forced_liquidation``partial_liquidation``sell_collateral``buy_transition_coin``sell_transition_coin``buy_borrowed_coin` |
| after | String | No | Pagination of data to return records earlier than the requested `refId`(not include) |
| before | String | No | Pagination of data to return records newer than the requested `refId`(not include) |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "amt": "-0.001",
 "ccy": "DOT",
 "refId": "17316594851045086",
 "ts": "1731659485000",
 "type": "collateral_locked"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| refId | String | Reference ID |
| type | String | Action type |
| ccy | String | Currency, e.g. `BTC` |
| amt | String | Amount |
| ts | String | Timestamp for the action, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Accrued interest

Retrieves the interest accrual history for flexible loans over the past 30 days.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/interest-accrued`

Request Example

```
GET /api/v5/finance/flexible-loan/interest-accrued
```

```
from okx.Finance import FlexibleLoan

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "0" # Production trading:0 , demo trading:1

flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
result = flexibleLoanAPI.interest_accrued()
print(result)
```

#### Request Parameters

| Parameters | Types | Required | Description |
| --- | --- | --- | --- |
| ccy | String | No | Loan currency, e.g. `BTC` |
| after | String | No | Pagination of data to return records earlier than the requested `refId`(not include) |
| before | String | No | Pagination of data to return records newer than the requested `refId`(not include) |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |

返回结果

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDC",
 "interest": "0.00004054",
 "interestRate": "0.41",
 "loan": "0.86599309",
 "refId": "17319133035195744",
 "ts": "1731913200000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| refId | String | Reference ID |
| ccy | String | Loan currency, e.g. `BTC` |
| loan | String | Loan when calculated interest |
| interest | String | Interest |
| interestRate | String | APY, e.g. `0.01` represents `1%` |
| ts | String | Timestamp to calculated interest, Unix timestamp format in milliseconds, e.g. `1597026383085` |
