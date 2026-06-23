> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Notifications

RPC to mark specified notifications as seen for a given subaccount.
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
    "/private/update_notifications": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Update Notifications",
        "description": "RPC to mark specified notifications as seen for a given subaccount.\nRequired minimum session key permission level is `account`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateUpdateNotificationsResponseSchema"
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
                "$ref": "#/components/schemas/PrivateUpdateNotificationsParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateUpdateNotificationsParamsSchema": {
        "required": [
          "notification_ids",
          "subaccount_id"
        ],
        "properties": {
          "notification_ids": {
            "title": "notification_ids",
            "type": "array",
            "description": "List of notification IDs to be marked as seen",
            "items": {
              "title": "notification_ids",
              "type": "integer"
            }
          },
          "status": {
            "title": "status",
            "type": "string",
            "default": "seen",
            "enum": [
              "unseen",
              "seen",
              "hidden"
            ],
            "description": "Status of the notification"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount_id"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateUpdateNotificationsResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateUpdateNotificationsResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateUpdateNotificationsResultSchema": {
        "required": [
          "updated_count"
        ],
        "properties": {
          "updated_count": {
            "title": "updated_count",
            "type": "integer",
            "description": "Number of notifications marked as seen"
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```