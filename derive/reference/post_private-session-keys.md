# Session Keys


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
    "/private/session_keys": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Session Keys",
        "description": "\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateSessionKeysResponseSchema"
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
                "$ref": "#/components/schemas/PrivateSessionKeysParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateSessionKeysParamsSchema": {
        "type": "object",
        "required": [
          "wallet"
        ],
        "properties": {
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Ethereum wallet address of account"
          }
        },
        "additionalProperties": false
      },
      "PrivateSessionKeysResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateSessionKeysResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateSessionKeysResultSchema": {
        "type": "object",
        "required": [
          "public_session_keys"
        ],
        "properties": {
          "public_session_keys": {
            "title": "public_session_keys",
            "type": "array",
            "description": "List of session keys (includes unactivated and expired keys)",
            "items": {
              "$ref": "#/components/schemas/SessionKeyResponseSchema"
            }
          }
        },
        "additionalProperties": false
      },
      "SessionKeyResponseSchema": {
        "type": "object",
        "required": [
          "expiry_sec",
          "ip_whitelist",
          "label",
          "public_session_key",
          "registered_sec",
          "scope"
        ],
        "properties": {
          "expiry_sec": {
            "title": "expiry_sec",
            "type": "integer",
            "description": "Session key expiry timestamp in sec"
          },
          "ip_whitelist": {
            "title": "ip_whitelist",
            "type": "array",
            "description": "List of whitelisted IPs, if empty then any IP is allowed.",
            "items": {
              "title": "ip_whitelist",
              "type": "string"
            }
          },
          "label": {
            "title": "label",
            "type": "string",
            "description": "User-defined session key label"
          },
          "public_session_key": {
            "title": "public_session_key",
            "type": "string",
            "description": "Public session key address (Ethereum EOA)"
          },
          "registered_sec": {
            "title": "registered_sec",
            "type": "integer",
            "description": "Session key registration time"
          },
          "scope": {
            "title": "scope",
            "type": "string",
            "description": "Session key permission level scope"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```