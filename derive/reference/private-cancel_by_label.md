# Cancel By Label

### Method Name

#### `private/cancel_by_label`

Cancel all open orders for a given subaccount and a given label.  If instrument\_name is provided, only orders for that instrument will be cancelled.<br />Required minimum session key permission level is `admin`

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
    <strong>label</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Cancel all orders for this label</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>subaccount_id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>instrument_name</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name. If not provided, all orders for all instruments with the label will be cancelled.  If provided, request counts as a regular matching request for ratelimit purposes.</span>
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
    <strong>cancelled_orders</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of cancelled orders</span>
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