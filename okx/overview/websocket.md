## WebSocket

### Overview

WebSocket is a new HTML5 protocol that achieves full-duplex data transmission between the client and server, allowing data to be transferred effectively in both directions. A connection between the client and server can be established with just one handshake. The server will then be able to push data to the client according to preset rules. Its advantages include:

- The WebSocket request header size for data transmission between client and server is only 2 bytes.

- Either the client or server can initiate data transmission.

- There's no need to repeatedly create and delete TCP connections, saving resources on bandwidth and server.

We recommend developers use WebSocket API to retrieve market data and order book depth.

### Connect

**Connection limit**: 3 requests per second (based on IP)

When subscribing to a public channel, use the address of the public service. When subscribing to a private channel, use the address of the private service

**Request limit**:

The total number of 'subscribe'/'unsubscribe'/'login' requests per connection is limited to 480 times per hour.

If there’s a network problem, the system will automatically disable the connection.
The connection will break automatically if the subscription is not established or data has not been pushed for more than 30 seconds.
To keep the connection stable:
1. Set a timer of N seconds whenever a response message is received, where N is less than 30.
2. If the timer is triggered, which means that no new message is received within N seconds, send the String 'ping'.
3. Expect a 'pong' as a response. If the response message is not received within N seconds, please raise an error or reconnect.

### Connection count limit

The limit will be set at 30 WebSocket connections per specific WebSocket channel per sub-account. Each WebSocket connection is identified by the unique `connId`.

**The WebSocket channels subject to this limitation are as follows:

