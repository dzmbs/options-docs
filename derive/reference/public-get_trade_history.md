> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Trade History

### Method Name

#### `public/get_trade_history`

Get trade history for a subaccount, with filter parameters.

### Parameters

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

            <strong>currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Currency to filter by (defaults to all)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>from\_timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Earliest timestamp to filter by (in ms since Unix epoch). If not provied, defaults to 0.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name to filter by (defaults to all)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>instrument\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument type to filter by (defaults to all)</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>erc20</code> <code>option</code> <code>perp</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>page</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Page number of results to return (default 1, returns last if above <code>num\_pages</code>)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>page\_size</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of results per page (default 100, max 1000)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID to filter by</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>to\_timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Latest timestamp to filter by (in ms since Unix epoch). If not provied, defaults to returning all data up to current time.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>trade\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Trade ID to filter by. If set, all other filters are ignored</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>tx\_hash</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>On-chain tx hash to filter by. If set, all other filters are ignored</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>tx\_status</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Transaction status to filter by (default <code>settled</code>).</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>settled</code> <code>reverted</code> <code>timed\_out</code>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

### Response

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

            <strong>id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>result</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.</span>
            <strong>pagination</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Pagination info</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.pagination.</span>
            <strong>count</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total number of items, across all pages</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.pagination.</span>
            <strong>num\_pages</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of pages</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.</span>
            <strong>trades</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of objects</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>List of trades</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>direction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order direction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>buy</code> <code>sell</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>expected\_rebate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Expected rebate for this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>extra\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Extra fee in USDC added by the referring client (included in trade fee)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>index\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Index price of the underlying at the time of the trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>liquidity\_role</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Role of the user in the trade</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>maker</code> <code>taker</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>mark\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Mark price of the instrument at the time of the trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>quote\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Quote ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>realized\_pnl</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL for this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>realized\_pnl\_excl\_fees</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL for this trade using cost accounting that excludes fees</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>rfq\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>RFQ ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Trade timestamp (in ms since Unix epoch)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>trade\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amount filled in this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>trade\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Fee for this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>trade\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Trade ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>trade\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Price at which the trade was filled</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>tx\_hash</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain transaction hash</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>tx\_status</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain transaction status</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>settled</code> <code>reverted</code> <code>timed\_out</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.trades\[].</span>
            <strong>wallet</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Wallet address (owner) of the subaccount</span>
          </td>
        </tr>
      </tbody>
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