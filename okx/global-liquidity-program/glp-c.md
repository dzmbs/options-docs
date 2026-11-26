## GLP-C

### GLP-C API

GLP-C (Global Liquidity Program - C) APIs let eligible market makers discover and enroll instruments, and query their quote assessment results.

| Category | Endpoint |
| --- | --- |
| Enrollment | Get eligible instruments · Enroll instruments · Get enrollment statistics |
| Quote assessment | Get minute assessment · Get hourly instrument assessment · Get hourly assessment summary |

**Program rules**

Instruments are grouped into G1 / G2 / G3 with required bilateral weighted quoting share of 5% / 10% / 15%. Top 3 price levels are weighted 2 / 1 / 0.5. An instrument qualifies for an hour when it qualifies in at least 70% of minutes. Spot and Perpetuals are assessed separately. The tier is based directly on the number of qualified instruments, without a multiplier: Tier 1 ≥ 40 → VIP 9 Maker; Tier 2 30–39 → VIP 8; Tier 3 20–29 → VIP 7; Tier 4 10–19 → VIP 6. Taker fees follow the organic VIP tier.

During the public beta (24 Nov – 1 Dec 2026), the hourly uptime requirement is 50%, and `requiredUptime` / `requiredHourlyUptime` return `"0.5"`. From 1 Dec 2026, the requirement is 70% (`"0.7"`).

**General notes**

- In requests, use `PERP` for perpetuals (including X-Perp). The hourly assessment summary returns `SWAP` for the same category.

- Only accounts whitelisted for GLP-C can call these endpoints. Results are returned for the participant of the authenticated account. No user ID parameter is accepted.

- An instrument is identified by `instType` + `instId`. The same `instId` can exist under different `instType`.

- Timestamps use Unix timestamp format in milliseconds (UTC), e.g. `1795154400000`. Query ranges are inclusive. Assessment data is available for the last 72 hours.

- Quote assessment endpoints return all values as strings. Unavailable values are returned as `""`. Empty results are returned as `[]`.

#### Assessment reason codes

| Reason code | Description |
| --- | --- |
| QUALIFIED | The minute meets the qualification requirements |
| BELOW_THRESHOLD | Share is below the threshold |
| NO_CUSTOMER_QUOTE | No quotes from the account in this minute |
| MARKET_DENOMINATOR_ZERO | No market quotes in this minute |
| SOURCE_DATA_MISSING | Market snapshot is missing |
| SOURCE_DATA_INVALID | Market snapshot is unusable |

### Get GLP-C eligible instruments

Retrieve GLP-C instruments eligible for the current account, with registration counts and qualification requirements.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/instruments`

Request Example

```
GET /api/v5/users/glp-c/instruments?instType=SPOT&page=1&pageSize=10&filterType=1
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`SPOT`: Spot`PERP`: Perpetual |
| page | Integer | Yes | Page number, starting from `1` |
| pageSize | Integer | Yes | Number of results per page. The maximum is `100` |
| filterType | Integer | Yes | `1`: All eligible instruments`2`: Registered`3`: Open for registration |
| instId | String | No | Instrument ID, e.g. `BTC-USDT` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": {
 "page": 1,
 "pageSize": 10,
 "total": 1,
 "startIndex": 0,
 "hasNextPage": false,
 "rows": [
 {
 "instType": "SPOT",
 "instId": "BTC-USDT",
 "instGroup": "G1",
 "registeredClientCount": 0,
 "dailyAvgPlatTv7d": "0",
 "b3PriceLevel": "5",
 "b3PriceQuoteSize": "25",
 "requiredMarketShare": "0.05",
 "requiredUptime": "0.7"
 }
 ]
 }
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| page | Integer | Current page number |
| pageSize | Integer | Number of results per page |
| total | Integer | Total number of results before pagination |
| startIndex | Integer | Zero-based offset of the current page: (page − 1) × pageSize |
| hasNextPage | Boolean | Whether there is a next page |
| rows | Array of objects | Instrument list. `[]` if there are no results |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| > instGroup | String | Instrument group`G1``G2``G3` |
| > registeredClientCount | Integer | Number of clients registered for the instrument |
| > dailyAvgPlatTv7d | String | 7-day daily average platform trading volume |
| > b3PriceLevel | String | Average spread between the third-best ask and bid over the past 7 days, calculated as (ask₃ − bid₃) ÷ their midpoint × 10,000, in bp. Lower values indicate a tighter order book. |
| > b3PriceQuoteSize | String | Average combined bid and ask quote size across order book levels 1–3 over the past 7 days, in USD. For example, `25` means 25 USD. |
| > requiredMarketShare | String | Required minute market share. e.g. `0.05` means 5%. |
| > requiredUptime | String | Required hourly uptime. e.g. `0.7` means 70% |

