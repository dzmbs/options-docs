> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference Data

> Instrument metadata for the Starbase Binary API — InstrumentDefinition messages with contract terms, tick sizes, and product identifier fields.

## Reference data

<Info>
  **Combination Orders**: Combination orders are treated as orders on outright books and are not differentiated in any way. Their orderbook\_id links to a combination order book.
</Info>

<Note>
  **Multicast is the recommended source for full reference data.** The Starbase REST API exposes a subset of instrument fields and does not include all attributes available in the SBE `InstrumentDefinition` message — for example, `minOrderQuantity` is not available via REST. Use the multicast reference data feed to obtain complete instrument definitions.
</Note>

## Reference data sources

The Starbase and standard Deribit APIs expose overlapping, but not identical, instrument metadata:

| Source                                                                                 | Access                                                                | Use it for                                                                                                                        |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| SBE multicast `InstrumentDefinition`                                                   | Starbase private connectivity                                         | Authoritative Starbase order-entry units, minimum quantity, tick sizes, instrument type, status, and combo legs                   |
| [Standard `public/get_instruments`](/api-reference/market-data/public-get_instruments) | Standard public JSON-RPC API; Starbase network access is not required | Standard instrument metadata including `contract_size`, `index_id`, and `product_group`                                           |
| Starbase REST `get_instruments`                                                        | Starbase private connectivity                                         | `index_id`, `product_group`, and a subset of standard instrument metadata; fields such as `contract_size` may be absent or `null` |
| FIX `SecurityList`                                                                     | Standard FIX session                                                  | FIX contract-based metadata including `ContractMultiplier`                                                                        |

Do not assume that a field available through one interface is available through every other interface. In particular, use the multicast `InstrumentDefinition` when constructing or validating SBE order-entry messages.

## Quantity units and contract size

Starbase does not use contract counts or contract size for matching. All SBE order, quote, trade, and position quantities use Deribit's native **amount**:

| `quantityAsset`                                        | Starbase amount unit |
| ------------------------------------------------------ | -------------------- |
| `USD`                                                  | Dollar value         |
| The instrument's base currency, such as `BTC` or `ETH` | Number of coins      |

Encode amounts directly as [`Decimal72`](/starbase/binary-api-reference#composite-types), determine whether the amount represents dollar value or coins from `quantityAsset`, and validate the value against `minOrderQuantity`.

<Warning>
  Do not derive a contract count before sending an SBE `quantity`, and do not copy a FIX `OrderQty` expressed in contracts into an SBE message. `contract_size` and FIX `ContractMultiplier` remain available for standard JSON-RPC and FIX workflows, but Starbase does not consume either value.
</Warning>

Starbase is designed as a closed system for latency-sensitive matching. Broker, clearing, and other account-management workflows remain on the standard Deribit APIs, so applications that use those workflows may still need the standard reference data in addition to the Starbase feed.

### InstrumentDefinition (10)

| Field | Name                        | Type   | Length | Description                                                                        |
| ----- | --------------------------- | ------ | ------ | ---------------------------------------------------------------------------------- |
| 1     | instrumentId                | int64  | 8      | Numeric instrument ID                                                              |
| 2     | name                        | char   | 128    | Name of instrument on Deribit                                                      |
| 3     | indexId                     | int64  | 8      | The associated index                                                               |
| 4     | underlying                  | char   | 64     | The underlying future; only applicable to options                                  |
| 5     | quantityAsset               | char   | 8      | Asset used for quantity/amount                                                     |
| 6     | priceAsset                  | char   | 8      | Asset used for pricing                                                             |
| 7     | expiryTime                  | int64  | 8      | Nanoseconds since epoch. Time of expiration (optional)                             |
| 8     | strikePrice                 | int64  | 8      | Strike price mantissa (×10⁻⁹); optional                                            |
| 9     | minOrderQuantity            | int64  | 8      | Minimum order quantity mantissa (aka baseIncrement)                                |
| 10    | tickSize                    | int64  | 8      | Default tick size mantissa (×10⁻⁹)                                                 |
| 11    | quantityExponent            | int8   | 1      | Exponent applied to all quantity fields (value = mantissa × 10^quantityExponent)   |
| 12    | type                        | int8   | 1      | `0`=PerpFuture `1`=Option `2`=Spot `3`=FutureCombo `4`=OptionCombo `5`=DatedFuture |
| 13    | flags                       | uint8  | 1      | Instrument attributes (see flags table below)                                      |
| 14    | status                      | int8   | 1      | `0`=Open `1`=Inactive `2`=Settlement `3`=Delivered `4`=Locked `5`=Halted           |
| 15    | blockLengthOfLargeTickSizes | uint16 | 2      | Block length of each largeTickSizes group entry                                    |
| 16    | numberOfLargeTickSizes      | uint16 | 2      | Number of large tick size steps                                                    |
| ->17  | largeTickSize               | int64  | 8      | Tick size mantissa (×10⁻⁹) applicable when price ≥ thresholdPrice                  |
| ->18  | thresholdPrice              | int64  | 8      | Prices at or above this value use largeTickSize                                    |
| 19    | blockLengthOfLegs           | uint16 | 2      | Block length of each legs group entry                                              |
| 20    | numberOfLegs                | uint16 | 2      | Number of legs in the combination instrument. Maximum 4                            |
| ->21  | legInstrumentId             | int64  | 8      | Numeric instrumentId of the leg instrument                                         |
| ->22  | ratio                       | int8   | 1      | Amount of leg traded per combination unit. Positive = buy leg when buying combo    |

The table below outlines the content of field 13 (`flags`) of `InstrumentDefinition`.

| Bit (0 = LSB) | Name        | Description                        |
| ------------- | ----------- | ---------------------------------- |
| 0             | isReversed  | Set if the instrument is inverse   |
| 1             | isPutOption | Set if the option is a put         |
| 2             | isPerpetual | Set if the instrument is perpetual |

***

### InstrumentStatusUpdate (16)

| Field | Name          | Type  | Length | Description                                                              |
| ----- | ------------- | ----- | ------ | ------------------------------------------------------------------------ |
| 1     | instrumentId  | int64 | 8      | Numeric instrument ID                                                    |
| 2     | tradingStatus | int8  | 1      | `0`=Open `1`=Inactive `2`=Settlement `3`=Delivered `4`=Locked `5`=Halted |


## Related topics

- [Binary API Reference](/starbase/binary-api-reference.md)
- [Infrastructure, Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [Starbase API Overview](/starbase/overview.md)
- [Market Data Collection](/articles/market-data-collection-best-practices.md)
- [public/get_funding_chart_data](/api-reference/market-data/public-get_funding_chart_data.md)
