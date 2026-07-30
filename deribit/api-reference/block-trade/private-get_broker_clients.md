> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# private/get_broker_clients

> **Broker Method** Returns a list of clients registered under the broker account. Each client record includes:

- `client_id` — a numeric identifier that groups one or more linked users under a single client name. Use this value in other Broker Voice API calls (e.g. `private/execute_broker_trade`) to identify the client group.
- `links` — an array of individual user connections belonging to that client. Each link contains a `client_link_id` that uniquely identifies a single user within the client group.

**How to obtain `client_id` and `client_link_id`**

Call this endpoint without parameters to retrieve all clients. Locate the client by name or company, read `client_id` from the top-level object, and read `client_link_id` from the relevant entry in the `links` array. Use these two values together in subsequent Broker Voice API calls to specify which user within a client should be the counterparty.

A link `state` of `connected` means the user has accepted the broker invitation and is ready to trade. Links in `pending` state have not yet been accepted; links in `rejected` state are inactive.

Optionally filter by a specific `client_id` to return only that client's record, or set `include_subaccounts` to `true` to include clients managed by broker sub-accounts.

**Scope:** `block_trade:read`

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_broker_clients)





## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/get_broker_clients
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
paths:
  /private/get_broker_clients:
    get:
      tags:
        - Block Trade
        - Private
      description: >+
        **Broker Method** Returns a list of clients registered under the broker
        account. Each client record includes:


        - `client_id` — a numeric identifier that groups one or more linked
        users under a single client name. Use this value in other Broker Voice
        API calls (e.g. `private/execute_broker_trade`) to identify the client
        group.

        - `links` — an array of individual user connections belonging to that
        client. Each link contains a `client_link_id` that uniquely identifies a
        single user within the client group.


        **How to obtain `client_id` and `client_link_id`**


        Call this endpoint without parameters to retrieve all clients. Locate
        the client by name or company, read `client_id` from the top-level
        object, and read `client_link_id` from the relevant entry in the `links`
        array. Use these two values together in subsequent Broker Voice API
        calls to specify which user within a client should be the counterparty.


        A link `state` of `connected` means the user has accepted the broker
        invitation and is ready to trade. Links in `pending` state have not yet
        been accepted; links in `rejected` state are inactive.


        Optionally filter by a specific `client_id` to return only that client's
        record, or set `include_subaccounts` to `true` to include clients
        managed by broker sub-accounts.


        **Scope:** `block_trade:read`


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fget_broker_clients)

      parameters:
        - name: client_id
          in: query
          required: false
          schema:
            type: integer
          description: >-
            If provided, returns only the client with this ID. Omit to return
            all clients.
        - name: include_subaccounts
          in: query
          required: false
          schema:
            type: boolean
          description: >-
            If `true`, includes clients managed by broker sub-accounts. Default:
            `false`.
      requestBody:
        content:
          application/json:
            examples:
              request:
                value:
                  jsonrpc: '2.0'
                  id: 1
                  method: private/get_broker_clients
                  params: {}
                description: JSON-RPC Request Example
        description: JSON-RPC request body
      responses:
        '200':
          $ref: '#/components/responses/PrivateGetBrokerClientsResponse'
components:
  responses:
    PrivateGetBrokerClientsResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PrivateGetBrokerClientsResponse'
          examples:
            response:
              value:
                jsonrpc: '2.0'
                id: 1
                result:
                  - client_id: 1
                    client_name: Acme Trading Ltd
                    company_name: Acme Trading Ltd
                    broker_code: ACME01
                    main_user_id: '***456'
                    links:
                      - client_link_id: 1
                        user_id: '***456'
                        name: Main Trader
                        note: Primary trading account
                        state: connected
                        confirmations_required: 1
                      - client_link_id: 2
                        user_id: '***789'
                        name: Sub Trader
                        note: ''
                        state: pending
                        confirmations_required: 1
                  - client_id: 2
                    client_name: Beta Capital
                    company_name: Beta Capital GmbH
                    broker_code: BETA01
                    links:
                      - client_link_id: 3
                        user_id: '***012'
                        name: Portfolio Manager
                        note: ''
                        state: connected
                        confirmations_required: 2
              description: Response example
      description: Success response
  schemas:
    PrivateGetBrokerClientsResponse:
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
          type: array
          items:
            type: object
            properties:
              client_id:
                type: integer
                description: >-
                  Numeric identifier for the client group. Used in Broker Voice
                  API calls to reference this client.
              client_name:
                type: string
                description: Name of the client.
              company_name:
                type: string
                description: Company name of the client.
              broker_code:
                type: string
                description: Broker-assigned code used in invitation links for this client.
              main_user_id:
                type: string
                description: >-
                  Obscured user ID of the main account linked to this client, if
                  any.
              broker_sub_user_id:
                type: integer
                description: >-
                  ID of the broker sub-account that manages this client, if
                  applicable.
              lei:
                type: string
                description: Legal Entity Identifier (LEI) of the client, if provided.
              brn:
                type: string
                description: Business Registration Number (BRN) of the client, if provided.
              links:
                type: array
                items:
                  type: object
                  properties:
                    client_link_id:
                      type: integer
                      description: >-
                        Numeric identifier for an individual user within the
                        client group. Used together with `client_id` in Broker
                        Voice API calls.
                    user_id:
                      type: string
                      description: Obscured user ID of the linked user.
                    name:
                      type: string
                      description: Display name for this link.
                    note:
                      type: string
                      description: Optional note attached to this link.
                    state:
                      type: string
                      enum:
                        - connected
                        - pending
                        - rejected
                      description: >-
                        Connection state of the link: `connected` (user accepted
                        the invitation and is active), `pending` (invitation
                        sent, not yet accepted), or `rejected` (link is
                        inactive).
                    confirmations_required:
                      type: integer
                      description: >-
                        Number of broker confirmations required for block trades
                        involving this link.
                    broker_sub_user_id:
                      type: integer
                      description: >-
                        ID of the broker sub-account managing this link, if
                        applicable.
                  required:
                    - client_link_id
                    - user_id
                    - name
                    - state
                    - confirmations_required
                description: Array of individual user connections belonging to this client.
            required:
              - client_id
              - client_name
              - company_name
              - broker_code
              - links
      required:
        - jsonrpc
        - result
      type: object

````

## Related topics

- [Voice Broker Trading API](/articles/voice-broker-trading-api.md)
- [private/get_broker_trades](/api-reference/block-trade/private-get_broker_trades.md)
- [private/get_broker_trade_requests](/api-reference/block-trade/private-get_broker_trade_requests.md)
- [private/get_block_trade_requests](/api-reference/block-trade/private-get_block_trade_requests.md)
- [private/get_block_trades](/api-reference/block-trade/private-get_block_trades.md)
