## Market Maker Program

High-caliber trading teams are welcomed to work with OKX as market makers in providing a liquid, fair, and orderly platform to all users. OKX market makers could enjoy favourable fees in return for meeting the market making obligations.

Prerequisites (Satisfy any condition):

- VIP 2 or above on fee schedule

- Qualified Market Maker on other exchange

Interested parties can reach out to us at `Institutional@okx.com`

Remarks:

Market making obligations and trading fees will be shared to successful parties only.

OKX reserves the right of final decision and interpretation for the content hereinabove.

In fairness to all users, market makers will be ineligible for other VIP-related and volume-related promotions or rebates.

### POST / Register GLP-C pairs

Register one or more instruments for the GLP-C (Global Liquidity Program — Category C) market maker program. GLP-C assesses market maker order book depth on tail-end trading pairs on an hourly basis. Supports batch registration; each instrument returns an individual result code.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/users/glp/c/register-pairs`

Request Example

```
POST /api/v5/users/glp/c/register-pairs
body
{
 "instIds": ["DOGE-USDT", "SHIB-USDT", "PEPE-USDT-SWAP"]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instIds | Array of strings | Yes | List of instrument IDs to register for GLP-C |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "DOGE-USDT",
 "sCode": "0",
 "sMsg": ""
 },
 {
 "instId": "SHIB-USDT",
 "sCode": "0",
 "sMsg": ""
 },
 {
 "instId": "PEPE-USDT-SWAP",
 "sCode": "0",
 "sMsg": ""
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| sCode | String | Result code for this instrument. `0` means success |
| sMsg | String | Result message for this instrument |

### GET / GLP-C registered pairs

Retrieve the list of instruments that the account has registered for GLP-C.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/c/registered-pairs`

Request Example

```
GET /api/v5/users/glp/c/registered-pairs?instType=SPOT
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type filter`SPOT``SWAP`Returns all if omitted |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "DOGE-USDT",
 "instType": "SPOT",
 "registerTime": "1732300800000"
 },
 {
 "instId": "PEPE-USDT-SWAP",
 "instType": "SWAP",
 "registerTime": "1732300800000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| instType | String | Instrument type`SPOT``SWAP` |
| registerTime | String | Registration time. Unix timestamp in milliseconds |

### GET / GLP-C performance

Retrieve hourly assessment performance data for registered GLP-C pairs.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/c/performance`

Request Example

```
GET /api/v5/users/glp/c/performance?instId=DOGE-USDT&limit=10
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | No | Instrument ID. Returns all registered pairs if omitted |
| instType | String | No | Instrument type filter`SPOT``SWAP` |
| begin | String | No | Start time. Unix timestamp in milliseconds, inclusive |
| end | String | No | End time. Unix timestamp in milliseconds, inclusive |
| after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |

`ts` is not unique across pairs. When `instId` is omitted, several records can share the same `ts`, and `after`/`before` exclude every record at the requested `ts`, so records at a page boundary can be skipped. To paginate without missing records, specify `instId`.

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "DOGE-USDT",
 "instType": "SPOT",
 "ts": "1732363200000",
 "qualified": "true",
 "bidDepth": "50000",
 "askDepth": "48000",
 "reqDepth": "30000"
 },
 {
 "instId": "DOGE-USDT",
 "instType": "SPOT",
 "ts": "1732359600000",
 "qualified": "false",
 "bidDepth": "25000",
 "askDepth": "22000",
 "reqDepth": "30000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| instType | String | Instrument type`SPOT``SWAP` |
| ts | String | Assessment timestamp. Unix timestamp in milliseconds (on the hour) |
| qualified | String | Whether the hourly assessment was met`true``false` |
| bidDepth | String | Bid-side depth in top 3 levels |
| askDepth | String | Ask-side depth in top 3 levels |
| reqDepth | String | Required depth threshold to qualify |

### GET / GLP-C history performance

Retrieve aggregated historical assessment results for registered GLP-C pairs.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/users/glp/c/history/performance`

Request Example

```
GET /api/v5/users/glp/c/history/performance?instId=DOGE-USDT&begin=1732276800000&end=1732363200000
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instId | String | No | Instrument ID |
| instType | String | No | Instrument type filter`SPOT``SWAP` |
| begin | String | No | Filter with a begin timestamp `assessStartTime`. Unix timestamp in milliseconds |
| end | String | No | Filter with an end timestamp `assessStartTime`. Unix timestamp in milliseconds |
| after | String | No | Pagination of data to return records earlier than the requested `assessStartTime`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| before | String | No | Pagination of data to return records newer than the requested `assessStartTime`, Unix timestamp format in milliseconds, e.g. `1597026383085` |
| limit | String | No | Number of results per request. The maximum is `100`. The default is `100`. |

`assessStartTime` is not unique across pairs. When `instId` is omitted, several records can share the same `assessStartTime`, and `after`/`before` exclude every record at the requested `assessStartTime`, so records at a page boundary can be skipped. To reduce the chance of skipped records, specify `instId` when paginating.

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "DOGE-USDT",
 "instType": "SPOT",
 "assessStartTime": "1732276800000",
 "assessEndTime": "1732363200000",
 "qualifiedHours": "20",
 "totalHours": "24",
 "qualifiedRate": "0.8333"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID |
| instType | String | Instrument type`SPOT``SWAP` |
| assessStartTime | String | Assessment period start time. Unix timestamp in milliseconds |
| assessEndTime | String | Assessment period end time. Unix timestamp in milliseconds |
| qualifiedHours | String | Number of qualified hours in the period |
| totalHours | String | Total assessment hours in the period |
| qualifiedRate | String | Qualification rate. Decimal string, e.g. `0.8333` = 83.33% |
