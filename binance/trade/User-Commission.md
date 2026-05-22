- [](/docs/)
- Options Trading
- Trade
- User Commission
**On this page


# User Commission (USER_DATA)

## API Description​

Get account commission.

## HTTP Request​

GET `/eapi/v1/commission`

## Request Weight​

5**

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| recvWindow | LONG | NO | |
| timestamp | LONG | YES | |

## Response Example​

```
{
 "commissions": [
 {
 "underlying": "BTCUSDT",
 "makerFee": "0.000240",
 "takerFee": "0.000240"
 },
 {
 "underlying": "ETHUSDT",
 "makerFee": "0.000240",
 "takerFee": "0.000240"
 },
 {
 "underlying": "BNBUSDT",
 "makerFee": "0.000240",
 "takerFee": "0.000240"
 },
 {
 "underlying": "SOLUSDT",
 "makerFee": "0.000240",
 "takerFee": "0.000240"
 },
 {
 "underlying": "XRPUSDT",
 "makerFee": "0.000240",
 "takerFee": "0.000240"
 },
 {
 "underlying": "DOGEUSDT",
 "makerFee": "0.000240",
 "takerFee": "0.000240"
 }
 ]
}

```
