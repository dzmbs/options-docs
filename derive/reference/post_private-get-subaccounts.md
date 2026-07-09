# Get Subaccounts

Get all subaccounts of an account / wallet
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
    "/private/get_subaccounts": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Get Subaccounts",
        "description": "Get all subaccounts of an account / wallet\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateGetSubaccountsResponseSchema"
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
                "$ref": "#/components/schemas/PrivateGetSubaccountsParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateGetSubaccountsParamsSchema": {
        "required": [
          "wallet"
        ],
        "type": "object",
        "properties": {
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Ethereum wallet address of account"
          }
        },
        "additionalProperties": false
      },
      "PrivateGetSubaccountsResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateGetSubaccountsResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateGetSubaccountsResultSchema": {
        "required": [
          "subaccount_ids",
          "wallet"
        ],
        "type": "object",
        "properties": {
          "subaccount_ids": {
            "title": "subaccount_ids",
            "type": "array",
            "description": "List of subaccount_ids owned by the wallet in `SubAccounts.sol`",
            "items": {
              "title": "subaccount_ids",
              "type": "integer"
            }
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Ethereum wallet address"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```