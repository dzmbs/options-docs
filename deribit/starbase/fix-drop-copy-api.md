> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starbase FIX Drop Copy API

> Starbase FIX Drop Copy delivers a per-Member feed of orders, trades, and executions, with reconciliation guidance for ID mapping, dedup, and gap replay.

## Downloads

<CardGroup cols={1}>
  <Card title="FIX Specification XML" icon="file-code">
    FIX 5.0 SP2 specification file for the Drop Copy API.

    * [Production](/specifications/FIX50.xml)
    * [Testnet](/specifications/FIX50.xml)
  </Card>
</CardGroup>

The FIX Drop Copy API provides a complete record of orders and trades. It uses two distinct message types depending on the trade type:

<Note>
  The FIX Drop Copy gateway is designed for **direct access users**: clients placing orders through one of the Starbase order entry gateways. Non-direct users (e.g. orders placed via the Web UI or WebSocket API) are not supported.
</Note>

<Note>
  **Drop Copy is configured per Member.** By default a single Drop Copy session receives the full Member feed — order and trade activity for **all** portfolios (subaccounts) assigned to that Member, across all gateways and API keys. Every message identifies the portfolio it belongs to in **Tag 1 `Account`** (the `portfolioId`) — the subaccount the order or trade is booked to — so you can demultiplex a full-Member feed per subaccount.

  If you want the gateway to restrict a session to a **single portfolio** instead of filtering client-side, set **`PortfolioScopeOnly` (Tag 25002 = `Y`)** on logon. The session is then scoped to the portfolio the API key's credentials belong to, and events for the Member's other subaccounts are filtered out server-side. See [Scoping a Session to One Portfolio](#scoping-a-session-to-one-portfolio-25002).
</Note>

## Connection and Authentication

### FIX Version

The gateway uses **FIX 5.0 SP2 (FIXT.1.1)**. The `BeginString` field in the logon message must be set to `FIXT.1.1`. Connections using an older version (e.g. `FIX.4.4`) are rejected before parsing can identify the sender, so no reject message is returned.

```text theme={null}
Example FIX logon message
8=FIXT.1.1|9=280|35=A|49=<client_id>|56=CBDRBDC|34=1|52=<timestamp_in_ms>|98=0|108=30|141=Y|1137=9|553=<client_id>|554=<secret>|96=<raw_data>|95=78|58=<signature>|10=135|
```

### Logon Fields

| Tag   | Name               | Value                                                                                                                                                                                                                                                                                                    |
| ----- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 49    | SenderCompID       | Client-defined. Must remain consistent for the duration of the session.                                                                                                                                                                                                                                  |
| 56    | TargetCompID       | `CBDRBDC`                                                                                                                                                                                                                                                                                                |
| 553   | Username           | Client ID (API key)                                                                                                                                                                                                                                                                                      |
| 554   | Password           | Client Secret (API Secret)                                                                                                                                                                                                                                                                               |
| 96    | RawData            | `raw_data` as generated below                                                                                                                                                                                                                                                                            |
| 58    | Text               | `signature` as generated below                                                                                                                                                                                                                                                                           |
| 25001 | Messages           | `TRADES_ONLY`<br />`ORDERS_AND_TRADES`<br />`ALL_EVENTS` - Enabled by default                                                                                                                                                                                                                            |
| 25002 | PortfolioScopeOnly | BOOLEAN. `Y` = scope this session to the single portfolio (subaccount) the credentials belong to; events for the Member's other subaccounts are **not** delivered. `N` or omitted = full per-Member feed (default). See [Scoping a Session to One Portfolio](#scoping-a-session-to-one-portfolio-25002). |

```python theme={null}
import base64
import hashlib
import secrets

def build_signature(secret: str) -> tuple[str, str]:
    """Returns (raw_data, signature_b64)"""
    timestamp_ms = int(time.time() * 1000)
    nonce        = secrets.token_hex(32)
    raw_data     = f"{timestamp_ms}.{nonce}"
    digest       = hashlib.sha256((raw_data + secret).encode("utf-8")).digest()
    signature    = base64.b64encode(digest).decode("ascii")
    return raw_data, signature
```

### Scoping a Session to One Portfolio (25002)

<a id="scoping-a-session-to-one-portfolio-25002" />

By default a Drop Copy session delivers the **full Member feed** — every portfolio (subaccount) assigned to the Member. There are two ways to work with a specific portfolio:

* **Client-side demux (default):** take the full feed and split it yourself on **Tag 1 `Account`** (the `portfolioId`) present on every Execution Report and Trade Capture Report.
* **Server-side scoping:** set **`PortfolioScopeOnly` (Tag 25002) = `Y`** on the logon message. The session is scoped to the single portfolio the logon credentials belong to, and the gateway suppresses events for the Member's other subaccounts.

`PortfolioScopeOnly` is a FIX `BOOLEAN` — the value is `Y` or `N`. Omitting the tag is equivalent to `N` (full feed).

```text theme={null}
Example logon scoped to the credentials' portfolio (note 25002=Y)
8=FIXT.1.1|9=288|35=A|49=<client_id>|56=CBDRBDC|34=1|52=<timestamp_in_ms>|98=0|108=30|141=Y|1137=9|553=<client_id>|554=<secret>|96=<raw_data>|95=78|58=<signature>|25002=Y|10=135|
```

<Note>
  With `25002=Y`, the [open order snapshot on connect](#open-order-snapshot-on-connect) and all subsequent Execution Reports / Trade Capture Reports are limited to the credentials' own portfolio. To receive events for every subaccount under the Member on one session, omit the tag (or send `25002=N`) and demultiplex on Tag 1 `Account`. To run each portfolio on its own session, log on with that portfolio's API key and `25002=Y`.
</Note>

* **Execution Reports** (`35=8`) cover orders and trades that occur **in the order book.**
* **Trade Capture Reports** (`35=AE`) cover trades that occur **outside the order book.**

<Note>
  Mass quotes (submitted via the SBE Mass Quote API) appear in the Drop Copy feed **only when they result in fills**. Unexecuted quotes are not included.
</Note>

<Warning>
  **Old rejected and zero-fill orders cannot be recovered after the fact.** REST/WebSocket order history endpoints (e.g. `private/get_order_history_by_instrument`) only return orders that reached the book or filled — an IOC/FAK order that expired with zero fills, or any order that was hard-rejected synchronously (invalid params, insufficient margin, etc.), will not appear there, and there is no separate endpoint to retrieve them retroactively. To maintain a complete audit trail of every order outcome including rejects, persist Execution Reports from this Drop Copy feed as they arrive rather than relying on pulling history later. Note that synchronous hard rejects fail before an order is accepted, so they will not appear on Drop Copy either — track your own request/response pairs for those.
</Warning>

<Note>
  Trades placed through Starbase are visible on both the standard WebSocket/FIX trade feeds and on Starbase FIX Drop Copy. **Open Starbase orders are different**: they are only visible via Starbase FIX Drop Copy (or an SBE order-entry session) — the standard Deribit WebSocket and FIX feeds do not surface open order state for orders placed through Starbase. See [Consolidated View: FIX Drop Copy](/starbase/connectivity-best-practices#consolidated-view-fix-drop-copy) for the reasoning.
</Note>

## Open Order Snapshot on Connect

When a new Drop Copy session is established, Starbase immediately sends Execution Reports for all currently open orders. These snapshot messages are sent automatically (no request is needed) and are marked with a snapshot indicator to distinguish them from live messages. This allows clients to synchronize their order state on connect without requesting an ER replay.

## Report Types

### Order book trades: Execution Reports

Execution Reports are sent for all activity that goes through the order book:

| Source               | Description                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| Starbase Order Entry | Orders placed via the Starbase Direct Access APIs.                       |
| Other Order Entry    | Orders placed via other methods: Websocket API, Web UI, mobile app, etc. |
| Liquidations         | Liquidation and rebalancing orders generated by Deribit's risk system.   |

### Reported trades: Trade Capture Reports

Trade Capture Reports are sent for trades that bypass the order book entirely:

| Source         | Description                                                                    |
| -------------- | ------------------------------------------------------------------------------ |
| Block Trades   | Privately negotiated trades reported to the exchange. Includes Block RFQ.      |
| Position Moves | Transfer of an open position between two accounts under the same main account. |

## Drop Copy Message Types

<AccordionGroup>
  <Accordion title="Orders">
    * [ExecutionReport \<8> | 150=0/4/5](#order-execution-reports): Sent when an order is new, amended, or cancelled. Intermediate speed-bump states are suppressed.
  </Accordion>

  <Accordion title="Trades">
    * [ExecutionReport \<8> | 150=F](#trade-150f): Sent on any trade generated by an order.
    * [TradeCaptureReport \<AE>](#tradecapturereport-ae): Sent on any trade *not* generated by an order (e.g. block trades).
    * [TradeCaptureReportRequestAck \<AQ>](#tradecapturereportrequestack-aq): Marks the end of a successful trade-capture replay, or rejects the replay request.
  </Accordion>
</AccordionGroup>

## Parties Repeating Group (453)

| Tag   | Name          | FIX Type   | Req | Description                                                                                                                                           |
| :---- | :------------ | :--------- | :-- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| 453   | NoPartyIDs    | NumInGroup | Y   | Number of PartyIDs in repeating group: `453=5` for all order-status, trade, and drop copy messages.                                                   |
| → 448 | PartyID       | String(20) | Y   | Party identifier/code                                                                                                                                 |
| → 447 | PartyIDSource | Char       | Y   | 447 = D (Proprietary)                                                                                                                                 |
| → 452 | PartyRole     | Int        | Y   | 1 - Subfirm Code<br />4 - Clearing Firm Code<br />11 - Order Originating Trader<br />55 - Session ID<br />3 - Client ID (ITM name used for the order) |

<Note>
  The new `PartyRole=3 (Client ID)` entry carries the name of the ITM (clearing account) that the order actually used. When firm/ITM overrides are enabled on Order Entry, this value reflects the overridden ITM; otherwise it matches the user's default ITM.
</Note>

## Orders

<a id="order-execution-reports" />

### ExecutionReport \<8> | 150=0/4/5

New (`150=0`), Canceled (`150=4`), and Replaced (`150=5`) reports share the same subset of Execution Report tags. The gateway ignores the intermediate speed-bump state and does not emit Pending New (`150=A`) or Pending Replace (`150=E`) reports for it.

* **New** (`150=0`): Confirms a new order in response to any request to generate a new order, such as `NewOrderResponse(200)` via the SBE Order Entry API. Sent for every new order, even those matched immediately.
* **Canceled** (`150=4`): Confirms an order is canceled in response to any request to cancel an order, such as `CancelOrderRequest(120)` via the SBE Order Entry API or to an unsolicited cancel.
* **Replaced** (`150=5`): Confirms order is replaced in response to any request to amend an order such as `AmendOrderRequest(110)` via the SBE Order Entry API.

| Tag  | Name                        | FIX Type         | Req | Description                                                                                                                                                                                                                                                             |
| :--- | :-------------------------- | :--------------- | :-- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Account                     | String(16)       | Y   | Unique ID representing the account — the `portfolioId` of the subaccount this order is booked to. On a full per-Member session, split the feed on this tag to separate portfolios; with `PortfolioScopeOnly` (25002=Y) it always equals the credentials' own portfolio. |
| 453  | NoPartyIDs                  | NumInGroup       | Y   | Represents the Parties repeating group. See [Parties Repeating Group (453)](#parties-repeating-group-453).                                                                                                                                                              |
| 11   | ClOrdID                     | String(36)       | Y   | Unique client ID representing the order. Must not exceed 36 ascii characters. Client system must maintain uniqueness of this value for the life of the order.                                                                                                           |
| 14   | CumQty                      | Int(9)           | Y   | Cumulated traded quantity throughout lifespan of an order.                                                                                                                                                                                                              |
| 17   | ExecID                      | String(40)       | Y   | Unique exchange ID representing the trade execution.                                                                                                                                                                                                                    |
| 37   | OrderID                     | String(17)       | Y   | Unique exchange ID representing the order.                                                                                                                                                                                                                              |
| 38   | OrderQty                    | Int(9)           | Y   | Order quantity.                                                                                                                                                                                                                                                         |
| 39   | OrdStatus                   | Char(1)          | Y   | Represents order status. <ul><li>`0` = New</li><li>`4` = Canceled</li><li>`5` = Replaced</li></ul>                                                                                                                                                                      |
| 40   | OrdType                     | Char(1)          | Y   | Order type. Market orders are not accepted during opening auction.                                                                                                                                                                                                      |
| 41   | OrigClOrdID                 | String(36)       | N   | Last accepted `ClOrdID` in the order chain.                                                                                                                                                                                                                             |
| 44   | Price                       | Price(20)        | C   | Price per single contract unit. Required for limit or stop-limit orders.                                                                                                                                                                                                |
| 54   | Side                        | Char(1)          | Y   | Side of order.                                                                                                                                                                                                                                                          |
| 55   | Symbol                      | String(24)       | Y   | Represents details of an instrument. Future Example: `EUM20`                                                                                                                                                                                                            |
| 167  | SecurityType                | String(6)        | N   | Represents security type.                                                                                                                                                                                                                                               |
| 59   | TimeInForce                 | Char(1)          | N   | Represents how long the order remains in effect. Default is `59=0` (TimeInForce="Day"). For `59=3` (TimeInForce="FAK"), `MinQty` can also be specified.                                                                                                                 |
| 60   | TransactTime                | UTCTimestamp(21) | Y   | Time when the order message was submitted. UTC format `YYYYMMDD-HH:MM:SS.ssssss` in microseconds. <br /> Example: `20091216-19:21:41.109000`                                                                                                                            |
| 99   | StopPx                      | Price(20)        | C   | Stop price of the order. Required for stop and stop-limit orders.                                                                                                                                                                                                       |
| 18   | ExecInst                    | Char             | N   | The execution instruction flags for the order.<br /><br />Supported values:<br />`6` = Add Liquidity Only (Post Only)                                                                                                                                                   |
| 110  | MinQty                      | Int(9)           | N   | Minimum quantity of an order to be executed. Used only when `59=3` (TimeInForce="Fill and Kill").                                                                                                                                                                       |
| 150  | ExecType                    | Char(1)          | Y   | Represents execution type. <ul><li>`0` = New</li><li>`4` = Canceled</li><li>`5` = Replaced</li></ul>                                                                                                                                                                    |
| 151  | LeavesQty                   | Int(9)           | Y   | Number of contracts remaining for execution.                                                                                                                                                                                                                            |
| 378  | ExecRestatementReason       | Int(3)           | N   | Reason why the order was canceled by the system (e.g., cancel on disconnect, self-match prevention, etc.).                                                                                                                                                              |
| 432  | ExpireDate                  | LocalMktDate(8)  | C   | Order expiration date, or the last day the order could trade.                                                                                                                                                                                                           |
| 528  | OrderCapacity               | Int(1)           | C   | Pass through field from/when present in NewOrder. Identifies origin of order (i.e., capacity of firm placing the order).                                                                                                                                                |
| 582  | CustOrderCapacity           | Char(1)          | C   | Pass through field from/when present in NewOrder. Customer Type Indicator as defined by NFA.                                                                                                                                                                            |
| 1028 | ManualOrderIndicator        | Boolean(1)       | Y   | Represents whether or not the order was generated manually (`Y`) or automatically (`N`) with trading software.                                                                                                                                                          |
| 1031 | CustOrderHandlingInst       | String(1)        | Y   | Source of the original order.                                                                                                                                                                                                                                           |
| 3040 | StopLimitPx                 | Price(20)        | C   | Limit order price when stop loss is triggered                                                                                                                                                                                                                           |
| 5979 | RequestTime                 | Int(20)          | N   | Time when the request was received by the exchange. Integer value representing UTC time in microseconds since epoch.                                                                                                                                                    |
| 7928 | SelfMatchPreventionID       | Int(8)           | C   | Unique ID (per executing firm) representing two orders that should not match. Required when market participants enable SelfMatch Prevention. Max length is 8 digits.                                                                                                    |
| 8000 | SelfMatchPreventionStrategy | Char(1)          | N   | Represents type of cancel instruction when SelfMatch Prevention is triggered. Client systems must also include `SelfMatchPreventionID` (7928) on the originating message.                                                                                               |
| 8001 | MmpGroupId                  | String           | N   | Identifier of the Market Maker Protection group applied to this order, mirroring the `mmpGroupId` field on the SBE Order Entry API. Present only for orders subject to MMP.                                                                                             |

## Trades

### ExecutionReport \<8> | 150=1 or 150=2

Sent for trades on orders.

| Tag  | Name                  | FIX Type         | Req | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :--- | :-------------------- | :--------------- | :-- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Account               | String(16)       | Y   | Unique ID representing the account — the `portfolioId` of the subaccount this trade is booked to. On a full per-Member session, split the feed on this tag to separate portfolios; with `PortfolioScopeOnly` (25002=Y) it always equals the credentials' own portfolio.                                                                                                                                                                                                                                                                         |
| 453  | NoPartyIDs            | NumInGroup       | Y   | Represents the Parties repeating group. See [Parties Repeating Group (453)](#parties-repeating-group-453).                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 11   | ClOrdID               | String(36)       | Y   | Unique client ID representing the order. Must not exceed 36 ascii characters. Client system must maintain uniqueness of this value for the life of the order.                                                                                                                                                                                                                                                                                                                                                                                   |
| 14   | CumQty                | Int(9)           | Y   | Cumulated traded quantity throughout lifespan of an order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 17   | ExecID                | String(40)       | Y   | Unique exchange ID representing the trade execution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 880  | TrdMatchID            | String (20)      | Y   | Unique exchange ID representing a match event that results in multiple executions or trades.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 31   | LastPx                | Price(20)        | Y   | Price at which order was filled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 32   | LastQty               | Int(9)           | Y   | Quantity filled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 37   | OrderID               | String(17)       | Y   | Unique exchange ID representing the order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 38   | OrderQty              | Int(9)           | C   | Order quantity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 39   | OrdStatus             | Char(1)          | Y   | Represents order status, "Partial Fill" (`1`) or "Complete Fill" (`2`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 40   | OrdType               | Char(1)          | Y   | Order type such as market, limit, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 41   | OrigClOrdID           | String(36)       | N   | Last accepted `ClOrdID` in the order chain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 44   | Price                 | Price(20)        | C   | Price per single contract unit.<br /><br />For Execution Report messages sent in response to Market or Stop orders (with protection), Price is the Protection Price Limit (best available price +/- protection points).<br /> If the order is not completely filled, the remaining open quantity rests on the order book at the Protection Price Limit.<br />**Note:** For spread trade Execution Reports, Price (44) is sent in the Execution Report – Fill Notice (35=`8`, 39=`1` or `2`) for the spread only and not the legs of the spread. |
| 54   | Side                  | Char(1)          | Y   | Side of order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 55   | Symbol                | String(24)       | Y   | Represents details of an instrument. Future Example: `EUM20`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 167  | SecurityType          | String(6)        | N   | Represents security type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 59   | TimeInForce           | Char(1)          | N   | Represents how long the order remains in effect. Default is `59=0` (TimeInForce="Day"). For `59=3` (TimeInForce="FAK"), `MinQty` can also be specified.                                                                                                                                                                                                                                                                                                                                                                                         |
| 60   | TransactTime          | UTCTimestamp(21) | Y   | Time when the order message was submitted. UTC format `YYYYMMDD-HH:MM:SS.ssssss` in microseconds. <br /> Example: `20091216-19:21:41.109000`                                                                                                                                                                                                                                                                                                                                                                                                    |
| 18   | ExecInst              | Char             | N   | The execution instruction flags for the order.<br /><br />Supported values:<br />`6` = Add Liquidity Only (Post Only)                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 75   | TradeDate             | LocalMktDate(8)  | Y   | Indicates date of trade reference in this message in `YYYYMMDD` format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 150  | ExecType              | Char(1)          | Y   | Represents execution type, "Trade" (`150=1 (partial fill) or 150=2 (full fill)`).                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 151  | LeavesQty             | Int(9)           | C   | Number of contracts remaining for execution after this fill.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 393  | TotalNumSecurities    | Int(3)           | N   | Number of leg fill acknowledgment messages sent with spread summary. Sent for spread fill messages only.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 442  | MultiLegReportingType | Int(1)           | N   | Represents acknowledgment of Outright, Leg of Spread, and Spread.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 527  | SecondaryExecID       | String(40)       | C   | Unique exchange ID representing link between spread summary fill notice with leg fill notice and trade cancel messages.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 528  | OrderCapacity         | Int(1)           | Y   | Represents the type of business conducted: <ul><li>`528=0` = Customer/Agency</li><li>`528=1` = Principal</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 1028 | ManualOrderIndicator  | Boolean(1)       | Y   | Represents whether or not the order was generated manually (`Y`) or automatically (`N`) with trading software.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1031 | CustOrderHandlingInst | String(1)        | Y   | Source of the original order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 5979 | RequestTime           | Int(20)          | N   | Time when the request was received by the exchange. Integer value representing UTC time in microseconds since epoch.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 828  | TrdType               | Int(1)           | N   | Type of trade. <ul><li>`0` = CLOB trade</li><li>`1` = Block trade</li><li>`2` = Liquidation trade</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 830  | TransferReason        | String           | N   | Reason for the transfer; present on fills resulting from a position transfer. `LIQUIDATED`, `ASSIGNED`                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### TradeCaptureReportRequest \<AD>

By sending a TradeCaptureReportRequest on a drop copy connection, a replay of non-order book trades (block trades, position moves) is triggered as a series of sequential TradeCaptureReport (`35=AE`) messages. The replay starts from the ExecID specified in the request. Trades are available for **24 hours**. For a full history of all trades, the Websocket APIs should be utilized.

| Tag | Name             | FIX Type   | Req | Description                                                                           |
| --- | ---------------- | ---------- | --- | ------------------------------------------------------------------------------------- |
| 568 | TradeRequestID   | String     | Y   |                                                                                       |
| 569 | TradeRequestType | Int        | Y   | Should always be set to `1`                                                           |
| 17  | ExecID           | String(40) | N   | All trades with ExecIDs larger than or equal to this value will be resent by Starbase |

### TradeCaptureReportRequestAck \<AQ>

<a id="tradecapturereportrequestack-aq" />

`TradeCaptureReportRequestAck` (`35=AQ`) is sent at the end of a successful trade-capture replay, or if the replay request is rejected. It is the trade-capture equivalent of `EventResendComplete` (`F4`) / `EventResendReject` (`F5`) for fill Execution Report replay (`F3`).

| Tag | Name               | FIX Type | Req | Description                                                                                                                                                       |
| --- | ------------------ | -------- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 568 | TradeRequestID     | String   | Y   | Echoed from the originating `TradeCaptureReportRequest`                                                                                                           |
| 569 | TradeRequestType   | Int      | Y   | Echoed from the originating `TradeCaptureReportRequest`; always `1` (matched trades)                                                                              |
| 748 | TotNumTradeReports | Int      | N   | Total number of `TradeCaptureReport` messages sent in response to the request                                                                                     |
| 749 | TradeRequestResult | Int      | Y   | Result of the request. `0` = Successful, `9` = Not authorized to retrieve trade data, `10` = Resend already in progress, `11` = ExecID out of range, `99` = Other |
| 750 | TradeRequestStatus | Int      | Y   | Status of the request. `1` = Completed, `2` = Rejected                                                                                                            |
| 58  | Text               | String   | N   | Human-readable description of the result, present on rejects                                                                                                      |

### TradeCaptureReport \<AE>

<a id="tradecapturereport-ae" />

Sent for each non-order book trade (block trade, position move), both proactively as trades occur and in response to a `TradeCaptureReportRequest`.

| Tag  | Name                  | FIX Type         | Req | Description                                                                                                                                                                                                                                                             |
| ---- | --------------------- | ---------------- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 571  | TradeReportID         | String           | Y   | Unique identifier for this trade report                                                                                                                                                                                                                                 |
| 568  | TradeRequestID        | String           | N   | Echoed from the originating `TradeCaptureReportRequest`; absent if unsolicited                                                                                                                                                                                          |
| 1    | Account               | String(16)       | Y   | Unique ID representing the account — the `portfolioId` of the subaccount this trade is booked to. On a full per-Member session, split the feed on this tag to separate portfolios; with `PortfolioScopeOnly` (25002=Y) it always equals the credentials' own portfolio. |
| 150  | ExecType              | Char(1)          | Y   | Always `F` (full and partial fills)                                                                                                                                                                                                                                     |
| 17   | ExecID                | String(40)       | Y   | Unique exchange identifier for this execution                                                                                                                                                                                                                           |
| 570  | PreviouslyReported    | Boolean(1)       | Y   | Whether this trade was previously reported to the counterparty. `Y` = previously reported, `N` = first report                                                                                                                                                           |
| 1003 | TradeID               | String           | Y   | Unique identifier for the trade                                                                                                                                                                                                                                         |
| 828  | TradeType             | Int(1)           | Y   | Type of trade. `0` = CLOB trade, `1` = Block trade, `2` = Liquidation trade, `3` = Position move                                                                                                                                                                        |
| 880  | TrdMatchID            | String(20)       | Y   | Unique identifier for the match event                                                                                                                                                                                                                                   |
| 1040 | BlockID               | String           | N   | Block trade identifier; present for block trades only                                                                                                                                                                                                                   |
| 32   | TradeQuantity         | Int(9)           | Y   | Quantity traded                                                                                                                                                                                                                                                         |
| 31   | LastPx                | Price(20)        | Y   | Price at which the trade occurred                                                                                                                                                                                                                                       |
| 60   | TransactTime          | UTCTimestamp(21) | Y   | Time of trade in UTC; `YYYYMMDD-HH:MM:SS.ssssss`                                                                                                                                                                                                                        |
| 442  | MultiLegReportingType | Int(1)           | N   | Present for trades on multi-leg instruments. `1` = Single-leg trade, `2` = Leg of a multi-leg trade, `3` = Multi-leg trade                                                                                                                                              |
| 55   | Symbol                | String(24)       | Y   | Instrument name                                                                                                                                                                                                                                                         |
| 54   | Side                  | Char(1)          | Y   | Side of the trade. `1` = Buy, `2` = Sell                                                                                                                                                                                                                                |
| 75   | TradeDate             | LocalMktDate(8)  | Y   | Trade date in `YYYYMMDD` format                                                                                                                                                                                                                                         |
| 453  | NoPartyIDs            | NumInGroup       | C   | Represents the Parties repeating group. See [Parties Repeating Group (453)](#parties-repeating-group-453).                                                                                                                                                              |
| 830  | TransferReason        | String           | N   | Reason for the transfer; present for position moves. `LIQUIDATED`, `ASSIGNED`                                                                                                                                                                                           |
| 8002 | LiquidationMechanism  | String           | N   | Liquidation mechanism; present for liquidation trades. `LSP`, `ADL`                                                                                                                                                                                                     |

## Fill Execution Report Replay

Detect gaps in the Drop Copy feed from the standard FIX `MsgSeqNum` (34) sequence numbers on incoming messages. After a gap or reconnect, recover state as follows:

* **Open orders** — resynchronize from the [open order snapshot](#open-order-snapshot-on-connect) sent automatically on connect.
* **Fills** — request a replay with `EventResendRequest` (F3), below.
* **Block trades and position moves** — request a replay with [`TradeCaptureReportRequest` (AD)](#tradecapturereportrequest-ad).

The Drop Copy connection supports on-demand replay of **fill** Execution Reports (`150=1 or 150=2`) using two message types. Non-fill Execution Reports (`150=0/4/5`) are not replayed; use the [open order snapshot](#open-order-snapshot-on-connect) to recover order state after a reconnect. Fill reports are retained for **24 hours**.

ExecIDs are sequential integers assigned per member and track fill events only. The typical flow is to first request the current last fill ExecID as a baseline, then request a replay starting from that point.

### LastFillExecIDRequest \<F1>

Sent by the client to retrieve the server's current last fill `ExecID` for this member.

| Tag | Name      | FIX Type | Req | Description                                             |
| :-- | :-------- | :------- | :-- | :------------------------------------------------------ |
| 35  | MsgType   | String   | Y   | `F1`                                                    |
| 790 | TestReqID | String   | N   | Ignored; required only to satisfy FIX schema validation |

**Response: LastFillExecID \<F2>**

| Tag | Name      | FIX Type | Req | Description                                            |
| :-- | :-------- | :------- | :-- | :----------------------------------------------------- |
| 35  | MsgType   | String   | Y   | `F2`                                                   |
| 45  | RefSeqNum | Int      | Y   | `MsgSeqNum` of the originating `LastFillExecIDRequest` |
| 17  | ExecID    | Int      | Y   | Server's current last fill ExecID for this member      |

***

### EventResendRequest \<F3>

Requests replay of fill Execution Reports (`150=1 or 150=2`) within an ExecID range. The server streams all matching reports in order, then sends `EventResendComplete`. Only fill events within the 24-hour retention window are available.

| Tag    | Name        | FIX Type | Req | Description                                                                                                  |
| :----- | :---------- | :------- | :-- | :----------------------------------------------------------------------------------------------------------- |
| 35     | MsgType     | String   | Y   | `F3`                                                                                                         |
| custom | BeginExecId | Int      | Y   | First fill ExecID to replay, inclusive. Must be within the 24-hour retention window.                         |
| custom | EndExecId   | Int      | N   | Last fill ExecID to replay, inclusive. If omitted, defaults to the current last fill ExecID for this member. |

<Note>
  Replayed fill Execution Reports are identical in format to live fill reports. There is no flag or field distinguishing a replayed message from a live one.
</Note>

**Response: EventResendComplete \<F4>**

Sent after all replayed reports have been delivered.

| Tag    | Name             | FIX Type | Req | Description                                         |
| :----- | :--------------- | :------- | :-- | :-------------------------------------------------- |
| 35     | MsgType          | String   | Y   | `F4`                                                |
| 45     | RefSeqNum        | Int      | Y   | `MsgSeqNum` of the originating `EventResendRequest` |
| custom | ResentEventCount | Int      | Y   | Total number of fill Execution Reports replayed     |

**Reject: EventResendReject \<F5>**

| Tag   | Name                    | FIX Type | Req | Description                                                    |
| :---- | :---------------------- | :------- | :-- | :------------------------------------------------------------- |
| 35    | MsgType                 | String   | Y   | `F5`                                                           |
| 45    | RefSeqNum               | Int      | Y   | `MsgSeqNum` of the originating `EventResendRequest`            |
| 22006 | EventResendRejectReason | Int      | Y   | `1` = `BEGIN_EXEC_ID_TOO_SMALL`, `2` = `END_EXEC_ID_TOO_LARGE` |
| 58    | Text                    | String   | N   | Human-readable description                                     |

<Note>
  `BEGIN_EXEC_ID_TOO_SMALL` means `BeginExecId` is older than the 24-hour retention window, or no fill Execution Reports exist yet for this member. Send a `LastFillExecIDRequest` to re-establish a valid baseline.

  `END_EXEC_ID_TOO_LARGE` means `EndExecId` refers to an event that does not yet exist. Omit `EndExecId` to replay up to the current last fill event.
</Note>

## Reconciliation Across APIs

Use the following identifiers to reconcile Drop Copy against SBE sessions and the standard WebSocket/REST APIs.

### Mapping orders

The exchange-assigned order ID is the same value on every feed:

| Feed                    | Field                                                                   |
| ----------------------- | ----------------------------------------------------------------------- |
| SBE order entry         | `orderId` (int64) on responses and unsolicited events                   |
| FIX Drop Copy           | `OrderID` (Tag 37)                                                      |
| Standard WebSocket/REST | `starbase_order_id` on orders, user trades, and transaction log entries |

To map an order seen on the standard APIs to its Drop Copy records, match `starbase_order_id` to Tag 37.

### Mapping portfolios (subaccounts)

The portfolio each event books to is carried in **Tag 1 `Account`** (the `portfolioId`) on every Execution Report and Trade Capture Report. Use it to route Drop Copy events to the right subaccount, or match it against `portfolioId` on the standard APIs. When a session is opened with `PortfolioScopeOnly` (Tag 25002=Y), Tag 1 is constant and equal to the credentials' own portfolio.

### Deduplicating fills: ExecID vs TrdMatchID

`ExecID` (Tag 17) identifies an **event**, and one event can contain multiple fills. `TrdMatchID` (Tag 880) identifies a single **fill** and is globally unique. When deduplicating fills across feeds, use the tuple `(starbase_match_id, starbase_order_id)` — `starbase_match_id` on the standard APIs corresponds to `TrdMatchID` (Tag 880) on Drop Copy.

### End-to-end client order IDs

`ClOrdID` (Tag 11) is **FIX-only** — it does not propagate to the standard WebSocket API. To track a client order ID end-to-end on WebSocket notifications, send the value in the `deribitLabel` field and read it back from the order/trade payloads there. Within SBE itself, use the numeric `clientOrderId` and the per-connection `correlationId` for request/response matching.


## Related topics

- [Infrastructure, Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [Starbase API Overview](/starbase/overview.md)
- [Starbase API Changelog](/changelogs/starbase.md)
