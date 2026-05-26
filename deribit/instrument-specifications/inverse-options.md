# Inverse Options

> Source: https://support.deribit.com/hc/en-us/articles/31424939096093-Inverse-Options
> Section: Exchange → Instrument Specifications

Deribit offers European style cash-settled inverse options for BTC and ETH.

European style options are exercised only at expiry and cannot be exercised before. On Deribit, this happens automatically at expiry. Option positions can still be closed before expiry by trading them in the open market.

Cash settlement means that at expiry, the writer pays only the intrinsic value of the option to the holder's cash balance, rather than exchanging the underlying asset for the strike price. When purchasing an option, the premium is immediately subtracted from the buyer's cash balance.

Inverse options are **priced in the base currency** (BTC or ETH). The equivalent USD price is also displayed, calculated using the latest index price. The implied volatility displayed uses the forward (not the index) as the underlying price in the IV calculation. Orders can be set in BTC/ETH, USD, or implied volatility — however, when USD or IV is used, the price is converted to the equivalent base currency amount and rounded to the nearest valid price.

The contract multiplier for inverse options is 1: a BTC call option is the right to buy 1 BTC at the strike price, and a put option is the right to sell 1 BTC at the strike price.

## Trade Examples

**Buying a call option**

A trader buys a BTC call option with a strike of 100,000 USD for 0.05 BTC. At expiry, the BTC Index is at 125,000 USD. The option settles for 25,000 USD per BTC (125,000 - 100,000 = 25,000). The trader's account is credited with 0.2 BTC (25,000 / 125,000), the seller's account is debited with 0.2 BTC. Initial purchase price was 0.05 BTC; profit is 0.15 BTC.

**Buying a put option**

A trader buys an ETH put option with a strike of 5,000 USD for 0.05 ETH. At expiry, the ETH Index is at 2,500 USD. The option settles for 2,500 USD per ETH (5,000 - 2,500 = 2,500). The trader's account is credited with 1 ETH (2,500 / 2,500), the seller's account is debited with 1 ETH. Initial purchase price was 0.05 ETH; profit is 0.95 ETH.

**Selling a call option**

A trader sells a BTC call option with a strike of 100,000 USD for 0.05 BTC. At expiry, the BTC Index is at 95,000 USD — the option expires worthless. The buyer lost 0.05 BTC and the seller gained 0.05 BTC.

**Selling a put option**

A trader sells an ETH put option with a strike of 5,000 USD for 0.05 ETH. At expiry, the ETH Index is at 6,000 USD — the option expires worthless. The buyer lost 0.05 ETH and the seller gained 0.05 ETH.

## Inverse Option Contract Specifications

| Field | BTC | ETH |
| --- | --- | --- |
| **Symbol** | `BTC-DDMMMYY-STRIKE-SIDE` | `ETH-DDMMMYY-STRIKE-SIDE` |
| **Underlying Index** | Deribit BTC Index | Deribit ETH Index |
| **Type** | Inverse | Inverse |
| **Category** | Option | Option |
| **Trading Hours** | 24/7 | 24/7 |
| **Quoted Currency** | BTC (USD equivalent shown in orderbook via BTC index) | ETH (USD equivalent shown in orderbook via ETH index) |
| **Margin Currency** | BTC | ETH |
| **Contract Multiplier** | 1 BTC | 1 ETH |
| **Contract Size** | 1 BTC | 1 ETH |
| **Minimum Order Size** | 0.1 option contract | 1 option contract |
| **Minimum Tick Size** | ≤0.0050 BTC: 0.0001 BTC; >0.0050 BTC: 0.0005 BTC | ≤0.0050 ETH: 0.0001 ETH; >0.0050 ETH: 0.0005 ETH |
| **Minimum Block Size** | 25 BTC (options) | 250 ETH (options) |
| **Minimum Block Tick** | 0.0001 BTC | 0.0001 ETH |
| **Minimum Combo Tick** | 0.0001 BTC | 0.0001 ETH |
| **Liquidation Fee** | 0.0019 BTC | 0.0019 ETH |
| **Position Limit** | Max total short option: 1,000 BTC (Standard Margin) | Max total short option: 10,000 ETH (Standard Margin) |
| **Mistrade Correction Value** | 0.05 BTC from mark price | 0.05 ETH from mark price |

**Symbol format:** Date = DDMMMYY (e.g. 28MAR25), Strike = strike price in USD, Side = C (call) or P (put).

