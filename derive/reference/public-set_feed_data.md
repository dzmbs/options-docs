> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Feed Data

### Method Name

#### `public/set_feed_data`

TODO description

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

            <strong>forward</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of objects</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>confidence</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The confidence score of the price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The currency for which the spot feed represents</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>deadline</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The latest time the data can be submitted on chain</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>expiry</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The expiry for the forward feed</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>fwd\_diff</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>difference of forward price from current spot price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>spot\_aggregate\_latest</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>expiry -> spot \* time value at the latest timestamp</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>spot\_aggregate\_start</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>spot \* time value at the start of the settlement period</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The timestamp for which the data was created</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Signatures</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].signatures.</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signatures of the given signers</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">forward\[].signatures.</span>
            <strong>signers</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signers who verify the data integrity</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>perp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of objects</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].</span>
            <strong>confidence</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The confidence score of the price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].</span>
            <strong>currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The currency for which the spot feed represents</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].</span>
            <strong>deadline</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The latest time the data can be submitted on chain</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].</span>
            <strong>spot\_diff\_value</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The difference between the spot price and the perp price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The timestamp for which the data was created</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].</span>
            <strong>type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The type of perp feed; mid price, ask impact or bid impact</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>P</code> <code>A</code> <code>B</code>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Signatures</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].signatures.</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signatures of the given signers</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">perp\[].signatures.</span>
            <strong>signers</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signers who verify the data integrity</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>rate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of objects</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].</span>
            <strong>confidence</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The confidence score of the rate</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].</span>
            <strong>currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The currency for which the spot feed represents</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].</span>
            <strong>deadline</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The latest time the data can be submitted on chain</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].</span>
            <strong>expiry</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The expiry for the rate feed</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].</span>
            <strong>rate</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The implied rate for the currency/expiry</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The timestamp for which the data was created</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Signatures</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].signatures.</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signatures of the given signers</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">rate\[].signatures.</span>
            <strong>signers</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signers who verify the data integrity</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>spot</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of objects</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].</span>
            <strong>confidence</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The confidence score of the price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].</span>
            <strong>currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The currency for which the spot feed represents</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].</span>
            <strong>deadline</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The latest time the data can be submitted on chain</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].</span>
            <strong>price</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The price of the currency in USD</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The timestamp for which the data was created</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Signatures</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].signatures.</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signatures of the given signers</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].signatures.</span>
            <strong>signers</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signers who verify the data integrity</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">spot\[].</span>
            <strong>feed\_source\_type</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The source of the feed</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>enum </span><code>S</code> <code>O</code>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font" />

            <strong>vol</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of objects</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].</span>
            <strong>confidence</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The confidence score of the price</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].</span>
            <strong>currency</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The currency for which the spot feed represents</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].</span>
            <strong>deadline</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The latest time the data can be submitted on chain</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].</span>
            <strong>expiry</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The expiry for the options for the vol feed</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].</span>
            <strong>timestamp</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>integer</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The timestamp for which the data was created</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>Signatures</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].signatures.</span>
            <strong>signatures</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signatures of the given signers</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].signatures.</span>
            <strong>signers</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>array of strings</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The signers who verify the data integrity</span>
          </td>
        </tr>

        <tr>
          <td className="ws-row-blank" />
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].</span>
            <strong>vol\_data</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>object</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span><br /><span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>The SVI parameters for the vol curve</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].vol\_data.</span>
            <strong>SVI\_a</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].vol\_data.</span>
            <strong>SVI\_b</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].vol\_data.</span>
            <strong>SVI\_fwd</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].vol\_data.</span>
            <strong>SVI\_m</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].vol\_data.</span>
            <strong>SVI\_refTau</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].vol\_data.</span>
            <strong>SVI\_rho</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
          </td>
        </tr>

        <tr>
          <td style={{textAlign: "left"}}>
            <span className="ws-small-font">vol\[].vol\_data.</span>
            <strong>SVI\_sigma</strong> 
            <span className="ws-data-type ws-small-font" style={{color: "#adb4c1", fontSize: "13px"}}>string</span> <span className="ws-required-tag ws-small-font" style={{color: "#e95f6a", marginLeft: "8px", fontSize: "13px"}}>required</span>
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