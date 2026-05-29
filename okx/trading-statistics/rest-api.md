## REST API

The API endpoints of `Trading Statistics` do not require authentication.

### Get support coin

Retrieve the currencies supported by the trading statistics endpoints.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/trading-data/support-coin`

Request Example

```
GET /api/v5/rubik/stat/trading-data/support-coin
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the currencies supported by the trading statistics endpoints
result = tradingDataAPI.get_support_coin()
print(result)
```

Response Example

```
{
 "code": "0",
 "data": {
 "contract": [
 "ADA",
 "BTC"
 ],
 "option": [
 "BTC"
 ],
 "spot": [
 "ADA",
 "BTC"
 ]
 },
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| contract | Array of strings | Currency supported by derivatives trading data |
| option | Array of strings | Currency supported by option trading data |
| spot | Array of strings | Currency supported by spot trading data |

### Get contract open interest history

Retrieve the contract open interest statistics of futures and perp. This endpoint can retrieve the latest 1,440 data entries.

For period=1D, the data time range is up to January 1, 2024; for other periods, the data time range is up to early February 2024.

#### Rate limit: 10 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/open-interest-history`

Request example

```
GET /api/v5/rubik/stat/contracts/open-interest-history?instId=BTC-USDT-SWAP
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the open interest history
result = tradingDataAPI.get_open_interest_history(
 instId="BTC-USDT-SWAP"
)

print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP Only applicable to `FUTURES`, `SWAP` |
| period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`] UTC+8 opening price k-line: [`6H/12H/1D/2D/3D/5D/1W/1M/3M`] UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`] |
| end | string | No | Pagination of data to return records earlier than the requested `ts` |
| begin | string | No | return records newer than the requested `ts` |
| limit | string | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1701417600000", // timestamp
 "731377.57500501", // open interest (oi, contracts)
 "111", // open interest (oiCcy, coin)
 "8888888" // open interest (oiUsd, USD)
 ],
 [
 "1701417500000", // timestamp
 "731377.57500501", // open interest (oi, contracts)
 "111", // open interest (oiCcy, coin)
 "8888888" // open interest (oiUsd, USD)
 ]
 ]
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085` |
| oi | String | Open interest in the unit of contracts |
| oiCcy | String | Open interest in the unit of crypto |
| oiUsd | String | Open interest in the unit of USD |

The data returned will be arranged in an array like this: [ts, oi, oiCcy, oiUsd].

### Get taker volume

Retrieve the taker volume for both buyers and sellers.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/taker-volume`

Request Example

```
GET /api/v5/rubik/stat/taker-volume?ccy=BTC&instType=SPOT
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the taker volume for both buyers and sellers
result = tradingDataAPI.get_taker_volume(
 ccy="BTC",
 instType="SPOT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| instType | String | Yes | Instrument type`SPOT``CONTRACTS` |
| begin | String | No | Begin time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| end | String | No | End time, Unix timestamp format in milliseconds, e.g. `1597026383011` |
| period | String | No | Period, the default is `5m`, e.g. [`5m`/`1H`/`1D`] `5m` granularity can only query data within two days at most`1H` granularity can only query data within 30 days at most `1D` granularity can only query data within 180 days at most |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630425600000",
 "7596.2651",
 "7149.4855"
 ],
 [
 "1630339200000",
 "5312.7876",
 "7002.7541"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| sellVol | String | Sell volume |
| buyVol | String | Buy volume |

The return value array order is: [ts,sellVol,buyVol]

### Get contract taker volume

Retrieve the contract taker volume for both buyers and sellers. This endpoint can retrieve the latest 1,440 data entries.

For period=1D, the data time range is up to January 1, 2024; for other periods, the data time range is up to early February 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/taker-volume-contract`

Request example

```
GET /api/v5/rubik/stat/taker-volume-contract?instId=BTC-USDT-SWAP
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the contract taker volume for both buyers and sellers
result = tradingDataAPI.get_contract_taker_volume(
 instId="BTC-USDT-SWAP"
)

print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP Only applicable to `FUTURES`, `SWAP` |
| period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`] UTC+8 opening price k-line:[`6H/12H/1D/2D/3D/5D/1W/1M/3M`] UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`] |
| unit | string | No | The unit of buy/sell volume, the default is `1` `0`: Crypto `1`: Contracts `2`: U |
| end | string | No | return records earlier than the requested `ts` |
| begin | string | No | return records newer than the requested `ts` |
| limit | string | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1701417600000", // timestamp
 "200", // taker sell volume
 "380" // taker buy volume
 ],
 [
 "1701417600000", // timestamp
 "100", // taker sell volume
 "300" // taker buy volume
 ]
 ]
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085` |
| sellVol | String | taker sell volume |
| buyVol | String | taker buy volume |

The data returned will be arranged in an array like this: [ts, sellVol, buyVol].

### Get margin long/short ratio

Retrieve the ratio of cumulative amount of quote currency to base currency.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/margin/loan-ratio`

