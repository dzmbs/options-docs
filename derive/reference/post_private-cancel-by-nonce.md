> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel By Nonce

Cancel a single order by nonce. Uses up that nonce if the order does not exist, so any future orders with that nonce will fail
Required minimum session key permission level is `admin`

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
    "/private/cancel_by_nonce": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Cancel By Nonce",
        "description": "Cancel a single order by nonce. Uses up that nonce if the order does not exist, so any future orders with that nonce will fail\nRequired minimum session key permission level is `admin`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateCancelByNonceResponseSchema"
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
                "$ref": "#/components/schemas/PrivateCancelByNonceParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateCancelByNonceParamsSchema": {
        "required": [
          "instrument_name",
          "nonce",
          "subaccount_id",
          "wallet"
        ],
        "properties": {
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Instrument name"
          },
          "nonce": {
            "title": "nonce",
            "type": "integer",
            "description": "Cancel an order with this nonce"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Wallet address"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateCancelByNonceResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateCancelByNonceResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateCancelByNonceResultSchema": {
        "required": [
          "cancelled_orders"
        ],
        "properties": {
          "cancelled_orders": {
            "title": "cancelled_orders",
            "type": "integer",
            "description": "Number of cancelled orders"
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```