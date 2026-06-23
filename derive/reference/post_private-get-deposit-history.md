> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Deposit History

Get subaccount deposit history.
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
    "/private/get_deposit_history": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Get Deposit History",
        "description": "Get subaccount deposit history.\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateGetDepositHistoryResponseSchema"
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
                "$ref": "#/components/schemas/PrivateGetDepositHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateGetDepositHistoryParamsSchema": {
        "required": [
          "subaccount_id"
        ],
        "properties": {
          "end_timestamp": {
            "title": "end_timestamp",
            "type": "integer",
            "default": 9223372036854776000,
            "description": "End timestamp of the event history in ms since Unix epoch (default current time)"
          },
          "start_timestamp": {
            "title": "start_timestamp",
            "type": "integer",
            "default": 0,
            "description": "Start timestamp of the event history in ms since Unix epoch (default 0)"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount id"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateGetDepositHistoryResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateGetDepositHistoryResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateGetDepositHistoryResultSchema": {
        "required": [
          "events"
        ],
        "properties": {
          "events": {
            "title": "events",
            "type": "array",
            "description": "List of deposit payments",
            "items": {
              "$ref": "#/components/schemas/DepositSchema"
            }
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "DepositSchema": {
        "required": [
          "amount",
          "asset",
          "error_log",
          "timestamp",
          "transaction_id",
          "tx_hash",
          "tx_status"
        ],
        "properties": {
          "amount": {
            "title": "amount",
            "type": "string",
            "format": "decimal",
            "description": "Amount deposited by the subaccount"
          },
          "asset": {
            "title": "asset",
            "type": "string",
            "description": "Asset deposited"
          },
          "error_log": {
            "title": "error_log",
            "type": "object",
            "default": null,
            "description": "If failed, error log for reason",
            "additionalProperties": {},
            "nullable": true
          },
          "timestamp": {
            "title": "timestamp",
            "type": "integer",
            "description": "Timestamp of the deposit (in ms since UNIX epoch)"
          },
          "transaction_id": {
            "title": "transaction_id",
            "type": "string",
            "format": "uuid",
            "description": "Transaction ID"
          },
          "tx_hash": {
            "title": "tx_hash",
            "type": "string",
            "description": "Hash of the transaction that deposited the funds"
          },
          "tx_status": {
            "title": "tx_status",
            "type": "string",
            "enum": [
              "requested",
              "pending",
              "settled",
              "reverted",
              "ignored",
              "timed_out"
            ],
            "description": "Status of the transaction that deposited the funds"
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```