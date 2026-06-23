> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Change Subaccount Label

Change a user defined label for given subaccount
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
    "/private/change_subaccount_label": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Change Subaccount Label",
        "description": "Change a user defined label for given subaccount\nRequired minimum session key permission level is `account`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateChangeSubaccountLabelResponseSchema"
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
                "$ref": "#/components/schemas/PrivateChangeSubaccountLabelParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateChangeSubaccountLabelParamsSchema": {
        "required": [
          "label",
          "subaccount_id"
        ],
        "properties": {
          "label": {
            "title": "label",
            "type": "string",
            "description": "User defined label"
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
      "PrivateChangeSubaccountLabelResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateChangeSubaccountLabelResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateChangeSubaccountLabelResultSchema": {
        "required": [
          "label",
          "subaccount_id"
        ],
        "properties": {
          "label": {
            "title": "label",
            "type": "string",
            "description": "User defined label"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount_id"
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```