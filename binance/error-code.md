- [](/docs/)
- Options Trading
- Error Code
On this page


# Error Codes

Here is the error JSON payload:

```
{
 "code":-1121,
 "msg":"Invalid symbol."
}

```

Errors consist of two parts: an error code and a message.

Codes are universal,but messages can vary.

## 10xx - General Server or Network issues​

### -1000 UNKNOWN​

- An unknown error occurred while processing the request.

### -1001 DISCONNECTED​

- Internal error; unable to process your request. Please try again.

### -1002 UNAUTHORIZED​

- You are not authorized to execute this request.

### -1008 TOO_MANY_REQUESTS​

- Too many requests queued.

- Too much request weight used; please use the websocket for live updates to avoid polling the API.

- Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.

- Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.

### -1014 UNKNOWN_ORDER_COMPOSITION​

- Unsupported order combination.

### -1015 TOO_MANY_ORDERS​

- Too many new orders.

- Too many new orders; current limit is %s orders per %s.

### -1016 SERVICE_SHUTTING_DOWN​

- This service is no longer available.

### -1020 UNSUPPORTED_OPERATION​

- This operation is not supported.

### -1021 INVALID_TIMESTAMP​

- Timestamp for this request is outside of the recvWindow.

- Timestamp for this request was 1000ms ahead of the server's time.

### -1022 INVALID_SIGNATURE​

- Signature for this request is not valid.

## 11xx - 2xxx Request issues​

### -1100 ILLEGAL_CHARS​

- Illegal characters found in a parameter.

- Illegal characters found in a parameter. %s

- Illegal characters found in parameter `%s`; legal range is `%s`.

### -1101 TOO_MANY_PARAMETERS​

- Too many parameters sent for this endpoint.

- Too many parameters; expected `%s` and received `%s`.

- Duplicate values for a parameter detected.

### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED​

- A mandatory parameter was not sent, was empty/null, or malformed.

- Mandatory parameter `%s` was not sent, was empty/null, or malformed.

- Param `%s` or `%s` must be sent, but both were empty/null!

### -1103 UNKNOWN_PARAM​

- An unknown parameter was sent.

### -1104 UNREAD_PARAMETERS​

- Not all sent parameters were read.

- Not all sent parameters were read; read `%s` parameter(s) but was sent `%s`.

### -1105 PARAM_EMPTY​

- A parameter was empty.

- Parameter `%s` was empty.

### -1106 PARAM_NOT_REQUIRED​

- A parameter was sent when not required.

- Parameter `%s` sent when not required.

### -1111 BAD_PRECISION​

- Precision is over the maximum defined for this asset.

### -1115 INVALID_TIF​

- Invalid timeInForce.

### -1116 INVALID_ORDER_TYPE​

- Invalid orderType.

### -1117 INVALID_SIDE​

- Invalid side.

### -1118 EMPTY_NEW_CL_ORD_ID​

- New client order ID was empty.

### -1119 EMPTY_ORG_CL_ORD_ID​

- Original client order ID was empty.

### -1120 BAD_INTERVAL​

- Invalid interval.

### -1121 BAD_SYMBOL​

- Invalid symbol.

### -1125 INVALID_LISTEN_KEY​

- This listenKey does not exist.

### -1127 MORE_THAN_XX_HOURS​

- Lookup interval is too big.

- More than %s hours between startTime and endTime.

### -1128 BAD_CONTRACT​

- Invalid underlying

### -1129 BAD_CURRENCY​

- Invalid asset。

### -1130 INVALID_PARAMETER​

- Invalid data sent for a parameter.

- Data sent for paramter `%s` is not valid.

### -1131 BAD_RECV_WINDOW​

- recvWindow must be less than 60000

### -2010 NEW_ORDER_REJECTED​

- NEW_ORDER_REJECTED

### -2013 NO_SUCH_ORDER​

- Order does not exist.

### -2014 BAD_API_KEY_FMT​

- API-key format invalid.

### -2015 INVALID_API_KEY​

- Invalid API-key, IP, or permissions for action.

### -2018 BALANCE_NOT_SUFFICIENT​

- Balance is insufficient.

### -2027 OPTION_MARGIN_NOT_SUFFICIENT​

- Option margin is insufficient.

## 3xxx-5xxx Filters and other issues​

### -3029 TRANSFER_FAILED​

- Asset transfer fail.

### -4001 PRICE_LESS_THAN_ZERO​

- Price less than 0.

### -4002 PRICE_GREATER_THAN_MAX_PRICE​

- Price greater than max price.

### -4003 QTY_LESS_THAN_ZERO​

- Quantity less than zero.

### -4004 QTY_LESS_THAN_MIN_QTY​

- Quantity less than min quantity.

### -4005 QTY_GREATER_THAN_MAX_QTY​

- Quantity greater than max quantity.

### -4013 PRICE_LESS_THAN_MIN_PRICE​

- Price less than min price.

### -4029 INVALID_TICK_SIZE_PRECISION​

- Tick size precision is invalid.

### -4030 INVALID_QTY_PRECISION​

- Step size precision is invalid.

### -4055 AMOUNT_MUST_BE_POSITIVE​

- Amount must be positive.

### -4056 INVALID_AMOUNT​

- Amount is invalid.

### -4078 OPTIONS_COMMON_ERROR​

- options internal error

### -5001 USER_EXIST​

- Option user already exist

### -5002 USER_NOT_ACCESS​

- Option user not access

### -5003 BAD_INVITE_CODE​

- Invalid invite code

### -5004 USED_INVITE_CODE​

- Invite code has bean used

### -5005 BLACK_COUNTRY​

- Black country

### -5006 ITEMS_EXIST​

- Items '%s' already exist

### -5007 USER_API_EXIST​

- User api already exist

