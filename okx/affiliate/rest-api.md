## REST API

### Get performance summary

Aggregated affiliate performance metrics for a specified time period.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/performance/summary`

Request Example

```
GET /api/v5/affiliate/performance/summary?periodType=total
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| periodType | String | No | Stats window for all summary fields except `uTime`.`last_7d``last_30d``this_month``last_month``total``today``this_week``custom`: pass `begin` and `end` to define a custom window.The default is `total`. |
| begin | String | Conditional | Custom stats-window start, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `end`. Inclusive. |
| end | String | Conditional | Custom stats-window end, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `begin`. Inclusive. |

When `periodType=custom`, supply both `begin` and `end`. Supplying only one returns `50014`.

For all other `periodType` values, server-defined windows are used and any `begin` / `end` passed alongside are ignored.

`periodType` / `begin` / `end` filter the statistics window for all summary fields (`inviteeCnt`, `depAmt`, `details.*`). `uTime` always reflects the latest data snapshot regardless of the window.

Response Example

```
{
 "code": "0",
 "msg": "",
 "data": [
 {
 "uTime": "1777541513000",
 "inviteeCnt": "102",
 "depAmt": "1756.287846940199989393",
 "details": [
 {
 "commissionCategory": "SPOT",
 "firstTraderCnt": "17",
 "traderCnt": "17",
 "vol": "21548.6417826825604",
 "commission": "3.322319946747010328"
 },
 {
 "commissionCategory": "DERIVATIVE",
 "firstTraderCnt": "9",
 "traderCnt": "9",
 "vol": "94531.94802",
 "commission": "3.25142568535855"
 },
 {
 "commissionCategory": "BSC",
 "firstTraderCnt": "0",
 "traderCnt": "0",
 "vol": "0",
 "commission": "0"
 }
 ]
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| uTime | String | Last data update timestamp, Unix timestamp in millisecond format. |
| inviteeCnt | String | Total number of invitees. |
| depAmt | String | Total deposit amount, unit in `USDT`. |
| details | Array of objects | One entry per instrument bucket. |
| > commissionCategory | String | Commission calculation category.`SPOT``DERIVATIVE``BSC` |
| > firstTraderCnt | String | Count of invitees whose lifetime-first trade occurred within the selected window, scoped to this `commissionCategory`. Each invitee can contribute at most once in their lifetime. |
| > traderCnt | String | Number of invitees who traded in this `commissionCategory` bucket within the selected window. Period-scoped. |
| > vol | String | Trading volume in this `commissionCategory` bucket within the selected window, unit in `USDT`. Period-scoped — distinct from `totalVol` on `/invitee/list` and `/sub-affiliate/list` which is lifetime cumulative. |
| > commission | String | Commission earned in this `commissionCategory` bucket within the selected window, unit in `USDT`. Period-scoped — distinct from `totalCommission` on other endpoints which is lifetime cumulative. |

### Get the invitee's detail

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/affiliate/invitee/detail`

Request sample

