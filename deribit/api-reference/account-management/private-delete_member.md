> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# private/delete_member

> Deletes a Direct Access member from the account. Returns the resulting list of all members
configured for the account.

This method is dedicated to Starbase. See [Starbase Account Model](https://docs.deribit.com/starbase/account-model)
for an explanation of Members, portfolios, and their relationship to Deribit accounts.

Requires Direct Access trading to be enabled for the account.

**Scope:** `account:read_write` and mainaccount

[Try in API console](https://test.deribit.com/api_console?method=%2Fprivate%2Fdelete_member)





## OpenAPI

````yaml /specifications/deribit_openapi.json get /private/delete_member
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
  /private/delete_member:
    get:
      tags:
        - Account Management
        - Private
      description: >+
        Deletes a Direct Access member from the account. Returns the resulting
        list of all members

        configured for the account.


        This method is dedicated to Starbase. See [Starbase Account
        Model](https://docs.deribit.com/starbase/account-model)

        for an explanation of Members, portfolios, and their relationship to
        Deribit accounts.


        Requires Direct Access trading to be enabled for the account.


        **Scope:** `account:read_write` and mainaccount


        [Try in API
        console](https://test.deribit.com/api_console?method=%2Fprivate%2Fdelete_member)

      parameters:
        - name: member_id
          required: true
          in: query
          schema:
            type: integer
            minimum: 1
            example: 195
          description: ID of the member to delete.
      requestBody:
        content:
          application/json:
            examples:
              request:
                value:
                  jsonrpc: '2.0'
                  id: 60
                  method: private/delete_member
                  params:
                    member_id: 195
                description: JSON-RPC Request Example
        description: JSON-RPC request body
      responses:
        '200':
          $ref: '#/components/responses/PrivateDeleteMemberResponse'
components:
  responses:
    PrivateDeleteMemberResponse:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PrivateDeleteMemberResponse'
          examples:
            response:
              value:
                jsonrpc: '2.0'
                id: 60
                result:
                  members: []
                  is_direct_access_allowed: true
              description: Response example
      description: Success response
  schemas:
    PrivateDeleteMemberResponse:
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

- [private/set_member](/api-reference/account-management/private-set_member.md)
- [private/get_members](/api-reference/account-management/private-get_members.md)
- [private/delete_address_beneficiary](/api-reference/wallet/private-delete_address_beneficiary.md)
- [Self Match Prevention (SMP)](/starbase/smp.md)
- [Account Model](/starbase/account-model.md)
