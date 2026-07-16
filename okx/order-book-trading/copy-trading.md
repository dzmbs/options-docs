## Copy Trading

Lead trading API Workflow as follows:**1. Apply to become a leading trader.**

- The procedure can refer to [How to become a lead trader](https://www.okx.com/help/11639154398221);**You can know whether you are a lead trader by checking whether `roleType` or `spotRoleType` from [Get account configuration](/docs-v5/en/#trading-account-rest-api-get-account-configuration) is 1.

2. Leading instruments:**

[GET / Leading instruments](/docs-v5/en/#order-book-trading-copy-trading-get-leading-instruments) can get instruments that are supported to have leading trades and the instruments that you enable leading trade. For instruments that are disenabled copy trading, you can still trade normally, but copy trading will not be triggered;**[Amend leading instruments](/docs-v5/en/#order-book-trading-copy-trading-amend-leading-instruments) can amend your leading instruments. You need to set initial leading instruments while applying to become a leading trader. All non-leading contracts can't have position or pending orders for the current request when setting non-leading contracts as leading contracts.

3. Open position:**

You can open the position by placing order endpoints and channels including [Place order](/docs-v5/en/#order-book-trading-trade-post-place-order) endpoint, [Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders) endpoint, [Place order channel](/docs-v5/en/#order-book-trading-trade-ws-place-order), [Place multiple orders channel](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders), `tdMode` should be `spot_isolated` for `SPOT` lead trading. **For buy/sell mode, the orders must be in the same direction as your existing positions and open orders. You can select the direction you want if the instrument does not have position and pending orders.
For long/short mode, you can open long or open short as you want.

4. Close position**

You can close the position with customized price or size by placing order endpoints and channels including [Place order](/docs-v5/en/#order-book-trading-trade-post-place-order) endpoint, [Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders) endpoint, [Place order channel](/docs-v5/en/#order-book-trading-trade-ws-place-order), [Place multiple orders channel](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders), or close the position by [Close positions](/docs-v5/en/#order-book-trading-trade-post-close-positions) / [Close lead position](/docs-v5/en/#order-book-trading-copy-trading-post-close-lead-position);**[Close positions](/docs-v5/en/#order-book-trading-trade-post-close-positions) can close certain position under the current instrument(e.g. the long or short position under long/shor mode ), which can contain multiple leading positions;
[Close lead position](/docs-v5/en/#order-book-trading-copy-trading-post-close-lead-position) can only close a leading position once a time. It is required to pass subPosId which can get from [Get existing leading positions](/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions).

5. TP/SL**

TP/SL can be set by [Place algo order](/docs-v5/en/#order-book-trading-trade-ws-mass-cancel-order) or [Place lead stop order](/docs-v5/en/#order-book-trading-copy-trading-post-place-lead-stop-order);

- [Place algo order](/docs-v5/en/#order-book-trading-trade-ws-mass-cancel-order) can set TP/SL for certain position under the current instrument(e.g. the long or short position under long/shor mode ), which can contain multiple leading positions;

- [Place lead stop order](/docs-v5/en/#order-book-trading-copy-trading-post-place-lead-stop-order) set set TP/SL for only a leading position once a time. It is required to pass subPosId which can get from [Get existing leading positions](/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions).

### GET / Existing lead positions

Retrieve lead positions that are not closed.

Returns reverse chronological order with `openTime`

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/current-subpositions`

Request example

```
GET /api/v5/copytrading/current-subpositions?instId=BTC-USDT-SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`It returns all types by default. |
| instId | String | No | Instrument ID, e.g. BTC-USDT-SWAP |
| after | String | No | Pagination of data to return records earlier than the requested `subPosId`. |
| before | String | No | Pagination of data to return records newer than the requested `subPosId`. |
| limit | String | No | Number of results per request. Maximum is 500. Default is 500. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "algoId": "",
 "ccy": "USDT",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "lever": "3",
 "margin": "12.6417",
 "markPx": "38205.8",
 "mgnMode": "isolated",
 "openAvgPx": "37925.1",
 "openOrdId": "",
 "openTime": "1701231120479",
 "posSide": "net",
 "slOrdPx": "",
 "slTriggerPx": "",
 "subPos": "1",
 "subPosId": "649945658862370816",
 "tpOrdPx": "",
 "tpTriggerPx": "",
 "uniqueCode": "25CD5A80241D6FE6",
 "upl": "0.2807",
 "uplRatio": "0.0222042921442527",
 "availSubPos": "1"
 },
 {
 "algoId": "",
 "ccy": "USDT",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "lever": "3",
 "margin": "12.6263333333333333",
 "markPx": "38205.8",
 "mgnMode": "isolated",
 "openAvgPx": "37879",
 "openOrdId": "",
 "openTime": "1701225074786",
 "posSide": "net",
 "slOrdPx": "",
 "slTriggerPx": "",
 "subPos": "1",
 "subPosId": "649920301388038144",
 "tpOrdPx": "",
 "tpTriggerPx": "",
 "uniqueCode": "25CD5A80241D6FE6",
 "upl": "0.3268",
 "uplRatio": "0.0258824150584758",
 "availSubPos": "1"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| subPosId | String | Lead position ID |
| posSide | String | Position side`long` `short` `net`(Long positions have positive subPos; short positions have negative subPos) |
| mgnMode | String | Margin mode. `cross` `isolated` |
| lever | String | Leverage |
| openOrdId | String | Order ID for opening position, only applicable to lead position |
| openAvgPx | String | Average open price |
| openTime | String | Open time |
| subPos | String | Quantity of positions |
| tpTriggerPx | String | Take-profit trigger price. |
| slTriggerPx | String | Stop-loss trigger price. |
| algoId | String | Stop order ID |
| instType | String | Instrument type |
| tpOrdPx | String | Take-profit order price, it is -1 for market price |
| slOrdPx | String | Stop-loss order price, it is -1 for market price |
| margin | String | Margin |
| upl | String | Unrealized profit and loss |
| uplRatio | String | Unrealized profit and loss ratio |
| markPx | String | Latest mark price, only applicable to contract |
| uniqueCode | String | Lead trader unique code |
| ccy | String | Margin currency |
| availSubPos | String | Quantity of positions that can be closed |

### GET / Lead position history

Retrieve the completed lead position of the last 3 months.

Returns reverse chronological order with `subPosId`.

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/subpositions-history`

Request example

```
GET /api/v5/copytrading/subpositions-history?instId=BTC-USDT-SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`It returns all types by default. |
| instId | String | No | Instrument ID, e.g. BTC-USDT-SWAP |
| after | String | No | Pagination of data to return records earlier than the requested `subPosId`. |
| before | String | No | Pagination of data to return records newer than the requested `subPosId`. |
| limit | String | No | Number of results per request. Maximum is 100. Default is 100. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "closeAvgPx": "37617.5",
 "closeTime": "1701188587950",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "lever": "3",
 "margin": "37.41",
 "markPx": "38203.4",
 "mgnMode": "isolated",
 "openAvgPx": "37410",
 "openOrdId": "",
 "openTime": "1701184638702",
 "pnl": "0.6225",
 "pnlRatio": "0.0166399358460306",
 "posSide": "net",
 "profitSharingAmt": "0.0407967",
 "subPos": "3",
 "closeSubPos": "2",
 "type": "1",
 "subPosId": "649750700213698561",
 "uniqueCode": "25CD5A80241D6FE6"
 },
 {
 "ccy": "USDT",
 "closeAvgPx": "37617.5",
 "closeTime": "1701188587950",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "lever": "3",
 "margin": "24.94",
 "markPx": "38203.4",
 "mgnMode": "isolated",
 "openAvgPx": "37410",
 "openOrdId": "",
 "openTime": "1701184635381",
 "pnl": "0.415",
 "pnlRatio": "0.0166399358460306",
 "posSide": "net",
 "profitSharingAmt": "0.0271978",
 "subPos": "2",
 "closeSubPos": "2",
 "type": "2",
 "subPosId": "649750686292803585",
 "uniqueCode": "25CD5A80241D6FE6"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| subPosId | String | Lead position ID |
| posSide | String | Position side`long` `short` `net`(long position has positive subPos; short position has negative subPos) |
| mgnMode | String | Margin mode. `cross` `isolated` |
| lever | String | Leverage |
| openOrdId | String | Order ID for opening position, only applicable to lead position |
| openAvgPx | String | Average open price |
| openTime | String | Time of opening |
| subPos | String | Quantity of positions |
| closeTime | String | Time of closing position |
| closeAvgPx | String | Average price of closing position |
| pnl | String | Profit and loss |
| pnlRatio | String | P&L ratio |
| instType | String | Instrument type |
| margin | String | Margin |
| ccy | String | Currency |
| markPx | String | Latest mark price, only applicable to contract |
| uniqueCode | String | Lead trader unique code |
| profitSharingAmt | String | Profit sharing amount, only applicable to copy trading. Note: this parameter is already deprecated. |
| closeSubPos | String | Quantity of positions that is already closed |
| type | String | The type of closing position`1`：Close position partially;`2`：Close all |

### POST / Place lead stop order

Set TP/SL for the current lead position that are not closed.

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP Request

`POST /api/v5/copytrading/algo-order`

Request example

```
POST /api/v5/copytrading/algo-order
body
{
 "subPosId": "518541406042591232",
 "tpTriggerPx": "10000"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`, the default value |
| subPosId | String | Yes | Lead position ID |
| tpTriggerPx | String | Conditional | Take-profit trigger price. Take-profit order price will be the market price after triggering. At least one of tpTriggerPx and slTriggerPx must be filledThe take profit order will be deleted if it is 0 |
| slTriggerPx | String | Conditional | Stop-loss trigger price. Stop-loss order price will be the market price after triggering. The stop loss order will be deleted if it is 0 |
| tpOrdPx | String | No | Take-profit order priceIf the price is -1, take-profit will be executed at the market price, the default is `-1`Only applicable to `SPOT` lead trader |
| slOrdPx | String | No | Stop-loss order priceIf the price is -1, stop-loss will be executed at the market price, the default is `-1`Only applicable to `SPOT` lead trader |
| tpTriggerPxType | String | No | Take-profit trigger price type `last`: last price`index`: index price`mark`: mark price Default is `last` |
| slTriggerPxType | String | No | Stop-loss trigger price type`last`: last price `index`: index price `mark`: mark price Default is last |
| tag | String | No | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "subPosId": "518560559046594560",
 "tag":""
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| subPosId | String | Lead position ID |
| tag | String | Order tag |

### POST / Close lead position

You can only close a lead position once a time.

It is required to pass subPosId which can get from [Get existing leading positions](/docs-v5/en/#order-book-trading-copy-trading-get-existing-lead-positions).

#### Rate limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/close-subposition`

Request example

```
POST /api/v5/copytrading/close-subposition
body
{
 "subPosId": "518541406042591232",
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`, the default value |
| subPosId | String | Yes | Lead position ID |
| ordType | String | No | Order type`market`：Market order, the default value`limit`：Limit order |
| px | String | No | Order price. Only applicable to `limit` order and `SPOT` lead trader If the price is 0, the pending order will be canceled. It is modifying order if you set `px` after placing limit order. |
| tag | String | No | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "subPosId": "518560559046594560",
 "tag":""
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| subPosId | String | Lead position ID |
| tag | String | Order tag |

### GET / Leading instruments

Retrieve instruments that are supported to lead by the platform.
Retrieve instruments that the lead trader has set.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/instruments`

Request example

```
GET /api/v5/copytrading/instruments
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`, the default value |

Response example

```
{
 "code": "0",
 "data": [
 {
 "enabled": true,
 "instId": "BTC-USDT-SWAP"
 },
 {
 "enabled": true,
 "instId": "ETH-USDT-SWAP"
 },
 {
 "enabled": false,
 "instId": "ADA-USDT-SWAP"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| enabled | Boolean | Whether instrument is a lead instrument. `true` or `false` |

### POST / Amend leading instruments

The leading trader can amend current leading instruments, need to set initial leading instruments while applying to become a leading trader.

All non-leading instruments can't have position or pending orders for the current request when setting non-leading instruments as leading instruments.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/set-instruments`

Request example

```
POST /api/v5/copytrading/set-instruments
body
{
 "instId": "BTC-USDT-SWAP,ETH-USDT-SWAP"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`, the default value |
| instId | String | Yes | Instrument ID, e.g. BTC-USDT-SWAP. If there are multiple instruments, separate them with commas. |

The value of `instId` must include all instruments that you are going to have the lead trading with because the previous settings will be overwritten after the current request is set successfully

Response example

```
{
 "code": "0",
 "data": [
 {
 "enabled": true,
 "instId": "BTC-USDT-SWAP"
 },
 {
 "enabled": true,
 "instId": "ETH-USDT-SWAP"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| enabled | Boolean | Whether you set it successfully `true` or `false` |

### GET / Profit sharing details

The leading trader gets profits shared details for the last 3 months.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/profit-sharing-details`

Request example

```
GET /api/v5/copytrading/profit-sharing-details?limit=2
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`It returns all types by default. |
| after | String | No | Pagination of data to return records earlier than the requested `profitSharingId` |
| before | String | No | Pagination of data to return records newer than the requested `profitSharingId` |
| limit | String | No | Number of results per request. Maximum is 100. Default is 100. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "nickName": "Potato",
 "profitSharingAmt": "0.00536",
 "profitSharingId": "148",
 "portLink": "",
 "ts": "1723392000000",
 "instType": "SWAP"
 },
 {
 "ccy": "USDT",
 "nickName": "Apple",
 "profitSharingAmt": "0.00336",
 "profitSharingId": "20",
 "portLink": "",
 "ts": "1723392000000",
 "instType": "SWAP"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | The currency of profit sharing. |
| profitSharingAmt | String | Profit sharing amount. It would be 0 if there is no any profit sharing. |
| nickName | String | Nickname of copy trader. |
| profitSharingId | String | Profit sharing ID. |
| instType | String | Instrument type |
| portLink | String | Portrait link |
| ts | String | Profit sharing time. |

### GET / Total profit sharing

The leading trader gets the total amount of profit shared since joining the platform.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/total-profit-sharing`

Request example

```
GET /api/v5/copytrading/total-profit-sharing
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`It returns all types by default. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "totalProfitSharingAmt": "0.6584928",
 "instType": "SWAP"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | The currency of profit sharing. |
| totalProfitSharingAmt | String | Total profit sharing amount. |
| instType | String | Instrument type |

### GET / Unrealized profit sharing details

The leading trader gets the profit sharing details that are expected to be shared in the next settlement cycle.

The unrealized profit sharing details will update once there copy position is closed.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/unrealized-profit-sharing-details`

Request example

```
GET /api/v5/copytrading/unrealized-profit-sharing-details
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SPOT``SWAP`It returns all types by default. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "nickName": "Potato",
 "portLink": "",
 "ts": "1669901824779",
 "unrealizedProfitSharingAmt": "0.455472",
 "instType": "SWAP"
 },
 {
 "ccy": "USDT",
 "nickName": "Apple",
 "portLink": "",
 "ts": "1669460210113",
 "unrealizedProfitSharingAmt": "0.033608",
 "instType": "SWAP"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | The currency of profit sharing. e.g. USDT |
| unrealizedProfitSharingAmt | String | Unrealized profit sharing amount. |
| nickName | String | Nickname of copy trader. |
| instType | String | Instrument type |
| portLink | String | Portrait link |
| ts | String | Update time. |

### GET / Total unrealized profit sharing

The leading trader gets the total unrealized amount of profit shared.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/total-unrealized-profit-sharing`

Request example

```
GET /api/v5/copytrading/total-unrealized-profit-sharing
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "profitSharingTs": "1705852800000",
 "totalUnrealizedProfitSharingAmt": "0.114402985553185"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| profitSharingTs | String | The settlement time for the total unrealized profit sharing amount. Unix timestamp format in milliseconds, e.g.1597026383085 |
| totalUnrealizedProfitSharingAmt | String | Total unrealized profit sharing amount |

### POST / Amend profit sharing ratio

It is used to amend profit sharing ratio.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/amend-profit-sharing-ratio`

Request example

```
POST /api/v5/copytrading/amend-profit-sharing-ratio
body
{
 "instType": "SWAP",
 "profitSharingRatio": "0.1"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP` |
| profitSharingRatio | String | Yes | Profit sharing ratio. 0.1 represents 10% |

Response example

```
{
 "code": "0",
 "data": [
 {
 "result": true
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| result | Boolean | The result of setting `true` |

### GET / Account configuration

Retrieve current account configuration related to copy/lead trading.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/config`

Request example

```
GET /api/v5/copytrading/config
```

#### Request Parameters

None

Response example

```
{
 "code": "0",
 "data": [
 {
 "details": [
 {
 "copyTraderNum": "1",
 "instType": "SWAP",
 "maxCopyTraderNum": "100",
 "profitSharingRatio": "0",
 "roleType": "1"
 },
 {
 "copyTraderNum": "",
 "instType": "SPOT",
 "maxCopyTraderNum": "",
 "profitSharingRatio": "",
 "roleType": "0"
 }
 ],
 "nickName": "155***9957",
 "portLink": "",
 "uniqueCode": "5506D3681454A304"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| uniqueCode | String | User unique code |
| nickName | String | Nickname |
| portLink | String | Portrait link |
| details | Array of objects | Details |
| > instType | String | Instrument type`SPOT``SWAP` |
| > roleType | String | Role type`0`: General user`1`: Leading trader`2`: Copy trader |
| > profitSharingRatio | String | Profit sharing ratio. Only applicable to lead trader, or it will be "". 0.1 represents 10% |
| > maxCopyTraderNum | String | Maximum number of copy traders |
| > copyTraderNum | String | Current number of copy traders |

### POST / First copy settings

The first copy settings for the certain lead trader. You need to first copy settings after stopping copying.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/first-copy-settings`

Request example

```
POST /api/v5/copytrading/first-copy-settings
body
{
 "instType": "SWAP",
 "uniqueCode": "25CD5A80241D6FE6",
 "copyMgnMode": "cross",
 "copyInstIdType": "copy",
 "copyMode": "ratio_copy",
 "copyRatio": "1",
 "copyTotalAmt": "500",
 "subPosCloseType": "copy_close"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| copyMgnMode | String | Yes | Copy margin mode`cross`: cross`isolated`: isolated`copy`: Use the same margin mode as lead trader when opening positions |
| copyInstIdType | String | Yes | Copy contract type setted`custom`: custom by `instId` which is required；`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do |
| instId | String | Conditional | Instrument ID. If there are multiple instruments, separate them with commas. |
| copyMode | String | No | Copy mode`fixed_amount`: set the same fixed amount for each order, and `copyAmt` is required；`ratio_copy`: set amount as a multiple of the lead trader’s order value, and `copyRatio` is required The default is `fixed_amount` |
| copyTotalAmt | String | Yes | Maximum total amount in USDT. The maximum total amount you'll invest at any given time across all orders in this copy tradeYou won’t copy new orders if you exceed this amount |
| copyAmt | String | Conditional | Copy amount per order in USDT. |
| copyRatio | String | Conditional | Copy ratio per order. |
| tpRatio | String | No | Take profit per order. 0.1 represents 10% |
| slRatio | String | No | Stop loss per order. 0.1 represents 10% |
| slTotalAmt | String | No | Total stop loss in USDT for trader. If your net loss (total profit - total loss) reaches this amount, you'll stop copying this trader |
| subPosCloseType | String | Yes | Action type for open positions`market_close`: immediately close at market price`copy_close`：close when trader closes`manual_close`: close manuallyThe default is `copy_close` |
| tag | String | No | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "result": true
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| result | Boolean | The result of setting `true` |

### POST / Amend copy settings

You need to use this endpoint to amend copy settings

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/amend-copy-settings`

Request example

```
POST /api/v5/copytrading/amend-copy-settings
body
{
 "instType": "SWAP",
 "uniqueCode": "25CD5A80241D6FE6",
 "copyMgnMode": "cross",
 "copyInstIdType": "copy",
 "copyMode": "ratio_copy",
 "copyRatio": "1",
 "copyTotalAmt": "500",
 "subPosCloseType": "copy_close"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP` |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| copyMgnMode | String | Yes | Copy margin mode`cross`: cross`isolated`: isolated`copy`: Use the same margin mode as lead trader when opening positions |
| copyInstIdType | String | Yes | Copy contract type setted`custom`: custom by `instId` which is required；`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do |
| instId | String | Conditional | Instrument ID. If there are multiple instruments, separate them with commas. |
| copyMode | String | No | Copy mode`fixed_amount`: set the same fixed amount for each order, and `copyAmt` is required；`ratio_copy`: set amount as a multiple of the lead trader’s order value, and `copyRatio` is required The default is `fixed_amount` |
| copyTotalAmt | String | Yes | Maximum total amount in USDT. The maximum total amount you'll invest at any given time across all orders in this copy tradeYou won’t copy new orders if you exceed this amount |
| copyAmt | String | Conditional | Copy amount per order in USDT |
| copyRatio | String | Conditional | Copy ratio per order. |
| tpRatio | String | No | Take profit per order. 0.1 represents 10% |
| slRatio | String | No | Stop loss per order. 0.1 represents 10% |
| slTotalAmt | String | No | Total stop loss in USDT for trader.If your net loss (total profit - total loss) reaches this amount, you'll stop copying this trader |
| subPosCloseType | String | Yes | Action type for open positions`market_close`: immediately close at market price`copy_close`：close when trader closes`manual_close`: close manuallyThe default is `copy_close` |
| tag | String | No | Order tagA combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "result": true
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| result | Boolean | The result of setting `true` |

### POST / Stop copying

You need to use this endpoint to stop copy trading

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`POST /api/v5/copytrading/stop-copy-trading`

Request example

```
POST /api/v5/copytrading/stop-copy-trading
body
{
 "instType": "SWAP",
 "uniqueCode": "25CD5A80241D6FE6",
 "subPosCloseType": "manual_close"
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP` |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| subPosCloseType | String | Yes | Action type for open positions, it is required if you have related copy position`market_close`: immediately close at market price`copy_close`：close when trader closes`manual_close`: close manually |

Response example

```
{
 "code": "0",
 "data": [
 {
 "result": true
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| result | Boolean | The result of setting `true` |

### GET / Copy settings

Retrieve the copy settings about certain lead trader.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/copy-settings`

Request example

```
GET /api/v5/copytrading/copy-settings?instType=SWAP&uniqueCode=25CD5A80241D6FE6
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP` |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "copyAmt": "",
 "copyInstIdType": "copy",
 "copyMgnMode": "isolated",
 "copyMode": "ratio_copy",
 "copyRatio": "1",
 "copyState": "1",
 "copyTotalAmt": "500",
 "instIds": [
 {
 "enabled": "1",
 "instId": "ADA-USDT-SWAP"
 },
 {
 "enabled": "1",
 "instId": "YFII-USDT-SWAP"
 }
 ],
 "slRatio": "",
 "slTotalAmt": "",
 "subPosCloseType": "copy_close",
 "tpRatio": "",
 "tag": ""
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| copyMode | String | Copy mode`fixed_amount` `ratio_copy` |
| copyAmt | String | Copy amount in USDT per order. |
| copyRatio | String | Copy ratio per order. |
| copyTotalAmt | String | Maximum total amount in USDT. The maximum total amount you'll invest at any given time across all orders in this copy trade |
| tpRatio | String | Take profit per order. 0.1 represents 10% |
| slRatio | String | Stop loss per order. 0.1 represents 10% |
| copyInstIdType | String | Copy contract type setted`custom`: custom by `instId` which is required；`copy`: Keep your contracts consistent with this trader by automatically adding or removing contracts when they do |
| instIds | Array of objects | Instrument list. It will return all lead contracts of the lead trader |
| > instId | String | Instrument ID |
| > enabled | String | Whether copying this `instId``0` `1` |
| slTotalAmt | String | Total stop loss in USDT for trader. |
| subPosCloseType | String | Action type for open positions`market_close`: immediately close at market price`copy_close`：close when trader closes`manual_close`: close manually |
| copyMgnMode | String | Copy margin mode`cross`: cross`isolated`: isolated`copy`: Use the same margin mode as lead trader when opening positions |
| ccy | String | Margin currency |
| copyState | String | Current copy state `0`: non-copy, `1`: copy |
| tag | String | Order tag |

### GET / My lead traders

Retrieve my lead traders.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### HTTP request

`GET /api/v5/copytrading/current-lead-traders`

Request example

```
GET /api/v5/copytrading/current-lead-traders?instType=SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |

Response example

```
{
 "code": "0",
 "data": [
 {
 "beginCopyTime": "1701224821936",
 "ccy": "USDT",
 "copyTotalAmt": "500",
 "copyTotalPnl": "0",
 "leadMode": "public",
 "margin": "1.89395",
 "nickName": "Trader9527",
 "portLink": "",
 "profitSharingRatio": "0.08",
 "todayPnl": "0",
 "uniqueCode": "25CD5A80241D6FE6",
 "upl": "0"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| portLink | String | Portrait link |
| nickName | String | Nick name |
| margin | String | Margin for copy trading |
| copyTotalAmt | String | Copy total amount |
| copyTotalPnl | String | Copy total pnl |
| uniqueCode | String | Lead trader unique code |
| ccy | String | margin currency |
| profitSharingRatio | String | Profit sharing ratio. 0.1 represents 10% |
| beginCopyTime | String | Begin copying time. Unix timestamp format in milliseconds, e.g.1597026383085 |
| upl | String | Unrealized profit & loss |
| todayPnl | String | Today pnl |
| leadMode | String | Lead mode `public` `private` |

### GET / Copy trading configuration

Public endpoint. Retrieve copy trading parameter configuration information of copy settings

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-config`

Request example

```
GET /api/v5/copytrading/public-config?instType=SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |

Response example

```
{
 "code": "0",
 "data": [
 {
 "maxCopyAmt": "1000",
 "maxCopyRatio": "100",
 "maxCopyTotalAmt": "30000",
 "maxSlRatio": "0.75",
 "maxTpRatio": "1.5",
 "minCopyAmt": "20",
 "minCopyRatio": "0.01"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| maxCopyAmt | String | Maximum copy amount per order in USDT when you are using copy mode `fixed_amount` |
| minCopyAmt | String | Minimum copy amount per order in USDT when you are using copy mode `fixed_amount` |
| maxCopyTotalAmt | String | Maximum copy total amount under the certain lead trader, the minimum is the same with `minCopyAmt` |
| minCopyRatio | String | Minimum ratio per order when you are using copy mode `ratio_copy` |
| maxCopyRatio | String | Maximum ratio per order when you are using copy mode `ratio_copy` |
| maxTpRatio | String | Maximum ratio of taking profit per order, the minimum is 0 |
| maxSlRatio | String | Maximum ratio of stopping loss per order, the minimum is 0 |

### GET / Lead trader ranks

Public endpoint. Retrieve lead trader ranks.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-lead-traders`

Request example

```
GET /api/v5/copytrading/public-lead-traders?instType=SWAP
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |
| sortType | String | No | Sort type`overview`: overview, the default value`pnl`: profit and loss`aum`: assets under management`win_ratio`: win ratio`pnl_ratio`: pnl ratio`current_copy_trader_pnl`: current copy trader pnl |
| state | String | No | Lead trader state`0`: All lead traders, the default, including vacancy and non-vacancy `1`: lead traders who have vacancy |
| minLeadDays | String | No | Minimum lead days`1`: 7 days`2`: 30 days`3`: 90 days`4`: 180 days |
| minAssets | String | No | Minimum assets in USDT |
| maxAssets | String | No | Maximum assets in USDT |
| minAum | String | No | Minimum assets in USDT under management. |
| maxAum | String | No | Maximum assets in USDT under management. |
| dataVer | String | No | Data version. It is 14 numbers. e.g. 20231010182400. Generally, it is used for pagination A new version will be generated every 10 minutes. Only last 5 versions are storedThe default is latest version. If it is not exist, error will not be throwed and the latest version will be used. |
| page | String | No | Page for pagination |
| limit | String | No | Number of results per request. The maximum is 20; the default is 10 |

Response example

```
{
 "code": "0",
 "data": [
 {
 "dataVer": "20231129213200",
 "ranks": [
 {
 "accCopyTraderNum": "3536",
 "aum": "1509265.3238761567721365",
 "ccy": "USDT",
 "copyState": "0",
 "copyTraderNum": "999",
 "leadDays": "156",
 "maxCopyTraderNum": "1000",
 "nickName": "Crypto to the moon",
 "pnl": "48805.1105999999972258",
 "pnlRatio": "1.6898",
 "pnlRatios": [
 {
 "beginTs": "1701187200000",
 "pnlRatio": "1.6744"
 },
 {
 "beginTs": "1700755200000",
 "pnlRatio": "1.649"
 }
 ],
 "portLink": "https://static.okx.com/cdn/okex/users/headimages/20230624/f49a683aaf5949ea88b01bbc771fb9fc",
 "traderInsts": [
 "ICP-USDT-SWAP",
 "MINA-USDT-SWAP"

 ],
 "uniqueCode": "540D011FDACCB47A",
 "winRatio": "0.6957"
 }
 ],
 "totalPage": "1"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| dataVer | String | Data version |
| totalPage | String | Total number of pages |
| ranks | Array of objects | The rank information of lead traders |
| > aum | String | assets under management |
| > copyState | String | Current copy state `0`: non-copy, `1`: copy |
| > maxCopyTraderNum | String | Maximum number of copy traders |
| > copyTraderNum | String | Current number of copy traders |
| > accCopyTraderNum | String | Accumulated number of copy traders |
| > portLink | String | Portrait link |
| > nickName | String | Nick name |
| > ccy | String | Margin currency |
| > uniqueCode | String | Lead trader unique code |
| > winRatio | String | Win ratio, 0.1 represents 10% |
| > leadDays | String | Lead days |
| > traderInsts | Array of strings | Contract list which lead trader is leading |
| > pnl | String | Pnl (in USDT) of last 90 days. |
| > pnlRatio | String | Pnl ratio of last 90 days. 0.1 represents 10% |
| > pnlRatios | Array of objects | Pnl ratios |
| >> beginTs | String | Begin time of pnl ratio on that day |
| >> pnlRatio | String | Pnl ratio on that day |

### GET / Lead trader weekly pnl

Public endpoint. Retrieve lead trader weekly pnl. Results are returned in counter chronological order.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-weekly-pnl`

Request example

```
GET /api/v5/copytrading/public-weekly-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |

Response example

```
{
 "code": "0",
 "data": [
 {
 "beginTs": "1701014400000",
 "pnl": "-2.8428",
 "pnlRatio": "-0.0106"
 },
 {
 "beginTs": "1700409600000",
 "pnl": "81.8446",
 "pnlRatio": "0.3036"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| beginTs | String | Begin time of pnl ratio on that week |
| pnl | String | Pnl on that week |
| pnlRatio | String | Pnl ratio on that week |

### GET / Lead trader daily pnl

Public endpoint. Retrieve lead trader daily pnl. Results are returned in counter chronological order.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-pnl`

Request example

```
GET /api/v5/copytrading/public-pnl?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| lastDays | String | Yes | Last days`1`: last 7 days `2`: last 30 days`3`: last 90 days `4`: last 365 days |

Response example

```
{
 "code": "0",
 "data": [
 {
 "beginTs": "1701100800000",
 "pnl": "97.3309",
 "pnlRatio": "0.3672"
 },
 {
 "beginTs": "1701014400000",
 "pnl": "96.7755",
 "pnlRatio": "0.3651"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| beginTs | String | Begin time on that day |
| pnl | String | Accumulated pnl |
| pnlRatio | String | Accumulated pnl ratio |

### GET / Lead trader stats

Public endpoint. Key data related to lead trader performance.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-stats`

Request example

```
GET /api/v5/copytrading/public-stats?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD&lastDays=1
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| lastDays | String | Yes | Last days`1`: last 7 days `2`: last 30 days`3`: last 90 days `4`: last 365 days |

Response example

```
{
 "code": "0",
 "data": [
 {
 "avgSubPosNotional": "213.1038",
 "ccy": "USDT",
 "curCopyTraderPnl": "96.8071",
 "investAmt": "265.095252476476294",
 "lossDays": "1",
 "profitDays": "2",
 "winRatio": "0.6667"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| winRatio | String | Win ratio |
| profitDays | String | Profit days |
| lossDays | String | Loss days |
| curCopyTraderPnl | String | Current copy trader pnl (USDT) |
| avgSubPosNotional | String | Average lead position notional (USDT) |
| investAmt | String | Investment amount (USDT) |
| ccy | String | Margin currency |

### GET / Lead trader currency preferences

Public endpoint. The most frequently traded crypto of this lead trader. Results are sorted by ratio from large to small.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-preference-currency`

Request example

```
GET /api/v5/copytrading/public-preference-currency?instType=SWAP&uniqueCode=CB4594A3BB5D3538
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "ETH",
 "ratio": "0.8881"
 },
 {
 "ccy": "BTC",
 "ratio": "0.0666"
 },
 {
 "ccy": "YFII",
 "ratio": "0.0453"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| ccy | String | Currency |
| ratio | String | Ratio. 0.1 represents 10% |

### GET / Lead trader current lead positions

Public endpoint. Get current leading positions of lead trader

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-current-subpositions`

Request example

```
GET /api/v5/copytrading/public-current-subpositions?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value. |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| after | String | No | Pagination of data to return records earlier than the requested `subPosId`. |
| before | String | No | Pagination of data to return records newer than the requested `subPosId`. |
| limit | String | No | Number of results per request. Maximum is 100. Default is 100. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "instId": "ETH-USDT-SWAP",
 "instType": "SWAP",
 "lever": "5",
 "margin": "16.23304",
 "markPx": "2027.31",
 "mgnMode": "isolated",
 "openAvgPx": "2029.13",
 "openTime": "1701144639417",
 "posSide": "short",
 "subPos": "4",
 "subPosId": "649582930998104064",
 "uniqueCode": "D9ADEAB33AE9EABD",
 "upl": "0.0728",
 "uplRatio": "0.0044846806266725"
 }
 ],
 "msg": ""
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| subPosId | String | Lead position ID |
| posSide | String | Position side`long` `short` `net`(Long positions have positive subPos; short positions have negative subPos) |
| mgnMode | String | Margin mode. `cross` `isolated` |
| lever | String | Leverage |
| openAvgPx | String | Average open price |
| openTime | String | Open time |
| subPos | String | Quantity of positions |
| instType | String | Instrument type |
| margin | String | Margin |
| upl | String | Unrealized profit and loss |
| uplRatio | String | Unrealized profit and loss ratio |
| markPx | String | Latest mark price, only applicable to contract |
| uniqueCode | String | Lead trader unique code |
| ccy | String | Currency |

### GET / Lead trader lead position history

Public endpoint. Retrieve the lead trader completed leading position of the last 3 months.

Returns reverse chronological order with `subPosId`.

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-subpositions-history`

Request example

```
GET /api/v5/copytrading/public-subpositions-history?instType=SWAP&uniqueCode=9A8534AB09862774
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value. |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| after | String | No | Pagination of data to return records earlier than the requested `subPosId`. |
| before | String | No | Pagination of data to return records newer than the requested `subPosId`. |
| limit | String | No | Number of results per request. Maximum is 100. Default is 100. |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "closeAvgPx": "28385.9",
 "closeTime": "1697709137162",
 "instId": "BTC-USDT-SWAP",
 "instType": "SWAP",
 "lever": "20",
 "margin": "4.245285",
 "mgnMode": "isolated",
 "openAvgPx": "28301.9",
 "openTime": "1697698048031",
 "pnl": "0.252",
 "pnlRatio": "0.05935997229868",
 "posSide": "long",
 "subPos": "3",
 "subPosId": "635126416883355648",
 "uniqueCode": "9A8534AB09862774"
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| instId | String | Instrument ID, e.g. BTC-USDT-SWAP |
| subPosId | String | Lead position ID |
| posSide | String | Position side`long` `short` `net`(long position has positive subPos; short position has negative subPos) |
| mgnMode | String | Margin mode. `cross` `isolated` |
| lever | String | Leverage |
| openAvgPx | String | Average open price |
| openTime | String | Time of opening |
| subPos | String | Quantity of positions |
| closeTime | String | Time of closing position |
| closeAvgPx | String | Average price of closing position |
| pnl | String | Profit and loss |
| pnlRatio | String | P&L ratio |
| instType | String | Instrument type |
| margin | String | Margin |
| ccy | String | Currency |
| uniqueCode | String | Lead trader unique code |

### GET / Copy traders

Public endpoint. Retrieve copy trader coming from certain lead trader. Return according to `pnl` from high to low

#### Rate limit: 5 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP request

`GET /api/v5/copytrading/public-copy-traders`

Request example

```
GET /api/v5/copytrading/public-copy-traders?instType=SWAP&uniqueCode=D9ADEAB33AE9EABD
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| instType | String | No | Instrument type`SWAP`, the default value |
| uniqueCode | String | Yes | Lead trader unique codeA combination of case-sensitive alphanumerics, all numbers and the length is 16 or 18 characters, e.g. 213E8C92DC61EFAC (16 characters) or 381749205163847291 (18 characters) |
| limit | String | No | Number of results per request. The maximum is `100`; The default is `100` |

Response example

```
{
 "code": "0",
 "data": [
 {
 "ccy": "USDT",
 "copyTotalPnl": "2060.12242",
 "copyTraderNumChg": "1",
 "copyTraderNumChgRatio": "0.5",
 "copyTraders": [
 {
 "beginCopyTime": "1686125051000",
 "nickName": "bre***@gmail.com",
 "pnl": "1076.77388",
 "portLink": ""
 },
 {
 "beginCopyTime": "1698133811000",
 "nickName": "MrYanDao505",
 "pnl": "983.34854",
 "portLink": "https://static.okx.com/cdn/okex/users/headimages/20231010/fd31f45e99fe41f7bb219c0b53ae0ada"
 }
 ]
 }
 ],
 "msg": ""
}

```

#### Response parameters

| Parameter | Type | Description |
| --- | --- | --- |
| copyTotalPnl | String | Total copy trader profit and loss |
| ccy | String | The currency name of profit and loss |
| copyTraderNumChg | String | Number change in last 7 days |
| copyTraderNumChgRatio | String | Ratio change in last 7 days |
| copyTraders | Array of objects | Copy trader information |
| > beginCopyTime | String | Begin copying time. Unix timestamp format in milliseconds, e.g.1597026383085 |
| > nickName | String | Nick name |
| > portLink | String | Copy trader portrait link |
| > pnl | String | Copy trading profit and loss |

### WS / Lead trading notification channel

The notification when failing to lead trade.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [{
 "channel": "copytrading-lead-notification",
 "instType": "SWAP"
 }]
}
```

```
import asyncio

from okx.websocket.WsPrivateAsync import WsPrivateAsync

def callbackFunc(message):
 print(message)

async def main():

 ws = WsPrivateAsync(
 apiKey = "YOUR_API_KEY",
 passphrase = "YOUR_PASSPHRASE",
 secretKey = "YOUR_SECRET_KEY",
 url = "wss://ws.okx.com:8443/ws/v5/business",
 useServerTime=False
 )
 await ws.start()
 args = [{
 "channel": "copytrading-lead-notification",
 "instType": "SWAP"
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
| > channel | String | Yes | Channel name`copytrading-lead-notification` |
| > instType | String | Yes | Instrument type`SWAP` |
| > instId | String | No | Instrument ID |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "copytrading-lead-notification",
 "instType": "SWAP"
 },
 "connId": "aa993428"
}

```

Failure Response Example

```
{
 "id": "1512",
 "event": "error",
 "code": "60012",
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"copytrading-lead-notification\", \"instType\" : \"FUTURES\"}]}",
 "connId":"a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instType | String | Yes | Instrument type`SWAP` |
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example:

```
{
 "arg": {
 "channel": "copytrading-lead-notification",
 "instType": "SWAP",
 "uid": "525627088439549953"
 },
 "data": [
 {
 "infoType": "2",
 "instId": "",
 "instType": "SWAP",
 "maxLeadTraderNum": "3",
 "minLeadEq": "",
 "posSide": "",
 "side": "",
 "subPosId": "667695035433385984",
 "uniqueCode": "3AF72F63E3EAD701"
 }
 ]
}

```

#### Push data parameters

| Parameter | Type | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > instType | String | Instrument type |
| data | Array of objects | Subscribed data |
| > instType | String | Instrument type |
| > infoType | String | Information type`1`: lead trading failed due to touch max position limitation `2`: lead trading failed due to touch the maximum daily number of lead trading `3`: lead trading failed due to your USDT equity less than the minimum USDT equity of lead trading |
| > subPosId | String | Lead position ID |
| > uniqueCode | String | Lead trader unique code |
| > instId | String | Instrument ID |
| > side | String | Side `buy` `sell` |
| > posSide | String | Position side `long``short``net` |
| > maxLeadTraderNum | String | Maximum daily number of lead trading. |
| > minLeadEq | String | Minimum USDT equity of lead trading. |