[Orders channel](/docs-v5/en/#order-book-trading-trade-ws-order-channel)
[Account channel](/docs-v5/en/#trading-account-websocket-account-channel)
[Positions channel](/docs-v5/en/#trading-account-websocket-positions-channel)
[Balance and positions channel](/docs-v5/en/#trading-account-websocket-balance-and-position-channel)
[Position risk warning channel](/docs-v5/en/#trading-account-websocket-position-risk-warning)
[Account greeks channel](/docs-v5/en/#trading-account-websocket-account-greeks-channel)

If users subscribe to the same channel through the same WebSocket connection through multiple arguments, for example, by using `{"channel": "orders", "instType": "ANY"}` and `{"channel": "orders", "instType": "SWAP"}`, it will be counted once only. If users subscribe to the listed channels (such as orders and accounts) using either the same or different connections, it will not affect the counting, as these are considered as two different channels. The system calculates the number of WebSocket connections per channel.

The platform will send the number of active connections to clients through the `channel-conn-count` event message to new channel subscriptions**.

**Connection count update

```
{
 "event":"channel-conn-count",
 "channel":"orders",
 "connCount": "2",
 "connId":"abcd1234"
}

```

When the limit is breached, generally the latest connection that sends the subscription request will be rejected. Client will receive the usual subscription acknowledgement followed by the `channel-conn-count-error` from the connection that the subscription has been terminated. In exceptional circumstances the platform may unsubscribe existing connections.

Connection limit error

```
{
 "event": "channel-conn-count-error",
 "channel": "orders",
 "connCount": "30",
 "connId":"a4d3ae55"
}

```

Order operations through WebSocket, including place, amend and cancel orders, are not impacted through this change.

### Login

Request Example

```
{
 "op": "login",
 "args": [
 {
 "apiKey": "******",
 "passphrase": "******",
 "timestamp": "1538054050",
 "sign": "7L+zFQ+CEgGu5rzCj4+BdV2/uUHGqddA9pI6ztsRRPs="
 }
 ]
}
```

#### Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| op | String | Yes | Operation`login` |
| args | Array of objects | Yes | List of account to login |
| > apiKey | String | Yes | API Key |
| > passphrase | String | Yes | API Key password |
| > timestamp | String | Yes | Unix Epoch time, the unit is seconds |
| > sign | String | Yes | Signature string |

Successful Response Example

```
{
 "event": "login",
 "code": "0",
 "msg": "",
 "connId": "a4d3ae55"
}

```

Failure Response Example

```
{
 "event": "error",
 "code": "60009",
 "msg": "Login failed.",
 "connId": "a4d3ae55"
}

```

#### Response parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| event | String | Yes | Operation`login``error` |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

apiKey**: Unique identification for invoking API. Requires user to apply one manually.

**passphrase**: API Key password

**timestamp**: the Unix Epoch time, the unit is seconds, e.g. 1704876947

**sign**: signature string, the signature algorithm is as follows:

First concatenate `timestamp`, `method`, `requestPath`, strings, then use HMAC SHA256 method to encrypt the concatenated string with SecretKey, and then perform Base64 encoding.

**secretKey**: The security key generated when the user applies for API key, e.g. `22582BD0CFF14C41EDBF1AB98506286D`

**Example of timestamp**: const timestamp = '' + Date.now() / 1,000

**Among sign example**: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+'/users/self/verify', secretKey))

**method**: always 'GET'.

**requestPath** : always '/users/self/verify'

The request will expire 30 seconds after the timestamp. If your server time differs from the API server time, we recommended using the REST API to query the API server time and then set the timestamp.

### Subscribe

**Subscription Instructions**

**Request format description

```
{
 "id": "1512",
 "op": "subscribe",
 "args": [""]
}
```

WebSocket channels are divided into two categories: `public` and `private` channels.

`Public channels` -- No authentication is required, include tickers channel, K-Line channel, limit price channel, order book channel, and mark price channel etc.

`Private channels` -- including account channel, order channel, and position channel, etc -- require log in.

Users can choose to subscribe to one or more channels, and the total length of multiple channels cannot exceed 64 KB.

Below is an example of subscription parameters. The requirement of subscription parameters for each channel is different. For details please refer to the specification of each channels.

Request Example

```
{
 "id": "1512",
 "op":"subscribe",
 "args":[
 {
 "channel":"tickers",
 "instId":"BTC-USDT"
 }
 ]
}
```

Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message Provided by client. It will be returned in response message for identifying the corresponding request. A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters. |
| op | String | Yes | Operation`subscribe` |
| args | Array of objects | Yes | List of subscribed channels |
| > channel | String | Yes | Channel name |
| > instType | String | No | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``ANY` |
| > instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > instId | String | No | Instrument ID |

**Response Example

```
{
 "id": "1512",
 "event": "subscribe",
 "arg": {
 "channel": "tickers",
 "instId": "BTC-USDT"
 },
 "connId": "accb8e21"
}

```

Return parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | No | Unique identifier of the message |
| event | String | Yes | Event`subscribe``error` |
| arg | Object | No | Subscribed channel |
| > channel | String | Yes | Channel name |
| > instType | String | No | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``ANY` |
| > instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |
| connId | String | Yes | WebSocket connection ID |

### Unsubscribe

Unsubscribe from one or more channels.

**Request format description

```
{
 "op": "unsubscribe",
 "args": [" "]
}
```

Request Example

```
{
 "op": "unsubscribe",
 "args": [
 {
 "channel": "tickers",
 "instId": "BTC-USDT"
 }
 ]
}
```

Request parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| op | String | Yes | Operation`unsubscribe` |
| args | Array of objects | Yes | List of channels to unsubscribe from |
| > channel | String | Yes | Channel name |
| > instType | String | No | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION``ANY` |
| > instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > instId | String | No | Instrument ID |

**Response Example

```
{
 "event": "unsubscribe",
 "arg": {
 "channel": "tickers",
 "instId": "BTC-USDT"
 },
 "connId": "d0b44253"
}

```

Response parameters**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| event | String | Yes | Event`unsubscribe``error` |
| arg | Object | No | Unsubscribed channel |
| > channel | String | Yes | Channel name |
| > instType | String | No | Instrument type`SPOT``MARGIN``SWAP``FUTURES``OPTION` |
| > instFamily | String | No | Instrument familyApplicable to `FUTURES`/`SWAP`/`OPTION` |
| > instId | String | No | Instrument ID |
| code | String | No | Error code |
| msg | String | No | Error message |

### Notification

WebSocket has introduced a new message type (event = `notice`).

Client will receive the information in the following scenarios:

- Websocket disconnect for service upgrade

60 seconds prior to the upgrade of the WebSocket service, the notification message will be sent to users indicating that the connection will soon be disconnected.
Users are encouraged to establish a new connection to prevent any disruptions caused by disconnection.

Response Example

```
{
 "event": "notice",
 "code": "64008",
 "msg": "The connection will soon be closed for a service upgrade. Please reconnect.",
 "connId": "a4d3ae55"
}

```

The feature is supported by WebSocket Public (/ws/v5/public) and Private (/ws/v5/private) for now.