Request Example

```
GET /api/v5/rubik/stat/margin/loan-ratio?ccy=BTC
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the ratio of cumulative amount between currency margin quote currency and base currency
result = tradingDataAPI.get_margin_lending_ratio(
 ccy="BTC",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| begin | String | No | Begin time, e.g. `1597026383085` |
| end | String | No | End time, e.g. `1597026383085` |
| period | String | No | Period`m`: Minute, `H`: Hour, `D`: Daythe default is `5m`, e.g. [`5m`/`1H`/`1D`] `5m` granularity can only query data within two days at most`1H` granularity can only query data within 30 days at most`1D` granularity can only query data within 180 days at most |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630492800000",
 "0.4614"
 ],
 [
 "1630492500000",
 "0.5767"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| ratio | String | Margin lending ratio |

The return value array order is: [ts,ratio]

### Get top traders contract long/short ratio

Retrieve the account net long/short ratio of a contract for top traders. Top traders refer to the top 5% of traders with the largest open position value. This endpoint can retrieve the latest 1,440 data entries. The data time range is up to March 22, 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader`

Request Example

```
GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader?instId=BTC-USDT-SWAP
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the top trader long short account ratio
result = tradingDataAPI.get_top_trader_long_short_account_ratio(
 instId="BTC-USDT-SWAP"
)

print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP Only applicable to `FUTURES`, `SWAP` |
| period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`] UTC+8 opening price k-line: [`6H/12H/1D/2D/3D/5D/1W/1M/3M`] UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`] |
| end | string | No | return records earlier than the requested `ts` |
| begin | string | No | return records newer than the requested `ts` |
| limit | string | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1701417600000", // timestamp
 "1.1739" // long/short account num ratio of top traders
 ],
 [
 "1701417600000", // timestamp
 "0.1236" // long/short account num ratio of top traders
 ],
 ]
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085` |
| longShortAcctRatio | String | Long/short account num ratio of top traders |

The data returned will be arranged in an array like this: [ts, longShortAcctRatio].

### Get top traders contract long/short ratio (by position)

Retrieve the position long/short ratio of a contract for top traders. Top traders refer to the top 5% of traders with the largest open position value. This endpoint can retrieve the latest 1,440 data entries. The data time range is up to March 22, 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader`

Request example

```
GET /api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader?instId=BTC-USDT-SWAP
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the top trader long short position ratio
result = tradingDataAPI.get_top_trader_long_short_position_ratio(
 instId="BTC-USDT-SWAP"
)

print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | string | Yes | Instrument ID, e.g. `BTC-USDT-SWAP` Only applicable to `FUTURES`/`SWAP` |
| period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`] UTC+8 opening price k-line: [`6H/12H/1D/2D/3D/5D/1W/1M/3M`] UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`] |
| end | string | No | return records earlier than the requested `ts` |
| begin | string | No | return records newer than the requested `ts` |
| limit | string | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1701417600000", // timestamp
 "1.1739" // long/short position num ratio of top traders
 ],
 [
 "1701417600000", // timestamp
 "0.1236" // long/short position num ratio of top traders
 ],
 ]
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085` |
| longShortPosRatio | String | Long/short position ratio of top traders |

The data returned will be arranged in an array like this: [ts, longShortPosRatio].

### Get contract long/short ratio

Retrieve the account long/short ratio of a contract. This endpoint can retrieve the latest 1,440 data entries.

For period=1D, the data time range is up to January 1, 2024; for other periods, the data time range is up to early February 2024.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP + Instrument ID

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract`

Request example

