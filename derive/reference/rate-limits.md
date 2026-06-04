> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits

The below rate limits have been implemented to safeguard our system. Rate limiters use a "fixed window" algorithm to discretely refill the request allowance every 5 seconds.

Market makers are eligible for higher rate limits. To apply for increased rates, please contact our support team.

| Type         | matching | per-instrument matching | non-matching | connections      | Burst Multiplier |
| ------------ | -------- | :---------------------- | ------------ | ---------------- | :--------------- |
| Trader       | 1 TPS    | 1 TPS                   | 5 TPS        | 4x per IP        | 5x               |
| Market Maker | 500+ TPS | 10+ TPS                 | 500+ TPS     | up to 64x per IP | 5x               |

> Burst requests for both REST and WebSockets are refreshed every 5 seconds. E.g a trader can send 5x matching requests in a single burst but must wait 5 seconds before any further requests can be sent.

<br />

## Matching, Non-Matching, and Custom Requests

The below requests are counted as `matching` and `per-instrument matching` requests:

* `private/order`
* `private/replace` (counted as 1 request)
* `private/cancel`
* `private/cancel_by_nonce`
* `private/cancel_by_instrument`
* `private/cancel_by_label`(if  `instrument_name` param is set)

`custom` rate-limited requests:

* `private/cancel_all`- 1 TPS
* `private/cancel_by_label` - 10 TPS (if  `instrument_name` param is NOT set)

All requests outside of the above are counted as `non-matching`.

<br />

## REST

All `non-matching` requests over the REST API are rate limited per IP at a flat 10 TPS with 5x burst. If the limit is crossed,`429 Too Many Requests` response is returned.

<br />

## WebSocket

To access the above rate limits, all clients **must authorize themselves via the`public/login` route**. Otherwise, a reduced rate limit will be applied. Requests exceeding the rate limit will receive the below response:

```json
{
  id: number
  error: {
    code: -32000,
    message: "Rate limit exceeded",
    data: "Retry after ${cooldown} ms"
  }
}
```

Only via WebSockets, the live remaining rate limits can be checked using the `private/getRateLimits` route.

```javascript
// send getRateLimit request
ws.send(JSON.stringify({
  'public/getRateLimits`,
  {},
  id: 1,
});

// example response
{
  "id": 4,
  "result": {
      "remaining_matching": {
        "remainingPoints": 22,
        "msBeforeNext": 4809,
        "consumedPoints": 3
      },
      "remaining_non_matching": {
        "remainingPoints": 98,
        "msBeforeNext": 4809,
        "consumedPoints": 2
      },
      "remaining_connections": {
        "remainingPoints": 29,
        "msBeforeNext": 8881,
        "consumedPoints": 3
      },
      "remaining_per_instrument": {
      	"ETH-PERP": {
          "remainingPoints": 29,
          "msBeforeNext": 381,
          "consumedPoints": 3
        },
        "ETH-08242024-3200-C": {
          "remainingPoints": 29,
          "msBeforeNext": 381,
          "consumedPoints": 10
        }
      }
}  
```