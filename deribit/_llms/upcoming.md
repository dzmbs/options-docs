# Deribit API Documentation: Upcoming

## Upcoming

- [Upcoming / API Reference (307 pages)](https://docs.deribit.com/_llms/upcoming/api-reference.md): Documentation for Upcoming / API Reference.

### Overview

#### Introduction

- [Welcome to Deribit API](https://docs.deribit.com/index.md): Deribit is a crypto derivatives exchange offering futures, options, and perpetuals — this documentation is your integration entry point for the API.
- [Quickstart Guide](https://docs.deribit.com/articles/deribit-quickstart.md): Get started with the Deribit API — environment setup, first authenticated request, and key endpoints for placing your first order in minutes.

#### Authentication

- [Creating new API key](https://docs.deribit.com/articles/creating-api-key.md): Generate a new Deribit API key from the web interface or programmatically, including choosing scopes, IP restrictions, and secret handling tips.
- [Authentication](https://docs.deribit.com/articles/authentication.md): OAuth 2.0-style authentication for private Deribit API requests, covering access tokens, refresh tokens, scopes, and signature-based login flows.
- [Access Scope](https://docs.deribit.com/articles/access-scope.md): OAuth scope controls read and write access for Deribit API tokens, letting you set granular permission levels for account, trade, and wallet actions.
- [Security Keys](https://docs.deribit.com/articles/security-keys.md): Hardware security keys and additional signing requirements for sensitive Deribit API methods like withdrawals, key management, and Travel Rule data.

#### Technical Information

- [API Usage Policy](https://docs.deribit.com/articles/api-usage-policy.md): Deribit fair-use API policy outlines acceptable traffic patterns, throttling rules, and consequences of abuse to keep exchange infrastructure healthy.
- [Rate Limits](https://docs.deribit.com/articles/rate-limits.md): Credit-based rate limiting on the Deribit API — burst versus sustained caps, matching engine limits, and per-tier request allocations by account.

#### Best Practices

- [Connection Management](https://docs.deribit.com/articles/connection-management-best-practices.md): Best practices for Deribit WebSocket connection lifecycle including heartbeats, session versus connection tokens, and reliable reconnect strategies.
- [Market Data Collection](https://docs.deribit.com/articles/market-data-collection-best-practices.md): Strategies for efficient Deribit market data ingestion — snapshots, incremental updates, throttling, and choosing the right channels per instrument.
- [Options Data Collection](https://docs.deribit.com/articles/options-data-collection-best-practices.md): Collect Deribit options market data efficiently — order books, ticker greeks, mark prices, implied volatility, combos, trades, and settlement data.
- [Order Management](https://docs.deribit.com/articles/order-management-best-practices.md): High-performance order management on Deribit — batching, cancel and replace flows, label usage, and avoiding rate limit throttling under load.

#### Guides

- [Managing Deposits](https://docs.deribit.com/articles/managing-deposits-api.md): Generate deposit addresses, check deposit status and history, and submit Travel Rule originator information using the Deribit deposit API endpoints.
- [Managing Transfers](https://docs.deribit.com/articles/managing-transfers-api.md): Transfer funds between the main account and subaccounts or to other Deribit users using the API, including two-step confirmation flows for security.
- [Managing Subaccounts](https://docs.deribit.com/articles/managing-subaccounts-api.md): Create, rename, configure permissions, and manage Deribit subaccounts programmatically via API for team access control and portfolio segregation.
- [Managing Withdrawals](https://docs.deribit.com/articles/managing-withdrawals-api.md): Whitelist withdrawal addresses, create withdrawal requests, and handle Travel Rule compliance through Deribit API endpoints for crypto asset payouts.
- [Coinbase Wallet API](https://docs.deribit.com/articles/coinbase-wallet-api.md): Wallet API behavior for Coinbase-custodied Deribit accounts: network selection, deposit addresses, address book and CTN counterparties, and withdrawals.
- [Moving Positions](https://docs.deribit.com/articles/moving-positions-api.md): Transfer open positions between Deribit subaccounts using the API, including required permissions, valuation, and settlement of moved contracts.
- [Block Trading](https://docs.deribit.com/articles/block-trading-api.md): Negotiate and execute block trades between two counterparties on Deribit via API, including quote verification, approval, and settlement workflows.
- [Voice Broker Trading API](https://docs.deribit.com/articles/voice-broker-trading-api.md): How voice brokers submit block trades for clients on Deribit and how clients approve, reject, and monitor those trades via API endpoints and events.
- [Asymmetric API Keys](https://docs.deribit.com/articles/asymmetric-api-keys.md): Asymmetric API keys use public and private key pairs to sign Deribit requests, offering stronger authentication and reduced credential exposure risk.
- [Market Maker Protection (MMP) API Configuration](https://docs.deribit.com/articles/market-maker-protection.md): Configure MMP thresholds, freeze times, and reset behavior for market maker order flow on Deribit via API to guard against toxic fills and runaways.
- [Liquidity Support Program (LSP) API Guide](https://docs.deribit.com/articles/lsp-api-guide.md): Deribit's Liquidity Support Program (LSP) transfers liquidated positions to designated participant accounts before falling back to auto-deleveraging (ADL).
- [Accessing Historical Trades and Orders Using API](https://docs.deribit.com/articles/accessing-historical-trades-orders.md): Use the historical parameter on Deribit API endpoints to retrieve past trades and orders beyond the default lookback window for backfills and audits.
- [Deribit Block RFQ API Walkthrough](https://docs.deribit.com/articles/block-rfq-api-walkthrough.md): Step-by-step Block RFQ API walkthrough for requesting quotes on large block trades from Deribit market makers and executing multi-leg strategies.
- [Mass Quotes Specifications](https://docs.deribit.com/articles/mass-quotes-specifications.md): Use the Deribit mass quote API to submit many bid and ask pairs in a single request for lower latency during option and future market making.
- [Spot Trading: Deribit and Coinbase-Routed Instruments](https://docs.deribit.com/articles/spot-trading-venues.md): Which Deribit spot instruments are matched on Deribit and which are routed to Coinbase Exchange, and how order entry and market data differ between them.

### Changelogs

#### Changelogs

- [JSON-RPC API Changelog](https://docs.deribit.com/changelogs/jsonrpc.md): Release notes for the Deribit JSON-RPC API covering new endpoints, parameter changes, subscription updates, and backward-compatibility announcements.
- [FIX API Changelog](https://docs.deribit.com/changelogs/fix.md): Release notes for the Deribit FIX API covering new tags, message changes, session behavior updates, and backward-compatibility announcements.
- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md): Release notes for the Deribit Starbase binary and REST APIs covering new messages, protocol changes, performance updates, and compatibility notes.

## OpenAPI Specs

- [deribit_upcoming_openapi](/specifications/deribit_upcoming_openapi.json)
- [starbase_rest_openapi](/specifications/starbase_rest_openapi.json)

## AsyncAPI Specs

- [deribit_upcoming_asyncapi](/specifications/deribit_upcoming_asyncapi.json)
