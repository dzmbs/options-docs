> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Vault Share

Gets the value of a vault's token against the base currency, underlying currency, and USD for a timestamp range.<br /><br />The name of the vault from the Vault proxy contract is used to fetch the vault's value.

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
    "/public/get_vault_share": {
      "post": {
        "tags": [
          "Public"
        ],
        "summary": "Get Vault Share",
        "description": "Gets the value of a vault's token against the base currency, underlying currency, and USD for a timestamp range.<br /><br />The name of the vault from the Vault proxy contract is used to fetch the vault's value.",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicGetVaultShareResponseSchema"
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
                "$ref": "#/components/schemas/PublicGetVaultShareParamsSchema"
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
        "type": "object",
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
        "additionalProperties": false
      },
      "PublicGetVaultShareParamsSchema": {
        "required": [
          "from_timestamp_sec",
          "to_timestamp_sec",
          "vault_name"
        ],
        "type": "object",
        "properties": {
          "from_timestamp_sec": {
            "title": "from_timestamp_sec",
            "type": "integer",
            "description": "From timestamp in seconds"
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
          "to_timestamp_sec": {
            "title": "to_timestamp_sec",
            "type": "integer",
            "description": "To timestamp in seconds"
          },
          "vault_name": {
            "title": "vault_name",
            "type": "string",
            "description": "Name of the vault"
          }
        },
        "additionalProperties": false
      },
      "PublicGetVaultShareResponseSchema": {
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
            "$ref": "#/components/schemas/PublicGetVaultShareResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PublicGetVaultShareResultSchema": {
        "required": [
          "pagination",
          "vault_shares"
        ],
        "type": "object",
        "properties": {
          "pagination": {
            "$ref": "#/components/schemas/PaginationInfoSchema"
          },
          "vault_shares": {
            "title": "vault_shares",
            "type": "array",
            "description": "List of vault history shares, recent first",
            "items": {
              "$ref": "#/components/schemas/VaultShareResponseSchema"
            }
          }
        },
        "additionalProperties": false
      },
      "VaultShareResponseSchema": {
        "required": [
          "base_value",
          "block_number",
          "block_timestamp",
          "underlying_value",
          "usd_value"
        ],
        "type": "object",
        "properties": {
          "base_value": {
            "title": "base_value",
            "type": "string",
            "format": "decimal",
            "description": "The value of the vault's token against the base currency. Ex: rswETHC vs rswETH"
          },
          "block_number": {
            "title": "block_number",
            "type": "integer",
            "description": "The Derive chain block number"
          },
          "block_timestamp": {
            "title": "block_timestamp",
            "type": "integer",
            "description": "Timestamp of the Derive chain block number"
          },
          "underlying_value": {
            "title": "underlying_value",
            "type": "string",
            "format": "decimal",
            "default": null,
            "description": "The value of the vault's token against the underlying currency. Ex: rswETHC vs ETH",
            "nullable": true
          },
          "usd_value": {
            "title": "usd_value",
            "type": "string",
            "format": "decimal",
            "description": "The value of the vault's token against USD"
          }
        },
        "additionalProperties": false
      }
    }
  }
}
```