### -5008 KYC_NOT_PASS​

- User kyc not pass

### -5009 IP_COUNTRY_BLACK​

- Restricted jurisdiction ip address

### -5010 NOT_ENOUGH_POSITION​

- User doesn't have enough position to sell

### -6001 INVALID_MMP_WINDOW_TIME_LIMIT​

- Invalid mmp window time limit

### -6002 INVALID_MMP_FROZEN_TIME_LIMIT​

- Invalid mmp frozen time limit

### -6003 INVALID_UNDERLYING​

- Invalid underlying

### -6004 MMP_UNDERLYING_NOT_FOUND​

- Underlying not found

### -6005 IS_NOT_MARKET_MAKER​

- It is not market maker

### -6006 MMP_RULES_NOT_EXISTING​

- Mmp rules are not existing

### -6007 MMP_ERROR_UNKNOWN​

- Mmp unknown error

### -6008 INVALID_LIMIT​

- parameter 'limit' is invalid.

### -6009 INVALID_COUNTDOWN_TIME​

- countdownTime must be no less than 5000 or equal to 0

### -6010 OPEN_INTEREST_ERR_DATA​

- open interest error data.

### -6011 EXCEED_MAXIMUM_BATCH_ORDERS​

- Maximum 10 orders in one batchOrder request.

### -6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS​

- Exceed maximum number of legs in one block order request.

### -6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL​

- Duplicate symbol in one block order request.

### -6014 GRFQ_INVALID_LEGS​

- Invalid legs

### -6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY​

- Quantity is not multiple of minimum quantity

### -6016 GRFQ_QUOTE_NOT_FOUND​

- Quote is not found

### -6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT​

- Not enough quantity left

### -6018 GRFQ_QUOTE_REQUEST_NOT_FOUND​

- Quote request is not found

### -6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME​

- Invalid quote expire time

### -6020 GRFQ_QUOTE_EXPIRED​

- Quote expired

### -6021 GRFQ_INVALID_SIDE​

- Invalid side

### -6022 GRFQ_INVALID_USER​

- Not Global RFQ user

### -6023 SELF_TRADE_PREVENTION​

- Self trade prevention

### -6024 CHANGE_USER_FLAG_FAILED​

- Change user flag failed

### -6025 GRFQ_INVALID_QUOTE_PRICE​

- Invalid quote price

### -6026 INVALID_QTY​

- Invalid qty

### -6027 INVALID_PRICE​

- Invalid price

### -6028 ORDER_IS_FINAL​

- Order is in final state

### -6029 PARAMETER_IS_REQUIRED​

- %s is required

### -6030 INVALID_TIME_INTERVAL​

- Invalid time interval.

### -6031 START_TIME_GREATER_THAN_END_TIME​

- Start time is greater than end time.

### -6032 HAS_OPEN_ORDER​

- Has open order.

### -6033 HAS_NEGATIVE_BALANCE​

- Has negative balance.

### -6034 HAS_POSITION​

- Has position.

### -6035 NO_NEED_TO_CHANGE​

- No need to change.

### -6036 NO_PERMISSION_TO_CHANGE​

- no permission to change.

### -6037 NO_RECORDS_FOUND​

- No records found.

### -6038 SCALE_NOT_MATCH​

- scale not match.

### -6039 INVALID_STEP_SIZE_PRECISION​

- Step size precision is invalid.

### -6040 INVALID_QTYLIMIT_DELTALIMIT​

- Invalid qtyLimit or deltaLimit.

### -6041 START_TRADING_MUST_SLOWLY​

- Start Trading Must Slowly..

### -6042 INDEX_COMMISSION_NOT_MATCH​

- Index Commission Not Match..

### -6043 INDEX_RISKPARAMETER_NOT_MATCH​

- Index RiskParameter Not Match..

### -6044 CLI_ORD_ID_ERROR​

- clientOrderId is duplicated

### -6045 REDUCE_ONLY_REJECT​

- Reduce-only order rejected. The new reduce-only order conflicts with existing open orders. Please cancel the conflicting orders and resubmit.

### -6046 FOK_ORDER_REJECT​

- Due to the order could not be filled immediately, the FOK order has been rejected.

### -6047 GTX_ORDER_REJECT​

- Due to the order could not be executed as maker, the Post Only order will be rejected.

### -6048 INVALID_BLOCK_ORDER​

- Block order parameter is invalid

### -6049 SYMBOL_NOT_TRADING​

- this symbol is not in trading status

### -6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED​

- Maximum open orders reached for this symbol. Please cancel existing orders and try again.

### -6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED​

- Maximum open orders reached for this underlying. Please cancel existing orders and try again.

### -6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED​

- Maximum short position size reached for this symbol

### -6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED​

- Maximum short position size reached for this underlying

### -6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED​

- Quantity greater than max quantity

### -6055 USER_LIQUIDATING​

- User is in liquidation process

### -6056 REDUCE_ONLY_MARGIN_CHECK_FAILED​

- Reduce-only order failed. Your new reduce-only order, when combined with existing same-side open orders, would flip your position and cause insufficient margin. Please cancel those open orders and try again.

### -6057 WRITER_CANT_NAKED_SELL​

- The current symbol is not eligible for option writing.

### -6058 MMP_TRIGGERED​

- MMP triggered. Please reset MMP config

### -6059 USER_IN_LIQUIDATION​

- User is in liquidation process

### -6060 LOCKED_BALANCE_NOT_FOUND​

- OTC order fail due to unable to lock balance

### -6061 LOCKED_OTC_ORDER_NOT_FOUNT​

- OTC order fail due to unable to lock order

### -6062 INVALID_USER_STATUS​

- Operation is not supported for current user status

### -6063 CANCEL_REJECTED​

- Cancel rejected by system
