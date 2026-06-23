> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer Position

Transfers a positions from one subaccount to another, owned by the same wallet.<br /><br />The transfer is executed as a pair of orders crossing each other.<br />The maker order is created first, followed by a taker order crossing it.<br />The order amounts, limit prices and instrument name must be the same for both orders.<br />Fee is not charged and a zero `max_fee` must be signed.<br />The maker order is forcibly considered to be `reduce_only`, meaning it can only reduce the position size.<br /><br />History: For position transfer history, use the `private/get_trade_history` RPC (not `private/get_erc20_transfer_history`).
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
    "/private/transfer_position": {
      "post": {
        "tags": [
          "Private"
        ],
        "summary": "Transfer Position",
        "description": "Transfers a positions from one subaccount to another, owned by the same wallet.<br /><br />The transfer is executed as a pair of orders crossing each other.<br />The maker order is created first, followed by a taker order crossing it.<br />The order amounts, limit prices and instrument name must be the same for both orders.<br />Fee is not charged and a zero `max_fee` must be signed.<br />The maker order is forcibly considered to be `reduce_only`, meaning it can only reduce the position size.<br /><br />History: For position transfer history, use the `private/get_trade_history` RPC (not `private/get_erc20_transfer_history`).\nRequired minimum session key permission level is `admin`",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateTransferPositionResponseSchema"
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
                "$ref": "#/components/schemas/PrivateTransferPositionParamsSchema"
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
        "type": "object",
        "additionalProperties": false
      },
      "PrivateTransferPositionParamsSchema": {
        "required": [
          "maker_params",
          "taker_params",
          "wallet"
        ],
        "properties": {
          "maker_params": {
            "$ref": "#/components/schemas/TradeModuleParamsSchema"
          },
          "taker_params": {
            "$ref": "#/components/schemas/TradeModuleParamsSchema"
          },
          "wallet": {
            "title": "wallet",
            "type": "string",
            "description": "Public key (wallet) of the account"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "TradeModuleParamsSchema": {
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
        "properties": {
          "amount": {
            "title": "amount",
            "type": "string",
            "format": "decimal",
            "description": "Order amount in units of the base"
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
          "instrument_name": {
            "title": "instrument_name",
            "type": "string",
            "description": "Instrument name"
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
          "nonce": {
            "title": "nonce",
            "type": "integer",
            "description": "Unique nonce defined as (UTC_timestamp in ms)(random_number_up_to_3_digits) (e.g. 1695836058725001, where 001 is the random number).<br />Note, using a random number beyond 3 digits will cause JSON serialization to fail."
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
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateTransferPositionResponseSchema": {
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
            "$ref": "#/components/schemas/PrivateTransferPositionResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PrivateTransferPositionResultSchema": {
        "required": [
          "maker_order",
          "maker_trade",
          "taker_order",
          "taker_trade"
        ],
        "properties": {
          "maker_order": {
            "$ref": "#/components/schemas/OrderResponseSchema"
          },
          "maker_trade": {
            "$ref": "#/components/schemas/TradeResponseSchema"
          },
          "taker_order": {
            "$ref": "#/components/schemas/OrderResponseSchema"
          },
          "taker_trade": {
            "$ref": "#/components/schemas/TradeResponseSchema"
          }
        },
        "type": "object",
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
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```