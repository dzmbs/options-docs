> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# private/get_account_summaries

> Retrieves a per-currency list of account summaries for the authenticated user. Each summary includes balance, equity, available funds, and margin information for each currency.

To retrieve summaries for a specific subaccount, use the `subaccount_id` parameter. When the `extended` parameter is set to `true`, additional account details such as account ID, username, email, and account type are included.

**Scope:** `account:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_account_summaries)





## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_account_summaries
openapi: 3.0.0
info:
  title: Deribit API
  version: 2.1.1
servers:
  - url: https://test.deribit.com/api/v2
security: []
tags:
  - name: WebSocket Only
    description: Can only be used over websockets.
  - name: Public
    description: Public methods can be used without authentication.
  - name: Private
    description: >-
      <p>Private methods require authentication. All requests must include a
      valid OAuth2 token.</p>

      <p>A token can be requested using the <a
      href="#public-auth">/public/auth</a> method.</p>

      <p>When using the websockets protocol, the token must be included as a
      parameter <code>access_token</code> in the message. When using REST (HTTP
      GET), the token may also be passed in the <code>Authorization</code>
      header.</p>
  - name: Authentication
  - name: Session Management
  - name: Subscription Management
    description: >-
      Subscription works as [notifications](#notifications), so users will
      automatically (after subscribing) receive messages from the server.
      Overview for each channel response format is described in
      [subscriptions](#subscriptions) section.
  - name: Account Management
  - name: Trading
  - name: Market Data
  - name: Wallet
  - name: Chat
  - name: lsp
    description: >-
      Methods and notifications for the Liquidity Support Program (LSP), the
      mechanism that assigns risk from liquidated positions to designated LSP
      participant subaccounts before falling back to auto-deleveraging (ADL).
paths:
  /private/get_account_summaries:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Retrieves a per-currency list of account summaries for the authenticated
        user. Each summary includes balance, equity, available funds, and margin
        information for each currency.


        To retrieve summaries for a specific subaccount, use the `subaccount_id`
        parameter. When the `extended` parameter is set to `true`, additional
        account details such as account ID, username, email, and account type
        are included.


        **Scope:** `account:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_account_summaries)

      parameters:
        - name: subaccount_id
          in: query
          schema:
            type: integer
          required: false
          description: The user id for the subaccount
        - in: query
          name: extended
          required: false
          schema:
            type: boolean
            example: true
          description: Include additional fields
      requestBody:
        content:
          application/json:
            examples:
              request:
                value:
                  jsonrpc: '2.0'
                  id: 2515
                  method: private/get_account_summaries
                  params:
                    extended: true
                description: JSON-RPC Request Example
        description: JSON-RPC request body
      responses:
        '200':
          $ref: '#/components/responses/PrivateAccountSummariesResponse'
