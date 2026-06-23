> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Live Incidents

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
    "/public/get_live_incidents": {
      "post": {
        "tags": [
          "Public"
        ],
        "summary": "Get Live Incidents",
        "description": "",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PublicGetLiveIncidentsResponseSchema"
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
                "$ref": "#/components/schemas/PublicGetLiveIncidentsParamsSchema"
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "PublicGetLiveIncidentsParamsSchema": {
        "properties": {},
        "type": "object",
        "additionalProperties": false
      },
      "PublicGetLiveIncidentsResponseSchema": {
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
            "$ref": "#/components/schemas/PublicGetLiveIncidentsResultSchema"
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "PublicGetLiveIncidentsResultSchema": {
        "required": [
          "incidents"
        ],
        "properties": {
          "incidents": {
            "title": "incidents",
            "type": "array",
            "description": "List of ongoing incidents",
            "items": {
              "$ref": "#/components/schemas/IncidentResponseSchema"
            }
          }
        },
        "type": "object",
        "additionalProperties": false
      },
      "IncidentResponseSchema": {
        "required": [
          "creation_timestamp_sec",
          "label",
          "message",
          "monitor_type",
          "severity"
        ],
        "properties": {
          "creation_timestamp_sec": {
            "title": "creation_timestamp_sec",
            "type": "integer",
            "description": "Timestamp of incident in UTC sec"
          },
          "label": {
            "title": "label",
            "type": "string",
            "description": "Incident label"
          },
          "message": {
            "title": "message",
            "type": "string",
            "description": "Incident message"
          },
          "monitor_type": {
            "title": "monitor_type",
            "type": "string",
            "enum": [
              "manual",
              "auto"
            ],
            "description": "Incident trigger type"
          },
          "severity": {
            "title": "severity",
            "type": "string",
            "enum": [
              "low",
              "medium",
              "high"
            ],
            "description": "Incident severity"
          }
        },
        "type": "object",
        "additionalProperties": false
      }
    }
  }
}
```