Only instruments tradable by the current account are returned.

### POST / Enroll GLP-C instruments

Enroll one or more instruments in GLP-C. Enrollment applies to the whole participant and is assessed from the current minute.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/users/glp-c/enroll-instruments`

Request Example

```
POST /api/v5/users/glp-c/enroll-instruments
body
{
 "instsToEnroll": [
 {"instType": "SPOT", "instId": "BTC-USDT"},
 {"instType": "PERP", "instId": "BTC-USDT"}
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instsToEnroll | Array of objects | Yes | Instruments to enroll |
| > instType | String | Yes | Instrument type`SPOT``PERP` |
| > instId | String | Yes | Instrument ID, e.g. `BTC-USDT` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": {
 "enrolledInsts": [
 {"instType": "SPOT", "instId": "BTC-USDT"}
 ],
 "failedInsts": [
 {"instType": "PERP", "instId": "BTC-USDT"}
 ]
 }
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| enrolledInsts | Array of objects | Instruments enrolled successfully |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |
| failedInsts | Array of objects | Instruments that failed to enroll, because they are invalid or not eligible for the account |
| > instType | String | Instrument type |
| > instId | String | Instrument ID |

Enrolling an instrument that is already enrolled returns it in `enrolledInsts`. Withdrawal is not supported in this phase.

### Get GLP-C enrollment statistics

Retrieve the total, registered and open-for-registration instrument counts.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/enroll/stats`

Request Example

```
GET /api/v5/users/glp-c/enroll/stats?instType=SPOT
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | Yes | Instrument type`SPOT``PERP` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": {
 "totalInstCount": 500,
 "registeredInstCount": 40,
 "availableInstCount": 460
 }
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| totalInstCount | Integer | Total number of instruments |
| registeredInstCount | Integer | Number of registered instruments |
| availableInstCount | Integer | Number of instruments open for registration |

`availableInstCount` is not necessarily equal to `totalInstCount` − `registeredInstCount`.

### Get GLP-C minute assessment

