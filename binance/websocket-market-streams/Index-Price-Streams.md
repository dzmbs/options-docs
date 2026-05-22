- [](/docs/)
- Options Trading
- Websocket Market Streams
- Index Price Streams
**On this page


# Index Price Streams

## Stream Description​

Underlying(e.g ETHUSDT) index stream.

## URL PATH​

`/market`
Stream Name:****`!index@arr`

## Update Speed​

1000ms**

## Response Example​

```
[
 {
 "e":"indexPrice",
 "E":1763092572229,
 "s":"ETHUSDT",
 "p":"3224.51976744"
 },
 {
 "e": "indexPrice", // event type
 "E": 1763092572229, // time
 "s": "BTCUSDT", // underlying symbol
 "p": "99102.32326087" // index price
 }
]

```
