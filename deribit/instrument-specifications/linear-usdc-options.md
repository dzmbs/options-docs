# Linear USDC Options

> Source: https://support.deribit.com/hc/en-us/articles/31424932728093-Linear-USDC-Options
> Section: Exchange → Instrument Specifications

Linear USDC Options on Deribit are European options, priced and cash settled in USDC.

European style options are exercised only at expiry and cannot be exercised before. On Deribit, this will happen automatically at expiry. (Though the options are only exercised at expiry, traders are free to close their positions before expiry in the open market.)

Cash settlement means that at expiry, the writer of the options contract will pay the profit due to the holder in cash, rather than exchange the asset for the strike price.

The options are priced in USDC. Additionally, the implied volatility of the option's price is also displayed on the platform.

A call option is the right to buy the underlying asset at a specific price (the strike price), and a put option is the right to sell the underlying asset at a specific price (the strike price). Though remember, with cash settlement it is only the intrinsic value of the option that is paid when the option expires.

Altcoin options also typically have a contract multiplier, meaning each contract represents a certain amount of the underlying currency. More info on this below.

## Trading Examples

**Buying a call option**

A trader buys a SOL call option with a strike price of 250 USDC for 10 USDC. As Solana has a multiplier of 10 applied the buyer pays 10 * 10 USDC = 100 USDC. With the multiplier this call option represents the right to buy 10 SOL for 250 USDC each. The option is cash settled.

At the expiry, the SOL Index is at 275 USDC and the delivery price is 275 USDC. The option is settled for 25 USDC per 1 SOL (275 - 250 = 25). As Solana has a multiplier of 10 the total USDC settled is 25 * 10 = 250 USDC. The trader's account is credited with 250 USDC and the seller's account is debited with 250 USDC. The initial cost was 100 USDC, therefore the trader's profit is 150 USDC.

Any call option with a strike price above 275 USDC will expire worthless. Exercising of in-the-money options happens automatically at expiry.

**Buying a put option**

A trader buys a SOL put option with a strike price of 250 USDC for 10 USDC. At expiry, the SOL Index is at 225 USDC. The option is settled for 25 USDC per 1 SOL (250 - 225 = 25). As Solana has a multiplier of 10 the total USDC settled is 25 * 10 = 250 USDC. Initial purchase price was 100 USDC; trader's profit is 150 USDC.

**Selling a call option**

A trader sells a SOL call option with a strike price of 250 USDC for 10 USDC, receiving 100 USDC. At expiry the SOL Index is at 225 USDC — the option expires worthless. The buyer lost 100 USDC and the seller gained 100 USDC.

**Selling a put option**

A trader sells a put option with a strike price of 250 USDC for 10 USDC. At expiry the SOL Index is at 275 USDC — the option expires worthless. The buyer lost 100 USDC and the seller gained 100 USDC.

## Linear Option Contract Specifications

| Field | BTC_USDC | ETH_USDC | AVAX_USDC | SOL_USDC | TRX_USDC | XRP_USDC |
| --- | --- | --- | --- | --- | --- | --- |
| **Symbol** | `BTC_USDC-DDMMMYY-STRIKE-SIDE` | `ETH_USDC-DDMMMYY-STRIKE-SIDE` | `AVAX_USDC-DDMMMYY-STRIKE-SIDE` | `SOL_USDC-DDMMMYY-STRIKE-SIDE` | `TRX_USDC-DDMMMYY-STRIKE-SIDE` | `XRP_USDC-DDMMMYY-STRIKE-SIDE` |
| **Underlying Index** | Deribit BTC_USDC Index | Deribit ETH_USDC Index | Deribit AVAX_USDC Index | Deribit SOL_USDC Index | Deribit TRX_USDC Index | Deribit XRP_USDC Index |
| **Type** | Linear | Linear | Linear | Linear | Linear | Linear |
| **Category** | Option | Option | Option | Option | Option | Option |
| **Trading Hours** | 24/7 | 24/7 | 24/7 | 24/7 | 24/7 | 24/7 |
| **Quoted Currency** | USDC | USDC | USDC | USDC | USDC | USDC |
| **Margin Currency** | USDC | USDC | USDC | USDC | USDC | USDC |
| **Contract Multiplier** | 1 (1 BTC per contract) | 1 (1 ETH per contract) | 100 (100 AVAX per contract) | 10 (10 SOL per contract) | 10,000 (10,000 TRX per contract) | 1,000 (1,000 XRP per contract) |
| **Contract Size** | 1 BTC | 1 ETH | 100 AVAX | 10 SOL | 10,000 TRX | 1,000 XRP |
| **Minimum Order Size** | 0.01 contract | 0.1 contract | 1 contract | 1 contract | 1 contract | 1 contract |
| **Minimum Tick Size** | ≤1,000 USDC: 5 USDC; >1,000 USDC: 20 USDC | ≤50 USDC: 0.2 USDC; >50 USDC: 1 USDC | ≤0.1 USDC: 0.0005; >0.1 USDC: 0.0020 | 0.10 USDC | ≤0.01 USDC: 0.00005; >0.01 USDC: 0.0001 | 0.0005 USDC |
| **Minimum Block Size** | 25 contracts (25 BTC notional) | 250 contracts (250 ETH notional) | 25 contracts (2,500 AVAX notional) | 150 contracts (1,500 SOL notional) | 25 contracts (250,000 TRX notional) | 75 contracts (75,000 XRP notional) |
| **Minimum Block Tick** | 5 USDC | 0.2 USDC | 0.0005 USDC | 0.10 USDC | 0.00005 USDC | 0.0005 USDC |
| **Minimum Combo Tick** | 5 USDC | 0.2 USDC | 0.0005 USDC | 0.10 USDC | 0.00005 USDC | 0.0005 USDC |
| **Liquidation Fee** | 0.19% of Index price | | | | | |
| **Position Limit** | Maximum total short option position size: 1,000,000 USDC (Standard Margin) | | | | | |

