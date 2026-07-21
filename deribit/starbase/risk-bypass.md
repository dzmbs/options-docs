> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Risk Bypass

Starbase allows MMP orders and quotes to bypass the risk engine. Starbase can be assured that any single execution in the matching engine cannot lead to more than twice the Max Quote Quantity to be traded. A hold on initial margin is imposed on each Portfolio based on the Max Quote Quantity of each MMP Group. Together, this means, that the total immediate risk exposure of a portfolio is bounded by MMP and sufficient margin is already taken to cover this risk exposure. When processing orders and quotes, Starbase does not need to risk-check these in-flight and as such these orders and quotes go straight from the gateway to the matching engine, bypassing the risk module.

To explain further, please see the following sequence of events:

1. Alice has a Max Quote Quantity of 10 BTC and a Quantity Limit of 10 BTC
2. A margin hold is placed in Alice's account based on the Max Quote Quantity
3. Alice enters double-sided quotes for each BTC\_USD option order book or \~1600 orders
4. Bob sends an order that fills Alice for 9 BTC
5. Bob sends a second order that fills Alice for 10 BTC
6. Alice's MMP is triggered an atomically cancels all her orders
7. Starbase prevents Alice from re-entering the market for 1 second
8. Deribit's margin engine recalculates IM based on Alice's fills and communicates this to Starbase
9. After 1 second, Alice is free to re-enter the market

## Best-practice for low-latency order entry

Because the risk engine is bypassed for MMP-enabled orders and quotes, it is recommended that any latency-sensitive strategy utilized MMP and MMP groups for all order entry and quoting. Additionally, utilizing the MMP system reduces strain on Deribit's margin engine and Starbase's risk engine.
