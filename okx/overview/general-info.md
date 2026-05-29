## General Info

**The rules for placing orders at the exchange level are as follows:**

- The maximum number of pending orders (including post only orders, limit orders and taker orders that are being processed): 4,000

- The maximum number of pending orders per trading symbol is 500, the limit of 500 pending orders applies to the following **order types**:

Limit

- Market

- Post only

- Fill or Kill (FOK)

- Immediate or Cancel (IOC)

- Market order with Immediate-or-Cancel order (optimal limit IOC)

- Take Profit / Stop Loss (TP/SL)

- Limit and market orders triggered under the order types below:

Take Profit / Stop Loss (TP/SL)

- Trigger

- Trailing stop

- Arbitrage

- Iceberg

- TWAP

- Recurring buy

- The maximum number of pending spread orders: 500 across all spreads

- The maximum number of pending algo orders:

TP/SL order: 100 per instrument

- Trigger order: 500

- Trailing order: 50

- Iceberg order: 100

- TWAP order: 20

- The maximum number of grid trading

Spot grid: 100

- Contract grid: 100

**The rules for trading are as follows:**

- When the number of maker orders matched with a taker order exceeds the maximum number limit of 1000, the taker order will be canceled.

The limit orders will only be executed with a portion corresponding to 1000 maker orders and the remainder will be canceled.

- Fill or Kill (FOK) orders will be canceled directly.

**The rules for the returning data are as follows:**

- `code` and `msg` represent the request result or error reason when the return data has `code`, and has not `sCode`;

- It is `sCode` and `sMsg` that represent the request result or error reason when the return data has `sCode` rather than `code` and `msg`.

**`instFamily` and `uly` parameter explanation:**

- The following explanation is based on the `BTC` contract, other contracts are similar.

- `uly` is the index, like "BTC-USD", and there is a one-to-many relationship with the settlement and margin currency (`settleCcy`).

- `instFamily` is the trading instrument family, like `BTC-USD_UM`, and there is a one-to-one relationship with the settlement and margin currency (`settleCcy`).

- The following table shows the corresponding relationship of `uly`, `instFamily`, `settleCcy` and `instId`.

| Contract Type | uly | instFamily | settleCcy | Delivery contract instId | Swap contract instId |
| --- | --- | --- | --- | --- | --- |
| USDT-margined contract | BTC-USDT | BTC-USDT | USDT | BTC-USDT-250808 | BTC-USDT-SWAP |
| USDC-margined contract | BTC-USDC | BTC-USDC | USDC | BTC-USDC-250808 | BTC-USDC-SWAP |
| USD-margined contract | BTC-USD | BTC-USD_UM | USDⓈ | BTC-USD_UM-250808 | BTC-USD_UM-SWAP |
| Coin-margined contract | BTC-USD | BTC-USD | BTC | BTC-USD-250808 | BTC-USD-SWAP |

Note:

1. USDⓈ represents USD and multiple USD stable coins, like USDC, USDG.

2. The settlement and margin currency refers to the `settleCcy` field returned by the [Get instruments](/docs-v5/en/#trading-account-rest-api-get-instruments) endpoint.
