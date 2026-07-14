## REST API

Block trading is not supported under spot mode.

### Get Counterparties

Retrieves the list of counterparties that the user is permitted to trade with.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/counterparties`

Request Example

```
GET /api/v5/rfq/counterparties
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Get counterparts
result = blockTradingAPI.counterparties()
print(result)
```

#### Request parameters

None

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "traderName" : "Satoshi Nakamoto",
 "traderCode" : "SATOSHI",
 "type" : ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| traderName | String | The long formative username of trader or entity on the platform. |
| traderCode | String | A unique identifier of maker which will be publicly visible on the platform. All RFQ and Quote endpoints will use this as the unique counterparty identifier. |
| type | String | The counterparty type. `LP` refers to API connected auto market makers. |

### Create RFQ

Creates a new RFQ

Please select trading bot "WAGMI" as the counterparty when submitting RFQs in demo trading.

Prices provided on RFQs by the trading bot are for reference only.

To learn more, please visit [Support center > FAQ > Trading > Liquid marketplace > Demo trading](/help/demo-trading)

#### Rate Limit: 5 requests per 2 seconds; 80 requests per 12 hours

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/create-rfq`

Request Example

```
POST /api/v5/rfq/create-rfq

{
 "anonymous": true,
 "counterparties":[
 "Trader1",
 "Trader2"
 ],
 "allowPartialExecution":false,
 "clRfqId":"rfq01",
 "tag":"123456",
 "legs":[
 {
 "sz":"25",
 "side":"buy",
 "posSide": "long",
 "tdMode":"cross",
 "ccy":"USDT",
 "instId":"BTC-USD-221208-100000-C"
 },
 {
 "sz":"150",
 "side":"buy",
 "posSide": "long",
 "tdMode":"cross",
 "ccy":"USDT",
 "instId":"ETH-USDT",
 "tgtCcy":"base_ccy"
 }
 ]
}
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Create RFQ
result = blockTradingAPI.create_rfq(
 anonymous=True,
 counterparties=[
 "Trader1",
 "Trader2"
 ],
 clRfqId= "rfq01",
 legs=[
 {
 "sz":"25",
 "side":"buy",
 "posSide": "long",
 "tdMode":"cross",
 "ccy":"USDT",
 "instId":"BTC-USD-221208-100000-C"
 },
 {
 "sz":"150",
 "side":"buy",
 "posSide": "long",
 "tdMode":"cross",
 "ccy":"USDT",
 "instId":"ETH-USDT",
 "tgtCcy":"base_ccy"
 }
 ]
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| counterparties | Array of strings | Yes | The trader code(s) of the counterparties who receive the RFQ. Can be found via /api/v5/rfq/counterparties/ |
| anonymous | Boolean | No | Submit RFQ on a disclosed or anonymous basis. Valid values are `true` or `false`. If not specified, the default value is `false`. When anonymous = true, the taker’s identify is not disclosed to maker even after trade execution. |
| clRfqId | String | No | Client-supplied RFQ ID. A combination of case-sensitive alpha-numeric, all numbers, or all letters of up to 32 characters. |
| tag | String | No | RFQ tag. The block trade associated with the RFQ will have the same tag. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| allowPartialExecution | Boolean | No | Whether the RFQ can be partially filled provided that the shape of legs stays the same. Valid values are `true` or `false`. `false` by default. |
| legs | Array of objects | Yes | An Array of objects containing each leg of the RFQ. Maximum 15 legs can be placed per request |
| > instId | String | Yes | The Instrument ID of each leg. Example : "BTC-USDT-SWAP" |
| > tdMode | String | No | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| > ccy | String | No | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| > sz | String | Yes | The size of each leg |
| > lmtPx | String | No | Taker expected price for the RFQ If provided, RFQ trade will be automatically executed if the price from the quote is better than or equal to the price specified until the RFQ is canceled or expired. This field has to be provided for all legs to have the RFQ automatically executed, or leave empty for all legs, otherwise request will be rejected. The auto execution side depends on the leg side of the RFQ. For `SPOT/MARGIN/FUTURES/SWAP`, lmtPx will be in unit of the quote ccy. For `OPTION`, lmtPx will be in unit of settle ccy. The field will not be disclosed to counterparties. |
| > side | String | Yes | The direction of each leg. Valid values can be `buy` or `sell`. |
| > posSide | String | No | Position side. The default is `net` in the net mode. It can only be `long` or `short` in the long/short mode. If not specified, users in long/short mode always open new positions. Only applicable to `FUTURES`/`SWAP`. |
| > tgtCcy | String | No | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are `base_ccy` and `quote_ccy`. When not specified, this is equal to `base_ccy` by default. |
| > tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |
| acctAlloc | Array of objects | No | Account level allocation of the RFQ |
| > acct | String | Yes | The name of the allocated account of the RFQ. |
| > legs | Array of objects | Yes | The allocated legs of the account. |
| >> sz | String | Yes | The allocated size of each leg |
| >> instId | String | Yes | The Instrument ID of each leg. Example : "BTC-USDT-SWAP" |
| >> tdMode | String | No | Trade mode |
| >> ccy | String | No | Margin currency |
| >> posSide | String | No | Position side |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "cTime":"1611033737572",
 "uTime":"1611033737572",
 "traderCode":"SATOSHI",
 "tag":"123456",
 "rfqId":"22534",
 "clRfqId":"rfq01",
 "allowPartialExecution":false,
 "state":"active",
 "validUntil":"1611033857557",
 "counterparties":[
 "Trader1",
 "Trader2"
 ],
 "legs":[
 {
 "instId":"BTC-USD-221208-100000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "sz":"25",
 "side":"buy",
 "posSide": "long",
 "tgtCcy":""
 },
 {
 "instId":"ETH-USDT",
 "tdMode":"cross",
 "ccy":"USDT",
 "sz":"150",
 "side":"buy",
 "posSide": "long",
 "tgtCcy":"base_ccy",
 "tradeQuoteCcy": "USDT"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results of the RFQ creation. |
| > cTime | String | The timestamp the RFQ was created. Unix timestamp format in milliseconds. |
| > uTime | String | The timestamp the RFQ was last updated. Unix timestamp format in milliseconds. |
| > state | String | The status of the RFQ. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` `traded_away` `failed`. `filled` indicates the RFQ was successfully executed against the maker's quote. `traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another. Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`. |
| > counterparties | Array of strings | The list of counterparties traderCode the RFQ was broadcast to. |
| > validUntil | String | The timestamp the RFQ expires. Unix timestamp format in milliseconds. If all legs are options, the RFQ will expire after 10 minutes; otherwise, the RFQ will expire after 2 minutes. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string. |
| > tag | String | RFQ tag. The block trade associated with the RFQ will have the same tag. |
| > allowPartialExecution | Boolean | Whether the RFQ can be partially filled provided that the shape of legs stays the same. |
| > traderCode | String | A unique identifier of taker. |
| > rfqId | String | The unique identifier of the RFQ generated by system. |
| > legs | Array of objects | An Array of objects containing each leg of the RFQ. |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> tdMode | String | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| >> ccy | String | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| >> sz | String | Size of the leg in contracts or spot. |
| >> side | String | The direction of the leg. Valid values can be buy or sell. |
| >> posSide | String | Position side. The default is `net` in the net mode. If not specified, return "", which is equivalent to net. It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short). Only applicable to FUTURES/SWAP. |
| >> tgtCcy | String | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default. |
| >> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |
| > groupId | String | Group RFQ IDOnly applicable to group RFQ, return "" for normal RFQ |
| > acctAlloc | Array of objects | Account level allocation of the RFQ |
| >> acct | String | The name of the allocated account of the RFQ |
| >> sCode | String | The code of the event execution result, 0 means success |
| >> sMsg | String | Rejection message if the request is unsuccessful |
| >> legs | Array of objects | The allocated legs of the account |
| >>> instId | String | Instrument ID |
| >>> sz | String | The calculated size of each leg of allocated account |
| >>> tdMode | String | Trade mode |
| >>> ccy | String | Margin currency |
| >>> posSide | String | Position side |

