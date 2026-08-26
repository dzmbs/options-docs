> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# user.portfolio.(currency) 

> Real-time notifications for user portfolio information. This subscription provides comprehensive account and portfolio data for the specified currency, including balances, margins, profit and loss, and Greeks.

Each notification includes:

- **Account balances:** Current balance, equity, margin balance, available funds, and available withdrawal funds
- **Margin information:** Initial margin, maintenance margin, and projected margins
- **Profit and Loss:** Total P&L, session unrealized P&L (UPL), session realized P&L (RPL), and separate P&L for options and futures
- **Options Greeks:** Delta, gamma, theta, vega, and options value, with per-index mappings
- **Position data:** Delta total, projected delta total, and delta total map per index
- **Account settings:** Portfolio margining status, cross collateral status, and margin model
- **Cross collateral data:** Total equity, margins, and delta in USD (when cross collateral is enabled)
- **Additional reserves:** Fee balance and additional reserve information

When cross collateral is enabled, aggregated values are calculated by converting the sum of each cross collateral currency's value to the given currency, using each cross collateral currency's index.

Subscribe to a specific currency (BTC, ETH, USDC, USDT, etc.) or use `any` to receive portfolio updates for all currencies.




## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.portfolio.(currency)
id: user.portfolio.(currency)
title: 'user.portfolio.(currency) '
description: >
  Real-time notifications for user portfolio information. This subscription
  provides comprehensive account and portfolio data for the specified currency,
  including balances, margins, profit and loss, and Greeks.


  Each notification includes:


  - **Account balances:** Current balance, equity, margin balance, available
  funds, and available withdrawal funds

  - **Margin information:** Initial margin, maintenance margin, and projected
  margins

  - **Profit and Loss:** Total P&L, session unrealized P&L (UPL), session
  realized P&L (RPL), and separate P&L for options and futures

  - **Options Greeks:** Delta, gamma, theta, vega, and options value, with
  per-index mappings

  - **Position data:** Delta total, projected delta total, and delta total map
  per index

  - **Account settings:** Portfolio margining status, cross collateral status,
  and margin model

  - **Cross collateral data:** Total equity, margins, and delta in USD (when
  cross collateral is enabled)

  - **Additional reserves:** Fee balance and additional reserve information


  When cross collateral is enabled, aggregated values are calculated by
  converting the sum of each cross collateral currency's value to the given
  currency, using each cross collateral currency's index.


  Subscribe to a specific currency (BTC, ETH, USDC, USDT, etc.) or use `any` to
  receive portfolio updates for all currencies.
servers:
  - id: production
    protocol: wss
    host: deribit.com/ws/api/v2
    bindings: []
    variables: []
  - id: testnet
    protocol: wss
    host: test.deribit.com/ws/api/v2
    bindings: []
    variables: []
address: user.portfolio.(currency)
parameters:
  - id: currency
    jsonSchema:
      type: string
      description: |-
        Currency code or `any` for all

        **Allowed values:** `BTC`, `ETH`, `USDC`, `USDT`, `EURR`, `any`
      enum:
        - BTC
        - ETH
        - USDC
        - USDT
        - EURR
        - any
    description: |-
      Currency code or `any` for all

      **Allowed values:** `BTC`, `ETH`, `USDC`, `USDT`, `EURR`, `any`
    type: string
    required: true
    deprecated: false
