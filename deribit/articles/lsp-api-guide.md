> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Liquidity Support Program (LSP) API Guide

> Deribit's Liquidity Support Program (LSP) transfers liquidated positions to designated participant accounts before falling back to auto-deleveraging (ADL).

The Liquidity Support Program (LSP) is Deribit's first line of defense for handling positions from liquidated accounts on linear (USDC-settled) perpetuals. Instead of immediately auto-deleveraging (ADL) counterparties, Deribit first attempts to transfer the liquidated position directly to one or more designated **LSP participant** accounts, at a small spread to the reference price. Only if no LSP participant has capacity does the position fall back to ADL, and from there to the standard liquidation engine.

<Note>
  This article is relevant to three different audiences:

  * **Any client whose position could be liquidated** — read [What happens when your position is liquidated](#what-happens-when-your-position-is-liquidated) to understand the order of operations and the notifications you'll receive.
  * **Any client holding a position on an ADL-eligible instrument** — read [What happens if you're an ADL counterparty](#what-happens-if-youre-an-adl-counterparty). If Deribit needs to auto-deleverage, your open position could absorb part of it even if you were never at risk of liquidation yourself.
  * **LSP participants** — accounts designated by Deribit to receive assigned positions — should read the full article, since it also covers configuration, capacity limits, and the reduce-only restriction that comes with participation.
</Note>

## Key Concepts

* **LSP participant** – A subaccount designated by Deribit to receive positions from liquidated accounts. Participation is arranged directly with Deribit; there is no public API to self-enroll.
* **Cooldown group** – Every LSP-eligible instrument is classified into one of 7 groups based on its underlying currency: crypto tiers `1`–`6`, or `rwa` for tokenized real-world-asset instruments (e.g. equities, commodities).
* **Group limit (`pct`)** – The maximum amount a participant can be assigned within a single cooldown group, expressed as a **percentage of the participant's own equity**.
* **Cooldown period** – A fixed time window (5 minutes by default) over which assignments to a group are accumulated against that group's limit — usage stays flat until the window closes, then resets to zero in one step (see [Understanding the Cooldown Period](#understanding-the-cooldown-period)).
* **Notional capacity factor** – A platform-wide cap on the total notional a participant can hold, expressed as a multiple of their own equity (2x by default), that further limits how much they can absorb, independent of the group limit. It does not change the account's own maximum leverage.
* **Transfer price** – The price at which an assignment or ADL move is executed: the reference price adjusted by a small spread.
* **Commission** – A small fee charged on the account being liquidated/deleveraged for the transferred amount.

<Tip>
  If you're not sure whether an account is an LSP participant, call [`private/get_lsp_participant_config`](/api-reference/lsp/private-get_lsp_participant_config) with that account's API key — it returns an error if the account has no LSP configuration.
</Tip>

## Which Instruments Are LSP/ADL-Eligible

LSP and ADL only apply to **linear (USDC-settled) perpetuals** — for example `BTC_USDC-PERPETUAL`. The following are **never** eligible:

* **Options** — handled entirely by other mechanisms.
* **Dated futures** — only perpetuals are in scope, even if linear.
* **Inverse (coin-margined) perpetuals** — for example `BTC-PERPETUAL` is *not* eligible; only the linear/USDC-settled version of an instrument is.

Within linear perpetuals, eligibility further depends on your margin model:

* **Standard Margin (SM) accounts**: every linear perpetual is eligible, except pre-IPO instruments (which go straight to ADL).
* **Portfolio Margin (PM) accounts**: a linear perpetual is eligible only if its currency pair has **no listed options** and the currency isn't pre-IPO — currency pairs with listed options are handled by PM's own risk mechanisms instead.

<Note>
  LSP evaluates a participant's assignment capacity against their **USDC portfolio equity**. Make sure your LSP participant account carries its risk capital in USDC.
</Note>

## Understanding Cooldown Groups

Every LSP-eligible instrument is classified into a cooldown group based on its base currency:

| Group   | Description                                                                                                                                                                                                         |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1`–`5` | Curated crypto tiers, roughly ordered by liquidity (e.g. tier `1` includes BTC and ETH).                                                                                                                            |
| `6`     | Catch-all tier for any other crypto base currency not listed in tiers `1`–`5`.                                                                                                                                      |
| `rwa`   | Real-world-asset instruments — any base currency whose underlying type is a commodity or equity (e.g. tokenized gold or tokenized stock perpetuals). New RWA listings are classified into this group automatically. |

<Note>
  Group membership is maintained by Deribit and may change over time as new instruments are listed or reclassified. Use [`private/get_lsp_usage`](/api-reference/lsp/private-get_lsp_usage) to see your current per-group usage rather than assuming a fixed instrument-to-group mapping.
</Note>

## Understanding Group Limits

Each cooldown group has a limit, expressed as a **percentage of the participant's equity**, that caps how much notional can be assigned to that participant within a single group during one cooldown window:

* A platform-wide default limit applies to every group unless overridden.
* Deribit can set a **per-participant override** for any group, via the `group_limits` field on the participant's LSP configuration.
* Setting a group's limit to `0` disables assignments to that participant for that group entirely.
* The maximum limit for any group is capped at `notional_capacity_factor × 100` (see [Understanding the Notional Capacity Factor](#understanding-the-notional-capacity-factor)) — a higher percentage would never bind, since the notional capacity factor would already prevent it.

For example, a participant with `equity = $1,000,000` and a tier `1` limit of `15%` can be assigned up to `$150,000` notional in tier `1` instruments within a single cooldown window.

## Understanding the Cooldown Period

Assignments are tracked in a **fixed time window** (5 minutes by default, platform-configurable) — not a smoothly-decaying rolling window. The mechanics:

* The first assignment to a group opens a new window, anchored at that assignment's timestamp.
* Every subsequent assignment within `cooldown_period` of that anchor is added to the same window — `used` accumulates, but the window's start does **not** move.
* `used` does **not** decrease as individual assignments individually "age out". It stays flat at its accumulated total for the entire window.
* Once an assignment arrives more than `cooldown_period` after the window's anchor, the **entire window resets at once**: `used` drops to `0`, and that assignment opens a brand new window.

In practice this means: if you're near a group's limit 4 minutes into a 5-minute window, waiting 1 more minute doesn't free up any capacity — you need to wait until the full window (5 minutes from the *first* assignment in it) elapses, at which point all of that window's usage clears in one step.

[`private/get_lsp_usage`](/api-reference/lsp/private-get_lsp_usage) and [`private/get_lsp_participants_usage`](/api-reference/lsp/private-get_lsp_participants_usage) report the window directly via `cooldown_start` (the anchor — when the first assignment in the current window happened) and `cooldown_end` (`cooldown_start + cooldown_period_ms` — when the window closes and `used` resets to `0`) per group, alongside `pct` and `used` — see [Checking your current usage](#checking-your-current-usage).

If a participant's group usage reaches its limit, that participant is skipped for further assignments to that group until the current window closes.

## Understanding the Notional Capacity Factor

Independent of group limits, a **notional capacity factor** (2x by default) further constrains how much a participant can absorb. It caps the participant's total notional at a multiple of their equity; it is not a change to the account's own maximum leverage:

```
remaining_capacity = min(
  notional_capacity_factor * equity - current_notional,  # notional capacity headroom
  group_limit_pct / 100 * equity - group_used  # group allowance remaining
)
```

<Warning>
  The API does not return this computed `remaining_capacity` value directly. [`private/get_lsp_usage`](/api-reference/lsp/private-get_lsp_usage) and [`private/get_lsp_participants_usage`](/api-reference/lsp/private-get_lsp_participants_usage) only report `pct`, `used`, and the cooldown window's timing per group. To estimate your own remaining capacity you'll need to combine `pct`/`used` with your account equity from `private/get_account_summary` — and even then, your true remaining capacity may be lower if you are already leveraged elsewhere in your portfolio, since the notional-capacity headroom term above is not exposed on any endpoint.
</Warning>

If a participant has no remaining capacity in the relevant group (whether due to the group limit or the notional capacity factor), they are simply excluded from that assignment — there is no rejection notification for this case.

## Transfer Pricing

When a position is assigned to a participant (LSP) or auto-deleveraged (ADL), the trade executes at a **transfer price**: the instrument's reference price, adjusted against the liquidated/deleveraged position by a small spread (i.e. in the receiving side's favor) — a short position transfers above the reference price, a long position transfers below it. This mirrors how liquidation penalties work generally: the cost of the spread falls on the account being liquidated or deleveraged. The spread applied to LSP transfers is configured separately from the spread applied to ADL transfers, though both currently default to the same small value.

A small **commission** is also charged on the account being liquidated/deleveraged, proportional to the amount actually transferred. For ADL specifically, a single run can close part of a position against the account's own subaccounts (at the position's average price) and part against external counterparties (at the ADL transfer price) — you may see both in your notifications and transaction log for one liquidation event. Commission is charged on both stages alike, with each receiving account's share proportional to the position it absorbed. If an assignment or ADL transfer is only partially filled, the commission is charged pro-rata to the amount moved.

Both the transfer amount and the commission appear in `private/get_transaction_log` — see [Transaction Log Entries](#transaction-log-entries) below.

## Becoming an LSP Participant

There is no public API to opt an account into the LSP program — participation is arranged directly with Deribit. Once an account is configured as an LSP participant:

<Warning>
  The account is **automatically locked to reduce-only trading** platform-side. This is not automatically released when the participant is removed from the program — an admin must clear it manually. Plan your position management around this: an LSP participant account cannot open new positions on its own initiative, only receive assignments and reduce/close them.
</Warning>

## Monitoring Your LSP Participation

Four private methods let you inspect your own LSP participation and, if you're the main account, your participants' as well.

### Checking your configuration

[`private/get_lsp_participant_config`](/api-reference/lsp/private-get_lsp_participant_config) returns the calling account's LSP configuration:

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "private/get_lsp_participant_config",
  "params": {}
}
```

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "config": {
      "enabled": true,
      "group_limits": {
        "1": 15.0,
        "6": 0.0
      }
    }
  }
}
```

Groups absent from `group_limits` inherit the platform-wide default for that group. In this example, the participant has an overridden `15%` limit for tier `1` and is fully opted out of tier `6` (`0%`), with every other group left at the default.

### Listing participants under your main account

If you manage multiple LSP participant subaccounts, [`private/get_lsp_participants`](/api-reference/lsp/private-get_lsp_participants) — called with the main account's API key — lists them all:

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "private/get_lsp_participants",
  "params": { "detailed": false }
}
```

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "participants": [
      { "user_id": 172345, "enabled": true },
      { "user_id": 172346, "enabled": false }
    ]
  }
}
```

Pass `"detailed": true` to include each participant's full `config` alongside `user_id` and `enabled`.

### Checking your current usage

[`private/get_lsp_usage`](/api-reference/lsp/private-get_lsp_usage) returns the calling participant's usage against each cooldown group within the current fixed window, including the window's timing:

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "cooldown_period_ms": 300000,
    "groups": {
      "1": { "pct": 15.0, "used": 250000.0, "cooldown_start": 1750000100000, "cooldown_end": 1750000400000 },
      "2": { "pct": 10.0, "used": 0.0, "cooldown_start": null, "cooldown_end": null },
      "rwa": { "pct": 10.0, "used": 0.0, "cooldown_start": null, "cooldown_end": null }
    }
  }
}
```

