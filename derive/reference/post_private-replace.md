# Replace

Cancel an existing order with nonce or order_id and create new order with different order_id in a single RPC call.<br /><br />If the cancel fails, the new order will not be created.<br />If the cancel succeeds but the new order fails, the old order will still be cancelled.
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
    "/private/replace": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Replace",
        "description": "Cancel an existing order with nonce or order_id and create new order with different order_id in a single RPC call.<br /><br />If the cancel fails, the new order will not be created.<br />If the cancel succeeds but the new order fails, the old order will still be cancelled.\nRequired minimum session key permission level is `admin`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateReplaceResponseSchema"
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
                "$ref": "#/components/schemas/PrivateReplaceParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "OrderResponseSchema": {
        "required": [
          "amount",
          "average_price",
          "cancel_reason",
          "creation_timestamp",
          "direction",
          "filled_amount",
          "instrument_name",
          "is_transfer",
          "label",
          "last_update_timestamp",
          "limit_price",
          "max_fee",
          "mmp",
          "nonce",
          "order_fee",
          "order_id",
          "order_status",
          "order_type",
          "quote_id",
          "signature",
          "signature_expiry_sec",
          "signer",
          "subaccount_id",
          "time_in_force"
        ],
        "type": "object",
        "properties": {
          "algo_duration_sec": {
            "title": "algo_duration_sec",
            "type": "integer",
            "default": null,
            "description": "Total execution window in seconds",
            "nullable": true
          },
          "algo_num_slices": {
            "title": "algo_num_slices",
            "type": "integer",
            "default": null,
            "description": "Number of child executions",
            "nullable": true
          },
          "algo_slices_completed": {
            "title": "algo_slices_completed",
            "type": "integer",
            "default": null,
            "description": "Number of slices executed so far",
            "nullable": true
          },
          "algo_type": {
            "title": "algo_type",
            "type": "string",
            "default": null,
            "enum": [
              "twap"
            ],
            "description": "Algo order type (twap or vwap)",
            "nullable": true
          },
          "amount": {
            "title": "amount",
            "type": "string",
            "format": "decimal",
            "description": "Order amount in units of the base"
          },
          "average_price": {
            "title": "average_price",
            "type": "string",
            "format": "decimal",
            "description": "Average fill price"
          },
          "cancel_reason": {
            "title": "cancel_reason",
            "type": "string",
            "enum": [
              "",
              "user_request",
              "mmp_trigger",
              "insufficient_margin",
              "signed_max_fee_too_low",
              "cancel_on_disconnect",
              "ioc_or_market_partial_fill",
              "session_key_deregistered",
              "subaccount_withdrawn",
              "compliance",
              "trigger_failed",
              "validation_failed",
              "algo_completed"
            ],
            "description": "If cancelled, reason behind order cancellation"
          },
          "creation_timestamp": {
            "title": "creation_timestamp",
            "type": "integer",
            "description": "Creation timestamp (in ms since Unix epoch)"
          },
          "direction": {
            "title": "direction",
            "type": "string",
            "enum": [
              "buy",
              "sell"
            ],
            "description": "Order direction"
          },
          "extra_fee": {
            "title": "extra_fee",
            "type": "string",
            "format": "decimal",
            "default": "0",
            "description": "(Optional) Extra fee in USDC added to the total final fee paid by user (must be between 0.000001 and 1,000 USDC).",
            "nullable": true
          },
          "filled_amount": {
            "title": "filled_amount",
            "type": "string",
            "format": "decimal",
            "description": "Total filled amount for the order"
          },
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Instrument name"
          },
          "is_transfer": {
            "title": "is_transfer",
            "type": "boolean",
            "description": "Whether the order was generated through `private/transfer_position`"
          },
          "label": {
            "title": "label",
            "type": "string",
            "description": "Optional user-defined label for the order"
          },
          "last_update_timestamp": {
            "title": "last_update_timestamp",
            "type": "integer",
            "description": "Last update timestamp (in ms since Unix epoch)"
          },
          "limit_price": {
            "title": "limit_price",
            "type": "string",
            "format": "decimal",
            "description": "Limit price in quote currency"
          },
          "max_fee": {
            "title": "max_fee",
            "type": "string",
            "format": "decimal",
            "description": "Max fee PER contract, denominated in USDC.Max fee must be > 2 x max(taker_fee, maker_fee) x spot_price + extra_fee / amount.If the order crosses the book, it must be >= 2 x max(taker_fee, maker_fee) x spot_price + base_fee / fill_amount + extra_fee / amount.Note, in this calculation, regardless of the account taker / maker fees, the standard taker / maker fees are used."
          },
          "mmp": {
            "title": "mmp",
            "type": "boolean",
            "description": "Whether the order is tagged for market maker protections"
          },
          "nonce": {
            "title": "nonce",
            "type": "integer",
            "description": "Unique nonce defined as (UTC_timestamp in ms)(random_number_up_to_3_digits) (e.g. 1695836058725001, where 001 is the random number)"
          },
          "order_fee": {
            "title": "order_fee",
            "type": "string",
            "format": "decimal",
            "description": "Order fee paid so far"
          },
          "order_id": {
            "title": "order_id",
            "type": "string",
            "description": "Order ID"
          },
          "order_status": {
            "title": "order_status",
            "type": "string",
            "enum": [
              "open",
              "filled",
              "cancelled",
              "expired",
              "untriggered",
              "algo_active"
            ],
            "description": "Order status"
          },
          "order_type": {
            "title": "order_type",
            "type": "string",
            "enum": [
              "limit",
              "market"
            ],
            "description": "Order type"
          },
          "quote_id": {
            "title": "quote_id",
            "type": "string",
            "format": "uuid",
            "default": null,
            "description": "Quote ID if the trade was executed via RFQ",
            "nullable": true
          },
          "replaced_order_id": {
            "title": "replaced_order_id",
            "type": "string",
            "format": "uuid",
            "default": null,
            "description": "If replaced, ID of the order that was replaced",
            "nullable": true
          },
          "signature": {
            "title": "signature",
            "type": "string",
            "description": "Ethereum signature of the order"
          },
          "signature_expiry_sec": {
            "title": "signature_expiry_sec",
            "type": "integer",
            "description": "Signature expiry timestamp"
          },
          "signed_limit_price": {
            "title": "signed_limit_price",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "The original limit price that the user signed. Only set when the order was adjusted (i.e., for post-only orders with reject_post_only=false that would have crossed). Used for on-chain submission.",
            "nullable": true
          },
          "signer": {
            "title": "signer",
            "type": "string",
            "description": "Owner wallet address or registered session key that signed order"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          },
          "time_in_force": {
            "title": "time_in_force",
            "type": "string",
            "enum": [
              "gtc",
              "post_only",
              "fok",
              "ioc"
            ],
            "description": "Time in force"
          },
          "trigger_price": {
            "title": "trigger_price",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "(Required for trigger orders) Index or Market price to trigger order at",
            "nullable": true
          },
          "trigger_price_type": {
            "title": "trigger_price_type",
            "type": "string",
            "default": null,
            "enum": [
              "mark",
              "index"
            ],
            "description": "(Required for trigger orders) Trigger with Index or Mark Price",
            "nullable": true
          },
          "trigger_reject_message": {
            "title": "trigger_reject_message",
            "type": "string",
            "default": null,
            "description": "(Required for trigger orders) Error message if error occured during trigger",
            "nullable": true
          },
          "trigger_type": {
            "title": "trigger_type",
            "type": "string",
            "default": null,
            "enum": [
              "stoploss",
              "takeprofit"
            ],
            "description": "(Required for trigger orders) Stop-loss or Take-profit.",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "TradeResponseSchema": {
        "required": [
          "direction",
          "expected_rebate",
          "extra_fee",
          "index_price",
          "instrument_name",
          "is_transfer",
          "label",
          "liquidity_role",
          "mark_price",
          "order_id",
          "quote_id",
          "realized_pnl",
          "realized_pnl_excl_fees",
          "rfq_id",
          "subaccount_id",
          "timestamp",
          "trade_amount",
          "trade_fee",
          "trade_id",
          "trade_price",
          "transaction_id",
          "tx_hash",
          "tx_status"
        ],
        "type": "object",
        "properties": {
          "direction": {
            "title": "direction",
            "type": "string",
            "enum": [
              "buy",
              "sell"
            ],
            "description": "Order direction"
          },
          "expected_rebate": {
            "title": "expected_rebate",
            "type": "string",
            "format": "decimal",
            "description": "Expected rebate for this trade"
          },
          "extra_fee": {
            "title": "extra_fee",
            "type": "string",
            "format": "decimal",
            "description": "Extra fee in USDC added by the referring client (included in trade fee)"
          },
          "index_price": {
            "title": "index_price",
            "type": "string",
            "format": "decimal",
            "description": "Index price of the underlying at the time of the trade"
          },
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Instrument name"
          },
          "is_transfer": {
            "title": "is_transfer",
            "type": "boolean",
            "description": "Whether the trade was generated through `private/transfer_position`"
          },
          "label": {
            "title": "label",
            "type": "string",
            "description": "Optional user-defined label for the order"
          },
          "liquidity_role": {
            "title": "liquidity_role",
            "type": "string",
            "enum": [
              "maker",
              "taker"
            ],
            "description": "Role of the user in the trade"
          },
          "mark_price": {
            "title": "mark_price",
            "type": "string",
            "format": "decimal",
            "description": "Mark price of the instrument at the time of the trade"
          },
          "order_id": {
            "title": "order_id",
            "type": "string",
            "description": "Order ID"
          },
          "quote_id": {
            "title": "quote_id",
            "type": "string",
            "format": "uuid",
            "default": null,
            "description": "Quote ID if the trade was executed via RFQ",
            "nullable": true
          },
          "realized_pnl": {
            "title": "realized_pnl",
            "type": "string",
            "format": "decimal",
            "description": "Realized PnL for this trade"
          },
          "realized_pnl_excl_fees": {
            "title": "realized_pnl_excl_fees",
            "type": "string",
            "format": "decimal",
            "description": "Realized PnL for this trade using cost accounting that excludes fees"
          },
          "rfq_id": {
            "title": "rfq_id",
            "type": "string",
            "format": "uuid",
            "default": null,
            "description": "RFQ ID if the trade was executed via RFQ",
            "nullable": true
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          },
          "timestamp": {
            "title": "timestamp",
            "type": "integer",
            "description": "Trade timestamp (in ms since Unix epoch)"
          },
          "trade_amount": {
            "title": "trade_amount",
            "type": "string",
            "format": "decimal",
            "description": "Amount filled in this trade"
          },
          "trade_fee": {
            "title": "trade_fee",
            "type": "string",
            "format": "decimal",
            "description": "Base_fee (only takers) + unit_fee (adjusted via rebates / discounts) + extra_fee (set by referrring client))"
          },
          "trade_id": {
            "title": "trade_id",
            "type": "string",
            "description": "Trade ID"
          },
          "trade_price": {
            "title": "trade_price",
            "type": "string",
            "format": "decimal",
            "description": "Price at which the trade was filled"
          },
          "transaction_id": {
            "title": "transaction_id",
            "type": "string",
            "description": "The transaction id of the related settlement transaction"
          },
          "tx_hash": {
            "title": "tx_hash",
            "type": "string",
            "default": null,
            "description": "Blockchain transaction hash",
            "nullable": true
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
            "description": "Blockchain transaction status"
          }
        },
        "additionalProperties": false
      },
      "RPCErrorFormatSchema": {
        "required": [
          "code",
          "message"
        ],
        "type": "object",
        "properties": {
          "code": {
            "title": "code",
            "type": "integer"
          },
          "data": {
            "title": "data",
            "type": "string",
            "default": null,
            "nullable": true
          },
          "message": {
            "title": "message",
            "type": "string"
          }
        },
        "additionalProperties": false
      },
      "PrivateReplaceParamsSchema": {
        "required": [
          "amount",
          "direction",
          "instrument_name",
          "limit_price",
          "max_fee",
          "nonce",
          "signature",
          "signature_expiry_sec",
          "signer",
          "subaccount_id"
        ],
        "type": "object",
        "properties": {
          "algo_duration_sec": {
            "title": "algo_duration_sec",
            "type": "integer",
            "default": null,
            "description": "Total execution window in seconds (required for algo orders)",
            "nullable": true
          },
          "algo_num_slices": {
            "title": "algo_num_slices",
            "type": "integer",
            "default": null,
            "description": "Number of child executions to split the order into (required for algo orders)",
            "nullable": true
          },
          "algo_type": {
            "title": "algo_type",
            "type": "string",
            "default": null,
            "enum": [
              "twap"
            ],
            "description": "Algo order type (twap). Cannot be combined with trigger fields.",
            "nullable": true
          },
          "amount": {
            "title": "amount",
            "type": "string",
            "format": "decimal",
            "description": "Order amount in units of the base"
          },
          "client": {
            "title": "client",
            "type": "string",
            "default": "",
            "description": "Client that submitted the order",
            "nullable": true
          },
          "direction": {
            "title": "direction",
            "type": "string",
            "enum": [
              "buy",
              "sell"
            ],
            "description": "Order direction"
          },
          "expected_filled_amount": {
            "title": "expected_filled_amount",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Optional check to only create new order if old order filled_amount is equal to this value.",
            "nullable": true
          },
          "extra_fee": {
            "title": "extra_fee",
            "type": "string",
            "format": "decimal",
            "default": "0",
            "description": "Extra fee in USDC added to the total final fee paid by user and directly sent to client / builder (must be between 0.000001 and 1000 USDC). The `referral_code` field must also be filled out. See Builder Fee page in docs for more info."
          },
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Instrument name"
          },
          "is_atomic_signing": {
            "title": "is_atomic_signing",
            "type": "boolean",
            "default": false,
            "description": "Used by vaults to determine whether the signature is an EIP-1271 signature.",
            "nullable": true
          },
          "label": {
            "title": "label",
            "type": "string",
            "default": "",
            "description": "Optional user-defined label for the order"
          },
          "limit_price": {
            "title": "limit_price",
            "type": "string",
            "format": "decimal",
            "description": "Limit price in quote currency.<br />This field is still required for market orders because it is a component of the signature. However, market orders will not leave a resting order in the book in case of a partial fill."
          },
          "max_fee": {
            "title": "max_fee",
            "type": "string",
            "format": "decimal",
            "description": "Max fee PER contract, denominated in USDC.<br />For resting orders (maker orders), max_fee must be > 2 x max(taker_fee, maker_fee) x spot_price + extra_fee / amount.For crossing orders (taker order), max_fee must be > maker max_fee + base_fee / fill_amount.<br />Note, in this calculation, regardless of the custom account taker / maker fees, the standard taker / maker fees are used.<br />The max(limit_price, index_price) is used to calculate the notional volume."
          },
          "mmp": {
            "title": "mmp",
            "type": "boolean",
            "default": false,
            "description": "Whether the order is tagged for market maker protections (default false)"
          },
          "nonce": {
            "title": "nonce",
            "type": "integer",
            "description": "Unique nonce defined as (UTC_timestamp in ms)(random_number_up_to_3_digits) (e.g. 1695836058725001, where 001 is the random number).<br />Note, using a random number beyond 3 digits will cause JSON serialization to fail."
          },
          "nonce_to_cancel": {
            "title": "nonce_to_cancel",
            "type": "integer",
            "default": null,
            "description": "Cancel order by nonce (choose either order_id or nonce).",
            "nullable": true
          },
          "order_id_to_cancel": {
            "title": "order_id_to_cancel",
            "type": "string",
            "format": "uuid",
            "default": null,
            "description": "Cancel order by order_id (choose either order_id or nonce).",
            "nullable": true
          },
          "order_type": {
            "title": "order_type",
            "type": "string",
            "default": "limit",
            "enum": [
              "limit",
              "market"
            ],
            "description": "Order type:<br />- `limit`: limit order (default)<br />- `market`: market order, note that limit_price is still required for market orders, but unfilled order portion will be marked as cancelled"
          },
          "reduce_only": {
            "title": "reduce_only",
            "type": "boolean",
            "default": false,
            "description": "If true, the order will not be able to increase position's size (default false). If the order amount exceeds available position size, the order will be filled up to the position size and the remainder will be cancelled. This flag is only supported for market orders or non-resting limit orders (IOC or FOK)"
          },
          "referral_code": {
            "title": "referral_code",
            "type": "string",
            "default": "",
            "description": "Optional referral code for the order"
          },
          "reject_post_only": {
            "title": "reject_post_only",
            "type": "boolean",
            "default": true,
            "description": "If true (default), post-only orders that would cross the book are rejected. If false, the limit price is adjusted to be 1 tick away from the BBO instead of rejecting."
          },
          "reject_timestamp": {
            "title": "reject_timestamp",
            "type": "integer",
            "default": 9223372036854776000,
            "description": "UTC timestamp in ms, if provided the matching engine will reject the order with an error if `reject_timestamp` < `server_time`. Note that the timestamp must be consistent with the server time: use `public/get_time` method to obtain current server time."
          },
          "signature": {
            "title": "signature",
            "type": "string",
            "description": "Ethereum signature of the order"
          },
          "signature_expiry_sec": {
            "title": "signature_expiry_sec",
            "type": "integer",
            "description": "Unix timestamp in seconds. Order signature becomes invalid after this time, and the system will cancel the order.<br />Expiry MUST be at least 5 min from now."
          },
          "signer": {
            "title": "signer",
            "type": "string",
            "description": "Owner wallet address or registered session key that signed order"
          },
          "subaccount_id": {
            "title": "subaccount_id",
            "type": "integer",
            "description": "Subaccount ID"
          },
          "time_in_force": {
            "title": "time_in_force",
            "type": "string",
            "default": "gtc",
            "enum": [
              "gtc",
              "post_only",
              "fok",
              "ioc"
            ],
            "description": "Time in force behaviour:<br />- `gtc`: good til cancelled (default)<br />- `post_only`: a limit order that will be rejected if it crosses any order in the book, i.e. acts as a taker order<br />- `fok`: fill or kill, will be rejected if it is not fully filled<br />- `ioc`: immediate or cancel, fill at best bid/ask (market) or at limit price (limit), the unfilled portion is cancelled<br />Note that the order will still expire on the `signature_expiry_sec` timestamp."
          },
          "trigger_price": {
            "title": "trigger_price",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "(Required for trigger orders) \"index\" or \"mark\" price to trigger order at",
            "nullable": true
          },
          "trigger_price_type": {
            "title": "trigger_price_type",
            "type": "string",
            "default": null,
            "enum": [
              "mark",
              "index"
            ],
            "description": "(Required for trigger orders) Trigger with \"mark\" price as \"index\" price type not supported yet.",
            "nullable": true
          },
          "trigger_type": {
            "title": "trigger_type",
            "type": "string",
            "default": null,
            "enum": [
              "stoploss",
              "takeprofit"
            ],
            "description": "(Required for trigger orders) \"stoploss\" or \"takeprofit\"",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "PrivateReplaceResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateReplaceResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PrivateReplaceResultSchema": {
        "required": [
          "cancelled_order"
        ],
        "type": "object",
        "properties": {
          "cancelled_order": {
            "$ref": "#/components/schemas/OrderResponseSchema"
          },
          "create_order_error": {
            "$ref": "#/components/schemas/RPCErrorFormatSchema",
            "nullable": true
          },
          "order": {
            "$ref": "#/components/schemas/OrderResponseSchema",
            "nullable": true
          },
          "trades": {
            "title": "trades",
            "type": "array",
            "default": null,
            "description": "List of trades executed by the created order",
            "items": {
              "$ref": "#/components/schemas/TradeResponseSchema"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```