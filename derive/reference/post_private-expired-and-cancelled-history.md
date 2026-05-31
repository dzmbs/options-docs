# Expired And Cancelled History

Generate a list of URLs to retrieve archived orders
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
    "/private/expired_and_cancelled_history": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Expired And Cancelled History",
        "description": "Generate a list of URLs to retrieve archived orders\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateExpiredAndCancelledHistoryResponseSchema"
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
                "$ref": "#/components/schemas/PrivateExpiredAndCancelledHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateExpiredAndCancelledHistoryParamsSchema": {
        "type": "object",
        "required": [
          "end_timestamp",
          "expiry",
          "start_timestamp",
          "subaccount_id",
          "wallet"
        ],
        "properties": {
          "end_timestamp": {
            "title": "end_timestamp",
            "type": "integer",
            "description": "End Unix timestamp"
          },
          "expiry": {
            "title": "expiry",
            "type": "integer",
            "description": "Expiry of download link in seconds. Maximum of 604800."
          },
          "start_timestamp": {
            "title": "start_timestamp",
            "type": "integer",
            "description": "Start Unix timestamp"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount to download data for"
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Wallet to download data for"
          }
        },
        "additionalProperties": false
      },
      "PrivateExpiredAndCancelledHistoryResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateExpiredAndCancelledHistoryResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateExpiredAndCancelledHistoryResultSchema": {
        "type": "object",
        "required": [
          "presigned_urls"
        ],
        "properties": {
          "presigned_urls": {
            "title": "presigned_urls",
            "type": "array",
            "description": "List of presigned URLs to the snapshots",
            "items": {
              "title": "presigned_urls",
              "type": "string"
            }
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```