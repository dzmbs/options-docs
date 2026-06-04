> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer Position

### Method Name

#### `private/transfer_position`

Transfers a positions from one subaccount to another, owned by the same wallet.<br /><br />The transfer is executed as a pair of orders crossing each other.<br />The maker order is created first, followed by a taker order crossing it.<br />The order amounts, limit prices and instrument name must be the same for both orders.<br />Fee is not charged and a zero `max_fee` must be signed.<br />The maker order is forcibly considered to be `reduce_only`, meaning it can only reduce the position size.<br /><br />History: For position transfer history, use the `private/get_trade_history` RPC (not `private/get_erc20_transfer_history`).<br />Required minimum session key permission level is `admin`

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

            <strong>wallet</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Public key (wallet) of the account</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>maker\_params</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Maker order parameters and signature. Maximum transfer amount is limited by the size of the maker position. Transfers that increase the maker's position size are not allowed.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order amount in units of the base</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>direction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order direction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>buy</code> <code>sell</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>limit\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Limit price in quote currency.<br />This field is still required for market orders because it is a component of the signature. However, market orders will not leave a resting order in the book in case of a partial fill.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>max\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Max fee PER contract, denominated in USDC.<br />For resting orders (maker orders), max\_fee must be > 2 x max(taker\_fee, maker\_fee) x spot\_price + extra\_fee / amount.For crossing orders (taker order), max\_fee must be > maker max\_fee + base\_fee / fill\_amount.<br />Note, in this calculation, regardless of the custom account taker / maker fees, the standard taker / maker fees are used.<br />The max(limit\_price, index\_price) is used to calculate the notional volume.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>nonce</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unique nonce defined as (UTC\_timestamp in ms)(random\_number\_up\_to\_3\_digits) (e.g. 1695836058725001, where 001 is the random number).<br />Note, using a random number beyond 3 digits will cause JSON serialization to fail.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>signature</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Ethereum signature of the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>signature\_expiry\_sec</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unix timestamp in seconds. Order signature becomes invalid after this time, and the system will cancel the order.<br />Expiry MUST be at least 5 min from now.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>signer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Owner wallet address or registered session key that signed order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">maker\_params.</span>
            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>taker\_params</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Taker order parameters and signature</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order amount in units of the base</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>direction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order direction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>buy</code> <code>sell</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>limit\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Limit price in quote currency.<br />This field is still required for market orders because it is a component of the signature. However, market orders will not leave a resting order in the book in case of a partial fill.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>max\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Max fee PER contract, denominated in USDC.<br />For resting orders (maker orders), max\_fee must be > 2 x max(taker\_fee, maker\_fee) x spot\_price + extra\_fee / amount.For crossing orders (taker order), max\_fee must be > maker max\_fee + base\_fee / fill\_amount.<br />Note, in this calculation, regardless of the custom account taker / maker fees, the standard taker / maker fees are used.<br />The max(limit\_price, index\_price) is used to calculate the notional volume.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>nonce</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unique nonce defined as (UTC\_timestamp in ms)(random\_number\_up\_to\_3\_digits) (e.g. 1695836058725001, where 001 is the random number).<br />Note, using a random number beyond 3 digits will cause JSON serialization to fail.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>signature</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Ethereum signature of the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>signature\_expiry\_sec</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unix timestamp in seconds. Order signature becomes invalid after this time, and the system will cancel the order.<br />Expiry MUST be at least 5 min from now.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>signer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Owner wallet address or registered session key that signed order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">taker\_params.</span>
            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
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
            <strong>maker\_order</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order amount in units of the base</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>average\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Average fill price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>cancel\_reason</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>If cancelled, reason behind order cancellation</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>user\_request</code> <code>mmp\_trigger</code> <code>insufficient\_margin</code> <code>signed\_max\_fee\_too\_low</code> <code>cancel\_on\_disconnect</code> <code>ioc\_or\_market\_partial\_fill</code> <code>session\_key\_deregistered</code> <code>subaccount\_withdrawn</code> <code>compliance</code> <code>trigger\_failed</code> <code>validation\_failed</code> <code>algo\_completed</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>creation\_timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Creation timestamp (in ms since Unix epoch)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>direction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order direction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>buy</code> <code>sell</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>filled\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total filled amount for the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>is\_transfer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Whether the order was generated through <code>private/transfer\_position</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>label</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Optional user-defined label for the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>last\_update\_timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Last update timestamp (in ms since Unix epoch)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>limit\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Limit price in quote currency</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>max\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Max fee PER contract, denominated in USDC.Max fee must be > 2 x max(taker\_fee, maker\_fee) x spot\_price + extra\_fee / amount.If the order crosses the book, it must be >= 2 x max(taker\_fee, maker\_fee) x spot\_price + base\_fee / fill\_amount + extra\_fee / amount.Note, in this calculation, regardless of the account taker / maker fees, the standard taker / maker fees are used.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>mmp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Whether the order is tagged for market maker protections</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>nonce</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unique nonce defined as (UTC\_timestamp in ms)(random\_number\_up\_to\_3\_digits) (e.g. 1695836058725001, where 001 is the random number)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>order\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order fee paid so far</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>order\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>order\_status</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order status</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>open</code> <code>filled</code> <code>cancelled</code> <code>expired</code> <code>untriggered</code> <code>algo\_active</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>order\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order type</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>limit</code> <code>market</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>quote\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Quote ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>signature</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Ethereum signature of the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>signature\_expiry\_sec</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Signature expiry timestamp</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>signer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Owner wallet address or registered session key that signed order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>time\_in\_force</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Time in force</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>gtc</code> <code>post\_only</code> <code>fok</code> <code>ioc</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>algo\_duration\_sec</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total execution window in seconds</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>algo\_num\_slices</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of child executions</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>algo\_slices\_completed</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of slices executed so far</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>algo\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Algo order type (twap or vwap)</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>twap</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>extra\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Optional) Extra fee in USDC added to the total final fee paid by user (must be between 0.000001 and 1,000 USDC).</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>replaced\_order\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>If replaced, ID of the order that was replaced</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>signed\_limit\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The original limit price that the user signed. Only set when the order was adjusted (i.e., for post-only orders with reject\_post\_only=false that would have crossed). Used for on-chain submission.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>trigger\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Index or Market price to trigger order at</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>trigger\_price\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Trigger with Index or Mark Price</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>mark</code> <code>index</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>trigger\_reject\_message</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Error message if error occured during trigger</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_order.</span>
            <strong>trigger\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Stop-loss or Take-profit.</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>stoploss</code> <code>takeprofit</code>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.</span>
            <strong>maker\_trade</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>direction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order direction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>buy</code> <code>sell</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>expected\_rebate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Expected rebate for this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>extra\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Extra fee in USDC added by the referring client (included in trade fee)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>index\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Index price of the underlying at the time of the trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>is\_transfer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Whether the trade was generated through <code>private/transfer\_position</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>label</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Optional user-defined label for the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>liquidity\_role</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Role of the user in the trade</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>maker</code> <code>taker</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>mark\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Mark price of the instrument at the time of the trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>order\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>quote\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Quote ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>realized\_pnl</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL for this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>realized\_pnl\_excl\_fees</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL for this trade using cost accounting that excludes fees</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>rfq\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>RFQ ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Trade timestamp (in ms since Unix epoch)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>trade\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amount filled in this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>trade\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Base\_fee (only takers) + unit\_fee (adjusted via rebates / discounts) + extra\_fee (set by referrring client))</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>trade\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Trade ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>trade\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Price at which the trade was filled</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>transaction\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The transaction id of the related settlement transaction</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>tx\_hash</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain transaction hash</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.maker\_trade.</span>
            <strong>tx\_status</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain transaction status</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>requested</code> <code>pending</code> <code>settled</code> <code>reverted</code> <code>ignored</code> <code>timed\_out</code>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.</span>
            <strong>taker\_order</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order amount in units of the base</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>average\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Average fill price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>cancel\_reason</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>If cancelled, reason behind order cancellation</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>user\_request</code> <code>mmp\_trigger</code> <code>insufficient\_margin</code> <code>signed\_max\_fee\_too\_low</code> <code>cancel\_on\_disconnect</code> <code>ioc\_or\_market\_partial\_fill</code> <code>session\_key\_deregistered</code> <code>subaccount\_withdrawn</code> <code>compliance</code> <code>trigger\_failed</code> <code>validation\_failed</code> <code>algo\_completed</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>creation\_timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Creation timestamp (in ms since Unix epoch)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>direction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order direction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>buy</code> <code>sell</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>filled\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total filled amount for the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>is\_transfer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Whether the order was generated through <code>private/transfer\_position</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>label</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Optional user-defined label for the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>last\_update\_timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Last update timestamp (in ms since Unix epoch)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>limit\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Limit price in quote currency</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>max\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Max fee PER contract, denominated in USDC.Max fee must be > 2 x max(taker\_fee, maker\_fee) x spot\_price + extra\_fee / amount.If the order crosses the book, it must be >= 2 x max(taker\_fee, maker\_fee) x spot\_price + base\_fee / fill\_amount + extra\_fee / amount.Note, in this calculation, regardless of the account taker / maker fees, the standard taker / maker fees are used.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>mmp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Whether the order is tagged for market maker protections</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>nonce</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Unique nonce defined as (UTC\_timestamp in ms)(random\_number\_up\_to\_3\_digits) (e.g. 1695836058725001, where 001 is the random number)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>order\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order fee paid so far</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>order\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>order\_status</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order status</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>open</code> <code>filled</code> <code>cancelled</code> <code>expired</code> <code>untriggered</code> <code>algo\_active</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>order\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order type</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>limit</code> <code>market</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>quote\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Quote ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>signature</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Ethereum signature of the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>signature\_expiry\_sec</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Signature expiry timestamp</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>signer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Owner wallet address or registered session key that signed order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>time\_in\_force</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Time in force</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>gtc</code> <code>post\_only</code> <code>fok</code> <code>ioc</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>algo\_duration\_sec</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Total execution window in seconds</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>algo\_num\_slices</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of child executions</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>algo\_slices\_completed</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Number of slices executed so far</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>algo\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Algo order type (twap or vwap)</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>twap</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>extra\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Optional) Extra fee in USDC added to the total final fee paid by user (must be between 0.000001 and 1,000 USDC).</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>replaced\_order\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>If replaced, ID of the order that was replaced</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>signed\_limit\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The original limit price that the user signed. Only set when the order was adjusted (i.e., for post-only orders with reject\_post\_only=false that would have crossed). Used for on-chain submission.</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>trigger\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Index or Market price to trigger order at</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>trigger\_price\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Trigger with Index or Mark Price</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>mark</code> <code>index</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>trigger\_reject\_message</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Error message if error occured during trigger</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_order.</span>
            <strong>trigger\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>(Required for trigger orders) Stop-loss or Take-profit.</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>stoploss</code> <code>takeprofit</code>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.</span>
            <strong>taker\_trade</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>direction</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order direction</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>buy</code> <code>sell</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>expected\_rebate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Expected rebate for this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>extra\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Extra fee in USDC added by the referring client (included in trade fee)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>index\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Index price of the underlying at the time of the trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>instrument\_name</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Instrument name</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>is\_transfer</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>boolean</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Whether the trade was generated through <code>private/transfer\_position</code></span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>label</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Optional user-defined label for the order</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>liquidity\_role</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Role of the user in the trade</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>maker</code> <code>taker</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>mark\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Mark price of the instrument at the time of the trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>order\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Order ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>quote\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Quote ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>realized\_pnl</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL for this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>realized\_pnl\_excl\_fees</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Realized PnL for this trade using cost accounting that excludes fees</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>rfq\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>RFQ ID if the trade was executed via RFQ</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>subaccount\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Subaccount ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Trade timestamp (in ms since Unix epoch)</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>trade\_amount</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Amount filled in this trade</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>trade\_fee</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Base\_fee (only takers) + unit\_fee (adjusted via rebates / discounts) + extra\_fee (set by referrring client))</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>trade\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Trade ID</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>trade\_price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Price at which the trade was filled</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>transaction\_id</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The transaction id of the related settlement transaction</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>tx\_hash</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string or null</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain transaction hash</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">result.taker\_trade.</span>
            <strong>tx\_status</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Blockchain transaction status</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>requested</code> <code>pending</code> <code>settled</code> <code>reverted</code> <code>ignored</code> <code>timed\_out</code>
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