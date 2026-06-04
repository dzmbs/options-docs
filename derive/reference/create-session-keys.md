> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Session Keys

For more information on why you need session keys, refer to the "API Reference" > "Session Keys".

Managing session keys via UX can easily be done by going to the ''Session Keys'' section on the [Developers page](https://app.derive.xyz/developers).

<Image align="center" src="https://files.readme.io/60705dc4c0ff2f18f2b7e65374a499fe5455029d1c2295227bc7d0be4d555dff-app.derive.xyz_developers_1.png" />

Session Keys in the UX are broken down into two types. Under the hood, both have the same access rights, however each is stored in a separate manner:

* Developer Session Keys: private keys of these session keys are never stored in in the client nor server. Common use case for this is to register the session key via UX and then use the private key to sign requests in your trading scripts.
* Device Session Keys: created when a user deposits and trades via the UX. To enable instant deposits and trades, a random session private key is generated, registered and encrypted in the browser's local storage. You can manually revoke device session keys below.

You may revoke both developer and device session keys at any time.

<br />

### Logging into UI with Session Key

You may use session keys to both access the API and UI.

<br />

When logging in with a session key into the UI:

1. Import the Session Key into your desired wallet provider (e.g. MetaMask).
2. Click on the "connect" button in the top right.
3. Choose your wallet provider and make sure the account is the Session Key which you imported in step #1.
4. Once you connect, you will see a dropdown menu allowing you to connect as "account" owner or as "session key". Choose the "session key" option.

![](https://files.readme.io/ccf45c9f249a671937402453a1bad24a562a5ba571ec1ceb1da8e3ec0615c138-Screenshot_2026-03-09_at_12.06.17PM.png)

<br />