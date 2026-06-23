> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Reset Mmp

Resets (unfreezes) the mmp state for a subaccount (optionally filtered by currency)
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
    "/private/reset_mmp": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Reset Mmp",
        "description": "Resets (unfreezes) the mmp state for a subaccount (optionally filtered by currency)\nRequired minimum session key permission level is `account`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateResetMmpResponseSchema"
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
                "$ref": "#/components/schemas/PrivateResetMmpParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateResetMmpParamsSchema": {
        "required": [
          "subaccount_id"
        ],
        "properties": {
          "currency": {
            "title": "currency",
            "type": "string",
            "default": null,
            "description": "Currency to reset the mmp for. If not provided, resets all configs for the subaccount",
            "nullable": true
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount_id for which to reset the mmp state"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateResetMmpResponseSchema": {
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
            "type": "string",
            "enum": [
              "ok"
            ],
            "description": "The result of this method call, `ok` if successful"
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```