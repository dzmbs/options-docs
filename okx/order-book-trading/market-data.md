## Market Data

The API endpoints of `Market Data` do not require authentication.

There are multiple services for market data, and each service has an independent cache. A random service will be requested for every request. So for two requests, it’s expected that the data obtained in the second request is earlier than the first request.

For event contracts, market data module will only return data of the YES side. Users can derive NO side data on their own.

### GET / Tickers

Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours. Best ask price may be lower than the best bid price during the pre-open period.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/tickers`

Request Example

```
GET /api/v5/market/tickers?instType=SWAP
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours
result = marketDataAPI.get_tickers(
 instType="SWAP"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`SPOT``SWAP``FUTURES``OPTION``EVENTS` |
| instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "instType":"SWAP",
 "instId":"LTC-USD-SWAP",
 "last":"9999.99",
 "lastSz":"1",
 "askPx":"9999.99",
 "askSz":"11",
 "bidPx":"8888.88",
 "bidSz":"5",
 "open24h":"9000",
 "high24h":"10000",
 "low24h":"8888.88",
 "volCcy24h":"2222",
 "vol24h":"2222",
 "sodUtc0":"0.1",
 "sodUtc8":"0.1",
 "ts":"1597026383085"
 },
 {
 "instType":"SWAP",
 "instId":"BTC-USD-SWAP",
 "last":"9999.99",
 "lastSz":"1",
 "askPx":"9999.99",
 "askSz":"11",
 "bidPx":"8888.88",
 "bidSz":"5",
 "open24h":"9000",
 "high24h":"10000",
 "low24h":"8888.88",
 "volCcy24h":"2222",
 "vol24h":"2222",
 "sodUtc0":"0.1",
 "sodUtc8":"0.1",
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| last | String | Last traded price |
| lastSz | String | Last traded size. 0 represents there is no trading volume |
| askPx | String | Best ask price |
| askSz | String | Best ask size |
| bidPx | String | Best bid price |
| bidSz | String | Best bid size |
| open24h | String | Open price in the past 24 hours |
| high24h | String | Highest price in the past 24 hours |
| low24h | String | Lowest price in the past 24 hours |
| volCcy24h | String | 24h trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. e.g. the unit is BTC for BTC-USD-SWAP and BTC-USDT-SWAP If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| vol24h | String | 24h trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| sodUtc0 | String | Open price in the UTC 0 |
| sodUtc8 | String | Open price in the UTC 8 |
| ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Ticker

Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours. Best ask price may be lower than the best bid price during the pre-open period.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/ticker`

Request Example

```
GET /api/v5/market/ticker?instId=BTC-USD-SWAP
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours
result = marketDataAPI.get_ticker(
 instId="BTC-USD-SWAP"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USD-SWAP` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "instType":"SWAP",
 "instId":"BTC-USD-SWAP",
 "last":"9999.99",
 "lastSz":"0.1",
 "askPx":"9999.99",
 "askSz":"11",
 "bidPx":"8888.88",
 "bidSz":"5",
 "open24h":"9000",
 "high24h":"10000",
 "low24h":"8888.88",
 "volCcy24h":"2222",
 "vol24h":"2222",
 "sodUtc0":"2222",
 "sodUtc8":"2222",
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| last | String | Last traded price |
| lastSz | String | Last traded size. 0 represents there is no trading volume |
| askPx | String | Best ask price |
| askSz | String | Best ask size |
| bidPx | String | Best bid price |
| bidSz | String | Best bid size |
| open24h | String | Open price in the past 24 hours |
| high24h | String | Highest price in the past 24 hours |
| low24h | String | Lowest price in the past 24 hours |
| volCcy24h | String | 24h trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| vol24h | String | 24h trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| sodUtc0 | String | Open price in the UTC 0 |
| sodUtc8 | String | Open price in the UTC 8 |
| ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |

### GET / Order book

Retrieve order book of the instrument. The data will be updated once every 50 milliseconds. Best ask price may be lower than the best bid price during the pre-open period.

This endpoint does not return data immediately. Instead, it returns the latest data once the server-side cache has been updated.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/books`

Request Example

```
GET /api/v5/market/books?instId=BTC-USDT
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve order book of the instrument
result = marketDataAPI.get_orderbook(
 instId="BTC-USDT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| sz | String | No | Order book depth per side. Maximum 400, e.g. 400 bids + 400 asks Default returns to `1` depth data |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "asks": [
 [
 "41006.8",
 "0.60038921",
 "0",
 "1"
 ]
 ],
 "bids": [
 [
 "41006.3",
 "0.30178218",
 "0",
 "2"
 ]
 ],
 "ts": "1629966436396",
 "seqId": 3235851742
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| asks | Array of Arrays | Order book on sell side |
| bids | Array of Arrays | Order book on buy side |
| ts | String | Order book generation time |
| seqId | Integer | Sequence ID of the current message |

An example of the array of asks and bids values: ["411.8", "10", "0", "4"]

- "411.8" is the depth price

- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)

- "0" is part of a deprecated feature and it is always "0"

- "4" is the number of orders at the price.

The order book data will be updated around once a second during the call auction.

### GET / Full order book

Retrieve order book of the instrument. The data will be updated once a second. Best ask price may be lower than the best bid price during the pre-open period.

This endpoint does not return data immediately. Instead, it returns the latest data once the server-side cache has been updated.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/books-full`

Request Example

```
GET /api/v5/market/books-full?instId=BTC-USDT&sz=1
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| sz | String | No | Order book depth per side. Maximum 5000, e.g. 5000 bids + 5000 asks Default returns to `1` depth data. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "asks": [
 [
 "41006.8",
 "0.60038921",
 "1"
 ]
 ],
 "bids": [
 [
 "41006.3",
 "0.30178218",
 "2"
 ]
 ],
 "ts": "1629966436396"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| asks | Array of Arrays | Order book on sell side |
| bids | Array of Arrays | Order book on buy side |
| ts | String | Order book generation time |

An example of the array of asks and bids values: ["411.8", "10", "4"]

- "411.8" is the depth price

- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)

- "4" is the number of orders at the price.

The order book data will be updated around once a second during the call auction.

### GET / Candlesticks

Retrieve the candlestick charts. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/candles`

Request Example

```
GET /api/v5/market/candles?instId=BTC-USDT
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the candlestick charts
result = marketDataAPI.get_candlesticks(
 instId="BTC-USDT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| bar | String | No | Bar size, the default is `1m`e.g. [1m/3m/5m/15m/30m/1H/2H/4H] UTC+8 opening price k-line: [6H/12H/1D/2D/3D/1W/1M/3M]UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc] |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually |
| limit | String | No | Number of results per request. The maximum is `300`. The default is `100`. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1597026383085",
 "3.721",
 "3.743",
 "3.677",
 "3.708",
 "8422410",
 "22698348.04828491",
 "12698348.04828491",
 "0"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "24912403",
 "67632347.24399722",
 "37632347.24399722",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| o | String | Open price |
| h | String | highest price |
| l | String | Lowest price |
| c | String | Close price |
| vol | String | Trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| volCcy | String | Trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| volCcyQuote | String | Trading volume, the value is the quantity in quote currency e.g. The unit is USDT for BTC-USDT and BTC-USDT-SWAP;The unit is USD for BTC-USD-SWAP |
| confirm | String | The state of candlesticks.`0`: K line is uncompleted`1`: K line is completed |

The first candlestick data may be incomplete, and should not be polled repeatedly.

The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm].

For the current cycle of k-line data, when there is no transaction, the opening high and closing low default take the closing price of the previous cycle.

### GET / Candlesticks history

Retrieve history candlestick charts from recent years(It is last 3 months supported for 1s candlestick).

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-candles`

Request Example

```
GET /api/v5/market/history-candles?instId=BTC-USDT
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve history candlestick charts from recent years
result = marketDataAPI.get_history_candlesticks(
 instId="BTC-USDT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| after | String | No | Pagination of data to return records earlier than the requested `ts` |
| before | String | No | Pagination of data to return records newer than the requested `ts`. The latest data will be returned when using `before` individually |
| bar | String | No | Bar size, the default is `1m`e.g. [1s/1m/3m/5m/15m/30m/1H/2H/4H] UTC+8 opening price k-line: [6H/12H/1D/2D/3D/1W/1M/3M]UTC+0 opening price k-line: [6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc] |
| limit | String | No | Number of results per request. The maximum is `300`. The default is `100`. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 [
 "1597026383085",
 "3.721",
 "3.743",
 "3.677",
 "3.708",
 "8422410",
 "22698348.04828491",
 "12698348.04828491",
 "1"
 ],
 [
 "1597026383085",
 "3.731",
 "3.799",
 "3.494",
 "3.72",
 "24912403",
 "67632347.24399722",
 "37632347.24399722",
 "1"
 ]
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| o | String | Open price |
| h | String | Highest price |
| l | String | Lowest price |
| c | String | Close price |
| vol | String | Trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| volCcy | String | Trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| volCcyQuote | String | Trading volume, the value is the quantity in quote currencye.g. The unit is USDT for BTC-USDT and BTC-USDT-SWAP;The unit is USD for BTC-USD-SWAP |
| confirm | String | The state of candlesticks`0`: K line is uncompleted`1`: K line is completed |



The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,volCcy,volCcyQuote,confirm]

1s candle is not supported by OPTION, but it is supported by other business lines (SPOT, MARGIN, FUTURES and SWAP)

### GET / Trades

Retrieve the recent transactions of an instrument.

#### Rate Limit: 100 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/trades`

Request Example

```
GET /api/v5/market/trades?instId=BTC-USDT
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the recent transactions of an instrument
result = marketDataAPI.get_trades(
 instId="BTC-USDT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| limit | String | No | Number of results per request. The maximum is `500`; The default is `100` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "BTC-USDT",
 "side": "sell",
 "sz": "0.00001",
 "source": "0",
 "px": "29963.2",
 "tradeId": "242720720",
 "ts": "1654161646974"
 },
 {
 "instId": "BTC-USDT",
 "side": "sell",
 "sz": "0.00001",
 "source": "0",
 "px": "29964.1",
 "tradeId": "242720719",
 "ts": "1654161641568"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| tradeId | String | Trade ID |
| px | String | Trade price |
| sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| side | String | Trade side of taker `buy` `sell` |
| source | String | Order source `0`: normal order `1`: Enhanced Liquidity Program order |
| ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |

Up to 500 most recent historical public transaction data can be retrieved.

### GET / Trades history

Retrieve the recent transactions of an instrument from the last 3 months with pagination.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/history-trades`

Request Example

```
GET /api/v5/market/history-trades?instId=BTC-USDT
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the recent transactions of an instrument from the last 3 months with pagination
result = marketDataAPI.get_history_trades(
 instId="BTC-USD-SWAP"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |
| type | String | No | Pagination Type `1`: tradeId `2`: timestampThe default is `1` |
| after | String | No | Pagination of data to return records earlier than the requested tradeId or ts. |
| before | String | No | Pagination of data to return records newer than the requested tradeId. Do not support timestamp for pagination. The latest data will be returned when using `before` individually |
| limit | String | No | Number of results per request. The maximum and default both are `100` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "BTC-USDT",
 "side": "sell",
 "sz": "0.00001",
 "source": "0",
 "px": "29963.2",
 "tradeId": "242720720",
 "ts": "1654161646974"
 },
 {
 "instId": "BTC-USDT",
 "side": "sell",
 "sz": "0.00001",
 "source": "0",
 "px": "29964.1",
 "tradeId": "242720719",
 "ts": "1654161641568"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| tradeId | String | Trade ID |
| px | String | Trade price |
| sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| side | String | Trade side of taker `buy` `sell` |
| source | String | Order source `0`: normal order`1`: Enhanced Liquidity Program order |
| ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |

### GET / Option trades by instrument family

Retrieve the recent transactions of an instrument under same instFamily. The maximum is 100.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/option/instrument-family-trades`

Request Example

```
GET /api/v5/market/option/instrument-family-trades?instFamily=BTC-USD
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instFamily | String | Yes | Instrument family, e.g. BTC-USDApplicable to `OPTION` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "vol24h": "103381",
 "tradeInfo": [
 {
 "instId": "BTC-USD-221111-17750-C",
 "side": "sell",
 "sz": "1",
 "px": "0.0075",
 "tradeId": "20",
 "ts": "1668090715058"
 },
 {
 "instId": "BTC-USD-221111-17750-C",
 "side": "sell",
 "sz": "91",
 "px": "0.01",
 "tradeId": "19",
 "ts": "1668090421062"
 }
 ],
 "optType": "C"
 },
 {
 "vol24h": "144499",
 "tradeInfo": [
 {
 "instId": "BTC-USD-230127-10000-P",
 "side": "sell",
 "sz": "82",
 "px": "0.019",
 "tradeId": "23",
 "ts": "1668090967057"
 },
 {
 "instId": "BTC-USD-221111-16250-P",
 "side": "sell",
 "sz": "102",
 "px": "0.0045",
 "tradeId": "24",
 "ts": "1668090885050"
 }
 ],
 "optType": "P"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| vol24h | String | 24h trading volume, with a unit of contract. |
| optType | String | Option type, C: Call P: Put |
| tradeInfo | Array of objects | The list trade data |
| > instId | String | The Instrument ID |
| > tradeId | String | Trade ID |
| > px | String | Trade price |
| > sz | String | Trade quantity. The unit is contract. |
| > side | String | Trade side`buy``sell` |
| > ts | String | Trade time, Unix timestamp format in milliseconds, e.g. 1597026383085. |

### GET / Option trades

The maximum is 100.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/option-trades`

Request Example

```
GET /api/v5/public/option-trades?instFamily=BTC-USD
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Conditional | Instrument ID, e.g. BTC-USD-221230-4000-C, Either `instId` or `instFamily` is required. If both are passed, `instId` will be used. |
| instFamily | String | Conditional | Instrument family, e.g. BTC-USD |
| optType | String | No | Option type, `C`: Call `P`: put |

Response Example

```
{
 "code": "0",
 "data": [
 {
 "fillVol": "0.24415013671875",
 "fwdPx": "16676.907614127158",
 "idxPx": "16667",
 "instFamily": "BTC-USD",
 "instId": "BTC-USD-221230-16600-P",
 "markPx": "0.006308943261227884",
 "optType": "P",
 "px": "0.005",
 "side": "sell",
 "sz": "30",
 "tradeId": "65",
 "ts": "1672225112048"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| instFamily | String | Instrument family |
| tradeId | String | Trade ID |
| px | String | Trade price |
| sz | String | Trade quantity. The unit is contract. |
| side | String | Trade side `buy` `sell` |
| optType | String | Option type, C: Call P: Put |
| fillVol | String | Implied volatility while trading (Correspond to trade price) |
| fwdPx | String | Forward price while trading |
| idxPx | String | Index price while trading |
| markPx | String | Mark price while trading |
| ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |

### GET / 24H total volume

The 24-hour trading volume is calculated on a rolling basis.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/platform-24-volume`

Request Example

```
GET /api/v5/market/platform-24-volume
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve 24 total volume
result = marketDataAPI.get_volume()
print(result)
```

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "volCny": "230900886396766",
 "volUsd": "34462818865189",
 "ts": "1657856040389"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| volUsd | String | 24-hour total trading volume from the order book trading in "USD" |
| volCny | String | 24-hour total trading volume from the order book trading in "CNY" |
| ts | String | Data return time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### GET / Call auction details

Retrieve call auction details.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/call-auction-details`

Request Example

```
GET /api/v5/market/call-auction-details?instId=ONDO-USDC
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "ONDO-USDC",
 "unmatchedSz": "9988764",
 "eqPx": "0.6",
 "matchedSz": "44978",
 "state": "continuous_trading",
 "auctionEndTime": "1726542000000",
 "ts": "1726542000007"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| eqPx | String | Equilibrium price |
| matchedSz | String | Matched size for both buy and sellThe unit is in base currency |
| unmatchedSz | String | Unmatched size |
| auctionEndTime | String | Call auction end time. Unix timestamp in milliseconds. |
| state | String | Trading state of the symbol`call_auction``continuous_trading` |
| ts | String | Data generation time. Unix timestamp in millieseconds. |

During call auction, users can get the updates of equilibrium price, matched size, unmatched size, and auction end time. The data will be updated around once a second. The endpoint returns the actual open price, matched size, and unmatched size when the call auction ends.

For symbols that never go through call auction, the endpoint will also return results but with state always as `continuous_trading` and other fields as 0 or empty.

### WS / Tickers channel

Retrieve the last traded price, bid price, ask price and 24-hour trading volume of instruments. Best ask price may be lower than the best bid price during the pre-open period.

The fastest rate is 1 update/100ms. There will be no update if the event is not triggered. The events which can trigger update: trade, the change on best ask/bid.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "tickers",
 "instId": "BTC-USDT"
 }
 ]
}
```

```
import asyncio

from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [{
 "channel": "tickers",
 "instId": "BTC-USDT"
 }]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`tickers` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "tickers",
 "instId": "BTC-USDT"
 },
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "tickers",
 "instId": "BTC-USDT"
 },
 "data": [
 {
 "instType": "SPOT",
 "instId": "BTC-USDT",
 "last": "9999.99",
 "lastSz": "0.1",
 "askPx": "9999.99",
 "askSz": "11",
 "bidPx": "8888.88",
 "bidSz": "5",
 "open24h": "9000",
 "high24h": "10000",
 "low24h": "8888.88",
 "volCcy24h": "2222",
 "vol24h": "2222",
 "sodUtc0": "2222",
 "sodUtc8": "2222",
 "ts": "1597026383085"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > last | String | Last traded price |
| > lastSz | String | Last traded size. 0 represents there is no trading volume |
| > askPx | String | Best ask price |
| > askSz | String | Best ask size |
| > bidPx | String | Best bid price |
| > bidSz | String | Best bid size |
| > open24h | String | Open price in the past 24 hours |
| > high24h | String | Highest price in the past 24 hours |
| > low24h | String | Lowest price in the past 24 hours |
| > volCcy24h | String | 24h trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| > vol24h | String | 24h trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| > sodUtc0 | String | Open price in the UTC 0 |
| > sodUtc8 | String | Open price in the UTC 8 |
| > ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### WS / Candlesticks channel

Retrieve the candlesticks data of an instrument. the push frequency is the fastest interval 1 second push the data.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "candle1D",
 "instId": "BTC-USDT"
 }
 ]
}
```

```
import asyncio

from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
 await ws.start()
 args = [
 {
 "channel": "candle1D",
 "instId": "BTC-USDT"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name `candle3M``candle1M``candle1W` `candle1D``candle2D``candle3D``candle5D``candle12H``candle6H``candle4H``candle2H``candle1H``candle30m``candle15m``candle5m``candle3m``candle1m``candle1s``candle3Mutc``candle1Mutc``candle1Wutc``candle1Dutc``candle2Dutc``candle3Dutc``candle5Dutc``candle12Hutc``candle6Hutc` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "candle1D",
 "instId": "BTC-USDT"
 },
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | yes | channel name |
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "candle1D",
 "instId": "BTC-USDT"
 },
 "data": [
 [
 "1597026383085",
 "8533.02",
 "8553.74",
 "8527.17",
 "8548.26",
 "45247",
 "529.5858061",
 "5529.5858061",
 "0"
 ]
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of Arrays | Subscribed data |
| > ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > o | String | Open price |
| > h | String | highest price |
| > l | String | Lowest price |
| > c | String | Close price |
| > vol | String | Trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| > volCcy | String | Trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| > volCcyQuote | String | Trading volume, the value is the quantity in quote currency e.g. The unit is `USDT` for `BTC-USDT` and `BTC-USDT-SWAP`The unit is `USD` for `BTC-USD-SWAP` |
| > confirm | String | The state of candlesticks`0`: K line is uncompleted`1`: K line is completed |

### WS / Trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update may aggregate multiple trades.

The message is sent only once per taker order, filled price, source. The count field is used to represent the number of aggregated matches.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "trades",
 "instId": "BTC-USDT"
 }
 ]
}
```

```
import asyncio

from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "trades",
 "instId": "BTC-USDT"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`trades` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "trades",
 "instId": "BTC-USDT"
 },
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades\", \"instId\" : \"BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "trades",
 "instId": "BTC-USDT"
 },
 "data": [
 {
 "instId": "BTC-USDT",
 "tradeId": "130639474",
 "px": "42219.9",
 "sz": "0.12060306",
 "side": "buy",
 "ts": "1630048897897",
 "count": "3",
 "source": "0",
 "seqId": 1234
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instId | String | Instrument ID, e.g. `BTC-USDT` |
| > tradeId | String | The last trade ID in the trades aggregation |
| > px | String | Trade price |
| > sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| > side | String | Trade side of taker`buy``sell` |
| > ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| > count | String | The count of trades aggregated |
| > source | String | Order source `0`: normal orders`1`: Enhanced Liquidity Program order |
| > seqId | Integer | Sequence ID of the current message. |

Aggregation function description:

1. The system will send only one message per taker order, filled price, source. The `count` field will be used to represent the number of aggregated matches.

2. The `tradeId` field in the message becomes the last trade ID in the aggregation.

3. When the `count` = 1, it means the taker order matches only one maker order with the specific price.

4. When the `count` > 1, it means the taker order matches multiple maker orders with the same price. For example, if `tradeId` = 123 and `count` = 3, it means the message aggregates the trades of `tradeId` = 123, 122, and 121. Maker side has filled multiple orders.

5. Users can use this information to compare with data from the `trades-all` channel.

6. Order book and the aggregated trades data are still published sequentially.

The seqId may be the same for different trade updates that occur at the same time.

### WS / All trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update contain only one trade.

#### URL Path

/ws/v5/business

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "trades-all",
 "instId": "BTC-USDT"
 }
 ]
}
```

```
import asyncio

from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
 await ws.start()
 args = [
 {
 "channel": "trades-all",
 "instId": "BTC-USDT"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`trades-all` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "trades-all",
 "instId": "BTC-USDT"
 },
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"trades-all\", \"instId\" : \"BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "trades-all",
 "instId": "BTC-USDT"
 },
 "data": [
 {
 "instId": "BTC-USDT",
 "tradeId": "130639474",
 "px": "42219.9",
 "sz": "0.12060306",
 "side": "buy",
 "source": "0",
 "ts": "1630048897897"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instId | String | Instrument ID, e.g. `BTC-USDT` |
| > tradeId | String | Trade ID |
| > px | String | Trade price |
| > sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| > side | String | Trade direction`buy``sell` |
| > source | String | Order source `0`: normal`1`: Enhanced Liquidity Program order |
| > ts | String | Filled time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### WS / Order book channel

Retrieve order book data. Best ask price may be lower than the best bid price during the pre-open period.

Use `books` for 400 depth levels, `books5` for 5 depth levels, `bbo-tbt` tick-by-tick 1 depth level, `books50-l2-tbt` tick-by-tick 50 depth levels, and `books-l2-tbt` for tick-by-tick 400 depth levels.

- `books`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 100 ms for the changes in the order book during that period of time.

- `books-elp`: only push ELP orders. 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 100 ms for the changes in the order book during that period of time.

- `books5`: 5 depth levels snapshot will be pushed in the initial push. Snapshot data will be pushed every 100 ms when there are changes in the 5 depth levels snapshot.

- `bbo-tbt`: 1 depth level snapshot will be pushed in the initial push. Snapshot data will be pushed every 10 ms when there are changes in the 1 depth level snapshot.

- `books-l2-tbt`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time.

- `books50-l2-tbt`: 50 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time.

- The push sequence for order book channels within the same connection and trading symbols is fixed as: bbo-tbt -> books-l2-tbt -> books50-l2-tbt -> books -> books-elp -> books5.

- Users can not simultaneously subscribe to `books-l2-tbt` and `books50-l2-tbt/books` channels for the same trading symbol.

For more details, please refer to the changelog [2024-07-17](/docs-v5/log_en/#2024-07-17)

Only API users who are VIP4 and above in trading fee tier are allowed to subscribe to "books-l2-tbt" 400 depth channels. Other users will receive error code 64003.

Only API users who are VIP4 and above in trading fee tier are allowed to subscribe to "books50-l2-tbt" 50 depth channels. Other users will receive error code 64003.

Identity verification refers to [Login](/docs-v5/en/#overview-websocket-login)

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "books",
 "instId": "BTC-USDT"
 }
 ]
}
```

```
import asyncio

from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [
 {
 "channel": "books",
 "instId": "BTC-USDT"
 }
 ]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`books``books5``bbo-tbt``books50-l2-tbt``books-l2-tbt` |
| > instId | String | Yes | Instrument ID |

Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "books",
 "instId": "BTC-USDT"
 },
 "connId": "a4d3ae55"
}

```

Failure example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"books\", \"instId\" : \"BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instId | String | Yes | Instrument ID |
| msg | String | No | Error message |
| code | String | No | Error code |
| connId | String | Yes | WebSocket connection ID |

Push Data Example: Full Snapshot

```
{
 "arg": {
 "channel": "books",
 "instId": "BTC-USDT"
 },
 "action": "snapshot",
 "data": [
 {
 "asks": [
 ["8476.98", "415", "0", "13"],
 ["8477", "7", "0", "2"],
 ["8477.34", "85", "0", "1"],
 ["8477.56", "1", "0", "1"],
 ["8505.84", "8", "0", "1"],
 ["8506.37", "85", "0", "1"],
 ["8506.49", "2", "0", "1"],
 ["8506.96", "100", "0", "2"]
 ],
 "bids": [
 ["8476.97", "256", "0", "12"],
 ["8475.55", "101", "0", "1"],
 ["8475.54", "100", "0", "1"],
 ["8475.3", "1", "0", "1"],
 ["8447.32", "6", "0", "1"],
 ["8447.02", "246", "0", "1"],
 ["8446.83", "24", "0", "1"],
 ["8446", "95", "0", "3"]
 ],
 "ts": "1597026383085",
 "checksum": -855196043,
 "prevSeqId": -1,
 "seqId": 123456
 }
 ]
}

```

Push Data Example: Incremental Data

```
{
 "arg": {
 "channel": "books",
 "instId": "BTC-USDT"
 },
 "action": "update",
 "data": [
 {
 "asks": [
 ["8476.98", "415", "0", "13"],
 ["8477", "7", "0", "2"],
 ["8477.34", "85", "0", "1"],
 ["8477.56", "1", "0", "1"],
 ["8505.84", "8", "0", "1"],
 ["8506.37", "85", "0", "1"],
 ["8506.49", "2", "0", "1"],
 ["8506.96", "100", "0", "2"]
 ],
 "bids": [
 ["8476.97", "256", "0", "12"],
 ["8475.55", "101", "0", "1"],
 ["8475.54", "100", "0", "1"],
 ["8475.3", "1", "0", "1"],
 ["8447.32", "6", "0", "1"],
 ["8447.02", "246", "0", "1"],
 ["8446.83", "24", "0", "1"],
 ["8446", "95", "0", "3"]
 ],
 "ts": "1597026383085",
 "checksum": -855196043,
 "prevSeqId": 123456,
 "seqId": 123457
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| action | String | Push data action, incremental data or full snapshot. `snapshot`: full `update`: incremental |
| data | Array of objects | Subscribed data |
| > asks | Array of Arrays | Order book on sell side |
| > bids | Array of Arrays | Order book on buy side |
| > ts | String | Order book generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` Exception: For the `bbo-tbt` channel, `ts` is the timestamp when the book is generated by matching engine. |
| > checksum | Integer | Checksum, implementation details below |
| > prevSeqId | Integer | Sequence ID of the last sent message. Only applicable to `books`, `books-l2-tbt`, `books50-l2-tbt` |
| > seqId | Integer | Sequence ID of the current message, implementation details below |

An example of the array of asks and bids values: ["411.8", "10", "0", "4"]

- "411.8" is the depth price

- "10" is the quantity at the price (number of contracts for derivatives, quantity in base currency for Spot and Spot Margin)

- "0" is part of a deprecated feature and it is always "0"

- "4" is the number of orders at the price.

If you need to subscribe to many 50 or 400 depth level channels, it is recommended to subscribe through multiple websocket connections, with each of less than 30 channels.

The order book data will be updated around once a second during the call auction.

`books/books5/bbo-tbt/books-l2-tbt/books50-l2-tbt` don't return ELP orders

`books-elp` only return ELP orders, including both valid and invalid parts (invalid parts means ELP buy orders with a price higher than best bid of non-ELP orders; or ELP sell orders with a price lower than best ask of non-ELP orders). Users should distinguish valid and invalid parts using the best bid/ask price of non-ELP orders.

#### Sequence ID

`seqId` is the sequence ID of the market data published. The set of sequence ID received by users is the same if users are connecting to the same channel through multiple websocket connections. Each `instId` has an unique set of sequence ID. Users can use `prevSeqId` and `seqId` to build the message sequencing for incremental order book updates. Generally the value of seqId is larger than prevSeqId. The `prevSeqId` in the new message matches with `seqId` of the previous message. The smallest possible sequence ID value is 0, except in snapshot messages where the prevSeqId is always -1.

Exceptions:

1. If there are no updates to the depth for an extended period(Around 60 seconds), for the channel that always updates snapshot data, OKX will send the latest snapshot, for the channel that has incremental data, OKX will send a message with `'asks': [], 'bids': []` to inform users that the connection is still active. `seqId` is the same as the last sent message and `prevSeqId` equals to `seqId`.
2. The sequence number may be reset due to maintenance, and in this case, users will receive an incremental message with `seqId` smaller than `prevSeqId`. However, subsequent messages will follow the regular sequencing rule.

##### Example

- Snapshot message: prevSeqId = -1, seqId = 10

- Incremental message 1 (normal update): prevSeqId = 10, seqId = 15

- Incremental message 2 (no update): prevSeqId = 15, seqId = 15

- Incremental message 3 (sequence reset): prevSeqId = 15, seqId = 3

- Incremental message 4 (normal update): prevSeqId = 3, seqId = 5

#### Checksum

This mechanism can assist users in checking the accuracy of depth data.

##### Merging incremental data into full data

After subscribing to the incremental load push (such as `books` 400 levels) of Order Book Channel, users first receive the initial full load of market depth. After the incremental load is subsequently received, update the local full load.

- If there is the same price, compare the size. If the size is 0, delete this depth data. If the size changes, replace the original data.

- If there is no same price, sort by price (bid in descending order, ask in ascending order), and insert the depth information into the full load.

##### Calculate Checksum

Use the first 25 bids and asks in the full load to form a string (where a colon connects the price and size in an ask or a bid), and then calculate the CRC32 value (32-bit signed integer).

Calculate Checksum

```
1. More than 25 levels of bid and ask
A full load of market depth (only 2 levels of data are shown here, while 25 levels of data should actually be intercepted):
```

```
{
 "bids": [
 ["3366.1", "7", "0", "3"],
 ["3366", "6", "3", "4"]
 ],
 "asks": [
 ["3366.8", "9", "10", "3"],
 ["3368", "8", "3", "4"]
 ]
}

```

```
Check string:
"3366.1:7:3366.8:9:3366:6:3368:8"

2. Less than 25 levels of bid or ask
A full load of market depth:
```

```
{
 "bids": [
 ["3366.1", "7", "0", "3"]
 ],
 "asks": [
 ["3366.8", "9", "10", "3"],
 ["3368", "8", "3", "4"],
 ["3372", "8", "3", "4"]
 ]
}

```

```
Check string:
"3366.1:7:3366.8:9:3368:8:3372:8"
```

- When the bid and ask depth data exceeds 25 levels, each of them will intercept 25 levels of data, and the string to be checked is queued in a way that the bid and ask depth data are alternately arranged. Such as: `bid[price:size]`:`ask[price:size]`:`bid[price:size]`:`ask[price:size]`...

- When the bid or ask depth data is less than 25 levels, the missing depth data will be ignored.Such as: `bid[price:size]`:`ask[price:size]`:`asks[price:size]`:`asks[price:size]`...

Push Data Example of bbo-tbt channel

```
{
 "arg": {
 "channel": "bbo-tbt",
 "instId": "BCH-USDT-SWAP"
 },
 "data": [
 {
 "asks": [
 [
 "111.06","55154","0","2"
 ]
 ],
 "bids": [
 [
 "111.05","57745","0","2"
 ]
 ],
 "ts": "1670324386802",
 "seqId": 363996337
 }
 ]
}

```

Push Data Example of books5 channel

```
{
 "arg": {
 "channel": "books5",
 "instId": "BCH-USDT-SWAP"
 },
 "data": [
 {
 "asks": [
 ["111.06","55154","0","2"],
 ["111.07","53276","0","2"],
 ["111.08","72435","0","2"],
 ["111.09","70312","0","2"],
 ["111.1","67272","0","2"]],
 "bids": [
 ["111.05","57745","0","2"],
 ["111.04","57109","0","2"],
 ["111.03","69563","0","2"],
 ["111.02","71248","0","2"],
 ["111.01","65090","0","2"]],
 "instId": "BCH-USDT-SWAP",
 "ts": "1670324386802",
 "seqId": 363996337
 }
 ]
}

```

### WS / Option trades channel

Retrieve the recent trades data. Data will be pushed whenever there is a trade. Every update contain only one trade.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "option-trades",
 "instType": "OPTION",
 "instFamily": "BTC-USD"
 }]
}
```

```
import asyncio

from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [{
 "channel": "option-trades",
 "instType": "OPTION",
 "instFamily": "BTC-USD"
 }]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | `subscribe` `unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name`option-trades` |
| > instType | String | Yes | Instrument type, `OPTION` |
| > instId | String | Conditional | Instrument ID, e.g. BTC-USD-221230-4000-C, Either `instId` or `instFamily` is required. If both are passed, `instId` will be used. |
| > instFamily | String | Conditional | Instrument family, e.g. BTC-USD |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "option-trades",
 "instType": "OPTION",
 "instFamily": "BTC-USD"
 },
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"option-trades\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | `subscribe` `unsubscribe` `error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`status` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "option-trades",
 "instType": "OPTION",
 "instFamily": "BTC-USD"
 },
 "data": [
 {
 "fillVol": "0.5066007836914062",
 "fwdPx": "16469.69928595038",
 "idxPx": "16537.2",
 "instFamily": "BTC-USD",
 "instId": "BTC-USD-230224-18000-C",
 "markPx": "0.04690107010619562",
 "optType": "C",
 "px": "0.045",
 "side": "sell",
 "sz": "2",
 "tradeId": "38",
 "ts": "1672286551080"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| data | Array of objects | Subscribed data |
| > instId | String | Instrument ID |
| > instFamily | String | Instrument family |
| > tradeId | String | Trade ID |
| > px | String | Trade price |
| > sz | String | Trade quantity. The unit is contract. |
| > side | String | Trade side `buy` `sell` |
| > optType | String | Option type, C: Call P: Put |
| > fillVol | String | Implied volatility while trading (Correspond to trade price) |
| > fwdPx | String | Forward price while trading |
| > idxPx | String | Index price while trading |
| > markPx | String | Mark price while trading |
| > ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |

The first data you receive after subscribing may be cached from the previous trade, so please ignore it.

### WS / Call auction details channel

Retrieve call auction details.

#### URL Path

/ws/v5/public

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "call-auction-details",
 "instId": "ONDO-USDC"
 }]
}
```

```
import asyncio

