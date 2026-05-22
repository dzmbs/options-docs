- [](/docs/)
- Options Trading
- User Data Streams
- Event Greek Update
On this page


# Event: Greek Update

## Event Description​

`GREEK_UPDATE` will be triggered when a position changes or periodically every 10 seconds when having position.

## URL PATH​

`/private`

## Event Name​

`GREEK_UPDATE`

## Response Example​

```
{
 "e": "GREEK_UPDATE",
 "E": 1762917544216,
 "T": 1762917544216,
 "G": [
 {
 "u": "BTCUSDT",
 "d": "-0.01304097", //delta
 "g": "-0.00000124", //gamma
 "t": "16.11648100", //theta
 "v": "-3.83444011" //vega
 }
 ]
}

```
