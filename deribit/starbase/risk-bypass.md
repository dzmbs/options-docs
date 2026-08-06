> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Risk Bypass

> How privileged Starbase sessions can bypass pre-trade risk checks for certain low-latency workflows — configuration, scope, and eligibility requirements.

Starbase allows MMP orders and quotes to bypass the risk engine. Starbase can be assured that any single execution in the matching engine cannot lead to more than twice the Max Quote Quantity to be traded. A hold on initial margin is imposed on each Portfolio based on the Max Quote Quantity of each MMP Group. Together, this means, that the total immediate risk exposure of a portfolio is bounded by MMP and sufficient margin is already taken to cover this risk exposure. When processing orders and quotes, Starbase does not need to risk-check these in-flight and as such these orders and quotes go straight from the gateway to the matching engine, bypassing the risk module.

To explain further, please see the following sequence of events:

1. Alice has a Max Quote Quantity of 10 BTC and a Quantity Limit of 10 BTC
2. A margin hold is placed in Alice's account based on the Max Quote Quantity
3. Alice enters double-sided quotes for each BTC\_USD option order book or \~1600 orders
4. Bob sends an order that fills Alice for 9 BTC
5. Bob sends a second order that fills Alice for 10 BTC
6. Alice's MMP is triggered and atomically cancels all her orders
7. Starbase prevents Alice from re-entering the market for 1 second
8. Deribit's margin engine recalculates IM based on Alice's fills and communicates this to Starbase
9. After 1 second, Alice is free to re-enter the market

## Recommended: MMP risk bypass for order entry

Utilizing the MMP risk bypass is the **lowest-latency method for market access** in Starbase. MMP-enabled flow goes straight from the gateway to the matching engine, so no order-entry path that passes through the risk module can be faster.

This works for both orders and mass quotes:

* **Orders** — set the `MMP` flag (field 10, bit 4) on [`NewOrderRequest`](/starbase/placing-new-order#neworderrequest-100) to tag the order for the default MMP group
* **Mass quotes** — MMP is always enforced for quotes via their MMP group, so mass quoting uses the bypass by default

The bypass applies to any MMP-tagged order, whether the order makes or takes — it is not restricted to resting, liquidity-providing flow. An MMP-tagged order that aggresses skips the risk module exactly like a quote does. This is independent of the [speed bump](/starbase/speed-bumps): on speed-bumped instruments, an aggressing order is still made pending for the speed bump duration, regardless of MMP tagging.

Most clients integrating with Starbase should prefer this path for all order entry and quoting:

* **Lowest latency** — the risk engine is not on the critical path for MMP-enabled flow
* **Reduced system load** — bypassing the risk module reduces strain on Starbase's risk engine and Deribit's margin engine
* **Isolation from pre-trade risk testing** — while pre-trade risk checks are being tested and rolled out, MMP-enabled flow bypasses the risk module entirely, so order acceptance and latency behavior on this path are unaffected by that work


## Related topics

- [Placing a New Order](/starbase/placing-new-order.md)
- [Starbase Connectivity Quickstart](/starbase/quickstart.md)
- [Mass Quotes](/starbase/mass-quotes.md)
- [Starbase API Overview](/starbase/overview.md)
- [Starbase FIX Drop Copy API](/starbase/fix-drop-copy-api.md)
