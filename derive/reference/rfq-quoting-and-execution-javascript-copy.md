> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# RFQ Quoting and Execution [Python / Rust]

Before making API calls, make sure to setup and fund you account in the "Getting Started" guide.

Similar to orderbook trading, RFQs are "self-custodial", and they require signed messages to be settled. Those signed messages guarantee that all legs of an RFQ will execute at the specified prices and amounts, as well as that the fee charged by the orderbook does not exceed the signed `max_fee`.

Unlike orderbook trading, makers and takers follow different rules and sign slightly different messages in order to complete an RFQ. The full flow is below:

1. **\[Taker & Maker]** Authentication
2. **\[Taker]** Send RFQ
3. **\[Maker]** Listen or poll for RFQs
4. **\[Maker]** In response to an RFQ, sign and send a quote
5. **\[Taker]** Poll for the Quotes (market makers' replies to RFQs) and pick the best one
6. **\[Taker]** Sign an execute message for the selected quote

The [Derive Python Action Signing SDK](https://pypi.org/project/derive_action_signing/)  can be used to help with signing the self-custodial actions as part of the above flow.

For Taker actions (steps 1, 2, 5, 6) refer to the [RFQ execute example](https://github.com/derivexyz/v2-action-signing-python/blob/master/examples/rfq_execute.py)

For Maker actions (steps 1, 3, 4) refer to the [RFQ quote example](https://github.com/derivexyz/v2-action-signing-python/blob/master/examples/rfq_quote.py)

<br />

Please refer to our clients for working code:

* Python: <https://github.com/8ball030/derive_client/blob/main/examples/create_order.py>
* Rust: <https://github.com/derivexyz/cockpit/blob/master/lyra-vaults/src/shared/rfq.rs>