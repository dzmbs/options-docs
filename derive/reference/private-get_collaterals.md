# Get Collaterals

### Method Name

#### `private/get_collaterals`

Get collaterals of a subaccount<br />Required minimum session key permission level is `read_only`

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
    <strong>subaccount_id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount_id</span>
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
    <strong>subaccount_id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount_id</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>collaterals</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array&nbsp;of&nbsp;objects</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>All collaterals that count towards margin of subaccount</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>amount</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Asset amount of given collateral</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>amount_step</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Minimum amount step for the collateral</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>asset_name</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Asset name</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>asset_type</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Type of asset collateral (currently always <code>erc20</code>)</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>erc20</code> <code>option</code> <code>perp</code>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>average_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Average price of the collateral, 0 for USDC.</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>average_price_excl_fees</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Average price of whole position excluding fees</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>creation_timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp of when the position was opened (in ms since Unix epoch)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>cumulative_interest</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Cumulative interest earned on supplying collateral or paid for borrowing</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>currency</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Underlying currency of asset (<code>ETH</code>, <code>BTC</code>, etc)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>delta</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Asset delta w.r.t. the delta currency</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>delta_currency</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Currency with respect to which delta is reported.For example, LRTs like WEETH have their delta reported in ETH</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>initial_margin</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>USD value of collateral that contributes to initial margin</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>maintenance_margin</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>USD value of collateral that contributes to maintenance margin</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>mark_price</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Current mark price of the asset</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>mark_value</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>USD value of the collateral (amount * mark price)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>open_orders_margin</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>USD margin requirement for all open orders for this asset / instrument</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>pending_interest</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Portion of interest that has not yet been settled on-chain. This number is added to the portfolio value for margin calculations purposes.</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>realized_pnl</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized trading profit or loss of the collateral, 0 for USDC.</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>realized_pnl_excl_fees</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized trading profit or loss of the position excluding fees</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>total_fees</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total fees paid for opening and changing the position</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>unrealized_pnl</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unrealized trading profit or loss of the collateral, 0 for USDC.</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.collaterals[].</span>
    <strong>unrealized_pnl_excl_fees</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unrealized trading profit or loss of the position excluding fees</span>
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