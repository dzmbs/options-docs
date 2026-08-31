# Deribit API Documentation: Production API Reference

## API Reference

- [Production / API Reference / JSON-RPC API (183 pages)](https://docs.deribit.com/_llms/production/api-reference/json-rpc-api.md): Documentation for Production / API Reference / JSON-RPC API.

### Subscription Channels

#### Introduction

- [Notifications](https://docs.deribit.com/articles/notifications.md): Subscribe to Deribit WebSocket notification channels for real-time order updates, trade fills, market data changes, and account events across sessions.

#### Websockets

##### Platform

- [platform_state ](https://docs.deribit.com/subscriptions/platform/platform_state.md): Platform state notifications.
- [platform_state.public_methods_state ](https://docs.deribit.com/subscriptions/platform/platform_statepublic_methods_state.md): Notifications indicating whether unauthenticated (public) requests are currently allowed.

##### Announcements

- [announcements ](https://docs.deribit.com/subscriptions/announcements/announcements.md): General announcements concerning the Deribit platform.

##### Orderbook

- [book.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_nameinterval.md): Real-time order book updates for a specific instrument.
- [book.(instrument_name).(group).(depth).(interval) ](https://docs.deribit.com/subscriptions/orderbook/bookinstrument_namegroupdepthinterval.md): Aggregated order book updates for a specific instrument.

##### Market Data

- [ticker.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/market-data/tickerinstrument_nameinterval.md): Real-time ticker data providing comprehensive market information for the specified instrument.
- [incremental_ticker.(instrument_name) ](https://docs.deribit.com/subscriptions/market-data/incremental_tickerinstrument_name.md): Real-time ticker updates for an instrument, delivered as a snapshot followed by incremental updates.
- [perpetual.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/market-data/perpetualinstrument_nameinterval.md): Provide current interest rate - but only for **perpetual** instruments. Other types won't generate any notification.
- [quote.(instrument_name) ](https://docs.deribit.com/subscriptions/market-data/quoteinstrument_name.md): Best bid/ask price and size for a specific instrument.
- [deribit_price_index.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_indexindex_name.md): Deribit index price updates for the given `index_name` (current index value).
- [deribit_price_ranking.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_rankingindex_name.md): Price ranking updates for the component exchanges used to calculate the Deribit index.
- [deribit_price_statistics.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_price_statisticsindex_name.md): Basic statistics for the Deribit index.
- [deribit_volatility_index.(index_name) ](https://docs.deribit.com/subscriptions/market-data/deribit_volatility_indexindex_name.md): Volatility index updates for the given `index_name`.
- [markprice.options.(index_name) ](https://docs.deribit.com/subscriptions/market-data/markpriceoptionsindex_name.md): Options mark price updates for the given `index_name`.
- [estimated_expiration_price.(index_name) ](https://docs.deribit.com/subscriptions/market-data/estimated_expiration_priceindex_name.md): Estimated expiration (delivery) price updates for the given `index_name`.
- [chart.trades.(instrument_name).(resolution) ](https://docs.deribit.com/subscriptions/market-data/charttradesinstrument_nameresolution.md): Publicly available market data used to generate a TradingView trade candle chart.
- [instrument.creation.(kind).(currency) ](https://docs.deribit.com/subscriptions/market-data/instrumentcreationkindcurrency.md): Notification published once when an instrument is created, carrying full instrument data in the same format as `public/get_instruments`.
- [instrument.state.(kind).(currency) ](https://docs.deribit.com/subscriptions/market-data/instrumentstatekindcurrency.md): Notifications about new or terminated instruments of a given kind in a given currency.

##### Trades

- [trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/trades/tradesinstrument_nameinterval.md): Trade notifications for a specific instrument.
- [trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/trades/tradeskindcurrencyinterval.md): Trade notifications across all instruments for a given kind and currency.

##### Block Trade

- [block_trade_confirmations ](https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmations.md): Provides notifications regarding block trade approval. Subscribe to this channel to receive notifications about pending block trades that require your approval.
- [block_trade_confirmations.(currency) ](https://docs.deribit.com/subscriptions/block-trade/block_trade_confirmationscurrency.md): Provides notifications regarding block trade approval. Supports filtering by currency. Subscribe to this channel to receive notifications about pending block trades that require your approval, filtered by a specific currency.

##### User

- [user.mmp_trigger.(index_name) ](https://docs.deribit.com/subscriptions/user/usermmp_triggerindex_name.md): Real-time notifications for Market Maker Protection (MMP) triggers. This subscription provides feedback when MMP protection is activated for a given index, enabling clients to react promptly when protection is triggered.
- [user.portfolio.(currency) ](https://docs.deribit.com/subscriptions/user/userportfoliocurrency.md): Real-time notifications for user portfolio information. This subscription provides comprehensive account and portfolio data for the specified currency, including balances, margins, profit and loss, and Greeks.
- [user.trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/user/usertradesinstrument_nameinterval.md): User trade notifications for a specific instrument.
- [user.trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/user/usertradeskindcurrencyinterval.md): User trade notifications across all instruments for a given kind and currency.
- [user.combo_trades.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/user/usercombo_tradesinstrument_nameinterval.md): User trade notifications for a specific combo instrument.
- [user.combo_trades.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/user/usercombo_tradeskindcurrencyinterval.md): User trade notifications across all combo instruments for a given kind and currency.
- [user.orders.(instrument_name).raw ](https://docs.deribit.com/subscriptions/user/userordersinstrument_nameraw.md): User order updates for a specific instrument (raw stream).
- [user.orders.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/user/userordersinstrument_nameinterval.md): User order updates for a specific instrument (aggregated).
- [user.orders.(kind).(currency).raw ](https://docs.deribit.com/subscriptions/user/userorderskindcurrencyraw.md): User order updates across all instruments for a given kind and currency (raw stream).
- [user.orders.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/user/userorderskindcurrencyinterval.md): User order updates across all instruments for a given kind and currency (aggregated).
- [user.changes.(instrument_name).(interval) ](https://docs.deribit.com/subscriptions/user/userchangesinstrument_nameinterval.md): User change stream (orders, trades, and related updates) for a specific instrument.
- [user.changes.(kind).(currency).(interval) ](https://docs.deribit.com/subscriptions/user/userchangeskindcurrencyinterval.md): User change stream (orders, trades, and related updates) across all instruments for a given kind and currency.
- [user.access_log ](https://docs.deribit.com/subscriptions/user/useraccess_log.md): Security event notifications for the account.
- [user.lock ](https://docs.deribit.com/subscriptions/user/userlock.md): Notifications when the account is locked or unlocked.
- [user.liquidation ](https://docs.deribit.com/subscriptions/user/userliquidation.md): Notifications about the authenticated account's own liquidation, auto-deleveraging (ADL), and LSP (Liquidity Support Program) activity — both as the account being liquidated/deleveraged and, for ADL, as a counterparty receiving a deleveraged position.
- [user.isolated.liquidation ](https://docs.deribit.com/subscriptions/user/userisolatedliquidation.md): Lets a **main** account observe the liquidation, ADL, and LSP activity of all of its **isolated-margin subaccounts**, without subscribing to each subaccount's own `user.liquidation` channel individually.
- [user.lsp ](https://docs.deribit.com/subscriptions/user/userlsp.md): Notifications for an LSP (Liquidity Support Program) participant subaccount: assignment attempts (successful or failed), enable/disable state changes, and effective configuration changes.

##### Block Rfq

- [block_rfq.maker.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakercurrency.md): Real-time notifications for Block RFQs (Request for Quotes) that are available for the subscribed maker to respond to.
- [block_rfq.taker.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqtakercurrency.md): Get notifications about the state of your Block RFQ. `trades` are only visible if the Block RFQ was filled.
- [block_rfq.maker.quotes.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqmakerquotescurrency.md): Get notifications about the state of your Block RFQ quotes. Subscribe to this channel to receive real-time updates when your quotes are added, edited, cancelled, or when quotes are accepted by takers.
- [block_rfq.trades.(currency) ](https://docs.deribit.com/subscriptions/block-rfq/block_rfqtradescurrency.md): Get notifications about recent Block RFQ trades. This is a public channel that provides market data about completed Block RFQ trades.

### FIX API

#### Overview

- [Deribit Production FIX API Overview](https://docs.deribit.com/fix-api/production/overview.md): Overview of the Deribit production FIX 4.4 subset covering endpoints, supported message types, and how the live FIX gateway differs from the upcoming one.

#### Session Management

- [Logon(A) — Production FIX API](https://docs.deribit.com/fix-api/production/logon.md): Logon(A) authenticates and establishes a session on the Deribit production FIX API, covering credentials, heartbeat interval, and cancel-on-disconnect setup.
- [Logout(5) — Production FIX API](https://docs.deribit.com/fix-api/production/logout.md): Logout(5) terminates a session on the Deribit production FIX API, describing the proper shutdown sequence and Cancel on Disconnect behavior on exit.
- [Heartbeat(0) — Production FIX API](https://docs.deribit.com/fix-api/production/heartbeat.md): Heartbeat(0) message exchanged between counterparties to verify the Deribit production FIX session is alive and detect connection loss during idle periods.
- [Test Request(1) — Production FIX API](https://docs.deribit.com/fix-api/production/test-request.md): TestRequest(1) solicits a Heartbeat response from the counterparty to verify the Deribit production FIX session is responsive during idle connection periods.
- [Resend Request(2) — Production FIX API](https://docs.deribit.com/fix-api/production/resend-request.md): ResendRequest(2) recovers missed FIX messages from the Deribit production sequence gap by asking the counterparty to resend a specified message range.
- [Reject(3) — Production FIX API](https://docs.deribit.com/fix-api/production/reject.md): Reject(3) is the session-level reject sent by the Deribit production FIX server for malformed messages or protocol violations, with tag-level reason codes.
- [Sequence Reset(4) — Production FIX API](https://docs.deribit.com/fix-api/production/sequence-reset.md): SequenceReset(4) repositions FIX sequence numbers on the Deribit production FIX session to recover from gaps or apply a graceful counterparty reset.

#### Market Data

- [Security List Request(x) — Production FIX API](https://docs.deribit.com/fix-api/production/security-list-request.md): SecurityListRequest(x) requests the full list of tradable instruments from the Deribit production FIX API, filterable by underlying and product kind.
- [Security List(y) — Production FIX API](https://docs.deribit.com/fix-api/production/security-list.md): SecurityList(y) is the server response containing the tradable instrument catalogue for the Deribit production FIX API, returned per SecurityListRequest.
- [Market Data Request(V) — Production FIX API](https://docs.deribit.com/fix-api/production/market-data-request.md): FIX Market Data Request subscribes to order book data and market updates. Learn how to request snapshots and incremental updates via FIX.
- [Market Data Request Reject(Y) — Production FIX API](https://docs.deribit.com/fix-api/production/market-data-request-reject.md): MarketDataRequestReject(Y) is the Deribit production FIX API server response when a MarketDataRequest is refused, listing reject reason codes and remediation.
- [Market Data Snapshot (W) — Production FIX API](https://docs.deribit.com/fix-api/production/market-data-snapshot.md): MarketDataSnapshotFullRefresh(W) delivers the initial full order book snapshot on the Deribit production FIX API before incremental updates begin streaming.
- [Market Data Incremental Refresh(X) — Production FIX API](https://docs.deribit.com/fix-api/production/market-data-incremental.md): MarketDataIncrementalRefresh(X) delivers incremental order book updates and trade events on the Deribit production FIX API after a snapshot subscription.
- [Security Status Request(e) — Production FIX API](https://docs.deribit.com/fix-api/production/security-status-request.md): SecurityStatusRequest(e) subscribes to trading status updates for an instrument on the Deribit production FIX API, covering halts, resumes, and settlement.
- [Security Status(f) — Production FIX API](https://docs.deribit.com/fix-api/production/security-status.md): SecurityStatus(f) is the server-pushed notification of trading status changes such as halt, resume, or settlement for a Deribit production FIX instrument.

#### Order Management

- [New Order Single(D) — Production FIX API](https://docs.deribit.com/fix-api/production/new-order-single.md): NewOrderSingle(D) submits new orders to the Deribit production FIX API — order types, parameters, and how to place limit, market, and advanced orders.
- [Order Cancel Request(F) — Production FIX API](https://docs.deribit.com/fix-api/production/order-cancel-request.md): FIX Order Cancel Request cancels existing orders. Learn how to cancel orders by order ID, client order ID, or label using FIX protocol.
- [Order Cancel Reject(9) — Production FIX API](https://docs.deribit.com/fix-api/production/order-cancel-reject.md): OrderCancelReject(9) is the server reject for a cancel or cancel/replace request on the Deribit production FIX API, including reason codes for the failure.
- [Order Cancel/Replace Request(G) — Production FIX API](https://docs.deribit.com/fix-api/production/order-cancel-replace.md): OrderCancelReplaceRequest(G) modifies the price or quantity of a working order on the Deribit production FIX API without cancelling and resubmitting it.
- [Order Mass Cancel Request(q) — Production FIX API](https://docs.deribit.com/fix-api/production/order-mass-cancel-request.md): OrderMassCancelRequest(q) cancels all open orders matching filters like instrument, side, or underlying in one Deribit production FIX API message.
- [Order Mass Cancel Report(r) — Production FIX API](https://docs.deribit.com/fix-api/production/order-mass-cancel-report.md): OrderMassCancelReport(r) is the server report confirming or rejecting a mass cancel operation on the Deribit production FIX API, with affected order counts.
- [Order Mass Status Request(AF) — Production FIX API](https://docs.deribit.com/fix-api/production/order-mass-status-request.md): OrderMassStatusRequest(AF) requests the current status of many open orders in a single call on the Deribit production FIX API for efficient reconciliation.
- [Execution Reports(8) — Production FIX API](https://docs.deribit.com/fix-api/production/execution-reports.md): FIX Execution Reports provide order status updates and trade confirmations. Learn how to receive and interpret execution reports for order changes and fills.

#### Position Management

- [Request For Positions(AN) — Production FIX API](https://docs.deribit.com/fix-api/production/request-for-positions.md): RequestForPositions(AN) requests a snapshot of open positions from the Deribit production FIX API, returned to the client as PositionReport messages.
- [Position Report(AP) — Production FIX API](https://docs.deribit.com/fix-api/production/position-report.md): PositionReport(AP) is the server-pushed report of open positions on the Deribit production FIX API, sent in response to a RequestForPositions or trade update.

#### User Management

- [User Request(BE) — Production FIX API](https://docs.deribit.com/fix-api/production/user-request.md): UserRequest(BE) requests user status changes such as logging users in or out of the Deribit production FIX API session for account-level control.
- [User Response(BF) — Production FIX API](https://docs.deribit.com/fix-api/production/user-response.md): UserResponse(BF) is the server response to a UserRequest on the Deribit production FIX API, reporting the current user status after processing.

#### Market Maker Protection

- [MMProtection Limits (MM) — Production FIX API](https://docs.deribit.com/fix-api/production/mmprotection-limits.md): MMProtectionLimits(MM) sets market maker protection thresholds such as quantity, delta, and frozen time on the Deribit production FIX API endpoint.
- [MMProtection Limits Result (MR) — Production FIX API](https://docs.deribit.com/fix-api/production/mmprotection-limits-result.md): MMProtectionLimitsResult(MR) is the server response with current MMP settings or a reject on the Deribit production FIX market maker protection endpoint.
- [MMProtection Reset(MZ) — Production FIX API](https://docs.deribit.com/fix-api/production/mmprotection-reset.md): MMProtectionReset(MZ) clears a triggered market maker protection freeze on the Deribit production FIX API so quoting can resume after an MMP event.

#### Mass Quoting

- [Mass Quote(i) — Production FIX API](https://docs.deribit.com/fix-api/production/mass-quote.md): MassQuote(i) submits many two-sided quotes in a single message on the Deribit production FIX API, letting market makers reduce quoting latency at scale.
- [Mass Quote Acknowledgement(b) — Production FIX API](https://docs.deribit.com/fix-api/production/mass-quote-acknowledgement.md): MassQuoteAcknowledgement(b) is the server acknowledgement for a MassQuote submission on Deribit production FIX, with per-quote status and reject reasons.
- [Quote Cancel(Z) — Production FIX API](https://docs.deribit.com/fix-api/production/quote-cancel.md): QuoteCancel(Z) cancels one or many previously submitted mass quotes on the Deribit production FIX API without needing to submit any replacement quotes.

#### Trade Capture

- [TradeCaptureReportRequest(AD) — Production FIX API](https://docs.deribit.com/fix-api/production/trade-capture-report-request.md): TradeCaptureReportRequest(AD) requests historical or streaming trade capture reports on the Deribit production FIX API, filterable by trade criteria.
- [TradeCaptureReportRequestAck(AQ) — Production FIX API](https://docs.deribit.com/fix-api/production/trade-capture-report-request-ack.md): TradeCaptureReportRequestAck(AQ) acknowledges a TradeCaptureReportRequest on the Deribit production FIX API and indicates whether reports will follow.
- [TradeCaptureReport(AE) — Production FIX API](https://docs.deribit.com/fix-api/production/trade-capture-report.md): TradeCaptureReport(AE) delivers executed trade details on the Deribit production FIX API in response to a TradeCaptureReportRequest or as unsolicited updates.

#### Security Definition

- [Security Definition Request(c) — Production FIX API](https://docs.deribit.com/fix-api/production/security-definition-request.md): SecurityDefinitionRequest(c) requests detailed contract definitions for one instrument on the Deribit production FIX API before market data subscription.
- [Security Definition(d) — Production FIX API](https://docs.deribit.com/fix-api/production/security-definition.md): SecurityDefinition(d) is the server response describing an instrument's contract terms and trading parameters on the Deribit production FIX API.

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

- [deribit_openapi](/specifications/deribit_openapi.json)
- [starbase_rest_openapi](/specifications/starbase_rest_openapi.json)

## AsyncAPI Specs

- [deribit_asyncapi](/specifications/deribit_asyncapi.json)
