- [](/docs/)
- Options Trading
- Websocket Market Streams
- Open Interest
**On this page


# Open Interest

## Stream Description​

Option open interest for specific underlying asset on specific expiration date. E.g.[ethusdt@openInterest@221125](wss://fstream.binance.com/market/stream?streams=ethusdt@openInterest@221125)

## URL PATH​

`/market`

## Stream Name​

`underlying@optionOpenInterest@`

## Update Speed​

60s**

## Response Example​

```
[
 {
 "e":"openInterest", // Event type
 "E":1668759300045, // Event time
 "s":"ETH-221125-2700-C", // option symbol
 "o":"1580.87", // Open interest in contracts
 "h":"1912992.178168204" // Open interest in USDT
 }
]

```
