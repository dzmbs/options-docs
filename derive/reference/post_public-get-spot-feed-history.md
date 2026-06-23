> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Spot Feed History

Get spot feed history by currency<br /><br />DEPRECATION NOTICE: This RPC is deprecated in favor of get_index_chart_data and get_tradingview_chart_data

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
    "/public/get_spot_feed_history": {
      "post": {
        "tags": [
          "Public"
        ],
        "summary": "Get Spot Feed History",
        "description": "Get spot feed history by currency<br /><br />DEPRECATION NOTICE: This RPC is deprecated in favor of get_index_chart_data and get_tradingview_chart_data",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicGetSpotFeedHistoryResponseSchema"
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
                "$ref": "#/components/schemas/PublicGetSpotFeedHistoryParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PublicGetSpotFeedHistoryParamsSchema": {
        "required": [
          "currency",
          "end_timestamp",
          "period",
          "start_timestamp"
        ],
        "properties": {
          "currency": {
            "title": "currency",
            "type": "string",
            "description": "Currency"
          },
          "end_timestamp": {
            "title": "end_timestamp",
            "type": "integer",
            "description": "End timestamp"
          },
          "period": {
            "title": "period",
            "type": "integer",
            "description": "Period"
          },
          "start_timestamp": {
            "title": "start_timestamp",
            "type": "integer",
            "description": "Start timestamp"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PublicGetSpotFeedHistoryResponseSchema": {
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
            "$ref": "#/components/schemas/PublicGetSpotFeedHistoryResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PublicGetSpotFeedHistoryResultSchema": {
        "required": [
          "currency",
          "spot_feed_history"
        ],
        "properties": {
          "currency": {
            "title": "currency",
            "type": "string",
            "description": "Currency"
          },
          "spot_feed_history": {
            "title": "spot_feed_history",
            "type": "array",
            "description": "Spot feed history",
            "items": {
              "$ref": "#/components/schemas/SpotFeedHistoryResponseSchema"
            }
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "SpotFeedHistoryResponseSchema": {
        "required": [
          "price",
          "timestamp",
          "timestamp_bucket"
        ],
        "properties": {
          "price": {
            "title": "price",
            "type": "string",
            "format": "decimal",
            "description": "Spot price"
          },
          "timestamp": {
            "title": "timestamp",
            "type": "integer",
            "description": "Timestamp of when the spot price was recored into the database"
          },
          "timestamp_bucket": {
            "title": "timestamp_bucket",
            "type": "integer",
            "description": "Timestamp bucket; this value is regularly spaced out with `period` seconds between data points, missing values are forward-filled from earlier data where possible, if no earlier data is available, values are back-filled from the first observed data point"
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```