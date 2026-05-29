## Websocket Trade API

### WS / Place order

You can place an order only if you have sufficient funds.

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the Nitro Spread `Place order` REST API endpoints

Request Example

```
{
 "id": "1512",
 "op": "sprd-order",
 "args": [
 {
 "sprdId":"BTC-USDT_BTC-USDT-SWAP",
 "clOrdId":"b15",
 "side":"buy",
 "ordType":"limit",
 "px":"2.15",
 "sz":"2"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`sprd-order` |
| args | Array of objects | Yes | Request parameters |
| > sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USD-SWAP |
| > clOrdId | String | No | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| > tag | String | No | Order tag A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters. |
| > side | String | Yes | Order side `buy` `sell` |
| > ordType | String | Yes | Order type:`market`: Market order `limit`: Limit order `post_only`: Post-only order `ioc`: Immediate-or-cancel order |
| > sz | String | Yes | Quantity to buy or sell |
| > px | String | Yes | Order price. Only applicable to `limit, post_only, ioc` order. |

##### Successful Response Example

```
{
 "id": "1512",
 "op": "sprd-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "12345689",
 "tag": "",
 "sCode": "0",
 "sMsg": ""
 }
 ],
 "code": "0",
 "msg": ""
}

```

Failure Response Example

```
{
 "id": "1512",
 "op": "sprd-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "",
 "tag": "",
 "sCode": "5XXXX",
 "sMsg": "not exist"
 }
 ],
 "code": "1",
 "msg": ""
}

```

Response Example When Format Error

```
{
 "id": "1512",
 "op": "sprd-order",
 "data": [],
 "code": "60013",
 "msg": "Invalid args"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > tag | String | Order tag |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Rejection or success message of event execution. |

clOrdId

clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.

clOrdId must be unique among the clOrdIds of all pending orders.

### WS / Amend order

Amend an incomplete order.

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the `Amend order` REST API endpoints

Request Example

```
{
 "id":"1512",
 "op":"sprd-amend-order",
 "args":[
 {
 "ordId":"2510789768709120",
 "newSz":"2"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the messageProvided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`sprd-amend-order` |
| args | Array of objects | Yes | Request Parameters |
| > ordId | String | Conditional | Order ID Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used. |
| > clOrdId | String | Conditional | Client Order ID as assigned by the client |
| > reqId | String | No | Client Request ID as assigned by the client for order amendment A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| > newSz | String | Conditional | New quantity after amendment. Either `newSz` or `newPx` is required. When amending a partially-filled order, the newSz should include the amount that has been filled and failed. |
| > newPx | String | Conditional | New price after amendment. |

Successful Response Example

```
{
 "id": "1512",
 "op": "sprd-amend-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "reqId": "b12344",
 "sCode": "0",
 "sMsg": ""
 }
 ],
 "code": "0",
 "msg": ""
}

```

Failure Response Example

```
{
 "id": "1512",
 "op": "sprd-amend-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "reqId": "b12344",
 "sCode": "5XXXX",
 "sMsg": "order not exist"
 }
 ],
 "code": "1",
 "msg": ""
}

```

Response Example When Format Error

```
{
 "id": "1512",
 "op": "sprd-amend-order",
 "data": [],
 "code": "60013",
 "msg": "Invalid args"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > reqId | String | Client Request ID as assigned by the client for order amendment |
| > sCode | String | Order status code, 0 means success |
| > sMsg | String | Order status message |

newSz

If the new quantity of the order is less than or equal to the (accFillSz + canceledSz + pendingSettleSz), after pendingSettleSz is settled, the order status will be transitioned into filled (if canceledSz = 0), or canceled (if canceledSz > 0).

The amend order returns sCode equal to 0

It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query.

### WS / Cancel order

Cancel an incomplete order

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the Nitro Spread `Cancel order` REST API endpoints

Request Example

```
{
 "id": "1514",
 "op": "sprd-cancel-order",
 "args": [
 {
 "ordId": "2510789768709120"
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`sprd-cancel-order` |
| args | Array of objects | Yes | Request Parameters |
| > ordId | String | Conditional | Order ID Either ordId or clOrdId is required, if both are passed, ordId will be used |
| > clOrdId | String | Conditional | Client Order ID as assigned by the client A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |

Successful Response Example

```
{
 "id": "1514",
 "op": "sprd-cancel-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "sCode": "0",
 "sMsg": ""
 }
 ],
 "code": "0",
 "msg": ""
}

```

Failure Response Example

```
{
 "id": "1514",
 "op": "sprd-cancel-order",
 "data": [
 {
 "clOrdId": "",
 "ordId": "2510789768709120",
 "sCode": "5XXXX",
 "sMsg": "Order not exist"
 }
 ],
 "code": "1",
 "msg": ""
}

```

Response Example When Format Error

```
{
 "id": "1514",
 "op": "sprd-cancel-order",
 "data": [],
 "code": "60013",
 "msg": "Invalid args"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > ordId | String | Order ID |
| > clOrdId | String | Client Order ID as assigned by the client |
| > sCode | String | Order status code, `0` means success |
| > sMsg | String | Order status message |

Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the sprd-orders channel or the get order state.

### WS / Cancel all orders

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

Request Example

```
{
 "id": "1512",
 "op": "sprd-mass-cancel",
 "args": [{
 "sprdId": "BTC-USDT_BTC-USDT-SWAP"
 }]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message to identify the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`sprd-mass-cancel` |
| args | Array of objects | Yes | Request parameters |
| > sprdId | String | No | spread ID |

##### Successful Response Example

```
{
 "id": "1512",
 "op": "sprd-mass-cancel",
 "data": [
 {
 "result": true
 }
 ],
 "code": "0",
 "msg": ""
}

```

Response Example When Format Error

```
{
 "id": "1512",
 "op": "sprd-mass-cancel",
 "data": [],
 "code": "60013",
 "msg": "Invalid args"
}

```

#### Response Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the message |
| op | String | Operation |
| code | String | Error Code |
| msg | String | Error message |
| data | Array of objects | Data |
| > result | Boolean | Result of the request `true`, `false` |
