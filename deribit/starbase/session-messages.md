> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Session Messages

> Session-level messages in the Starbase Binary API — login, heartbeat, logout, and error messages that manage the gateway connection lifecycle.

## Session Messages

Session messages manage the lifecycle of a TCP connection to a Starbase gateway, including authentication, heartbeating, and sequence number recovery.

### LogonRequest (1)

First message sent by client after establishing TCP connection.

| Field | Name        | Type | Length | Description                                                                  |
| ----- | ----------- | ---- | ------ | ---------------------------------------------------------------------------- |
| 1     | username    | char | 16     | Client username                                                              |
| 2     | password    | char | 48     | Client password                                                              |
| 3     | resetSeqNum | int8 | 1      | `0`=no (do not reset sequence numbers)<br />`1`=yes (reset sequence numbers) |

### LogonResponse (2)

Response to `LogonRequest` on successful logon.

| Field | Name                     | Type  | Length | Description                                                                        |
| ----- | ------------------------ | ----- | ------ | ---------------------------------------------------------------------------------- |
| 1     | heartbeatIntervalSeconds | int32 | 4      | Interval in seconds at which the server expects heartbeat messages from the client |

### LogoutRequest (4)

Request by client to gracefully terminate a connection.

| Field | Name         | Type  | Length | Description            |
| ----- | ------------ | ----- | ------ | ---------------------- |
| 1     | reasonLength | uint8 | 1      | Length of reason field |
| 2     | reason       | char  | 0-255  | ASCII-encoded string   |

### LoggedOut (5)

Sent in response to `LogonRequest` if logon failed, or in response to `LogoutRequest`, or unsolicited for other reasons.

| Field | Name         | Type  | Length | Description            |
| ----- | ------------ | ----- | ------ | ---------------------- |
| 1     | reasonLength | uint8 | 1      | Length of reason field |
| 2     | reason       | char  | 0-255  | ASCII-encoded string   |

### Heartbeat (10)

Sent by client or server periodically in the absence of other messages.

| Field | Name          | Type  | Length | Description                                                         |
| ----- | ------------- | ----- | ------ | ------------------------------------------------------------------- |
| 1     | correlationId | int64 | 8      | Set if this Heartbeat is in response to a `TestRequest`; `0` if not |

### TestRequest (11)

Request a `Heartbeat` message. Can be sent by either client or server.

| Field | Name          | Type  | Length | Description                                                                             |
| ----- | ------------- | ----- | ------ | --------------------------------------------------------------------------------------- |
| 1     | correlationId | int64 | 8      | Value the recipient should echo back in the `correlationId` of the `Heartbeat` response |

### ResendRequest (20)

Sent by client to request resend of a limited number of missed events. Works only when reconnecting to the same gateway host. The server will never send this message to a client.

| Field | Name       | Type  | Length | Description                                                                                                            |
| ----- | ---------- | ----- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| 1     | fromSeqNum | int64 | 8      | Sequence number of first message to be resent                                                                          |
| 2     | toSeqNum   | int64 | 8      | Sequence number of the last message to be resent, or `0` if all available messages after `fromSeqNum` should be resent |

### GapFill (21)

Sent by server in lieu of admin/session messages while handling a resend request.

| Field | Name      | Type  | Length | Description                                          |
| ----- | --------- | ----- | ------ | ---------------------------------------------------- |
| 1     | newSeqNum | int64 | 8      | Sequence number of next message to be sent by server |

### Reject (30)

Sent by the server in response to an unrecognized or malformed message from the client.

| Field | Name          | Type  | Length | Description                                 |
| ----- | ------------- | ----- | ------ | ------------------------------------------- |
| 1     | refSeqNum     | int64 | 8      | Sequence number of the rejected message     |
| 2     | reason        | int8  | 1      | Rejection reason code. See the table below. |
| 3     | detailsLength | uint8 | 1      | Length of details field                     |
| 4     | details       | char  | 0-255  | ASCII-encoded string                        |

The table below lists all possible values of the `reason` field.

| Value | Name                   | Description                                                    |
| ----- | ---------------------- | -------------------------------------------------------------- |
| `1`   | `INVALID_SCHEMA_ID`    | Message schema ID does not match this gateway                  |
| `2`   | `INVALID_TEMPLATE_ID`  | Unrecognized message template ID                               |
| `3`   | `INVALID_BLOCK_LENGTH` | Message block length does not match the template               |
| `4`   | `INVALID_FIELD_VALUE`  | A field in the message contains an invalid value               |
| `5`   | `MESSAGE_DISABLED`     | The message being submitted has been administratively disabled |


## Related topics

- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [Starbase API Changelog](/changelogs/starbase.md)
- [Logon(A) — Production FIX API](/fix-api/production/logon.md)
- [Cancelling an Order](/starbase/cancelling-order.md)
- [Connection Management](/articles/connection-management-best-practices.md)