Group RFQ introduction

1. Only a master account can conduct group RFQ and the available scope of allocated subaccounts is its normal and managed subaccounts.

2. Users will pass in acctAlloc request parameter to indicate the details of group RFQ account allocation, account name, instrument ID, allocated size, etc. master account is also allowed and should be indicated as "0". For tdMode, ccy and posSide fields, they will inherit the system default value if you leave them empty.

3. Add groupId, acctAlloc as a new response parameter.

4. The upper limit of the number of allocated subaccounts is 10. You will receive error code 70516 if you exceed the upper limit.

5. For each symbol, the total size of RFQ legs in all accounts should be equal to its combined amount in the group RFQ. If not, you will receive error code 70514.

6. For each sub-account, the ratio of a leg's size to the group RFQ must be the same across all symbols. If not, you will receive error code 70515. Here is an example:

 1. Parent RFQ legs

 1. Symbol: BTC-USDT, size: 50, symbol: ETH-USDT, size: 100

 2. Child RFQ legs, happy case

 1. Acct1: symbol: BTC-USDT, size: 30, symbol: ETH-USDT, size: 60 (ratio: 0.6)

 2. Acct2: symbol: BTC-USDT, size: 20, symbol: ETH-USDT, size: 40 (ratio: 0.4)

 3. Child RFQ legs, bad case

 1. Acct1: symbol: BTC-USDT, size: 30, symbol: ETH-USDT, size: 50

 2. Acct2: symbol: BTC-USDT, size: 20, symbol: ETH-USDT, size: 50

 3. The total size is equal. But the ratio is not equal for different legs per subaccount.

7. For allowPartialExecution field, it will be ignored even though users pass it in. For a group RFQ, allowPartialExecution will always be true, since taker can not determine whether the RFQ can be partially or fully filled if any subaccount fails. Thus, makers should regard it as a RFQ that can be partially filled.

8. Group RFQ will not be created if any subaccount fails.

### Cancel RFQ

