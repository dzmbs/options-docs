## REST API

### Get the invitee's detail

#### Rate limit：20 requests per 2 seconds

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
 "firstTradeTime": "",
 "inviteeLevel": "2",
 "inviteeRebateRate": "0.39",
 "joinTime": "1712546713000",
 "kycTime": "",
 "level": "Lv1",
 "region": "Vietnam",
 "totalCommission": "0",
 "volMonth": "0"
 }
 ]
}

```

#### Response parameters

| Parameter name | Type | Description |
| --- | --- | --- |
| inviteeLevel | String | Invitee's relative level to the affiliateIf the user is a invitee, the level will be `2`. |
| joinTime | String | Timestamp that the rebate relationship is established, Unix timestamp in millisecond format, e.g. `1597026383085` |
| inviteeRebateRate | String | Self rebate rate of the invitee (in decimal), e.g. `0.01` represents `10%` |
| totalCommission | String | Total commission earned from the invitee, unit in `USDT` |
| firstTradeTime | String | Timestamp that the first trade is completed after the latest rebate relationship is established with the parent affiliate Unix timestamp in millisecond format, e.g. 1597026383085If user has not traded, "" will be returned |
| level | String | Invitee trading fee level, e.g. Lv1 |
| depAmt | String | Accumulated amount of deposit in USDTIf user has not deposited, 0 will be returned |
| volMonth | String | Accumulated Trading volume in the current month in USDTIf user has not traded, 0 will be returned |
| accFee | String | Accumulated Amount of trading fee in USDTIf there is no any fee, 0 will be returned |
| kycTime | String | KYC2 verification time. Unix timestamp in millisecond format and the precision is in dayIf user has not passed KYC2, "" will be returned |
| region | String | User country or region. e.g. "United Kingdom" |
| affiliateCode | String | Affiliate invite code that the invitee registered/recalled via |
