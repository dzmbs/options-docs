> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Market Model

> The market model of Starbase is a subset of Deribit's market model. In Starbase, instruments are linked with Indices and Underlyings.

## Instrument States

Instruments can be in different states that determine their availability for trading and what operations are allowed:

| State          | Description                                                                                                                                                                                                                                                                               |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Open**       | The instrument is available for trading. Only in this state can orders and quotes be entered or amended.                                                                                                                                                                                  |
| **Locked**     | Signifies an unexpected technical event. Instruments would become locked in the case of an incident. Orders can still be cancelled.                                                                                                                                                       |
| **Inactive**   | Instruments can be inactive for two different reasons:<br />- A newly listed instrument can start out as inactive, typically for new product launches.<br />- A combination instrument can become inactive (and later open again) to save ME capacity and to remove a quoting obligation. |
| **Settlement** | The instrument is temporarily unavailable as positions are settled and day orders are removed. Typically only lasts a few seconds. On the settlement moment where the instrument is delivered, a state of Delivered is sent instead.                                                      |
| **Halted**     | Signifies an expected technical event. Instruments would become halted in the case of scheduled maintenance. Orders can still be cancelled.                                                                                                                                               |
| **Delivered**  | At the moment of expiry, an instrument's state will change to Delivered. Afterwards, the instrument will never become tradeable again.                                                                                                                                                    |

## Instrument Hierarchy

### Instrument

Any tradeable spot pair or derivative is an Instrument. Periodically, Instrument Definition Messages are disseminated on the snapshot multicast channels of the SBE Market Data Feed. Instrument definitions can change during the lifetime of the instruments. Tick sizes, states and underlying instruments can all change intra-day.

### Index

Each Instrument is linked to an Index. The Index is the top-level underlying used for delivery price calculation, funding rates and circuit breakers. The Indices are disseminated in the SBE Market Data Feed in the Index Definition Message. Indices are linked to Instruments via the indexId field in the Instrument Definition Message.

### Underlying

Each instrument also has an immediate underlying. For options, this will be the associated tradeable or synthetic futures. For futures, this will be the index. The Underlying visibile in the Instrument Definition Message as a text field in the Instrument Definition message.


## Related topics

- [Starbase API Changelog](/changelogs/starbase.md)
- [Account Model](/starbase/account-model.md)
- [private/change_margin_model](/api-reference/account-management/private-change_margin_model.md)
- [Options Data Collection](/articles/options-data-collection-best-practices.md)
- [Cancel on Disconnect](/starbase/cancel-on-disconnect.md)
