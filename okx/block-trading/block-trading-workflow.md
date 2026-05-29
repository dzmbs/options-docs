## Block Trading Workflow

A block trade is a **large sized, privately negotiated** transaction that allows traders to execute spot, perpetuals, futures, options and a combination of instruments (multi leg) which are traded **outside the order book** and at a **mutually agreed price** between the counter-parties. Once the transaction economics have been agreed upon, it will be submitted to OKX to be seamlessly margined, cleared and executed.

**Basic Concepts**

- **RFQs** - Request for Quote sent by the Taker to Maker(s). It captures the quantity, instrument or multi instrument strategy that a Taker wants to trade.

- **Quotes** - Quotes are created by the *Maker* in response to a requested RFQ.

- **Trades** - Trades occur when the *Taker* successfully *executes* upon a makers quote to an RFQ.

**High Level Workflow**

To trade as either Taker or Maker, users need to deposit at least 100,000 USD into their trading account.
In addition, to become a Maker, [Please complete the form to access block trading](https://share.hsforms.com/1mYdfKtJJR3CC03IyCeC6hg3a1fq).

- Taker creates an RFQ and selects which counterparties to broadcast the RFQ to.

- Multiple Maker(s) send a two way quote as a response to the RFQ.

- Taker chooses to execute upon the best quote and the trade is sent to OKX for clearing & settlement.

- Taker & Maker receive confirmation of the trade's execution.

- Trade economics are published to market feed. (minus counterparty info)

**Self-trade Prevention**
Users cannot send RFQ requests to themselves.

**Taker's Perspective**

- Taker creates an RFQ using `POST /api/v5/rfq/create-rfq`. Taker can pull available instruments via `GET /api/v5/public/instruments` and available counterparties from `GET /api/v5/rfq/counterparties`.

- Taker can cancel an RFQ anytime until it becomes inactive with `POST /api/v5/rfq/cancel-rfq`.

- Maker, who is a requested counterparty to the RFQ, and is notified over the `rfqs` WebSocket channel, can provide a Quote to the RFQ.

- Taker, who will be notified of quotes from the `quotes` WebSocket channel, can execute upon the best Quote with `POST /api/v5/rfq/execute-quote`.

- Taker will receive confirmation of the trade's successful execution on the `struc-block-trades` and `rfqs` WebSocket channel.

- Taker will also receive confirmation of the trade being completed on the `public-struc-block-trades` WebSocket channel as well as all other block trades on OKX.

**Maker's Perspective**

- Maker is notified about a new RFQ who they are a counterparty to, on the `rfqs` WebSocket channel.

- Maker can create a one way or two way Quote using `POST /api/v5/rfq/create-quote`.

- Maker can cancel an existing quote anytime until it becomes inactive with `POST /api/v5/rfq/cancel-quote`.

- Taker chooses to execute upon an available Quote.

- Maker will receive updates of their Quote from the `quotes` WebSocket channel.

- Maker will receive confirmation of the successful execution of their Quote from the `struc-block-trades` and `quotes` WebSocket channel.

- Maker will receive confirmation of the trade being completed on the `public-struc-block-trades` WebSocket channel as well as all other block trades on OKX.
