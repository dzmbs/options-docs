# Get Interest History

Get interest payment history for a subaccount or wallet.
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
    "/private/get_interest_history": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Get Interest History",
        "description": "Get interest payment history for a subaccount or wallet.\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateGetInterestHistoryResponseSchema"
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
                "$ref": "#/components/schemas/PrivateGetInterestHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateGetInterestHistoryParamsSchema": {
        "type": "object",
        "properties": {
          "end_timestamp": {
            "title": "end_timestamp",
            "type": "integer",
            "default": 9223372036854776000,
            "description": "End timestamp of the event history in ms since Unix epoch (default current time)"
          },
          "start_timestamp": {
            "title": "start_timestamp",
            "type": "integer",
            "default": 0,
            "description": "Start timestamp of the event history in ms since Unix epoch (default 0)"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "default": null,
            "description": "Subaccount id (must be set if wallet is blank)",
            "nullable": true
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "default": null,
            "description": "Wallet address (if set, subaccount_id ignored)",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "PrivateGetInterestHistoryResponseSchema": {
        "type": "object",
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
            "$ref": "#/components/schemas/PrivateGetInterestHistoryResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateGetInterestHistoryResultSchema": {
        "type": "object",
        "required": [
          "events"
        ],
        "properties": {
          "events": {
            "title": "events",
            "type": "array",
            "description": "List of interest payments",
            "items": {
              "$ref": "#/components/schemas/InterestPaymentSchema"
            }
          }
        },
        "additionalProperties": false
      },
      "InterestPaymentSchema": {
        "type": "object",
        "required": [
          "interest",
          "subaccount_id",
          "timestamp"
        ],
        "properties": {
          "interest": {
            "title": "interest",
            "type": "string",
            "format": "decimal",
            "description": "Dollar interest paid (if negative) or received (if positive) by the subaccount"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID of the subaccount that received the interest payment"
          },
          "timestamp": {
            "title": "timestamp",
            "type": "integer",
            "description": "Timestamp of the interest payment (in ms since UNIX epoch)"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```