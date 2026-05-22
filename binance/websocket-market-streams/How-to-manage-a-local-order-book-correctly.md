- [](/docs/)
- Options Trading
- Websocket Market Streams
- How To Manage A Local Order Book Correctly



# How to manage a local order book correctly

- Open a stream to **wss://fstream.binance.com/public/stream?streams=btc-200630-9000-p@depth@100ms**.

- Buffer the events you receive from the stream. For same price, latest received update covers the previous one.

- Get a depth snapshot from **[https://eapi.binance.com/eapi/v1/depth?symbol=btc-200630-9000-p&limit=1000](https://eapi.binance.com/eapi/v1/depth?symbol=btc-200630-9000-p&limit=1000)** .

- Drop any event where `u` is < `lastUpdateId` in the snapshot.

- The first processed event should have `U` `

- U = firstUpdateId (the first update ID) from the WebSocket stream.

- u = finalUpdateId (the last update ID) from the WebSocket stream.

- lastUpdateId = the update ID you got from the REST depth snapshot.

- While listening to the stream, each new event's `pu` should be equal to the previous event's `u`, otherwise initialize the process from step 3.ß

- The data in each event is the **absolute** quantity for a price level.

- If the quantity is 0, **remove** the price level.

- Receiving an event that removes a price level that is not in your local order book can happen and is normal.
