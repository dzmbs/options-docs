# Get Liquidation History

### Method Name

#### `public/get_liquidation_history`

Returns a paginated liquidation history for all subaccounts. Note that the pagination is based on the number of<br />raw events that include bids, auction start, and auction end events. This means that the count returned in the<br />pagination info will be larger than the total number of auction events. This also means the number of returned<br />auctions per page will be smaller than the supplied `page_size`.

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
    <strong>end_timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>End timestamp of the event history in ms since Unix epoch (default current time)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>page</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Page number of results to return (default 1, returns last if above <code>num_pages</code>)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>page_size</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of results per page (default 100, max 1000)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>start_timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Start timestamp of the event history in ms since Unix epoch (default 0)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font"></span>
    <strong>subaccount_id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Optional) Subaccount ID</span>
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
    <strong>auctions</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array&nbsp;of&nbsp;objects</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>List of auction results</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>auction_id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unique ID of the auction</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>auction_type</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Type of auction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>solvent</code> <code>insolvent</code>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>end_timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer&nbsp;or&nbsp;null</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp of the auction end (in ms since UNIX epoch), or <code>null</code> if not ended</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>fee</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Fee paid by the subaccount</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>start_timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp of the auction start (in ms since UNIX epoch)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>subaccount_id</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Liquidated subaccount ID</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>tx_hash</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Hash of the transaction that started the auction</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].</span>
    <strong>bids</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array&nbsp;of&nbsp;objects</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>List of auction bid events</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>cash_received</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Cash received by the subaccount for the liquidation. For the liquidated accounts this is the amount the liquidator paid to buy out the percentage of the portfolio. For the liquidator account, this is the amount they received from the security module (if positive) or the amount they paid for the bid (if negative)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>discount_pnl</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL due to liquidating or being liquidated at a discount to mark portfolio value</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>percent_liquidated</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Percent of the subaccount that was liquidated</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>realized_pnl</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL of the auction bid, assuming positions are closed at mark price at the time of the liquidation</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>realized_pnl_excl_fees</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL of the auction bid, excluding fees from total cost basis, assuming positions are closed at mark price at the time of the liquidation</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>timestamp</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Timestamp of the bid (in ms since UNIX epoch)</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>tx_hash</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Hash of the bid transaction</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>amounts_liquidated</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amounts of each asset that were closed</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>positions_realized_pnl</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL of each position that was closed</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.auctions[].bids[].</span>
    <strong>positions_realized_pnl_excl_fees</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL of each position that was closed, excluding fees from total cost basis</span>
  </td>
</tr><tr>
  <td className="ws-row-blank"></td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.</span>
    <strong>pagination</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Pagination info</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.pagination.</span>
    <strong>count</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total number of items, across all pages</span>
  </td>
</tr><tr>
  <td style={{textAlign: "left"}}>
    <span className="ws-small-font">result.pagination.</span>
    <strong>num_pages</strong>&nbsp;
    <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span>&nbsp;<span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of pages</span>
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