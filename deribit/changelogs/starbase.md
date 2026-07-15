> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Starbase API Changelog

> Changes and announcements for the Deribit Starbase API.

<Update label="Starbase Release 15.07.2026 — v1.2">
  ## API Changes

  The order entry SBE schema has been updated to version `9` (`semanticVersion` `1.2`).

  ### Order Entry

  New `OrderFlags` value (`NewOrderRequest`):

  * `cancelOnDisconnect` — new order-level flag for cancel-on-disconnect handling

  New `CancelReason` value:

  * `QTY_TICK_SIZE_RESCALE` (17) — instrument `qtyTickSize` changed and the order's quantity is not exactly representable under the new tick

  New `OrderRejectReason` value:

  * `MEMBER_SPEED_BUMP_LIMIT_EXCEEDED` (29) — member has too many live speed-bumped orders

  New `CancelOrderRejectReason` values:

  * `TIME_IN_FORCE` (7) — cancel rejected based on the order's time in force
  * `SPEED_BUMP_CONVERTED_TO_IOC` (8) — cancel rejected because the speed-bumped order was already converted to IOC

  `OrderPlaced` (312) updated:

  * New `correlationId` field — echoes the `correlationId` from the originating `NewOrderRequest`, aligning `OrderPlaced` with other order-entry response messages

  ### FIX Drop Copy

  New `ExecutionReport` fields:

  * `TransferReason`
  * `MmpGroupId` (tag `8001`)

  New `OrdRejReason` (103) value:

  * `69` — `MEMBER_SPEED_BUMP_LIMIT_EXCEEDED`

  New `ExecType` (150) value:

  * `I` — `ORDER_STATUS`
</Update>

<Update label="Announcement 03.07.2026">
  ## Announcement

  We're writing to inform you of a **delay** to the Starbase production go-live. The two key dates are changing, resulting in a total delay **of 2 weeks**.

  * Market data, FIX Drop Copy and gateway connectivity: now 21st of July, previously 13th of July
  * Speed bump activation: now 28th of July, previously 13th of July
  * SBE order entry gateway access: now 4th of August, previously 20th of July

  We have recently experienced postponements in production deployments, which in turn delayed the rollout of key features. To ensure stability throughout the entire migration, we are adjusting the schedule.

  Certain production order books are already matching on Starbase. The more order books we have on Starbase and the longer they match, the more certain we are of performance and resilience. We migrated some order books later than we would have liked and feel additional time is prudent.

  Three key features will appear on Starbase's test-environment in the coming week or so. To give you and us ample time to test these, two extra weeks are necessary.

  * Speed bumps. We aim to activate speed bumps on the test environment early next week.
  * Cancel-on-disconnect. Cancel-on-disconnect (CoD) is not yet available on the test environment. We will ensure this is available one week before the 4th of August.
  * L2 market data. As some of you have noticed, orders or quotes submitted directly on Starbase are not yet reflected in the Deribit UI or legacy L2 market data feeds. We aim to integrate this on the test environment next week.

  Deribit is undergoing many changes this year. We want to assure you that many of the other key initiatives are NOT affected by this delay, including:

  * The merger with Coinbase International, now scheduled for the 9th of September. This was communicated to Coinbase International clients earlier this week. If you are unaware, please reach out to your point of contact.
  * We plan to list all of Coinbase International's perpetuals on Deribit between the 10th of August and 9th of September.
  * Our BTC and ETH options will switch from cash-settled to futures-settled as of August 1st.
  * New fees, quoting programs and the launch of the Liquidity Support Program are still slated for August 1st.

  We apologize for the delay and hope the additional two weeks allow you to better support Starbase at launch. Please reach out to your point of contact with any questions or concerns.
</Update>

<Update label="Starbase Release 26.06.2026 — v1.1">
  ## API Changes

  The order entry SBE schema has been updated to version `4`.

  ### Order Entry

  New message:

  * `CancelOrderByIdRequest` (125) — cancel an order by its exchange-assigned `orderId` instead of `clientOrderId`

  New `CancelOrderRejectReason` values:

  * `IN_LIQUIDATION` (5) — cancel rejected because the portfolio is in liquidation
  * `INVALID_INSTRUMENT` (6) — cancel rejected because the instrument is not valid

  New `MassQuoteRejectReason` value:

  * `DUPLICATE_INSTRUMENT` (8) — the same instrument appears in more than one entry of a single mass quote