**Symbol format:** Date = DDMMMYY (e.g. 28MAR25), Strike = strike price, Side = C (call) or P (put).

> **Note:** For some USDC-settled options in the API, the strike can be shown as `xdyyyy` for options with strikes around or below $1. `x` = whole dollar, `d` = decimal point, `yyyy` = fraction of a dollar.

> **Note (as of 15 July 2025):** The BTC-USDC index is pegged to the BTC-USD index, and the ETH-USDC index is pegged to the ETH-USD index. For delivery and settlement, parity between USD and USDC is assumed. For collateral valuation in X:SM and X:PM accounts, the USDC/USD exchange rate is still used.

### Underlying Future

The forward price for an expiry is the corresponding future's mark price. If there is no corresponding future, a synthetic future is used.

### Strike Prices

ITM, ATM, and OTM strike prices are initially listed. New series are added when the underlying trades above the highest or below the lowest available strike.

### Initial Margin

**Standard Margin account:**

- **Long call/put:** Premium paid in full at purchase. No further margin requirements.
- **Short Call (BTC/ETH):** `MAX(0.15 - OTM_Amount/Index, 0.1) * Index + Mark_Price` where `OTM_Amount = MAX(Strike - Index, 0)`
- **Short Put (BTC/ETH):** `MAX((0.15 - OTM_Amount/Index) * Index, 0.1 * Strike) + Mark_Price` where `OTM_Amount = MAX(Index - Strike, 0)`

(ETH uses 0.2 / 0.13 instead of 0.15 / 0.1 for short calls/puts.)

### Maintenance Margin

**Standard Margin account:**

- **Long call/put:** No maintenance margin beyond the premium paid (positive PnL is locked in the position).
- **Short Call (BTC/ETH):** `0.075 * Index + Mark_Price`
- **Short Put (BTC/ETH):** `0.075 * MIN(Index, Strike) + Mark_Price`

(ETH uses 0.1 instead of 0.075.)

### Settlement

- **Delivery Price:** Time-weighted average of the Deribit index measured between 07:30–08:00 UTC.
- **Exercise Style:** European, cash settled. Automatic at expiry.
- **Settlement Amount (USDC):** Difference between delivery price and strike price.
- **Settlement Method:** Cash settlement in USDC.
- **Settlement / Expiration:** Daily at 08:00 AM UTC.

### Order Types

- Only limit orders accepted (no market orders).
- Post-only orders are supported.
- **Volatility (IV) orders** are supported via "Advanced Order" on the order form. IV orders use the forward price as the underlying.

### Mark Price

Usually the average of best bid and best ask. Risk management checks and bandwidths apply.

## Black-Scholes Formula (Linear / USDC-Settled)

Call option price:

```
C = (F * N(d1)) - (K * N(d2))
```

Put option price:

```
P = (K * N(-d2)) - (F * N(-d1))
```

Where:

```
d1 = (ln(F/K) + ((σ²)/2) * T) / (σ * sqrt(T))
d2 = d1 - (σ * sqrt(T))
```

| Symbol | Meaning |
| --- | --- |
| C / P | Mark price of the call / put option |
| K | Strike price |
| F | Forward price for the option expiry |
| T | Time until expiration (in years). E.g. 1 day 17 hours = (1 + 17/24) / 365 = 0.00468 |
| σ | Implied volatility |
| N | Standard cumulative normal distribution function |

## Allowed Trading Bandwidths

Option trades are limited by a combination of two parameters:

1. The highest potential value of the contract given a 6% price move up with a volatility range-up scenario.
2. The lowest potential value of the contract given a 6% price move down with a volatility range-down scenario.

Orders beyond the bandwidth will not be accepted. Bandwidth parameters may be adjusted at Deribit's sole discretion.

## Mistrade Rules

Deribit may adjust prices or reverse trades if options were traded at prices caused by abnormal, non-orderly market conditions. Adjustments are only made if the traded price was further than the **mistrade correction value** (10% of the index price) away from the mark price.

- Requests must be submitted within **2 hours** of trade execution to support@deribit.com.
- The theoretical price is the mark price; disagreements are resolved by consulting primary market makers.
- The insurance fund is not used for mistrades.
