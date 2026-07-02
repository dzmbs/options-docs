- [](/legacy-docs/)
- Options Trading
- Market Maker Block Trade
- Cancel Block Trade Order
**On this page


# Cancel Block Trade Order (TRADE)

## API Description​

Cancel a block trade order.

## HTTP Request​

DELETE `eapi/v1/block/order/create`

## Request Weight​

5**

## Request Parameters​

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| blockOrderMatchingKey | STRING | YES | |
| recvWindow | INT | NO | The value cannot be greater than 60000 |
| timestamp | INT | YES | |

## Response Example​

```
{}

```
