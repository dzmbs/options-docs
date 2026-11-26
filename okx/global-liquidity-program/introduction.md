## Introduction

The OKX Global Liquidity Program (GLP) offers fee benefits to eligible market makers based on trading or quoting performance.

- **GLP-A**: Type A (top) pairs. Assessed weekly on unadjusted trading market share, separately for Maker and Taker. Benefit: VIP 9 + Colo.

- **GLP-B**: Type B pairs (most other pairs). Assessed weekly on adjusted trading market share, separately for Maker and Taker. Benefit: VIP 6–9, with Colo at VIP 9. Expiry Futures & Nitro Spreads are assessed across all pairs on unadjusted share.

- **GLP-C**: Liquidity-incentive pairs (Spot and Perpetuals). Assessed hourly on bilateral weighted quoting share. Benefit: VIP 6–9 Maker fees from the next hour.

Participants must meet AUM and organic VIP tier requirements; see the [OKX Liquidity Program page](https://www.okx.com/fees/liquidity-program) for details. Where more than one program applies, the most favorable fee applies. Program participants are not eligible for other VIP-related or volume-related promotions or rebates.

Only enrolled accounts can access the user endpoints in this section. A sub-account API key returns the master account's data.

[Program details](https://www.okx.com/help/introducing-the-okx-global-liquidity-program) · [GLP Workspace](https://www.okx.com/glp-workspace) · To apply, contact your Relationship Manager or email `institutional@okx.com`.

**Common error codes**

| Error code | HTTP status code | Error message |
| --- | --- | --- |
| 50001 | 503 | Service temporarily unavailable. Please try again later. |
| 50014 | 200 | Parameter {param0} can not be empty |
| 50016 | 200 | Parameter {param0} does not match parameter {param1} |
| 50026 | 500 | System error. Try again later |
| 50030 | 200 | You don't have permission to use this API endpoint |
| 51000 | 200 | Parameter error |
