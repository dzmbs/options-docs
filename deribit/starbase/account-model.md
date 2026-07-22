> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Account Model

> How the Starbase account and subaccount hierarchy differs from the Deribit main platform for order entry, drop copy, and permission scoping.

| Concept       | Description                                                        | Mapping to Deribit                                   |
| ------------- | ------------------------------------------------------------------ | ---------------------------------------------------- |
| **Portfolio** | Container for positions, funds, and balances across all currencies | 1:1 with account (main- or sub-account)              |
| **Member**    | Group of portfolios representing a trading participant             | Can span multiple subaccounts under one main account |

<Note>
  Members can only be configured from a **main account**. Subaccounts cannot create or manage Members. Additionally, the Starbase section will only appear in your account panel once your account has been authorized by a Deribit admin.
</Note>

### Member limits

Rate limits are allocated **per Member** and are shared across all API keys, sessions, and portfolios within that Member. Having more sessions or more portfolios does not increase your rate limits.

See the table below for the Member/Portfolio setup for the three major account types.

| Use Case                      | Description                                                                                                                                                                                                                                                                                                                          |
| :---------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Directly onboarded client** | These clients are set up with **exactly one Member** and will not be granted additional Members. All portfolios/sub-accounts fall under this single Member.                                                                                                                                                                          |
| **Prime Broker clients**      | Clients of Prime Brokers can request their Prime Broker to set up their subaccounts as a single Member. This ensures that clients of a Prime Broker can trade completely independently of other clients of the same Prime Broker. Any new portfolios/sub-accounts will need to be added manually and by request of the Prime Broker. |
| **Pod-based trading firms**   | Trading firms with multiple trading pods that act independently can request each pod to be set up as a Member. This allows pods to trade completely independently from other pods. Any new portfolio/sub-account will not immediately be part of a Member grouping.                                                                  |

<Info>
  Members should reflect genuine business-level separation — for example, competing trading desks or independent prime broker end-clients. Multi-member setups are not allocated higher rate limits than single-member setups. An example of a justified multi-member setup is a Prime Broker with two distinct, independent market makers as end clients.
</Info>

### Members and margin mode

A Member is a grouping of portfolios and can contain a mix of margin modes — for example, one subaccount on Standard Margin (SM) alongside others on Segregated Portfolio Margin (S:PM) or Cross Portfolio Margin (X:PM). However, options positions are not supported on Standard Margin, and this restriction is enforced per portfolio regardless of where the order originates:

* **Existing positions**: A subaccount that already holds options positions while on Standard Margin cannot be added to a Member, even if other subaccounts being added to the same Member succeed.
* **New positions**: Once a Standard Margin subaccount is scoped to a Member, no new options positions can be opened on it — whether the order is submitted via Starbase (Direct Access) or via websocket API.

To trade options on a subaccount that belongs to a Member, switch that subaccount's margin mode to Segregated Portfolio Margin or Cross Portfolio Margin.


## Related topics

- [Starbase API Changelog](/changelogs/starbase.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [private/change_margin_model](/api-reference/account-management/private-change_margin_model.md)
- [Market Model](/starbase/market-model.md)
- [private/get_subaccounts](/api-reference/account-management/private-get_subaccounts.md)
