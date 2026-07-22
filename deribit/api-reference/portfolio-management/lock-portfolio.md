> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lock Portfolio

> Locks the authenticated portfolio. All currently open `DIRECT_ACCESS` orders and quotes for this portfolio are cancelled immediately. New `DIRECT_ACCESS` orders and quotes are rejected until the portfolio is unlocked.

REST-submitted orders are not affected by the lock state.



## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/private/lock_portfolio
openapi: 3.0.3
info:
  title: Starbase REST API
  version: '2.0'
  description: Portfolio-scoped REST API for the Starbase direct-access trading platform.
servers:
  - url: https://195.138.37.5:4410
    description: Production — Gateway A (rest-order)
  - url: https://195.138.37.6:4410
    description: Production — Gateway B (rest-order)
  - url: https://195.138.37.137:4410
    description: Test — Gateway A (rest-order)
  - url: https://195.138.37.138:4410
    description: Test — Gateway B (rest-order)
security: []
tags:
  - name: Portfolio Management
    description: Endpoints that operate on the authenticated portfolio.
  - name: Trading
    description: Authenticated trading endpoints scoped to the caller's portfolio.
  - name: Market Data
    description: Public reference and market data endpoints. No authentication required.
paths:
  /api/v2/private/lock_portfolio:
    get:
      tags:
        - Portfolio Management
      summary: Lock Portfolio
      description: >-
        Locks the authenticated portfolio. All currently open `DIRECT_ACCESS`
        orders and quotes for this portfolio are cancelled immediately. New
        `DIRECT_ACCESS` orders and quotes are rejected until the portfolio is
        unlocked.


        REST-submitted orders are not affected by the lock state.
      operationId: lock_portfolio
      responses:
        '200':
          description: Portfolio locked successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OkResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result: ok
      security:
        - BearerAuth: []
components:
  schemas:
    OkResponse:
      type: object
      required:
        - jsonrpc
        - result
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
          type: string
          enum:
            - ok
          description: Result of method execution. `ok` in case of success
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        API key passed as a Bearer token. The authenticated session determines
        the portfolio that operations are applied to.

````

## Related topics

- [Portfolio Management](/starbase/portfolio-management.md)
- [user.lock ](/subscriptions/user/userlock.md)
- [Notifications](/articles/notifications.md)
- [Order Management](/articles/order-management-best-practices.md)
- [private/get_user_locks](/api-reference/account-management/private-get_user_locks.md)