Cancel an existing active RFQ that you have created previously.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-rfq`

Request Example

```
POST /api/v5/rfq/cancel-rfq
{
 "rfqId":"22535",
 "clRfqId":"rfq001"
}
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Cancel RFQ
result = blockTradingAPI.cancel_rfq(
 rfqId="22535",
 clRfqId="rfq001"
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| rfqId | String | Conditional | RFQ ID created . |
| clRfqId | String | Conditional | Client-supplied RFQ ID. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. Either rfqId or clRfqId is required. If both are passed, rfqId will be used. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "rfqId":"22535",
 "clRfqId":"rfq001",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > rfqId | String | RFQ ID |
| > clRfqId | String | Client-supplied RFQ ID. |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |

### Cancel multiple RFQs

Cancel one or multiple active RFQ(s) in a single batch. Maximum 100 RFQ orders can be canceled per request.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-batch-rfqs`

Request Example

```
POST /api/v5/rfq/cancel-batch-rfqs
{
 "rfqIds":[
 "2201",
 "2202",
 "2203"
 ],
 "clRfqIds":[
 "r1",
 "r2",
 "r3"
 ]
}
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Cancel multiple RFQs
result = blockTradingAPI.cancel_batch_rfqs(
 rfqIds=[
 "2201",
 "2202",
 "2203"
 ],
 clRfqIds=[
 "r1",
 "r2",
 "r3"
 ],
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| rfqIds | Array of strings | Conditional | RFQ IDs . |
| clRfqIds | Array of strings | Conditional | Client-supplied RFQ IDs. Either `rfqIds` or `clRfqIds` is required. If both attributes are sent, `rfqIds` will be used as primary identifier. |

Success - All requested RFQs canceled

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "rfqId":"2201",
 "clRfqId":"r1",
 "sCode":"0",
 "sMsg":""
 },
 {
 "rfqId":"2202",
 "clRfqId":"r2",
 "sCode":"0",
 "sMsg":""
 },
 {
 "rfqId":"2203",
 "clRfqId":"r3",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

Partial cancellation

```
{
 "code":"2",
 "msg":"Bulk operation partially ",
 "data":[
 {
 "rfqId":"2201",
 "clRfqId":"r1",
 "sCode":"70000",
 "sMsg":"RFQ does not exist."
 },
 {
 "rfqId":"2202",
 "clRfqId":"r2",
 "sCode":"0",
 "sMsg":""
 },
 {
 "rfqId":"2203",
 "clRfqId":"r3",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

Failure example

```
{
 "code":"1",
 "msg":"Operation failed.",
 "data":[
 {
 "rfqId":"2201",
 "clRfqId":"r1",
 "sCode":"70000",
 "sMsg":"RFQ does not exist."
 },
 {
 "rfqId":"2202",
 "clRfqId":"r2",
 "sCode":"70000",
 "sMsg":"RFQ does not exist."
 },
 {
 "rfqId":"2203",
 "clRfqId":"r3",
 "sCode":"70000",
 "sMsg":"RFQ does not exist."
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > rfqId | String | RFQ ID |
| > clRfqId | String | Client-supplied RFQ ID. |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |

### Cancel all RFQs

Cancels all active RFQs.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-all-rfqs`

Request Example

```
POST /api/v5/rfq/cancel-all-rfqs
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Cancel all RFQs
result = blockTradingAPI.cancel_all_rfqs()
print(result)
```

#### Request parameters

None

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "ts":"1697026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > ts | String | The timestamp of successful cancellation. Unix timestamp format in milliseconds, e.g. 1597026383085. |

### Execute Quote

Executes a Quote. It is only used by the creator of the RFQ

#### Rate Limit: 2 requests per 3 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/execute-quote`

Request Example

```
POST /api/v5/rfq/execute-quote
{
 "rfqId":"22540",
 "quoteId":"84073",
 "legs":[
 {
 "sz":"25",
 "instId":"BTC-USD-20220114-13250-C"
 },
 {
 "sz":"25",
 "instId":"BTC-USDT"
 }
 ]
}
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Execute quote
result = blockTradingAPI.execute_quote(
 rfqId="22540",
 quoteId="84073"
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| rfqId | String | Yes | RFQ ID . |
| quoteId | String | Yes | Quote ID. |
| legs | Array of objects | No | An Array of objects containing the execution size of each leg of the RFQ. The ratio of the leg sizes needs to be the same as the RFQ. *Note: `tgtCcy` and `side` of each leg will be same as ones in the RFQ. `px` will be the same as the ones in the Quote. |
| > instId | String | Yes | The Instrument ID, for example: "BTC-USDT-SWAP". |
| > sz | String | Yes | The size of each leg |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "blockTdId":"180184",
 "rfqId":"1419",
 "clRfqId":"r0001",
 "quoteId":"1046",
 "clQuoteId":"q0001",
 "tag":"123456",
 "tTraderCode":"Trader1",
 "mTraderCode":"Trader2",
 "cTime":"1649670009",
 "legs":[
 {
 "px":"0.1",
 "sz":"25",
 "instId":"BTC-USD-20220114-13250-C",
 "side":"sell",
 "fee":"-1.001",
 "feeCcy":"BTC",
 "tradeId":"10211"
 },
 {
 "px":"0.2",
 "sz":"25",
 "instId":"BTC-USDT",
 "side":"buy",
 "fee":"-1.001",
 "feeCcy":"BTC",
 "tradeId":"10212"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > cTime | String | The execution time for the trade. Unix timestamp in milliseconds. |
| > rfqId | String | RFQ ID. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string. |
| > quoteId | String | Quote ID. |
| > clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string. |
| > blockTdId | String | Block trade ID. |
| > tag | String | RFQ tag. |
| > tTraderCode | String | A unique identifier of the taker. Empty if the anonymous parameter of the RFQ is set to be `true`. |
| > mTraderCode | String | A unique identifier of the maker. Empty if the anonymous parameter of the Quote is set to be `true`. |
| > legs | Array of objects | Legs of trade |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> px | String | The price the leg executed |
| >> sz | String | Size of the leg in contracts or spot. |
| >> side | String | The direction of the leg from the Takers perspective. Valid value can be buy or sell. |
| >> fee | String | Fee for the individual leg. Negative fee represents the user transaction fee charged by the platform. Positive fee represents rebate. |
| >> feeCcy | String | Fee currency. To be read in conjunction with fee |
| >> tradeId | String | Last traded ID. |
| > acctAlloc | Array of objects | Account level allocation of the RFQ |
| >> acct | String | The name of the allocated account of the RFQ. |
| >> blockTdId | String | Block trade ID |
| >> sCode | String | The code of the event execution result, 0 means success |
| >> sMsg | String | Rejection message if the request is unsuccessful |
| >> legs | Array of objects | The allocated legs of the account. |
| >>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP" |
| >>> sz | String | The size of each account leg is filled. |
| >>> fee | String | The fee of each account level leg |
| >>> feeCcy | String | Fee currency. To be read in conjunction with fee |
| >>> tradeId | String | Last traded ID of each account leg |

Group RFQ introduction

1. Takers are not allowed to partially execuate the quote for group RFQ. You will receive error code 70507 if you don't pass in the full leg size.

2. Parent RFQ leg size will be the summation of the filled size of each child RFQ leg size while fee should also be the summation.

3. The blockTdId of parent RFQ and the tradeId of parent RFQ legs will be emoty. But there will be subaccount breakdown attached with blockTdId and tradeId populated.

### Get Quote products

Retrieve the products which makers want to quote and receive RFQs for, and the corresponding price and size limit.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/maker-instrument-settings`

Request Example

```
GET /api/v5/rfq/maker-instrument-settings
```

#### Request parameters

None

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instType": "OPTION",
 "includeAll": true,
 "data": [
 {
 "instFamily": "BTC-USD",
 "maxBlockSz": "10000",
 "makerPxBand": "5"
 },
 {
 "instFamily": "SOL-USD",
 "maxBlockSz": "100000",
 "makerPxBand": "15"
 }
 ]
 },
 {
 "instType": "FUTURES",
 "includeAll": false,
 "data": [
 {
 "instFamily": "BTC-USD",
 "maxBlockSz": "10000",
 "makerPxBand": "5"
 },
 {
 "instFamily": "ETH-USDT",
 "maxBlockSz": "100000",
 "makerPxBand": "15"
 }
 ]
 },
 {
 "instType:": "SWAP",
 "includeAll": false,
 "data": [
 {
 "instFamily": "BTC-USD",
 "maxBlockSz": "10000",
 "makerPxBand": "5"
 },
 {
 "instFamily": "ETH-USDT"
 }
 ]
 },
 {
 "instType:": "SPOT",
 "includeAll": false,
 "data": [
 {
 "instId": "BTC-USDT"
 },
 {
 "instId": "TRX-USDT"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not `0`. |
| data | Array of objects | Return data of the request. |
| > instType | String | Type of instrument. Valid value can be `FUTURES`, `OPTION`, `SWAP` or `SPOT`. |
| > includeAll | Boolean | Receive all instruments or not under specific instType setting. Valid value can be boolean (`True`/`False`). By default, the value will be `false`. |
| > data | Array of objects | Elements of the instType. |
| >> instFamily | String | Instrument family. Required for `FUTURES`, `OPTION` and `SWAP` only. |
| >> instId | String | Instrument ID. Required for `SPOT` only. |
| >> maxBlockSz | String | Max trade quantity for the product(s). For `FUTURES`, `OPTION` and `SWAP`, the max quantity of the RFQ/Quote is in unit of contracts. For `SPOT`, this parameter is in base currency. |
| >> makerPxBand | String | Price bands in unit of ticks, measured against mark price. Setting makerPxBand to 1 tick means: If Bid price > Mark + 1 tick, it will be stopped If Ask price < Mark - 1 tick, It will be stopped |

### Set Quote products

Customize the products which makers want to quote and receive RFQs for, and the corresponding price and size limit.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/maker-instrument-settings`

Request Example

```
POST /api/v5/rfq/maker-instrument-settings
body
[
 {
 "instType": "OPTION",
 "data":
 [{
 "instFamily": "BTC-USD",
 "maxBlockSz": "10000",
 "makerPxBand": "5"
 },
 {
 "instFamily": "SOL-USD",
 "maxBlockSz": "100000",
 "makerPxBand": "15"
 }]
 },
 {
 "instType": "FUTURES",
 "data":
 [{
 "instFamily": "BTC-USD",
 "maxBlockSz": "10000",
 "makerPxBand": "5"
 },
 {
 "instFamily": "ETH-USDT",
 "maxBlockSz": "100000",
 "makerPxBand": "15"
 }]
 },
 {
 "instType": "SWAP",
 "data":
 [{
 "instFamily": "BTC-USD",
 "maxBlockSz": "10000",
 "makerPxBand": "5"
 },
 {
 "instFamily": "ETH-USDT"
 }]
 },
 {
 "instType": "SPOT",
 "data":
 [{
 "instId": "BTC-USDT"
 },
 {
 "instId": "TRX-USDT"
 }]
 }
]
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Set quote products
data =[{
 "instType": "OPTION",
 "data": [{
 "uly": "BTC-USD",
 "maxBlockSz": "10000",
 "makerPxBand": "5"
 },
 {
 "uly": "SOL-USD",
 "maxBlockSz": "100000",
 "makerPxBand": "15"
 }
 ]
}]

result = blockTradingAPI.set_marker_instrument(
 data
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Type of instrument. Valid value can be `FUTURES`, `OPTION`, `SWAP` or `SPOT`. |
| includeAll | Boolean | No | Receive all instruments or not under specific instType setting. Valid value can be boolean (`True`/`False`). By default, the value will be `false`. |
| data | Array of objects | Yes | Elements of the instType. |
| > instFamily | String | Conditional | Instrument family. Required for `FUTURES`, `OPTION` and `SWAP` only. |
| > instId | String | Conditional | Instrument ID. Required for `SPOT` only. |
| > maxBlockSz | String | No | Max trade quantity for the product(s). For `FUTURES`, `OPTION` and `SWAP`, the max quantity of the RFQ/Quote is in unit of contracts. For `SPOT`, this parameter is in base currency. |
| > makerPxBand | String | No | Price bands in unit of ticks, measured against mark price. Setting makerPxBand to 1 tick means: If Bid price > Mark + 1 tick, it will be stopped If Ask price < Mark - 1 tick, It will be stopped |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "result":true
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not `0`. |
| data | Array of objects | Array of objects containing the results. |
| > result | Boolean | Result of the requestValid value is `true` or `false`. |

### Reset MMP status

Reset the MMP status to be inactive.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/mmp-reset`

Request Example

```
POST /api/v5/rfq/mmp-reset
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Reset MMP status
result = blockTradingAPI.reset_mmp()
print(result)
```

#### Request parameters

None

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not `0`. |
| data | Array of objects | Array of objects containing the results. |
| > ts | String | The timestamp of re-setting successfully. Unix timestamp format in milliseconds, e.g. `1597026383085`. |

### Set MMP

This endpoint is used to set MMP configure and only applicable to block trading makers

#### Rate Limit: 1 request per 10 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/mmp-config`

Request Example

```
POST /api/v5/rfq/mmp-config
body
{
 "timeInterval":"5000",
 "frozenInterval":"2000",
 "countLimit": "100"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| timeInterval | String | Yes | Time window (ms). MMP interval where monitoring is done."0" means disable MMP. Maximum time interval is 600,000. |
| frozenInterval | String | Yes | Frozen period (ms). "0" means the trade will remain frozen until you request "Reset MMP Status" to unfrozen. |
| countLimit | String | Yes | Limit in number of execution attempts. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "frozenInterval":"2000",
 "countLimit": "100",
 "timeInterval":"5000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| timeInterval | String | Time window (ms). MMP interval where monitoring is done |
| frozenInterval | String | Frozen period (ms). |
| countLimit | String | Limit in number of execution attempts |

Group RFQ introduction

For RFQ makers, the execution attempt of group RFQ will only count once towards MMP regardless of how many account allocations involved.

### Get MMP Config

This endpoint is used to get MMP configure information and only applicable to block trading market makers

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/mmp-config`

Request Example

```
GET /api/v5/rfq/mmp-config
```

#### Request Parameters

none

Response Example

```
{
 "code": "0",
 "data": [
 {
 "frozenInterval": "2000",
 "mmpFrozen": true,
 "mmpFrozenUntil": "1000",
 "countLimit": "10",
 "timeInterval": "5000"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| timeInterval | String | Time window (ms). MMP interval where monitoring is done"0" means MMP is diabled |
| frozenInterval | String | Frozen period (ms). If it is "0", the trade will remain frozen until manually reset and `mmpFrozenUntil` will be "". |
| countLimit | String | Limit in number of execution attempts |
| mmpFrozen | Boolean | Whether MMP is currently triggered. `true` or `false` |
| mmpFrozenUntil | String | If frozenInterval is not "0" and mmpFrozen = True, it is the time interval (in ms) when MMP is no longer triggered, otherwise "" |

### Create Quote

Allows the user to Quote an RFQ that they are a counterparty to. The user MUST quote the entire RFQ and not part of the legs or part of the quantity. Partial quoting is not allowed.

Only one active quote is allowed per RFQ at a time. Submitting a new quote for the same `rfqId` will automatically cancel the existing active quote before the new one is created. Two-sided quoting (providing simultaneous bid and ask for the same RFQ) is not supported — only the most recently submitted quote remains active.

#### Rate Limit: 50 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/create-quote`

Request Example

```
POST /api/v5/rfq/create-quote
{
 "rfqId":"22539",
 "clQuoteId":"q001",
 "tag":"123456",
 "quoteSide":"buy",
 "anonymous": true,
 "expiresIn":"30",
 "legs":[
 {
 "px":"39450.0",
 "sz":"200000",
 "instId":"BTC-USDT-SWAP",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"buy",
 "posSide": "long"
 },
 {
 "px":"39450.0",
 "sz":"200000",
 "instId":"BTC-USDT-SWAP",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"buy",
 "posSide": "long"
 }
 ]
}
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Create quote
result = blockTradingAPI.create_quote(
 rfqId="22539",
 clQuoteId="q001",
 anonymous=True,
 quoteSide="buy",
 expiresIn="30",
 legs=[
 {
 "px": "39450.0",
 "sz": "200000",
 "instId": "BTC-USDT-SWAP",
 "side": "buy"
 }
 ]
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| rfqId | String | Yes | RFQ ID . |
| clQuoteId | String | No | Client-supplied Quote ID. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| tag | String | No | Quote tag. The block trade associated with the Quote will have the same tag. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| anonymous | Boolean | No | Submit Quote on a disclosed or anonymous basis. Valid value is `true` or `false`. `false` by default. |
| quoteSide | String | Yes | The trading direction of the Quote. Its value can be `buy` or `sell`. For example, if quoteSide is `buy`, all the legs are executed in their leg sides; otherwise, all the legs are executed in the opposite of their leg sides. |
| expiresIn | String | No | Seconds that a quote expires in. Must be an integer between 10-120. Default is 60. |
| legs | Array of objects | Yes | The legs of the Quote. |
| > instId | String | Yes | The instrument ID of quoted leg. |
| > tdMode | String | No | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| > ccy | String | No | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| > sz | String | Yes | Size of the leg in contracts or spot. |
| > px | String | Yes | The price of the leg. |
| > side | String | Yes | The direction of the leg. Valid values can be buy or sell. |
| > posSide | String | No | Position side. The default is `net` in the net mode. It can only be `long` or `short` in the long/short mode. If not specified, users in long/short mode always open new positions. Only applicable to `FUTURES`/`SWAP`. |
| > tgtCcy | String | No | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default. |
| > tradeQuoteCcy | String | No | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |

Response Example

```
{
 "code":"",
 "msg":"",
 "data":[
 {
 "validUntil":"1608997227834",
 "uTime":"1608267227834",
 "cTime":"1608267227834",
 "legs":[
 {
 "px":"46000",
 "sz":"25",
 "instId":"BTC-USD-220114-25000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"sell",
 "posSide": "long",
 "tgtCcy":""
 },
 {
 "px":"4000",
 "sz":"25",
 "instId":"ETH-USD-220114-25000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"buy",
 "posSide": "long",
 "tgtCcy":""
 }
 ],
 "quoteId":"25092",
 "rfqId":"18753",
 "tag":"123456",
 "quoteSide":"sell",
 "state":"active",
 "reason": "mmp_canceled",
 "clQuoteId":"",
 "clRfqId":"",
 "traderCode":"Aksha"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > cTime | String | The timestamp the Quote was created, Unix timestamp format in milliseconds. |
| > uTime | String | The timestamp the Quote was last updated, Unix timestamp format in milliseconds. |
| > state | String | The status of the quote. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` or `failed`. |
| > reason | String | Reasons of state. Valid values can be `mmp_canceled`. |
| > validUntil | String | The timestamp the Quote expires. Unix timestamp format in milliseconds. |
| > rfqId | String | RFQ ID |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string. |
| > quoteId | String | Quote ID. |
| > clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string. |
| > tag | String | Quote tag. The block trade associated with the Quote will have the same tag. |
| > traderCode | String | A unique identifier of maker. |
| > quoteSide | String | The trading direction of the Quote. Its value can be `buy` or `sell`. For example, if quoteSide is `buy`, all the legs are executed in their leg sides; otherwise, all the legs are executed in the opposite of their leg sides. |
| > legs | Array of objects | The legs of the Quote. |
| >> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| >> tdMode | String | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| >> ccy | String | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| >> sz | String | Size of the leg in contracts or spot. |
| >> px | String | The price of the leg. |
| >> side | String | The direction of the leg. Valid values can be buy or sell. |
| >> posSide | String | Position side. The default is `net` in the net mode. If not specified, return "", which is equivalent to net. It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short). Only applicable to FUTURES/SWAP. |
| >> tgtCcy | String | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are `base_ccy` and `quote_ccy`. When not specified this is equal to `base_ccy` by default. |
| >> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |

### Cancel Quote

Cancels an existing active Quote you have created in response to an RFQ.

If a new `create-quote` for the same `rfqId` is processed before this cancel request arrives, the original quote will already be in `canceled` state and this request will return error `70400`. This can occur when requests are sent from different connections or processes, which do not guarantee ordering. To ensure strict create→cancel sequencing, wait for the create-quote response before issuing the cancel, using a single connection.

#### Rate Limit: 50 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-quote`

Request Example

```
POST /api/v5/rfq/cancel-quote
{
 "quoteId": "007",
 "clQuoteId":"Bond007"
}
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Cancel quote
result = blockTradingAPI.cancel_quote(
 quoteId="007",
 clQuoteId="Bond007"
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| quoteId | String | Conditional | Quote ID. |
| clQuoteId | String | Conditional | Client-supplied Quote ID. Either `quoteId` or `clQuoteId` is required. If both `clQuoteId` and `quoteId` are passed, `quoteId` will be treated as primary identifier. |
| rfqId | String | No | RFQ ID. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "quoteId":"007",
 "clQuoteId":"Bond007",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > quoteId | String | Quote ID |
| > clQuoteId | String | Client-supplied Quote ID. |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |

### Cancel multiple Quotes

Cancel one or multiple active Quote(s) in a single batch. Maximum 100 quote orders can be canceled per request.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-batch-quotes`

Request Example

```
POST /api/v5/rfq/cancel-batch-quotes
{
 "quoteIds": ["1150","1151","1152"],
 "clQuoteIds": ["q1","q2","q3"]
}
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Cancel multiple quotes
result = blockTradingAPI.cancel_batch_quotes(
 quoteIds=["1150","1151","1152"],
 clQuoteIds=["q1","q2","q3"]
)
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| quoteIds | Array of strings | Conditional | Quote IDs . |
| clQuoteIds | Array of strings | Conditional | Client-supplied Quote IDs. Either `quoteIds` or `clQuoteIds` is required.If both attributes are sent, `quoteIds` will be used as primary identifier. |

Success - All requested Quotes canceled

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "quoteId":"1150",
 "clQuoteId":"q1",
 "sCode":"0",
 "sMsg":""
 },
 {
 "quoteId":"1151",
 "clQuoteId":"q2",
 "sCode":"0",
 "sMsg":""
 },
 {
 "quoteId":"1152",
 "clQuoteId":"q3",
 "sCode":"0",
 "sMsg":""
 }
 ]
}

```

Partial cancellation

```
{
 "code":"2",
 "msg":"Bulk operation partially succeeded.",
 "data":[
 {
 "quoteId":"1150",
 "clQuoteId":"q1",
 "sCode":"0",
 "sMsg":""
 },
 {
 "quoteId":"1151",
 "clQuoteId":"q2",
 "sCode":"70001",
 "sMsg":"Quote does not exist."
 },
 {
 "quoteId":"1152",
 "clQuoteId":"q3",
 "sCode":"70001",
 "sMsg":"Quote does not exist."
 }
 ]
}

```

Failure example

```
{
 "code":"1",
 "msg":"Operation failed.",
 "data":[
 {
 "quoteId":"1150",
 "clQuoteId":"q1",
 "sCode":"70001",
 "sMsg":"Quote does not exist."
 },
 {
 "quoteId":"1151",
 "clQuoteId":"q2",
 "sCode":"70001",
 "sMsg":"Quote does not exist."
 },
 {
 "quoteId":"1151",
 "clQuoteId":"q3",
 "sCode":"70001",
 "sMsg":"Quote does not exist."
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > quoteId | String | Quote ID |
| > clQuoteId | String | Client-supplied Quote ID. |
| > sCode | String | The code of the event execution result, `0` means success. |
| > sMsg | String | Rejection message if the request is unsuccessful. |

### Cancel all Quotes

Cancels all active Quotes.

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-all-quotes`

Request Example

```
POST /api/v5/rfq/cancel-all-quotes
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading:0 , demo trading:1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Cancel all quotes
result = blockTradingAPI.cancel_all_quotes()
print(result)
```

#### Request parameters

None

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "ts":"1697026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results |
| > ts | String | The timestamp of cancellation successfully. Unix timestamp format in milliseconds, e.g. 1597026383085. |

### Cancel All After

Cancel all quotes after the countdown timeout.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/rfq/cancel-all-after`

Request Example

```
POST /api/v5/rfq/cancel-all-after
body
{
 "timeOut":"60"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| timeOut | String | Yes | The countdown for quotes cancellation, with second as the unit.Range of value can be 0, [10, 120]. Setting timeOut to 0 disables Cancel All After. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "triggerTime":"1587971460",
 "ts":"1587971400"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| triggerTime | String | The time the cancellation is triggered.triggerTime=0 means Cancel All After is disabled. |
| ts | String | The time the request is received. |

Users are recommended to send a request to the exchange every second. When the cancel all after is triggered, the trading engine will cancel quotes on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies.

### Get rfqs

Retrieves details of RFQs that the user is a counterparty to (either as the creator or the receiver of the RFQ).

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/rfqs`

Request Example

```
GET /api/v5/rfq/rfqs
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Retrieves details of RFQs that the user is a counterparty to
result = blockTradingAPI.get_rfqs()
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| rfqId | String | No | RFQ ID . |
| clRfqId | String | No | Client-supplied RFQ ID. If both `clRfqId` and `rfqId` are passed, `rfqId` will be treated as primary identifier |
| state | String | No | The status of the RFQ. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` `failed` `traded_away`. `filled` indicates the RFQ was successfully executed against the maker's quote. `traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another. Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`. |
| beginId | String | No | Start rfq id the request to begin with. Pagination of data to return records newer than the requested rfqId, not including beginId |
| endId | String | No | End rfq id the request to end with. Pagination of data to return records earlier than the requested rfqId, not including endId |
| limit | String | No | Number of results per request. The maximum is 100 which is also the default value. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "rfqId": "123456",
 "clRfqId": "",
 "tag": "123456",
 "traderCode": "VITALIK",
 "validUntil": "1650969031817",
 "allowPartialExecution": false,
 "state": "filled",
 "flowType": "",
 "counterparties": [
 "SATOSHI"
 ],
 "legs": [
 {
 "instId": "BTC-USDT",
 "tdMode": "cross",
 "ccy": "USDT",
 "side": "buy",
 "posSide": "long",
 "sz": "25",
 "tgtCcy": "base_ccy",
 "tradeQuoteCcy": "USDT"
 }
 ],
 "cTime": "1650968131817",
 "uTime": "1650968164944"
 },
 {
 "rfqId": "1234567",
 "clRfqId": "",
 "tag": "1234567",
 "traderCode": "VITALIK",
 "validUntil": "1650967623729",
 "state": "filled",
 "flowType": "",
 "counterparties": [
 "SATOSHI"
 ],
 "legs": [
 {
 "instId": "BTC-USDT",
 "tdMode": "cross",
 "ccy": "USDT",
 "side": "buy",
 "posSide": "long",
 "sz": "1500000",
 "tgtCcy": "quote_ccy",
 "tradeQuoteCcy": "USDT"
 }
 ],
 "cTime": "1650966723729",
 "uTime": "1650966816577"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results of the RFQ creation. |
| > cTime | String | The timestamp the RFQ was created. Unix timestamp format in milliseconds. |
| > uTime | String | The timestamp the RFQ was last updated. Unix timestamp format in milliseconds. |
| > state | String | The status of the RFQ. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` `failed` `traded_away`. `filled` indicates the RFQ was successfully executed against the maker's quote. `traded_away` only applies to Maker. The same RFQ can appear as `filled` to one maker and `traded_away` to another. Example: taker creates RFQ → makerA quotes pxA, makerB quotes pxB → pxA is better than pxB → taker executes quoteA → makerA sees `filled`, makerB sees `traded_away`. |
| > counterparties | Array of strings | The list of counterparties traderCode the RFQ was broadcasted to. |
| > validUntil | String | The timestamp the RFQ expires. Unix timestamp format in milliseconds. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string. |
| > tag | String | RFQ tag. The block trade associated with the RFQ will have the same tag. |
| > flowType | String | Identify the type of the RFQ. Only applicable to Makers, return "" for Takers |
| > traderCode | String | A unique identifier of taker. Empty if the anonymous parameter of the RFQ is set to be `true`. |
| > rfqId | String | RFQ ID. |
| > allowPartialExecution | Boolean | Whether the RFQ can be partially filled provided that the shape of legs stays the same. Valid value is `true` or `false`. `false` by default. |
| > legs | Array of objects | Legs of RFQ |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> tdMode | String | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| >> ccy | String | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| >> sz | String | Size of the leg in contracts or spot. |
| >> side | String | The direction of the leg. Valid values can be buy or sell. |
| >> posSide | String | Position side. The default is `net` in the net mode. If not specified, return "", which is equivalent to net. It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short). Only applicable to `FUTURES`/`SWAP`. |
| >> tgtCcy | String | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are base_ccy and quote_ccy. When not specified this is equal to base_ccy by default. |
| >> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |
| > groupId | String | Group RFQ ID Only applicable to group RFQ, return "" for normal RFQ |
| > acctAlloc | Array of objects | Account level allocation of the RFQ This is only applicable to the taker. |
| >> acct | String | The name of the allocated account of the RFQ. |
| >> legs | Array of objects | The allocated legs of the account. |
| >>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP" |
| >>> sz | String | The allocated size of each leg. |
| >>> tdMode | String | Trade mode |
| >>> ccy | String | Margin currency |
| >>> posSide | String | Position side |

Group RFQ introduction

1. allowPartialExecution field is always true for group RFQ for taker and maker.

2. Add a new response parameter acctAlloc with all account allocation the same as the initial request, but it is only applicable to takers.

3. Add a new response parameter groupId, applicable to both takers and makers.

4. For group RFQ state,

 1. if any allocated account is pending execution, then pending_fill

 2. otherwise,

 1. if any allocated account is filled, then filled

 2. if all allocated accounts are failed, then failed

### Get quotes

Retrieve all Quotes that the user is a counterparty to (either as the creator or the receiver).

#### Rate Limit: 2 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/quotes`

Request Example

```
GET /api/v5/rfq/quotes
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Retrieve all Quotes that the user is a counterparty to
result = blockTradingAPI.get_quotes()
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| rfqId | String | No | RFQ ID . |
| clRfqId | String | No | Client-supplied RFQ ID. If both `clRfqId` and `rfqId` are passed, `rfqId` will be be treated as primary identifier. |
| quoteId | String | No | Quote ID |
| clQuoteId | String | No | Client-supplied Quote ID. If both clQuoteId and quoteId are passed, quoteId will be treated as primary identifier |
| state | String | No | The status of the quote. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` or `failed`. |
| beginId | String | No | Start quote id the request to begin with. Pagination of data to return records newer than the requested quoteId, not including beginId |
| endId | String | No | End quote id the request to end with. Pagination of data to return records earlier than the requested quoteId, not including endId |
| limit | String | No | Number of results per request. The maximum is 100 which is also the default value. |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "validUntil":"1608997227834",
 "uTime":"1608267227834",
 "cTime":"1608267227834",
 "legs":[
 {
 "px":"46000",
 "sz":"25",
 "instId":"BTC-USD-220114-25000-C",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"sell",
 "posSide": "long",
 "tgtCcy":""
 },
 {
 "px":"45000",
 "sz":"25",
 "instId":"BTC-USDT",
 "tdMode":"cross",
 "ccy":"USDT",
 "side":"buy",
 "posSide": "long",
 "tgtCcy":"base_ccy",
 "tradeQuoteCcy": "USDT"
 }
 ],
 "quoteId":"25092",
 "rfqId":"18753",
 "quoteSide":"sell",
 "state":"canceled",
 "reason":"mmp_canceled",
 "clQuoteId":"cq001",
 "clRfqId":"cr001",
 "tag":"123456",
 "traderCode":"Trader1"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results of the Quote creation. |
| > cTime | String | The timestamp the Quote was created, Unix timestamp format in milliseconds. |
| > uTime | String | The timestamp the Quote was last updated, Unix timestamp format in milliseconds. |
| > state | String | The status of the quote. Valid values can be `active` `canceled` `pending_fill` `filled` `expired` or `failed`. |
| > reason | String | Reasons of state. Valid values can be `mmp_canceled`. |
| > validUntil | String | The timestamp the Quote expires. Unix timestamp format in milliseconds. |
| > rfqId | String | RFQ ID. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string. |
| > quoteId | String | Quote ID. |
| > clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string. |
| > tag | String | Quote tag. The block trade associated with the Quote will have the same tag. |
| > traderCode | String | A unique identifier of maker. Empty If the anonymous parameter of the Quote is set to be `true`. |
| > quoteSide | String | Top level direction of Quote. Its value can be buy or sell. |
| > legs | Array of objects | The legs of the Quote. |
| >> instId | String | The instrument ID of the quoted leg. |
| >> tdMode | String | Trade mode Margin mode: `cross` `isolated` Non-Margin mode: `cash`. If not provided, tdMode will inherit default values set by the system shown below: Futures mode & SPOT: `cash` Buy options in Futures mode and Multi-currency Margin: `isolated` Other cases: `cross` |
| >> ccy | String | Margin currency. Only applicable to `cross` `MARGIN` orders in `Futures mode`. The parameter will be ignored in other scenarios. |
| >> sz | String | Size of the leg in contracts or spot. |
| >> px | String | The price of the leg. |
| >> side | String | The direction of the leg. Valid values can be buy or sell. |
| >> posSide | String | Position side. The default is `net` in the net mode. If not specified, return "", which is equivalent to net. It can only be `long` or `short` in the long/short mode. If not specified, return "", which corresponds to the direction that opens new positions for the trade (buy => long, sell => short). Only applicable to `FUTURES`/`SWAP`. |
| >> tgtCcy | String | Defines the unit of the “sz” attribute. Only applicable to instType = SPOT. The valid enumerations are base_ccy and quote_ccy. When not specified this is equal to base_ccy by default. |
| >> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |

### Get trades

Retrieves the executed trades that the user is a counterparty to (either as the creator or the receiver).

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/rfq/trades`

Request Example

```
GET /api/v5/rfq/trades
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Retrieves the executed trades that the user is a counterparty to
result = blockTradingAPI.get_trades()
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| rfqId | String | No | RFQ ID . |
| clRfqId | String | No | Client-supplied RFQ ID. If both `clRfqId` and `rfqId` are passed, `rfqId` will be treated as primary identifier |
| quoteId | String | No | Quote ID |
| blockTdId | String | No | Block trade ID |
| clQuoteId | String | No | Client-supplied Quote ID. If both `clQuoteId` and `quoteId` are passed, `quoteId` will be treated as primary identifier |
| beginId | String | No | The starting rfq id the request to begin with. Pagination of data to return records newer than the requested blockTdId, not including beginId. |
| endId | String | No | The last rfq id the request to end withPagination of data to return records earlier than the requested blockTdId, not including endId. |
| beginTs | String | No | Filter trade execution time with a begin timestamp (UTC timezone). Unix timestamp format in milliseconds, e.g. 1597026383085 |
| endTs | String | No | Filter trade execution time with an end timestamp (UTC timezone). Unix timestamp format in milliseconds, e.g. 1597026383085 |
| limit | String | No | Number of results per request. The maximum is 100 which is also the default value. If the number of trades in the requested range is bigger than 100, the latest 100 trades in the range will be returned. |
| isSuccessful | Boolean | No | Whether the trade is filled successfully.`true`: the default value. `false`. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "rfqId": "123456",
 "clRfqId": "",
 "quoteId": "0T5342O",
 "clQuoteId": "",
 "blockTdId": "439127542058958848",
 "tag": "123456",
 "isSuccessful": true,
 "errorCode": "",
 "legs": [
 {
 "instId": "BTC-USDT",
 "side": "sell",
 "sz": "0.666",
 "px": "100",
 "tradeId": "439127542058958850",
 "fee": "-0.0333",
 "feeCcy": "USDT",
 "tradeQuoteCcy": "USDT"
 }
 ],
 "cTime": "1650968164900",
 "tTraderCode": "SATS",
 "mTraderCode": "MIKE"
 },
 {
 "rfqId": "1234567",
 "clRfqId": "",
 "quoteId": "0T533T0",
 "clQuoteId": "",
 "blockTdId": "439121886014849024",
 "tag": "123456",
 "isSuccessful": true,
 "errorCode": "",
 "legs": [
 {
 "instId": "BTC-USDT",
 "side": "sell",
 "sz": "0.532",
 "px": "100",
 "tradeId": "439121886014849026",
 "fee": "-0.0266",
 "feeCcy": "USDT",
 "tradeQuoteCcy": "USDT"
 }
 ],
 "cTime": "1650966816550",
 "tTraderCode": "SATS",
 "mTraderCode": "MIKE"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results of the block trade. |
| > cTime | String | The time the trade was executed. Unix timestamp in milliseconds. |
| > rfqId | String | RFQ ID. |
| > clRfqId | String | Client-supplied RFQ ID. This attribute is treated as client sensitive information. It will not be exposed to the Maker, only return empty string. |
| > quoteId | String | Quote ID. |
| > clQuoteId | String | Client-supplied Quote ID. This attribute is treated as client sensitive information. It will not be exposed to the Taker, only return empty string. |
| > blockTdId | String | Block trade ID. |
| > tag | String | Trade tag. The block trade will have the tag of the RFQ or Quote it corresponds to. |
| > tTraderCode | String | A unique identifier of the Taker. Empty if the anonymous parameter of the RFQ is set to be `true`. |
| > mTraderCode | String | A unique identifier of the Maker. Empty if the anonymous parameter of the Quote is set to be `true`. |
| > isSuccessful | Boolean | Whether the trade is filled successfully |
| > errorCode | String | Error code for unsuccessful trades. It is "" for successful trade. |
| > legs | Array of objects | Legs of trade |
| >> instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| >> px | String | The price the leg executed |
| >> sz | String | Size of the leg in contracts or spot. |
| >> side | String | The direction of the leg. Valid value can be buy or sell. |
| >> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive number represents rebate. |
| >> feeCcy | String | Fee currency |
| >> tradeId | String | Last traded ID. |
| >> tradeQuoteCcy | String | The quote currency used for trading. Only applicable to SPOT. The default value is the quote currency of the instId, for example: for `BTC-USD`, the default is `USD`. |
| > acctAlloc | Array of objects | Applicable to both taker, maker |
| >> blockTdId | String | Block trade ID |
| >> errorCode | String | Error code for unsuccessful trades. It is "0" for successful trade. |
| >> acct | String | The name of the allocated account of the RFQ Only applicable to taker, return "" to makers |
| >> legs | Array of objects | The allocated legs of the account. |
| >>> instId | String | The Instrument ID of each leg. Example : "BTC-USDT-SWAP" |
| >>> sz | String | Filled size |
| >>> tradeId | String | Trade ID |
| >>> fee | String | Fee |
| >>> feeCcy | String | Fee currency |

Group RFQ introduction

1. This endpoint is at parent RFQ level and contains account allocation. For parent RFQ, we should return the actual executed size, i.e. failed execution size should not be included in the parent RFQ level.

2. For account allocation, we should include both filled and failed child RFQ but add an errorCode to indicate whether a child RFQ is filled.

3. Trade results will only be returned to group RFQ creator. Allocated subaccounts and MSAs will not see trade results. Allocated accounts are expected to get these trades through trading bills.

4. Trades data will only be returned after all child RFQs are execuated.

5. For parent RFQ isSuccessful field,

 1. it will return true if any child RFQs are filled

 2. otherwise, if all child RFQ fails, it will return false

6. Parent RFQ blockTdId or legs tradeId will be empty. However, account allocation breakdown will be offered and blockTdId/tradeId will be attached.

### Get block tickers

Retrieve the latest block trading volume in the last 24 hours.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/block-tickers`

Request Example

```
GET /api/v5/market/block-tickers?instType=SWAP
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the latest block trading volume in the last 24 hours
result = marketDataAPI.get_block_tickers(
 instType="SPOT"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`SPOT``SWAP``FUTURES``OPTION` |
| instFamily | String | No | Instrument family, e.g. `BTC-USD`Applicable to `FUTURES`/`SWAP`/`OPTION` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "instType":"SWAP",
 "instId":"LTC-USD-SWAP",
 "volCcy24h":"2222",
 "vol24h":"2222",
 "ts":"1597026383085"
 },
 {
 "instType":"SWAP",
 "instId":"BTC-USD-SWAP",
 "volCcy24h":"2222",
 "vol24h":"2222",
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| instType | String | Instrument type |
| volCcy24h | String | 24h trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| vol24h | String | 24h trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get block ticker

Retrieve the latest block trading volume in the last 24 hours.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/block-ticker`

Request Example

```
GET /api/v5/market/block-ticker?instId=LTC-USD-SWAP
```

```
import okx.MarketData as MarketData

flag = "0" # Production trading:0 , demo trading:1

marketDataAPI = MarketData.MarketAPI(flag=flag)

# Retrieve the latest block trading volume in the last 24 hours
result = marketDataAPI.get_block_ticker(
 instId="BTC-USDT"
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
 "instId":"LTC-USD-SWAP",
 "volCcy24h":"2222",
 "vol24h":"2222",
 "ts":"1597026383085"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| instType | String | Instrument type |
| volCcy24h | String | 24h trading volume, with a unit of `currency`. If it is a `derivatives` contract, the value is the number of base currency. If it is `SPOT`/`MARGIN`, the value is the quantity in quote currency. |
| vol24h | String | 24h trading volume, with a unit of `contract`. If it is a `derivatives` contract, the value is the number of contracts. If it is `SPOT`/`MARGIN`, the value is the quantity in base currency. |
| ts | String | Block ticker data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085` |

### Get public multi-leg transactions of block trades

Retrieves the executed block trades. The data will be updated 15 minutes after the block trade execution.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/rfq/public-trades`

Request Example

```
GET /api/v5/rfq/public-trades
```

```
import okx.BlockTrading as BlockTrading

# API initialization
apikey = "YOUR_API_KEY"
secretkey = "YOUR_SECRET_KEY"
passphrase = "YOUR_PASSPHRASE"

flag = "1" # Production trading: 0, Demo trading: 1

blockTradingAPI = BlockTrading.BlockTradingAPI(apikey, secretkey, passphrase, False, flag)

# Retrieves the executed block trades
result = blockTradingAPI.get_public_trades()
print(result)
```

#### Request parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| beginId | String | No | The starting blockTdId the request to begin with. Pagination of data to return records newer than the requested `blockTdId`, not including beginId. |
| endId | String | No | The last blockTdId the request to end with. Pagination of data to return records earlier than the requested `blockTdId`, not including endId. |
| limit | String | No | Number of results per request. The maximum is 100 which is also the default value. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "blockTdId": "439161457415012352",
 "groupId": "",
 "legs": [
 {
 "instId": "BTC-USD-210826",
 "side": "sell",
 "sz": "100",
 "px": "11000",
 "tradeId": "439161457415012354"
 },
 {
 "instId": "BTC-USD-SWAP",
 "side": "sell",
 "sz": "100",
 "px": "50",
 "tradeId": "439161457415012355"
 },
 {
 "instId": "BTC-USDT",
 "side": "buy",
 "sz": "0.1", //for public feed, spot "sz" is in baseccy
 "px": "10.1",
 "tradeId": "439161457415012356"
 },
 {
 "instId": "BTC-USD-210326-60000-C",
 "side": "buy",
 "sz": "200",
 "px": "0.008",
 "tradeId": "439161457415012357"
 },
 {
 "instId": "BTC-USD-220930-5000-P",
 "side": "sell",
 "sz": "200",
 "px": "0.008",
 "tradeId": "439161457415012360"
 },
 {
 "instId": "BTC-USD-220930-10000-C",
 "side": "sell",
 "sz": "200",
 "px": "0.008",
 "tradeId": "439161457415012361"
 },
 {
 "instId": "BTC-USD-220930-10000-P",
 "side": "sell",
 "sz": "200",
 "px": "0.008",
 "tradeId": "439161457415012362"
 },
 {
 "instId": "ETH-USD-220624-100100-C",
 "side": "sell",
 "sz": "100",
 "px": "0.008",
 "tradeId": "439161457415012363"
 }
 ],
 "strategy":"CALL_CALENDAR_SPREAD",
 "cTime": "1650976251241"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| code | String | The result code, `0` means success. |
| msg | String | The error message, not empty if the code is not 0. |
| data | Array of objects | Array of objects containing the results of the public block trade. |
| > strategy | String | Option strategy, e.g. CALL_CALENDAR_SPREAD |
| > cTime | String | The time the trade was executed. Unix timestamp in milliseconds. |
| > blockTdId | String | Block trade ID. |
| > groupId | String | Group RFQ ID Only applicable to group RFQ, return "" for normal RFQ |
| > legs | Array of objects | Legs of trade |
| >> instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| >> px | String | The price the leg executed |
| >> sz | String | Trade quantity For spot trading, the unit is base currencyFor `FUTURES`/`SWAP`/`OPTION`, the unit is contract. |
| >> side | String | The direction of the leg from the Takers perspective. Valid value can be buy or sell. |
| >> tradeId | String | Last traded ID. |

Group RFQ introduction

1. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.

2. Data return by this endpoint should be at **parent RFQ level** regardless of the subaccounts allocation. blockTdId and tradeId will be empty.

### Get public single-leg transactions of block trades

Retrieve the recent block trading transactions of an instrument. Descending order by tradeId. The data will be updated 15 minutes after the block trade execution.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/block-trades`

Request Example

```
GET /api/v5/public/block-trades?instId=BTC-USDT
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |

Response Example

```
{
 "code":"0",
 "msg":"",
 "data":[
 {
 "fillVol": "5",
 "fwdPx": "26857.86591585",
 "groupId": "",
 "idxPx": "26889.7",
 "instId": "BTC-USD-231013-22000-P",
 "markPx": "0.0000000000000001",
 "px": "0.0026",
 "side": "buy",
 "sz": "1",
 "tradeId": "632960608383700997",
 "ts": "1697181568974"
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
| side | String | Trade side `buy` `sell` |
| fillVol | String | Implied volatility Only applicable to `OPTION` |
| fwdPx | String | Forward price Only applicable to `OPTION` |
| idxPx | String | Index price Applicable to `FUTURES`, `SWAP`, `OPTION` |
| markPx | String | Mark price Applicable to `FUTURES`, `SWAP`, `OPTION` |
| groupId | String | Group RFQ ID Only applicable to group RFQ, return "" for normal RFQ |
| ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`. |

Up to 500 most recent historical public transaction data can be retrieved.

Group RFQ introduction

1. Add new response parameter groupId, facilitating clients to map subaccount execution to group RFQ. Only applicable to group RFQ, return "" for normal RFQ.

2. Data return by this endpoint should be at **child RFQ execution level** but split into a single leg. tradeId will be populated.