### Underlying Future

The forward price for an expiry is the corresponding future's mark price. If there is no corresponding future, a synthetic future is used.

### Strike Prices

ITM, ATM, and OTM strike prices are initially listed. New series are added when the underlying trades above the highest or below the lowest available strike.

### Initial Margin

**Standard Margin account:**

- **Long Call/Put:** Premium paid in full at purchase. No further margin requirements.
- **Short Call:** `MAX(0.15 - MAX((Strike - Index)/Index, 0), 0.1) + Mark_Price`
- **Short Put:** `MAX(MAX(0.15 - MAX(Index - Strike, 0)/Index, 0.1) + Mark_Price, Maintenance_Margin)`

### Maintenance Margin

**Standard Margin account:**

- **Long call/put:** No maintenance margin beyond the premium paid. Positive PnL is locked in the position and cannot be withdrawn or used to cover other positions.
- **Short Call:** `0.075 + Mark_Price`
- **Short Put:** `MAX(0.075, 0.075 * Mark_Price) + Mark_Price`

### Settlement

- **Delivery Price:** Time-weighted average of the Deribit index measured between 07:30–08:00 UTC.
- **Exercise Style:** European, cash settled. Automatic at expiry.
- **Settlement Amount (USD):** Difference between delivery price and strike price.
- **Settlement Amount (base currency):** USD settlement amount divided by the delivery price.
- **Settlement Method:** Cash settlement in BTC (for BTC options) / ETH (for ETH options).
- **Settlement / Expiration:** Daily at 08:00 AM UTC.

### Mark Price

Usually the average of best bid and best ask. Risk management checks and bandwidths apply.

## Black-Scholes Formula (Inverse / Coin-Settled)

Call option price:

```
C = (X * N(d1)) - (K * N(d2) * e^(-R * T))
```

Put option price:

```
P = (K * N(-d2) * e^(-R * T)) - (X * N(-d1))
```

Where:

```
d1 = (ln(X/K) + (R + (σ²)/2) * T) / (σ * sqrt(T))
d2 = d1 - (σ * sqrt(T))
R  = ln(F/X) / T
```

| Symbol | Meaning |
| --- | --- |
| C / P | Mark price of the call / put option |
| X | Index price (relevant Deribit index) |
| K | Strike price |
| F | Forward price for the option expiry |
| R | Interest rate as calculated by Deribit |
| T | Time until expiration (in years). E.g. 1 day 17 hours = (1 + 17/24) / 365 = 0.00468 |
| σ | Implied volatility |
| N | Standard cumulative normal distribution function |

## Order Types

Only **limit orders** are accepted for options (no market orders). Post-only orders are supported (not available for advanced order types).

Traders can determine the price in three ways: **BTC/ETH**, **USD**, or **Implied Volatility**.

When an order is priced in USD or IV, the Deribit engine continuously updates the order to maintain the fixed USD value or IV. USD and IV orders are updated once per **6 seconds** (IV orders use the forward price as the underlying).

### USD Orders

Fixed USD orders maintain a constant USD value despite changing BTC/ETH prices. The relevant Deribit index is used to determine the BTC/ETH equivalent price. The engine continuously monitors and edits the order.

### Volatility Orders

Volatility orders have a pre-set constant implied volatility. This enables market-making across options series without additional market-maker tooling. Black's option pricing model is used. For volatility orders, the **forward price** (not the index) is used as the input to the pricing model.

> Note: Automatic hedging with futures is not yet supported (on the roadmap).

## Allowed Trading Bandwidth

Option trades are limited by a combination of two parameters:

1. The highest potential value of the contract given a 1 price-bucket move in the portfolio margin risk matrix.
2. The lowest potential value of the contract given a 1 price-bucket move, plus a minimum trading bandwidth constant (currently 0.015).

Orders beyond the bandwidth are adjusted to the maximum possible buy price or minimum possible sell price. Bandwidth parameters may be adjusted at Deribit's sole discretion.

## Mistrade Rules

Deribit may adjust prices or reverse trades if options were traded at prices caused by abnormal, non-orderly market conditions. Adjustments are only made if the traded price was further than the **mistrade correction value** (0.05 BTC or 0.05 ETH) away from the mark price.

- Requests must be submitted within **2 hours** of trade execution to support@deribit.com.
- The theoretical price is the mark price; disagreements are resolved by consulting primary market makers.
- The insurance fund is not used for mistrades.