from okx.websocket.WsPublicAsync import WsPublicAsync

def callbackFunc(message):
 print(message)

async def main():
 ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/public")
 await ws.start()
 args = [{
 "channel": "call-auction-details",
 "instId": "ONDO-USDC"
 }]

 await ws.subscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

 await ws.unsubscribe(args, callback=callbackFunc)
 await asyncio.sleep(10)

asyncio.run(main())
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe``unsubscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name `call-auction-details` |
| > instId | String | Yes | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "call-auction-details",
 "instId": "ONDO-USDC"
 },
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"call-auction-details\", \"instId\" : \"BTC-USD-191227\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | yes | channel name |
| > instId | String | Yes | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "call-auction-details",
 "instId": "ONDO-USDC"
 },
 "data": [
 {
 "instId": "ONDO-USDC",
 "unmatchedSz": "9988764",
 "eqPx": "0.6",
 "matchedSz": "44978",
 "state": "continuous_trading",
 "auctionEndTime": "1726542000000",
 "ts": "1726542000007"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > instId | String | Instrument ID |
| data | Array of objects | Subscribed data |
| > instId | String | Instrument ID |
| > eqPx | String | Equilibrium price |
| > matchedSz | String | Matched size for both buy and sellThe unit is in base currency |
| > unmatchedSz | String | Unmatched size |
| > auctionEndTime | String | Call auction end time. Unix timestamp in milliseconds. |
| > state | String | Trading state of the symbol`call_auction``continuous_trading` |
| > ts | String | Data generation time. Unix timestamp in millieseconds. |

During call auction, users can get the updates of equilibrium price, matched size, unmatched size, and auction end time. The data will be updated around once a second. When call auction ends, this channel will push the last message, returning the actual open price, matched size, and unmatched size, with trading state as `continuous_trading`.