bindings: []
operations:
  - &ref_2
    id: send_subscribe_user_portfolio_currency
    title: Send subscribe request for user
    description: Client sends subscription request for user updates
    type: send
    messages:
      - &ref_4
        id: subscription_message
        contentType: application/json
        payload:
          - name: Subscription Notification Data
            description: Server sends subscription notification data
            type: object
            properties:
              - name: data
                type: object
                required: true
                properties:
                  - name: currency
                    type: string
                    description: The selected currency
                    required: true
                  - name: equity
                    type: number
                    description: >-
                      The account's equity in the selected currency: `balance +
                      futures (session UPL + RPL) + options mark value` (plus
                      any external/implied equity). Related: `margin_balance`
                      excludes options mark value under standard margin.
                    required: true
                  - name: maintenance_margin
                    type: number
                    description: >-
                      Minimum margin required to keep positions open. If
                      `margin_balance` falls below maintenance margin, positions
                      are liquidated. When cross collateral is enabled, this
                      aggregated value is calculated by converting the sum of
                      each cross collateral currency's value to the given
                      currency, using each cross collateral currency's index.
                    required: true
                  - name: initial_margin
                    type: number
                    description: >-
                      Minimum margin required to open or increase positions
                      (includes margin for open orders). If initial margin usage
                      exceeds 100%, `available_funds` is `0`. When cross
                      collateral is enabled, this aggregated value is calculated
                      by converting the sum of each cross collateral currency's
                      value to the given currency, using each cross collateral
                      currency's index.
                    required: true
                  - name: available_funds
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
                    required: true
                  - name: available_withdrawal_funds
                    type: number
                    description: >-
                      Funds available to withdraw in the selected currency.
                      Typically lower than `available_funds` because withdrawals
                      also exclude positive session profit, locked balance,
                      `spot_reserve`, `additional_reserve`, and non-withdrawable
                      external/implied equity components. Always ≥ `0`.
                    required: true
                  - name: locked_balance
                    type: number
                    description: >-
                      Portion of the account balance that is locked and excluded
                      from available withdrawal calculations.
                    required: false
                  - name: balance
                    type: number
                    description: >-
                      The account's cash balance in the selected currency
                      (deposits, withdrawals, transfers, option premiums,
                      settlements/deliveries, corrections, costs, and insurance
                      refills). Does not include open futures PnL or options
                      mark value.
                    required: true
                  - name: fee_balance
                    type: number
                    description: The account's fee balance (it can be used to pay for fees)
                    required: false
                  - name: margin_balance
                    type: number
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
                    required: true
                  - name: session_upl
                    type: number
                    description: >-
                      Unrealized profit and loss on open positions in the
                      current trading session (since the last daily settlement).
                    required: true
                  - name: session_rpl
                    type: number
                    description: >-
                      Realized profit and loss accrued in the current trading
                      session (since the last daily settlement). Resets at each
                      daily settlement.
                    required: true
                  - name: total_pl
                    type: number
                    description: >-
                      Total profit and loss of all open positions since each
                      position was opened (not limited to the current session).
                      Differs from `session_rpl` + `session_upl`, which reset at
                      daily settlement.
                    required: true
                  - name: options_pl
                    type: number
                    description: >-
                      Combined profit and loss of all options positions included
                      in `total_pl`.
                    required: true
                  - name: options_session_rpl
                    type: number
                    description: >-
                      Session realized profit and loss for options positions
                      (resets at daily settlement).
                    required: true
                  - name: options_session_upl
                    type: number
                    description: >-
                      Session unrealized profit and loss for open options
                      positions.
                    required: true
                  - name: options_delta
                    type: number
                    description: >-
                      Sum of the deltas of all options positions. For inverse
                      (coin-margined) options this is the Black-Scholes delta;
                      for linear options it is the index-price-adjusted delta.
                      Unlike account-level `delta_total`, the options mark value
                      is not subtracted.
                    required: true
                  - name: options_gamma
                    type: number
                    description: Sum of options position gammas (Black-Scholes).
                    required: true
                  - name: options_theta
                    type: number
                    description: >-
                      Sum of the thetas of all options positions. Theta is
                      expressed per day; for options with less than one day left
                      to expiry it is scaled down to the fraction of a day
                      remaining.
                    required: true
                  - name: options_value
                    type: number
                    description: >-
                      Mark value of all open options positions in the selected
                      currency. Under standard margin, `margin_balance = equity
                      - options_value`.
                    required: true
                  - name: options_vega
                    type: number
                    description: Sum of options position vegas (Black-Scholes).
                    required: true
                  - name: futures_pl
                    type: number
                    description: >-
                      Combined profit and loss of all futures and perpetual
                      positions included in `total_pl` (`total_pl -
                      options_pl`).
                    required: true
                  - name: futures_session_rpl
                    type: number
                    description: >-
                      Session realized profit and loss for futures and perpetual
                      positions (resets at daily settlement).
                    required: true
                  - name: futures_session_upl
                    type: number
                    description: >-
                      Session unrealized profit and loss for open futures and
                      perpetual positions.
                    required: true
                  - name: delta_total
                    type: number
                    description: >
                      The sum of position deltas. 


                      **DeltaTotal = Net Transaction Delta of options + BTC
                      Position of Futures**


                      The DeltaTotal uses the Net Transaction Delta (or price
                      adjusted Delta) of the options, where Net Transaction
                      Delta = Black Scholes Delta - Mark Price of Options.


                      This is because, from a risk perspective, we are
                      interested in the change in Bitcoin price as the
                      underlying changes.


                      You should actually treat your delta as **Equity + Delta
                      Total** if you want to have less risk for your USD PnL.


                      ⚠️ **During the 30 minute settlement period we decay your
                      Delta.** See [Delta decay during
                      settlement](https://support.deribit.com/hc/en-us/articles/25944751433757-Delta-decay-during-settlement)
                      for more details.
                    required: false
                  - name: delta_total_map
                    type: object
                    description: >
                      Map of position delta sums by price index (e.g.
                      `btc_usd`), covering both futures and options positions.

                      These are raw position deltas: they are not price-adjusted
                      for linear instruments and the options mark value is not
                      subtracted.

                      They therefore do not add up to `delta_total`, which is
                      calculated on the Net Transaction Delta basis described
                      under `delta_total`.
                    required: true
                  - name: options_gamma_map
                    type: object
                    description: Map of options' gammas per index
                    required: true
                  - name: options_theta_map
                    type: object
                    description: Map of options' thetas per index
                    required: true
                  - name: options_vega_map
                    type: object
                    description: Map of options' vegas per index
                    required: true
                  - name: projected_delta_total
                    type: number
                    description: >
                      The sum of position deltas excluding positions that expire
                      at the nearest expiration, so it shows the delta that will
                      remain once those positions have expired.

                      Calculated on the same Net Transaction Delta basis as
                      `delta_total`, including delta decay during the settlement
                      period.
                    required: true
                  - name: portfolio_margining_enabled
                    type: boolean
                    description: When `true` portfolio margining is enabled for user
                    required: true
                  - name: cross_collateral_enabled
                    type: boolean
                    description: When `true` cross collateral is enabled for user
                    required: true
                  - name: margin_model
                    type: string
                    description: Name of user's currently enabled margin model
                    required: true
                  - name: total_equity_usd
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total equity in all cross collateral currencies,
                      expressed in USD
                    required: false
                  - name: total_initial_margin_usd
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total initial margin in all cross collateral
                      currencies, expressed in USD
                    required: false
                  - name: total_maintenance_margin_usd
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total maintenance margin in all cross collateral
                      currencies, expressed in USD
                    required: false
                  - name: total_margin_balance_usd
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total margin balance in all cross collateral
                      currencies, expressed in USD
                    required: false
                  - name: total_delta_total_usd
                    type: number
                    description: >-
                      Optional (only for users using cross margin). The
                      account's total delta total in all cross collateral
                      currencies, expressed in USD
                    required: false
                  - name: projected_initial_margin
                    type: number
                    description: >
                      Initial margin calculated as if instruments expiring at
                      the nearest expiration were excluded, so it shows the
                      requirement that will remain once those instruments have
                      expired.

                      When cross collateral is enabled, this aggregated value is
                      calculated by converting the sum of each cross collateral
                      currency's value to the given currency, using each cross
                      collateral currency's index.
                    required: false
                  - name: projected_maintenance_margin
                    type: number
                    description: >
                      Maintenance margin calculated as if instruments expiring
                      at the nearest expiration were excluded, so it shows the
                      requirement that will remain once those instruments have
                      expired.

                      When cross collateral is enabled, this aggregated value is
                      calculated by converting the sum of each cross collateral
                      currency's value to the given currency, using each cross
                      collateral currency's index.
                    required: true
                  - name: close_out_margin
                    type: number
                    description: >
                      Close-out margin threshold in the selected currency, equal
                      to 50% of the positional maintenance margin.

                      Because it sits below `maintenance_margin`, it marks a
                      later and more severe stage than ordinary liquidation:
                      when `margin_balance` falls to or below this level,
                      close-out liquidation takes over.

                      On a cross account with an outstanding loan it is not
                      exactly half of the reported `maintenance_margin`: the
                      loan's maintenance margin is included in
                      `maintenance_margin` but excluded from the close-out
                      threshold.

                      Returned only when close-out margin is enabled on the
                      platform.
                    required: false
                  - name: projected_close_out_margin
                    type: number
                    description: >
                      Close-out margin calculated as if instruments expiring at
                      the nearest expiration were excluded, i.e. 50% of the
                      projected positional maintenance margin.

                      As with `close_out_margin`, the loan maintenance margin
                      counted in `projected_maintenance_margin` is excluded
                      here, so on a cross account with an outstanding loan the
                      two are not exactly proportional.

                      Returned only when close-out margin is enabled on the
                      platform.
                    required: false
                  - name: additional_reserve
                    type: number
                    description: >-
                      The account's balance reserved for open buy option orders
                      and option combo orders (the premium payable if they
                      fill). Only non-zero on the `cross_sm` margin model;
                      balance reserved by spot orders is reported separately in
                      `spot_reserve`.
                    required: false
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              type: object
              properties:
                currency:
                  type: string
                  description: The selected currency
                  example: ETH
                  x-parser-schema-id: <anonymous-schema-318>
                equity:
                  type: number
                  description: >-
                    The account's equity in the selected currency: `balance +
                    futures (session UPL + RPL) + options mark value` (plus any
                    external/implied equity). Related: `margin_balance` excludes
                    options mark value under standard margin.
                  example: 2.6437733
                  x-parser-schema-id: <anonymous-schema-319>
                maintenance_margin:
                  type: number
                  description: >-
                    Minimum margin required to keep positions open. If
                    `margin_balance` falls below maintenance margin, positions
                    are liquidated. When cross collateral is enabled, this
                    aggregated value is calculated by converting the sum of each
                    cross collateral currency's value to the given currency,
                    using each cross collateral currency's index.
                  example: 0.1334519
                  x-parser-schema-id: <anonymous-schema-320>
                initial_margin:
                  type: number
                  description: >-
                    Minimum margin required to open or increase positions
                    (includes margin for open orders). If initial margin usage
                    exceeds 100%, `available_funds` is `0`. When cross
                    collateral is enabled, this aggregated value is calculated
                    by converting the sum of each cross collateral currency's
                    value to the given currency, using each cross collateral
                    currency's index.
                  example: 0.379882
                  x-parser-schema-id: <anonymous-schema-321>
                available_funds:
                  type: number
                  description: >-
                    Funds available to increase margin usage (open or enlarge
                    positions). Equal to `margin_balance - initial_margin`,
                    floored at `0` in the API response. When initial margin
                    usage exceeds 100%, this is `0` and only reducing orders can
                    be placed. When cross collateral is enabled, this aggregated
                    value is calculated by converting the sum of each cross
                    collateral currency's value to the given currency, using
                    each cross collateral currency's index.
                  example: 2.2638913
                  x-parser-schema-id: <anonymous-schema-322>
                available_withdrawal_funds:
                  type: number
                  description: >-
                    Funds available to withdraw in the selected currency.
                    Typically lower than `available_funds` because withdrawals
                    also exclude positive session profit, locked balance,
                    `spot_reserve`, `additional_reserve`, and non-withdrawable
                    external/implied equity components. Always ≥ `0`.
                  example: 2.26
                  x-parser-schema-id: <anonymous-schema-323>
                locked_balance:
                  description: >-
                    Portion of the account balance that is locked and excluded
                    from available withdrawal calculations.
                  type: number
                  example: 0
                  x-parser-schema-id: <anonymous-schema-324>
                balance:
                  type: number
                  description: >-
                    The account's cash balance in the selected currency
                    (deposits, withdrawals, transfers, option premiums,
                    settlements/deliveries, corrections, costs, and insurance
                    refills). Does not include open futures PnL or options mark
                    value.
                  example: 3.4906363
                  x-parser-schema-id: <anonymous-schema-325>
                fee_balance:
                  description: The account's fee balance (it can be used to pay for fees)
                  type: number
                  x-parser-schema-id: <anonymous-schema-326>
                margin_balance:
                  type: number
                  description: >-
                    Collateral available against margin requirements. Under
                    standard margin (SM): `equity - options_value` (cash balance
                    plus futures session UPL and RPL). Under portfolio margin
                    (PM): equal to `equity` on a segregated account, and `equity
                    - outstanding_loan_amount` on a cross account. When cross
                    collateral is enabled, this aggregated value is calculated
                    by converting the sum of each cross collateral currency's
                    value to the given currency, using each cross collateral
                    currency's index.
                  example: 2.25
                  x-parser-schema-id: <anonymous-schema-327>
                session_upl:
                  description: >-
                    Unrealized profit and loss on open positions in the current
                    trading session (since the last daily settlement).
                  type: number
                  example: 0.846863
                  x-parser-schema-id: <anonymous-schema-328>
                session_rpl:
                  description: >-
                    Realized profit and loss accrued in the current trading
                    session (since the last daily settlement). Resets at each
                    daily settlement.
                  type: number
                  example: 0.1
                  x-parser-schema-id: <anonymous-schema-329>
                total_pl:
                  type: number
                  description: >-
                    Total profit and loss of all open positions since each
                    position was opened (not limited to the current session).
                    Differs from `session_rpl` + `session_upl`, which reset at
                    daily settlement.
                  example: 0.02032221
                  x-parser-schema-id: <anonymous-schema-330>
                options_pl:
                  type: number
                  description: >-
                    Combined profit and loss of all options positions included
                    in `total_pl`.
                  example: 0
                  x-parser-schema-id: <anonymous-schema-331>
                options_session_rpl:
                  type: number
                  description: >-
                    Session realized profit and loss for options positions
                    (resets at daily settlement).
                  example: 0
                  x-parser-schema-id: <anonymous-schema-332>
                options_session_upl:
                  type: number
                  description: >-
                    Session unrealized profit and loss for open options
                    positions.
                  example: 0
                  x-parser-schema-id: <anonymous-schema-333>
                options_delta:
                  type: number
                  description: >-
                    Sum of the deltas of all options positions. For inverse
                    (coin-margined) options this is the Black-Scholes delta; for
                    linear options it is the index-price-adjusted delta. Unlike
                    account-level `delta_total`, the options mark value is not
                    subtracted.
                  example: 0
                  x-parser-schema-id: <anonymous-schema-334>
                options_gamma:
                  type: number
                  description: Sum of options position gammas (Black-Scholes).
                  example: 0
                  x-parser-schema-id: <anonymous-schema-335>
                options_theta:
                  type: number
                  description: >-
                    Sum of the thetas of all options positions. Theta is
                    expressed per day; for options with less than one day left
                    to expiry it is scaled down to the fraction of a day
                    remaining.
                  example: 0
                  x-parser-schema-id: <anonymous-schema-336>
                options_value:
                  type: number
                  description: >-
                    Mark value of all open options positions in the selected
                    currency. Under standard margin, `margin_balance = equity -
                    options_value`.
                  example: 0
                  x-parser-schema-id: <anonymous-schema-337>
                options_vega:
                  type: number
                  description: Sum of options position vegas (Black-Scholes).
                  example: 0
                  x-parser-schema-id: <anonymous-schema-338>
                futures_pl:
                  type: number
                  description: >-
                    Combined profit and loss of all futures and perpetual
                    positions included in `total_pl` (`total_pl - options_pl`).
                  example: 0
                  x-parser-schema-id: <anonymous-schema-339>
                futures_session_rpl:
                  type: number
                  description: >-
                    Session realized profit and loss for futures and perpetual
                    positions (resets at daily settlement).
                  example: 0
                  x-parser-schema-id: <anonymous-schema-340>
                futures_session_upl:
                  type: number
                  description: >-
                    Session unrealized profit and loss for open futures and
                    perpetual positions.
                  example: 0
                  x-parser-schema-id: <anonymous-schema-341>
                delta_total:
                  description: >
                    The sum of position deltas. 


                    **DeltaTotal = Net Transaction Delta of options + BTC
                    Position of Futures**


                    The DeltaTotal uses the Net Transaction Delta (or price
                    adjusted Delta) of the options, where Net Transaction Delta
                    = Black Scholes Delta - Mark Price of Options.


                    This is because, from a risk perspective, we are interested
                    in the change in Bitcoin price as the underlying changes.


                    You should actually treat your delta as **Equity + Delta
                    Total** if you want to have less risk for your USD PnL.


                    ⚠️ **During the 30 minute settlement period we decay your
                    Delta.** See [Delta decay during
                    settlement](https://support.deribit.com/hc/en-us/articles/25944751433757-Delta-decay-during-settlement)
                    for more details.
                  example: 0.1334
                  type: number
                  x-parser-schema-id: <anonymous-schema-342>
                delta_total_map:
                  description: >
                    Map of position delta sums by price index (e.g. `btc_usd`),
                    covering both futures and options positions.

                    These are raw position deltas: they are not price-adjusted
                    for linear instruments and the options mark value is not
                    subtracted.

                    They therefore do not add up to `delta_total`, which is
                    calculated on the Net Transaction Delta basis described
                    under `delta_total`.
                  type: object
                  additionalProperties:
                    type: number
                    x-parser-schema-id: <anonymous-schema-344>
                  x-parser-schema-id: <anonymous-schema-343>
                options_gamma_map:
                  type: object
                  description: Map of options' gammas per index
                  x-parser-schema-id: <anonymous-schema-345>
                options_theta_map:
                  type: object
                  description: Map of options' thetas per index
                  x-parser-schema-id: <anonymous-schema-346>
                options_vega_map:
                  type: object
                  description: Map of options' vegas per index
                  x-parser-schema-id: <anonymous-schema-347>
                projected_delta_total:
                  description: >
                    The sum of position deltas excluding positions that expire
                    at the nearest expiration, so it shows the delta that will
                    remain once those positions have expired.

                    Calculated on the same Net Transaction Delta basis as
                    `delta_total`, including delta decay during the settlement
                    period.
                  example: 0.1334
                  type: number
                  x-parser-schema-id: <anonymous-schema-348>
                portfolio_margining_enabled:
                  type: boolean
                  description: When `true` portfolio margining is enabled for user
                  example: true
                  x-parser-schema-id: <anonymous-schema-349>
                cross_collateral_enabled:
                  type: boolean
                  description: When `true` cross collateral is enabled for user
                  example: true
                  x-parser-schema-id: <anonymous-schema-350>
                margin_model:
                  type: string
                  description: Name of user's currently enabled margin model
                  example: segregated_sm
                  x-parser-schema-id: <anonymous-schema-351>
                total_equity_usd:
                  type: number
                  description: >-
                    Optional (only for users using cross margin). The account's
                    total equity in all cross collateral currencies, expressed
                    in USD
                  example: 2.6437733
                  x-parser-schema-id: <anonymous-schema-352>
                total_initial_margin_usd:
                  type: number
                  description: >-
                    Optional (only for users using cross margin). The account's
                    total initial margin in all cross collateral currencies,
                    expressed in USD
                  example: 0.379882
                  x-parser-schema-id: <anonymous-schema-353>
                total_maintenance_margin_usd:
                  type: number
                  description: >-
                    Optional (only for users using cross margin). The account's
                    total maintenance margin in all cross collateral currencies,
                    expressed in USD
                  example: 0.1334519
                  x-parser-schema-id: <anonymous-schema-354>
                total_margin_balance_usd:
                  type: number
                  description: >-
                    Optional (only for users using cross margin). The account's
                    total margin balance in all cross collateral currencies,
                    expressed in USD
                  example: 2.25
                  x-parser-schema-id: <anonymous-schema-355>
                total_delta_total_usd:
                  type: number
                  description: >-
                    Optional (only for users using cross margin). The account's
                    total delta total in all cross collateral currencies,
                    expressed in USD
                  example: 1.8
                  x-parser-schema-id: <anonymous-schema-356>
                projected_initial_margin:
                  description: >
                    Initial margin calculated as if instruments expiring at the
                    nearest expiration were excluded, so it shows the
                    requirement that will remain once those instruments have
                    expired.

                    When cross collateral is enabled, this aggregated value is
                    calculated by converting the sum of each cross collateral
                    currency's value to the given currency, using each cross
                    collateral currency's index.
                  example: 1
                  type: number
                  x-parser-schema-id: <anonymous-schema-357>
                projected_maintenance_margin:
                  description: >
                    Maintenance margin calculated as if instruments expiring at
                    the nearest expiration were excluded, so it shows the
                    requirement that will remain once those instruments have
                    expired.

                    When cross collateral is enabled, this aggregated value is
                    calculated by converting the sum of each cross collateral
                    currency's value to the given currency, using each cross
                    collateral currency's index.
                  example: 1
                  type: number
                  x-parser-schema-id: <anonymous-schema-358>
                close_out_margin:
                  description: >
                    Close-out margin threshold in the selected currency, equal
                    to 50% of the positional maintenance margin.

                    Because it sits below `maintenance_margin`, it marks a later
                    and more severe stage than ordinary liquidation: when
                    `margin_balance` falls to or below this level, close-out
                    liquidation takes over.

                    On a cross account with an outstanding loan it is not
                    exactly half of the reported `maintenance_margin`: the
                    loan's maintenance margin is included in
                    `maintenance_margin` but excluded from the close-out
                    threshold.

                    Returned only when close-out margin is enabled on the
                    platform.
                  type: number
                  example: 0
                  x-parser-schema-id: <anonymous-schema-359>
                projected_close_out_margin:
                  description: >
                    Close-out margin calculated as if instruments expiring at
                    the nearest expiration were excluded, i.e. 50% of the
                    projected positional maintenance margin.

                    As with `close_out_margin`, the loan maintenance margin
                    counted in `projected_maintenance_margin` is excluded here,
                    so on a cross account with an outstanding loan the two are
                    not exactly proportional.

                    Returned only when close-out margin is enabled on the
                    platform.
                  type: number
                  example: 0
                  x-parser-schema-id: <anonymous-schema-360>
                additional_reserve:
                  description: >-
                    The account's balance reserved for open buy option orders
                    and option combo orders (the premium payable if they fill).
                    Only non-zero on the `cross_sm` margin model; balance
                    reserved by spot orders is reported separately in
                    `spot_reserve`.
                  example: 0.3
                  type: number
                  x-parser-schema-id: <anonymous-schema-361>
              required:
                - currency
                - equity
                - maintenance_margin
                - initial_margin
                - available_funds
                - available_withdrawal_funds
                - balance
                - margin_balance
                - session_upl
                - session_rpl
                - total_pl
                - options_pl
                - options_session_upl
                - options_session_rpl
                - options_delta
                - options_gamma
                - options_value
                - options_vega
                - options_theta
                - options_gamma_map
                - options_vega_map
                - options_theta_map
                - futures_pl
                - futures_session_upl
                - futures_session_rpl
                - delta_total_map
                - projected_delta_total
                - portfolio_margining_enabled
                - cross_collateral_enabled
                - margin_model
                - projected_maintenance_margin
              additionalProperties: false
              x-parser-schema-id: <anonymous-schema-317>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-316>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "delta_total_map": {
                "btc_usd": 31.594397699
              },
              "margin_balance": 302.62675921,
              "futures_session_rpl": -0.03311399,
              "options_session_rpl": 0,
              "session_upl": 0.05341555,
              "options_gamma_map": {
                "btc_usd": 0.00001
              },
              "options_vega": 0.07976,
              "options_value": -0.0079,
              "available_withdrawal_funds": 301.35426172,
              "projected_delta_total": 32.613978,
              "maintenance_margin": 0.8854841,
              "total_pl": -0.33014225,
              "options_theta_map": {
                "btc_usd": 16.13825
              },
              "projected_maintenance_margin": 0.7543841,
              "available_funds": 301.38036328,
              "options_delta": -1.01958,
              "balance": 302.60065765,
              "equity": 302.6188592,
              "futures_session_upl": 0.05921555,
              "fee_balance": 0,
              "currency": "BTC",
              "options_session_upl": -0.0058,
              "projected_initial_margin": 1.01529592,
              "options_theta": 16.13825,
              "portfolio_margining_enabled": false,
              "cross_collateral_enabled": false,
              "margin_model": "segregated_sm",
              "options_vega_map": {
                "btc_usd": 0.07976
              },
              "futures_pl": -0.32434225,
              "options_pl": -0.0058,
              "initial_margin": 1.24639592,
              "spot_reserve": 0,
              "delta_total": 31.602298,
              "options_gamma": 0.00001,
              "session_rpl": -0.03311399,
              "additional_reserve": 0
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: user.portfolio.(currency)
  - &ref_1
    id: receive_user_portfolio_currency_updates
    title: Receive user updates
    description: Client receives user update notifications
    type: receive
    messages:
      - &ref_3
        id: subscribe_request
        contentType: application/json
        payload:
          - name: Subscription Request
            description: >-
              Client sends subscription request to subscribe to notification
              channel. Please refer to [Notification
              page](https://deribit.mintlify.app/articles/notifications) for
              more information.
            type: object
            properties: []
        headers: []
        jsonPayloadSchema:
          properties: {}
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-315>
        title: Subscription Request
        description: >-
          Client sends subscription request to subscribe to notification
          channel. Please refer to [Notification
          page](https://deribit.mintlify.app/articles/notifications) for more
          information.
        example: |-
          {
            "jsonrpc": "2.0",
            "method": "public/subscribe",
            "id": 42,
            "params": {
              "channels": [
                "user.portfolio.(currency)"
              ]
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscribe_request
    bindings: []
    extensions: *ref_0
sendOperations:
  - *ref_1
receiveOperations:
  - *ref_2
sendMessages:
  - *ref_3
receiveMessages:
  - *ref_4
extensions:
  - id: x-parser-unique-object-id
    value: user.portfolio.(currency)
securitySchemes: []

````

## Related topics

- [Notifications](/articles/notifications.md)
- [JSON-RPC API Changelog](/changelogs/jsonrpc.md)
- [user.trades.(kind).(currency).(interval) ](/subscriptions/user/usertradeskindcurrencyinterval.md)
- [user.orders.(kind).(currency).raw ](/subscriptions/user/userorderskindcurrencyraw.md)
- [user.orders.(kind).(currency).(interval) ](/subscriptions/user/userorderskindcurrencyinterval.md)
