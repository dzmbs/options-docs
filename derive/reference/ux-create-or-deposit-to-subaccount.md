> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Subaccount and Deposit

This is the preferred / no-code method for integrating with the Derive exchange.

You may use the user interface to:

* Bridge from Mainnet / OP / Arbitrum / Base
* Deposit / withdraw funds into / from the exchange
* Transfer funds between subaccounts
* Create several subaccounts with different margin types
* Monitor and manage positions / open orders via UX
* Manage session keys (similar to API keys / user session access control)

<br />

## Step 1: Connect Wallet

Load the [www.derive.xyz](http://www.derive.xyz) website and follow the "connect'' wallet flow:

<Image align="center" border={false} src="https://files.readme.io/6558050d7176b8ba896adea67e7127c054662b95811b23d4912e332496f4177f-app.derive.xyz_trade_options_symbolBTC-20251120-100000-C.png" />

You may use "Metamask" if you'd like to onboard via a hardware wallet.

## Step 2: Deposit

Click on the "Deposit" button at the top right of the page. This should open the deposit dialog.

When you make your first deposit to Derive, a Standard Margin subaccount is created automatically.

<Image align="center" border={false} src="https://files.readme.io/81f606fc570333f02796273dff5faf5bff6ce4d76a6091c49e7f8dc1693f6007-app.derive.xyz_trade_options_symbolBTC-20251120-100000-C_1.png" />

Refer to the other guides in [Onboard via Interface](https://docs.derive.xyz/docs/onboard-via-interface) section for other actions.

## Smart-contract Wallets

When onboarding via the UX, Derive creates a smart-contract wallet wrapper around your original Ethereum Wallet. Your wallet still has full control over all actions, however the all funds are owned by the smart contract wallet.

This means when you view transactions on the explorer, transfers / fills / deposits will all appear to happen to this Smart-contract wallet address.

On the [Developers page](https://app.derive.xyz/developers), you can see:

<Image align="center" border={false} src="https://files.readme.io/8dcf7b58fd0d88c8c8fc20cb848ceb280024799a528eb3a310a4f4db7a2a3333-app.derive.xyz_developers.png" />

* Wallet: Your smart contract wallet on Derive's L2, controlled by your signer.
* Signer: Your signer wallet that controls your Derive wallet.