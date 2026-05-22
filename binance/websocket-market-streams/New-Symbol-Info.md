- [](/docs/)
- Options Trading
- Websocket Market Streams
- New Symbol Info
**On this page


# New Symbol Info

## Stream Description​

New symbol listing stream.

## URL PATH​

`/market`

## Stream Name​

`!optionSymbol`

## Update Speed​

50ms**

## Response Example​

```
{
 "e":"optionSymbol", // Event Type
 "E":1669356423908, // Event Time
 "s":"BTC-250926-140000-C", // Symbol
 "ps":"BTCUSDT", // Underlying index of the contract
 "qa":"USDT", // Quotation asset
 "d":"CALL", // Option type
 "sp":"21000", // Strike price
 "dt":4133404800000, // Delivery date time
 "u":1, // unit, the quantity of the underlying asset represented by a single contract.
 "ot":1569398400000, // onboard date time
 "cs":"TRADING" // Contract status
}

```
