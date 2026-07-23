> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List Instruments

> Returns the list of tradeable instruments, optionally filtered by base currency, instrument kind, and expiration status. This endpoint is public — no authentication is required.

Filter semantics:
- `currency` filters by the **base** currency of the instrument's currency pair (case-insensitive match).
- `kind` filters by instrument type (case-insensitive match against the `kind` value enum).
- `expired = true` returns only instruments whose `expiration_timestamp` is in the past; `expired = false` returns only non-expired instruments. Omit the parameter to get both.



## OpenAPI

````yaml /specifications/starbase_rest_openapi.json get /api/v2/public/get_instruments
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
  /api/v2/public/get_instruments:
    get:
      tags:
        - Market Data
      summary: List Instruments
      description: >-
        Returns the list of tradeable instruments, optionally filtered by base
        currency, instrument kind, and expiration status. This endpoint is
        public — no authentication is required.


        Filter semantics:

        - `currency` filters by the **base** currency of the instrument's
        currency pair (case-insensitive match).

        - `kind` filters by instrument type (case-insensitive match against the
        `kind` value enum).

        - `expired = true` returns only instruments whose `expiration_timestamp`
        is in the past; `expired = false` returns only non-expired instruments.
        Omit the parameter to get both.
      operationId: get_instruments
      parameters:
        - name: currency
          in: query
          required: false
          description: >-
            Filter by the base currency of the instrument's currency pair (e.g.
            `BTC`, `ETH`, `AVAX`). Case-insensitive.
          schema:
            type: string
          example: BTC
        - name: kind
          in: query
          required: false
          description: Filter by instrument kind. Case-insensitive.
          schema:
            type: string
            enum:
              - perp_future
              - option
              - spot
              - future_combo
              - option_combo
              - dated_future
          example: perp_future
        - name: expired
          in: query
          required: false
          description: >-
            When `true`, return only expired instruments. When `false`, return
            only currently-active (non-expired) instruments. Omit to return
            both.
          schema:
            type: boolean
          example: false
      responses:
        '200':
          description: List of instruments matching the supplied filters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetInstrumentsResponse'
              example:
                jsonrpc: '2.0'
                id: 1
                result:
                  - instrument_id: 124942
                    instrument_name: ETH-PERPETUAL
                    kind: perp_future
                    product_group: ETH
                    base_currency: ETH
                    quote_currency: USDC
                    settlement_currency: USDC
                    tick_size: 0.01
                    is_active: true
                    creation_timestamp: 1747500000000
                  - instrument_id: 200001
                    instrument_name: BTC-30MAY26-70000-C
                    kind: option
                    product_group: BTC
                    base_currency: BTC
                    quote_currency: USDC
                    settlement_currency: USDC
                    tick_size: 0.5
                    strike: 70000
                    option_type: call
                    is_active: true
                    expiration_timestamp: 1779148800000
                    creation_timestamp: 1748400000000
        '500':
          description: Internal server error while building the instrument list.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonRpcError'
      security: []
components:
  schemas:
    GetInstrumentsResponse:
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
          description: Array of instruments matching the supplied filters. May be empty.
          items:
            $ref: '#/components/schemas/Instrument'
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
    Instrument:
      type: object
      description: A tradeable instrument's reference data.
      required:
        - instrument_id
        - instrument_name
        - kind
        - is_active
      properties:
        instrument_id:
          type: integer
          format: int64
          description: Stable numeric identifier for the instrument.
          example: 124942
        instrument_name:
          type: string
          description: >-
            Human-readable instrument symbol (e.g. `ETH-PERPETUAL`,
            `BTC-30MAY26-70000-C`).
          example: ETH-PERPETUAL
        kind:
          type: string
          enum:
            - perp_future
            - option
            - spot
            - future_combo
            - option_combo
            - dated_future
          description: Instrument category.
        product_group:
          type: string
          nullable: true
          description: >-
            Product grouping resolved from the base symbol of the instrument's
            currency pair.
          example: ETH
        base_currency:
          type: string
          nullable: true
          description: Base currency of the instrument's currency pair.
          example: ETH
        quote_currency:
          type: string
          nullable: true
          description: Quote currency of the instrument's currency pair.
          example: USDC
        settlement_currency:
          type: string
          nullable: true
          description: >-
            Settlement currency for the instrument. Currently equal to
            `quote_currency`.
          example: USDC
        tick_size:
          type: number
          description: Minimum price increment for the instrument.
          example: 0.01
        strike:
          type: number
          nullable: true
          description: Strike price (options only). `null` for non-option instruments.
          example: 70000
        option_type:
          type: string
          enum:
            - call
            - put
          nullable: true
          description: Option type (options only). `null` for non-option instruments.
        is_active:
          type: boolean
          description: Whether the instrument is currently enabled for trading.
        expiration_timestamp:
          type: integer
          format: int64
          nullable: true
          description: >-
            Instrument expiration time in milliseconds since the Unix epoch.
            `null` for perpetuals and other non-expiring instruments.
          example: 1779148800000
        creation_timestamp:
          type: integer
          format: int64
          nullable: true
          description: >-
            Instrument creation/listing time in milliseconds since the Unix
            epoch.
          example: 1747500000000
        min_trade_amount:
          type: number
          nullable: true
          description: Minimum allowed order quantity. May be `null` if not yet populated.
        contract_size:
          type: number
          nullable: true
          description: >-
            Contract size for the instrument. May be `null` if not yet
            populated.
        settlement_period:
          type: string
          nullable: true
          description: Settlement period descriptor. May be `null` if not yet populated.
        maker_commission:
          type: number
          nullable: true
          description: Maker commission rate. May be `null` if not yet populated.
        taker_commission:
          type: number
          nullable: true
          description: Taker commission rate. May be `null` if not yet populated.
        block_trade_commission:
          type: number
          nullable: true
          description: Block trade commission rate. May be `null` if not yet populated.

````

## Related topics

- [Security List(y) — Production FIX API](/fix-api/production/security-list.md)
- [Security List Request(x) — Production FIX API](/fix-api/production/security-list-request.md)
- [Deribit Production FIX API Overview](/fix-api/production/overview.md)
- [private/cancel_all_by_instrument](/api-reference/trading/private-cancel_all_by_instrument.md)
- [private/get_open_orders_by_instrument](/api-reference/trading/private-get_open_orders_by_instrument.md)