</Update>

<Update label="Announcement 18.06.2026">
  ## Announcement

  We are one month away from the go-live of Starbase. Below is a confirmation of key timelines along with important details on speed bumps, rate limits, spot and circuit redundancy.

  ### Confirmation of Timelines

  * **July 13th:** Member and API key creation will be available in the UI, along with four SBE Order Entry endpoints for connectivity testing: Logon, Logout, Heartbeat, and Test. Access to market data and FIX drop copy will also be enabled on this date. Multicast market data feeds will begin propagating to client servers within LD4, AWS eu-west-2 and AWS ap-northeast-1 for all derivatives. This phased rollout ensures a smooth transition before order entry go-live.
  * **July 20th (Go-Live):** Clients will receive full access to the SBE Order Entry gateway for all derivatives.

  ### Speed Bumps

  We have experienced delays in the rollout of [speed bumps](/starbase/speed-bumps) to the test environment due to some downstream processes not handling the new order state well. The speed bump as described in our documentation will go live on Starbase's test environment at least two weeks ahead of the production go-live.

  Speed bumps will apply to every instrument except the top 5 crypto perpetuals by volume: BTC, ETH, SOL, XRP and HYPE. This also means BTC and ETH inverse perpetuals are exempt from speed bumps. The following instruments will all be speed bumped:

  * All crypto and RWA perpetuals, except BTC, ETH, SOL, XRP and HYPE
  * All options, both inverse and linear
  * All dated futures, both inverse and linear
  * All multi-leg instruments including one of the above as a leg (future spreads, option combinations)

  To align with market standards, each order or quote in the speed bump is guaranteed to be firm. Cancelling an order or quote in the speed bump will convert its TIF into IOC. CoD or triggers will also convert speed-bumped orders and quotes into IOCs. An order or quote subject to [self-match prevention](/starbase/smp) that leaves the speed bump will have the `CANCEL_MAKER` behaviour, even if `CANCEL_TAKER` is configured.

  ### Rate Limits

  The Starbase rate limit framework has been finalised. See the [rate limits article](/starbase/rate-limits) for a full explanation of the mechanics. Two important points:

  * Members receiving this announcement will likely receive a **Member Override**. Do not assume the default values in the article apply to you — treat them as illustrative examples. Please reach out to your account manager to confirm your production rate limits as of July 20th.
  * Rate limits are applied **per member, per gateway**. As each instrument is available through two gateways, not utilising both means not utilising your full rate limit allocation.

  ### Spot

  Deribit's spot order books will not be available on Starbase. Shortly after go-live, spot orders will be routed to Coinbase Exchange, located in the US. Until that migration, spot order books will remain available only via the current WebSocket and FIX APIs. A small subset of order books not available on Coinbase — such as BUIDL, USYC and USDE — will remain on Deribit's legacy matching engine indefinitely.

  ### Redundant Cross-Connect

  We strongly recommend maintaining a primary and a secondary circuit. During switch maintenance or cable-length validations, we assume clients have redundant connectivity in place so that trading can continue uninterrupted.

  Starbase is only available via hosted co-location, cross-connect or AWS PrivateLink. Downtime on a single circuit may require you to fall back to the WebSocket API. Please reach out to [colo-support@coinbase.com](mailto:colo-support@coinbase.com) or your technical account manager with any questions.
</Update>

