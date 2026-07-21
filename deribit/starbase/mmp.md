> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Market Maker Protection (MMP)

> Market Maker Protection (MMP) in Starbase Binary API including configuration, reset operations, and MMP-tagged orders.

## Overview

Market Maker Protection (MMP) helps reduce exposure risk by automatically pausing quoting activity when certain limits are reached. MMP monitors trading activity and automatically cancels all MMP-tagged orders when exposure limits are breached, then freezes quoting for a configured duration.

<Info>
  **For comprehensive MMP configuration details**, see:

  * [**Market Maker Protection (MMP) API Configuration**](/articles/market-maker-protection) - Complete guide to MMP configuration, parameters, and management via JSON-RPC API
  * [**Deribit MMP (Knowledge Base)**](https://support.deribit.com/hc/en-us/articles/25944738804509-Deribit-MMP) - Detailed explanation of MMP concepts, configuration, and best practices
</Info>

## MMP in Starbase Binary API

The Starbase Binary API provides the following MMP capabilities:

1. **MMP-tagged Orders** – Orders can be tagged with MMP flags to participate in MMP protection
2. **Mass Quoting** - Quotes placed by Mass Quoting have MMP enforced
3. **MMP Trigger Events** – Receive real-time notifications when MMP limits are breached via `MassQuoteMmpTriggered` and `OrdersMmpTriggered` events
4. **Resetting MMP** – Manually resetting MMP limits after a freeze to resume quoting

## MMP-Tagged Orders

Orders placed via the Starbase Binary API can be tagged with MMP flags to participate in Market Maker Protection. When MMP limits are breached, all orders within the same underlying with the MMP flag enabled are automatically canceled.

For details on how to enable MMP for individual orders, refer to the order entry documentation:

* [Placing a New Order](/starbase/placing-new-order) - Includes MMP flag configuration

### Quotes and MMP

MMP is **required** for quotes. For quotes, MMP groups can be defined per underlying. MMP groups are entirely independent from each other, allowing you to configure different risk limits for different underlyings.

For more information on quotes:

* [Mass Quotes Specifications](/articles/mass-quotes-specifications) - Complete guide to mass quotes functionality
* [Mass Quotes SBE Messages](/starbase/mass-quotes) - Binary API messages for placing and managing quotes (MassQuoteRequest, MassQuoteResponse, MassQuoteReject)

<Note>
  **MMP Trigger Messaging**: Cancels resulting from MMP triggers might not be sent in the same message as the fill that caused the MMP trigger. The fact that MMP is triggered will be indicated on the order/quote fill.
</Note>

<Note>
  **Speed-bumped orders**: When an MMP trigger cancels an order that is currently speed-bumped, the order is converted to IOC rather than removed immediately. It will attempt to fill when the speed bump expires; any unfilled remainder is then cancelled. See [Speed Bumps — Cancelling Pending Orders](/starbase/speed-bumps#cancelling-pending-orders) for the full message flow.
</Note>

<Note>
  **Speed-bumped orders**: When an MMP trigger cancels an order that is currently speed-bumped, the order is converted to IOC rather than removed immediately. It will attempt to fill when the speed bump expires; any unfilled remainder is then cancelled. See [Speed Bumps — Cancelling Pending Orders](/starbase/speed-bumps#cancelling-pending-orders) for the full message flow.
</Note>

## MMP Group IDs in Starbase

Starbase requires MMP groups to be identified by their **integer ID** (`int64`), not by the string name shown in the GUI or used by the JSON-RPC API (e.g., `"default"`). To find the integer ID for a given MMP group, call [`private/get_mmp_config`](/api-reference/trading/private-get_mmp_config).

The `id` field in each entry is the value to supply as `mmpGroupId` in mass quote requests. Groups that have no `mmp_group` name in the response correspond to the orders MMP group (the default group).

```json theme={null}
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": [
    {
      "id": 144790485158858750,
      "max_quote_quantity": 5,
      "quantity_limit": 5,
      "delta_limit": 0.5,
      "vega_limit": 0.2,
      "frozen_time": 5,
      "index_name": "btc_usd",
      "interval": 2
    },
    {
      "id": 175935387007455230,
      "max_quote_quantity": 100,
      "quantity_limit": 100,
      "frozen_time": 1,
      "index_name": "btc_usd",
      "interval": 1,
      "mmp_group": "TestBtc"
    }
  ]
}
```

In this example:

* `144790485158858750` is the orders MMP group for `btc_usd` (no `mmp_group` name — this is the default)
* `175935387007455230` is the `"TestBtc"` mass quote MMP group for `btc_usd`

<Note>
  The WebSocket API still accepts string names when configuring MMP, and also supports integer IDs for Starbase compatibility. Starbase itself only accepts the integer form.
</Note>

## Resetting MMP

If your MMP protection has been triggered and quoting is frozen for a given index, you can resume quoting either automatically after the configured freeze time or manually via the Starbase Binary API.

<Info>
  If the configured `frozen_time` has expired, the system will automatically reset MMP and quoting resumes for that index
</Info>

<Note>
  The minimum `fozen_time` is 1 second. Unfreezing is not possible until 1 second after an MMP trigger. This is to allow the risk engine time to process the sequence of trades that caused the trigger.
</Note>

### Manual Reset Methods

You can manually reset MMP using any of the following methods:

1. **JSON-RPC API**: Call [`private/reset_mmp`](/api-reference/trading/private-reset_mmp) to reset MMP for a specific index or MMP group
2. **Reset Flags in Order Messages**: Use reset flags in order entry messages to unfreeze MMP while placing or amending orders:
   * [**NewOrderRequest**](/starbase/placing-new-order#neworderrequest) (Field 10, flag 5: `resetMmp`) - Unfreeze orders MMP group when placing a new order
   * [**AmendOrderRequest**](/starbase/amending-order#amendorderrequest) (Field 7, flag 5: `resetMmp`) - Unfreeze orders MMP group when amending an existing order
   * [**MassQuoteRequest**](/starbase/mass-quotes#massquoterequest) (Fields 14/15, flag 3: `resetMMP`) - If an MMP freeze is active, this flag will remove the freeze before processing the rest of the message. Keep in mind there is a mandatory `1` second freeze that can't be overruled

<Warning>
  **Mandatory Minimum Freeze Period**: There is a mandatory minimum `1` second freeze period that cannot be overruled by any reset method (including reset flags). This minimum freeze period allows Deribit to properly risk manage. When using reset flags in order messages, the MMP freeze is removed before processing the order/quote, but you must wait at least 1 second after the MMP trigger before quoting can resume.
</Warning>

### Reset Behavior

* If `frozen_time` is set to `0` (automatic reset disabled), you must use one of the manual reset methods to re-enable quoting
* You can perform a manual reset during the frozen period if you want to resume quoting early (after the minimum 1 second period)
* After reset, the previous MMP configuration remains unchanged (the limits, interval, etc. stay in effect)

## Monitoring MMP

You can monitor MMP status and configuration using multiple methods:

### JSON-RPC API

* [`private/get_mmp_config`](/api-reference/trading/private-get_mmp_config) - Returns all currently active MMP parameters for the selected index
* [`private/get_mmp_status`](/api-reference/trading/private-get_mmp_status) - Returns the live MMP state for the index, including whether MMP is triggered and remaining frozen time

### WebSocket Notifications

For real-time MMP trigger notifications, subscribe to the `user.mmp_trigger.{index_name}` channel via WebSocket.

### Binary API

To query MMP freeze status directly on the gateway connection, without a round trip to the JSON-RPC API, use the following message pairs.

#### GetMassQuoteMmpStatusRequest (155)

Request the current MMP freeze status of a mass quote MMP group. Answered with a `GetMassQuoteMmpStatusResponse` or a `GetMassQuoteMmpStatusReject`.

| Field | Name          | Type  | Length | Description             |
| ----- | ------------- | ----- | ------ | ----------------------- |
| 1     | correlationId | int64 | 8      | Client-assigned ID      |
| 2     | mmpGroupId    | int64 | 8      | Identifier of MMP group |

#### GetMassQuoteMmpStatusResponse (280)

| Field | Name            | Type  | Length | Description                                                                                |
| ----- | --------------- | ----- | ------ | ------------------------------------------------------------------------------------------ |
| 1     | timestamp       | int64 | 8      | Nanoseconds since epoch. Gateway send time                                                 |
| 2     | correlationId   | int64 | 8      | Client-assigned ID                                                                         |
| 3     | mmpGroupId      | int64 | 8      | Identifier of MMP group                                                                    |
| 4     | frozenUntilTime | int64 | 8      | Nanoseconds since epoch. Present only while the MMP group is frozen; omitted if not frozen |

#### GetMassQuoteMmpStatusReject (281)

| Field | Name          | Type  | Length | Description                                 |
| ----- | ------------- | ----- | ------ | ------------------------------------------- |
| 1     | timestamp     | int64 | 8      | Nanoseconds since epoch. Gateway send time  |
| 2     | correlationId | int64 | 8      | Client-assigned ID                          |
| 3     | reason        | int8  | 1      | Rejection reason code. See the table below. |

#### GetOrdersMmpStatusRequest (156)

Request the current MMP freeze status of the orders MMP group for a given underlying currency pair. Answered with a `GetOrdersMmpStatusResponse` or a `GetOrdersMmpStatusReject`.

| Field | Name          | Type  | Length | Description         |
| ----- | ------------- | ----- | ------ | ------------------- |
| 1     | correlationId | int64 | 8      | Client-assigned ID  |
| 2     | indexId       | int64 | 8      | Underlying index ID |

#### GetOrdersMmpStatusResponse (282)

| Field | Name            | Type  | Length | Description                                                                                       |
| ----- | --------------- | ----- | ------ | ------------------------------------------------------------------------------------------------- |
| 1     | timestamp       | int64 | 8      | Nanoseconds since epoch. Gateway send time                                                        |
| 2     | correlationId   | int64 | 8      | Client-assigned ID                                                                                |
| 3     | indexId         | int64 | 8      | Underlying index ID                                                                               |
| 4     | frozenUntilTime | int64 | 8      | Nanoseconds since epoch. Present only while the orders MMP group is frozen; omitted if not frozen |

#### GetOrdersMmpStatusReject (283)

| Field | Name          | Type  | Length | Description                                 |
| ----- | ------------- | ----- | ------ | ------------------------------------------- |
| 1     | timestamp     | int64 | 8      | Nanoseconds since epoch. Gateway send time  |
| 2     | correlationId | int64 | 8      | Client-assigned ID                          |
| 3     | reason        | int8  | 1      | Rejection reason code. See the table below. |

The table below lists all possible values of the `reason` field used by `GetMassQuoteMmpStatusReject` and `GetOrdersMmpStatusReject`.

| Value | Name                | Description |
| ----- | ------------------- | ----------- |
| `0`   | `SYSTEM_ERROR`      |             |
| `1`   | `INVALID_MMP_GROUP` |             |

## Binary API Trigger Events

When MMP limits are breached, the Starbase Binary API sends unsolicited events to notify you of the trigger and provide details about canceled orders.

* [**MassQuoteMmpTriggered (320)**](/starbase/unsolicited-events#massquotempptriggered-320): Event generated when a mass quote Market Maker Protection limit is triggered. This event is sent for MMP groups used in mass quotes.
* [**OrdersMmpTriggered (322)**](/starbase/unsolicited-events#ordersmpptriggered-322): Event generated when an orders Market Maker Protection limit is triggered. This event is sent for standard orders (not mass quotes) when MMP limits are breached at the index level.
* [**MassQuoteMmpUnfrozen (324)**](/starbase/unsolicited-events#massquotemmpunfrozen-324): Event generated when a mass quote MMP group is unfrozen, either via a reset request or because the `frozenUntil` timer elapsed.
* [**OrdersMmpUnfrozen (326)**](/starbase/unsolicited-events#ordersmmpunfrozen-326): Event generated when an orders MMP group is unfrozen, either via a reset request or because the `frozenUntil` timer elapsed.

<Note>
  **Multiple Messages**: If not all canceled order IDs fit in one message, multiple messages may be sent. Check the `flags` field to determine if more messages are coming (`0` = isLastMessage).
</Note>

## MMP Configuration

MMP configuration is managed through the JSON-RPC API. To configure MMP settings, use the [`private/set_mmp_config`](/api-reference/trading/private-set_mmp_config) method. This method allows you to set MMP parameters including quantity limits, delta limits, vega limits, interval, frozen time, and maximum quote quantity (MQQ).
