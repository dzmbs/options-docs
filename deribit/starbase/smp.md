> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Self Match Prevention (SMP)

> Self Match Prevention (SMP) functionality in Starbase API for preventing orders from matching with each other.

## Overview

Self Match Prevention (SMP) is a mechanism that prevents orders from matching with each other when they originate from the same member AND share the same SMP token. SMP helps prevent accidental self-trading and allows for more granular control over order matching behavior.

SMP uses three components to control order matching:

| Component     | Description                                                       | Required                                                                                                                                                    | Scope        |
| ------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **SMP Mode**  | Determines which order is cancelled when a self-match is detected | Per order (default configured via the WebSocket API [`private/set_self_trading_config`](/api-reference/account-management/private-set_self_trading_config)) | Order-level  |
| **SMP Token** | Prevents matching between orders with the same token              | Mandatory (can be set to null/0)                                                                                                                            | Order-level  |
| **Member ID** | Scopes SMP to a specific member                                   | SMP cannot trigger between Members                                                                                                                          | Member-level |

<Tabs>
  <Tab title="SMP Mode">
    SMP mode determines which order is cancelled when a self-match is detected:

    | Mode              | Behavior                                |
    | ----------------- | --------------------------------------- |
    | **CANCEL\_MAKER** | The resting (maker) order is cancelled  |
    | **CANCEL\_TAKER** | The incoming (taker) order is cancelled |

    The SMP mode should be specified for each order. A default SMP mode can be configured via the WebSocket API [`private/set_self_trading_config`](/api-reference/account-management/private-set_self_trading_config) method, and users can change their default setting.

    <Warning>
      **Speed-bumped orders always use CANCEL\_MAKER on the SBE gateway.** When a taker order submitted via the SBE gateway is speed-bumped, the SMP mode is overridden to `CANCEL_MAKER` regardless of the value in the request. This is consistent with standard market practice for speed-bumped orders.

      Orders submitted via the WebSocket API may use `CANCEL_TAKER` regardless of speed-bump state.
    </Warning>

    <Warning>
      **Speed-bumped orders always use CANCEL\_MAKER on the SBE gateway.** When a taker order submitted via the SBE gateway is speed-bumped, the SMP mode is overridden to `CANCEL_MAKER` regardless of the value in the request. This is consistent with standard market practice for speed-bumped orders.

      Orders submitted via the WebSocket API may use `CANCEL_TAKER` regardless of speed-bump state.
    </Warning>

    <Note>
      **SMP Mode Selection**: When a self-match is detected, the SMP mode from the **aggressing order** (the incoming order) will be used to determine which order is cancelled.
    </Note>
  </Tab>

  <Tab title="SMP Token">
    The SMP token is a mandatory field in order messages that prevents matching between orders with the same token within the same Member. The field must always be present, but can be set to null (0) to allow self-matching.

    ### Matching Scenarios

    Matching is **prevented** only when **both** of the following conditions are met:

    * The same member ID (or both orders lack a member ID)
    * The same SMP token (non-null)

    | Scenario                      | Member    | SMP Token       | Matching Behavior                   |
    | ----------------------------- | --------- | --------------- | ----------------------------------- |
    | Same member, same token       | Same      | Same (non-null) | **Prevented**                       |
    | Same member, different tokens | Same      | Different       | **Allowed**                         |
    | Same member, null token       | Same      | Null            | **Allowed** (self-matching allowed) |
    | Different members             | Different | Same (non-null) | **Allowed**                         |
    | Different members             | Different | Different       | **Allowed**                         |

    **Key Points:**

    * SMP token is a mandatory field that must be specified on each order
    * Setting SMP token to null (0) allows self-matching
    * Orders with the same SMP token (non-null) within the same Member will not match
    * Two orders with the same SMP token from different Members can match
  </Tab>

  <Tab title="Member">
    **Self-match prevention is scoped to a Member** (a group of portfolios representing a trading participant). Two orders with the same SMP token within the same Member cannot match, but two orders with the same SMP token from different Members can match.
  </Tab>
</Tabs>

### Order from different systems

Orders originating from the Websocket API, User Interface or other non-Starbase origin will have the SMP Token set based on the table below. To avoid matching with these orders when utilizing Starbase APIs, the same SMP Tokens should be used.

| Setting                                              | SMP Token Value                                |
| ---------------------------------------------------- | ---------------------------------------------- |
| Self-match prevention restricted to subaccount       | `sub-account id` (equal to Deribit's User ID)  |
| Self-match prevention enabled across all subaccounts | `main-account id` (equal to Deribit's User ID) |
| Self-matching allowed                                | `null` (empty)                                 |

## API Usage

### Order Entry Messages

SMP fields are mandatory and must be specified in the following order entry messages:

| Message                                                          | SMP Token Field | Field Number | Description                                                                                                                      |
| ---------------------------------------------------------------- | --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| [`NewOrderRequest`](/starbase/placing-new-order#neworderrequest) | `SMPToken`      | 7            | This order cannot match with any other orders within the same portfolio with the same token. Set to null to allow self-matching. |
| [`MassQuoteRequest`](/starbase/mass-quotes#massquoterequest)     | `SMPToken`      | 4            | This order cannot match with any other orders within the same portfolio with the same token. Set to null to allow self-matching. |

### SMP Cancellation Indicators

When an order is cancelled due to self-match prevention, it will be indicated in the response messages:

| Message                                                             | Field                        | Value | Description           |
| ------------------------------------------------------------------- | ---------------------------- | ----- | --------------------- |
| [`NewOrderResponse`](/starbase/placing-new-order#neworderresponse)  | `cancelReason` (field 11)    | `1`   | `selfMatchPrevention` |
| [`AmendOrderResponse`](/starbase/amending-order#amendorderresponse) | `cancelReason` (field 12)    | `1`   | `selfMatchPrevention` |
| [`MassQuoteResponse`](/starbase/mass-quotes#massquoteresponse)      | `buyQuoteStatus` (field 18)  | `7`   | `CanceledBySelfMatch` |
| [`MassQuoteResponse`](/starbase/mass-quotes#massquoteresponse)      | `sellQuoteStatus` (field 19) | `7`   | `CanceledBySelfMatch` |
