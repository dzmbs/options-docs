# Deribit API Documentation: Upcoming API Reference

## API Reference

- [Upcoming / API Reference / JSON-RPC API (187 pages)](https://docs.deribit.com/_llms/upcoming/api-reference/json-rpc-api.md): Documentation for Upcoming / API Reference / JSON-RPC API.

### Subscription Channels

#### Introduction

- [Notifications](https://docs.deribit.com/articles/notifications.md): Subscribe to Deribit WebSocket notification channels for real-time order updates, trade fills, market data changes, and account events across sessions.

#### Websockets

##### Platform

- [platform_state ](https://docs.deribit.com/subscriptions/upcoming/platform/platform_state.md): Platform state notifications.
- [platform_state.public_methods_state ](https://docs.deribit.com/subscriptions/upcoming/platform/platform_statepublic_methods_state.md): Notifications indicating whether unauthenticated (public) requests are currently allowed.

##### Announcements

- [announcements ](https://docs.deribit.com/subscriptions/upcoming/announcements/announcements.md): General announcements concerning the Deribit platform.

##### Orderbook

- [book.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/orderbook/bookinstrument_nameinterval.md): Real-time order book updates for a specific instrument.
- [book.(instrument_name).(group).(depth).(interval) ](https://docs.deribit.com/subscriptions/upcoming/orderbook/bookinstrument_namegroupdepthinterval.md): Aggregated order book updates for a specific instrument.

##### Market Data

- [ticker.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/market-data/tickerinstrument_nameinterval.md): Real-time ticker data providing comprehensive market information for the specified instrument.
- [incremental_ticker.(instrument_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/incremental_tickerinstrument_name.md): Real-time ticker updates for an instrument, delivered as a snapshot followed by incremental updates.
- [perpetual.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/market-data/perpetualinstrument_nameinterval.md): Provide current interest rate - but only for **perpetual** instruments. Other types won't generate any notification.
- [quote.(instrument_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/quoteinstrument_name.md): Best bid/ask price and size for a specific instrument.
- [deribit_price_index.(index_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/deribit_price_indexindex_name.md): Deribit index price updates for the given `index_name` (current index value).
- [deribit_price_ranking.(index_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/deribit_price_rankingindex_name.md): Price ranking updates for the component exchanges used to calculate the Deribit index.
- [deribit_price_statistics.(index_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/deribit_price_statisticsindex_name.md): Basic statistics for the Deribit index.
- [deribit_volatility_index.(index_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/deribit_volatility_indexindex_name.md): Volatility index updates for the given `index_name`.
- [markprice.options.(index_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/markpriceoptionsindex_name.md): Options mark price updates for the given `index_name`.
- [estimated_expiration_price.(index_name) ](https://docs.deribit.com/subscriptions/upcoming/market-data/estimated_expiration_priceindex_name.md): Estimated expiration (delivery) price updates for the given `index_name`.
- [chart.trades.(instrument_name).(resolution) ](https://docs.deribit.com/subscriptions/upcoming/market-data/charttradesinstrument_nameresolution.md): Publicly available market data used to generate a TradingView trade candle chart.
- [instrument.creation.(kind).(currency) ](https://docs.deribit.com/subscriptions/upcoming/market-data/instrumentcreationkindcurrency.md): Notification published once when an instrument is created, carrying full instrument data in the same format as `public/get_instruments`.
- [instrument.state.(kind).(currency) ](https://docs.deribit.com/subscriptions/upcoming/market-data/instrumentstatekindcurrency.md): Notifications about new or terminated instruments of a given kind in a given currency.

##### Trades

- [trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/trades/tradesinstrument_nameinterval.md): Trade notifications for a specific instrument.
- [trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/upcoming/trades/tradeskindcurrencyinterval.md): Trade notifications across all instruments for a given kind and currency.

##### Block Trade

- [block_trade_confirmations ](https://docs.deribit.com/subscriptions/upcoming/block-trade/block_trade_confirmations.md): Provides notifications regarding block trade approval. Subscribe to this channel to receive notifications about pending block trades that require your approval.
- [block_trade_confirmations.(currency) ](https://docs.deribit.com/subscriptions/upcoming/block-trade/block_trade_confirmationscurrency.md): Provides notifications regarding block trade approval. Supports filtering by currency. Subscribe to this channel to receive notifications about pending block trades that require your approval, filtered by a specific currency.

##### User

- [user.mmp_trigger.(index_name) ](https://docs.deribit.com/subscriptions/upcoming/user/usermmp_triggerindex_name.md): Real-time notifications for Market Maker Protection (MMP) triggers. This subscription provides feedback when MMP protection is activated for a given index, enabling clients to react promptly when protection is triggered.
- [user.portfolio.(currency) ](https://docs.deribit.com/subscriptions/upcoming/user/userportfoliocurrency.md): Real-time notifications for user portfolio information. This subscription provides comprehensive account and portfolio data for the specified currency, including balances, margins, profit and loss, and Greeks.
- [user.trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/usertradesinstrument_nameinterval.md): User trade notifications for a specific instrument.
- [user.trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/usertradeskindcurrencyinterval.md): User trade notifications across all instruments for a given kind and currency.
- [user.combo_trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/usercombo_tradesinstrument_nameinterval.md): User trade notifications for a specific combo instrument.
- [user.combo_trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/usercombo_tradeskindcurrencyinterval.md): User trade notifications across all combo instruments for a given kind and currency.
- [user.orders.(instrument_name).raw ](https://docs.deribit.com/subscriptions/upcoming/user/userordersinstrument_nameraw.md): User order updates for a specific instrument (raw stream).
- [user.orders.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/userordersinstrument_nameinterval.md): User order updates for a specific instrument (aggregated).
- [user.orders.(kind).(currency).raw ](https://docs.deribit.com/subscriptions/upcoming/user/userorderskindcurrencyraw.md): User order updates across all instruments for a given kind and currency (raw stream).
- [user.orders.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/userorderskindcurrencyinterval.md): User order updates across all instruments for a given kind and currency (aggregated).
- [user.changes.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/userchangesinstrument_nameinterval.md): User change stream (orders, trades, and related updates) for a specific instrument.
- [user.changes.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/upcoming/user/userchangeskindcurrencyinterval.md): User change stream (orders, trades, and related updates) across all instruments for a given kind and currency.
- [user.access_log ](https://docs.deribit.com/subscriptions/upcoming/user/useraccess_log.md): Security event notifications for the account.
- [user.lock ](https://docs.deribit.com/subscriptions/upcoming/user/userlock.md): Notifications when the account is locked or unlocked.
- [user.liquidation ](https://docs.deribit.com/subscriptions/upcoming/user/userliquidation.md): Notifications about the authenticated account's own liquidation, auto-deleveraging (ADL), and LSP (Liquidity Support Program) activity — both as the account being liquidated/deleveraged and, for ADL, as a counterparty receiving a deleveraged position.
- [user.isolated.liquidation ](https://docs.deribit.com/subscriptions/upcoming/user/userisolatedliquidation.md): Lets a **main** account observe the liquidation, ADL, and LSP activity of all of its **isolated-margin subaccounts**, without subscribing to each subaccount's own `user.liquidation` channel individually.
- [user.lsp ](https://docs.deribit.com/subscriptions/upcoming/user/userlsp.md): Notifications for an LSP (Liquidity Support Program) participant subaccount: assignment attempts (successful or failed), enable/disable state changes, and effective configuration changes.

##### Block Rfq

- [block_rfq.maker.(currency) ](https://docs.deribit.com/subscriptions/upcoming/block-rfq/block_rfqmakercurrency.md): Real-time notifications for Block RFQs (Request for Quotes) that are available for the subscribed maker to respond to.
- [block_rfq.taker.(currency) ](https://docs.deribit.com/subscriptions/upcoming/block-rfq/block_rfqtakercurrency.md): Get notifications about the state of your Block RFQ. `trades` are only visible if the Block RFQ was filled.
- [block_rfq.maker.quotes.(currency) ](https://docs.deribit.com/subscriptions/upcoming/block-rfq/block_rfqmakerquotescurrency.md): Get notifications about the state of your Block RFQ quotes. Subscribe to this channel to receive real-time updates when your quotes are added, edited, cancelled, or when quotes are accepted by takers.
- [block_rfq.trades.(currency) ](https://docs.deribit.com/subscriptions/upcoming/block-rfq/block_rfqtradescurrency.md): Get notifications about recent Block RFQ trades. This is a public channel that provides market data about completed Block RFQ trades.

### FIX API

#### Overview

- [Deribit Upcoming FIX API Overview](https://docs.deribit.com/fix-api/upcoming/overview.md): Deribit upcoming FIX API release — a FIX 4.4 subset with new fields and messages; overview of endpoints, message types, and migration from current.

#### Session Management

- [Logon(A) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/logon.md): Logon(A) — Authenticates and starts a FIX session on the upcoming Deribit FIX API release, negotiating heartbeat interval and cancel-on-disconnect.
- [Logout(5) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/logout.md): Logout(5) — Cleanly ends a FIX session on the upcoming Deribit FIX API release and controls whether working orders are cancelled on disconnect.
- [Heartbeat(0) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/heartbeat.md): Heartbeat(0) — Keeps the FIX session alive on the upcoming Deribit FIX API release and lets peers detect broken connections during idle time.
- [Test Request(1) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/test-request.md): TestRequest(1) — Solicits a Heartbeat response to verify the upcoming Deribit FIX API release session is responsive during idle trading periods.
- [Resend Request(2) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/resend-request.md): ResendRequest(2) — Recovers missed FIX messages from the upcoming Deribit FIX API release by asking the counterparty to resend a sequence number range.
- [Reject(3) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/reject.md): Reject(3) — Session-level reject issued by the upcoming Deribit FIX API release server for malformed messages or protocol violations with reason codes.
- [Sequence Reset(4) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/sequence-reset.md): SequenceReset(4) — Adjusts FIX sequence numbers on the upcoming Deribit FIX API release session to recover from gaps or after a graceful reset.

#### Market Data

- [Security List Request(x) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/security-list-request.md): SecurityListRequest(x) — Requests the full tradable instrument catalogue from the upcoming Deribit FIX API release, filterable by underlying and kind.
- [Security List(y) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/security-list.md): SecurityList(y) — Server response containing tradable instruments for the upcoming Deribit FIX API release, returned per SecurityListRequest with details.
- [Market Data Request(V) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/market-data-request.md): MarketDataRequest(V) — Subscribe or unsubscribe from order book and trade streams on the upcoming Deribit FIX API release with request scope settings.
- [Market Data Request Reject(Y) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/market-data-request-reject.md): MarketDataRequestReject(Y) — Sent when a market data subscription is rejected on the upcoming Deribit FIX API release with reason codes for the failure.
- [Market Data Snapshot/Full Refresh(W) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/market-data-snapshot.md): MarketDataSnapshotFullRefresh(W) — Initial full order book snapshot sent before incremental updates begin on the upcoming Deribit FIX API release.
- [Market Data Incremental Refresh(X) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/market-data-incremental.md): MarketDataIncrementalRefresh(X) — Streams incremental order book and trade updates on the upcoming Deribit FIX API release after a snapshot.
- [Security Status Request(e) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/security-status-request.md): SecurityStatusRequest(e) — Subscribes to trading status updates for an instrument on the upcoming Deribit FIX API release — halts, resumes, settlement.
- [Security Status(f) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/security-status.md): SecurityStatus(f) — Server-pushed notice of trading status changes (halt, resume, settlement) for an instrument on the upcoming Deribit FIX API release.

#### Order Management

- [New Order Single(D) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/new-order-single.md): NewOrderSingle(D) — Submits a new single-instrument order on the upcoming Deribit FIX API release, supporting limit, market, and advanced order types.
- [Order Cancel Request(F) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/order-cancel-request.md): OrderCancelRequest(F) — Cancels a single working order on the upcoming Deribit FIX API release by ClOrdID or OrderID, with ExecutionReport response.
- [Order Cancel Reject(9) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/order-cancel-reject.md): OrderCancelReject(9) — Rejects a cancel or cancel/replace request on the upcoming Deribit FIX API release, including reason codes for the failure.
- [Order Cancel/Replace Request(G) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/order-cancel-replace.md): OrderCancelReplaceRequest(G) — Amends price or quantity of a working order on the upcoming Deribit FIX API release without cancelling and resubmitting.
- [Order Mass Cancel Request(q) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/order-mass-cancel-request.md): OrderMassCancelRequest(q) — Cancels all working orders matching filters (instrument, side, underlying) in one call on the upcoming Deribit FIX API release.
- [Order Mass Cancel Report(r) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/order-mass-cancel-report.md): OrderMassCancelReport(r) — Reports the outcome of an order mass cancel on the upcoming Deribit FIX API release, with affected order counts and status.
- [Order Mass Status Request(AF) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/order-mass-status-request.md): OrderMassStatusRequest(AF) — Queries the status of many working orders in a single request on the upcoming Deribit FIX API release for reconciliation.
- [Execution Reports(8) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/execution-reports.md): ExecutionReport(8) — Order lifecycle updates (fills, cancels, rejects, replaces) delivered on the upcoming Deribit FIX API release for each order.

#### Position Management

- [Request For Positions(AN) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/request-for-positions.md): RequestForPositions(AN) — Requests a snapshot of open positions from the upcoming Deribit FIX API release, returned as PositionReport messages.
- [Position Report(AP) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/position-report.md): PositionReport(AP) — Server-pushed report of open positions on the upcoming Deribit FIX API release, sent in response to RequestForPositions or trades.

#### User Management

- [User Request(BE) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/user-request.md): UserRequest(BE) — Requests user status changes such as logging users in or out of a session on the upcoming Deribit FIX API release endpoint layer.
- [User Response(BF) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/user-response.md): UserResponse(BF) — Server response to a UserRequest on the upcoming Deribit FIX API release, reporting the current user session status and details.

#### Market Maker Protection

- [MMProtection Limits (MM) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/mmprotection-limits.md): MMProtectionLimits(MM) — Configures market maker protection thresholds (quantity, delta, freeze time) on the upcoming Deribit FIX API release.
- [MMProtection Limits Result/Reject(MR) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/mmprotection-limits-result.md): MMProtectionLimitsResult(MR) — Response with current MMP settings or a reject on the upcoming Deribit FIX API release market maker protection endpoint.
- [MMProtection Reset(MZ) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/mmprotection-reset.md): MMProtectionReset(MZ) — Clears a triggered market maker protection freeze on the upcoming Deribit FIX API release so quoting can resume trading.

#### Mass Quoting

- [Mass Quote(i) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/mass-quote.md): MassQuote(i) — Submits many two-sided quotes in one message on the upcoming Deribit FIX API release for market makers seeking low-latency quoting.
- [Mass Quote Acknowledgement(b) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/mass-quote-acknowledgement.md): MassQuoteAcknowledgement(b) — Confirms a MassQuote submission on the upcoming Deribit FIX API release with per-quote acceptance or reject details.
- [Quote Cancel(Z) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/quote-cancel.md): QuoteCancel(Z) — Cancels one or many outstanding mass quotes on the upcoming Deribit FIX API release without submitting new replacement quotes.

#### Trade Capture

- [TradeCaptureReportRequest(AD) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/trade-capture-report-request.md): TradeCaptureReportRequest(AD) — Requests historical or streaming trade capture reports on the upcoming Deribit FIX API release, filterable by criteria.
- [TradeCaptureReportRequestAck(AQ) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/trade-capture-report-request-ack.md): TradeCaptureReportRequestAck(AQ) — Acknowledges a TradeCaptureReportRequest on the upcoming Deribit FIX API release and signals whether reports will follow.
- [TradeCaptureReport(AE) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/trade-capture-report.md): TradeCaptureReport(AE) — Delivers executed trade details on the upcoming Deribit FIX API release, sent for TradeCaptureReportRequest or unsolicited.

#### Security Definition

- [Security Definition Request(c) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/security-definition-request.md): SecurityDefinitionRequest(c) — Requests detailed contract definitions for one instrument on the upcoming Deribit FIX API release before subscribing.
- [Security Definition(d) — Upcoming FIX API](https://docs.deribit.com/fix-api/upcoming/security-definition.md): SecurityDefinition(d) — Server response describing an instrument's contract terms and trading parameters on the upcoming Deribit FIX API release.

### Starbase API

#### Introduction

- [Starbase API Overview](https://docs.deribit.com/starbase/overview.md): Introduction to Deribit Starbase covering the low-latency binary and FIX API stack, gateway architecture, product scope, and migration from legacy SBE.
- [Starbase Connectivity Quickstart](https://docs.deribit.com/starbase/quickstart.md): Plan Starbase network access, resolve No active member errors, connect to test gateways and multicast feeds, and prepare a resilient production deployment.
- [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md): Create Starbase API keys, add team members, pick Starbase-specific scopes, and resolve the No active member error before connecting to a gateway.
- [Production Readiness Checklist](https://docs.deribit.com/starbase/production-readiness-checklist.md): Readiness checklist for clients onboarding to Starbase SBE order entry: Member setup, API key scopes, MMP risk bypass, SBE XMLs, and logon testing.
- [Infrastructure, Connectivity & Best Practices](https://docs.deribit.com/starbase/connectivity-best-practices.md): Deployment options, commercial considerations, gateway architecture, protocols, failover, and low-latency integration guidance for Starbase.

#### API Reference

- [Binary API Reference](https://docs.deribit.com/starbase/binary-api-reference.md): Complete reference for the Starbase Binary API — SBE encoding, order entry messages, market data channels, and session lifecycle handling.

##### Session Messages

- [Starbase Session Messages](https://docs.deribit.com/starbase/session-messages.md): Session-level messages in the Starbase Binary API covering logon with schemaVersion negotiation, heartbeat, logout, and gateway connection lifecycle rejects.

##### Order Entry Messages

- [Placing a New Order](https://docs.deribit.com/starbase/placing-new-order.md): Submit new orders via the Starbase Binary API — NewOrderRequest, NewOrderResponse, and NewOrderReject messages with supported order types and flags.
- [Amending an Order](https://docs.deribit.com/starbase/amending-order.md): Amend existing orders using the Starbase Binary API including AmendOrderRequest, AmendOrderResponse, and AmendOrderReject messages.
- [Cancelling an Order](https://docs.deribit.com/starbase/cancelling-order.md): Cancel a working order with the Starbase Binary API — CancelOrderRequest, CancelOrderResponse, and CancelOrderReject message flow and error codes.
- [Mass Quotes](https://docs.deribit.com/starbase/mass-quotes.md): Submit many two-sided quotes in one Starbase Binary API message with MassQuoteRequest, MassQuoteResponse, and MassQuoteReject message details.
- [Starbase Mass Cancel Messages](https://docs.deribit.com/starbase/mass-cancel.md): Cancel many Starbase orders and quotes at once using MassCancelRequest, MassQuoteCancelRequest, and the currency_pair_id sourced from InstrumentDefinition.

##### Market Data Messages

- [Maintaining the order book](https://docs.deribit.com/starbase/order-book-maintenance.md): Maintain order books using the Starbase Binary API including Buy Put, Sell Put, Buy Amount Reduced, Sell Amount Reduced, and Order Delete messages.
- [Trades](https://docs.deribit.com/starbase/trades.md): Trade messages on the Starbase Binary API — Trade Summary, Trade, and Block Trade feeds with execution details and counterparty data for reporting.
- [Starbase Reference Data and Instrument Definitions](https://docs.deribit.com/starbase/reference-data.md): Instrument metadata for the Starbase Binary API, including InstrumentDefinition fields, index and mark price sources, and quantityExponent snapshot behavior.

##### Unsolicited Events

- [Starbase Unsolicited Events](https://docs.deribit.com/starbase/unsolicited-events.md): Server-initiated Starbase Binary API events including OrderFilled fills, MMPTrigger notifications, and liquidation cancels delivered on the originating gateway.

##### REST API

- [REST Order Gateway Authentication](https://docs.deribit.com/starbase/rest-authentication.md): Authenticate requests to the Starbase REST Order Gateway using HTTP Basic credentials, including API key handling and gateway session security.
- [Get Open Orders](https://docs.deribit.com/api-reference/trading/get-open-orders.md): Returns all currently-open orders belonging to the authenticated portfolio. Orders are returned regardless of instrument or order type; filtering by instrument kind and order type is not currently supported.
- [Mass Cancel](https://docs.deribit.com/api-reference/portfolio-management/mass-cancel.md): Cancels all open orders and quotes belonging to the authenticated portfolio. No filter parameters are accepted — the cancel applies to every instrument and every side.
- [Lock Portfolio](https://docs.deribit.com/api-reference/portfolio-management/lock-portfolio.md): Locks the authenticated portfolio. All currently open `DIRECT_ACCESS` orders and quotes for this portfolio are cancelled immediately. New `DIRECT_ACCESS` orders and quotes are rejected until the portfolio is unlocked.
- [Unlock Portfolio](https://docs.deribit.com/api-reference/portfolio-management/unlock-portfolio.md): Unlocks the authenticated portfolio, resuming normal acceptance of `DIRECT_ACCESS` orders and quotes.
- [List Instruments](https://docs.deribit.com/api-reference/market-data/list-instruments.md): Returns the list of tradeable instruments, including `index_id` and `product_group`, optionally filtered by base currency, instrument kind, and expiration status.

##### FIX Drop Copy

- [Starbase FIX Drop Copy API](https://docs.deribit.com/starbase/fix-drop-copy-api.md): Starbase FIX Drop Copy delivers a per-Member feed of orders, trades, and executions, with reconciliation guidance for ID mapping, dedup, and gap replay.

#### Core Concepts

- [Market Model](https://docs.deribit.com/starbase/market-model.md): The market model of Starbase is a subset of Deribit's market model. In Starbase, instruments are linked with Indices and Underlyings.
- [Account Model](https://docs.deribit.com/starbase/account-model.md): How the Starbase account and subaccount hierarchy differs from the Deribit main platform for order entry, drop copy, and permission scoping.
- [Underlying Tiers](https://docs.deribit.com/starbase/underlying-tiers.md): Assets on Starbase are classified into three tiers based on liquidity. Tier assignments determine rate limits and multicast channel assignments.
- [Speed Bumps](https://docs.deribit.com/starbase/speed-bumps.md): Speed bumps in Starbase API for options trading, including how aggressive orders are delayed and how market makers are protected from latency arbitrage.
- [Starbase Market Maker Protection (MMP)](https://docs.deribit.com/starbase/mmp.md): Configure and reset Starbase Market Maker Protection thresholds, tag orders as MMP, and understand the per subaccount and base/quote pair MMP scope.
- [Self Match Prevention (SMP)](https://docs.deribit.com/starbase/smp.md): Prevent orders on the same member from matching each other — configure Self Match Prevention groups and choose the cancel behavior policy.
- [Portfolio Management](https://docs.deribit.com/starbase/portfolio-management.md): Portfolio-scoped controls in Starbase — mass cancellation, direct-access order entry, and lock or unlock endpoints for risk operations workflows.

#### Technical Information

- [Starbase API Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md): Rate limiting rules for the Starbase order entry gateways. Covers per-subaccount key quotas, burst-equals-refill defaults, and gateway throttling behavior.
- [Risk Bypass](https://docs.deribit.com/starbase/risk-bypass.md): How privileged Starbase sessions can bypass pre-trade risk checks for certain low-latency workflows — configuration, scope, and eligibility requirements.
- [Cancel on Disconnect](https://docs.deribit.com/starbase/cancel-on-disconnect.md): Automatically cancel working orders when a Starbase session drops — enable Cancel on Disconnect, configure it, and combine with heartbeats for safety.
- [Gateway Connectivity](https://docs.deribit.com/starbase/gateway-connectivity.md): Starbase gateway endpoints, host lists, connection credentials, and network requirements for reaching the order entry and market data servers.
- [Multicast Channels](https://docs.deribit.com/starbase/multicast-channels.md): Starbase SBE Market Data Feed multicast channels over UDP — channel assignments sharded by product type with A/B twins for redundancy and low latency.
- [Multicast Subscription Guide](https://docs.deribit.com/starbase/multicast-subscription-guide.md): Step-by-step procedure to subscribe and unsubscribe from Starbase UDP multicast market data feeds, including channel discovery and IGMP setup.
- [Multicast Retransmit Gateway](https://docs.deribit.com/starbase/retransmit-gateway.md): Recover missed Starbase multicast messages via the UDP unicast retransmit service — request ranges by sequence number to fill incremental feed gaps.

## OpenAPI Specs

- [deribit_upcoming_openapi](/specifications/deribit_upcoming_openapi.json)
- [starbase_rest_openapi](/specifications/starbase_rest_openapi.json)

## AsyncAPI Specs

- [deribit_upcoming_asyncapi](/specifications/deribit_upcoming_asyncapi.json)
