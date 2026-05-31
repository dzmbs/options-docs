## Transaction Timeouts

Orders may not be processed in time due to network delay or busy OKX servers. You can configure the expiry time of the request using `expTime` if you want the order request to be discarded after a specific time.

If `expTime` is specified in the requests for Place (multiple) orders or Amend (multiple) orders, the request will not be processed if the current system time of the server is after the `expTime`.

### REST API

Set the following parameters in the request header

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085` |

The following endpoints are supported:

- [Place order](/docs-v5/en/#order-book-trading-trade-post-place-order)

- [Place multiple orders](/docs-v5/en/#order-book-trading-trade-post-place-multiple-orders)

- [Amend order](/docs-v5/en/#order-book-trading-trade-post-amend-order)

- [Amend multiple orders](/docs-v5/en/#order-book-trading-trade-post-amend-multiple-orders)

- [POST / Place sub order](/docs-v5/en/#order-book-trading-signal-bot-trading-post-place-sub-order) under signal bot trading

Request Example

```
curl -X 'POST' \
 'https://openapi.okx.com/api/v5/trade/order' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -H 'OK-ACCESS-KEY: *****' \
 -H 'OK-ACCESS-SIGN: *****'' \
 -H 'OK-ACCESS-TIMESTAMP: *****'' \
 -H 'OK-ACCESS-PASSPHRASE: *****'' \
 -H 'expTime: 1597026383085' \ // request effective deadline
 -d '{
 "instId": "BTC-USDT",
 "tdMode": "cash",
 "side": "buy",
 "ordType": "limit",
 "px": "1000",
 "sz": "0.01"
}'
```

### WebSocket

The following parameters are set in the request

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| expTime | String | No | Request effective deadline. Unix timestamp format in milliseconds, e.g. `1597026383085` |

The following endpoints are supported:

- [Place order](/docs-v5/en/#order-book-trading-trade-ws-place-order)

- [Place multiple orders](/docs-v5/en/#order-book-trading-trade-ws-place-multiple-orders)

- [Amend order](/docs-v5/en/#order-book-trading-trade-ws-amend-order)

- [Amend multiple orders](/docs-v5/en/#order-book-trading-trade-ws-amend-multiple-orders)

Request Example

```
{
 "id": "1512",
 "op": "order",
 "expTime":"1597026383085", // request effective deadline
 "args": [{
 "side": "buy",
 "instId": "BTC-USDT",
 "tdMode": "isolated",
 "ordType": "market",
 "sz": "100"
 }]
}
```
