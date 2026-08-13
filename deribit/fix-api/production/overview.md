> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deribit Production FIX API Overview

> Overview of the Deribit production FIX 4.4 subset covering endpoints, supported message types, and how the live FIX gateway differs from the upcoming one.

Deribit FIX API is a subset of FIX version 4.4. It also includes some tags from FIX 5.0 and several Deribit custom tags. Deribit uses the standard FIX header and trailer structure for all messages.

## Before you start

Complete these steps before opening a FIX session:

1. Sign in to your account and go to **Account > Security > API**. Enable API access with the checkbox on that page.
2. Create an API key on the same page. The `Client ID` becomes your FIX `Username`(`553`) and the `Client Secret` is used to derive the `Password`(`554`) sent in [`Logon`(`A`)](/fix-api/production/logon).
3. Choose an environment and endpoint from [Connection endpoints](#connection-endpoints) below. Use `fix-test.deribit.com` for integration testing before switching to `fix.deribit.com`.
4. Authenticate by sending a [`Logon`(`A`)](/fix-api/production/logon) message. See that page for how to build `RawData`(`96`) and `Password`(`554`).

<Warning>
  Do not share your `Client Secret`. Anyone with the secret can derive a valid `Password`(`554`) and gain full control over your account.
</Warning>

<Warning>
  **IMPORTANT ANNOUNCEMENT**

  Due to recent technical issues with one of our service providers, we have updated the FIX public endpoint. The FIX endpoint will no longer be accessible over the internet via [www.deribit.com](http://www.deribit.com). Going forward, customers should connect using fix.deribit.com for production and fix-test.deribit.com for test environment.
</Warning>

## Connection Endpoints

The FIX server can be reached at:

* **Production:**
  * `fix.deribit.com:9881` (raw tcp)
  * `fix.deribit.com:9883` (ssl)
* **Test Network:**
  * `fix-test.deribit.com:9881` (raw tcp)
  * `fix-test.deribit.com:9883` (ssl)

## Message Structure

### Request Message Headers

Each request message can include:

| Tag | Name           | Type         | Required | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --- | -------------- | ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 8   | `BeginString`  | String       | Yes      | Identifies beginning of new message and protocol version. Must always be first in the message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 9   | `BodyLength`   | Length       | Yes      | Message length in bytes, not including fields `BeginString`(`8`), `BodyLength`(`9`) and `CheckSum`(`10`). The length must be calculated by counting the number of octets in the message up to and including the end of field delimiter (Start of Heading) of the field immediately preceding the `CheckSum`(`10`) field. Must always be the second in the message. Please refer to [FIX specification](https://www.fixtrading.org/standards/tagvalue-online/#fix-tagvalue-message-syntax) for more details                                                                                                                                                                                                                                                                                                                           |
| 35  | `MsgType`      | String       | Yes      | The type of the message. See below for available types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 49  | `SenderCompID` | String       | Yes      | A user defined client name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 56  | `TargetCompID` | String       | Yes      | Constant value: `DERIBITSERVER`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 34  | `MsgSeqNum`    | SeqNum       | Yes      | A sequence number for the message, starts with 1, and must be incremented by 1 for every message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 52  | `SendingTime`  | UTCTimestamp | No       | The time the request is sent. This field is ignored by the server                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 10  | `CheckSum`     | String       | Yes      | The checksum of all preceding messages. In order to calculate checksum, sum up the binary value of each octet up to and including the end of field delimiter (Start of Heading) of the field immediately preceding the `CheckSum`(`10`). Afterwards calculate modulo 256 of that sum. The calculated modulo 256 checksum must then be encoded as an ISO 8859-1 three-octet representation of the decimal value. For example, if the message length sum of character values has been calculated to be 274 then the modulo 256 value is 18 (256 + 18 = 274). This value would be encoded in the CheckSum(10) field as "10=018". CheckSum must always be the last field in the message. Please refer to [FIX specification](https://www.fixtrading.org/standards/tagvalue-online/#fix-tagvalue-message-syntax) Annex A for more details |

### Response Message Headers

Responses sent by the server will at least include:

| Tag | Name           | Type         | Comments                                                                                                                                                                                                                                                                                                                                |
| --- | -------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 8   | `BeginString`  | String       | Identifies beginning of new message and protocol version. Must always be first in the message                                                                                                                                                                                                                                           |
| 9   | `BodyLength`   | Length       | Message length in bytes, not including fields `BeginString`(`8`), `BodyLength`(`9`) and `CheckSum`(`10`). Please refer to [FIX specification](https://www.fixtrading.org/standards/tagvalue-online/#fix-tagvalue-message-syntax) for more details                                                                                       |
| 35  | `MsgType`      | String       | The type of the message. See below for available types                                                                                                                                                                                                                                                                                  |
| 49  | `SenderCompID` | String       | Constant value: `DERIBITSERVER`                                                                                                                                                                                                                                                                                                         |
| 56  | `TargetCompID` | String       | A user defined client name                                                                                                                                                                                                                                                                                                              |
| 34  | `MsgSeqNum`    | SeqNum       | A server-chosen sequence number for the message                                                                                                                                                                                                                                                                                         |
| 52  | `SendingTime`  | UTCTimestamp | The time Deribit transmitted this response. For [Execution Reports](/fix-api/production/execution-reports), compare against `TransactTime` (60), which is when the transaction represented by the report occurred on the exchange. The difference is the interval between the exchange event and the report being sent to your session. |
| 10  | `CheckSum`     | String       | The checksum of all preceding messages. Please refer to [FIX specification](https://www.fixtrading.org/standards/tagvalue-online/#fix-tagvalue-message-syntax) Annex A for more details                                                                                                                                                 |

## Message Types

The FIX API supports the following message types organized by category:

### Session Management

* [Logon (A)](/fix-api/production/logon) - Initiate a session
* [Logout (5)](/fix-api/production/logout) - Terminate a session
* [Heartbeat (0)](/fix-api/production/heartbeat) - Keep connection alive
* [Test Request (1)](/fix-api/production/test-request) - Force a heartbeat
* [Resend Request (2)](/fix-api/production/resend-request) - Request message retransmission
* [Reject (3)](/fix-api/production/reject) - Reject invalid messages
* [Sequence Reset (4)](/fix-api/production/sequence-reset) - Recover from sequence loss

### Market Data

* [Security List Request (x)](/fix-api/production/security-list-request) - Request list of instruments
* [Security List (y)](/fix-api/production/security-list) - Response with instrument list
* [Market Data Request (V)](/fix-api/production/market-data-request) - Request market data
* [Market Data Request Reject (Y)](/fix-api/production/market-data-request-reject) - Reject market data request
* [Market Data Snapshot/Full Refresh (W)](/fix-api/production/market-data-snapshot) - Market data snapshot
* [Market Data Incremental Refresh (X)](/fix-api/production/market-data-incremental) - Incremental market data updates
* [Security Status Request (e)](/fix-api/production/security-status-request) - Request security status
* [Security Status (f)](/fix-api/production/security-status) - Security status response

### Order Management

* [New Order Single (D)](/fix-api/production/new-order-single) - Submit new order
* [Order Cancel Request (F)](/fix-api/production/order-cancel-request) - Cancel an order
* [Order Cancel Reject (9)](/fix-api/production/order-cancel-reject) - Reject cancel request
* [Order Cancel/Replace Request (G)](/fix-api/production/order-cancel-replace) - Modify an order
* [Order Mass Cancel Request (q)](/fix-api/production/order-mass-cancel-request) - Cancel multiple orders
* [Order Mass Cancel Report (r)](/fix-api/production/order-mass-cancel-report) - Mass cancel response
* [Order Mass Status Request (AF)](/fix-api/production/order-mass-status-request) - Request order status
* [Execution Reports (8)](/fix-api/production/execution-reports) - Order execution notifications

### Position Management

* [Request For Positions (AN)](/fix-api/production/request-for-positions) - Request position report
* [Position Report (AP)](/fix-api/production/position-report) - Position report response

### User Management

* [User Request (BE)](/fix-api/production/user-request) - Request user account info
* [User Response (BF)](/fix-api/production/user-response) - User account info response

### Market Maker Protection

* [MMProtection Limits (MM)](/fix-api/production/mmprotection-limits) - Set/get MMP limits
* [MMProtection Limits Result/Reject (MR)](/fix-api/production/mmprotection-limits-result) - MMP limits response
* [MMProtection Reset (MZ)](/fix-api/production/mmprotection-reset) - Reset MMP after trigger

### Mass Quoting

* [Mass Quote (i)](/fix-api/production/mass-quote) - Place multiple quotes
* [Mass Quote Acknowledgement (b)](/fix-api/production/mass-quote-acknowledgement) - Mass quote response
* [Quote Cancel (Z)](/fix-api/production/quote-cancel) - Cancel quotes

### Trade Capture

* [TradeCaptureReportRequest (AD)](/fix-api/production/trade-capture-report-request) - Request trade reports
* [TradeCaptureReportRequestAck (AQ)](/fix-api/production/trade-capture-report-request-ack) - Trade request acknowledgment
* [TradeCaptureReport (AE)](/fix-api/production/trade-capture-report) - Trade capture report

### Security Definition

* [Security Definition Request (c)](/fix-api/production/security-definition-request) - Request combo security
* [Security Definition (d)](/fix-api/production/security-definition) - Security definition response

### Changes Log

* [Changes Log](/fix-api/production/changes-log) - Release history and changes


## Related topics

- [Logon(A) — Production FIX API](/fix-api/production/logon.md)
- [Logout(5) — Production FIX API](/fix-api/production/logout.md)
- [Reject(3) — Production FIX API](/fix-api/production/reject.md)
- [Heartbeat(0) — Production FIX API](/fix-api/production/heartbeat.md)
- [Sequence Reset(4) — Production FIX API](/fix-api/production/sequence-reset.md)
