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
        "type": "object",
        "properties": {},
        "additionalProperties": false
      },
      "PublicGetLiveIncidentsResponseSchema": {
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
            "$ref": "#/components/schemas/PublicGetLiveIncidentsResultSchema"
          }
        },
        "additionalProperties": false
      },
      "PublicGetLiveIncidentsResultSchema": {
        "required": [
          "incidents"
        ],
        "type": "object",
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
        "type": "object",
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
        "additionalProperties": false
      }
    }
  }
}
```