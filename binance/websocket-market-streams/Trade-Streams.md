- [](/docs/)
- Options Trading
- Websocket Market Streams
- Trade Streams
**On this page


# Trade Streams

## Stream Description​

The Trade Streams push raw trade information for specific symbol or underlying asset. E.g.[btcusdt@optionTrade](wss://fstream.binance.com/public/stream?streams=btcusdt@optionTrade)

## URL PATH​

`/public`

## Stream Name​

`@optionTrade` or `@optionTrade`

## Update Speed​

50ms**

## Response Example​

```
{
 "e": "trade", // event type
 "E": 1762856064204, // event time
 "T": 1762856064203, // trade completed time
 "s": "BTC-251123-126000-C", // Option trading symbol
 "t": 4, // trade ID
 "p": "1300.000", // price
 "q": "0.1000", // quantity, always positive
 "X": "MARKET", // trade type enum, "MARKET" for Orderbook trading, "BLOCK" for Block trade
 "S": "BUY", // direction
 "m": false // Is the buyer the market maker?
}

```
