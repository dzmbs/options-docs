# Protocol Constants

## Rollup RPC Node

| Contract       | Mainnet Address                                                | Testnet Address                                                                                                  |
| -------------- | -------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| RPC Endpoint   | [https://rpc.lyra.finance](https://rpc.lyra.finance)           | [https://rpc-prod-testnet-0eakp60405.t.conduit.xyz](https://rpc-prod-testnet-0eakp60405.t.conduit.xyz)           |
| Block Explorer | [https://explorer.lyra.finance](https://explorer.lyra.finance) | [https://explorer-prod-testnet-0eakp60405.t.conduit.xyz](https://explorer-prod-testnet-0eakp60405.t.conduit.xyz) |

## Contracts

| Contract                      | Mainnet Address                            | Testnet Address                            |
| ----------------------------- | ------------------------------------------ | :----------------------------------------- |
| Matching.sol                  | 0xeB8d770ec18DB98Db922E9D83260A585b9F0DeAD | 0x3cc154e220c2197c5337b7Bd13363DD127Bc0C6E |
| SubAccount.sol                | 0xE7603DF191D699d8BD9891b821347dbAb889E5a5 | 0xb9ed1cc0c50bca7a391a6819e9cAb466f5501d73 |
| ERC20.sol \[USDC: 6 decimals] | 0x6879287835A86F50f784313dBEd5E5cCC5bb8481 | 0xe80F2a02398BBf1ab2C9cc52caD1978159c215BD |
| CashAsset.sol                 | 0x57B03E14d409ADC7fAb6CFc44b5886CAD2D5f02b | 0x6caf294DaC985ff653d5aE75b4FF8E0A66025928 |
| TradeModule.sol               | 0xB8D20c2B7a1Ad2EE33Bc50eF10876eD3035b5e7b | 0x87F2863866D85E3192a35A73b388BD625D83f2be |
| TransferModule.sol            | 0x01259207A40925b794C8ac320456F7F6c8FE2636 | 0x0CFC1a4a90741aB242cAfaCD798b409E12e68926 |
| DepositModule.sol             | 0x9B3FE5E5a3bcEa5df4E08c41Ce89C4e3Ff01Ace3 | 0x43223Db33AdA0575D2E100829543f8B04A37a1ec |
| WithdrawalModule.sol          | 0x9d0E8f5b25384C7310CB8C6aE32C8fbeb645d083 | 0xe850641C5207dc5E9423fB15f89ae6031A05fd92 |
| StandardRiskManager.sol       | 0x28c9ddF9A3B29c2E6a561c1BC520954e5A33de5D | 0x28bE681F7bEa6f465cbcA1D25A2125fe7533391C |
| RFQ.sol                       | 0x9371352CCef6f5b36EfDFE90942fFE622Ab77F1D | 0x4E4DD8Be1e461913D9A5DBC4B830e67a8694ebCa |
| LiquidateAddress.sol          | 0x66d23e59DaEEF13904eFA2D4B8658aeD05f59a92 | 0x3e2a570B915fEDAFf6176A261d105A4A68a0EA8D |

## ETH Market

| Contract                       | Mainnet Address                            | Testnet Address                            |
| ------------------------------ | ------------------------------------------ | :----------------------------------------- |
| BaseAsset.sol                  |                                            | 0x41675b7746AE0E464f2594d258CF399c392A179C |
| ERC20.sol \[WETH: 18 decimals] |                                            | 0x3a34565D81156cF0B1b9bC5f14FD00333bcf6B93 |
| Option.sol                     | 0x4BB4C3CDc7562f08e9910A0C7D8bB7e108861eB4 | 0xBcB494059969DAaB460E0B5d4f5c2366aab79aa1 |
| Perp.sol                       | 0xAf65752C4643E25C02F693f9D4FE19cF23a095E3 | 0x010e26422790C6Cb3872330980FAa7628FD20294 |
| PortfolioRiskManager.sol       | 0xe7cD9370CdE6C9b5eAbCe8f86d01822d3de205A0 | 0xDF448056d7bf3f9Ca13d713114e17f1B7470DeBF |
| PortfolioRiskManager\_v2       | 0xc755DAe3fd295A687adf3e192387163f813F0598 |                                            |

## BTC Market

| Contract                      | Mainnet Address                            | Testnet Address                            |
| ----------------------------- | ------------------------------------------ | :----------------------------------------- |
| BaseAsset.sol                 |                                            | 0x0776C34032C618770ca2Be9eD3a11148128b1A50 |
| ERC20.sol \[WBTC: 8 decimals] |                                            | 0xF1493F3602Ab0fC576375a20D7E4B4714DB4422d |
| Option.sol                    | 0xd0711b9eBE84b778483709CDe62BacFDBAE13623 | 0xAeB81cbe6b19CeEB0dBE0d230CFFE35Bb40a13a7 |
| Perp.sol                      | 0xDBa83C0C654DB1cd914FA2710bA743e925B53086 | 0xAFB6Bb95cd70D5367e2C39e9dbEb422B9815339D |
| PortfolioRiskManager.sol      | 0x45DA02B9cCF384d7DbDD7b2b13e705BADB43Db0D | 0xbaC0328cd4Af53d52F9266Cdbd5bf46720320A20 |
| PortfolioRiskManager\_v2      | 0xC7adAB7A2b92019098dA55Ba4C5A8C65Ae7e52DC |                                            |

## Constants

| Constant                         | Mainnet                                                            | Testnet                                                            |
| -------------------------------- | ------------------------------------------------------------------ | :----------------------------------------------------------------- |
| DOMAIN\_SEPARATOR (Matching.sol) | 0xd96e5f90797da7ec8dc4e276260c7f3f87fedf68775fbe1ef116e996fc60441b | 0x9bcf4dc06df5d8bf23af818d5716491b995020f377d3b7b64c29ed14e3dd1105 |
| ACTION\_TYPEHASH (Matching.sol)  | 0x4d7a9f27c403ff9c0f19bce61d76d82f9aa29f8d6d4b0c5474607d9770d1af17 | 0x4d7a9f27c403ff9c0f19bce61d76d82f9aa29f8d6d4b0c5474607d9770d1af17 |
| CHAIN\_ID                        | 957                                                                | 901                                                                |