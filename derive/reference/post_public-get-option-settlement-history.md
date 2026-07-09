# Get Option Settlement History

Get expired option settlement history, optionally filtered by subaccount or wallet.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "version": "1.0.0",
    "title": "REST API"
  },
  "servers": [
    {
      "url": "https://api.lyra.finance",
      "description": "Prod"
    },
    {
      "url": "https://api-demo.lyra.finance",
      "description": "Testnet"
    }
  ],
  "paths": {
    "/public/get_option_settlement_history": {
      "post": {
        "tags": [
          "Public"
        ],
        "summary": "Get Option Settlement History",
        "description": "Get expired option settlement history, optionally filtered by subaccount or wallet.",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicGetOptionSettlementHistoryResponseSchema"
                }
              }
            }
          }
        },
        "parameters": [],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PublicGetOptionSettlementHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PaginationInfoSchema": {
        "required": [
          "count",
          "num_pages"
        ],
        "type": "object",
        "properties": {
          "count": {
            "title": "count",
            "type": "integer",
            "description": "Total number of items, across all pages"
          },
          "num_pages": {
            "title": "num_pages",
            "type": "integer",
            "description": "Number of pages"
          }
        },
        "additionalProperties": false
      },
      "OptionSettlementResponseSchema": {
        "required": [
          "amount",
          "expiry",
          "instrument_name",
          "option_settlement_pnl",
          "option_settlement_pnl_excl_fees",
          "settlement_price",
          "subaccount_id"
        ],
        "type": "object",
        "properties": {
          "amount": {
            "title": "amount",
            "type": "string",
            "format": "decimal",
            "description": "Amount that was settled"
          },
          "expiry": {
            "title": "expiry",
            "type": "integer",
            "description": "Expiry timestamp of the option"
          },
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Instrument name"
          },
          "option_settlement_pnl": {
            "title": "option_settlement_pnl",
            "type": "string",
            "format": "decimal",
            "description": "USD profit or loss from option settlements calculated as: settlement value - (average cost including fees x amount)"
          },
          "option_settlement_pnl_excl_fees": {
            "title": "option_settlement_pnl_excl_fees",
            "type": "string",
            "format": "decimal",
            "description": "USD profit or loss from option settlements calculated as: settlement value - (average price excluding fees x amount)"
          },
          "settlement_price": {
            "title": "settlement_price",
            "type": "string",
            "format": "decimal",
            "description": "Price of option settlement"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID of the settlement event"
          }
        },
        "additionalProperties": false
      },
      "PublicGetOptionSettlementHistoryParamsSchema": {
        "type": "object",
        "properties": {
          "page": {
            "title": "page",
            "type": "integer",
            "default": 1,
            "description": "Page number of results to return (default 1, returns last if above `num_pages`)"
          },
          "page_size": {
            "title": "page_size",
            "type": "integer",
            "default": 100,
            "description": "Number of results per page (default 100, max 1000)"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "default": null,
            "description": "Subaccount ID filter (defaults to all if not provided)",
            "nullable": true
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "default": null,
            "description": "Wallet address filter (if set, subaccount_id is ignored)",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "PublicGetOptionSettlementHistoryResponseSchema": {
        "required": [
          "id",
          "result"
        ],
        "type": "object",
        "properties": {
          "id": {
            "oneOf": [
              {
                "title": "",
                "type": "string"
              },
              {
                "title": "",
                "type": "integer"
              }
            ]
          },
          "result": {
            "$ref": "#/components/schemas/PublicGetOptionSettlementHistoryResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PublicGetOptionSettlementHistoryResultSchema": {
        "required": [
          "pagination",
          "settlements"
        ],
        "type": "object",
        "properties": {
          "pagination": {
            "$ref": "#/components/schemas/PaginationInfoSchema"
          },
          "settlements": {
            "title": "settlements",
            "type": "array",
            "description": "List of expired option settlements",
            "items": {
              "$ref": "#/components/schemas/OptionSettlementResponseSchema"
            }
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```