`cooldown_start` is the timestamp of the first assignment in the group's current fixed window; `cooldown_end` (`cooldown_start + cooldown_period_ms`) is when that window closes and `used` resets to `0` in one step. Both are `null` when the group has no tracked usage.

[`private/get_lsp_participants_usage`](/api-reference/lsp/private-get_lsp_participants_usage) returns the same breakdown for every participant under your main account (optionally filtered to one participant via `user_id`).

## What Happens When Your Position Is Liquidated

If your account breaches its margin requirements on an LSP/ADL-eligible instrument, Deribit attempts the following, in order, for that position:

1. **LSP** — if enabled and the instrument is LSP-eligible for your margin model, Deribit looks for LSP participants with spare capacity and transfers the position to one or more of them.
2. **ADL** — if no LSP participant has capacity (or the instrument isn't LSP-eligible, e.g. pre-IPO under SM), the position is auto-deleveraged against a counterparty instead.
3. **Standard liquidation** — if neither route is available, the position is handed off to the standard, order-book-based liquidation engine.

You'll receive real-time updates on the `user.liquidation` channel throughout this process:

```
private/subscribe
{ "channels": ["user.liquidation"] }
```

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "user.liquidation",
    "data": {
      "state": "lsp_transfer",
      "user_id": 7,
      "instrument_name": "BTC_USDC-PERPETUAL",
      "direction": "sell",
      "amount": 5000,
      "price": 63481.75,
      "currency": "usdc",
      "commission": 1.25,
      "timestamp": 1750000400000
    }
  }
}
```

The `state` field tells you which stage of the process this event represents:

| `state`                                                             | Meaning                                                                                       |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `liquidation_started` / `liquidation_completed`                     | The standard, order-book-based liquidation process has started or completed for this account. |
| `close_out_liquidation_started` / `close_out_liquidation_completed` | The LSP/ADL close-out process has started or completed for this account.                      |
| `lsp_transfer`                                                      | A position was transferred off your account to an LSP participant.                            |
| `adl_transfer`                                                      | A position was auto-deleveraged off your account.                                             |

<Note>
  You can receive **both** the `liquidation_*` pair and the `close_out_liquidation_*` pair for the same episode — for example, if LSP/ADL close-out only partially resolves the breach and the remainder is handed off to standard liquidation. Each pair is independent and tied to its own mechanism's lifecycle.
</Note>

If your account is an isolated-margin subaccount, affected events include `"isolated": true`, and the same events are additionally delivered to your main account on `user.isolated.liquidation`.

The assigned/deleveraged amount and the commission charged will also show up in your transaction log — see below.

## What Happens If You're an ADL Counterparty

Auto-deleveraging works by matching a deleveraged position against a counterparty's open position on the same instrument — that counterparty doesn't need to be at risk of liquidation themselves; they're simply selected because their position is on the other side of the trade. If your account absorbs part of an ADL'd position, you'll receive an `adl_transfer_received` event on your own `user.liquidation` channel:

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "user.liquidation",
    "data": {
      "state": "adl_transfer_received",
      "user_id": 42,
      "instrument_name": "BTC_USDC-PERPETUAL",
      "direction": "buy",
      "amount": 4000,
      "price": 63481.75,
      "currency": "usdc",
      "commission": 0.2,
      "timestamp": 1750000400000
    }
  }
}
```

