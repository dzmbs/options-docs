> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Rfq

Requests two-sided quotes from participating market makers.
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
    "/private/send_rfq": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Send Rfq",
        "description": "Requests two-sided quotes from participating market makers.\nRequired minimum session key permission level is `account`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateSendRfqResponseSchema"
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
                "$ref": "#/components/schemas/PrivateSendRfqParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "LegUnpricedSchema": {
        "required": [
          "amount",
          "direction",
          "instrument_name"
        ],
        "type": "object",
        "properties": {
          "amount": {
            "title": "amount",
            "type": "string",
            "format": "decimal",
            "description": "Amount in units of the base"
          },
          "direction": {
            "title": "direction",
            "type": "string",
            "enum": [
              "buy",
              "sell"
            ],
            "description": "Leg direction"
          },
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Instrument name"
          }
        },
        "additionalProperties": false
      },
      "PrivateSendRfqParamsSchema": {
        "required": [
          "legs",
          "subaccount_id"
        ],
        "type": "object",
        "properties": {
          "client": {
            "title": "client",
            "type": "string",
            "default": "",
            "description": "Optional client that sent RFQ"
          },
          "counterparties": {
            "title": "counterparties",
            "type": "array",
            "default": null,
            "description": "Optional list of market maker account addresses to request quotes from. If not supplied, all market makers who are approved as RFQ makers will be notified.",
            "items": {
              "title": "counterparties",
              "type": "string"
            },
            "nullable": true
          },
          "extra_fee": {
            "title": "extra_fee",
            "type": "string",
            "format": "decimal",
            "default": "0",
            "description": "Extra fee in USDC added to the total final fee paid by user and directly sent to client / builder (must be between 0.000001 and 1000 USDC). The `referral_code` field must also be filled out. See Builder Fee page in docs for more info."
          },
          "label": {
            "title": "label",
            "type": "string",
            "default": "",
            "description": "Optional user-defined label for the RFQ"
          },
          "legs": {
            "title": "legs",
            "type": "array",
            "description": "RFQ legs",
            "items": {
              "$ref": "#/components/schemas/LegUnpricedSchema"
            }
          },
          "max_total_cost": {
            "title": "max_total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "An optional max total cost for the RFQ. Only used when the RFQ sender executes as buyer. Polling endpoints and channels will ignore quotes where the total cost across all legs is above this value. Positive values mean the RFQ sender expects to pay $, negative mean the RFQ sender expects to receive $.This field is not disclosed to the market makers.",
            "nullable": true
          },
          "min_total_cost": {
            "title": "min_total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "An optional min total cost for the RFQ. Only used when the RFQ sender executes as seller. Polling endpoints and channels will ignore quotes where the total cost across all legs is below this value. Positive values mean the RFQ sender expects to receive $, negative mean the RFQ sender expects to pay $.This field is not disclosed to the market makers.",
            "nullable": true
          },
          "partial_fill_step": {
            "title": "partial_fill_step",
            "type": "string",
            "format": "decimal",
            "default": "1",
            "description": "Optional step size for partial fills. If not supplied, the RFQ will not support partial fills."
          },
          "preferred_direction": {
            "title": "preferred_direction",
            "type": "string",
            "default": null,
            "enum": [
              "buy",
              "sell"
            ],
            "description": "If disclosed, the direction the user is aiming to execute as. Default None.",
            "nullable": true
          },
          "referral_code": {
            "title": "referral_code",
            "type": "string",
            "default": "",
            "description": "Optional referral code for the RFQ"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          }
        },
        "additionalProperties": false
      },
      "PrivateSendRfqResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateSendRfqResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateSendRfqResultSchema": {
        "required": [
          "ask_total_cost",
          "bid_total_cost",
          "cancel_reason",
          "counterparties",
          "creation_timestamp",
          "filled_direction",
          "filled_pct",
          "label",
          "last_update_timestamp",
          "legs",
          "mark_total_cost",
          "max_total_cost",
          "min_total_cost",
          "partial_fill_step",
          "preferred_direction",
          "reducing_direction",
          "rfq_id",
          "status",
          "subaccount_id",
          "total_cost",
          "valid_until",
          "wallet"
        ],
        "type": "object",
        "properties": {
          "ask_total_cost": {
            "title": "ask_total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Ask total cost for the RFQ implied from orderbook (as `sell`)",
            "nullable": true
          },
          "bid_total_cost": {
            "title": "bid_total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Bid total cost for the RFQ implied from orderbook (as `buy`)",
            "nullable": true
          },
          "cancel_reason": {
            "title": "cancel_reason",
            "type": "string",
            "enum": [
              "",
              "user_request",
              "insufficient_margin",
              "signed_max_fee_too_low",
              "mmp_trigger",
              "cancel_on_disconnect",
              "session_key_deregistered",
              "subaccount_withdrawn",
              "rfq_no_longer_open",
              "compliance"
            ],
            "description": "Cancel reason, if any"
          },
          "counterparties": {
            "title": "counterparties",
            "type": "array",
            "default": null,
            "description": "List of requested counterparties, if applicable",
            "items": {
              "title": "counterparties",
              "type": "string"
            },
            "nullable": true
          },
          "creation_timestamp": {
            "title": "creation_timestamp",
            "type": "integer",
            "description": "Creation timestamp in ms since Unix epoch"
          },
          "filled_direction": {
            "title": "filled_direction",
            "type": "string",
            "default": null,
            "enum": [
              "buy",
              "sell"
            ],
            "description": "Direction at which the RFQ was filled (only if filled)",
            "nullable": true
          },
          "filled_pct": {
            "title": "filled_pct",
            "type": "string",
            "format": "decimal",
            "description": "Percentage of the RFQ that has been filled, from 0 to 1."
          },
          "label": {
            "title": "label",
            "type": "string",
            "description": "User-defined label, if any"
          },
          "last_update_timestamp": {
            "title": "last_update_timestamp",
            "type": "integer",
            "description": "Last update timestamp in ms since Unix epoch"
          },
          "legs": {
            "title": "legs",
            "type": "array",
            "description": "RFQ legs",
            "items": {
              "$ref": "#/components/schemas/LegUnpricedSchema"
            }
          },
          "mark_total_cost": {
            "title": "mark_total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Mark total cost for the RFQ (assuming `buy` direction)",
            "nullable": true
          },
          "max_total_cost": {
            "title": "max_total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Max total cost for the RFQ",
            "nullable": true
          },
          "min_total_cost": {
            "title": "min_total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Min total cost for the RFQ",
            "nullable": true
          },
          "partial_fill_step": {
            "title": "partial_fill_step",
            "type": "string",
            "format": "decimal",
            "description": "Step size for partial fills (default: 1)"
          },
          "preferred_direction": {
            "title": "preferred_direction",
            "type": "string",
            "default": null,
            "enum": [
              "buy",
              "sell"
            ],
            "description": "If disclosed, the direction the user is aiming to execute as.",
            "nullable": true
          },
          "reducing_direction": {
            "title": "reducing_direction",
            "type": "string",
            "default": null,
            "enum": [
              "buy",
              "sell"
            ],
            "description": "If applicable, the direction from user's perspective that would reduce their position in each leg.",
            "nullable": true
          },
          "rfq_id": {
            "title": "rfq_id",
            "type": "string",
            "format": "uuid",
            "description": "RFQ ID"
          },
          "status": {
            "title": "status",
            "type": "string",
            "enum": [
              "open",
              "filled",
              "cancelled",
              "expired"
            ],
            "description": "Status"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          },
          "total_cost": {
            "title": "total_cost",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Total cost for the RFQ (only if filled)",
            "nullable": true
          },
          "valid_until": {
            "title": "valid_until",
            "type": "integer",
            "description": "RFQ expiry timestamp in ms since Unix epoch"
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Wallet address of the RFQ sender"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```