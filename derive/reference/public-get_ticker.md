# Get Ticker

### Method Name

#### `public/get_ticker`

Get ticker information (best bid / ask, instrument contraints, fees info, etc.) for a single instrument<br /><br />DEPRECATION NOTICE: This RPC is deprecated in favor of `get_tickers` on Dec 1, 2025.

### Parameters

<div className="rdmd-table">
  <div className="rdmd-table-inner">
    <table>
      <thead>
        <tr>
          <th style={{ textAlign: 'left' }}></th>
        </tr>
      </thead>
      <tbody><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>instrument_name</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
  </td>
</tr></tbody>
    </table>
  </div>
</div>

### Response

<div className="rdmd-table">
  <div className="rdmd-table-inner">
    <table>
      <thead>
        <tr>
          <th style={{ textAlign: 'left' }}></th>
        </tr>
      </thead>
      <tbody><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string&nbsp;or&nbsp;integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>result</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>amount_step</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum valid increment of order amount</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>base_asset_address</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain address of the base asset</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>base_asset_sub_id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Sub ID of the specific base asset as defined in Asset.sol</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>base_currency</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Underlying currency of base asset (<code>ETH</code>, <code>BTC</code>, etc)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>base_fee</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>$ base fee added to every taker order</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>best_ask_amount</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amount of contracts / tokens available at best ask price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>best_ask_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Best ask price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>best_bid_amount</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amount of contracts / tokens available at best bid price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>best_bid_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Best bid price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>erc20_details</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object&nbsp;or&nbsp;null</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Details of the erc20 asset (if applicable)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.erc20_details.</span>
    <strong>decimals</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of decimals of the underlying on-chain ERC20 token</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.erc20_details.</span>
    <strong>borrow_index</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Latest borrow index as per <code>CashAsset.sol</code> implementation</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.erc20_details.</span>
    <strong>supply_index</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Latest supply index as per <code>CashAsset.sol</code> implementation</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.erc20_details.</span>
    <strong>underlying_erc20_address</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Address of underlying on-chain ERC20 (not V2 asset)</span>
  </td>
</tr><tr>
  <td className="ws-row-blank"></td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>fifo_min_allocation</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum number of contracts that get filled using FIFO. Actual number of contracts that gets filled by FIFO will be the max between this value and (1 - pro_rata_fraction) x order_amount, plus any size leftovers due to rounding.</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>five_percent_ask_depth</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total amount of contracts / tokens available at 5 percent above best ask price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>five_percent_bid_depth</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total amount of contracts / tokens available at 5 percent below best bid price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>index_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Index price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>instrument_name</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>instrument_type</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}><code>erc20</code>, <code>option</code>, or <code>perp</code></span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>erc20</code> <code>option</code> <code>perp</code>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>is_active</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>If <code>True</code>: instrument is tradeable within <code>activation</code> and <code>deactivation</code> timestamps</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>maker_fee_rate</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Percent of spot price fee rate for makers</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>mark_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Mark price</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>max_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Maximum price at which an agressive buyer can be matched. Any portion of a market order that would execute above this price will be cancelled. A limit buy order with limit price above this value is treated as post only (i.e. it will be rejected if it would cross any existing resting order).</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>maximum_amount</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Maximum valid amount of contracts / tokens per trade</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>min_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum price at which an agressive seller can be matched. Any portion of a market order that would execute below this price will be cancelled. A limit sell order with limit price below this value is treated as post only (i.e. it will be rejected if it would cross any existing resting order).</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>minimum_amount</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum valid amount of contracts / tokens per trade</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>option_details</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object&nbsp;or&nbsp;null</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Details of the option asset (if applicable)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_details.</span>
    <strong>expiry</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unix timestamp of expiry date (in seconds)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_details.</span>
    <strong>index</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Underlying settlement price index</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_details.</span>
    <strong>option_type</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>C</code> <code>P</code>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_details.</span>
    <strong>strike</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_details.</span>
    <strong>settlement_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string&nbsp;or&nbsp;null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Settlement price of the option</span>
  </td>
</tr><tr>
  <td className="ws-row-blank"></td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>option_pricing</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object&nbsp;or&nbsp;null</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Greeks, forward price, iv and mark price of the instrument (options only)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>ask_iv</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Implied volatility of the current best ask</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>bid_iv</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Implied volatility of the current best bid</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>delta</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Delta of the option</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>discount_factor</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Discount factor used to calculate option premium</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>forward_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Forward price used to calculate option premium</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>gamma</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Gamma of the option</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>iv</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Implied volatility of the option</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>mark_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Mark price of the option</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>rho</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Rho of the option</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>theta</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Theta of the option</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.option_pricing.</span>
    <strong>vega</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Vega of the option</span>
  </td>
</tr><tr>
  <td className="ws-row-blank"></td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>perp_details</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object&nbsp;or&nbsp;null</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Details of the perp asset (if applicable)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.perp_details.</span>
    <strong>aggregate_funding</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Latest aggregated funding as per <code>PerpAsset.sol</code></span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.perp_details.</span>
    <strong>funding_rate</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Current hourly funding rate as per <code>PerpAsset.sol</code></span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.perp_details.</span>
    <strong>index</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Underlying spot price index for funding rate</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.perp_details.</span>
    <strong>max_rate_per_hour</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Max rate per hour as per <code>PerpAsset.sol</code></span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.perp_details.</span>
    <strong>min_rate_per_hour</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Min rate per hour as per <code>PerpAsset.sol</code></span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.perp_details.</span>
    <strong>static_interest_rate</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Static interest rate as per <code>PerpAsset.sol</code></span>
  </td>
</tr><tr>
  <td className="ws-row-blank"></td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>pro_rata_amount_step</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Pro-rata fill share of every order is rounded down to be a multiple of this number. Leftovers of the order due to rounding are filled FIFO.</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>pro_rata_fraction</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Fraction of order that gets filled using pro-rata matching. If zero, the matching is full FIFO.</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>quote_currency</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Quote currency (<code>USD</code> for perps, <code>USDC</code> for options)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>scheduled_activation</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp at which became or will become active (if applicable)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>scheduled_deactivation</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Scheduled deactivation time for instrument (if applicable)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>taker_fee_rate</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Percent of spot price fee rate for takers</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>tick_size</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Tick size of the instrument, i.e. minimum price increment</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp of the ticker feed snapshot</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>open_interest</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Margin type of subaccount (<code>PM</code> (Portfolio Margin), <code>PM2</code> (Portfolio Margin 2), or <code>SM</code> (Standard Margin)) -&gt; (current open interest, open interest cap, manager currency)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>mark_price_fee_rate_cap</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string&nbsp;or&nbsp;null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Percent of option price fee cap, e.g. 12.5%, null if not applicable</span>
  </td>
</tr></tbody>
    </table>
  </div>
</div>

### Example

```shell
{request_example_shell}
```
```javascript
{request_example_javascript}
```
```python
{request_example_python}
```

> The above command returns JSON structured like this:

```json
{response_example_json}
```