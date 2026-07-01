> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel All Trigger Orders

Cancel all trigger orders for this subaccount.<br /><br />Also used by cancel_all in WS.
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
    "/private/cancel_all_trigger_orders": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Cancel All Trigger Orders",
        "description": "Cancel all trigger orders for this subaccount.<br /><br />Also used by cancel_all in WS.\nRequired minimum session key permission level is `admin`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateCancelAllTriggerOrdersResponseSchema"
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
                "$ref": "#/components/schemas/PrivateCancelAllTriggerOrdersParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateCancelAllTriggerOrdersParamsSchema": {
        "required": [
          "subaccount_id"
        ],
        "type": "object",
        "properties": {
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer"
          }
        },
        "additionalProperties": false
      },
      "PrivateCancelAllTriggerOrdersResponseSchema": {
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