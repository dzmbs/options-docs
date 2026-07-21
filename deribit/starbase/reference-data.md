> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reference Data

> Reference data for the Starbase Binary API including InstrumentDefinition messages.

## Reference data

<Info>
  **Combination Orders**: Combination orders are treated as orders on outright books and are not differentiated in any way. Their orderbook\_id links to a combination order book.
</Info>

<Note>
  **Multicast is the recommended source for full reference data.** The Starbase REST API exposes a subset of instrument fields and does not include all attributes available in the SBE `InstrumentDefinition` message — for example, `minOrderQuantity` is not available via REST. Use the multicast reference data feed to obtain complete instrument definitions.
</Note>

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
