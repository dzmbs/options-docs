# Get Erc20 Transfer History

Get erc20 transfer history for a subaccount or wallet.<br /><br />Position transfers (e.g. options or perps) are treated as trades. Use `private/get_trade_history` for position transfer history.
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
    "/private/get_erc20_transfer_history": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Get Erc20 Transfer History",
        "description": "Get erc20 transfer history for a subaccount or wallet.<br /><br />Position transfers (e.g. options or perps) are treated as trades. Use `private/get_trade_history` for position transfer history.\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateGetErc20TransferHistoryResponseSchema"
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
                "$ref": "#/components/schemas/PrivateGetErc20TransferHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PrivateGetErc20TransferHistoryParamsSchema": {
        "type": "object",
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
            "default": null,
            "description": "Subaccount id (must be set if wallet is blank)",
            "nullable": true
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "default": null,
            "description": "Wallet address (if set, subaccount_id ignored)",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "PrivateGetErc20TransferHistoryResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateGetErc20TransferHistoryResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateGetErc20TransferHistoryResultSchema": {
        "type": "object",
        "required": [
          "events"
        ],
        "properties": {
          "events": {
            "title": "events",
            "type": "array",
            "description": "List of erc20 transfers",
            "items": {
              "$ref": "#/components/schemas/ERC20TransferSchema"
            }
          }
        },
        "additionalProperties": false
      },
      "ERC20TransferSchema": {
        "type": "object",
        "required": [
          "amount",
          "asset",
          "counterparty_subaccount_id",
          "is_outgoing",
          "subaccount_id",
          "timestamp",
          "tx_hash"
        ],
        "properties": {
          "amount": {
            "title": "amount",
            "type": "string",
            "format": "decimal",
            "description": "Amount withdrawn by the subaccount"
          },
          "asset": {
            "title": "asset",
            "type": "string",
            "description": "Asset withdrawn"
          },
          "counterparty_subaccount_id": {
            "title": "counterparty_subaccount_id",
            "type": "integer",
            "description": "Recipient or sender subaccount_id of transfer"
          },
          "is_outgoing": {
            "title": "is_outgoing",
            "type": "boolean",
            "description": "True if the transfer was initiated by the subaccount, False otherwise"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID of the subaccount involved in the transfer"
          },
          "timestamp": {
            "title": "timestamp",
            "type": "integer",
            "description": "Timestamp of the transfer (in ms since UNIX epoch)"
          },
          "tx_hash": {
            "title": "tx_hash",
            "type": "string",
            "description": "Hash of the transaction that withdrew the funds"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```