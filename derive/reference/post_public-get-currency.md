> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Currency

Get currency related risk params, spot price 24hrs ago and lending details for a specific currency.

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
    "/public/get_currency": {
      "post": {
        "tags": [
          "Public"
        ],
        "summary": "Get Currency",
        "description": "Get currency related risk params, spot price 24hrs ago and lending details for a specific currency.",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicGetCurrencyResponseSchema"
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
                "$ref": "#/components/schemas/PublicGetCurrencyParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PublicGetCurrencyParamsSchema": {
        "required": [
          "currency"
        ],
        "type": "object",
        "properties": {
          "currency": {
            "title": "currency",
            "type": "string",
            "description": "Underlying currency of asset (`ETH`, `BTC`, etc)"
          }
        },
        "additionalProperties": false
      },
      "PublicGetCurrencyResponseSchema": {
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
            "$ref": "#/components/schemas/PublicGetCurrencyResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PublicGetCurrencyResultSchema": {
        "required": [
          "asset_cap_and_supply_per_manager",
          "borrow_apy",
          "currency",
          "instrument_types",
          "managers",
          "market_type",
          "pm2_collateral_discounts",
          "protocol_asset_addresses",
          "spot_price",
          "srm_im_discount",
          "srm_mm_discount",
          "supply_apy",
          "total_borrow",
          "total_supply"
        ],
        "type": "object",
        "properties": {
          "asset_cap_and_supply_per_manager": {
            "title": "asset_cap_and_supply_per_manager",
            "type": "object",
            "description": "Current open interest and open interest cap by manager and asset type",
            "additionalProperties": {
              "title": "asset_cap_and_supply_per_manager",
              "type": "object",
              "additionalProperties": {
                "title": "asset_cap_and_supply_per_manager",
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/OpenInterestStatsSchema"
                }
              }
            }
          },
          "borrow_apy": {
            "title": "borrow_apy",
            "type": "string",
            "format": "decimal",
            "description": "Borrow APY (only for USDC)"
          },
          "currency": {
            "title": "currency",
            "type": "string",
            "description": "Underlying currency of asset (`ETH`, `BTC`, etc)"
          },
          "erc20_details": {
            "title": "erc20_details",
            "type": "object",
            "default": null,
            "description": "Details of the erc20 asset (if applicable)",
            "additionalProperties": {
              "title": "erc20_details",
              "type": "string",
              "nullable": true
            },
            "nullable": true
          },
          "instrument_types": {
            "title": "instrument_types",
            "type": "array",
            "description": "Instrument types supported for the currency",
            "items": {
              "title": "instrument_types",
              "type": "string",
              "enum": [
                "erc20",
                "option",
                "perp"
              ]
            }
          },
          "managers": {
            "title": "managers",
            "type": "array",
            "description": "Managers supported for the currency",
            "items": {
              "$ref": "#/components/schemas/ManagerContractResponseSchema"
            }
          },
          "market_type": {
            "title": "market_type",
            "type": "string",
            "enum": [
              "ALL",
              "SRM_BASE_ONLY",
              "SRM_OPTION_ONLY",
              "SRM_PERP_ONLY",
              "CASH"
            ],
            "description": "Market type of the currency"
          },
          "pm2_collateral_discounts": {
            "title": "pm2_collateral_discounts",
            "type": "array",
            "description": "Initial and Maintenance Margin discounts for given collateral in PM2",
            "items": {
              "$ref": "#/components/schemas/PM2CollateralDiscountsSchema"
            }
          },
          "protocol_asset_addresses": {
            "$ref": "#/components/schemas/ProtocolAssetAddressesSchema"
          },
          "spot_price": {
            "title": "spot_price",
            "type": "string",
            "format": "decimal",
            "description": "Spot price of the currency"
          },
          "spot_price_24h": {
            "title": "spot_price_24h",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "Spot price of the currency 24 hours ago",
            "nullable": true
          },
          "srm_im_discount": {
            "title": "srm_im_discount",
            "type": "string",
            "format": "decimal",
            "description": "Initial Margin discount for given collateral in Standard Manager (e.g. LTV). Only the Standard Manager supports non-USDC collateral"
          },
          "srm_mm_discount": {
            "title": "srm_mm_discount",
            "type": "string",
            "format": "decimal",
            "description": "Maintenance Margin discount for given collateral in Standard Manager (e.g. liquidation threshold). Only the Standard Manager supports non-USDC collateral"
          },
          "srm_perp_margin_requirements": {
            "$ref": "#/components/schemas/SRMPerpMarginRequirementsPublicSchema",
            "nullable": true
          },
          "supply_apy": {
            "title": "supply_apy",
            "type": "string",
            "format": "decimal",
            "description": "Supply APY (only for USDC)"
          },
          "total_borrow": {
            "title": "total_borrow",
            "type": "string",
            "format": "decimal",
            "description": "Total collateral borrowed in the protocol (only USDC is borrowable)"
          },
          "total_supply": {
            "title": "total_supply",
            "type": "string",
            "format": "decimal",
            "description": "Total collateral supplied in the protocol"
          }
        },
        "additionalProperties": false
      },
      "OpenInterestStatsSchema": {
        "required": [
          "current_open_interest",
          "interest_cap"
        ],
        "type": "object",
        "properties": {
          "current_open_interest": {
            "title": "current_open_interest",
            "type": "string",
            "format": "decimal",
            "description": "Current open interest for the margin type"
          },
          "interest_cap": {
            "title": "interest_cap",
            "type": "string",
            "format": "decimal",
            "description": "Total open interest cap"
          },
          "manager_currency": {
            "title": "manager_currency",
            "type": "string",
            "default": null,
            "description": "Currency of the manager (only applies to Portfolio Margin)",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "ManagerContractResponseSchema": {
        "required": [
          "address",
          "margin_type"
        ],
        "type": "object",
        "properties": {
          "address": {
            "title": "address",
            "type": "string",
            "description": "Address of the manager"
          },
          "currency": {
            "title": "currency",
            "type": "string",
            "default": null,
            "description": "Currency of the manager (only applies to portfolio managers)",
            "nullable": true
          },
          "margin_type": {
            "title": "margin_type",
            "type": "string",
            "enum": [
              "PM",
              "SM",
              "PM2"
            ],
            "description": "Margin type of the manager"
          }
        },
        "additionalProperties": false
      },
      "PM2CollateralDiscountsSchema": {
        "required": [
          "im_discount",
          "manager_currency",
          "mm_discount"
        ],
        "type": "object",
        "properties": {
          "im_discount": {
            "title": "im_discount",
            "type": "string",
            "format": "decimal",
            "description": "Initial Margin discount for given collateral in PM2"
          },
          "manager_currency": {
            "title": "manager_currency",
            "type": "string",
            "description": "Currency of the manager"
          },
          "mm_discount": {
            "title": "mm_discount",
            "type": "string",
            "format": "decimal",
            "description": "Maintenance Margin discount for given collateral in PM2"
          }
        },
        "additionalProperties": false
      },
      "ProtocolAssetAddressesSchema": {
        "type": "object",
        "properties": {
          "option": {
            "title": "option",
            "type": "string",
            "default": null,
            "description": "Address of the Derive protocol option contract (none if not supported)",
            "nullable": true
          },
          "perp": {
            "title": "perp",
            "type": "string",
            "default": null,
            "description": "Address of the Derive protocol perp contract (none if not supported)",
            "nullable": true
          },
          "spot": {
            "title": "spot",
            "type": "string",
            "default": null,
            "description": "Address of the Derive protocol spot contract (none if not supported)",
            "nullable": true
          },
          "underlying_erc20": {
            "title": "underlying_erc20",
            "type": "string",
            "default": null,
            "description": "Address of the erc20 asset on Derive chain. This is the asset that is deposited into the spot asset",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "SRMPerpMarginRequirementsPublicSchema": {
        "required": [
          "im_perp_req",
          "max_leverage",
          "mm_perp_req"
        ],
        "type": "object",
        "properties": {
          "im_perp_req": {
            "title": "im_perp_req",
            "type": "string",
            "format": "decimal",
            "description": "Initial margin requirement for perp positions (fraction of notional)"
          },
          "max_leverage": {
            "title": "max_leverage",
            "type": "string",
            "format": "decimal",
            "description": "Maximum leverage for perp positions (1 / im_perp_req)"
          },
          "mm_perp_req": {
            "title": "mm_perp_req",
            "type": "string",
            "format": "decimal",
            "description": "Maintenance margin requirement for perp positions (fraction of notional)"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```