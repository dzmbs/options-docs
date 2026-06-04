> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Ticker (Instrument Name) (Interval)

### Channel Name Schema

#### `ticker.{instrument_name}.{interval}`

DEPRECATED SINCE DECEMBER 1, 2025 IN FAVOR OF TICKER\_SLIM

### Channel Parameters

<div className="rdmd-table">
  <div className="rdmd-table-inner">
    <table>
      <thead>
        <tr>
          <th style={{ textAlign: 'left' }} />
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>interval</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Interval in milliseconds</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>100</code> <code>1000</code>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

### Notification Data

<div className="rdmd-table">
  <div className="rdmd-table-inner">
    <table>
      <thead>
        <tr>
          <th style={{ textAlign: 'left' }} />
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>channel</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subscribed channel name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>data</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp of the ticker feed snapshot</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.</span>
            <strong>instrument\_ticker</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument of the ticker feed snapshot</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>amount\_step</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum valid increment of order amount</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>base\_asset\_address</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain address of the base asset</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>base\_asset\_sub\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Sub ID of the specific base asset as defined in Asset.sol</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>base\_currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Underlying currency of base asset (<code>ETH</code>, <code>BTC</code>, etc)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>base\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>$ base fee added to every taker order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>best\_ask\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amount of contracts / tokens available at best ask price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>best\_ask\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Best ask price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>best\_bid\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amount of contracts / tokens available at best bid price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>best\_bid\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Best bid price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>erc20\_details</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Details of the erc20 asset (if applicable)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.erc20\_details.</span>
            <strong>decimals</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of decimals of the underlying on-chain ERC20 token</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.erc20\_details.</span>
            <strong>borrow\_index</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Latest borrow index as per <code>CashAsset.sol</code> implementation</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.erc20\_details.</span>
            <strong>supply\_index</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Latest supply index as per <code>CashAsset.sol</code> implementation</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.erc20\_details.</span>
            <strong>underlying\_erc20\_address</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Address of underlying on-chain ERC20 (not V2 asset)</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>fifo\_min\_allocation</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum number of contracts that get filled using FIFO. Actual number of contracts that gets filled by FIFO will be the max between this value and (1 - pro\_rata\_fraction) x order\_amount, plus any size leftovers due to rounding.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>five\_percent\_ask\_depth</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total amount of contracts / tokens available at 5 percent above best ask price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>five\_percent\_bid\_depth</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total amount of contracts / tokens available at 5 percent below best bid price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>index\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Index price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>instrument\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}><code>erc20</code>, <code>option</code>, or <code>perp</code></span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>erc20</code> <code>option</code> <code>perp</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>is\_active</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>If <code>True</code>: instrument is tradeable within <code>activation</code> and <code>deactivation</code> timestamps</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>maker\_fee\_rate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Percent of spot price fee rate for makers</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>mark\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Mark price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>max\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Maximum price at which an agressive buyer can be matched. Any portion of a market order that would execute above this price will be cancelled. A limit buy order with limit price above this value is treated as post only (i.e. it will be rejected if it would cross any existing resting order).</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>maximum\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Maximum valid amount of contracts / tokens per trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>min\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum price at which an agressive seller can be matched. Any portion of a market order that would execute below this price will be cancelled. A limit sell order with limit price below this value is treated as post only (i.e. it will be rejected if it would cross any existing resting order).</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>minimum\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum valid amount of contracts / tokens per trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>option\_details</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Details of the option asset (if applicable)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_details.</span>
            <strong>expiry</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unix timestamp of expiry date (in seconds)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_details.</span>
            <strong>index</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Underlying settlement price index</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_details.</span>
            <strong>option\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>C</code> <code>P</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_details.</span>
            <strong>strike</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_details.</span>
            <strong>settlement\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Settlement price of the option</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>option\_pricing</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Greeks, forward price, iv and mark price of the instrument (options only)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>ask\_iv</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Implied volatility of the current best ask</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>bid\_iv</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Implied volatility of the current best bid</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>delta</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Delta of the option</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>discount\_factor</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Discount factor used to calculate option premium</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>forward\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Forward price used to calculate option premium</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>gamma</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Gamma of the option</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>iv</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Implied volatility of the option</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>mark\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Mark price of the option</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>rho</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Rho of the option</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>theta</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Theta of the option</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.option\_pricing.</span>
            <strong>vega</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Vega of the option</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>perp\_details</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Details of the perp asset (if applicable)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.perp\_details.</span>
            <strong>aggregate\_funding</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Latest aggregated funding as per <code>PerpAsset.sol</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.perp\_details.</span>
            <strong>funding\_rate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Current hourly funding rate as per <code>PerpAsset.sol</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.perp\_details.</span>
            <strong>index</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Underlying spot price index for funding rate</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.perp\_details.</span>
            <strong>max\_rate\_per\_hour</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Max rate per hour as per <code>PerpAsset.sol</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.perp\_details.</span>
            <strong>min\_rate\_per\_hour</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Min rate per hour as per <code>PerpAsset.sol</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.perp\_details.</span>
            <strong>static\_interest\_rate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Static interest rate as per <code>PerpAsset.sol</code></span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>pro\_rata\_amount\_step</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Pro-rata fill share of every order is rounded down to be a multiple of this number. Leftovers of the order due to rounding are filled FIFO.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>pro\_rata\_fraction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Fraction of order that gets filled using pro-rata matching. If zero, the matching is full FIFO.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>quote\_currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Quote currency (<code>USD</code> for perps, <code>USDC</code> for options)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>scheduled\_activation</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp at which became or will become active (if applicable)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>scheduled\_deactivation</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Scheduled deactivation time for instrument (if applicable)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>taker\_fee\_rate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Percent of spot price fee rate for takers</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>tick\_size</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Tick size of the instrument, i.e. minimum price increment</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp of the ticker feed snapshot</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>open\_interest</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Margin type of subaccount (<code>PM</code> (Portfolio Margin), <code>PM2</code> (Portfolio Margin 2), or <code>SM</code> (Standard Margin)) -> (current open interest, open interest cap, manager currency)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">data.instrument\_ticker.</span>
            <strong>mark\_price\_fee\_rate\_cap</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Percent of option price fee cap, e.g. 12.5%, null if not applicable</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

### Example

> *Subscriptions are only available via websockets.*

```javascript
{request_example_javascript}
```

```python
{request_example_python}
```

> Notification messages on this channel will look like this:

```json
{response_example_json}
```