```
GET /api/v5/rubik/stat/contracts/long-short-account-ratio-contract?instId=BTC-USDT-SWAP
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the account long short ratio of a contract
result = tradingDataAPI.get_contract_long_short_ratio(
 instId="BTC-USDT-SWAP"
)

print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | string | Yes | Instrument ID, eg: BTC-USDT-SWAP Only applicable to `FUTURES`, `SWAP` |
| period | string | No | Bar size, the default is `5m`, e.g. [`5m/15m/30m/1H/2H/4H`] UTC+8 opening price k-line:[`6H/12H/1D/2D/3D/5D/1W/1M/3M`] UTC+0 opening price k-line: [`6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/5Dutc/1Wutc/1Mutc/3Mutc`] |
| end | string | No | return records earlier than the requested `ts` |
| begin | string | No | return records newer than the requested `ts` |
| limit | string | No | Number of results per request. The maximum is `100`. The default is `100`. |

Response example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1701417600000", // timestamp
 "1.1739" // long/short account num ratio of traders
 ],
 [
 "1701417600000", // timestamp
 "0.1236" // long/short account num ratio of traders
 ],
 ]
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp, millisecond format of Unix timestamp, e.g. `1597026383085` |
| longShortAcctRatio | String | Long/short position num ratio of all traders |

The data returned will be arranged in an array like this: [ts, longAcctPosRatio].

### Get long/short ratio

Retrieve the ratio of users with net long vs net short positions for Expiry Futures and Perpetual Futures.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/long-short-account-ratio`

Request Example

```
GET /api/v5/rubik/stat/contracts/long-short-account-ratio?ccy=BTC
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the ratio of users with net long vs net short positions for Expiry Futures and Perpetual Futures
result = tradingDataAPI.get_long_short_ratio(
 ccy="BTC",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| begin | String | No | Begin time, e.g. `1597026383085` |
| end | String | No | End time, e.g. `1597026383011` |
| period | String | No | Period, the default is `5m`, e.g. [`5m/1H/1D`] `5m` granularity can only query data within two days at most`1H` granularity can only query data within 30 days at most `1D` granularity can only query data within 180 days at most |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630502100000",
 "1.25"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| ratio | String | Long/Short ratio |

The return value array order is: [ts,ratio]

### Get contracts open interest and volume

Retrieve the open interest and trading volume for Expiry Futures and Perpetual Futures.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/contracts/open-interest-volume`

Request Example

```
GET /api/v5/rubik/stat/contracts/open-interest-volume?ccy=BTC
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the open interest and trading volume for Expiry Futures and Perpetual Futures
result = tradingDataAPI.get_contracts_interest_volume(
 ccy="BTC",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| begin | String | No | Begin time, e.g. `1597026383085` |
| end | String | No | End time, e.g. `1597026383011` |
| period | String | No | Period, the default is `5m`, e.g. [`5m/1H/1D`] `5m` granularity can only query data within two days at most`1H` granularity can only query data within 30 days at most `1D` granularity can only query data within 180 days at most |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630502400000",
 "1713028741.6898",
 "39800873.554"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| oi | String | Total open interest（USD） |
| vol | String | Total trading volume（USD） |

The return value array order is: [ts,oi,vol]

### Get options open interest and volume

Retrieve the open interest and trading volume for options.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume`

Request Example

```
GET /api/v5/rubik/stat/option/open-interest-volume?ccy=BTC
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the open interest and trading volume for options
result = tradingDataAPI.get_options_interest_volume(
 ccy="BTC",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| period | String | No | Period, the default is `8H`. e.g. [`8H/1D`] Each granularity can only query 72 pieces of data at the earliest |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630368000000",
 "3458.1000",
 "78.8000"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| oi | String | Total open interest , unit in `ccy` (in request parameter) |
| vol | String | Total trading volume , unit in `ccy` (in request parameter) |

The return value array order is: [ts,oi,vol]

### Get put/call ratio

Retrieve the open interest ratio and trading volume ratio of calls vs puts.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-ratio`

Request Example

