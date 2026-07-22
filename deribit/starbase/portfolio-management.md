> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Portfolio Management

> Portfolio-scoped controls in Starbase — mass cancellation, direct-access order entry, and lock or unlock endpoints for risk operations workflows.

The Starbase REST API exposes a set of portfolio-scoped management operations. All endpoints require authentication; the authenticated session determines which portfolio is acted upon.

## Mass Cancel

Mass cancel removes every open order and quote belonging to the authenticated portfolio in a single call. Unlike the binary [Mass Cancel](/starbase/mass-cancel) message, which targets orders by instrument or side, the REST endpoint applies unconditionally — no filters are accepted.

The typical use case is risk reduction: a single call clears the entire book across all instruments and both sides. The endpoint returns the total number of orders cancelled across all matching engine shards.

<Info>
  Mass cancel via REST is always available and cannot be disabled by admin configuration.
</Info>

→ [`GET /api/v2/private/cancel_all`](/api/v2/private/cancel_all)

## Portfolio Lock State

The portfolio lock controls whether `DIRECT_ACCESS` (SBE binary) order entry is accepted. The lock is a portfolio-level toggle, independent of individual sessions or gateway connections.

### Locking

Locking a portfolio has two immediate effects:

1. All open `DIRECT_ACCESS` orders and quotes for the portfolio are cancelled.
2. Any subsequent `DIRECT_ACCESS` order or quote submission is rejected until the portfolio is unlocked.

REST-submitted orders are not subject to the lock — only binary `DIRECT_ACCESS` order flow is gated.

→ [`GET /api/v2/private/lock_portfolio`](/api/v2/private/lock_portfolio)

### Unlocking

Unlocking restores normal acceptance of `DIRECT_ACCESS` order entry. Orders cancelled by the preceding lock are not reinstated; clients must resubmit any desired positions.

→ [`GET /api/v2/private/unlock_portfolio`](/api/v2/private/unlock_portfolio)

<Warning>
  After a lock, cancelled orders are gone permanently. Unlocking the portfolio does **not** restore them.
</Warning>

## Relationship to Other Risk Controls

Portfolio management complements but does not replace other Starbase risk features:

| Control                                                               | Scope                         | Trigger                               |
| --------------------------------------------------------------------- | ----------------------------- | ------------------------------------- |
| [Cancel on Disconnect](/starbase/cancel-on-disconnect)                | Session                       | TCP disconnection or missed heartbeat |
| [Mass Cancel (binary)](/starbase/mass-cancel)                         | Portfolio, filtered           | Explicit client request via SBE       |
| Mass Cancel (REST)                                                    | Portfolio, unfiltered         | Explicit client request via REST      |
| [Portfolio lock](/starbase/portfolio-management#portfolio-lock-state) | Portfolio                     | Explicit client request via REST      |
| [MMP](/starbase/mmp)                                                  | Underlying, MMP-tagged orders | Exposure limit breach                 |


## Related topics

- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [private/simulate_portfolio](/api-reference/account-management/private-simulate_portfolio.md)
- [Order Management](/articles/order-management-best-practices.md)
- [Lock Portfolio](/api-reference/portfolio-management/lock-portfolio.md)
- [Unlock Portfolio](/api-reference/portfolio-management/unlock-portfolio.md)
