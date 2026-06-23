> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Poll Rfqs

Retrieves a list of RFQs matching filter criteria. Market makers can use this to poll RFQs directed to them.
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
    "/private/poll_rfqs": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Poll Rfqs",
        "description": "Retrieves a list of RFQs matching filter criteria. Market makers can use this to poll RFQs directed to them.\nRequired minimum session key permission level is `read_only`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivatePollRfqsResponseSchema"
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
                "$ref": "#/components/schemas/PrivatePollRfqsParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PaginationInfoSchema": {
        "required": [
          "count",
          "num_pages"
        ],
        "properties": {
          "count": {
            "title": "count",
            "type": "integer",
            "description": "Total number of items, across all pages"
          },
          "num_pages": {
            "title": "num_pages",
            "type": "integer",
            "description": "Number of pages"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivatePollRfqsParamsSchema": {
        "required": [
          "subaccount_id"
        ],
        "properties": {
          "from_timestamp": {
            "title": "from_timestamp",
            "type": "integer",
            "default": 0,
            "description": "Earliest `last_update_timestamp` to filter by (in ms since Unix epoch). If not provied, defaults to 0."
          },
          "page": {
            "title": "page",
            "type": "integer",
            "default": 1,
            "description": "Page number of results to return (default 1, returns last if above `num_pages`)"
          },
          "page_size": {
            "title": "page_size",
            "type": "integer",
            "default": 100,
            "description": "Number of results per page (default 100, max 1000)"
          },
          "rfq_id": {
            "title": "rfq_id",
            "type": "string",
            "format": "uuid",
            "default": null,
            "description": "RFQ ID filter, if applicable",
            "nullable": true
          },
          "rfq_subaccount_id": {
            "title": "rfq_subaccount_id",
            "type": "integer",
            "default": null,
            "description": "Filter returned RFQs by rfq requestor subaccount",
            "nullable": true
          },
          "status": {
            "title": "status",
            "type": "string",
            "default": null,
            "enum": [
              "open",
              "filled",
              "cancelled",
              "expired"
            ],
            "description": "RFQ status filter, if applicable",
            "nullable": true
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID for auth purposes, returned data will be scoped to this subaccount."
          },
          "to_timestamp": {
            "title": "to_timestamp",
            "type": "integer",
            "default": 18446744073709552000,
            "description": "Latest `last_update_timestamp` to filter by (in ms since Unix epoch). If not provied, defaults to returning all data up to current time."
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivatePollRfqsResponseSchema": {
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
            "$ref": "#/components/schemas/PrivatePollRfqsResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivatePollRfqsResultSchema": {
        "required": [
          "pagination",
          "rfqs"
        ],
        "properties": {
          "pagination": {
            "$ref": "#/components/schemas/PaginationInfoSchema"
          },
          "rfqs": {
            "title": "rfqs",
            "type": "array",
            "description": "RFQs matching filter criteria",
            "items": {
              "$ref": "#/components/schemas/RFQResultPublicSchema"
            }
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "RFQResultPublicSchema": {
        "required": [
          "cancel_reason",
          "creation_timestamp",
          "fill_rate",
          "filled_direction",
          "filled_pct",
          "last_update_timestamp",
          "legs",
          "partial_fill_step",
          "preferred_direction",
          "recent_fill_rate",
          "reducing_direction",
          "rfq_id",
          "status",
          "subaccount_id",
          "total_cost",
          "valid_until",
          "wallet"
        ],
        "properties": {
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
          "creation_timestamp": {
            "title": "creation_timestamp",
            "type": "integer",
            "description": "Creation timestamp in ms since Unix epoch"
          },
          "fill_rate": {
            "title": "fill_rate",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Average taker fill rate, from 0 to 1. Returns null for users with insufficient RFQ history.",
            "nullable": true
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
          "recent_fill_rate": {
            "title": "recent_fill_rate",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Taker fill rate, weighted towards the recent several days of activity, from 0 to 1. Returns null for users with insufficient recent RFQ history.",
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
        "type": "object",
        "additionalProperties": false
      },
      "LegUnpricedSchema": {
        "required": [
          "amount",
          "direction",
          "instrument_name"
        ],
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
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```