```
GET /api/v5/rubik/stat/option/open-interest-volume-ratio?ccy=BTC
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the open interest ratio and trading volume ratio of calls vs puts
result = tradingDataAPI.get_put_call_ratio(
 ccy="BTC",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| period | String | No | Period, the default is `8H`. e.g. [`8H/1D`] Each granularity can only query 72 pieces of data at the earliest |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630512000000",
 "2.7261",
 "2.3447"
 ],
 [
 "1630425600000",
 "2.8101",
 "2.3438"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp of data generation time |
| oiRatio | String | Long/Short open interest ratio |
| volRatio | String | Long/Short trading volume ratio |

The return value array order is: [ts,oiRatio,volRatio]

### Get open interest and volume (expiry)

Retrieve the open interest and trading volume of calls and puts for each upcoming expiration.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-expiry`

Request Example

```
GET /api/v5/rubik/stat/option/open-interest-volume-expiry?ccy=BTC
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the open interest and trading volume of calls and puts for each upcoming expiration
result = tradingDataAPI.get_interest_volume_expiry(
 ccy="BTC"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| period | String | No | Period, the default is `8H`. e.g. [`8H/1D`] Each granularity can provide only one latest piece of data |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630540800000",
 "20210902",
 "6.4",
 "18.4",
 "0.7",
 "0.4"
 ],
 [
 "1630540800000",
 "20210903",
 "47",
 "36.6",
 "1",
 "10.7"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| expTime | String | Contract expiry date, the format is `YYYYMMDD`, e.g. `20210623` |
| callOI | String | Total call open interest (`coin` as the unit) |
| putOI | String | Total put open interest (`coin` as the unit) |
| callVol | String | Total call trading volume (`coin` as the unit) |
| putVol | String | Total put trading volume (`coin` as the unit) |

The return value array order is: [ts,expTime,callOI,putOI,callVol,putVol]

### Get open interest and volume (strike)

Retrieve the taker volume for both buyers and sellers of calls and puts.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/open-interest-volume-strike`

Request Example

```
GET /api/v5/rubik/stat/option/open-interest-volume-strike?ccy=BTC&expTime=20210901
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# Retrieve the taker volume for both buyers and sellers of calls and puts
result = tradingDataAPI.get_interest_volume_strike(
 ccy="BTC",
 expTime="20210623"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | Currency |
| expTime | String | Yes | Contract expiry date, the format is `YYYYMMdd`, e.g. `20210623` |
| period | String | No | Period, the default is `8H`. e.g. [`8H/1D`] Each granularity can provide only one latest piece of data |

Response Example

```
{
 "code": "0",
 "data": [
 [
 "1630540800000",
 "10000",
 "0",
 "0.5",
 "0",
 "0"
 ],
 [
 "1630540800000",
 "14000",
 "0",
 "5.2",
 "0",
 "0"
 ]
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| strike | String | Strike price |
| callOI | String | Total call open interest (`coin` as the unit) |
| putOI | String | Total put open interest (`coin` as the unit) |
| callVol | String | Total call trading volume (`coin` as the unit) |
| putVol | String | Total put trading volume (`coin` as the unit) |

The return value array order is: [ts,strike,callOI,putOI,callVol,putVol]

### Get taker flow

This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rubik/stat/option/taker-block-volume`

Request Example

```
GET /api/v5/rubik/stat/option/taker-block-volume?ccy=BTC
```

```
import okx.TradingData as TradingData_api

flag = "0" # Production trading:0 , demo trading:1

tradingDataAPI = TradingData_api.TradingDataAPI(flag=flag)

# This shows the relative buy/sell volume for calls and puts. It shows whether traders are bullish or bearish on price and volatility
result = tradingDataAPI.get_taker_block_volume(
 ccy="BTC",
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| ccy | String | Yes | currency |
| period | String | No | period, the default is `8H`. e.g. [`8H/1D`] Each granularity can provide only one latest piece of data |

Response Example

```
{
 "code": "0",
 "data": [
 "1630512000000",
 "8.55",
 "67.3",
 "16.05",
 "16.3",
 "126.4",
 "40.7"
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Timestamp |
| callBuyVol | String | call option buy volume, in settlement currency |
| callSellVol | String | call option sell volume, in settlement currency |
| putBuyVol | String | put option buy volume, in settlement currency |
| putSellVol | String | put option sell volume, in settlement currency |
| callBlockVol | String | call block volume |
| putBlockVol | String | put block volume |

The return value array order is: [ts,callBuyVol,callSellVol,putBuyVol,putSellVol,callBlockVol,putBlockVol]
