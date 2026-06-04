> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer Collateral and Positions [Python / Rust]

Before making API calls, make sure to setup and fund you account in the "Getting Started" guide.

Note there are 3 primary methods of transferring assets on Derive:

1. Transfer Collateral via `private/transfer_ec20` (e.g. USDC, ETH, BTC and etc): see [Transfer Collateral Example](https://github.com/derivexyz/v2-action-signing-python/blob/master/examples/transfer_erc20.py)
2. Transfer a single position via `private/transfer_position` (e.g. ETH-PERP or ETH option): example is WIP but same effect can be achieved by #3
3. Transfer multiple positions via `private/transfer_positions`: e.g. ETH\_PERP + BTC option: see [Transfer Multiple Positions Example](https://github.com/derivexyz/v2-action-signing-python/blob/master/examples/transfer_positions.py)

The above examples use the [Derive Python Action Signing SDK](https://pypi.org/project/derive_action_signing/)  to greatly simplify signing the self-custodial actions and authentication.

<br />

Please refer to our clients for working code:

* Python: [https://github.com/8ball030/derive\_client/blob/main/examples/create\_order.py](https://github.com/8ball030/derive_client/blob/main/examples/create_order.py)
* Rust: [https://github.com/derivexyz/cockpit](https://github.com/derivexyz/cockpit/tree/master/lyra-client)