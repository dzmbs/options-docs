- [](/docs/)
- Options Trading
- Websocket Market Streams
- BookTicker
**On this page


# Individual Symbol Book Ticker Streams

## Stream Description​

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

## URL PATH​

`/public`

## Stream Name​

`@bookTicker`

## Update Speed​

Real-Time**

## Response Example​

```
{
 "e": "bookTicker", // event type
 "u": 2472, // order book updateId
 "s": "BTC-251226-110000-C", // symbol
 "b": "5000.000", // best bid price
 "B": "0.2000", // bid bid quantity
 "a": "5100.000", // best ask price
 "A": "0.1000", // best ask quantity
 "T": 1763041762942, // transaction time
 "E": 1763041762942 // event time
}

```