Retrieve minute-level assessment results of one instrument, including the share against the threshold and quote sizes by price level.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/quote-assessment/minute`

Request Example

```
GET /api/v5/users/glp-c/quote-assessment/minute?instType=PERP&instIdCode=10459&beginTs=1795154460000&endTs=1795154519999
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``PERP` (including X-Perp) |
| instId | String | Conditional | Instrument ID, e.g. `BTC-USDT-SWAP`. Either `instId` or `instIdCode` is required |
| instIdCode | String | Conditional | Instrument ID code, e.g. `10459`. If both are passed, `instIdCode` is used |
| beginTs | Integer | Yes | Start time, Unix timestamp in milliseconds. Within the last 72 hours |
| endTs | Integer | Yes | End time, Unix timestamp in milliseconds. Not later than the request time |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instIdCode": "10459",
 "instType": "PERP",
 "instId": "BTC-USDT-SWAP",
 "minuteTs": "1795154460000",
 "bilateralWeightedShare": "0.0600000000",
 "threshold": "0.05",
 "minuteStatus": "QUALIFIED",
 "reasonCode": "QUALIFIED",
 "participantBidOriginalQuoteSizeUsd": "2300",
 "participantAskOriginalQuoteSizeUsd": "2300",
 "participantBidWeightedQuoteSizeUsd": "3050",
 "participantAskWeightedQuoteSizeUsd": "3250",
 "levels": [
 {"level": "1", "multiplier": "2", "bidQuoteSizeUsd": "1000", "askQuoteSizeUsd": "1200", "bidMultipliedSizeUsd": "2000", "askMultipliedSizeUsd": "2400"},
 {"level": "2", "multiplier": "1", "bidQuoteSizeUsd": "800", "askQuoteSizeUsd": "600", "bidMultipliedSizeUsd": "800", "askMultipliedSizeUsd": "600"},
 {"level": "3", "multiplier": "0.5", "bidQuoteSizeUsd": "500", "askQuoteSizeUsd": "500", "bidMultipliedSizeUsd": "250", "askMultipliedSizeUsd": "250"}
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instIdCode | String | Instrument ID code |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| minuteTs | String | Start of the minute, Unix timestamp in milliseconds |
| bilateralWeightedShare | String | Bilateral weighted share, 10 decimal places. e.g. `0.0600000000` means 6% |
| threshold | String | Share threshold for this minute |
| minuteStatus | String | `QUALIFIED``NOT_QUALIFIED` |
| reasonCode | String | Assessment reason. See Assessment reason codes in GLP-C API |
| participantBidOriginalQuoteSizeUsd | String | Total bid quote size, in USD |
| participantAskOriginalQuoteSizeUsd | String | Total ask quote size, in USD |
| participantBidWeightedQuoteSizeUsd | String | Total weighted bid quote size, in USD |
| participantAskWeightedQuoteSizeUsd | String | Total weighted ask quote size, in USD |
| levels | Array of objects | Details by price level. `[]` if there are no details |
| > level | String | Price level, starting from `1` |
| > multiplier | String | Weight of the price level |
| > bidQuoteSizeUsd | String | Bid quote size, in USD |
| > askQuoteSizeUsd | String | Ask quote size, in USD |
| > bidMultipliedSizeUsd | String | bidQuoteSizeUsd × multiplier, in USD |
| > askMultipliedSizeUsd | String | askQuoteSizeUsd × multiplier, in USD |

Results are sorted by `minuteTs` in ascending order. Minutes without results are not filled in.

### Get GLP-C hourly instrument assessment

Retrieve hourly qualification results of one instrument for ended hours.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/quote-assessment/hour/instrument`

Request Example

