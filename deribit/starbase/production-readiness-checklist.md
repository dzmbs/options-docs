> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Production Readiness Checklist

> Readiness checklist for clients onboarding to Starbase SBE order entry: Member setup, API key scopes, MMP risk bypass, SBE XMLs, and logon testing.

<Note>
  The Starbase direct access (SBE order entry) gateways go live on **Tuesday, 11 August 2026**, immediately after the scheduled maintenance at **9:00 AM UTC**. The maintenance is followed by a longer cancel-only period, during which the order entry gateways are fully available.
</Note>

This checklist is for clients already onboarded to Starbase. Work through the steps below to make sure your transition to production order entry is smooth.

<Note>
  Read the [Connectivity Quickstart](/starbase/quickstart) first — it covers network access, key creation, and end-to-end validation. This checklist assumes that setup is done and only verifies the points most likely to block a smooth go-live.
</Note>

<Steps>
  <Step title="Confirm Your Member Setup">
    A Member groups the portfolios (accounts/subaccounts) that trade on Starbase. Members are managed at the **main-account level only** — subaccounts cannot create or manage Members.

    * Add every main-account or subaccount UID that needs Starbase access to your Member. Most clients can configure exactly **one Member**. Broker clients that require separate Members for independent end clients must contact <a href="mailto:support@deribit.com" style={{ whiteSpace: "nowrap" }}>[support@deribit.com](mailto:support@deribit.com)</a> to have multi-Member access enabled.
    * Verify the setup in the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel or programmatically with [`private/get_members`](/api-reference/account-management/private-get_members).

    <Warning>
      A subaccount that does not belong to an active Member cannot authenticate to Starbase — API key creation for it fails with a **"No active member"** error.
    </Warning>

    See [Account Model](/starbase/account-model) and [Creating a Starbase API Key](/starbase/creating-api-key) for details.
  </Step>

  <Step title="Check API Key Scopes for SBE Order Entry">
    Starbase API keys are separate from standard Deribit API keys — a standard key cannot authenticate to Starbase.

    * Create keys in the [Starbase section](https://www.deribit.com/account/BTC/starbase/api-keys) of the Account Panel while switched into the **subaccount UID** that will use the key.
    * The key needs the **SBE Order Entry** scope to submit, amend, and cancel orders. Add **FIX Drop Copy** and **REST** scopes if your integration uses those APIs.
    * Plan your key allocation: up to **8 Starbase API keys per subaccount**, one connection per gateway per key. Reconnecting the same key to the same gateway terminates the existing session.
  </Step>

  <Step title="Configure MMP and Use the Risk Bypass">
    The lowest-latency order entry path on Starbase is the [MMP risk bypass](/starbase/risk-bypass): MMP-tagged flow goes straight from the gateway to the matching engine, skipping the risk module. It also reduces load on Deribit's risk and margin engines and is unaffected by the ongoing pre-trade risk testing.

    * **Orders** — set the `MMP` flag (field 10, bit 4) on [`NewOrderRequest`](/starbase/placing-new-order#neworderrequest-100). The bypass applies to both making and taking flow.
    * **Mass quotes** — MMP is always enforced through the `mmpGroupId` referenced on every `MassQuoteRequest`, so mass quoting uses the bypass by default.
    * Configure your MMP limits (quantity, delta, vega, interval, frozen time, and Max Quote Quantity) with [`private/set_mmp_config`](/api-reference/trading/private-set_mmp_config) before go-live. Note the scoping difference: order MMP applies **per subaccount and base/quote pair**, while mass-quote MMP works through an explicit `mmpGroupId`.

    See [Market Maker Protection](/starbase/mmp) for configuration, reset, and monitoring details.
  </Step>

  <Step title="Update to the Latest SBE XMLs">
    Download the current integration resources and regenerate your SBE codecs (or update to the latest SDK):

    * [SBE order entry XML](/specifications/deribit-sbe-xmls/deribit-sbe-order-api.xml)
    * [SBE market data XML](/specifications/deribit-sbe-xmls/deribit-sbe-market-data-api.xml)
    * [Order entry SDK](/starbase/starbase-deribit-order-sdk-13.0.zip)
    * [Market data SDK](/starbase/starbase-deribit-md-sdk-1.0.zip)

    <Info>
      As of **[11 August 2026](/changelogs/starbase#starbase-release-11-08-2026)**, the latest schema versions are:

      * **Order entry** — schema `version` **14** (`semanticVersion` **1.5**)
      * **Market data** — schema `version` **1** (`semanticVersion` **1.0**)

      The `version` and `semanticVersion` attributes are at the top of each XML file — check them against your local copies.
    </Info>

    Note that reference data is published on the multicast market data feeds, and your integration should be comfortable consuming it from there:

    * `InstrumentDefinition` — full instrument definitions on the snapshot channels
    * `IndexInfo` (12) — index price per currency pair
    * `InstrumentInfo` (14) — `minSellPrice`, `maxBuyPrice`, and `markPrice` per instrument
    * `InstrumentRef` (15) — funding, settlement/delivery prices, and open interest per instrument

    See [Reference Data](/starbase/reference-data) for full message details.
  </Step>

  <Step title="Test Order Entry Logon and Heartbeats">
    The session-level endpoints (Logon, Logout, Heartbeat, and Test) are already enabled on the production gateways for connectivity testing. **If you have not tested order entry logon yet, do so as soon as possible.**

    1. Establish TCP connectivity to the gateway pair for each product group you trade — see [Gateway Connectivity](/starbase/gateway-connectivity).
    2. Send a `LogonRequest` and expect a `LogonResponse` — note the `heartbeatIntervalSeconds` value the server returns.
    3. Keep the session alive with `Heartbeat` messages at the expected interval, and use `TestRequest` to elicit a `Heartbeat` echoing your `correlationId`.
    4. Repeat on **both the A and B sides** of each required gateway pair.

    <Note>
      Do not treat a successful TCP connection as a pass — authentication and the heartbeat exchange must both work. See [Session Messages](/starbase/session-messages) for the full message flows.
    </Note>
  </Step>

  <Step title="Know Where to Find Fees, Open Orders, and Order History">
    Starbase order state is distributed differently from the standard Deribit APIs. Before go-live, make sure your reconciliation and reporting pull each data type from the right place:

    | Data              | Where to get it                                                                                                                                                                                                                                                                                                                   |
    | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Open orders**   | The originating SBE session, [FIX Drop Copy](/starbase/fix-drop-copy-api), or the Starbase REST `GET /api/v2/private/get_open_orders` snapshot (capped at 1 request per minute per portfolio — a recovery tool, not a live feed). Open Starbase orders do **not** appear in the web UI or the standard WebSocket/FIX order feeds. |
    | **Order history** | Standard [`private/get_order_history_*`](/api-reference/trading/private-get_order_history_by_currency) endpoints return only orders that reached the book or filled. Rejected and zero-fill orders cannot be retrieved retroactively — persist FIX Drop Copy Execution Reports as they arrive.                                    |
    | **Fees**          | Trades executed on Starbase appear on the standard private trade feeds, which include per-trade `fee` and `fee_currency` fields — for example [`private/get_user_trades_by_currency`](/api-reference/trading/private-get_user_trades_by_currency).                                                                                |

    <Tip>
      If you need to adjust your Member setup quickly around go-live, [`private/set_member`](/api-reference/account-management/private-set_member), [`private/delete_member`](/api-reference/account-management/private-delete_member), and [`private/get_members`](/api-reference/account-management/private-get_members) are available on the standard JSON-RPC API and in the Starbase tab of the Account Panel.
    </Tip>
  </Step>
</Steps>

## Questions?

If anything on this list is not working as expected:

* Send network and multicast issues to <a href="mailto:colo-support@coinbase.com" style={{ whiteSpace: "nowrap" }}>[colo-support@coinbase.com](mailto:colo-support@coinbase.com)</a>.
* Send protocol rejects and account-configuration questions to your Technical Account Manager or <a href="mailto:support@deribit.com" style={{ whiteSpace: "nowrap" }}>[support@deribit.com](mailto:support@deribit.com)</a>.

## Next steps

<CardGroup cols={2}>
  <Card title="Infrastructure & Best Practices" icon="server" href="/starbase/connectivity-best-practices">
    Deployment costs, gateway architecture, failover, and protocol selection.
  </Card>

  <Card title="Gateway Connectivity" icon="network-wired" href="/starbase/gateway-connectivity">
    Production and test addresses, ports, and gateway pairs.
  </Card>

  <Card title="Risk Bypass" icon="forward-fast" href="/starbase/risk-bypass">
    How MMP-tagged flow bypasses the risk module.
  </Card>

  <Card title="Starbase Changelog" icon="clock-rotate-left" href="/changelogs/starbase">
    Release notes and go-live announcements.
  </Card>
</CardGroup>


## Related topics

- [Starbase API Changelog](/changelogs/starbase.md)
- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Starbase API Overview](/starbase/overview.md)
- [Infrastructure, Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [REST Order Gateway Authentication](/starbase/rest-authentication.md)
