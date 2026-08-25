> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# private/get_lsp_participants_usage

> Retrieves per-cooldown-group assignment usage for all LSP (Liquidity Support Program) participant subaccounts configured under the authenticated main account.

Must be called with an API key belonging to the main account — returns an error if called from a subaccount. Use the `user_id` parameter to filter the result down to a single participant.

As with `private/get_lsp_usage`, each participant's group usage reports `pct` (limit, as a percentage of equity), `used` (USD within the current fixed window — flat until the window closes, then resets to `0` in one step), and `cooldown_start`/`cooldown_end` (the current window's timing) — remaining capacity is not computed for you and the leverage-derived cap applied at assignment time is not exposed on any user-facing endpoint.

**Scope:** `account:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_lsp_participants_usage)





## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_lsp_participants_usage
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
  /private/get_lsp_participants_usage:
    get:
      tags:
        - lsp
        - Private
      description: >+
        Retrieves per-cooldown-group assignment usage for all LSP (Liquidity
        Support Program) participant subaccounts configured under the
        authenticated main account.


        Must be called with an API key belonging to the main account — returns
        an error if called from a subaccount. Use the `user_id` parameter to
        filter the result down to a single participant.


        As with `private/get_lsp_usage`, each participant's group usage reports
        `pct` (limit, as a percentage of equity), `used` (USD within the current
        fixed window — flat until the window closes, then resets to `0` in one
        step), and `cooldown_start`/`cooldown_end` (the current window's timing)
        — remaining capacity is not computed for you and the leverage-derived
        cap applied at assignment time is not exposed on any user-facing
        endpoint.


        **Scope:** `account:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_lsp_participants_usage)

      parameters:
        - name: user_id
          in: query
          schema:
            type: integer
            example: 1
          required: false
          description: Id of a (sub)account - by default current user id is used
      requestBody:
        content:
          application/json:
            examples:
              request:
                value:
                  jsonrpc: '2.0'
                  id: 8804
                  method: private/get_lsp_participants_usage
                  params:
                    user_id: 172345
                description: JSON-RPC Request Example
        description: JSON-RPC request body
      responses:
        '200':
          $ref: '#/components/responses/PrivateGetLspParticipantsUsageResponse'
        '401':
          $ref: '#/components/responses/ErrorMessageResponse'
components:
  responses:
    PrivateGetLspParticipantsUsageResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PrivateGetLspParticipantsUsageResponse'
          examples:
            response:
              value:
                jsonrpc: '2.0'
                id: 8804
                result:
                  cooldown_period_ms: 300000
                  participants:
                    - user_id: 172345
                      groups:
                        '1':
                          pct: 15
                          used: 250000
                          cooldown_start: 1750000100000
                          cooldown_end: 1750000400000
                        '2':
                          pct: 10
                          used: 0
                          cooldown_start: null
                          cooldown_end: null
                        '3':
                          pct: 10
                          used: 0
                          cooldown_start: null
                          cooldown_end: null
                        '4':
                          pct: 10
                          used: 0
                          cooldown_start: null
                          cooldown_end: null
                        '5':
                          pct: 10
                          used: 0
                          cooldown_start: null
                          cooldown_end: null
                        '6':
                          pct: 0
                          used: 0
                          cooldown_start: null
                          cooldown_end: null
                        rwa:
                          pct: 10
                          used: 0
                          cooldown_start: null
                          cooldown_end: null
              description: Response example
      description: Success response
    ErrorMessageResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorMessageResponse'
      description: Success response
  schemas:
    PrivateGetLspParticipantsUsageResponse:
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
            cooldown_period_ms:
              type: integer
              description: >-
                Length of the fixed cooldown window in milliseconds, common to
                all participants.
            participants:
              type: array
              items:
                type: object
                properties:
                  user_id:
                    $ref: '#/components/schemas/user_id'
                  groups:
                    $ref: '#/components/schemas/lsp_group_usage'
                required:
                  - user_id
                  - groups
          required:
            - cooldown_period_ms
            - participants
      required:
        - result
        - jsonrpc
      type: object
    ErrorMessageResponse:
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
          description: The JSON-RPC version (2.0)
        id:
          type: integer
          description: The id that was sent in the request
        message:
          type: string
        error:
          type: integer
      required:
        - message
        - error
        - jsonrpc
      type: object
    user_id:
      example: 57874
      type: integer
      description: Unique user identifier
    lsp_group_usage:
      additionalProperties:
        properties:
          pct:
            type: number
            description: >-
              The effective limit for this group as a percentage of the
              participant's equity (the participant's `group_limits` override if
              set, otherwise the platform-wide default for that group).
          used:
            type: number
            description: >
              USD notional already assigned to this group within the current
              fixed cooldown window.


              This is a fixed window, not a smoothly-decaying rolling one: usage
              accumulates from the first assignment in the window and stays flat
              — it does not decrease as individual entries "age" — until the
              window as a whole expires (`cooldown_end`), at which point it
              resets to `0` in one step and the next assignment starts a brand
              new window.


              Note: neither the absolute limit (`pct / 100 * equity`) nor the
              remaining capacity is returned directly — compute it yourself from
              `pct`, `used`, and your own equity
              (`private/get_account_summary`). Even that computed figure won't
              reflect the additional notional-capacity cap
              (`notional_capacity_factor * equity - notional`) applied at
              assignment time, which is not exposed on any user-facing endpoint.
          cooldown_start:
            type: integer
            nullable: true
            description: >-
              Timestamp (milliseconds since the UNIX epoch) of the first
              assignment that opened this group's current fixed window, or
              `null` if the group has no tracked usage.
          cooldown_end:
            type: integer
            nullable: true
            description: >-
              Timestamp (milliseconds since the UNIX epoch) at which the current
              fixed window closes (`cooldown_start + cooldown_period_ms`) and
              this group's `used` resets to `0`, or `null` if the group has no
              tracked usage.
        required:
          - pct
          - used
          - cooldown_start
          - cooldown_end
        type: object
      type: object
      description: >-
        Per-cooldown-group assignment usage, keyed by group (`"1"`-`"6"` for
        crypto tiers, `"rwa"` for real-world-asset instruments). Groups with no
        configured limit and no usage may be absent.

````

## Related topics

- [Liquidity Support Program (LSP) API Guide](/articles/lsp-api-guide.md)
- [private/get_lsp_usage](/api-reference/lsp/private-get_lsp_usage.md)
- [private/get_lsp_participants](/api-reference/lsp/private-get_lsp_participants.md)
- [private/get_lsp_participant_config](/api-reference/lsp/private-get_lsp_participant_config.md)
- [user.lsp ](/subscriptions/user/userlsp.md)
