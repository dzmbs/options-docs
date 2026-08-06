> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON-RPC API Changelog

> Release notes for the Deribit JSON-RPC API covering new endpoints, parameter changes, subscription updates, and backward-compatibility announcements.

<Update label="Release 21.07.2026">
  A new method [private/get\_currencies](https://docs.deribit.com/api-reference/account-management/private-get_currencies) has been added. It returns a list of cryptocurrencies available for the authenticated user's account.

  The following fields have been added to the Trade and Order objects in order to support the Starbase migration:

  **Trade object**

  | Field                | Description                                                                                                    |
  | -------------------- | -------------------------------------------------------------------------------------------------------------- |
  | `starbase_match_id`  | The unique identifier for a match (trade) in Starbase.<br />Note: This is separate from the standard trade ID. |
  | `starbase_timestamp` | The timestamp of the match (trade) in Starbase, provided in nanosecond precision.                              |

  **Order object**

  | Field                            | Description                                                                                             |
  | -------------------------------- | ------------------------------------------------------------------------------------------------------- |
  | `starbase_order_id`              | The unique identifier for an order in Starbase.<br />Note: This is separate from the standard order ID. |
  | `starbase_last_update_timestamp` | The last-update timestamp of the order in Starbase, provided in nanosecond precision.                   |
</Update>

<Update label="Release 30.06.2026">
  The response of [private/get\_margins](https://docs.deribit.com/api-reference/trading/private-get_margins) now includes fee fields.

  The `underlying_type` field is now returned in [public/get\_instrument](https://docs.deribit.com/api-reference/market-data/public-get_instrument) and [public/get\_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments).
</Update>

<Update label="Release 27.06.2026">
  The response of [private/get\_margins](https://docs.deribit.com/api-reference/trading/private-get_margins) now includes fee fields.

  The `underlying_type` field is now returned in [public/get\_instrument](https://docs.deribit.com/api-reference/market-data/public-get_instrument) and [public/get\_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments).
</Update>

<Update label="Release 19.05.2026">
  As part of our ongoing platform improvements, there are a few minor breaking changes.

  **Editing the mmp flag is no longer supported**

  Passing an `mmp` value that differs from the order's current value is rejected. Passing the same value the order already has continues to be accepted. `private/edit` returns an `Invalid params` error (`-32602`) with `param: mmp` and `reason: "editing mmp flag is not supported"`.

  **Editing a quote-originated order is rejected**

  Attempting to edit a quote-originated order via `private/edit` now returns `order_not_found` (code `10004`). Previously this would cancel the entire quote; now the quote remains open.

  **SMP taker orders may now be cancelled instead of rejected**

  With self-match prevention in reject-taker mode, the taker order may now be cancelled instead of rejected. In both cases the taker does not enter the book and the maker order remains resting. When the taker is cancelled, `cancel_reason` is populated. Affected methods: `private/buy`, `private/sell` and `private/edit`. The `cancel_reason` is `order_overlap` for SMP within the same account and `order_overlap_another_sub` for SMP across subaccounts.
</Update>

<Update label="Release 06.05.2026">
  **Breaking Change — MMP configuration time limits**

  [MMP configuration](https://docs.deribit.com/api-reference/trading/private-set_mmp_config) `interval` and `frozen_time` parameters are now capped at a maximum of 3,600 seconds (1 hour).

  <Warning>
    This change affects existing configurations. Existing configurations exceeding this limit will be automatically migrated to the maximum allowed value.
  </Warning>

  **Instrument creation notification channel**

  New public subscription channel `instrument.creation.<kind>.<currency>` delivers a single notification with full instrument data (same format as [public/get\_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments)) when an instrument is created. The notification fires once at creation time, regardless of the instrument's initial state. Examples: `instrument.creation.any.any` (all instruments), `instrument.creation.future.BTC` (BTC futures only), `instrument.creation.option.any` (all options).

  **Main account trade query access**

  Main accounts are now permitted to call the following methods to retrieve subaccount trade data: `private/get_user_trades_by_instrument`, `private/get_user_trades_by_instrument_and_time`, `private/get_user_trades_by_currency_and_time` and `private/get_user_trades_by_order`. To retrieve trades for a specific subaccount, use the `subaccount_id` parameter.

  **Direct access status in account summary**

  The `is_direct_access_allowed` field has been added to the response of [private/get\_account\_summary](https://docs.deribit.com/api-reference/account-management/private-get_account_summary).

  **Idempotent subaccount transfers**

  An optional `nonce` parameter has been added to [private/withdraw](https://docs.deribit.com/api-reference/wallet/private-withdraw) and `private/submit_transfer_between_subaccounts` for idempotency. Duplicate requests carrying the same `nonce` will be rejected. The `nonce` is persisted on the transaction record and returned in the response.
</Update>

<Update label="Release 24.02.2026">
  New API method: [public/get\_index\_chart\_data](https://docs.deribit.com/api-reference/market-data/public-get_index_chart_data) is now publicly accessible.

  <Warning>
    **Action required:** The deprecated method [private/get\_pending\_block\_trades](https://docs.deribit.com/api-reference/block-trade/private-get_pending_block_trades) will be removed. Please use [private/get\_block\_trade\_requests](https://docs.deribit.com/api-reference/block-trade/private-get_block_trade_requests) instead.
  </Warning>
</Update>

<Update label="Release 13.01.2026">
  **⚠️ New order book lifecycle - BREAKING CHANGE**

  As part of the **Instrument Order Book lifecycle enhancement**, the `state` field in the following methods and channels has been updated:

  **Affected methods:**

  * [/public/get\_instrument](https://docs.deribit.com/api-reference/market-data/public-get_instrument)
  * [/public/get\_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments)
  * [/public/get\_order\_book](https://docs.deribit.com/api-reference/market-data/public-get_order_book)
  * [/public/get\_order\_book\_by\_instrument\_id](https://docs.deribit.com/api-reference/market-data/public-get_order_book_by_instrument_id)
  * [/public/ticker](https://docs.deribit.com/api-reference/market-data/public-ticker)

  **Affected channels:**

  * `incremental_ticker.{instrument_name}`
  * `instrument.state.{kind}.{currency}`
  * `ticker.{instrument_name}.{interval}`

  **Extended pme/simulate method with additional data**

  Extended [private/pme/simulate](https://docs.deribit.com/api-reference/account-management/private-simulate) API response with `pre_aggregated_risk_vectors`, which contain `aggregated_risk_vectors` before applying the `pnl_offset` and `extended_dampener` params.
</Update>

<Update label="Release 16.12.2025">
  `max_quote_quantity` is now required in [/private/set\_mmp\_config](https://docs.deribit.com/api-reference/trading/private-set_mmp_config).

  The precision of MMP configuration limits is restricted to a maximum of four decimal places.

  New fields were added to the responses of [private/get\_account\_summary](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) and [private/get\_account\_summaries](https://docs.deribit.com/api-reference/account-management/private-get_account_summaries):

  * `affiliate_promotion_fee` (if greater than 0.0)
  * `trading_products_details` (which trading products are enabled or can be overwritten for the account)
  * `receive_notifications`

  The `fees` field structure in [private/get\_account\_summary](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) and [private/get\_account\_summaries](https://docs.deribit.com/api-reference/account-management/private-get_account_summaries) has been updated. It is now a list of fee objects for all currency pairs and instrument types related to the currency. This field is visible when parameter `extended` = `true` and the user has any discounts.
</Update>

<Update label="Release 25.11.2025">
  **Breaking Changes**

  Removed deprecated method `public/get_index`. Users are advised to use [/public/get\_index\_price](https://docs.deribit.com/api-reference/market-data/public-get_index_price) instead.

  **Non-Breaking Changes**

  Added `max_quote_quantity` parameter to [private/set\_mmp\_config](https://docs.deribit.com/api-reference/trading/private-set_mmp_config) (when `block_rfq: false`).

  Limited precision of Quantity Limit, Delta Limit and Vega Limit to 4 decimals.
</Update>

<Update label="Release 07.10.2025">
  **Breaking Changes**

  * `fee_precision` field has been removed from the [public/get\_currencies](https://docs.deribit.com/api-reference/market-data/public-get_currencies) method.
</Update>

<Update label="Release 02.09.2025">
  **Non-Breaking Changes**

  Added USDC APR data to [public/get\_currencies](https://docs.deribit.com/api-reference/market-data/public-get_currencies) and [public/get\_apr\_history](https://docs.deribit.com/api-reference/market-data/public-get_apr_history).

  Introduced new method [private/get\_reward\_eligibility](https://docs.deribit.com/api-reference/wallet/private-get_reward_eligibility) returning reward eligibility status and 7-day SMA APR per currency.
</Update>

<Update label="Release 05.08.2025">
  **Breaking Changes**

  API keys with the `account:read` scope can no longer view secrets of other API keys, even if those keys share the same scope. Only API keys with the `account:read_write` scope are now permitted to view API key secrets.

  **Non-Breaking Changes**

  The [public/get\_index\_price\_names](https://docs.deribit.com/api-reference/market-data/public-get_index_price_names) method now provides information regarding the potential creation of future/option combinations for the specified index.

  Added `expires_at` to the [private/verify\_block\_trade](https://docs.deribit.com/api-reference/block-trade/private-verify_block_trade) response.
</Update>

<Update label="Release 01.07.2025">
  **Non-Breaking Changes**

  The `currency` parameter is now optional for the [private/get\_block\_trades](https://docs.deribit.com/api-reference/block-trade/private-get_block_trades) method. If the method is called without specifying a currency, it will return block trades for all available currencies.
</Update>

<Update label="Release 10.06.2025">
  **Breaking Changes**

  Deprecated the `max_show` parameter and introduced `display_amount` to define the visible portion of an iceberg order.

  The [private/buy](https://docs.deribit.com/api-reference/trading/private-buy), [private/sell](https://docs.deribit.com/api-reference/trading/private-sell), and [private/edit](https://docs.deribit.com/api-reference/trading/private-edit) API methods now support the optional `display_amount` parameter.

  Order responses and events for iceberg orders now include `display_amount` (current visible portion) and `refresh_amount` (initially requested display amount).

  <Note>
    `refresh_amount` remains constant throughout the order's lifecycle. It represents the intended size of each iceberg "tip" as it gets replenished. The actual `display_amount` can be lower than `refresh_amount` when the order is partially or nearly fully filled.

    For example, if the total order amount is 10,000, `refresh_amount` is 1,000, and 9,500 has already been filled, the current `display_amount` would be 500 — the remaining visible portion.
  </Note>

  Fee discounts are now returned per currency pair in the responses of [private/get\_account\_summary](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) and [private/get\_account\_summaries](https://docs.deribit.com/api-reference/account-management/private-get_account_summaries).

  Rate limiting for [public/get\_instruments](https://docs.deribit.com/api-reference/market-data/public-get_instruments) on the WebSocket API has been updated: 1 request per 10 seconds, with a burst of 5.

  <Warning>
    To avoid rate limits, we recommend using either the REST requests or the WebSocket subscription to `instrument_state.{kind}.{currency}` for real-time updates.
  </Warning>

  Added a new field `beneficiary_vasp_website` to [private/add\_to\_address\_book](https://docs.deribit.com/api-reference/wallet/private-add_to_address_book), [private/update\_in\_address\_book](https://docs.deribit.com/api-reference/wallet/private-update_in_address_book), and [private/get\_address\_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book). This field is mandatory if the address belongs to a VASP not listed among known VASPs.

  **Non-Breaking Changes**

  Added a new `extra_currencies` parameter to the [private/add\_to\_address\_book](https://docs.deribit.com/api-reference/wallet/private-add_to_address_book) method, allowing a list of valid ERC20 currencies. The `extra_currencies` parameter can only be used when currency is set to an ERC20 and type is set to withdrawal.

  Introduced a new event channel `block_trade_confirmations.{currency}`, which functions like `block_trade_confirmations` but supports filtering by currency for more efficient data handling.
</Update>

<Update label="Release 13.05.2025">
  **Breaking Changes**

  The [public/exchange\_token](https://docs.deribit.com/api-reference/authentication/public-exchange_token) method now supports an optional `scope` parameter. This allows overriding the token scope when creating a new session for a subaccount. Scopes cannot be elevated beyond the caller's permissions. If no `session` scope is provided to [public/exchange\_token](https://docs.deribit.com/api-reference/authentication/public-exchange_token) then the provided `refresh_token` (and corresponding `access_token`) will be invalidated.

  <Warning>
    **Important (Breaking Change)**

    In the previous version, the `scope` parameter wasn't available. As of this release, if no scope is provided, the associated `refresh_token` and `access_token` will be invalidated. When the `scope` parameter is provided to [public/exchange\_token](https://docs.deribit.com/api-reference/authentication/public-exchange_token), the created token will no longer include the `mainaccount` scope.

    This affects all implementations relying on the previous behaviour and may lead to unexpected session terminations if not updated accordingly.

    We recommend explicitly providing a session scope, along with any other required scopes, to both [public/auth](https://docs.deribit.com/api-reference/authentication/public-auth) and [public/exchange\_token](https://docs.deribit.com/api-reference/authentication/public-exchange_token).

    More details about access scopes can be found in our [API documentation](https://docs.deribit.com/articles/access-scope).
  </Warning>

  The methods `private/get_portfolio_margins` and `public/get_portfolio_margins` have now been fully removed from the API, following a period of deprecation.

  <Tip>
    Please head to [private/simulate\_portfolio](https://docs.deribit.com/api-reference/portfolio-margin/private-simulate_portfolio) to perform simulation on current margin models.
  </Tip>

  **Non-Breaking Changes**

  We have introduced a new [public/get\_apr\_history](https://docs.deribit.com/api-reference/market-data/public-get_apr_history) method. This method retrieves historical APR data for a specified currency. This applies to yield-generating tokens, currently including `USDE` and `STETH`.

  The `apr` field has been added to the [public/get\_currencies](https://docs.deribit.com/api-reference/market-data/public-get_currencies) result. It represents the Simple Moving Average (SMA) of the last 7 days of rewards. If there are fewer than 7 days of reward data, the APR is calculated as the average of the available rewards. This applies to yield-generating tokens, currently including `USDE` and `STETH`.
</Update>

<Update label="Release 15.04.2025">
  * An `ip` field has been added to trade type transaction logs in `private/get_transaction_log`.
  * Added `price` parameter to `/private/add_block_rfq_quote` and `/private/edit_block_rfq_quote`. This parameter can be used as aggregated price for quoting future spreads.
  * Added new endpoint [/private/get\_mmp\_status](https://docs.deribit.com/api-reference/trading/private-get_mmp_status) to retrieve MMP status for a triggered index or MMP group.
</Update>

<Update label="Release 01.04.2025">
  * The `public/get_expirations` endpoint now supports filtering by currency pair using the new `currency_pair` parameter.
  * The main account can now use the `subaccount_id` parameter in `private/get_transaction_log` to retrieve the transaction log for a specific subaccount.

  Our API now allows users to retrieve historical trade and order records by utilizing the `historical` parameter. This feature has been added recently and is immediately available. While recent records (30 minutes for orders and 24 hours for trades) can be accessed without this parameter, they are only stored temporarily and eventually removed. After this period, the records are only available through the `historical` parameter.

  The following API endpoints support historical data retrieval:

  * `private/get_order_history_by_instrument`
  * `private/get_order_history_by_currency`
  * `private/get_user_trades_by_instrument`
  * `private/get_user_trades_by_instrument_and_time`
  * `private/get_user_trades_by_currency`
  * `private/get_user_trades_by_currency_and_time`
  * `private/get_user_trades_by_order`

  To retrieve historical trades and orders, use the `historical` parameter in your API request to any of the endpoints listed above:

  * `historical`: `false` → Retrieves recent records (available immediately after execution).
  * `historical`: `true` → Retrieves historical records (available after a short delay for indexing).
</Update>

<Update label="Release 04.02.2025">
  The following methods can be used to manage the withdrawal process:

  * [private/add\_to\_address\_book](https://docs.deribit.com/api-reference/wallet/private-add_to_address_book)
  * [private/update\_in\_address\_book](https://docs.deribit.com/api-reference/wallet/private-update_in_address_book)
  * [private/remove\_from\_address\_book](https://docs.deribit.com/api-reference/wallet/private-remove_from_address_book)
  * [private/get\_address\_book](https://docs.deribit.com/api-reference/wallet/private-get_address_book)
  * [private/set\_clearance\_originator](https://docs.deribit.com/api-reference/wallet/private-set_clearance_originator)
</Update>

<Update label="Release 08.01.2025">
  The following API updates have been added recently and are already available for use:

  * A new transaction type, `options_settlement_summary`, has been added to `/private/get_transaction_log`. This provides realized and unrealized profit and loss for an account's option positions.
  * Deposit originator information can now be submitted using `/private/set_clearance_originator` ([docs](https://docs.deribit.com/api-reference/wallet/private-set_clearance_originator)).
</Update>

<Update label="Release 03.12.2024">
  **Potential breaking change: scientific notation in JSON responses**

  We have updated the JSON formatting of numeric values in our API responses. Starting with this release, some numerical values, such as prices, may be returned in scientific notation. For example, `"strike": 64000` may now be returned as `"strike": 6.4e4`. Our system does not enforce a strict rule for its use, so numeric values may be represented either way. Scientific notation is fully compatible with JSON standards and supported by most modern JSON libraries. Clients are advised to test their implementation against testnet to ensure compatibility.

  **Breaking changes**

  * We have removed the legacy method `private/toggle_portfolio_margining`. Clients are advised to use [private/change\_margin\_model](https://docs.deribit.com/api-reference/account-management/private-change_margin_model) instead.
</Update>

<Update label="Release 08.10.2024">
  A new method [public/get\_expirations](https://docs.deribit.com/api-reference/market-data/public-get_expirations) has been added. It returns a map of all expiration strings for the given currency and instrument kind.

  We added validation to check the tick size of secondary OTO, OCO, and OTOCO orders when they are placed, in addition to the existing validation when they are triggered. Affected methods:

  * `private/buy`
  * `private/sell`
</Update>

<Update label="Release 03.09.2024">
  `private/add_to_address_book` and `private/update_in_address_book`: when executed for one of the ETH/ERC20 supported currencies, we will automatically add or update the address for all other ETH/ERC20 supported currencies.
</Update>

<Update label="Release 03.07.2024">
  **Breaking changes**

  * Added a `settlement_price` field to transaction logs of type delivery in [/private/get\_transaction\_log](https://docs.deribit.com/api-reference/trading/private-get_transaction_log). The `index_price` field now contains the index price instead of the settlement price.
  * `freeze_quotes` will only affect the given currency pair instead of the entire currency when cancelling quotes by currency pair in [/private/cancel\_all\_by\_currency\_pair](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_currency_pair).

  **New**

  * [private/get\_mmp\_config](https://docs.deribit.com/api-reference/trading/private-get_mmp_config) and [private/set\_mmp\_config](https://docs.deribit.com/api-reference/trading/private-set_mmp_config): we now allow `delta_limit` to be greater than `quantity_limit`, and added `vega_limit`.
  * Added `simulated_positions` and `add_positions` to [private/pme/simulate](https://docs.deribit.com/api-reference/portfolio-margin/private-pme-simulate).
</Update>

<Update label="Release 04.06.2024">
  **Breaking changes**

  * Matching engine rate limits: the `matching_engine` field in the `limits` field of [private/get\_account\_summary](https://docs.deribit.com/api-reference/account-management/private-get_account_summary) now contains multiple groups, and for each group there are objects with burst and rate. The `_quotes` rate limits are the rate limits for mass quotes; the `cancel_all` rate limit refers to cancelling all orders; the `spot` limits are the rate limits for spot instruments.
  * Removed the deprecated `stop_price` and `stop_order_id` fields from the responses of [/private/get\_order\_state](https://docs.deribit.com/api-reference/trading/private-get_order_state), `/private/get_open_orders*`, `/private/cancel*` and the `user.orders.*` notification.
  * Removed the deprecated `stop_price` param, which was replaced by `trigger_price`, from [/private/buy](https://docs.deribit.com/api-reference/trading/private-buy), [/private/sell](https://docs.deribit.com/api-reference/trading/private-sell) and `/private/edit*`.
  * Removed the deprecated `stop_id` field from the [/private/get\_trigger\_order\_history](https://docs.deribit.com/api-reference/trading/private-get_trigger_order_history) response.
  * Removed `open_orders_margin` from positions in `user.changes.*` notifications. This field was always zero and hence irrelevant.

  **New**

  * Added block trade approval related endpoints and channel: [/private/get\_pending\_block\_trades](https://docs.deribit.com/api-reference/block-trade/private-get_pending_block_trades), [/private/approve\_block\_trade](https://docs.deribit.com/api-reference/block-trade/private-approve_block_trade), [/private/reject\_block\_trade](https://docs.deribit.com/api-reference/block-trade/private-reject_block_trade) and `block_trade_confirmations`.
  * Added [private/set\_disabled\_trading\_products](https://docs.deribit.com/api-reference/account-management/private-set_disabled_trading_products) to deactivate trading products for specific subaccounts.
  * The `freeze_quotes` parameter has been added to multiple requests. This parameter determines whether incoming quotes should be rejected for 1 second after cancellation. Affected endpoints: [private/cancel\_all](https://docs.deribit.com/api-reference/trading/private-cancel_all), [private/cancel\_all\_by\_kind\_or\_type](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_kind_or_type), [private/cancel\_all\_by\_currency](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_currency), [private/cancel\_all\_by\_instrument](https://docs.deribit.com/api-reference/trading/private-cancel_all_by_instrument) and [private/cancel\_quotes](https://docs.deribit.com/api-reference/trading/private-cancel_quotes).
  * The `mark_iv` field has been added to multiple responses. This field indicates the implied volatility of a mark price and is applicable only to options. Affected endpoints: [public/get\_book\_summary\_by\_currency](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_currency) and [public/get\_book\_summary\_by\_instrument](https://docs.deribit.com/api-reference/market-data/public-get_book_summary_by_instrument).
  * New API endpoint [private/simulate\_portfolio](https://docs.deribit.com/api-reference/portfolio-margin/private-simulate_portfolio) has been added. This new endpoint functions in the same manner as the now deprecated `get_portfolio_margins` endpoints.
  * Added `currency` to the `not_enough_funds_in_currency` API error.
  * Added `index_price` to settlements in [private/get\_transaction\_log](https://docs.deribit.com/api-reference/trading/private-get_transaction_log).
</Update>

<Update label="Release 09.03.2024">
  **Breaking changes**

  * Renamed the `session_bankrupcy` field to `session_bankruptcy` in `/public/get_last_settlements_by_*` and `/private/get_settlement_history_by_*`.
  * `/private/get_transaction_log` will return the Invalid params exception when the `count` parameter is negative.

  **New**

  * The `currency` parameter has been made optional for some methods, and the value `any` is now supported: `/public/get_instruments`, `/public/get_combos` and `/private/get_positions`.
  * Added subscription channel `user.portfolio.any`, which returns notifications for portfolios for all currencies.
  * Added a new API method `/private/get_account_summaries`, which returns all the account summaries for all currencies.
  * Added a new API method `/private/get_open_orders` that returns all open orders for all currencies.
</Update>

<Update label="Release 13.02.2024">
  **Mass Quotes**

  Mass quote functionality allows users to place multiple quotes in a single request, based on the predefined MMP group configuration. Mass Quote functionality is auto-enabled for all accounts with MMP settings activated.

  * Added `private/mass_quote`.
  * Added `private/cancel_quote`.

  **MMP Groups**

  * Added an optional `mmp_group` parameter and response field to `private/get_mmp_config`, `private/reset_mmp` and `private/set_mmp_config`.
  * Added an optional `mmp_group` to the `user.mmp_trigger.{index_name}` channel.

  **Other (non-breaking)**

  * Added XRP and MATIC currencies to multiple API endpoints.
  * `private/get_transaction_log`: added a `contracts` field to see linear USDC option contracts.
  * `private/get_subaccounts`: added a `margin_model` field.
</Update>

<Update label="Release 12.12.2023">
  **Breaking Change**

  When `private/get_subaccounts` is called from a subaccount, the following fields are no longer shown for the main account object: `security_keys_enabled`, `security_keys_assignments`, `proof_id_signature`, `proof_id`, `login_enabled` and `is_password`.

  **Non-breaking change**

  When a new book is started we now first emit the instrument state event and subsequently the ticker events (previously the ticker event was emitted first). Affected channels: `instrument.state.{kind}.{currency}`, `incremental_ticker.{instrument_name}` and `ticker.{instrument_name}.{interval}`.
</Update>

<Update label="Release 07.11.2023">
  * Added support for USDT to multiple API methods and channels. USDT is not yet available in the wallet or for trading until the official launch.
</Update>

<Update label="Release 03.10.2023">
  **MMP — Breaking Changes**

  MMP methods now require the `trade` scope instead of `account`. Affected methods:

  * `private/set_mmp_config` → `trade:read_write`
  * `private/reset_mmp` → `trade:read_write`
  * `private/get_mmp_config` → `trade:read`

  Clients are recommended to add the `trade` scope to current production keys before the release and remove the `account` scope after the release.

  **Liquidation information**

  To avoid sharing potentially price-sensitive data with the market, Deribit has removed the real-time liquidation field for all public trade subscriptions and methods. Clients undergoing liquidation still receive this information via private subscriptions and methods. One hour after a liquidation trade has been executed, the field is made available in public methods so that it remains possible to obtain liquidation statistics. Affected methods: `/public/get_last_trades_by_currency`, `/public/get_last_trades_by_currency_and_time`, `/public/get_last_trades_by_instrument` and `/public/get_last_trades_by_instrument_and_time`. Affected channels: `trades.{instrument_name}.{interval}` and `trades.{kind}.{currency}.{interval}`.
</Update>

<Update label="Release 05.09.2023">
  **Breaking changes**

  * As announced on 1 August, `profit_loss` and `commission` are removed from order objects to further improve platform performance and reduce latencies.
  * Removed `profit_loss` and `commission` from order-related method responses and event notifications.
  * Commissions per trade can still be retrieved using trade methods (e.g. `private/get_user_trades_by_currency`) or from the transaction log ([private/get\_transaction\_log](https://docs.deribit.com/api-reference/trading/private-get_transaction_log)).
</Update>

<Update label="Release 01.08.2023">
  **API changes**

  * Backwards incompatible change for `private/get_position`: for USDC instruments the delta is now in the base currency instead of USDC.
  * New method `public/get_supported_index_names` to list all supported index names (this can, for instance, be used to get all index names supported in MMP).
  * New greeks breakdown for USDC options: `options_gamma_map`, `options_vega_map` and `options_theta_map` are added to `user.portfolio.{currency}` notifications and `private/get_account_summary`.
  * `private/get_account_summary` (with `extended` = `true`) will include `mmp_enabled`: `true` when the user has MMP enabled.
  * `private/edit` will return the cancel reason `edit_post_only_reject` if the edit fails because of `reject_post_only` behavior.

  **MMP: switch from currency to index name**

  MMP configuration switches from a currency-based configuration to an index-name-based one (e.g. `btc_usd` instead of `btc`). Existing currency-based MMP configurations are automatically migrated (`btc` → `btc_usd`, `eth` → `eth_usd`); MMP configuration for SOL and USDC is removed.

  * `private/get_mmp_config`: the `currency` param is replaced with `index_name`. `index_name` is optional; omitting it returns all configured MMP settings. A list is always returned.
  * `private/set_mmp_config`: the `currency` param is replaced with `index_name`. On success, the new configuration is returned instead of "OK".
  * `private/reset_mmp`: the `currency` param is replaced with `index_name`.
  * `user.mmp_trigger.{currency}`: `{currency}` is replaced with `{index_name}`. The `user.mmp_trigger.any` channel is also available.

  **Deprecations**

  * In September we will remove `profit_loss` and `commission` from order objects.
</Update>

<Update label="Release 06.07.2023">
  The instrument object returned in `public/get_instrument` and `public/get_instruments` has two changes:

  * The `tick_size` field represents the new minimum tick size.
  * A new `tick_size_steps` field represents the new price-step validation rules. It is a list of objects `{above_price, tick_size}`, describing that a price above `above_price` should be a multiple of `tick_size`. Multiple price steps are possible.

  An order will be rejected if the price does not conform to the appropriate tick size.
</Update>

<Update label="Release 04.07.2023">
  Allow the main account to read the account summary, trades and positions of a subaccount. To do this, use the `subaccount_id` parameter. Supported methods:

  * `/private/get_account_summary`
  * `/private/get_user_trades_by_currency`
  * `/private/get_positions`
</Update>

<Update label="Release 01.06.2023">
  **Potential Breaking Changes**

  * Block trades returned by the API no longer have the `currency` field. Affected methods: `/private/execute_block_trade`, `/private/get_last_block_trades_by_currency` and `/private/get_block_trade`.
  * `private/verify_block_trade`: changed the error returned when the minimum amount requirement is not satisfied. The response now includes a `minimums` object (for example `btc_future` and `btc_option`) instead of the previous free-text reason.
  * After this release all active sessions will be removed and all API access/refresh tokens will be invalidated (API keys stay valid).

  **New Features**

  * Block trades: spot instruments can be included, and instruments in different currencies can be included in a single block trade.

  **Non-breaking Changes**

  * New block trade IDs are prefixed with `BLOCK`, e.g. `BLOCK-123`. Historical block trades are not affected.
  * The `currency` field is ignored in block trade API methods: `private/execute_block_trade`, `private/verify_block_trade` and `private/simulate_block_trade`.
</Update>

<Update label="Release 20.04.2023">
  **Breaking WS API Changes**

  * Removed `open_interest` from the combo book ticker. Affected endpoint: `public/ticker`. Affected subscriptions: `ticker.{instrument_name}.{interval}` and `incremental_ticker.{instrument_name}`.
  * `private/close_position`: returns an error if the given price is not a multiple of the tick size.
  * The error code `11098` (`account_locked`) is returned when the account is locked.
  * The trade endpoints return an error instead of an empty result if a parameter is invalid (time, trade id, …): `public/get_last_trades_by_currency`, `public/get_last_trades_by_currency_and_time`, `public/get_last_trades_by_instrument`, `public/get_last_trades_by_instrument_and_time`, `private/get_user_trades_by_currency`, `private/get_user_trades_by_currency_and_time`, `private/get_user_trades_by_instrument` and `private/get_user_trades_by_instrument_and_time`.

  **Non-breaking WS API changes**

  * Added `volume_usd` (for options) and `volume_notional` (volume in quote currency, for linear futures) to ticker and book summary. Affected endpoints: `public/ticker`, `public/get_book_summary_by_currency` and `public/get_book_summary_by_instrument`.
  * New endpoints for fetching open orders by label: `private/get_open_orders_by_label` and `private/get_order_state_by_label`.
</Update>

<Update label="Release 22.03.2023">
  **Potentially Breaking Change**

  * `private/get_portfolio_margins` will return an error when called for currency USDC, as Portfolio Margin is not yet available for USDC.

  **WS API changes**

  * Deribit Event Nodes is a new feature created to offload traffic from the retail nodes and to decrease latency. It is dedicated to handling public subscriptions and allows unauthenticated users to subscribe to raw and aggregated market data. To use Event Nodes, change the WebSocket endpoint: for test, use `wss://test.deribit.com/den/ws`; for production, use `wss://streams.deribit.com/ws/api/v2`.
  * `public/get_instrument`: the field `future_type` is deprecated and will be replaced by the new field `instrument_type`.
  * Added optional `start_timestamp` and `end_timestamp` filters to `public/get_last_trades_by_currency`, `public/get_last_trades_by_instrument`, `private/get_user_trades_by_currency` and `private/get_user_trades_by_instrument`.
  * `order` object: new optional `mobile` field (`true` for orders made with the mobile app) and new `cancel_reason` field (the reason the order was canceled). Affected endpoints: `private/get_open_orders_by_currency`, `private/get_open_orders_by_instrument`, `private/get_order_history_by_currency`, `private/get_order_history_by_instrument` and `private/get_order_state`. Affected subscriptions: `user.orders.{kind}.{currency}.raw`, `user.orders.{kind}.{currency}.{interval}`, `user.orders.{instrument_name}.raw`, `user.orders.{instrument_name}.{interval}` and `user.changes.{kind}.{currency}.{interval}`.
</Update>

<Update label="Release 22.02.2023">
  * `/public/get_order_book` and `get_order_book_by_instrument_id`: random numbers for the depth parameter are no longer permitted. Supported depth levels are `[1, 5, 10, 20, 50, 100, 1000, 10000]`. If the depth parameter is not one of the supported levels it will be rounded up to the closest supported level, with a maximum value of 10,000.
  * `private/toggle_portfolio_margining`: the `user_id` parameter is now optional (by default the authenticated user is used). The method is also available for subaccounts, so users that only have access to one of the subaccounts can also switch margin settings from standard to portfolio margining (and vice versa).
  * Fixed a bug that prevented sending combination or strategy orders.
  * Resetting the login password will close all open sessions.
</Update>

<Update label="Release 25.01.2023">
  * New WS API error when an order falls outside the trading bandwidth for futures & perpetual orders (when a bid is higher than the Max Buy or an ask is lower than the Min Sell). Previously these orders were price-adjusted to the Min Sell or Max Buy; as of this release they receive the error `price_too_high` or `price_too_low`.
  * All trades & orders in API results are now always chronologically ordered. Previously these were sorted by order/trade ID, which was not necessarily chronological.
</Update>

<Update label="Release 08.12.2022">
  * Added two numerical fields `block_trade_tick_size` and `block_trade_min_trade_amount` to `/public/get_instruments` and `/public/get_instrument` (WS API).
  * New WS endpoint `private/simulate_block_trade`. This endpoint can be used to verify whether a certain trade would be accepted by Deribit (price trading bandwidth, quantity, margins, risks, and all other platform checks).
  * Margin balance will be equal to equity for PM users in `private/get_account_summary` and `user.portfolio.{currency}` notifications.
  * Direct transfers between sub-accounts are no longer allowed (they can only be done via the main account).
  * Position move: when the price is not specified, the average price of the position (which can be outside the trading bandwidth) is used instead of the instrument mark price.
  * Support for RSA and ed25519 signatures in the API.
</Update>

<Update label="Release 06.10.2022">
  **Potential Breaking Change**

  * Subscribing to instruments that are not open is no longer allowed. This implies clients cannot subscribe to deactivated combo books.
  * Deribit will only allow subscriptions to the `combo_trades` endpoint for combo instruments and rejects the subscription for other instruments.

  **Other changes**

  * Add index price to deposits, withdrawals, transfers and swap logs in the transaction log.
  * Removed the minimum order price on Call Calendar Spread and Put Calendar Spread combos.
  * Allowed the `any` value for the `currency` field in `public/get_rfqs`.
  * Subscription `user.portfolio.{currency}` now also works with `account:read`-scoped API keys (previously it worked only for `trade:read`).
</Update>

<Update label="Release 18.08.2022">
  **Potential Breaking Change**

  * The `deribit_price_ranking.{index_name}` notification now returns `null` values instead of `"undefined"` for unavailable ranking prices.

  **Other changes**

  * Added an initial event for the `deribit_volatility_index` subscription.
  * Increased the limit of whitelisted addresses for API keys.
  * Access for all 3rd party applications is revoked after a password change and requires renewed consent.
  * Added `MMP` and `risk_reducing` flags to the order response object (request responses and subscription notifications).
  * Added `MMP`, `risk_reducing` and `API` flags and an `advanced` field to the private trade response object (request responses and subscription notifications).
  * New field `sid` (session id) in the `public/auth` response, returned for session tokens (scope `session:name`). This allows a user to kill a specific session instead of all sessions.
</Update>

<Update label="Release 06.07.2022">
  * Added `private/toggle_portfolio_margining` method (it existed earlier but was designed only for internal use). Added a `dry_run` parameter to only check the effect of toggling PM — it skips risk checks (returns the portfolio change even if it would otherwise return a `not_enough_funds` error).
  * Added an `interest_value` field to `public/ticker`, `private/get_position` and `private/get_positions` responses and to `incremental_ticker.{instrument_name}`, `ticker.{instrument_name}.{interval}` and `user.changes.*` (in positions) notifications for perpetual instruments.
  * `public/get_instruments` now returns instruments pre-sorted by expiration date and kind (futures before options).
</Update>

<Update label="Release 27.04.2022">
  **Possible Breaking Change**

  * In all notifications from the `platform_state` subscription, the `currency` field has been removed and replaced by a `price_index` field. This enables locking a specific instrument range (e.g. USDC perpetual linked to the ADA index) instead of all instruments within a currency.

  **Other changes**

  * Added field `price_index` with the name of the Price Index used in the instrument to `/public/get_instrument` and `/public/get_instruments` results.
  * New error `move_positions_over_limit` (code `13780`) is returned after a user reaches the allowed number of `private/move_positions` executions.
</Update>

<Update label="Release 31.03.2022">
  * New trailing stop-loss order type: it lets the client set a max drop from the high of an instrument, measured in USD for inverse instruments and USDC for linear instruments. It can be triggered by the same triggers as other triggers (index price, mark price or last price). If the price moves in favor of the client, the trigger level moves up accordingly; once the instrument price falls by the maximum offset value (`trigger_offset`), the position gets stopped out.
  * Added a new `valid_until` parameter (timestamp) to all `private/buy`, `private/sell`, `private/edit` and `private/edit_by_label` requests. The request is only executed if the current server timestamp is lower than the provided value when the request reaches the book; otherwise a `timed_out` error is returned. This feature is not available from the UI.
  * Added a new `/private/send_rfq` request, which sends a notification to market makers or anyone subscribing to the `rfq.{currency}` notification channel or requesting RFQs via `/public/get_rfqs`. The RFQ request is rate limited to 10 per 3 days. Amount and side (buy/sell) are non-compulsory fields.
</Update>

<Update label="Release 23.02.2022">
  * The `platform_state` channel notification has been modified: in addition to existing currency lock notifications, `{"maintenance": true}` data is now sent before moving the platform to maintenance mode during releases.
  * Added the `private/move_positions` method, enabling clients to move full or partial existing positions from a source subaccount to a target subaccount. It is not possible to create new open interest (non-existing positions) using this method. A maximum of 1 position transfer per day per account per currency is allowed (one transfer can consist of multiple positions).
  * Added the following fields to `public/get_instrument` and `public/get_instruments` responses (to facilitate trading of linear instruments): `settlement_currency`, `counter_currency` and `future_type` (futures only; possible values: `linear`, `reversed`).
</Update>

<Update label="Release 15.01.2022">
  * Deribit will no longer allow unauthenticated connections to subscribe to raw book changes (WS users only). Affected subscriptions: `book.{instrument_name}.raw`, `ticker.{instrument_name}.raw`, `trades.{instrument_name}.raw`, `trades.{instrument_kind}.{currency}.raw` and `perpetual.{instrument_name}.raw`. Attempts to subscribe without authentication are rejected with `raw_subscriptions_not_available_for_unauthorized`.
  * Fee coupons/vouchers: a new `fee_balance` field with the current value of the fee balance is added to the response of `private/get_transaction_log` (for every log), to the response of `private/get_account_summary`, and to the `user.portfolio.{currency}` notification.
</Update>

<Update label="Release 22.10.2021">
  * All orders with an invalid quantity or price (not conforming to the tick size) are now rejected instead of being truncated to the minimum granularity. Affected methods: `private/buy`, `private/sell`, `private/edit`, `private/verify_block_trade` and `private/execute_block_trade`.
  * Passing the optional `detailed: true` parameter to `private/cancel_all*` and `private/cancel_by_label` methods changes their response to contain a detailed report of cancelling errors/results.
  * Added a new `user.access_log` subscription; the `private/get_access_log` method has been made visible in the documentation.
  * `private/get_portfolio_margins` can now be used with the `account:read` scope (previously the more restrictive `account:read_write` was required).
  * Complex parameters can now be provided in GET requests as URI-encoded strings (the `trades` parameter in `private/verify_block_trade` and `private/execute_block_trade`).
  * Reversed the sorting of the bids and asks lists generated by the `change` event of the `book.{instrument_name}.{interval}` and `book.{instrument_name}.{group}.{depth}.{interval}` subscription channels.
</Update>

<Update label="Release 21.09.2021">
  **Breaking Changes**

  * Using the `stop` value for the `type` parameter in `/private/cancel_all_by_currency` and `/private/cancel_all_by_instrument` will now result in cancellation of only Stop-Loss orders. To cancel Take-Profit orders, use one of two new values: `take` (only Take-Profit) or `trigger_all` (both Stop-Loss and Take-Profit). `trigger_all` should be used in place of `algo_all`, which is now deprecated and will be removed in future updates.
  * Removed the `initiator_user_id` and `executor_user_id` fields from the response object of `/private/execute_block_trade`, `/private/get_block_trade` and `/private/get_last_block_trades_by_currency`.

  **Other changes**

  * Added an optional `app_name` field to the block trade response object.
  * Added `private/get_daily_withdrawal_limit` and `private/set_daily_withdrawal_limit` (only for reducing the current limit) methods.
  * Added the ability to whitelist an IP range (subnet) for an API Key, for example `126.23.12.x/24`.
  * Added `private/get_portfolio_margins` method, returning portfolio margins for provided simulated positions.
  * Added `private/get_subaccounts_details` method. Affects `/private/get_position` and `/private/get_positions`: added parameter `all_accounts` (default `false`); if set to `true` this returns the positions for all subaccounts.
  * Added an optional `currency` parameter for `private/cancel_by_label` (passing it optimizes execution, but cancels orders only in the selected currency).
  * Added notifications after editing notes in withdrawals, deposits and transfers (`withdrawal.*`, `deposit.*` and `transfer.*` channels).
  * Added the `incremental_ticker.{instrument_name}` subscription. It is more efficient in terms of the number of updates and data sent: it sends a full ticker in the initial event and later only incremental changes between consecutive tickers; it is not sent more than once per second; if nothing changes it is not sent at all (a normal ticker is sent at least every 5 seconds), but if nothing changes for more than 1 minute a full ticker is resent.
  * Clients subscribing to private channels of multiple accounts on the same connection can now receive the assigned label in notification messages.
</Update>

<Update label="Release 25.06.2021">
  * Deribit has enabled sending market-limit orders to be placed as hidden orders.
  * Added new `public/unsubscribe_all` and `private/unsubscribe_all` API endpoints for fast unsubscribing.
  * Optimised the `markprice.options.{index_name}` subscription: the initial event sends all prices and after that only changes are propagated; values are rounded to 4 decimal places (as they were in the initial event before); a `timestamp` field has been added; and the undocumented `synthetic_future` field has been removed.
  * New feature to set a maximum quantity of total short options for non-PM accounts. To notify the client of a breach of this limit, a new API error code `non_pme_total_short_options_positions_size` (code `10037`) is introduced.
</Update>

<Update label="Release 14.05.2021">
  **New features / changes**

  * The instrument descriptive field "quoted currency" for BTC and ETH options has been corrected from USD to the respective currency (BTC or ETH). The actual quoted currency does not change, but this may be a breaking change for some clients. Affected endpoints: `/public/get_instruments`, `/public/get_book_summary_by_currency` and `/public/get_book_summary_by_instrument`.
  * Modified error message text for API error codes: `10034` `stop_price_too_high` → `trigger_price_too_high`; `10035` `stop_price_too_low` → `trigger_price_too_low`; `10044` `stop_price_wrong_tick` → `trigger_price_wrong_tick`; `11036` `invalid_stop_price` → `invalid_trigger_price`.

  **New order types**

  * New order type "Market Limit" (market-to-limit): submitted as a market order to execute at the current best available market price. If only partially filled, the remainder is entered as a limit order with the limit price equal to the price at which the filled portion was executed. Available for all products using the API.
  * New time-in-force order type "Good 'til day" (GTD): a limit order that stays in the book until the end of the session at 8 UTC, when it is automatically cancelled (maximum lifetime up to 24 hrs).
  * New "Take profit" algorithmic orders: order types `take_market` and `take_limit` were added to `/private/buy` and `/private/sell`; order types `algo_all`, `take_all`, `take_market` and `take_limit` were added to the filter lists of `/private/get_open_orders_by_instrument`, `/private/get_open_orders_by_currency` and `/private/get_subaccount_details`.
  * The optional `stop_price` parameter for `/private/buy`, `/private/sell` and `/private/edit` was renamed to `trigger_price`. Fallback to the old parameter name is preserved but will be removed soon.
  * The `trigger_price` field was added to the responses of `/private/buy`, `/private/sell`, `/private/edit` and `/private/get_order_state` as a replacement for `stop_price`.
  * The `stop_id` and `stop_order_id` fields were replaced with `trigger_order_id` in the API response documentation, but remain present in the JSON object for backward compatibility.
  * The `/private/get_stop_order_history` endpoint was renamed to `/private/get_trigger_order_history`. The old one remains for backward compatibility only.

  **Other**

  * New API v2 method `/private/edit_by_label`, which can edit orders that are waiting to be processed. This feature is only available for WebSocket, not FIX.
  * More restrictive instrument validation in APIv1 and APIv2 subscriptions (only "active" instruments allowed); subscribing to expired instruments has been disabled.
  * Added a new public subscription channel `deribit_price_statistics.{index_name}`, which disseminates 24h price index statistics (`low24h`, `high24h` and `change24h` prices), updated every 15 seconds.
</Update>

<Update label="Release 20.03.2021">
  **Breaking changes**

  * Removed `estimated_liquidation_price` from positions in `user.changes.{instrument_name}.{interval}` notifications.
  * In responses of `/private/get_position` and `/private/get_positions`, `estimated_liquidation_price` is now returned as `null` if it has an undefined value (previously `999999.99` was returned in such a case).
  * Renamed the `rpl` and `upl` fields to `session_rpl` and `session_upl` to maintain the same naming convention as in other methods. Documentation was also added for the previously undocumented `/private/get_transaction_log` method.

  **Other changes**

  * Added an `estimated_liquidation_ratio` field to `user.portfolio.{currency}` notifications (returned only for non-PM users). Users can use this ratio to determine the estimated liquidation price of their future positions by multiplying the current position market price by this ratio.
</Update>

<Update label="Release 10.02.2021">
  * New message informing clients when the system is in Maintenance Mode: `{"jsonrpc":"2.0","error":{"message":"system_maintenance","code":11051}}`.
  * Market Maker Protection: a new MMP flag `mmp_cancelled` is available in WS responses and event notifications, indicating that an order was cancelled due to MMP triggering.
</Update>

<Update label="Release 10.11.2020">
  * Due to event pipeline optimisations, clients using the incremental changes subscription may (in a very low-chance scenario) receive redundant events with `change_id <= snapshot change_id` after the initial full book snapshot. Such events should simply be discarded.
</Update>

<Update label="Release 14.10.2020">
  * Canceling an unprocessed order in the manageable request queue now results in a new error code `13666` `request_cancelled_by_user`.
</Update>

<Update label="Release 18.08.2020">
  * A new authorization method has been added for registered applications to generate access tokens using API keys provided by their users (such access token has an additional `app_id: APP_ID` scope).
</Update>

<Update label="Release 22.07.2020">
  * All WS API trade responses have been expanded with a new field `profit_loss` (the same field already present for all orders).
  * Added MMP (Market Maker Protection) functionality, available via the API.
  * `public/get_trade_volumes` is enriched with rolling 7 and 30 days trade volume statistics.
  * Additional fields in `estimated_expiration_price`, `user_portfolio` notifications and the `get_account_summary` method response: `projected_delta_total`, `left_ticks` and `total_ticks`.
</Update>

<Update label="Release 28.05.2020">
  * Added APIv2 methods `private/enable_affiliate_program` and `private/get_affiliate_program_info` to provide details about affiliate status.
  * `public/get_trade_volumes` accepts a new parameter `extended`, which allows receiving statistics for 7 and 30 days.
  * A new mark price field has been added to the trade confirmations for REST and WebSocket (this field is not available in FIX). The field is added in all responses that return a list of trades, i.e. `buy`/`sell`/`edit`/`get_last_trades` and trades events.
</Update>

<Update label="Release 30.04.2020">
  * APIv2 method `private/get_stop_order_history` provides new fields: `order_type`, `label`, `post_only` and `reduce_only`.
</Update>

<Update label="Release 26.03.2020">
  * For API v2 a `price_change` response/notification parameter has been introduced; it reflects the 24-hour asset price change.
  * The API v2 request `private/get_account_summary` has been extended with a `creation_timestamp` field.
</Update>

<Update label="Release 21.01.2020">
  * Added APIv2 method `public/get_delivery_prices`.
  * APIv2 response parameter `position` (for perpetual instruments) includes the field `realized_funding`.
  * APIv2 methods `public/exchange_token` and `public/fork_token` don't accept registered application tokens.
</Update>


## Related topics

- [FIX API Changelog](/changelogs/fix.md)
- [Starbase API Changelog](/changelogs/starbase.md)
- [Starbase API Rate Limits](/starbase/api-rate-limits.md)
- [JSON-RPC 2.0 Protocol](/articles/json-rpc-overview.md)
