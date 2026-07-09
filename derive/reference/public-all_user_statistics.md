# All User Statistics

### Method Name

#### `public/all_user_statistics`

Get statistics for a specific user

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
    <strong>currency</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Currency for stats</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>end_time</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>End time for statistics in ms</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>instrument_name</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name for stats</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>is_rfq</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>True to select only RFQs, false to ignore them</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>start_time</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Start time for statistics in ms</span>
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
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array&nbsp;of&nbsp;objects</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_base_fee</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total base fee paid by the user</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_contract_fee</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total contract fee paid by the user</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_fees</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total fees paid by the user (<code>total_base_fee</code> + <code>total_contract_fee</code>)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_notional_volume</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total notional volume</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_premium_volume</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total premium volume</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_regular_base_fee</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total base fee user would have paid if they had no discounts</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_regular_contract_fee</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total contract fee user would have paid if they had no discounts</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>total_trades</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total trades</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>wallet</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Wallet address for the user</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>first_trade_timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer&nbsp;or&nbsp;null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>First trade timestamp</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result[].</span>
    <strong>last_trade_timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer&nbsp;or&nbsp;null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Last trade timestamp</span>
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