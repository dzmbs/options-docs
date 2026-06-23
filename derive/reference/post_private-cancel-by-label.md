> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel By Label

Cancel all open orders for a given subaccount and a given label.  If instrument_name is provided, only orders for that instrument will be cancelled.
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
    "/private/cancel_by_label": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Cancel By Label",
        "description": "Cancel all open orders for a given subaccount and a given label.  If instrument_name is provided, only orders for that instrument will be cancelled.\nRequired minimum session key permission level is `admin`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateCancelByLabelResponseSchema"
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
                "$ref": "#/components/schemas/PrivateCancelByLabelParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateCancelByLabelParamsSchema": {
        "required": [
          "label",
          "subaccount_id"
        ],
        "properties": {
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "default": null,
            "description": "Instrument name. If not provided, all orders for all instruments with the label will be cancelled.  If provided, request counts as a regular matching request for ratelimit purposes.",
            "nullable": true
          },
          "label": {
            "title": "label",
            "type": "string",
            "description": "Cancel all orders for this label"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateCancelByLabelResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateCancelByLabelResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateCancelByLabelResultSchema": {
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