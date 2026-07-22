> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel on Disconnect

> Automatically cancel working orders when a Starbase session drops — enable Cancel on Disconnect, configure it, and combine with heartbeats for safety.

Cancel On Disconnect (CoD) is a risk management feature that automatically cancels tagged open orders when a connection to the Starbase gateway is lost or terminated. CoD helps prevent orders from remaining active after a client disconnection and reduces exposure to unintended positions.

**CoD is opt-in per order — it is not enabled by default and is not a connection/session setting.** An order is covered only if it is explicitly tagged with the `cancelOnDisconnect` flag (`OrderFlags` bit 0). Orders submitted without the flag are not cancelled on disconnect and remain resting. CoD is **session-scoped**, meaning it cancels only the tagged orders associated with the specific disconnected session.

## Session Model

The gateway tracks which session submitted each order to determine which orders should be cancelled when a connection is lost. Each session is completely independent:

* **One session per API Key per gateway host**: A client may have at most one active session per API Key per gateway host
* **Independent sessions**: Two sessions for the same API key on different gateway hosts (Gateway A vs Gateway B) are completely independent with respect to CoD
* **Session-to-order mapping**: This enables accurate cancellation scoped to the disconnected session

## Cancellation Behavior and Detection

When a connection is lost, **CoD triggers instantaneously** and cancels all active CoD-tagged orders and quotes (from [mass quote requests](/starbase/mass-quotes)) submitted through the disconnected session. Orders submitted without the flag are left resting. Any tagged orders that are currently speed-bumped are converted to IOC rather than removed immediately — they will attempt to fill when the speed bump expires and any unfilled remainder is cancelled. See [Speed Bumps — Cancelling Pending Orders](/starbase/speed-bumps#cancelling-pending-orders) for details. Cancelled orders are reported via the [`OrdersCanceled`](/starbase/unsolicited-events#orderscanceled-310) unsolicited event message, which includes:

* The cancelled orders (buy orders, sell orders, and quotes)
* The `cancelReason` field indicating the reason for cancellation (`CLIENT_DISCONNECT` for CoD)
* Order details including `clientOrderId`, `orderId`, `instrumentId`, and `totalFilled`

The gateway detects connection loss through:

* **TCP connection closure**
* **Missing heartbeats**: SBE uses heartbeats to detect connection issues, helping detect stale or dropped connections more quickly. **Heartbeat monitoring cannot be disabled.** The heartbeat interval is returned by the server in the `LogonResponse` (`heartbeatIntervalSeconds` field) and is **5 seconds** by default. This value is set by the server and cannot be configured by the client at logon. If a client maintains the TCP connection but stops sending heartbeats, CoD will trigger after approximately one heartbeat interval (5 seconds).
* **Explicit logout**: A graceful/explicit logout still triggers CoD for tagged orders — it is not a way to preserve them.
* **Session displacement**: A second logon with the same API key on the same gateway host displaces the existing session; the displaced session is dropped and its tagged orders are cancelled.

<Note>
  Authentication occurs only at logon time before any orders can be submitted, so it has no impact on cancellation detection.
</Note>

## Connection Management

### Re-establishment

If a connection is lost and then re-established:

* **Orders are not automatically restored.** Clients must resubmit orders if they wish to maintain their order book.
* **CoD is per order**: reapply the `cancelOnDisconnect` flag on any resubmitted orders you want covered

### Multiple Gateway Connections

When using multiple gateway connections, each session operates independently:

* Orders submitted on Gateway A are only cancelled if the Gateway A session is lost
* Orders submitted on Gateway B are only cancelled if the Gateway B session is lost
* **Losing one session does not affect orders on other sessions**

### Cross-Session Amends and Cancels

Cross-session amending and cross-session cancelling are both supported. CoD binding, however, always stays with the session that originally submitted the order — it does not rebind when the order is amended or cancelled from a different session.

If an order is submitted on session A and later amended or cancelled from session B, disconnecting session A will still trigger CoD for that order (if it is still active), regardless of whether session B remains connected.

See [Gateway Connectivity](/starbase/gateway-connectivity) for more information on managing multiple connections.

## Best Practices

* **Tag Deliberately**: Apply the `cancelOnDisconnect` flag only to orders you want pulled on disconnect; leave it off for orders that should survive a session teardown
* **Monitor Connection Health**: Implement robust connection monitoring and automatic reconnection logic to minimize unintended CoD triggers
* **Handle Cancellations**: Ensure your application properly handles [`OrdersCanceled`](/starbase/unsolicited-events#orderscanceled-310) messages to maintain accurate order state
* **Re-submit Orders**: After reconnecting, evaluate whether previously cancelled orders should be resubmitted based on current market conditions
* **Session Independence**: Each session is independent. Orders submitted on one session will only generate events on that session.
* **Graceful Logout**: A graceful logout still triggers CoD for tagged orders — it does not preserve them. Untag orders you intend to keep across an intentional disconnect.

<Note>
  Once an order is tagged with CoD it cannot be exempted, and it will trigger regardless of how the session ends — abrupt disconnect, missing heartbeats, session displacement, or graceful logout. Orders that are not tagged are never auto-cancelled.
</Note>


## Related topics

- [Connection Management](/articles/connection-management-best-practices.md)
- [private/disable_cancel_on_disconnect](/api-reference/session-management/private-disable_cancel_on_disconnect.md)
- [private/get_cancel_on_disconnect](/api-reference/session-management/private-get_cancel_on_disconnect.md)
- [private/enable_cancel_on_disconnect](/api-reference/session-management/private-enable_cancel_on_disconnect.md)
- [Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
