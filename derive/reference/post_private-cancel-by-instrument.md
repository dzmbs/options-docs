> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel By Instrument

Cancel all orders for this instrument.
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
    "/private/cancel_by_instrument": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Cancel By Instrument",
        "description": "Cancel all orders for this instrument.\nRequired minimum session key permission level is `admin`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateCancelByInstrumentResponseSchema"
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
                "$ref": "#/components/schemas/PrivateCancelByInstrumentParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateCancelByInstrumentParamsSchema": {
        "required": [
          "instrument_name",
          "subaccount_id"
        ],
        "type": "object",
        "properties": {
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Cancel all orders for this instrument"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          }
        },
        "additionalProperties": false
      },
      "PrivateCancelByInstrumentResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateCancelByInstrumentResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateCancelByInstrumentResultSchema": {
        "required": [
          "cancelled_orders"
        ],
        "type": "object",
        "properties": {
          "cancelled_orders": {
            "title": "cancelled_orders",
            "type": "integer",
            "description": "Number of cancelled orders"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```