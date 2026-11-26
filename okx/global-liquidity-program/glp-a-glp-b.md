## GLP-A / GLP-B

### Get GLP instrument types

Retrieve the GLP-A / GLP-B classification of SPOT and SWAP instruments. Use this endpoint to check which program and pool an instrument is assessed under. Expiry Futures & Nitro Spreads are not classified by pair type; all pairs are assessed together. GLP-C instruments are listed by [Get GLP-C eligible instruments](#global-liquidity-program-glp-c-get-glp-c-eligible-instruments). Classifications and volume weights are for reference only; the OKX website and the program brochure prevail.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/public/mm-instrument-types`

Request Example

```
GET /api/v5/public/mm-instrument-types?instType=SWAP
```

```
import okx.PublicData as PublicData

flag = "0" # Production trading: 0, Demo trading: 1

publicDataAPI = PublicData.PublicAPI(flag=flag)

# Retrieve the list of GLP-A / GLP-B instrument classifications
result = publicDataAPI.get_mm_instrument_types(
 instType="SWAP"
)
print(result)
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type.`SPOT``SWAP`When not specified, returns all types. |
| instId | String | No | Instrument ID, e.g. `BTC-USDT`, `BTC-USDT-SWAP`.When specified, returns at most one record. |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "pairType": "A"
 },
 {
 "instId": "ETH-USDT-SWAP",
 "instType": "SWAP",
 "pairType": "A"
 },
 {
 "instId": "XAU-USDT-SWAP",
 "instType": "SWAP",
 "pairType": "B-TradFi"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. `BTC-USDT-SWAP` |
| instType | String | Instrument type.`SPOT``SWAP` |
| pairType | String | GLP-A / GLP-B classification.`A`: Type A pair. Assessed under GLP-A (unadjusted share)`B-Crypto`: Type B crypto pair. Assessed under GLP-B; volume weight 1×`B-TradFi`: Type B TradFi pair (Spot and Perpetuals). Assessed under GLP-B; volume weight 2×`Type Special`: GLP Special Pair. Assessed under GLP-B; volume weight 4× |

### Get GLP v2 overview

Retrieve active GLP-A / GLP-B enrollments, current tiers, estimated next tiers, tier requirements, and week-to-date performance for the authenticated account. A sub-account API key retrieves the master account's data.

Weekly assessment: upgrades take effect on Tuesday 00:00 (UTC+8) and downgrades on Wednesday 00:00 (UTC+8). `gracePeriodEndTime` is the earliest time a downgrade can take effect.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp/v2/overview`

Request Example

```
GET /api/v5/users/glp/v2/overview
```

#### Request Parameters

No request parameters.

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "programs": [
 {
 "bizId": "16",
 "program": "GLP_B",
 "side": "MAKER",
 "instrument": "PERP",
 "currentTier": "Tier 2",
 "estNextTier": "Tier 2",
 "estNextStatus": "qualify",
 "gracePeriodEndTime": "",
 "requirement": [
 {
 "tier": "Tier 1",
 "share": "0.005"
 },
 {
 "tier": "Tier 2",
 "share": "0.003"
 }
 ],
 "performance": [
 {
 "date": "1726531200000",
 "assessPeriod": "PREVIOUS",
 "share": "0.0035",
 "vol": "140000"
 },
 {
 "date": "1726876800000",
 "assessPeriod": "CURRENT",
 "share": "0.004",
 "vol": "200"
 }
 ]
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| programs | Array of objects | Active GLP enrollments. Empty array when none available. |
| > bizId | String | Product and trading-side identifier.`14`: SPOT MAKER`15`: FUT_NTO MAKER`16`: PERP MAKER`17`: SPOT TAKER`18`: FUT_NTO TAKER`19`: PERP TAKER |
| > program | String | GLP program name.`GLP_A``GLP_B` |
| > side | String | Trading side.`MAKER``TAKER` |
| > instrument | String | GLP product category.`SPOT`: Spot trading`PERP`: Perpetuals`FUT_NTO`: Expiry Futures and Nitro |
| > currentTier | String | GLP tier currently in effect. Empty string when unavailable. |
| > estNextTier | String | Estimated GLP tier based on latest assessment. Empty string when unavailable. |
| > estNextStatus | String | Estimated tier outcome.`disqualify``downgrade``qualify``upgrade`Empty string when unavailable. |
| > gracePeriodEndTime | String | Earliest date on which a downgrade can take effect. Unix timestamp in milliseconds. Empty string when not applicable. |
| > requirement | Array of objects | Market-share thresholds for GLP tiers. |
| >> tier | String | GLP tier name. |
| >> share | String | Required market share as a decimal fraction. GLP-A thresholds are unadjusted share; GLP-B Spot / Perpetual thresholds are adjusted share. `"0.007"` = 0.7%. `null` when unavailable. |
| > performance | Array of objects | Week-to-date performance by trading date. |
| >> date | String | Trading date. Unix timestamp in milliseconds. |
| >> assessPeriod | String | Assessment period containing this trading date.`PREVIOUS``CURRENT` |
| >> share | String | Week-to-date market share as a decimal fraction. `null` when unavailable. |
| >> vol | String | Week-to-date trading volume. `null` when unavailable. |

### Get GLP v2 assessment details

Retrieve daily and week-to-date GLP-A / GLP-B performance for the selected product and trading side within the current assessment week. A sub-account API key retrieves the master account's data.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp/v2/details`

Request Example

```
GET /api/v5/users/glp/v2/details?bizId=16
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| bizId | String | Yes | Product and trading-side identifier.`14`: SPOT MAKER`15`: FUT_NTO MAKER`16`: PERP MAKER`17`: SPOT TAKER`18`: FUT_NTO TAKER`19`: PERP TAKER |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "assessStartTime": "1726790400000",
 "assessEndTime": "1727308800000",
 "performance": [
 {
 "date": "1726790400000",
 "origVol": "100",
 "origShare": "0.004",
 "adjVol": "200",
 "adjShare": "0.004",
 "accOrigVol": "100",
 "accOrigShare": "0.004",
 "accAdjVol": "200",
 "accAdjShare": "0.004"
 },
 {
 "date": "1726876800000",
 "origVol": "200",
 "origShare": "0.004",
 "adjVol": "400",
 "adjShare": "0.004",
 "accOrigVol": "300",
 "accOrigShare": "0.004",
 "accAdjVol": "600",
 "accAdjShare": "0.004"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| assessStartTime | String | Start of the assessment period. Unix timestamp in milliseconds. |
| assessEndTime | String | End of the assessment period. Unix timestamp in milliseconds. |
| performance | Array of objects | Daily and week-to-date performance. Empty array when no data available. |
| > date | String | Trading date. Unix timestamp in milliseconds. |
| > origVol | String | Daily unadjusted trading volume. Used for GLP-A and for Expiry Futures & Nitro. `null` when unavailable. |
| > origShare | String | Daily unadjusted market share as a decimal fraction. Used for GLP-A and for Expiry Futures & Nitro. `null` when unavailable. |
| > adjVol | String | Daily weighted Type B trading volume. Used for GLP-B Spot / Perpetuals. `null` when unavailable. |
| > adjShare | String | Daily adjusted share as a decimal fraction. Used for GLP-B Spot / Perpetuals. Adjusted share = weighted Type B volume ÷ (platform Type B pool volume − GLP-A Tier 1 participants' volume in that pool). `null` when unavailable. |
| > accOrigVol | String | Week-to-date trading volume before weighting. `null` when unavailable. |
| > accOrigShare | String | Week-to-date market share as a decimal fraction. `null` when unavailable. |
| > accAdjVol | String | Adjusted week-to-date trading volume. `null` when unavailable. |
| > accAdjShare | String | Adjusted week-to-date market share as a decimal fraction. `null` when unavailable. |

### Get GLP v2 performance history

Retrieve weekly GLP-A / GLP-B assessment results, tier outcomes and performance for the selected product and trading side. A sub-account API key retrieves the master account's data.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp/v2/history/performance`

Request Example

```
GET /api/v5/users/glp/v2/history/performance?bizId=16
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| bizId | String | Yes | Product and trading-side identifier.`14`: SPOT MAKER`15`: FUT_NTO MAKER`16`: PERP MAKER`17`: SPOT TAKER`18`: FUT_NTO TAKER`19`: PERP TAKER |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "performance": [
 {
 "assessStartTime": "1726185600000",
 "assessEndTime": "1726704000000",
 "tier": "Tier 3",
 "nextTier": "Tier 2",
 "accOrigVol": "100000",
 "accOrigShare": "0.004",
 "accAdjVol": "200000",
 "accAdjShare": "0.004",
 "assessResult": "upgrade"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| performance | Array of objects | Weekly assessment results. Empty array when no history available. |
| > assessStartTime | String | Start of the assessment period. Unix timestamp in milliseconds. |
| > assessEndTime | String | End of the assessment period. Unix timestamp in milliseconds. |
| > tier | String | GLP tier used for this assessment. |
| > nextTier | String | Tier determined by this assessment. Empty string when unavailable. |
| > accOrigVol | String | Trading volume for the assessment period before weighting. `null` when unavailable. |
| > accOrigShare | String | Market share for the assessment period as a decimal fraction. `null` when unavailable. |
| > accAdjVol | String | Adjusted trading volume for the assessment period. `null` when unavailable. |
| > accAdjShare | String | Adjusted market share for the assessment period as a decimal fraction. `null` when unavailable. |
| > assessResult | String | Tier outcome.`disqualify``downgrade``qualify``upgrade`Empty string when unavailable. |
