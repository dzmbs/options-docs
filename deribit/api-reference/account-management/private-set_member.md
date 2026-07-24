> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# private/set_member

> Creates a new Direct Access member, or edits an existing one. Returns the resulting list of all
members configured for the account.

This method is dedicated to Starbase. See [Starbase Account Model](https://docs.deribit.com/starbase/account-model)
for an explanation of Members, portfolios, and their relationship to Deribit accounts.

Omit `member_id` to create a new member; a non-empty `accounts` list is then required, and the
member cannot be created inactive. Pass an existing `member_id` to edit that member's `name` or
`accounts` list, or to toggle its `is_active` state — toggling `is_active` and changing
`name`/`accounts` cannot be done in the same request.

Requires Direct Access trading to be enabled for the account.

**Scope:** `account:read_write` and mainaccount

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fset_member)





## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/set_member
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
  /private/set_member:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Creates a new Direct Access member, or edits an existing one. Returns
        the resulting list of all

        members configured for the account.


        This method is dedicated to Starbase. See [Starbase Account
        Model](https://docs.deribit.com/starbase/account-model)

        for an explanation of Members, portfolios, and their relationship to
        Deribit accounts.


        Omit `member_id` to create a new member; a non-empty `accounts` list is
        then required, and the

        member cannot be created inactive. Pass an existing `member_id` to edit
        that member's `name` or

        `accounts` list, or to toggle its `is_active` state — toggling
        `is_active` and changing

        `name`/`accounts` cannot be done in the same request.


        Requires Direct Access trading to be enabled for the account.


        **Scope:** `account:read_write` and mainaccount


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fset_member)

      parameters:
        - name: member_id
          in: query
          schema:
            type: integer
            minimum: 1
            example: 195
          description: ID of the member to edit. Omit to create a new member.
          required: false
        - name: name
          required: true
          in: query
          schema:
            type: string
            maxLength: 64
            example: Member1
          description: Name of the member.
        - name: is_active
          in: query
          schema:
            type: boolean
            default: true
            example: true
          description: >-
            Whether the member should be active. `true` by default. A member
            cannot be created inactive.
          required: false
        - name: accounts
          in: query
          schema:
            type: array
            default: []
            items:
              type: integer
              minimum: 1
            example:
              - 85867
          description: >-
            List of (sub)account user ids to grant the member Direct Access
            trading rights on.
          style: form
          explode: true
          required: false
      requestBody:
        content:
          application/json:
            examples:
              request:
                value:
                  jsonrpc: '2.0'
                  id: 59
                  method: private/set_member
                  params:
                    member_id: 195
                    name: Member1
                    is_active: true
                    accounts:
                      - 85867
                description: JSON-RPC Request Example
        description: JSON-RPC request body
      responses:
        '200':
          $ref: '#/components/responses/PrivateSetMemberResponse'
components:
  responses:
    PrivateSetMemberResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PrivateSetMemberResponse'
          examples:
            response:
              value:
                jsonrpc: '2.0'
                id: 59
                result:
                  members:
                    - member_id: 195
                      main_uid: 57874
                      name: Member1
                      is_active: true
                      accounts:
                        - 85867
                      m_tstamp: 1690000000000
                  is_direct_access_allowed: true
              description: Response example
      description: Success response
  schemas:
    PrivateSetMemberResponse:
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
          $ref: '#/components/schemas/members_list'
      required:
        - jsonrpc
        - result
      type: object
    members_list:
      properties:
        members:
          type: array
          items:
            $ref: '#/components/schemas/member'
        is_direct_access_allowed:
          type: boolean
          example: true
          description: Whether Direct Access trading is enabled for the account.
      required:
        - members
        - is_direct_access_allowed
      type: object
    member:
      properties:
        member_id:
          type: integer
          minimum: 1
          example: 195
          description: >-
            Member identifier. Only present when the request is made from the
            main account.
        main_uid:
          type: integer
          minimum: 1
          example: 57874
          description: >-
            User ID of the main account the member belongs to. Only present when
            the request is made from the main account.
        name:
          type: string
          maxLength: 64
          example: Member1
          description: Name of the member.
        is_active:
          type: boolean
          example: true
          description: >-
            Whether the member is active. Only active members have Direct Access
            trading rights.
        accounts:
          type: array
          items:
            type: integer
            minimum: 1
          example:
            - 85867
          description: >-
            List of (sub)account user ids the member has Direct Access trading
            rights on. Only present when the request is made from the main
            account.
        m_tstamp:
          type: integer
          minimum: 0
          example: 1690000000000
          description: >-
            Timestamp of the last modification of the member, in milliseconds
            since the UNIX epoch. Only present when the request is made from the
            main account.
      required:
        - name
        - is_active
      type: object
      description: >
        Represents a Direct Access member: an external identity (e.g. a FIX or
        Direct Access order

        gateway user) that can be granted Direct Access trading rights on the
        account or one of its

        subaccounts.

````

## Related topics

- [private/delete_member](/api-reference/account-management/private-delete_member.md)
- [private/get_members](/api-reference/account-management/private-get_members.md)
- [private/set_email_language](/api-reference/account-management/private-set_email_language.md)
- [private/set_clearance_originator](/api-reference/wallet/private-set_clearance_originator.md)
- [private/set_mmp_config](/api-reference/trading/private-set_mmp_config.md)
