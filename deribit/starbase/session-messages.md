> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starbase Session Messages

> Session-level messages in the Starbase Binary API covering logon with schemaVersion negotiation, heartbeat, logout, and gateway connection lifecycle rejects.

## Session Messages

Session messages manage the lifecycle of a TCP connection to a Starbase gateway, including authentication, heartbeating, and sequence number recovery.

### LogonRequest (1)

First message sent by client after establishing TCP connection.

| Field | Name               | Type   | Length | Description                                                                                                                                                                                                                                                             |
| ----- | ------------------ | ------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | username           | char   | 16     | Client username                                                                                                                                                                                                                                                         |
| 2     | password           | char   | 48     | Client password                                                                                                                                                                                                                                                         |
| 3     | resetSeqNum        | int8   | 1      | `0`=no (do not reset sequence numbers)<br />`1`=yes (reset sequence numbers)                                                                                                                                                                                            |
| 4     | schemaVersion      | uint16 | 2      | Client-negotiated SBE schema (protocol) version. Optional; added in schema version `12`. See the version negotiation note below.                                                                                                                                        |
| 5     | cancelOnDisconnect | int8   | 1      | Session-wide cancel-on-disconnect opt-in: `0`=no — each order and quote carries its own per-message flag<br />`1`=yes — every order and quote submitted on this session is covered. Optional. See [Session-level CoD](/starbase/cancel-on-disconnect#session-level-cod) |

### LogonResponse (2)

Response to `LogonRequest` on successful logon.

| Field | Name                     | Type   | Length | Description                                                                                                                                                                                |
| ----- | ------------------------ | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1     | heartbeatIntervalSeconds | int32  | 4      | Interval in seconds at which the server expects heartbeat messages from the client                                                                                                         |
| 2     | schemaVersion            | uint16 | 2      | Echoes the schema (protocol) version accepted by the gateway — the authoritative negotiated version for the session. Added in schema version `12`. See the version negotiation note below. |

<Note>
  **Schema version negotiation** (schema version `12` and later): `schemaVersion` on `LogonRequest` acts as a gate — it determines whether new messages and new versions of existing messages are sent to the client. A value outside the gateway's accepted range is rejected at logon. The gateway echoes the accepted version in `LogonResponse`.

  There are two version numbers on the wire, and they are not equal:

  * **Session ceiling** — the `schemaVersion` sent at logon: the highest schema version the client can accept. One number per session, echoed back in `LogonResponse.schemaVersion`. This is the authoritative negotiated version for the session.
  * **Per-message stamp** — the `version` field in the header of each message the gateway sends: the newest schema version at which that particular message last changed, never above the session ceiling. If a message did not change between schema versions, its stamp is not bumped.

  For example, after negotiating version `15`, `LogonResponse` arrives with header `version = 12` because `LogonResponse` has not changed since version `12`. This is expected — always read the negotiated version from the `schemaVersion` field, never from per-message header stamps.
</Note>

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
| `6`   | `GATEWAY_NOT_ACTIVE`   | The target gateway is not active                               |


## Related topics

- [Starbase Mass Cancel Messages](/starbase/mass-cancel.md)
- [Starbase API Changelog](/changelogs/starbase.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [Cancelling an Order](/starbase/cancelling-order.md)
- [Starbase FIX Drop Copy API](/starbase/fix-drop-copy-api.md)
