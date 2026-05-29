## WebSocket

### Deposit info channel

A push notification is triggered when a deposit is initiated or the deposit status changes.

Supports subscriptions for accounts

- If it is a master account subscription, you can receive the push of the deposit info of both the master account and the sub-account.

- If it is a sub-account subscription, only the push of sub-account deposit info you can receive.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "deposit-info"
 }
 ]
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
 args = [
 {
 "channel": "deposit-info"
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
| > channel | String | Yes | Channel name`deposit-info` |
| > ccy | String | No | Currency, e.g. `BTC` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "deposit-info"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"deposit-info\""}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Operation`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`deposit-info` |
| > ccy | String | No | Currency, e.g. `BTC` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "deposit-info",
 "uid": "289320****60975104"
 },
 "data": [{
 "actualDepBlkConfirm": "0",
 "amt": "1",
 "areaCodeFrom": "",
 "ccy": "USDT",
 "chain": "USDT-TRC20",
 "depId": "88165462",
 "from": "",
 "fromWdId": "",
 "pTime": "1674103661147",
 "state": "0",
 "subAcct": "test",
 "to": "TEhFAqpuHa3LY*****8ByNoGnrmexeGMw",
 "ts": "1674103661123",
 "txId": "bc5376817*****************dbb0d729f6b",
 "uid": "289320****60975104"
 }]
}

```

#### Push data parameters

| Parameters | Types | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name`deposit-info` |
| > uid | String | User Identifier |
| > ccy | String | Currency, e.g. `BTC` |
| data | Array of objects | Subscribed data |
| > uid | String | User Identifier of the message producer |
| > subAcct | String | Sub-account nameIf the message producer is master account, the parameter will return "" |
| > pTime | String | Push time, the millisecond format of the Unix timestamp, e.g. `1597026383085` |
| > ccy | String | Currency |
| > chain | String | Chain name |
| > amt | String | Deposit amount |
| > from | String | Deposit accountOnly the internal OKX account (masked mobile phone number or email address) is returned, not the address on the blockchain. |
| > areaCodeFrom | String | If `from` is a phone number, this parameter return area code of the phone number |
| > to | String | Deposit address |
| > txId | String | Hash record of the deposit |
| > ts | String | Time of deposit record is created, Unix timestamp format in milliseconds, e.g. `1655251200000` |
| > state | String | Status of deposit`0`: waiting for confirmation`1`: deposit credited `2`: deposit successful `8`: pending due to temporary deposit suspension on this crypto currency`11`: match the address blacklist`12`: account or deposit is frozen`13`: sub-account deposit interception`14`: KYC limit |
| > depId | String | Deposit ID |
| > fromWdId | String | Internal transfer initiator's withdrawal IDIf the deposit comes from internal transfer, this field displays the withdrawal ID of the internal transfer initiator, and will return "" in other cases |
| > actualDepBlkConfirm | String | The actual amount of blockchain confirmed in a single deposit |

### Withdrawal info channel

A push notification is triggered when a withdrawal is initiated or the withdrawal status changes.

Supports subscriptions for accounts

- If it is a master account subscription, you can receive the push of the withdrawal info of both the master account and the sub-account.

- If it is a sub-account subscription, only the push of sub-account withdrawal info you can receive.

#### URL Path

/ws/v5/business (required login)

Request Example

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [
 {
 "channel": "withdrawal-info"
 }
 ]
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
 args = [
 {
 "channel": "withdrawal-info"
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
| > channel | String | Yes | Channel name`withdrawal-info` |
| > ccy | String | No | Currency, e.g. `BTC` |

Successful Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "withdrawal-info"
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
 "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"withdrawal-info\"}]}",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Operation`subscribe``unsubscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name`withdrawal-info` |
| > ccy | String | No | Currency, e.g. `BTC` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

Push Data Example

```
{
 "arg": {
 "channel": "withdrawal-info",
 "uid": "289320*****0975104"
 },
 "data": [{
 "addrEx": null,
 "amt": "2",
 "areaCodeFrom": "",
 "areaCodeTo": "",
 "ccy": "USDT",
 "chain": "USDT-TRC20",
 "clientId": "",
 "fee": "0.8",
 "feeCcy": "USDT",
 "from": "",
 "memo": "",
 "nonTradableAsset": false,
 "note": "",
 "pTime": "1674103268578",
 "pmtId": "",
 "state": "0",
 "subAcct": "test",
 "tag": "",
 "to": "TN8CKTQMnpWfT******8KipbJ24ErguhF",
 "toAddrType": "1",
 "ts": "1674103268472",
 "txId": "",
 "uid": "289333*****1101696",
 "wdId": "63754560"
 }]
}

```

#### Push data parameters

| Parameters | Types | Description |
| --- | --- | --- |
| arg | Object | Successfully subscribed channel |
| > channel | String | Channel name |
| > uid | String | User Identifier |
| > ccy | String | Currency, e.g. `BTC` |
| data | Array of objects | Subscribed data |
| > uid | String | User Identifier of the message producer |
| > subAcct | String | Sub-account nameIf the message producer is master account, the parameter will return "" |
| > pTime | String | Push time, the millisecond format of the Unix timestamp, e.g. `1597026383085` |
| > ccy | String | Currency |
| > chain | String | Chain name, e.g. `USDT-ERC20`, `USDT-TRC20` |
| > nonTradableAsset | String | Whether it is a non-tradable asset or not`true`: non-tradable asset, `false`: tradable asset |
| > amt | String | Withdrawal amount |
| > ts | String | Time the withdrawal request was submitted, Unix timestamp format in milliseconds, e.g. `1655251200000`. |
| > from | String | Withdrawal accountIt can be `email`/`phone`/`sub-account name` |
| > areaCodeFrom | String | Area code for the phone numberIf `from` is a phone number, this parameter returns the area code for the phone number |
| > to | String | Receiving address |
| > areaCodeTo | String | Area code for the phone numberIf `to` is a phone number, this parameter returns the area code for the phone number |
| > toAddrType | String | Address type`1`: wallet address, email, phone, or login account name`2`: UID |
| > tag | String | Some currencies require a tag for withdrawals |
| > pmtId | String | Some currencies require a payment ID for withdrawals |
| > memo | String | Some currencies require this parameter for withdrawals |
| > addrEx | Object | Withdrawal address attachment, e.g. `TONCOIN` attached tag name is comment, the return will be {'comment':'123456'} |
| > txId | String | Hash record of the withdrawal This parameter will return "" for internal transfers. |
| > fee | String | Withdrawal fee amount |
| > feeCcy | String | Withdrawal fee currency, e.g. `USDT` |
| > state | String | Status of withdrawalStage 1 : Pending withdrawal`17`: Pending response from Travel Rule vendor`10`: Waiting transfer`0`: Waiting withdrawal`4`/`5`/`6`/`8`/`9`/`12`: Waiting manual review`7`: ApprovedStage 2 : Withdrawal in progress (Applicable to on-chain withdrawals, internal transfers do not have this stage)`1`: Broadcasting your transaction to chain`15`: Pending transaction validation`16`: Due to local laws and regulations, your withdrawal may take up to 24 hours to arrive`-3`: Canceling Final stage`-2`: Canceled `-1`: Failed`2`: Success |
| > wdId | String | Withdrawal ID |
| > clientId | String | Client-supplied ID |
| > note | String | Withdrawal note |