<Update label="Starbase Release 06.05.2026 — v1.0">
  ## Starbase Release

  ### Key Dates & Access

  * **July 13th:** Member and API key creation will become available in the UI, along with four SBE Order Entry endpoints for connectivity testing: Logon, Logout, Heartbeat, and Test. Access to market data and FIX drop copy will also be granted on this date. Multicast market data feeds will begin propagating to client servers within LD4, AWS eu-west-2 and AWS ap-northeast-1 for all derivatives.
  * **July 20th (Go-Live):** Clients will receive full access to the SBE Order Entry gateway for all derivatives.

  ### Equalization

  Due to hardware shortages and delivery delays, equalization of all connections for trading on Starbase is expected before the end of August. The maximum possible latency difference between the fastest and slowest member is \<5 microseconds, depending on the length of the cross connects. Equalization will involve migrating existing cross connects; no new cross connects are necessary. Because Deribit's hosted co-location uses very short cables to the edge switch, hosted co-location is expected to be a few microseconds faster than cross connects during July and some parts of August.

  ### Stability

  Starbase's test environment has performed stably for two consecutive weeks and is well positioned to support technical integration.

  ### Introduction of ETH to Starbase's test environment

  Inverse and linear ETH products have been migrated from the legacy matching engine to Starbase on test.deribit.com. The following products are now matching on Starbase in the test environment:

  * Linear ETH options, futures and the perpetual (options and futures with a 10ms speed bump)
  * Inverse ETH options, futures and the perpetual (options and futures with a 10ms speed bump)
  * AVAX options, futures and perpetual (all with a 10ms speed bump)
  * PAXG perpetual

  All BTC products remain on the legacy matching engine.

  ### REST gateway

  A REST API with utility endpoints is now [available](/starbase/rest-authentication). Notable endpoints include:

  * **Platform-wide mass cancellation:** allows cancellation of all open orders across the platform.
  * **Subaccount lock:** enables you to completely lock Starbase APIs from accessing a specific subaccount. This endpoint also cancels all open orders and will be made available over the internet.

  ### Environment resets

  In the coming weeks, engineers may trigger resets of Starbase's test environment. These resets will cause only brief downtime and will not reset any credentials or configurations. However, they will disconnect open connections and wipe all open orders and related histories. Please reach out to your account manager to be notified in advance of any resets.

  ### Documentation updates

  Now that Starbase has stabilized, the SDK and PCAPs will be versioned with the `version` and `semanticVersion` from the XML messageSchema. The latest `version` and `semanticVersion` will appear on the specification pages.

  ## API Changes

  ### Market Data

  `Instrument` message has been renamed to `InstrumentDefinition` and redesigned:

  * New fields added: `indexId`, `underlying`, `quantityAsset`, `priceAsset`, `minOrderQuantity`
  * Removed fields: `symbol`, `baseCurrency`, `quoteCurrency`, `baseIncrement`, `creationTime`, `logicalExpiry`
  * Large tick size information is now represented as a repeating `largeTickSizes` group instead of flat fields
  * A new repeating `legs` group has been added to support combo instruments

  New `IndexDefinition` message added, providing `indexId` and `name` for each index.

  Message ID changes:

  * `TradingStatusUpdate` has been removed and replaced by `InstrumentStatusUpdate`
  * `InstrumentInfo` and `InstrumentRef` have been renumbered

  `sortOrderId` field added to `Buy Put` and `Sell Put` messages.

  `TradeSummary` message redesigned:

  * `impliedVolatility` field removed
  * `tradeCount` field added — indicates the number of `Trade` messages following the summary
  * `takerFlags` field renumbered

  ### Order Entry

  New `CancelReason` values:

  * `PORTFOLIO_LOCKED` — order cancelled because the portfolio is locked
  * `POST_ONLY` — post-only order would have crossed

  New `OrderRejectReason` values:

  * `PORTFOLIO_LOCKED` — order rejected because the portfolio is locked
  * `POSITION_LIMIT_EXCEEDED` — future or options position size limit exceeded
  * `ORDER_SIZE_LIMIT_EXCEEDED` — open order aggregate size limit exceeded

  New `MassQuoteRejectReason` value:

  * `PORTFOLIO_LOCKED` — mass quote rejected because the portfolio is locked
</Update>

<Update label="Announcement 17.04.2026">
  ## Announcement

  Thank you to everyone who has already started trading on the Starbase test environment — members have logged on and sent, amended, and cancelled orders, including mass quotes.

  ### Documentation and downloads

  Refreshed XMLs, PCAPs and SDKs can be found on the [Binary API Reference](/starbase/binary-api-reference) page. Updated documentation is available across the [Starbase](/starbase/overview) section.

  ### Multicast

  Nothing will change for the current production multicast feeds — they will continue as-is under all circumstances. To receive the new Starbase multicast feeds:

  1. **Deribit-hosted colo servers:** No changes needed. Send an IGMP join for the multicast feeds you want to consume.
  2. **Cross-connected clients:** PIM configuration with an RP is required. For configuration details, contact [colo-support@coinbase.com](mailto:colo-support@coinbase.com).
  3. **Third-party clients (Beeks, UltraFX, LiquidityConnect, AWS):** Setup is in progress. You will be notified when connectivity is verified and ready.

  Since only AVAX/USDC and PAXG/USDC instruments have been migrated, not every multicast channel has market data flowing yet. To test connectivity, use channel `224.0.12.234`, which includes all AVAX options. All channels are listed on the [Multicast Channels](/starbase/multicast-channels) page. A [table mapping underlyings to tiers](/starbase/underlying-tiers) is also available.

  For any questions or concerns, contact [colo-support@coinbase.com](mailto:colo-support@coinbase.com).
