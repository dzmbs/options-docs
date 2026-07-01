> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Subaccount Value History

Get the value history of a subaccount.<br />Supported periods: 900 (15m), 3600 (1h), 86400 (1d), 604800 (1w).<br />Returns up to 1000 entries per request. If the time range exceeds 1000 * period seconds,<br />the start is clamped forward to return the most recent 1000 entries.
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
    "/private/get_subaccount_value_history": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Get Subaccount Value History",
        "description": "Get the value history of a subaccount.<br />Supported periods: 900 (15m), 3600 (1h), 86400 (1d), 604800 (1w).<br />Returns up to 1000 entries per request. If the time range exceeds 1000 * period seconds,<br />the start is clamped forward to return the most recent 1000 entries.\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateGetSubaccountValueHistoryResponseSchema"
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
                "$ref": "#/components/schemas/PrivateGetSubaccountValueHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateGetSubaccountValueHistoryParamsSchema": {
        "required": [
          "end_timestamp",
          "period",
          "start_timestamp",
          "subaccount_id"
        ],
        "type": "object",
        "properties": {
          "end_timestamp": {
            "title": "end_timestamp",
            "type": "integer",
            "description": "End timestamp in unix seconds"
          },
          "period": {
            "title": "period",
            "type": "integer",
            "description": "Period in seconds. One of 900, 3600, 86400, 604800"
          },
          "start_timestamp": {
            "title": "start_timestamp",
            "type": "integer",
            "description": "Start timestamp in unix seconds"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount_id"
          }
        },
        "additionalProperties": false
      },
      "PrivateGetSubaccountValueHistoryResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateGetSubaccountValueHistoryResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateGetSubaccountValueHistoryResultSchema": {
        "required": [
          "subaccount_id",
          "subaccount_value_history"
        ],
        "type": "object",
        "properties": {
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount_id"
          },
          "subaccount_value_history": {
            "title": "subaccount_value_history",
            "type": "array",
            "description": "Subaccount value history",
            "items": {
              "$ref": "#/components/schemas/SubAccountValueHistoryResponseSchema"
            }
          }
        },
        "additionalProperties": false
      },
      "SubAccountValueHistoryResponseSchema": {
        "required": [
          "currency",
          "delayed_maintenance_margin",
          "initial_margin",
          "maintenance_margin",
          "margin_type",
          "subaccount_value",
          "timestamp"
        ],
        "type": "object",
        "properties": {
          "currency": {
            "title": "currency",
            "type": "string",
            "description": "Currency of the manager (empty string for SRM)"
          },
          "delayed_maintenance_margin": {
            "title": "delayed_maintenance_margin",
            "type": "string",
            "format": "decimal",
            "description": "Delayed liquidation maintenance margin (0 if not applicable)"
          },
          "initial_margin": {
            "title": "initial_margin",
            "type": "string",
            "format": "decimal",
            "description": "Initial margin requirement"
          },
          "maintenance_margin": {
            "title": "maintenance_margin",
            "type": "string",
            "format": "decimal",
            "description": "Maintenance margin requirement"
          },
          "margin_type": {
            "title": "margin_type",
            "type": "string",
            "description": "Margin type of the subaccount (e.g. PM, PM2, SM)"
          },
          "subaccount_value": {
            "title": "subaccount_value",
            "type": "string",
            "format": "decimal",
            "description": "Total mark-to-market value of all positions and collaterals"
          },
          "timestamp": {
            "title": "timestamp",
            "type": "integer",
            "description": "Timestamp of when the subaccount value was recorded into the database"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```