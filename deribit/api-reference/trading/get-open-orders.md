> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Open Orders

> Returns all currently-open orders belonging to the authenticated portfolio. Orders are returned regardless of instrument or order type; filtering by instrument kind and order type is not currently supported.

The portfolio is resolved from the authenticated session — there is no parameter to query another portfolio's orders. MMP-flagged orders are visible via this endpoint. Orders placed via Mass Quote (MassQuoteRequest) are not currently returned.

This endpoint is rate-limited per portfolio. Exceeding the limit returns HTTP 429.



## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/private/get_open_orders
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
  /api/v2/private/get_open_orders:
    get:
      tags:
        - Trading
      summary: Get Open Orders
      description: >-
        Returns all currently-open orders belonging to the authenticated
        portfolio. Orders are returned regardless of instrument or order type;
        filtering by instrument kind and order type is not currently supported.


        The portfolio is resolved from the authenticated session — there is no
        parameter to query another portfolio's orders. MMP-flagged orders are
        visible via this endpoint. Orders placed via Mass Quote
        (MassQuoteRequest) are not currently returned.


        This endpoint is rate-limited per portfolio. Exceeding the limit returns
        HTTP 429.
      operationId: get_open_orders
      responses:
        '200':
          description: List of open orders for the authenticated portfolio. May be empty.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetOpenOrdersResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result:
                  - order_id: 1cc1c718-49e0-4ea5-8902-f3f22968c350
                    instrument_name: TREE-USD
                    side: sell
                    price: 0.0717
                    amount: 83698
                    filled_amount: 0
                    average_price: 0
                    order_state: open
                    order_type: limit
                    creation_timestamp: 1778270370643
                    last_update_timestamp: 1778270370643
        '401':
          description: Missing or invalid `Authorization` header.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
        '429':
          description: >-
            Per-portfolio rate limit for this endpoint exceeded. Configured via
            `portfolio-rate-limit.get_open_orders`.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
        '500':
          description: Internal server error while reading the active-order set.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
      security:
        - BearerAuth: []
components:
  schemas:
    GetOpenOrdersResponse:
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
          type: array
          description: Array of open orders for the authenticated portfolio. May be empty.
          items:
            $ref: '#/components/schemas/Order'
    JsonRpcError:
      type: object
      required:
        - jsonrpc
        - error
      description: JSON-RPC 2.0 error envelope returned for failed requests.
      properties:
        jsonrpc:
          type: string
          enum:
            - '2.0'
        id:
          type: integer
          nullable: true
          description: The id that was sent in the request, if any.
        error:
          type: object
          required:
            - code
            - message
          properties:
            code:
              type: integer
              description: Numeric JSON-RPC error code.
            message:
              type: string
              description: Human-readable error description.
            data:
              description: Optional additional error details.
    Order:
      type: object
      description: A single open order from the authenticated portfolio.
      required:
        - order_id
        - instrument_name
        - side
        - price
        - amount
        - filled_amount
        - order_state
        - order_type
      properties:
        order_id:
          type: string
          description: >-
            Exchange-assigned order identifier (UUID-style string). Stable for
            the lifetime of the order.
          example: 1cc1c718-49e0-4ea5-8902-f3f22968c350
        instrument_name:
          type: string
          description: Human-readable instrument symbol the order was placed against.
          example: TREE-USD
        side:
          type: string
          enum:
            - buy
            - sell
          description: Order side.
        price:
          type: number
          description: Limit price of the order (in quote-currency units).
          example: 0.0717
        amount:
          type: number
          description: Original order quantity, in base-currency units.
          example: 83698
        filled_amount:
          type: number
          description: Quantity filled so far, in base-currency units.
          example: 0
        average_price:
          type: number
          description: >-
            Volume-weighted average fill price across all executions on this
            order. Zero if the order has no fills yet.
          example: 0
        order_state:
          type: string
          enum:
            - open
          description: >-
            Order state. Currently always `open` for entries returned by this
            endpoint, since only open orders are listed.
        order_type:
          type: string
          enum:
            - limit
            - market
          description: Order type, derived from the price field.
        time_in_force:
          type: string
          nullable: true
          enum:
            - GTC
            - IOC
            - FOK
            - GTD
          description: Time-in-force policy.
        post_only:
          type: boolean
          nullable: true
          description: Whether the order was submitted as post-only.
        reduce_only:
          type: boolean
          nullable: true
          description: Whether the order was submitted as reduce-only.
        creation_timestamp:
          type: integer
          format: int64
          description: Order submission time in milliseconds since the Unix epoch.
          example: 1778270370643
        last_update_timestamp:
          type: integer
          format: int64
          description: >-
            Time of the most recent change to the order, in milliseconds since
            the Unix epoch.
          example: 1778270370643
        label:
          type: string
          nullable: true
          description: Client-supplied label for the order, if any.
        api:
          type: boolean
          nullable: true
          description: Whether the order was placed via API.
        max_show:
          type: number
          nullable: true
          description: Iceberg display quantity, if applicable.
        profit_loss:
          type: number
          nullable: true
          description: Realised profit/loss attributable to this order, if any.
        commission:
          type: number
          nullable: true
          description: Commission accrued by this order so far, if any.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        API key passed as a Bearer token. The authenticated session determines
        the portfolio that operations are applied to.

````

## Related topics

- [private/get_open_orders](/api-reference/trading/private-get_open_orders.md)
- [private/get_open_orders_by_instrument](/api-reference/trading/private-get_open_orders_by_instrument.md)
- [private/get_open_orders_by_currency](/api-reference/trading/private-get_open_orders_by_currency.md)
- [private/get_open_orders_by_label](/api-reference/trading/private-get_open_orders_by_label.md)
- [Quickstart Guide](/articles/deribit-quickstart.md)
