## Comprehensive API Workflow

Notifications regarding Orders and Trades will be received by both the Taker and the Maker through the WebSocket Notification channels.

A user assumes the role of a *Maker* when their Order is executed upon by another Order. A user becomes a *Taker* when they submit an Order that crosses an existing Order in the Order Book.

### Obtaining Available Spreads

To retrieve all available Spreads for trading on OKX, make a request to the `GET /api/v5/sprd/spreads` endpoint.

### Retrieving Your Orders

To retrieve orders on OKX, make a request to the `GET /api/v5/sprd/order` endpoint.

### Retrieving Your Trades

To retrieve trades on OKX, make a request to the `GET /api/v5/sprd/trades` endpoint.

### Submitting an Order

To submit an order to a Spread's Order Book, make a request to the `POST /api/v5/sprd/order` endpoint.

### Spread States

There are three different states during a Spread's life cycle: `live`, `suspend`, and `expired` as detailed below:

- `live`: Spreads that are actively traded on Nitro Spreads

- `suspend`: Spreads in which at least one of the legs is suspended and the other one is active or suspended on the OKX orderbook exchange; or spreads in which the underlying instruments are still live on the OKX orderbook exchange, but removed from Nitro Spreads

- `expired`: Spreads in which at least one of the underlying instruments is expired on the OKX orderbook exchange

Please refer to the following table for all possible scenarios given the state of the underlying instruments and the resulting state of the spread on Nitro Spreads (except for the case that the spread is delisted on Nitro Spreads):

| Instrument A | Instrument B | Spread State |
| --- | --- | --- |
| Live | Live | Live |
| Suspend | Live | Suspend |
| Live | Suspend | Suspend |
| Suspend | Suspend | Suspend |
| Expired | Live | Expired |
| Live | Expired | Expired |
| Suspend | Expired | Expired |
| Expired | Suspend | Expired |
| Expired | Expired | Expired |

### Trade Lifecycle

In order for a trade to take place, two orders must be crossed within a Spread's Order Book.

Obtain information about the state of an Order and determine if it has reached its final state by monitoring the `sprd-orders`WebSocket channel. The `state` key in the channel indicates the current state of the Order. If the state is `live` or `partially_filled`, it means that the Order still has available size (`sz`) that the creator or another user can take action on. On the other hand, if the state is `canceled` or `filled`, the Order no longer has any available actions that the creator or any other user can take action on.

It is important to closely track the values of the following attributes: `sz`(size),`pendingFillSz` (pending fill size), `canceledSz` (canceled size), and `accFillSz`(accumulated fill size). These attributes provide crucial information regarding the status and progression of the Order.

### Order State

Track the state of an order by subscribing to the `sprd-orders` WebSocket channel.

- Upon submitting an order, whether as a Maker or Taker, an order update message is sent via the orders WebSocket channel. The message will indicate the order's `state` == `live`.

- Order matching and trade settlement are asynchronous processes. When the order is matched but not settled, system pushes `pendingSettleSz` > 0 and `fillSz` == ""

- If the order is partially filled, an order update message is sent with `state` == `partially_filled`.

- In the event that the order is completely filled, an order update message is sent with the `state` == `filled`.

- If the order is not fully filled but has reached its final state, an order update message is sent with the `state` == `canceled`.

- If a certain part of an order is rejected, an order update message is sent with updated `canceledSz` and `pendingFillSz`, and `code` and `msg` corresponding to the error.

### Trade State

Track the state of a trade by subscribing to the `sprd-trades`WebSocket channel.

- After an executed trade undergoes clearing and settlement on OKX, it reaches finality.

- For successfully cleared trades, a WebSocket message is sent with the `state`denoted as `filled`.

- In the case of an unsuccessful trade clearing, a trade update message is sent with the `state` reflected as `rejected`.

- If the trade state is `rejected`, the trade update message will also include the error `code` and a corresponding error message (`msg`) that explains the reason for the rejection.

### All Trades

All users have the ability to receive updates on all trades that take place through the OKX Nitro Spreads product.

It's important to note that OKX Nitro Spreads does not disclose information about the counterparties involved in the trades or the individual `side` (`buy` or `sell`) of the composite legs that were traded.

- By subscribing to the `sprd-public-trades`WebSocket channel, WebSocket messages are sent exclusively for trades that have been successfully cleared and settled.
