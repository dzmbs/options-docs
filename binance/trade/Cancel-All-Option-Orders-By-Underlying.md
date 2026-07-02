- [](/legacy-docs/)
- Options Trading
- Trade
- Cancel All Option Orders By Underlying
**On this page


# Cancel All Option Orders By Underlying (TRADE)

## API Description​

Cancel all active orders on specified underlying.

## HTTP Request​

DELETE `/eapi/v1/allOpenOrdersByUnderlying`

## Request Weight​

1**

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| underlying | STRING | YES | Option underlying, e.g BTCUSDT |
| recvWindow | LONG | NO | |
| timestamp | LONG | YES | |

## Response Example​

```
{
 "code": 0,
 "msg": "success",
}

```
