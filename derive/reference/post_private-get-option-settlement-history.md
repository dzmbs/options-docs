> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Option Settlement History

Get expired option settlement history for a subaccount or wallet.<br />If wallet is provided, returns settlements for all subaccounts belonging to that wallet.
Required minimum session key permission level is `read_only`

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
    "/private/get_option_settlement_history": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Get Option Settlement History",
        "description": "Get expired option settlement history for a subaccount or wallet.<br />If wallet is provided, returns settlements for all subaccounts belonging to that wallet.\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateGetOptionSettlementHistoryResponseSchema"
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
                "$ref": "#/components/schemas/PrivateGetOptionSettlementHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateGetOptionSettlementHistoryParamsSchema": {
        "properties": {
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "default": null,
            "description": "Subaccount ID for which to get expired option settlement history",
            "nullable": true
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "default": null,
            "description": "Wallet address (if set, returns settlements for all subaccounts)",
            "nullable": true
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateGetOptionSettlementHistoryResponseSchema": {
        "required": [
          "id",
          "result"
        ],
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
            "$ref": "#/components/schemas/PrivateGetOptionSettlementHistoryResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateGetOptionSettlementHistoryResultSchema": {
        "required": [
          "settlements"
        ],
        "properties": {
          "settlements": {
            "title": "settlements",
            "type": "array",
            "description": "List of expired option settlements",
            "items": {
              "$ref": "#/components/schemas/OptionSettlementResponseSchema"
            }
          }
        },
        "type": "object",
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
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```