```
GET /api/v5/users/glp-c/quote-assessment/hour/instrument?instType=PERP&instIdCode=10459&beginTs=1795154400000&endTs=1795157999999
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``PERP` (including X-Perp) |
| instId | String | Conditional | Instrument ID, e.g. `BTC-USDT-SWAP`. Either `instId` or `instIdCode` is required |
| instIdCode | String | Conditional | Instrument ID code, e.g. `10459`. If both are passed, `instIdCode` is used |
| beginTs | Integer | Yes | Start time, Unix timestamp in milliseconds. Within the last 72 hours |
| endTs | Integer | Yes | End time, Unix timestamp in milliseconds. Not later than the request time |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "instIdCode": "10459",
 "instType": "PERP",
 "instId": "BTC-USDT-SWAP",
 "assessmentHour": "1795154400000",
 "instGroup": "G1",
 "threshold": "0.05",
 "requiredHourlyUptime": "0.7",
 "qualifiedMinutes": "1",
 "notQualifiedMinutes": "1",
 "hourlyUptime": "0.0166666667",
 "hourStatus": "DELAYED",
 "intendedEffectiveHour": "1795158000000",
 "finalizedAt": "",
 "minuteStatusDetail": [
 {"minuteTs": "1795154400000", "minuteStatus": "NOT_QUALIFIED", "reasonCode": "BELOW_THRESHOLD"},
 {"minuteTs": "1795154460000", "minuteStatus": "QUALIFIED", "reasonCode": "QUALIFIED"}
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instIdCode | String | Instrument ID code |
| instType | String | Instrument type |
| instId | String | Instrument ID |
| assessmentHour | String | Start of the assessment hour, Unix timestamp in milliseconds |
| instGroup | String | Instrument group for this hour |
| threshold | String | Minute share threshold for this hour |
| requiredHourlyUptime | String | Required hourly uptime. e.g. `0.7` means 70% |
| qualifiedMinutes | String | Number of qualified minutes |
| notQualifiedMinutes | String | Number of not-qualified minutes |
| hourlyUptime | String | qualifiedMinutes ÷ 60, 10 decimal places |
| hourStatus | String | `QUALIFIED``NOT_QUALIFIED``DELAYED`: the hour has ended but is not finalized |
| intendedEffectiveHour | String | Hour in which the result is intended to take effect, Unix timestamp in milliseconds |
| finalizedAt | String | Finalization time, Unix timestamp in milliseconds. `""` if `DELAYED` |
| minuteStatusDetail | Array of objects | Result of each minute |
| > minuteTs | String | Start of the minute, Unix timestamp in milliseconds |
| > minuteStatus | String | `QUALIFIED``NOT_QUALIFIED` |
| > reasonCode | String | Assessment reason |

An hour is qualified when `qualifiedMinutes` ≥ ceil(`requiredHourlyUptime` × 60). For example, 70% requires at least 42 qualified minutes. The current hour is not returned.

### Get GLP-C hourly assessment summary

Retrieve hourly qualified instrument counts and the calculated GLP-C tier.

#### Rate Limit: 5 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/users/glp-c/quote-assessment/hour/summary`

Request Example

```
GET /api/v5/users/glp-c/quote-assessment/hour/summary?instType=PERP&beginTs=1795150800000&endTs=1795158000000
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``PERP` (including X-Perp)If not passed, both are returned |
| beginTs | Integer | Yes | Start time, Unix timestamp in milliseconds. Within the last 72 hours |
| endTs | Integer | Yes | End time, Unix timestamp in milliseconds. Not later than the request time. The current hour can be included |

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "assessmentHour": "1795150800000",
 "instType": "SWAP",
 "state": "finalized",
 "registeredInstCount": "47",
 "qualifiedInstCount": "23",
 "qualifiedInstRatio": "0.4893617021",
 "tier": "3",
 "intendedEffectiveHour": "1795154400000"
 },
 {
 "assessmentHour": "1795158000000",
 "instType": "SWAP",
 "state": "in_progress",
 "registeredInstCount": "47",
 "qualifiedInstCount": "0",
 "qualifiedInstRatio": "0.0000000000",
 "tier": "",
 "intendedEffectiveHour": "1795161600000"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| assessmentHour | String | Start of the assessment hour, Unix timestamp in milliseconds |
| instType | String | Instrument type`SPOT``SWAP` (including X-Perp) |
| state | String | `in_progress`: current hour, provisional`finalized``delayed`: ended but not finalized |
| registeredInstCount | String | Number of registered instruments assessed in this hour |
| qualifiedInstCount | String | Number of qualified instruments |
| qualifiedInstRatio | String | qualifiedInstCount ÷ registeredInstCount, 10 decimal places |
| tier | String | Calculated GLP-C tier, based directly on the number of qualified instruments in the hour. `1`: ≥ 40 (VIP 9 Maker); `2`: 30–39 (VIP 8); `3`: 20–29 (VIP 7); `4`: 10–19 (VIP 6). `""` if fewer than 10 or unknown. For the current hour, this is the estimated tier for the next hour. |
| intendedEffectiveHour | String | Hour in which the result is intended to take effect, Unix timestamp in milliseconds |

Results are sorted by `assessmentHour` in ascending order, with `SPOT` before `SWAP` in the same hour. `tier` and `intendedEffectiveHour` do not confirm the fee tier actually applied.