components:
  responses:
    PrivateAccountSummariesResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PrivateAccountSummariesResponse'
          examples:
            response:
              value:
                jsonrpc: '2.0'
                id: 2515
                result:
                  id: 10
                  email: user@example.com
                  system_name: user
                  username: user
                  block_rfq_self_match_prevention: true
                  creation_timestamp: 1687352432143
                  type: main
                  referrer_id: null
                  login_enabled: false
                  security_keys_enabled: false
                  mmp_enabled: false
                  interuser_transfers_enabled: false
                  self_trading_reject_mode: cancel_maker
                  self_trading_extended_to_subaccounts: false
                  summaries:
                    - currency: BTC
                      delta_total_map:
                        btc_usd: 31.594357699
                      margin_balance: 302.62729214
                      futures_session_rpl: -0.03258105
                      options_session_rpl: 0
                      session_upl: 0.05271555
                      options_gamma_map:
                        btc_usd: 0.00001
                      options_vega: 0.0858
                      options_value: -0.0086
                      available_withdrawal_funds: 301.35396172
                      projected_delta_total: 32.613978
                      maintenance_margin: 0.8857841
                      total_pl: -0.33084225
                      limits:
                        limits_per_currency: false
                        non_matching_engine:
                          burst: 1500
                          rate: 1000
                        matching_engine:
                          trading:
                            total:
                              burst: 250
                              rate: 200
                          spot:
                            burst: 250
                            rate: 200
                          quotes:
                            burst: 500
                            rate: 500
                          max_quotes:
                            burst: 10
                            rate: 10
                          guaranteed_quotes:
                            burst: 2
                            rate: 2
                          cancel_all:
                            burst: 250
                            rate: 200
                      projected_maintenance_margin: 0.7543841
                      available_funds: 301.38059622
                      options_delta: -1.01962
                      balance: 302.60065765
                      equity: 302.61869214
                      futures_session_upl: 0.05921555
                      fee_balance: 0
                      options_session_upl: -0.0065
                      projected_initial_margin: 1.01529592
                      options_theta: 15.97071
                      portfolio_margining_enabled: false
                      cross_collateral_enabled: false
                      margin_model: segregated_sm
                      options_vega_map:
                        btc_usd: 0.0858
                      futures_pl: -0.32434225
                      options_pl: -0.0065
                      initial_margin: 1.24669592
                      spot_reserve: 0
                      delta_total: 31.602958
                      options_gamma: 0.00001
                      session_rpl: -0.03258105
                      fees:
                        btc_usd:
                          option:
                            default:
                              type: relative
                              taker: 0.625
                              maker: 0.625
                            block_trade: 0.625
                          perpetual:
                            default:
                              type: fixed
                              taker: 0.00035000000000000005
                              maker: -0.0001
                            block_trade: 0.3
                          future:
                            default:
                              type: fixed
                              taker: 0.00035000000000000005
                              maker: -0.0001
                            block_trade: 0.3
                    - currency: ETH
                      futures_session_upl: 0
                      portfolio_margining_enabled: false
                      available_funds: 99.999598
                      initial_margin: 0.000402
                      futures_session_rpl: 0
                      options_gamma: 0
                      balance: 100
                      options_vega_map: {}
                      session_upl: 0
                      fee_balance: 0
                      delta_total_map:
                        eth_usd: 0
                      projected_maintenance_margin: 0
                      options_gamma_map: {}
                      projected_delta_total: 0
                      margin_model: segregated_sm
                      futures_pl: 0
                      options_theta: 0
                      limits:
                        limits_per_currency: false
                        non_matching_engine:
                          burst: 1500
                          rate: 1000
                        matching_engine:
                          trading:
                            total:
                              burst: 250
                              rate: 200
                          spot:
                            burst: 250
                            rate: 200
                          quotes:
                            burst: 500
                            rate: 500
                          max_quotes:
                            burst: 10
                            rate: 10
                          guaranteed_quotes:
                            burst: 2
                            rate: 2
                          cancel_all:
                            burst: 250
                            rate: 200
                      options_delta: 0
                      equity: 100
                      projected_initial_margin: 0.0002
                      spot_reserve: 0.0002
                      cross_collateral_enabled: false
                      available_withdrawal_funds: 99.999597
                      delta_total: 0
                      options_session_upl: 0
                      maintenance_margin: 0
                      options_theta_map: {}
                      additional_reserve: 0
                      options_pl: 0
                      options_session_rpl: 0
                      options_vega: 0
                      total_pl: 0
                      session_rpl: 0
                      options_value: 0
                      margin_balance: 100
                      fees:
                        eth_usd:
                          option:
                            default:
                              type: relative
                              taker: 0.5
                              maker: 0.5
                            block_trade: 0.5
                          perpetual:
                            default:
                              type: fixed
                              taker: 0.00025
                              maker: -0.00005
                            block_trade: 0.2
                          future:
                            default:
                              type: fixed
                              taker: 0.00025
                              maker: -0.00005
                            block_trade: 0.2
              description: Response example
      description: Success response
  schemas:
    PrivateAccountSummariesResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        result:
          type: object
          properties:
            id:
              type: integer
              example: 12354
              description: Account id (available when parameter `extended` = `true`)
            system_name:
              example: myname
              type: string
              description: >-
                System generated user nickname (available when parameter
                `extended` = `true`)
            username:
              type: string
              example: name
              description: >-
                Account name (given by user) (available when parameter
                `extended` = `true`)
            type:
              enum:
                - main
                - subaccount
              type: string
              description: Account type (available when parameter `extended` = `true`)
            login_enabled:
              type: boolean
              example: false
              description: >-
                Whether account is loginable using email and password (available
                when parameter `extended` = `true` and account is a subaccount)
            email:
              example: support@deribit.com
              type: string
              description: User email (available when parameter `extended` = `true`)
            security_keys_enabled:
              example: false
              type: boolean
              description: >-
                Whether Security Key authentication is enabled (available when
                parameter `extended` = `true`)
            mmp_enabled:
              example: false
              type: boolean
              description: >-
                Whether MMP is enabled (available when parameter `extended` =
                `true`)
            interuser_transfers_enabled:
              type: boolean
              example: false
              description: >-
                `true` when the inter-user transfers are enabled for user
                (available when parameter `extended` = `true`)
            referrer_id:
              type: string
              example: '517.6035'
              description: >-
                Optional identifier of the referrer (of the affiliation program,
                and available when parameter `extended` = `true`), which link
                was used by this account at registration. It coincides with
                suffix of the affiliation link path after `/reg-`
            creation_timestamp:
              type: integer
              example: 1542100802842
              description: >-
                Time at which the account was created (milliseconds since the
                Unix epoch; available when parameter `extended` = `true`)
            self_trading_reject_mode:
              type: string
              description: >-
                Self trading rejection behavior - `reject_taker` or
                `cancel_maker` (available when parameter `extended` = `true`)
            self_trading_extended_to_subaccounts:
              type: string
              description: >-
                `true` if self trading rejection behavior is applied to trades
                between subaccounts (available when parameter `extended` =
                `true`)
            block_rfq_self_match_prevention:
              type: boolean
              example: false
              description: >-
                When enabled, Block RFQ self-match prevention stops RFQ
                execution between accounts under the same legal entity.
                Independent of general self-match prevention (available when
                parameter `extended` = `true`).
            affiliate_promotion_fee:
              type: number
              example: 0
              description: Affiliate promotion fee (if greater than 0.0)
            trading_products_details:
              type: object
              description: >-
                Which trading products are enabled or can be overwritten for the
                account
            receive_notifications:
              type: boolean
              example: false
              description: Whether the account receives notifications
            summaries:
              type: array
              items:
                type: object
                properties:
                  total_pl:
                    example: 0.02032221
                    type: number
                    description: >-
                      Total profit and loss of all open positions since each
                      position was opened (not limited to the current session).
                      Differs from `session_rpl` + `session_upl`, which reset at
                      daily settlement.
                  session_rpl:
                    $ref: '#/components/schemas/rpl'
                  session_upl:
                    $ref: '#/components/schemas/upl'
                  available_funds:
                    example: 2.2638913
                    type: number
                    description: >-
                      Funds available to increase margin usage (open or enlarge
                      positions). Equal to `margin_balance - initial_margin`,
                      floored at `0` in the API response. When initial margin
                      usage exceeds 100%, this is `0` and only reducing orders
                      can be placed. When cross collateral is enabled, this
                      aggregated value is calculated by converting the sum of
                      each cross collateral currency's value to the given
                      currency, using each cross collateral currency's index.
                  available_withdrawal_funds:
                    type: number
                    example: 2.26
                    description: >-
                      Funds available to withdraw in the selected currency.
                      Typically lower than `available_funds` because withdrawals
                      also exclude positive session profit, locked balance,
                      `spot_reserve`, `additional_reserve`, and non-withdrawable
                      external/implied equity components. Always ≥ `0`.
                  margin_balance:
                    type: number
                    example: 2.25
                    description: >-
                      Collateral available against margin requirements. Under
                      standard margin (SM): `equity - options_value` (cash
                      balance plus futures session UPL and RPL). Under portfolio
                      margin (PM): equal to `equity` on a segregated account,
                      and `equity - outstanding_loan_amount` on a cross account.
                      When cross collateral is enabled, this aggregated value is
                      calculated by converting the sum of each cross collateral
                      currency's value to the given currency, using each cross
                      collateral currency's index.
                  balance:
                    example: 3.4906363
                    type: number
                    description: >-
                      The account's cash balance in the selected currency
                      (deposits, withdrawals, transfers, option premiums,
                      settlements/deliveries, corrections, costs, and insurance
                      refills). Does not include open futures PnL or options
                      mark value.
                  spot_reserve:
                    example: 0.3
                    type: number
                    description: The account's balance reserved in active spot orders
                  locked_balance:
                    $ref: '#/components/schemas/locked_balance'
                  additional_reserve:
                    $ref: '#/components/schemas/additional_reserve'
                  fee_balance:
                    $ref: '#/components/schemas/fee_balance'
                  fee_group:
                    type: string
                    description: >-
                      Fee group indicates the level of fee discounts applied to
                      an account. Use `extended`: `true` to view this field. If
                      the field is missing, the account is not assigned to any
                      fee group. **📖 Related Support Article:** [Automatically
                      applied volume based fee
                      discounts](https://support.deribit.com/hc/en-us/articles/25944746248989-Fees#heading-11)
                  currency:
                    example: ETH
                    type: string
                    description: Currency of the summary
                  delta_total:
                    $ref: '#/components/schemas/delta_total'
                  projected_delta_total:
                    $ref: '#/components/schemas/projected_delta_total'
                  delta_total_map:
                    $ref: '#/components/schemas/delta_total_map'
                  deposit_address:
                    example: 14diAAyXL5UzhPTCKC998ch2GV7DMb7yDi
                    type: string
                    description: The deposit address for the account (if available)
                  equity:
                    example: 2.6437733
                    type: number
                    description: >-
                      The account's equity in the selected currency: `balance +
                      futures (session UPL + RPL) + options mark value` (plus
                      any external/implied equity). Related: `margin_balance`
                      excludes options mark value under standard margin.
                  futures_pl:
                    example: 0
                    type: number
                    description: >-
                      Combined profit and loss of all futures and perpetual
                      positions included in `total_pl` (`total_pl -
                      options_pl`).
                  futures_session_rpl:
                    example: 0
                    type: number
                    description: >-
                      Session realized profit and loss for futures and perpetual
                      positions (resets at daily settlement).
                  futures_session_upl:
                    example: 0
                    type: number
                    description: >-
                      Session unrealized profit and loss for open futures and
                      perpetual positions.
                  initial_margin:
                    example: 0.379882
                    type: number
                    description: >-
                      Minimum margin required to open or increase positions
                      (includes margin for open orders). If initial margin usage
                      exceeds 100%, `available_funds` is `0`. When cross
                      collateral is enabled, this aggregated value is calculated
                      by converting the sum of each cross collateral currency's
                      value to the given currency, using each cross collateral
                      currency's index.
                  maintenance_margin:
                    example: 0.1334519
                    type: number
                    description: >-
                      Minimum margin required to keep positions open. If
                      `margin_balance` falls below maintenance margin, positions
                      are liquidated. When cross collateral is enabled, this
                      aggregated value is calculated by converting the sum of
                      each cross collateral currency's value to the given
                      currency, using each cross collateral currency's index.
                  options_delta:
                    example: 0
                    type: number
                    description: >-
                      Sum of the deltas of all options positions. For inverse
                      (coin-margined) options this is the Black-Scholes delta;
                      for linear options it is the index-price-adjusted delta.
                      Unlike account-level `delta_total`, the options mark value
                      is not subtracted.
                  options_gamma:
                    example: 0
                    type: number
                    description: Sum of options position gammas (Black-Scholes).
                  options_pl:
                    example: 0
                    type: number
                    description: >-
                      Combined profit and loss of all options positions included
                      in `total_pl`.
                  options_session_rpl:
                    example: 0
                    type: number
                    description: >-
                      Session realized profit and loss for options positions
                      (resets at daily settlement).
                  options_session_upl:
                    example: 0
                    type: number
                    description: >-
                      Session unrealized profit and loss for open options
                      positions.
                  options_theta:
                    example: 0
                    type: number
                    description: >-
                      Sum of the thetas of all options positions. Theta is
                      expressed per day; for options with less than one day left
                      to expiry it is scaled down to the fraction of a day
                      remaining.
                  options_value:
                    example: 0
                    type: number
                    description: >-
                      Mark value of all open options positions in the selected
                      currency. Under standard margin, `margin_balance = equity
                      - options_value`.
                  options_vega:
                    example: 0
                    type: number
                    description: Sum of options position vegas (Black-Scholes).
                  options_gamma_map:
                    type: object
                    additionalProperties:
                      type: number
                    description: Map of options' gammas per index
                  options_theta_map:
                    type: object
                    additionalProperties:
                      type: number
                    description: Map of options' thetas per index
                  options_vega_map:
                    type: object
                    additionalProperties:
                      type: number
                    description: Map of options' vegas per index
                  projected_initial_margin:
                    $ref: '#/components/schemas/projected_initial_margin'
                  projected_maintenance_margin:
                    $ref: '#/components/schemas/projected_maintenance_margin'
                  close_out_margin:
                    $ref: '#/components/schemas/close_out_margin'
                  projected_close_out_margin:
                    $ref: '#/components/schemas/projected_close_out_margin'
                  portfolio_margining_enabled:
                    type: boolean
                    example: true
                    description: '`true` when portfolio margining is enabled for user'
                  cross_collateral_enabled:
                    type: boolean
                    example: true
                    description: When `true` cross collateral is enabled for user
                  margin_model:
                    type: string
                    example: segregated_sm
                    description: Name of user's currently enabled margin model
                  total_equity_usd:
                    example: 2.6437733
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total equity in all cross collateral currencies,
                      expressed in USD
                  total_initial_margin_usd:
                    example: 0.379882
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total initial margin in all cross collateral
                      currencies, expressed in USD
                  total_maintenance_margin_usd:
                    example: 0.1334519
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total maintenance margin in all cross collateral
                      currencies, expressed in USD
                  total_margin_balance_usd:
                    type: number
                    example: 2.25
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total margin balance in all cross collateral
                      currencies, expressed in USD
                  total_delta_total_usd:
                    type: number
                    example: 1.8
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total delta total in all cross collateral
                      currencies, expressed in USD
                  limits:
                    $ref: '#/components/schemas/api_limits'
                  has_non_block_chain_equity:
                    type: boolean
                    description: >-
                      Optional field returned with value `true` when user has
                      non block chain equity that is excluded from proof of
                      reserve calculations
                  fees:
                    type: object
                    additionalProperties:
                      type: object
                      additionalProperties:
                        type: object
                        properties:
                          default:
                            type: object
                            properties:
                              type:
                                type: string
                                description: Fee calculation type (e.g., fixed, relative)
                              taker:
                                type: number
                                description: Taker fee
                              maker:
                                type: number
                                description: Maker fee
                            required:
                              - type
                              - taker
                              - maker
                          block_trade:
                            type: number
                            description: Block trade fee (if applicable)
                        required:
                          - default
                    description: >-
                      Fee structure for all currency pairs and instrument types
                      related to the currency (available when parameter
                      `extended` = `true` and user has any discounts). Keys are
                      index names (e.g., "btc_usd"), values are objects with
                      instrument types as keys (option, perpetual, future).
                  affiliate_promotion_fee:
                    type: number
                    example: 0
                    description: Affiliate promotion fee (if greater than 0.0)
                  trading_products_details:
                    type: object
                    description: >-
                      Which trading products are enabled or can be overwritten
                      for the account
                  receive_notifications:
                    type: boolean
                    example: false
                    description: Whether the account receives notifications
                required:
                  - equity
                  - currency
                  - maintenance_margin
                  - initial_margin
                  - available_funds
                  - available_withdrawal_funds
                  - balance
                  - session_upl
                  - session_rpl
                  - total_pl
                  - options_pl
                  - options_session_upl
                  - options_session_rpl
                  - options_delta
                  - options_gamma
                  - options_vega
                  - options_value
                  - options_theta
                  - futures_pl
                  - options_gamma_map
                  - options_theta_map
                  - options_vega_map
                  - futures_session_upl
                  - futures_session_rpl
                  - projected_maintenance_margin
                  - delta_total
                  - projected_delta_total
              description: Aggregated list of per-currency account summaries
          required:
            - security_keys_enabled
            - system_name
            - username
            - email
            - type
            - id
      required:
        - result
        - jsonrpc
      type: object
    rpl:
      example: 0.1
      type: number
      description: >-
        Realized profit and loss accrued in the current trading session (since
        the last daily settlement). Resets at each daily settlement.
    upl:
      example: 0.846863
      type: number
      description: >-
        Unrealized profit and loss on open positions in the current trading
        session (since the last daily settlement).
    locked_balance:
      example: 0
      type: number
      description: >-
        Portion of the account balance that is locked and excluded from
        available withdrawal calculations.
    additional_reserve:
      example: 0.3
      type: number
      description: >-
        The account's balance reserved for open buy option orders and option
        combo orders (the premium payable if they fill). Only non-zero on the
        `cross_sm` margin model; balance reserved by spot orders is reported
        separately in `spot_reserve`.
    fee_balance:
      type: number
      description: The account's fee balance (it can be used to pay for fees)
    delta_total:
      example: 0.1334
      type: number
      description: >
        The sum of position deltas. 


        **DeltaTotal = Net Transaction Delta of options + BTC Position of
        Futures**


        The DeltaTotal uses the Net Transaction Delta (or price adjusted Delta)
        of the options, where Net Transaction Delta = Black Scholes Delta - Mark
        Price of Options.


        This is because, from a risk perspective, we are interested in the
        change in Bitcoin price as the underlying changes.


        You should actually treat your delta as **Equity + Delta Total** if you
        want to have less risk for your USD PnL.


        ⚠️ **During the 30 minute settlement period we decay your Delta.** See
        [Delta decay during
        settlement](https://support.deribit.com/hc/en-us/articles/25944751433757-Delta-decay-during-settlement)
        for more details.
    projected_delta_total:
      example: 0.1334
      type: number
      description: >
        The sum of position deltas excluding positions that expire at the
        nearest expiration, so it shows the delta that will remain once those
        positions have expired.

        Calculated on the same Net Transaction Delta basis as `delta_total`,
        including delta decay during the settlement period.
    delta_total_map:
      additionalProperties:
        type: number
      type: object
      description: >
        Map of position delta sums by price index (e.g. `btc_usd`), covering
        both futures and options positions.

        These are raw position deltas: they are not price-adjusted for linear
        instruments and the options mark value is not subtracted.

        They therefore do not add up to `delta_total`, which is calculated on
        the Net Transaction Delta basis described under `delta_total`.
    projected_initial_margin:
      example: 1
      type: number
      description: >
        Initial margin calculated as if instruments expiring at the nearest
        expiration were excluded, so it shows the requirement that will remain
        once those instruments have expired.

        When cross collateral is enabled, this aggregated value is calculated by
        converting the sum of each cross collateral currency's value to the
        given currency, using each cross collateral currency's index.
    projected_maintenance_margin:
      example: 1
      type: number
      description: >
        Maintenance margin calculated as if instruments expiring at the nearest
        expiration were excluded, so it shows the requirement that will remain
        once those instruments have expired.

        When cross collateral is enabled, this aggregated value is calculated by
        converting the sum of each cross collateral currency's value to the
        given currency, using each cross collateral currency's index.
    close_out_margin:
      example: 0
      type: number
      description: >
        Close-out margin threshold in the selected currency, equal to 50% of the
        positional maintenance margin.

        Because it sits below `maintenance_margin`, it marks a later and more
        severe stage than ordinary liquidation: when `margin_balance` falls to
        or below this level, close-out liquidation takes over.

        On a cross account with an outstanding loan it is not exactly half of
        the reported `maintenance_margin`: the loan's maintenance margin is
        included in `maintenance_margin` but excluded from the close-out
        threshold.

        Returned only when close-out margin is enabled on the platform.
    projected_close_out_margin:
      example: 0
      type: number
      description: >
        Close-out margin calculated as if instruments expiring at the nearest
        expiration were excluded, i.e. 50% of the projected positional
        maintenance margin.

        As with `close_out_margin`, the loan maintenance margin counted in
        `projected_maintenance_margin` is excluded here, so on a cross account
        with an outstanding loan the two are not exactly proportional.

        Returned only when close-out margin is enabled on the platform.
    api_limits:
      type: object
      description: >-
        Returned object is described in [separate
        document](https://support.deribit.com/hc/en-us/articles/25944617523357-Rate-Limits).

````

## Related topics

- [private/get_account_summary](/api-reference/account-management/private-get_account_summary.md)
- [JSON-RPC API Changelog](/changelogs/jsonrpc.md)
- [Managing Subaccounts](/articles/managing-subaccounts-api.md)
- [private/get_lsp_usage](/api-reference/lsp/private-get_lsp_usage.md)
- [Rate Limits](/articles/rate-limits.md)
