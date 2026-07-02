- [](/legacy-docs/)
- Options Trading
- User Data Streams
- Event Risk Level Change
**On this page


# Event: Risk level change

## Event Description​

Updates whenever there is an account risk level change. The following are possibly values:

NORMAL
REDUCE_ONLY

Note: Risk level changes are only applicable to VIP and Market Makers user accounts. VIP and certain Market Maker accounts will be automatically placed into REDUCE_ONLY mode if their margin balance is insufficient to meet their maintenance margin obligations. Once in REDUCE_ONLY mode, the system will re-evaluate the risk level only upon the following events:

Funds transfer
Trade fill
Option expiry

## URL PATH​

`/private`

## Event Name​

`RISK_LEVEL_CHANGE`

## Update Speed​

50ms**

## Response Example​

```
{
 "e":"RISK_LEVEL_CHANGE", //Event Type
 "E":1587727187525, //Event Time
 "s":"REDUCE_ONLY", //risk level
 "mb":"1534.11708371", //margin balance
 "mm":"254789.11708371" //maintenance margin
}

```
