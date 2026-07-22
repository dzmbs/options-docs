> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# REST Order Gateway Authentication

> Authenticate requests to the Starbase REST Order Gateway using HTTP Basic credentials, including API key handling and gateway session security.

Every request to the REST Order Gateway must carry an `Authorization` header. There is no session or token layer — each request re-authenticates independently.

## Authorization Header Format

```
Authorization: Basic base64({clientId}:{clientSecret})
```

The header has two parts:

1. The literal prefix `Basic ` (case-sensitive, with a trailing space).
2. Your `clientId` and `clientSecret` joined by a single colon (`:`), then base64-encoded.

### Example

Given these credentials:

| Field         | Value                                         |
| ------------- | --------------------------------------------- |
| Client ID     | `atUkltkq`                                    |
| Client Secret | `xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow` |

The base64 of `atUkltkq:xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow` is `YXRVa2x0a3E6eG4tdjRKVktZSnhDNXY4VWd4VnZ3b0JiUS1rX0d2a2daRlVYSmdsZTNPdw==`, so the header you send is:

```
Authorization: Basic YXRVa2x0a3E6eG4tdjRKVktZSnhDNXY4VWd4VnZ3b0JiUS1rX0d2a2daRlVYSmdsZTNPdw==
```

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -X GET "https://195.138.37.137:4410/api/v2/private/cancel_all" \
      -H "Authorization: Basic $(echo -n 'atUkltkq:xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow' | base64)"
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={null}
    import base64
    import requests

    client_id = "atUkltkq"
    client_secret = "xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow"

    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Authorization": f"Basic {credentials}"
    }

    response = requests.get(
        "https://195.138.37.137:4410/api/v2/private/cancel_all",
        headers=headers
    )
    print(response.json())
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript theme={null}
    const clientId = "atUkltkq";
    const clientSecret = "xn-v4JVKYJxC5v8UgxVvwoBbQ-k_GvkgZFUXJgle3Ow";

    const credentials = btoa(`${clientId}:${clientSecret}`);
    const response = await fetch("https://195.138.37.137:4410/api/v2/private/cancel_all", {
      headers: {
        "Authorization": `Basic ${credentials}`
      }
    });
    const data = await response.json();
    console.log(data);
    ```
  </Tab>
</Tabs>

## Error Responses

Any authentication failure returns HTTP `401`. The table below maps each failure cause to its error message:

| Cause                                        | Error message                                                |
| -------------------------------------------- | ------------------------------------------------------------ |
| Header missing or not starting with `Basic ` | `Missing or invalid Authorization header`                    |
| Decoded credential string contains no colon  | `Invalid credentials format. Expected clientId:clientSecret` |
| Deribit rejects the credentials              | `Authentication failed`                                      |

Treat every `401` as terminal for that request. Retry only after fixing the header or credentials — do not retry an invalid request blindly.

## Practical Checklist

<Steps>
  <Step title="Use HTTPS">
    HTTPS is required to protect credentials in transit.
  </Step>

  <Step title="Send the header on every request">
    There is no session or token reuse. Every request must include the `Authorization` header.
  </Step>

  <Step title="Base64-encode the credentials">
    Concatenate `clientId:clientSecret` with a colon separator, then base64-encode the result. Send that encoded string after `Basic `.
  </Step>

  <Step title="Obtain a REST Order Entry API key">
    Your API key must have the **REST Order Entry** scope. See [Creating a Starbase API Key](/starbase/creating-api-key) for steps.
  </Step>
</Steps>

## Next Steps

<CardGroup cols={2}>
  <Card title="Creating a Starbase API Key" icon="key" href="/starbase/creating-api-key">
    Generate credentials with the REST Order Entry scope
  </Card>

  <Card title="Placing a New Order" icon="arrow-up-right" href="/starbase/placing-new-order">
    Submit your first order via the REST Order Gateway
  </Card>

  <Card title="Rate Limits" icon="gauge" href="/starbase/api-rate-limits">
    Per-gateway rate limit rules for REST requests
  </Card>

  <Card title="Gateway Connectivity" icon="server" href="/starbase/gateway-connectivity">
    Gateway addresses, ports, and connection rules
  </Card>
</CardGroup>


## Related topics

- [Gateway Connectivity](/starbase/gateway-connectivity.md)
- [Authentication](/articles/authentication.md)
- [Order Management](/articles/order-management-best-practices.md)
- [Cancel on Disconnect](/starbase/cancel-on-disconnect.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
