- [](/legacy-docs/)
- Options Trading
- User Data Streams
- Event Account Data
**On this page


# Event: Account data

## Event Description​

Update under the following conditions:

Account deposit or withdrawal
Position info change
Periodic update every 10s when having position

## URL PATH​

`/private`

## Event Name​

`ACCOUNT_UPDATE`

## Update Speed​

50ms**

## Response Example​

```
{
 "stream": "89ljxuL6jFTN3Ej85aYOqH2BYXQ7eeuNYcGm7ktV",
 "data": {
 "e": "ACCOUNT_UPDATE", // Event type
 "E": 1762914568643, // Event time
 "T": 1762914568619, // Transaction Time
 "eq": "10000371.61462086", // account equity in USDT
 "aeq": "10000475.51032086", // account adjusted equity in USDT
 "b": "10000475.51032086", // account wallet balance in USDT
 "m": "-103.89570000", // position value
 "u": "16.10430000", // unrealized pnl
 "i": "32354.38562539", // initial margin in USDT
 "M": "6089.28766956" // maintenance margin in USDT
 }
}

```
