# Session Keys

A session key is simply an Ethereum wallet. Account owners can give other Ethereum wallets temporary access to their accounts via session keys. Any Ethereum wallet can be registered as a session key.

# Use-case

For large accounts, session keys are a useful way to give other users temporary access to:

1. Sign `private/` requests (note: always pass in the "derive wallet" of the account in to `X-LyraWallet` and not the session key).
2. Due to the self-custodial nature of the API, the orderbook cannot force withdrawals, transfers or orders without an explicit user signature. Session Keys (and the account owner) can sign payloads for these sensitive requests (e.g. orders, withdrawals, deposits).
3. Session Keys can only deposit and withdraw funds to the original account owner
4. Session keys cannot be used to bridge funds
5. When using the UX to on-board (see "UX Guides"), session keys are the only way to programmatically trade / manage your account.
6. Session keys also allow IP Whitelisting - where users can force session keys to only be used from a list of IPs.

For guides on managing session keys, refer to [Onboard via Interface](https://docs.derive.xyz/docs/onboard-via-interface) and [Onboard Manually](https://docs.derive.xyz/docs/onboard-manually) guides.

<br />

Please refer to our clients for working code:

* Python: [https://github.com/8ball030/derive\_client](https://github.com/8ball030/derive_client)
* Rust: [https://github.com/derivexyz/cockpit](https://github.com/derivexyz/cockpit/tree/master/lyra-client)

<br />

# Scopes

When registering a scoped session key, you have the ability to specify a scope for what that session key can access. For now there are three different scopes for session keys.

1. Admin
   1. This scope gives all permissions to all endpoints. Including trading, depositing/withdrawing, signing orders, and any other API on the system. This scope is applied by default to all session keys that are registered via raw transaction in either the public `register_session_key` endpoint, or the private `register_scoped_session_key` endpoint.
2. Account
   1. This scope can set non-order attributes at an account level. For example, this API can toggle `set_cancel_on_disconnect`, cancel orders, send RFQs, or edit session key attributes.
   2. This scope is not able to deposit, withdraw, trade, or call any other endpoint that requires a `signature` parameter.
   3. This scope includes all permissions from `read_only`.
3. Read only
   1. This scope is responsible for viewing orders, account info, or any other kind of private history. This scope can not edit any attributes of an account, or create any orders.

Each private endpoint is required to inform you of the minimum required scope. For example, If an API requires `account` scope. You can call it with your `admin` or `account` level session keys.