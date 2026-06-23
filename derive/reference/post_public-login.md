> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Login

Authenticate a websocket connection. Unavailable via HTTP.

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
    "/public/login": {
      "post": {
        "tags": [
          "Public"
        ],
        "summary": "Login",
        "description": "Authenticate a websocket connection. Unavailable via HTTP.",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicLoginResponseSchema"
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
                "$ref": "#/components/schemas/PublicLoginParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PublicLoginParamsSchema": {
        "required": [
          "signature",
          "timestamp",
          "wallet"
        ],
        "properties": {
          "signature": {
            "title": "signature",
            "type": "string",
            "description": "Signature of the timestamp, signed with the wallet's private key or a session key"
          },
          "timestamp": {
            "title": "timestamp",
            "type": "string",
            "description": "Message that was signed, in the form of a timestamp in ms since Unix epoch"
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Public key (wallet) of the account"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PublicLoginResponseSchema": {
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
            "title": "result",
            "type": "array",
            "description": "List of subaccount IDs that have been authenticated",
            "items": {
              "title": "result",
              "type": "integer"
            }
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```