</Update>

<Update label="Announcement 08.04.2026">
  ## Announcement

  Starbase is now live on test.deribit.com. Starbase is Deribit's new matching engine, which unlocks throughput of more than 100k orders per second with submillisecond latencies, and will be the home of all of Coinbase's international derivatives. To learn more, see the [Starbase overview](/starbase/overview).

  ### Instruments on Starbase (test.deribit.com)

  The following instruments are currently handled by Starbase:

  * PAXG\_USDC-PERPETUAL
  * AVAX\_USDC-PERPETUAL
  * All AVAX\_USDC dated futures
  * All AVAX\_USDC options

  All other instruments operate on the legacy matching engine. Starbase is under active development, so improvements will be added to the test.deribit.com deployment often and without notice.

  ### Connecting

  1. Contact your Deribit account manager via Telegram or Slack with your test.deribit.com main account user ID. They will enable direct access for all underlying subaccounts.
  2. [Create a Starbase API key](/starbase/creating-api-key).
  3. Use the connectivity details below for order entry and market data.

  No changes are required for existing cross-connects or other direct connections. Full connectivity details are available on the [Gateway Connectivity](/starbase/gateway-connectivity) page.

  ### SDK and specifications

  The latest [SDK](https://statics.deribit.com/files/starbase-deribit-sdk.zip) is available for download. XML schemas for the SBE APIs are included with the SDK release.

  Starbase remains on track to go live on Deribit's production environment for all derivatives in the first half of July.
</Update>

<Update label="Announcement 11.03.2026">
  ## Announcement

  Starbase will replace some order books on test.deribit.com on **April 8th**. On that date:

  * Members can create API keys to authenticate against Starbase using the existing API key creation UI on test.deribit.com.
  * Members will receive an email with the IPs of the gateways and the usable ports.
  * Market data will be published on the [multicast channels](/starbase/multicast-channels).
  * That same email will include a list of instruments whose order books have been migrated to Starbase.
  * XML specs for the SBE APIs will be made available.

  [FIX Drop Copy specifications](/starbase/fix-drop-copy-api) are now available. A Python SDK (.whl) is also available to kickstart integration of the Starbase order entry and market data APIs.
</Update>

<Update label="Announcement 01.02.2026">
  ## Announcement

  A change in company strategy has led to changes in technology and timelines, driven by the decision to align with other Coinbase exchanges.

  ### What won't change

  All existing APIs will continue to work throughout the ME replacement. The physical location and network connectivity won't change, and the tradeable contracts will stay the same. Unless you care about performance, you won't notice a thing.

  ### Timelines

  * **Early April:** A test environment will be made available.
  * **Early June:** We will start rolling out direct access.
  * **August:** Every order book will have moved over and every direct access API will be available.

  ### Starbase specifications

  The new matching engine, Starbase, comes with a low-latency order entry API and multicast market data feed. The specifications are available [here](/starbase/overview). Other key information:

  * [Market model](/starbase/market-model)
  * [Account model](/starbase/account-model)
  * [Market Maker Protection](/starbase/mmp)
  * [Self-Match Prevention](/starbase/smp)
  * [Speed Bumps](/starbase/speed-bumps)
  * [Gateway connectivity model and limits](/starbase/gateway-connectivity)

  This is made available early to allow for feedback and to help with planning your integration.

  ### Coming soon

  * FIX Drop Copy specifications will be made available next month
  * A REST API with utility endpoints will be made available next month
  * XML specs of the SBE and FIX APIs will be available before the test environment is live
  * PCAPs of all APIs will be available before the test environment is live
  * Code examples will be available before the test environment is live

  Minor updates to the APIs can be expected as designs are adapted based on member feedback.
</Update>
