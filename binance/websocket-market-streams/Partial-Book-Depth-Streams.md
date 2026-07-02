- [](/legacy-docs/)
- Options Trading
- Websocket Market Streams
- Partial Book Depth Streams
**On this page


# Partial Book Depth Streams

## Stream Description​

Top <levels>** bids and asks, Valid levels are **<levels>** are 5, 10, 20.

## URL PATH​

`/public`

## Stream Name​

`@depth@100ms` or `@depth@500ms`

## Update Speed​

**100ms** or **500ms**

## Response Example​

```
{
 "e": "depthUpdate", // event type
 "E": 1762866729459, // event time
 "T": 1762866729358, // transaction time
 "s": "BTC-251123-126000-C", // Option symbol
 "U": 465, // First update ID in event
 "u": 465, // Final update ID in event
 "pu": 464, // Final update Id in last stream(ie `u` in last stream)
 "b": [ // Buy order
 [
 "1100.000", // Price
 "0.6000" // quantity
 ]
 ],
 "a": [ // Sell order
 [
 "1300.000",
 "0.6000"
 ]
 ]
}

```
