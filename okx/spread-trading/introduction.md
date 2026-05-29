## Introduction

### Basic Concepts

- **Spread -** Entering a trade where the trader is long one instrument and short an offsetting quantity of a related instrument, forming a trade with two risk offsetting legs.

- **Order-book -** A collection of offers to trade an instrument or basket. Each offer contains a defined instrument or group of instruments, relevant quantity, and the price at which the offerer is willing to transact. Takers can then immediately consume these offers up to the full amount of quantity listed at the offered price. The pending order limit of spread trading is 500 across all spreads.

### High Level Workflow

Nitro Spreads is centered around the familiar concept of a Central Limit Order Book (**CLOB**).

- Spreads consist of instruments sourced from OKX where they are cleared and settled.

- Anyone can act as a "Taker," who consumes an existing resting order, or a "Maker," whose order is consumed.

- Trades take place when orders are crossed. Trades are then sent for clearing and settlement on OKX.

At a high level, the Nitro Spreads workflow is as follows:

- *Maker* rests a Limit Order upon a Spread's Order Book.

- *Taker* consumes a resting Order via a Limit Order.

- The crossed orders are sent for clearing and settlement.

- The *Taker* and *Maker* receive confirmation of the success or rejection of the Trade.

- All users are notified of successfully settled & cleared Trades, minus the counterparties or sides (`buy` / `sell`) involved.

Key aspects of Nitro Spreads:

- All Spreads have **publicly accessible** Central Limit Order Books **(CLOB)**.

- The availability of trading Spreads is determined by OKX. Typically, these Spreads encompass all possible combinations of delta one derivatives (Expiry Futures and Perpetual Futures) and SPOT within a specific instrument family (e.g. "BTC/USDT" or "ETH/USDC").

- **Partial fills** and multiple orders can be consumed as part of a single trade.

- **Counterparties** are **NOT** selected. All Spread Order Books can be engaged by anyone, effectively trading against the broader market.

- Anonymity is maintained throughout the process, with all orders and trades conducted on an **anonymous basis**.

- Users have the flexibility to place multiple orders on both the bid and ask sides of the Order Book, allowing for a **ladder-style** configuration.
