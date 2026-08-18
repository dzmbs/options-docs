> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# user.isolated.liquidation 

> Lets a **main** account observe the liquidation, ADL, and LSP activity of all of its **isolated-margin subaccounts**, without subscribing to each subaccount's own `user.liquidation` channel individually.

Every event on this channel is a fan-out copy of an event also delivered on the affected subaccount's own `user.liquidation` channel — the payload is identical, including `isolated: true` and the subaccount's `user_id`. The main account's *own* liquidation activity is never delivered here; it stays on the main account's regular `user.liquidation` channel.

Requires the `account:read` scope on an API key belonging to the **main account**, and is only available while isolated margin is enabled on the platform.




## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.isolated.liquidation
id: user.isolated.liquidation
title: 'user.isolated.liquidation '
description: >
  Lets a **main** account observe the liquidation, ADL, and LSP activity of all
  of its **isolated-margin subaccounts**, without subscribing to each
  subaccount's own `user.liquidation` channel individually.


  Every event on this channel is a fan-out copy of an event also delivered on
  the affected subaccount's own `user.liquidation` channel — the payload is
  identical, including `isolated: true` and the subaccount's `user_id`. The main
  account's *own* liquidation activity is never delivered here; it stays on the
  main account's regular `user.liquidation` channel.


  Requires the `account:read` scope on an API key belonging to the **main
  account**, and is only available while isolated margin is enabled on the
  platform.
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
address: user.isolated.liquidation
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_user_isolated_liquidation
    title: Send subscribe request
    description: Client sends subscription request for user
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
                  - name: state
                    type: string
                    description: >
                      The stage of the liquidation/ADL/LSP process this
                      notification represents:

                      - `liquidation_started` / `liquidation_completed`: The
                      standard (order-book) liquidation process has started or
                      completed for this account.

                      - `close_out_liquidation_started` /
                      `close_out_liquidation_completed`: The LSP/ADL close-out
                      process has started or completed for this account. An
                      account can go through this pair, the
                      `liquidation_started`/`liquidation_completed` pair, or
                      both in sequence (e.g. LSP/ADL close-out first, handed off
                      to standard liquidation if it can't fully resolve the
                      breach).

                      - `lsp_transfer`: A position was transferred off this
                      account to an LSP participant. Sent to the liquidated
                      (source) account — see the `user.lsp` channel for the
                      notification sent to the receiving participant.

                      - `adl_transfer`: A position was auto-deleveraged off this
                      account. Sent to the account being deleveraged (source).

                      - `adl_transfer_received`: A position was auto-deleveraged
                      onto this account from a counterparty. Sent to the
                      receiving (counterparty) account.
                    enumValues:
                      - liquidation_started
                      - liquidation_completed
                      - close_out_liquidation_started
                      - close_out_liquidation_completed
                      - lsp_transfer
                      - adl_transfer
                      - adl_transfer_received
                    required: true
                  - name: user_id
                    type: integer
                    description: Unique user identifier
                    required: true
                  - name: isolated
                    type: boolean
                    description: >-
                      Present and `true` only when this event applies to an
                      isolated-margin subaccount.
                    required: false
                  - name: currency
                    type: string
                    description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
                    enumValues:
                      - BTC
                      - ETH
                      - USDC
                      - USDT
                      - EURR
                    required: false
                  - name: margin_balance
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: maintenance_margin
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: initial_margin
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: close_out_margin
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: equity
                    type: number
                    description: >-
                      Present for `liquidation_started`,
                      `liquidation_completed`, `close_out_liquidation_started`,
                      and `close_out_liquidation_completed`.
                    required: false
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: false
                  - name: direction
                    type: string
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`. This account's own resulting
                      position side.
                    enumValues:
                      - buy
                      - sell
                    required: false
                  - name: amount
                    type: number
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`.
                    required: false
                  - name: price
                    type: number
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`. The transfer price applied.
                    required: false
                  - name: commission
                    type: number
                    description: >-
                      Present for `lsp_transfer`, `adl_transfer`, and
                      `adl_transfer_received`. The commission charged (on
                      `lsp_transfer`/`adl_transfer`) or this account's share of
                      the commission (on `adl_transfer_received`, proportional
                      to the position this account absorbed). Intra-account
                      subaccount ADL moves are commissioned the same way as
                      moves onto another user's account.
                    required: false
                  - name: timestamp
                    type: integer
                    description: The timestamp (milliseconds since the Unix epoch)
                    required: true
        headers: []
        jsonPayloadSchema:
          type: object
          description: Response containing notification data
          properties:
            data:
              type: object
              properties:
                state:
                  type: string
                  description: >
                    The stage of the liquidation/ADL/LSP process this
                    notification represents:

                    - `liquidation_started` / `liquidation_completed`: The
                    standard (order-book) liquidation process has started or
                    completed for this account.

                    - `close_out_liquidation_started` /
                    `close_out_liquidation_completed`: The LSP/ADL close-out
                    process has started or completed for this account. An
                    account can go through this pair, the
                    `liquidation_started`/`liquidation_completed` pair, or both
                    in sequence (e.g. LSP/ADL close-out first, handed off to
                    standard liquidation if it can't fully resolve the breach).

                    - `lsp_transfer`: A position was transferred off this
                    account to an LSP participant. Sent to the liquidated
                    (source) account — see the `user.lsp` channel for the
                    notification sent to the receiving participant.

                    - `adl_transfer`: A position was auto-deleveraged off this
                    account. Sent to the account being deleveraged (source).

                    - `adl_transfer_received`: A position was auto-deleveraged
                    onto this account from a counterparty. Sent to the receiving
                    (counterparty) account.
                  enum:
                    - liquidation_started
                    - liquidation_completed
                    - close_out_liquidation_started
                    - close_out_liquidation_completed
                    - lsp_transfer
                    - adl_transfer
                    - adl_transfer_received
                  x-parser-schema-id: <anonymous-schema-1162>
                user_id:
                  description: Unique user identifier
                  type: integer
                  example: 57874
                  x-parser-schema-id: <anonymous-schema-1163>
                isolated:
                  type: boolean
                  description: >-
                    Present and `true` only when this event applies to an
                    isolated-margin subaccount.
                  x-parser-schema-id: <anonymous-schema-1164>
                currency:
                  type: string
                  description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
                  enum:
                    - BTC
                    - ETH
                    - USDC
                    - USDT
                    - EURR
                  x-parser-schema-id: <anonymous-schema-1165>
                margin_balance:
                  type: number
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  x-parser-schema-id: <anonymous-schema-1166>
                maintenance_margin:
                  type: number
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  x-parser-schema-id: <anonymous-schema-1167>
                initial_margin:
                  type: number
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  x-parser-schema-id: <anonymous-schema-1168>
                close_out_margin:
                  type: number
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  x-parser-schema-id: <anonymous-schema-1169>
                equity:
                  type: number
                  description: >-
                    Present for `liquidation_started`, `liquidation_completed`,
                    `close_out_liquidation_started`, and
                    `close_out_liquidation_completed`.
                  x-parser-schema-id: <anonymous-schema-1170>
                instrument_name:
                  type: string
                  description: Unique instrument identifier
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-1171>
                direction:
                  type: string
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`. This account's own resulting
                    position side.
                  enum:
                    - buy
                    - sell
                  x-parser-schema-id: <anonymous-schema-1172>
                amount:
                  type: number
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`.
                  x-parser-schema-id: <anonymous-schema-1173>
                price:
                  type: number
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`. The transfer price applied.
                  x-parser-schema-id: <anonymous-schema-1174>
                commission:
                  type: number
                  description: >-
                    Present for `lsp_transfer`, `adl_transfer`, and
                    `adl_transfer_received`. The commission charged (on
                    `lsp_transfer`/`adl_transfer`) or this account's share of
                    the commission (on `adl_transfer_received`, proportional to
                    the position this account absorbed). Intra-account
                    subaccount ADL moves are commissioned the same way as moves
                    onto another user's account.
                  x-parser-schema-id: <anonymous-schema-1175>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-1176>
              required:
                - state
                - user_id
                - timestamp
              additionalProperties: false
              x-parser-schema-id: <anonymous-schema-1161>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1160>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "state": "liquidation_started",
              "user_id": 220042,
              "isolated": true,
              "currency": "USDC",
              "margin_balance": 110,
              "maintenance_margin": 120,
              "initial_margin": 150,
              "close_out_margin": 130,
              "equity": 110,
              "timestamp": 1750000400000
            }
          }
        bindings: []
        extensions:
          - id: x-parser-unique-object-id
            value: subscription_message
    bindings: []
    extensions: &ref_0
      - id: x-parser-unique-object-id
        value: user.isolated.liquidation
  - &ref_1
    id: receive_user_isolated_liquidation
    title: Receive user
    description: Client receives user notifications
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
          x-parser-schema-id: <anonymous-schema-1159>
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
                "user.isolated.liquidation"
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
    value: user.isolated.liquidation
securitySchemes: []

````

## Related topics

- [user.liquidation ](/subscriptions/user/userliquidation.md)
- [Mass Quotes Specifications](/articles/mass-quotes-specifications.md)
- [user.lsp ](/subscriptions/user/userlsp.md)
- [JSON-RPC API Changelog](/changelogs/jsonrpc.md)
- [private/get_user_trades_by_order](/api-reference/trading/private-get_user_trades_by_order.md)