```
GET /api/v5/affiliate/invitee/detail?uid=11111111
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| uid | String | Yes | UID of the invitee. Only applicable to the UID of invitee master account. The data returned covers invitee master account and invitee sub-accounts. |

Returned results

```
{
 "msg": "",
 "code": "0",
 "data": [
 {
 "accFee": "0",
 "affiliateCode": "HIIIIII",
 "depAmt": "0",
 "wdAmt": "0",
 "firstTradeTime": "",
 "inviteeLevel": "2",
 "inviteeRebateRate": "0.39",
 "joinTime": "1712546713000",
 "kycTime": "",
 "level": "Lv1",
 "region": "Vietnam",
 "totalCommission": "0",
 "volMonth": "0",
 "totalVol": "0"
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| inviteeLevel | String | Invitee's relative level to the affiliateIf the user is a invitee, the level will be `2`. |
| joinTime | String | Timestamp that the rebate relationship is established, Unix timestamp in millisecond format, e.g. `1597026383085` |
| inviteeRebateRate | String | Self rebate rate of the invitee (in decimal), e.g. `0.01` represents `1%` |
| totalCommission | String | Total commission earned from the invitee, unit in `USDT` |
| firstTradeTime | String | Timestamp that the first trade is completed after the latest rebate relationship is established with the parent affiliate Unix timestamp in millisecond format, e.g. 1597026383085If user has not traded, "" will be returned |
| level | String | Invitee trading fee level, e.g. Lv1 |
| depAmt | String | Accumulated amount of deposit in USDTIf user has not deposited, 0 will be returned |
| wdAmt | String | Accumulated amount of withdrawal in USDTIf user has not withdrawn, 0 will be returned |
| volMonth | String | Accumulated Trading volume in the current month in USDTIf user has not traded, 0 will be returned |
| totalVol | String | Lifetime accumulated trading volume in USDTIf user has not traded, 0 will be returned |
| accFee | String | Accumulated Amount of trading fee in USDTIf there is no any fee, 0 will be returned |
| kycTime | String | KYC2 verification time. Unix timestamp in millisecond format and the precision is in dayIf user has not passed KYC2, "" will be returned |
| region | String | User country or region. e.g. "United Kingdom" |
| affiliateCode | String | Affiliate invite code that the invitee registered/recalled via |

### Get invitee list

Paginated invitee list with trading stats and KYC info.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/invitee/list`

Request Example

```
GET /api/v5/affiliate/invitee/list?page=1&kycStatus=verified
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`. |
| limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`. |
| periodType | String | No | Stats window.`last_7d``last_30d``this_month``last_month``total``today``this_week``custom`: pass `begin` and `end` to define a custom window. |
| begin | String | Conditional | Custom stats-window start, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `end`. Inclusive. |
| end | String | Conditional | Custom stats-window end, Unix timestamp in millisecond format. Required when `periodType=custom`, together with `begin`. Inclusive. |
| keyword | String | No | Search by UID or channel name. |
| commissionCategory | String | No | Commission calculation category.`SPOT``DERIVATIVE``BSC` |
| orderBy | String | No | Sort field.`cTime``depAmt``vol``fee``rebate`The default is `cTime`. |
| orderDir | String | No | Sort direction.`asc``desc`The default is `desc`. |
| kycStatus | String | No | KYC status.`unverified``verified` (passed at least KYC2) |
| subAffiliateUid | String | No | Filter invitees under a specific sub-affiliate (external UID). |

When `periodType=custom`, supply both `begin` and `end`. Supplying only one returns `50014`.

For all other `periodType` values, server-defined windows are used and any `begin` / `end` passed alongside are ignored. The window between `begin` and `end` must not exceed 90 days. `begin` cannot be earlier than 180 days from now.

Response Example

```
{
 "code": "0",
 "msg": "",
 "totalPage": "5",
 "data": [
 {
 "uid": "835449167911924693",
 "country": "CN",
 "joinTime": "1777448564000",
 "firstTradeTime": "",
 "channelName": "X2UWA2T89",
 "rebateRate": "0.1600",
 "feeTierRank": "0",
 "kycStatus": "verified",
 "kycTime": "1777448563000",
 "depAmt": "0.0000000000",
 "totalVol": "0.0000000000",
 "totalFee": "0.0000000000",
 "totalCommission": "0.0000000000",
 "isCompliant": true
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response. |
| uid | String | External user UID. |
| country | String | ISO 3166-1 alpha-2 country code of the invitee's residence, e.g. `KR`, `CN`. Empty string when residence is not set. |
| joinTime | String | Relationship established timestamp, Unix timestamp in millisecond format. |
| firstTradeTime | String | First trade timestamp, Unix timestamp in millisecond format. `""` if never traded. |
| channelName | String | Affiliate channel name used at registration. |
| rebateRate | String | Invitee's effective rebate rate from the active rebate calculation rule (in decimal), e.g. `0.1000` represents `10%`. |
| feeTierRank | String | Cross-category fee tier ranking integer (`0` = lowest, `13` = highest). Does not distinguish regular vs VIP — for the categorized label use `level` on Get the invitee's detail. |
| kycStatus | String | KYC status.`unverified``verified` |
| kycTime | String | KYC2 verification timestamp, Unix timestamp in millisecond format. `""` if user has not passed KYC2. |
| depAmt | String | Total deposit amount, unit in `USDT`. |
| totalVol | String | Total trading volume, unit in `USDT`. |
| totalFee | String | Total trading fees, unit in `USDT`. |
| totalCommission | String | Total commission earned from this invitee, unit in `USDT`. |
| isCompliant | Boolean | Whether the invitee is permitted under regional compliance rules.`true`: unrestricted`false`: restricted due to KYC entity or jurisdiction (e.g. sanctioned region) |

### Get link list

Paginated affiliate invite links with commission rates and stats.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/link/list`

Request Example

```
GET /api/v5/affiliate/link/list
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`. |
| limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`. |
| linkType | String | No | Link kind filter.`standard`: regular affiliate invite link`co_inviter`: co-inviter shared link |
| linkStatus | String | No | Link status.`normal``abnormal` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "totalPage": "1",
 "data": [
 {
 "channelId": "78295211",
 "channelName": "78295211",
 "joinLink": "https://okx.com/join/78295211",
 "linkType": "standard",
 "inviterCommissionRate": "0.2900",
 "coInviterCommissionRate": "",
 "inviteeDiscountRate": "0.0100",
 "inviteeCnt": "1",
 "traderCnt": "1",
 "totalCommission": "2.656307",
 "commission24h": "0.5",
 "cTime": "1773739123000",
 "isDefault": true,
 "linkStatus": "normal"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response. |
| channelId | String | Unique channel/link ID. |
| channelName | String | User-defined link name. |
| joinLink | String | Shareable invitation URL. |
| linkType | String | Link kind.`standard`: regular affiliate invite link`co_inviter`: co-inviter shared link |
| inviterCommissionRate | String | Parent inviter's commission rate (the link owner's), in decimal. |
| coInviterCommissionRate | String | Co-inviter's commission rate (in decimal). Empty string for standard links. |
| inviteeDiscountRate | String | Invitee rebate rate template configured on this affiliate link (in decimal), applied to invitees registering via this link. |
| inviteeCnt | String | Number of invitees from this link. |
| traderCnt | String | Number of invitees who traded. |
| totalCommission | String | Cumulative commission, unit in `USDT`. |
| commission24h | String | Commission earned in the rolling past 24 hours, unit in `USDT`. Independent of `periodType` / `begin` / `end` filters. |
| cTime | String | Link creation timestamp, Unix timestamp in millisecond format. |
| isDefault | Boolean | Whether this is the default link. |
| linkStatus | String | Link status.`normal``abnormal` |

### Get co-inviter link list

Co-inviter links where the authenticated user is the co-inviter.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/co-inviter/list`

Request Example

```
GET /api/v5/affiliate/co-inviter/list
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`. |
| limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`. |
| linkStatus | String | No | Link status.`normal``abnormal` |

Response Example

```
{
 "code": "0",
 "msg": "",
 "totalPage": "1",
 "data": [
 {
 "channelId": "31075853",
 "channelName": "MXCUS",
 "joinLink": "https://okx.com/join/MXCUS",
 "inviterCommissionRate": "0.0000",
 "coInviterCommissionRate": "0.1400",
 "inviteeDiscountRate": "0.1600",
 "parUserName": "12****23",
 "coUserName": "***",
 "isCompliant": true,
 "isDefault": false,
 "totalCommission": "0.032111",
 "commission24h": "0",
 "inviteeCnt": "1",
 "traderCnt": "1",
 "clickCnt": "1",
 "totalFee": "0",
 "cTime": "1773739123000",
 "channelAssessmentStatus": "valid",
 "inviterChannelStatus": "valid",
 "coInviterChannelStatus": "valid",
 "linkStatus": "normal"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response. |
| channelId | String | Channel ID. |
| channelName | String | Channel name. |
| joinLink | String | Shareable invitation URL. |
| inviterCommissionRate | String | Parent inviter's commission rate, in decimal. |
| coInviterCommissionRate | String | Co-inviter's commission rate, in decimal (the caller's, since the caller is the co-inviter on this endpoint). |
| inviteeDiscountRate | String | Invitee rebate rate template configured on this affiliate link (in decimal), applied to invitees registering via this link. |
| parUserName | String | Partner affiliate's username string (partially masked, not a UID). |
| coUserName | String | Co-inviter's username placeholder, always fully masked as `***` (PII fully hidden, not a UID). |
| isCompliant | Boolean | Whether the co-inviter is permitted under regional compliance rules.`true`: unrestricted`false`: restricted due to KYC entity or jurisdiction |
| note | String | Optional channel note set by the affiliate (free-form text, may be empty `""`). |
| isDefault | Boolean | Whether this is the default co-inviter link. |
| totalCommission | String | Total commission, unit in `USDT`. |
| commission24h | String | Commission earned in the rolling past 24 hours, unit in `USDT`. Independent of `periodType` / `begin` / `end` filters. |
| inviteeCnt | String | Number of invitees. |
| traderCnt | String | Number of invitees who placed at least one trade. |
| clickCnt | String | Number of times the affiliate link was clicked (click count). |
| totalFee | String | Total service fees, unit in `USDT`. |
| cTime | String | Link creation timestamp, Unix timestamp in millisecond format. |
| channelAssessmentStatus | String | Channel assessment result (trade + invite metrics).`valid`: all assessment metrics met`not_reach_trade`: trade metric unmet`not_reach_invite`: invite metric unmet`not_reach_both`: both unmet |
| inviterChannelStatus | String | Parent inviter's channel compliance.`valid`: parent inviter is compliant`identity_invalid`: parent inviter's identity has been revoked`level_downgraded`: parent inviter's level has been reduced to 0 |
| coInviterChannelStatus | String | Co-inviter's channel compliance (compound: identity × assessment).`valid``identity_invalid``not_reach_assessment``identity_invalid_and_not_reach_assessment` |
| linkStatus | String | Link status.`normal``abnormal` |

### Get sub-affiliate list

Paginated sub-affiliates under current user.

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/affiliate/sub-affiliate/list`

Request Example

```
GET /api/v5/affiliate/sub-affiliate/list
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| page | String | No | 1-indexed page number. Non-numeric values fall back to `1`. The default is `1`. |
| limit | String | No | Items per page. Clamped to `[1, 100]`. The default is `100`. |
| keyword | String | No | Search by sub-affiliate UID. |
| commissionCategory | String | No | Commission calculation category.`SPOT``DERIVATIVE``BSC` |
| orderBy | String | No | Sort field.`cTime``depAmt``vol``fee``rebate`The default sorts by `joinTime` (most recently joined first). |
| orderDir | String | No | Sort direction.`asc``desc`The default is `desc`. |

The endpoint reports lifetime data.

Sort is stable: ties on `orderBy` are broken by `subAffiliateUid` ascending. Safe to paginate large result sets without losing or duplicating rows.

Response Example

```
{
 "code": "0",
 "msg": "",
 "totalPage": "1",
 "data": [
 {
 "subAffiliateUid": "668418489887292061",
 "country": "CN",
 "joinTime": "1773739123000",
 "subAffiliateLevel": "2",
 "commissionRate": "0.3000",
 "isCompliant": true,
 "inviteeCnt": "8",
 "traderCnt": "3",
 "depAmt": "37.281133",
 "totalVol": "3618.561430",
 "totalFee": "1.628353",
 "totalCommission": "0.289847"
 }
 ]
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| totalPage | String | Total number of pages under the current filters and `limit`. Same level as `data` in the response. |
| subAffiliateUid | String | External UID of the sub-affiliate. |
| country | String | ISO 3166-1 alpha-2 country code of the sub-affiliate's residence, e.g. `CN`. Empty string when residence is not set. |
| joinTime | String | Timestamp the user was registered as a sub-affiliate, Unix timestamp in millisecond format. |
| subAffiliateLevel | String | Depth of this sub-affiliate relative to the caller.`2`: direct sub-affiliate (caller's L1 child)`3`: indirect sub-affiliate, 1 level below a direct sub-affiliate |
| commissionRate | String | Sub-affiliate's commission rate, in decimal. |
| isCompliant | Boolean | Whether the sub-affiliate is permitted under regional compliance rules.`true`: unrestricted`false`: restricted due to KYC entity or jurisdiction (e.g. sanctioned region) |
| inviteeCnt | String | Direct invitees of the sub-affiliate. |
| traderCnt | String | Sub-affiliate's invitees who traded. |
| depAmt | String | Total deposit from invitees, unit in `USDT`. |
| totalVol | String | Total trading volume from invitees, unit in `USDT`. |
| totalFee | String | Total trading fees from invitees, unit in `USDT`. |
| totalCommission | String | Your commission earned from this sub-affiliate's invitees, unit in `USDT`. |
