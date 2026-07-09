# Set Cancel On Disconnect

Enables cancel on disconnect for the account
Required minimum session key permission level is `account`

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
    "/private/set_cancel_on_disconnect": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Set Cancel On Disconnect",
        "description": "Enables cancel on disconnect for the account\nRequired minimum session key permission level is `account`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateSetCancelOnDisconnectResponseSchema"
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
                "$ref": "#/components/schemas/PrivateSetCancelOnDisconnectParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateSetCancelOnDisconnectParamsSchema": {
        "required": [
          "enabled",
          "wallet"
        ],
        "type": "object",
        "properties": {
          "enabled": {
            "title": "enabled",
            "type": "boolean",
            "description": "Whether to enable or disable cancel on disconnect"
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Public key (wallet) of the account"
          }
        },
        "additionalProperties": false
      },
      "PrivateSetCancelOnDisconnectResponseSchema": {
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
            "title": "result",
            "type": "string",
            "enum": [
              "ok"
            ],
            "description": ""
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```