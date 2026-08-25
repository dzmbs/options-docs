> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# private/get_lsp_participants

> Lists the LSP (Liquidity Support Program) participant subaccounts configured under the authenticated main account.

Must be called with an API key belonging to the main account — returns an error if called from a subaccount.

Use the `detailed` parameter to include each participant's full configuration alongside its `user_id` and `enabled` state.

**Scope:** `account:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_lsp_participants)





## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_lsp_participants
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
  /private/get_lsp_participants:
    get:
      tags:
        - lsp
        - Private
      description: >+
        Lists the LSP (Liquidity Support Program) participant subaccounts
        configured under the authenticated main account.


        Must be called with an API key belonging to the main account — returns
        an error if called from a subaccount.


        Use the `detailed` parameter to include each participant's full
        configuration alongside its `user_id` and `enabled` state.


        **Scope:** `account:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_lsp_participants)

      parameters:
        - name: detailed
          in: query
          schema:
            example: false
            type: boolean
          required: false
          description: >-
            When `true`, includes each participant's full LSP configuration
            (`config`). When `false` (default), only `user_id` and `enabled` are
            returned.
      requestBody:
        content:
          application/json:
            examples:
              request:
                value:
                  jsonrpc: '2.0'
                  id: 8802
                  method: private/get_lsp_participants
                  params:
                    detailed: false
                description: JSON-RPC Request Example
        description: JSON-RPC request body
      responses:
        '200':
          $ref: '#/components/responses/PrivateGetLspParticipantsResponse'
        '401':
          $ref: '#/components/responses/ErrorMessageResponse'
components:
  responses:
    PrivateGetLspParticipantsResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PrivateGetLspParticipantsResponse'
          examples:
            response:
              value:
                jsonrpc: '2.0'
                id: 8802
                result:
                  participants:
                    - user_id: 172345
                      enabled: true
                    - user_id: 172346
                      enabled: false
              description: Response example
      description: Success response
    ErrorMessageResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorMessageResponse'
      description: Success response
  schemas:
    PrivateGetLspParticipantsResponse:
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
            participants:
              type: array
              items:
                type: object
                properties:
                  user_id:
                    $ref: '#/components/schemas/user_id'
                  enabled:
                    type: boolean
                    description: >-
                      Present when `detailed=false` (or omitted). Whether the
                      participant is currently enabled.
                  config:
                    $ref: '#/components/schemas/lsp_config'
                    description: Present when `detailed=true`.
                required:
                  - user_id
          required:
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
    lsp_config:
      properties:
        enabled:
          type: boolean
          description: >-
            Whether this subaccount is currently an active LSP participant
            eligible to receive assignments.
        group_limits:
          type: object
          additionalProperties:
            type: number
          description: >
            Per-participant overrides of the assignment limit for each cooldown
            group, expressed as a percentage of the participant's own equity.
            Keyed by group: `"1"` through `"6"` (crypto tiers, `"6"` is the
            catch-all tier) or `"rwa"` (real-world-asset instruments, e.g.
            tokenized equities/commodities).


            A group absent from this map inherits the platform-wide default for
            that group. A value of `0` disables assignments for that group
            entirely. The maximum allowed value for any group is
            `notional_capacity_factor * 100` (see the global LSP config) — that
            factor caps the total notional LSP may assign to a participant as a
            multiple of its equity, and does not change the participant
            account's own maximum leverage.
      required:
        - enabled
        - group_limits
      type: object
      description: >
        LSP participation configuration for a single subaccount.


        Note: designating a subaccount as an LSP participant also locks it to
        reduce-only trading platform-side. This lock is not automatically
        released when the participant is removed — an admin must clear it
        manually.

````

## Related topics

- [Liquidity Support Program (LSP) API Guide](/articles/lsp-api-guide.md)
- [private/get_lsp_participant_config](/api-reference/lsp/private-get_lsp_participant_config.md)
- [private/get_lsp_participants_usage](/api-reference/lsp/private-get_lsp_participants_usage.md)
- [private/get_lsp_usage](/api-reference/lsp/private-get_lsp_usage.md)
- [user.lsp ](/subscriptions/user/userlsp.md)
