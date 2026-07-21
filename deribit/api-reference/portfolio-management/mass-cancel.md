> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mass Cancel

> Cancels all open orders and quotes belonging to the authenticated portfolio. No filter parameters are accepted — the cancel applies to every instrument and every side.



## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/private/cancel_all
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
  /api/v2/private/cancel_all:
    get:
      tags:
        - Portfolio Management
      summary: Mass Cancel
      description: >-
        Cancels all open orders and quotes belonging to the authenticated
        portfolio. No filter parameters are accepted — the cancel applies to
        every instrument and every side.
      operationId: cancel_all
      responses:
        '200':
          description: All open orders and quotes cancelled successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CancelAllResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result: 42
      security:
        - BearerAuth: []
components:
  schemas:
    CancelAllResponse:
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
          type: number
          example: 7
          description: Total number of successfully cancelled orders
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        API key passed as a Bearer token. The authenticated session determines
        the portfolio that operations are applied to.

````