`commission` here is your share of the deleveraged account's commission for this transfer, proportional to the position your account absorbed. Intra-account moves — for example a position absorbed by one of your own subaccounts — are commissioned the same way.

## What Happens When You Receive an Assignment

As an LSP participant, subscribe to the `user.lsp` channel to be notified about assignment attempts and configuration changes:

```
private/subscribe
{ "channels": ["user.lsp"] }
```

```json theme={null}
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "user.lsp",
    "data": {
      "type": "transfer",
      "instrument_name": "BTC_USDC-PERPETUAL",
      "direction": "sell",
      "amount": 5000,
      "price": 63481.75,
      "currency": "usdc",
      "success": true,
      "timestamp": 1750000400000
    }
  }
}
```

The `type` field distinguishes four kinds of events on this channel:

| `type`                  | Meaning                                                                                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `transfer`              | An assignment attempt to you completed — check `success` to see whether it succeeded or failed. On failure, `error_reason` explains why and the amount was redistributed to other participants (or fell through to ADL). |
| `enabled`               | Your LSP configuration transitioned from disabled to enabled.                                                                                                                                                            |
| `disabled`              | Your LSP configuration transitioned from enabled to disabled — check `automatic` to see whether this was a manual change/removal or an automatic disable after repeated transfer failures.                               |
| `configuration_changed` | Your effective configuration changed — from your own edit, or from a platform-wide default change that affects you. Carries the full resolved `configuration` (`enabled` + every group's effective limit).               |

A failed `transfer` includes a machine-readable `error_reason`: `platform_locked`, `lock_count_exceeded`, `timeout`, `temporarily_unavailable`, `not_enough_funds`, or `internal_error`. There is no `usd_value` field, and there is no commission field on this channel — participants don't pay LSP commission (only the liquidated account does, see [Transfer Pricing](#transfer-pricing)).

<Note>
  An assignment immediately opens or adds to a position in your account at the transfer price, consuming margin exactly like a normal trade would. Because your account is reduce-only, you cannot open an opposing hedge directly on it — plan your risk management (e.g. hedging via another account) accordingly.
</Note>

## Auto-Disable

If your account repeatedly fails to accept assignments within a short window (for example, due to insufficient margin), Deribit automatically disables your LSP participation to avoid repeated failed attempts. You'll receive a `disabled` event on `user.lsp` with `automatic: true`:

```json theme={null}
{
  "type": "disabled",
  "automatic": true,
  "failure_count": 5,
  "window_minutes": 10,
  "timestamp": 1750000500000
}
```

A manual disable (or participant removal) emits the same `disabled` type with `automatic: false` and no `failure_count`/`window_minutes`.

<Warning>
  Auto-disable turns off future assignments (`enabled: false`, reflected in a following `configuration_changed` event) but does **not** release the reduce-only lock on your account. Contact Deribit to re-enable participation once the underlying issue is resolved.
</Warning>

## Transaction Log Entries

Both sides of a transfer appear in `private/get_transaction_log`:

* `"type": "LSP transfer"` / `"type": "ADL transfer"` — the position move itself, with `"role": "source"` on the liquidated/deleveraged account's entry and `"role": "destination"` on the receiving account's entry (the LSP participant, or the ADL counterparty).
* `"type": "LSP commission"` / `"type": "ADL commission"` — the commission charged on the liquidated/deleveraged account for the transferred amount.

## Best Practices

* **If you're a regular trader**: subscribe to `user.liquidation` so you're notified immediately if your position starts moving through the liquidation process, regardless of which mechanism (LSP, ADL, or standard liquidation) ultimately handles it — and so you're notified if you absorb part of someone else's ADL as a counterparty.
* **If you're an LSP participant**: monitor `user.lsp` for `transfer` events (checking `success`), and poll [`private/get_lsp_usage`](/api-reference/lsp/private-get_lsp_usage) periodically to track how close you are to your per-group limits using `pct`, `used`, and `cooldown_end` — remember that none of this includes the notional-capacity headroom, so keep spare margin available.
* **If you're an LSP participant**: remember your account is reduce-only. Size your available equity and group limits around the assignments you're willing to receive, since you cannot proactively open positions to manage risk on that account.
* Always check `enabled` (via `configuration_changed`, or [`private/get_lsp_participant_config`](/api-reference/lsp/private-get_lsp_participant_config)) after any auto `disabled` event — repeated failures require manual re-enablement by Deribit, not just fixing the underlying cause.


## Related topics

- [user.lsp ](/subscriptions/user/userlsp.md)
- [private/get_lsp_participants](/api-reference/lsp/private-get_lsp_participants.md)
- [private/get_lsp_participant_config](/api-reference/lsp/private-get_lsp_participant_config.md)
- [private/get_lsp_participants_usage](/api-reference/lsp/private-get_lsp_participants_usage.md)
- [private/get_lsp_usage](/api-reference/lsp/private-get_lsp_usage.md)
