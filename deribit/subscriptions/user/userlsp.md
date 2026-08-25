> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# user.lsp 

> Notifications for an LSP (Liquidity Support Program) participant subaccount: assignment attempts (successful or failed), enable/disable state changes, and effective configuration changes.

Subscribe to this channel with an API key belonging to the LSP participant subaccount itself. See `user.liquidation` for the notification sent to the liquidated (source) user whose position was transferred.

Every notification includes a `type` field identifying the event kind — see the notification schema for the full list of types and which fields accompany each.




## AsyncAPI

````yaml specifications/deribit_asyncapi.json user.lsp
id: user.lsp
title: 'user.lsp '
description: >
  Notifications for an LSP (Liquidity Support Program) participant subaccount:
  assignment attempts (successful or failed), enable/disable state changes, and
  effective configuration changes.


  Subscribe to this channel with an API key belonging to the LSP participant
  subaccount itself. See `user.liquidation` for the notification sent to the
  liquidated (source) user whose position was transferred.


  Every notification includes a `type` field identifying the event kind — see
  the notification schema for the full list of types and which fields accompany
  each.
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
address: user.lsp
parameters: []
bindings: []
operations:
  - &ref_2
    id: send_subscribe_user_lsp
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
                  - name: type
                    type: string
                    description: >
                      The kind of LSP (Liquidity Support Program) event this
                      notification represents:

                      - `transfer`: An assignment attempt to this participant
                      completed — check `success` to see whether it succeeded
                      (fully or partially) or failed and was redistributed to
                      other participants (or fell through to ADL).

                      - `enabled`: This participant's LSP configuration
                      transitioned from disabled to enabled.

                      - `disabled`: This participant's LSP configuration
                      transitioned from enabled to disabled — check `automatic`
                      to see whether this was a manual change or an automatic
                      disable after repeated transfer failures.

                      - `configuration_changed`: This participant's effective
                      configuration changed (enable state and/or any group
                      limit, including a change to the platform-wide default
                      that affects this participant). Fired on every
                      configuration write, including no-op enable/disable
                      transitions.
                    enumValues:
                      - transfer
                      - enabled
                      - disabled
                      - configuration_changed
                    required: true
                  - name: instrument_name
                    type: string
                    description: Unique instrument identifier
                    required: false
                  - name: direction
                    type: string
                    description: Present for `transfer` only.
                    enumValues:
                      - buy
                      - sell
                    required: false
                  - name: amount
                    type: number
                    description: >-
                      Present for `transfer` only. Size of the position assigned
                      (or attempted).
                    required: false
                  - name: price
                    type: number
                    description: >-
                      Present for `transfer` only. The transfer price applied to
                      this assignment attempt.
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
                  - name: success
                    type: boolean
                    description: >-
                      Present for `transfer` only. `true` if the assignment
                      succeeded, `false` if it failed (see `error_reason`).
                    required: false
                  - name: error_reason
                    type: string
                    description: >-
                      Present for `transfer` only, and only when `success` is
                      `false`. Machine-readable failure reason.
                    enumValues:
                      - platform_locked
                      - lock_count_exceeded
                      - timeout
                      - temporarily_unavailable
                      - not_enough_funds
                      - internal_error
                    required: false
                  - name: automatic
                    type: boolean
                    description: >-
                      Present for `disabled` only. `true` if this was an
                      automatic disable after repeated transfer failures,
                      `false` if a manual configuration change.
                    required: false
                  - name: failure_count
                    type: integer
                    description: >-
                      Present for `disabled` only, and only when `automatic` is
                      `true`. Number of transfer failures that triggered the
                      auto-disable.
                    required: false
                  - name: window_minutes
                    type: integer
                    description: >-
                      Present for `disabled` only, and only when `automatic` is
                      `true`. Length of the failure-counting window, in minutes.
                    required: false
                  - name: configuration
                    type: object
                    description: >-
                      Present for `configuration_changed` only. The
                      participant's resolved effective configuration: `enabled`,
                      plus every cooldown group's effective limit percentage
                      (`group_limits`, keyed by group) — per-participant
                      overrides are already resolved against the platform-wide
                      defaults, so every group appears here regardless of
                      whether this participant has an explicit override.
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
                type:
                  type: string
                  description: >
                    The kind of LSP (Liquidity Support Program) event this
                    notification represents:

                    - `transfer`: An assignment attempt to this participant
                    completed — check `success` to see whether it succeeded
                    (fully or partially) or failed and was redistributed to
                    other participants (or fell through to ADL).

                    - `enabled`: This participant's LSP configuration
                    transitioned from disabled to enabled.

                    - `disabled`: This participant's LSP configuration
                    transitioned from enabled to disabled — check `automatic` to
                    see whether this was a manual change or an automatic disable
                    after repeated transfer failures.

                    - `configuration_changed`: This participant's effective
                    configuration changed (enable state and/or any group limit,
                    including a change to the platform-wide default that affects
                    this participant). Fired on every configuration write,
                    including no-op enable/disable transitions.
                  enum:
                    - transfer
                    - enabled
                    - disabled
                    - configuration_changed
                  x-parser-schema-id: <anonymous-schema-1180>
                instrument_name:
                  type: string
                  description: Unique instrument identifier
                  example: BTC-PERPETUAL
                  x-parser-schema-id: <anonymous-schema-1181>
                direction:
                  type: string
                  description: Present for `transfer` only.
                  enum:
                    - buy
                    - sell
                  x-parser-schema-id: <anonymous-schema-1182>
                amount:
                  type: number
                  description: >-
                    Present for `transfer` only. Size of the position assigned
                    (or attempted).
                  x-parser-schema-id: <anonymous-schema-1183>
                price:
                  type: number
                  description: >-
                    Present for `transfer` only. The transfer price applied to
                    this assignment attempt.
                  x-parser-schema-id: <anonymous-schema-1184>
                currency:
                  type: string
                  description: Currency, i.e `"BTC"`, `"ETH"`, `"USDC"`
                  enum:
                    - BTC
                    - ETH
                    - USDC
                    - USDT
                    - EURR
                  x-parser-schema-id: <anonymous-schema-1185>
                success:
                  type: boolean
                  description: >-
                    Present for `transfer` only. `true` if the assignment
                    succeeded, `false` if it failed (see `error_reason`).
                  x-parser-schema-id: <anonymous-schema-1186>
                error_reason:
                  type: string
                  description: >-
                    Present for `transfer` only, and only when `success` is
                    `false`. Machine-readable failure reason.
                  enum:
                    - platform_locked
                    - lock_count_exceeded
                    - timeout
                    - temporarily_unavailable
                    - not_enough_funds
                    - internal_error
                  x-parser-schema-id: <anonymous-schema-1187>
                automatic:
                  type: boolean
                  description: >-
                    Present for `disabled` only. `true` if this was an automatic
                    disable after repeated transfer failures, `false` if a
                    manual configuration change.
                  x-parser-schema-id: <anonymous-schema-1188>
                failure_count:
                  type: integer
                  description: >-
                    Present for `disabled` only, and only when `automatic` is
                    `true`. Number of transfer failures that triggered the
                    auto-disable.
                  x-parser-schema-id: <anonymous-schema-1189>
                window_minutes:
                  type: integer
                  description: >-
                    Present for `disabled` only, and only when `automatic` is
                    `true`. Length of the failure-counting window, in minutes.
                  x-parser-schema-id: <anonymous-schema-1190>
                configuration:
                  type: object
                  description: >-
                    Present for `configuration_changed` only. The participant's
                    resolved effective configuration: `enabled`, plus every
                    cooldown group's effective limit percentage (`group_limits`,
                    keyed by group) — per-participant overrides are already
                    resolved against the platform-wide defaults, so every group
                    appears here regardless of whether this participant has an
                    explicit override.
                  x-parser-schema-id: <anonymous-schema-1191>
                timestamp:
                  type: integer
                  example: 1536569522277
                  description: The timestamp (milliseconds since the Unix epoch)
                  x-parser-schema-id: <anonymous-schema-1192>
              required:
                - type
                - timestamp
              additionalProperties: false
              x-parser-schema-id: <anonymous-schema-1179>
          required:
            - data
          additionalProperties: false
          x-parser-schema-id: <anonymous-schema-1178>
        title: Subscription Notification Data
        description: Server sends subscription notification data
        example: |-
          {
            "data": {
              "type": "transfer",
              "instrument_name": "BTC-PERPETUAL",
              "direction": "sell",
              "amount": 5000,
              "price": 63481.75,
              "currency": "BTC",
              "success": true,
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
        value: user.lsp
  - &ref_1
    id: receive_user_lsp
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
          x-parser-schema-id: <anonymous-schema-1177>
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
                "user.lsp"
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
    value: user.lsp
securitySchemes: []

````

## Related topics

- [user.liquidation ](/subscriptions/user/userliquidation.md)
- [Liquidity Support Program (LSP) API Guide](/articles/lsp-api-guide.md)
- [private/get_lsp_participants](/api-reference/lsp/private-get_lsp_participants.md)
- [private/get_lsp_participants_usage](/api-reference/lsp/private-get_lsp_participants_usage.md)
- [private/get_lsp_usage](/api-reference/lsp/private-get_lsp_usage.md)
