- [](/docs/)
- Options Trading
- Market Maker Endpoints
- Reset Market Maker Protection Config
**On this page


# Reset Market Maker Protection Config (TRADE)

## API Description​

Reset MMP, start MMP order again.

## HTTP Request​

POST `/eapi/v1/mmpReset`

## Request Weight​

1**

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | TRUE | underlying, e.g BTCUSDT |
| recvWindow | LONG | NO | |
| timestamp | LONG | YES | |

## Response Example​

```
{
 "underlyingId": 2,
 "underlying": "BTCUSDT",
 "windowTimeInMilliseconds": 3000,
 "frozenTimeInMilliseconds": 300000,
 "qtyLimit": "2",
 "deltaLimit": "2.3",
 "lastTriggerTime": 0
}

```
