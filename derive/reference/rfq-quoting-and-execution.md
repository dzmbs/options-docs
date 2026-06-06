> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# RFQ Quoting and Execution [JavaScript]

Before making API calls, make sure to setup and fund you account in the "Getting Started" guide.

Similar to orderbook trading, RFQs are "self-custodial", and they require signed messages to be settled. Those signed messages guarantee that all legs of an RFQ will execute at the specified prices and amounts, as well as that the fee charged by the orderbook does not exceed the signed `max_fee`.

Unlike orderbook trading, makers and takers follow different rules and sign slightly different messages in order to complete an RFQ. The full flow is below:

1. **\[Taker & Maker]** Authentication
2. **\[Taker]** Send RFQ
3. **\[Maker]** Listen or poll for RFQs
4. **\[Maker]** In response to an RFQ, sign and send a quote
5. **\[Taker]** Poll for the Quotes (market makers' replies to RFQs) and pick the best one
6. **\[Taker]** Sign an execute message for the selected quote

NOTE: to greatly simplify signatures, you may use our [Derive Python Signing SDK](https://pypi.org/project/derive_action_signing/)  (see the Python RFQ example on the next page).

# 0. Constants & Setup

This examples use the following protocol constants, subaccount IDs, leg instruments, etc.

```typescript
import { ethers } from 'ethers';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const PRIVATE_KEY = process.env.OWNER_PRIVATE_KEY as string;
const PROVIDER_URL = 'https://testnet-rpc.derive.xyz/';
const HTTP_ADDRESS = 'https://api-demo.lyra.finance';
const ACTION_TYPEHASH = '0x4d7a9f27c403ff9c0f19bce61d76d82f9aa29f8d6d4b0c5474607d9770d1af17';
const DOMAIN_SEPARATOR = '0x9bcf4dc06df5d8bf23af818d5716491b995020f377d3b7b64c29ed14e3dd1105';
const OPTION_ADDRESS = '0xBcB494059969DAaB460E0B5d4f5c2366aab79aa1';
const RFQ_ADDRESS = '0x4E4DD8Be1e461913D9A5DBC4B830e67a8694ebCa'

const PROVIDER = new ethers.JsonRpcProvider(PROVIDER_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, PROVIDER);
const encoder = ethers.AbiCoder.defaultAbiCoder();

const subaccount_id_rfq = 23525
const subaccount_id_maker = 8

const LEG_1_NAME = 'ETH-20240329-2400-C'
const LEG_2_NAME = 'ETH-20240329-2600-C'

// can retreive with public/get_instrument
const LEGS_TO_SUB_ID: any = {
  'ETH-20240329-2400-C': '39614082287924319838483674368',
  'ETH-20240329-2600-C': '39614082373823665758483674368'
}
```

# 1. Authentication (both makers and takers)

In this guide, we'll use REST API for all examples / requests. As such, auth is done over headers as described in  the [Authentication](https://docs.derive.xyz/reference/authentication) section:

```typescript TypeScript
async function signAuthenticationHeader() {
  const timestamp = Date.now().toString();
  const signature = await wallet.signMessage(timestamp);
  return {
      "X-LyraWallet": wallet.address,
      "X-LyraTimestamp": timestamp,
      "X-LyraSignature": signature
  };
}
```

# 2. Send RFQ

Takers send RFQs, which do *not* specify the direction of execution.

```typescript
function createRfqObject(): object {
  const rfq = {
    subaccount_id: subaccount_id_rfq,
    // NOTE: legs MUST be sorted by instrument_name where sorting key is instrument_name
    legs: [
      {
        instrument_name: LEG_1_NAME,
        amount: '3',
        direction: 'buy'
      },
      {
        instrument_name: LEG_2_NAME,
        amount: '3',
        direction: 'sell'
      }
    ],
  };
  return rfq;
}

async function sendRfq(rfq: object) {
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/send_rfq`, rfq, {headers: authHeader})
  return resp.data.result;
}
```

# 3. Listen or poll for RFQs

Note that market maker wallets must be approved by the support team in order to get access to the maker API. To get live RFQs, one can use either the polling endpoint (`poll_rfqs`) or the `{wallet}.rfqs` channel. Below example shows uses the `poll_rfqs` endpoint.

```typescript
// NOTE: types defined in this example are just for illustration and are not robust,
// use the docs to get more info such as allowed enum values, etc.
type RfqLeg = {
  instrument_name: string,
  amount: string,
  direction: 'buy' | 'sell'
}

type RfqResponse = {
  subaccount_id: number,
  creation_timestamp: number,
  last_update_timestamp: number,
  status: string,
  cancel_reason: string,
  rfq_id: string,
  valid_until: number,
  legs: Array<RfqLeg>
}

async function pollRfq() : Promise<RfqResponse> {
  // account owner of the subaccount_id must be approved to act as RFQ maker
  // can also use {wallet}.rfqs channel to listen for RFQs (same response format)
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/poll_rfqs`, {subaccount_id: subaccount_id_maker, status: 'open'}, {headers: authHeader})
  // for the sake of example just return the latest RFQ
  return resp.data.result.rfqs[0]
}
```

# 4. In response to an RFQ, sign and send a quote

When the execution occurs, the `RfqModule.sol` contract will validate the maker and taker signatures, effectively ensuring that the two parties "agreed" on all of the leg names, amounts and prices.

Quotes can be sent in either `buy` or `sell` direction. The `buy` quote will execute the legs in the same direction as the legs' definition (e.g. a `buy` quote on a `sell` call option leg will be executed as a short call). A `sell` quote flips the direction of every leg in the RFQ. Note that the quote direction affects signature logic, because the contracts work with *signed* leg amounts.

```typescript
type QuoteLeg = {
  instrument_name: string,
  amount: string,
  direction: 'buy' | 'sell',
  price: string
}

type EncodedLeg = [string, string, ethers.BigNumberish, ethers.BigNumberish]

function encodePricedLegs(legs: Array<QuoteLeg>, direction: 'buy' | 'sell'): Array<EncodedLeg> {
  const dirSign = BigInt(direction === 'buy' ? 1 : -1);
  const encoded_legs : Array<EncodedLeg> = legs.map((leg) => {
    const subid = LEGS_TO_SUB_ID[leg.instrument_name];
    const legSign = BigInt(leg.direction === 'buy' ? 1 : -1);
    const signedAmount = ethers.parseUnits(leg.amount, 18) * legSign * dirSign;
    return [OPTION_ADDRESS, subid, ethers.parseUnits(leg.price, 18), signedAmount];
  });
  return encoded_legs;
}

function encodeQuoteData(encoded_legs: Array<EncodedLeg>, max_fee: string): string {
  const rfqData = [ethers.parseUnits(max_fee, 18), encoded_legs];
  const QuoteDataABI = ['(uint,(address,uint,uint,int)[])'];
  const encodedData = encoder.encode(QuoteDataABI, [rfqData]);
  const hashedData = ethers.keccak256(Buffer.from(encodedData.slice(2), 'hex'));
  return hashedData;
}

function signAction(action: any, actionData: string) {
  const action_hash = ethers.keccak256(
    encoder.encode(
      ['bytes32', 'uint256', 'uint256', 'address', 'bytes32', 'uint256', 'address', 'address'],
      [
        ACTION_TYPEHASH,
        action.subaccount_id,
        action.nonce,
        RFQ_ADDRESS,
        actionData,
        action.signature_expiry_sec,
        wallet.address,
        action.signer
      ]
    )
  );
  action.signature = wallet.signingKey.sign(
    ethers.keccak256(Buffer.concat([
      Buffer.from("1901", "hex"),
      Buffer.from(DOMAIN_SEPARATOR.slice(2), "hex"),
      Buffer.from(action_hash.slice(2), "hex")
    ]))
  ).serialized;
}

function signQuote(quote: any) {
  const encoded_legs = encodePricedLegs(quote.legs, quote.direction);
  const quoteData = encodeQuoteData(encoded_legs, quote.max_fee);
  signAction(quote, quoteData)
}

function createQuoteObject(rfq_response: RfqResponse, direction: 'buy' | 'sell') : object {
  const pricedLegs: Array<any> = rfq_response.legs;
  pricedLegs[0].price = direction == 'buy' ? '160' : '180';
  pricedLegs[1].price = direction == 'buy' ? '70' : '50';
  return {
    subaccount_id: subaccount_id_maker,
    rfq_id: rfq_response.rfq_id,
    legs: pricedLegs,
    direction: direction,
    max_fee: '10',
    nonce: Number(`${Date.now()}${Math.round(Math.random() * 999)}`),
    signer: wallet.address,
    signature_expiry_sec: Math.floor(Date.now() / 1000 + 350),
    signature: "filled_in_below"
  };
}

async function sendQuote(rfq_response: RfqResponse, direction: 'buy' | 'sell') {
  const quote = createQuoteObject(rfq_response, direction);
  signQuote(quote);
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/send_quote`, quote, {headers: authHeader})
  return resp.data.result;
}
```

# 5. Poll for the Quotes and pick the best one

Takers can poll the quotes, and use the polled object's fields to sign an execute message in the next step.

```typescript
type QuoteResultPublicSchema = {
  cancel_reason: string;
  creation_timestamp: number;
  direction: 'buy' | 'sell';
  last_update_timestamp: number;
  legs: Array<QuoteLeg>;
  legs_hash: string;
  liquidity_role: 'maker' | 'taker';
  quote_id: string;
  rfq_id: string;
  status: string;
  subaccount_id: number;
  tx_hash: string | null;
  tx_status: string | null;
}

async function pollQuotes(rfq_id: string): Promise<Array<QuoteResultPublicSchema>> {
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/poll_quotes`, {subaccount_id: subaccount_id_rfq, rfq_id: rfq_id, status: 'open'}, {headers: authHeader})
  return resp.data.result.quotes;
}
```

# 6. Sign an execute message for the selected quote

Signing an execute message is very similar to the quote signing, except the type signatures differ a little:

* Market makers sign `{'max_fee': uint, legs: EncodedLeg[]}`
* Takers sign `{'max_fee': uint, legs_hash: bytes32}`

The `legs_hash` is simply a keccak256-hashed array of the same legs as what market makers sign in their quote. The smart contract ensures that the two parties agreed on the leg amounts / prices etc. by hashing maker's array of legs and comparing it to the `legs_hash`.

```typescript
function encodeExecuteData(encoded_legs: Array<EncodedLeg>, max_fee: string): string {
  const encoder = ethers.AbiCoder.defaultAbiCoder();
  const orderHashABI = ['(address,uint,uint,int)[]'];
  const orderHash = ethers.keccak256(Buffer.from(encoder.encode(orderHashABI, [encoded_legs]).slice(2), 'hex'));
  const ExectuteDataABI = ['bytes32', 'uint'];
  const encodedData = encoder.encode(ExectuteDataABI, [orderHash, ethers.parseUnits(max_fee, 18)]);
  const hashedData = ethers.keccak256(Buffer.from(encodedData.slice(2), 'hex'));
  return hashedData;
}

function signExecute(execute: any) {
  const encoded_legs = encodePricedLegs(execute.legs, execute.direction === 'buy' ? 'sell' : 'buy');
  const executeData = encodeExecuteData(encoded_legs, execute.max_fee);
  signAction(execute, executeData)
}

function createExecuteObject(quote: QuoteResultPublicSchema) : object {
  return {
    subaccount_id: subaccount_id_rfq,
    quote_id: quote.quote_id,
    rfq_id: quote.rfq_id,
    direction: quote.direction === 'buy' ? 'sell' : 'buy',
    max_fee: '10',
    nonce: Number(`${Date.now()}${Math.round(Math.random() * 999)}`),
    signer: wallet.address,
    signature_expiry_sec: Math.floor(Date.now() / 1000 + 350),
    legs: quote.legs,
    signature: "filled_in_below"
  }
}

async function sendExecute(quote: QuoteResultPublicSchema) {
  const execute = createExecuteObject(quote);
  signExecute(execute);
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/execute_quote`, execute, {headers: authHeader})
  return resp.data.result;
}
```

## Putting it all together

Below is an example of the end-to-end RFQ flow, from creating RFQs, to signing maker quotes, to executing them. For illustration purposes the same account is used (the account owns two different subaccounts).

```typescript
import { ethers } from 'ethers';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const PRIVATE_KEY = process.env.OWNER_PRIVATE_KEY as string;
const PROVIDER_URL = 'https://l2-prod-testnet-0eakp60405.t.conduit.xyz';
const HTTP_ADDRESS = 'https://api-demo.lyra.finance';
const ACTION_TYPEHASH = '0x4d7a9f27c403ff9c0f19bce61d76d82f9aa29f8d6d4b0c5474607d9770d1af17';
const DOMAIN_SEPARATOR = '0x9bcf4dc06df5d8bf23af818d5716491b995020f377d3b7b64c29ed14e3dd1105';
const OPTION_ADDRESS = '0xBcB494059969DAaB460E0B5d4f5c2366aab79aa1';
const RFQ_ADDRESS = '0x4E4DD8Be1e461913D9A5DBC4B830e67a8694ebCa'

const PROVIDER = new ethers.JsonRpcProvider(PROVIDER_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, PROVIDER);
const encoder = ethers.AbiCoder.defaultAbiCoder();

const subaccount_id_rfq = 23525
const subaccount_id_maker = 8

const LEG_1_NAME = 'ETH-20240329-2400-C'
const LEG_2_NAME = 'ETH-20240329-2600-C'

// can retreive with public/get_instrument
const LEGS_TO_SUB_ID: any = {
  'ETH-20240329-2400-C': '39614082287924319838483674368',
  'ETH-20240329-2600-C': '39614082373823665758483674368'
}

async function signAuthenticationHeader() {
  const timestamp = Date.now().toString();
  const signature = await wallet.signMessage(timestamp);
  return {
      "X-LyraWallet": wallet.address,
      "X-LyraTimestamp": timestamp,
      "X-LyraSignature": signature
  };
}

// Schemas

type RfqLeg = {
  instrument_name: string,
  amount: string,
  direction: 'buy' | 'sell'
}

type QuoteLeg = {
  instrument_name: string,
  amount: string,
  direction: 'buy' | 'sell',
  price: string
}

type RfqResponse = {
  subaccount_id: number,
  creation_timestamp: number,
  last_update_timestamp: number,
  status: string,
  cancel_reason: string,
  rfq_id: string,
  valid_until: number,
  legs: Array<RfqLeg>
}

type QuoteResultPublicSchema = {
  cancel_reason: string;
  creation_timestamp: number;
  direction: 'buy' | 'sell';
  last_update_timestamp: number;
  legs: Array<QuoteLeg>;
  legs_hash: string;
  liquidity_role: 'maker' | 'taker';
  quote_id: string;
  rfq_id: string;
  status: string;
  subaccount_id: number;
  tx_hash: string | null;
  tx_status: string | null;
}

function createRfqObject(): object {
  const rfq = {
    subaccount_id: subaccount_id_rfq,
    // NOTE: legs MUST be sorted by instrument_name where sorting key is instrument_name
    legs: [
      {
        instrument_name: LEG_1_NAME,
        amount: '3',
        direction: 'buy'
      },
      {
        instrument_name: LEG_2_NAME,
        amount: '3',
        direction: 'sell'
      }
    ],
  };
  return rfq;
}

function createQuoteObject(rfq_response: RfqResponse, direction: 'buy' | 'sell') : object {
  const pricedLegs: Array<any> = rfq_response.legs;
  pricedLegs[0].price = direction == 'buy' ? '160' : '180';
  pricedLegs[1].price = direction == 'buy' ? '70' : '50';
  return {
    subaccount_id: subaccount_id_maker,
    rfq_id: rfq_response.rfq_id,
    legs: pricedLegs,
    direction: direction,
    max_fee: '10',
    nonce: Number(`${Date.now()}${Math.round(Math.random() * 999)}`),
    signer: wallet.address,
    signature_expiry_sec: Math.floor(Date.now() / 1000 + 350),
    signature: "filled_in_below"
  };
}

function createExecuteObject(quote: QuoteResultPublicSchema) : object {
  return {
    subaccount_id: subaccount_id_rfq,
    quote_id: quote.quote_id,
    rfq_id: quote.rfq_id,
    direction: quote.direction === 'buy' ? 'sell' : 'buy',
    max_fee: '10',
    nonce: Number(`${Date.now()}${Math.round(Math.random() * 999)}`),
    signer: wallet.address,
    signature_expiry_sec: Math.floor(Date.now() / 1000 + 350),
    legs: quote.legs,
    signature: "filled_in_below"
  }
}

// Getters / Polling

async function pollRfq() : Promise<RfqResponse> {
  // account owner of the subaccount_id must be approved to act as RFQ maker
  // can also use {wallet}.rfqs channel to listen for RFQs (same response format)
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/poll_rfqs`, {subaccount_id: subaccount_id_maker, status: 'open'}, {headers: authHeader})
  console.log(`found ${resp.data.result.rfqs.length} RFQs`)
  return resp.data.result.rfqs[0]
}

async function pollQuotes(rfq_id: string): Promise<Array<QuoteResultPublicSchema>> {
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/poll_quotes`, {subaccount_id: subaccount_id_rfq, rfq_id: rfq_id, status: 'open'}, {headers: authHeader})
  return resp.data.result.quotes;
}

// Signatures and Encoding

function signAction(action: any, actionData: string) {
  const action_hash = ethers.keccak256(
    encoder.encode(
      ['bytes32', 'uint256', 'uint256', 'address', 'bytes32', 'uint256', 'address', 'address'],
      [
        ACTION_TYPEHASH,
        action.subaccount_id,
        action.nonce,
        RFQ_ADDRESS,
        actionData,
        action.signature_expiry_sec,
        wallet.address,
        action.signer
      ]
    )
  );
  action.signature = wallet.signingKey.sign(
    ethers.keccak256(Buffer.concat([
      Buffer.from("1901", "hex"),
      Buffer.from(DOMAIN_SEPARATOR.slice(2), "hex"),
      Buffer.from(action_hash.slice(2), "hex")
    ]))
  ).serialized;
}

type EncodedLeg = [string, string, ethers.BigNumberish, ethers.BigNumberish]

function encodePricedLegs(legs: Array<QuoteLeg>, direction: 'buy' | 'sell'): Array<EncodedLeg> {
  const dirSign = BigInt(direction === 'buy' ? 1 : -1);
  const encoded_legs : Array<EncodedLeg> = legs.map((leg) => {
    const subid = LEGS_TO_SUB_ID[leg.instrument_name];
    const legSign = BigInt(leg.direction === 'buy' ? 1 : -1);
    const signedAmount = ethers.parseUnits(leg.amount, 18) * legSign * dirSign;
    return [OPTION_ADDRESS, subid, ethers.parseUnits(leg.price, 18), signedAmount];
  });
  return encoded_legs;
}

function encodeQuoteData(encoded_legs: Array<EncodedLeg>, max_fee: string): string {
  const rfqData = [ethers.parseUnits(max_fee, 18), encoded_legs];
  const QuoteDataABI = ['(uint,(address,uint,uint,int)[])'];
  const encodedData = encoder.encode(QuoteDataABI, [rfqData]);
  const hashedData = ethers.keccak256(Buffer.from(encodedData.slice(2), 'hex'));
  return hashedData;
}


function signQuote(quote: any) {
  const encoded_legs = encodePricedLegs(quote.legs, quote.direction);
  const quoteData = encodeQuoteData(encoded_legs, quote.max_fee);
  signAction(quote, quoteData)
}

function encodeExecuteData(encoded_legs: Array<EncodedLeg>, max_fee: string): string {
  const encoder = ethers.AbiCoder.defaultAbiCoder();
  const orderHashABI = ['(address,uint,uint,int)[]'];
  const orderHash = ethers.keccak256(Buffer.from(encoder.encode(orderHashABI, [encoded_legs]).slice(2), 'hex'));
  const ExectuteDataABI = ['bytes32', 'uint'];
  const encodedData = encoder.encode(ExectuteDataABI, [orderHash, ethers.parseUnits(max_fee, 18)]);
  const hashedData = ethers.keccak256(Buffer.from(encodedData.slice(2), 'hex'));
  return hashedData;
}

function signExecute(execute: any) {
  const encoded_legs = encodePricedLegs(execute.legs, execute.direction === 'buy' ? 'sell' : 'buy');
  const executeData = encodeExecuteData(encoded_legs, execute.max_fee);
  signAction(execute, executeData)
}

// Send API

async function sendRfq(rfq: object) {
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/send_rfq`, rfq, {headers: authHeader})
  return resp.data.result;
}

async function sendQuote(rfq_response: RfqResponse, direction: 'buy' | 'sell') {
  const quote = createQuoteObject(rfq_response, direction);
  signQuote(quote);
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/send_quote`, quote, {headers: authHeader})
  return resp.data.result;
}

async function sendExecute(quote: QuoteResultPublicSchema) {
  const execute = createExecuteObject(quote);
  signExecute(execute);
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/execute_quote`, execute, {headers: authHeader})
  return resp.data.result;
}

// Helpers to check if the RFQ is filled

async function getSubaccount(subaccount_id: number) {
  const resp = await axios.post(`${HTTP_ADDRESS}/private/get_subaccount`, {subaccount_id: subaccount_id}, {headers: await signAuthenticationHeader()})
  return resp.data.result;
}

async function getFilledQuotes() {
  const authHeader = await signAuthenticationHeader();
  const resp = await axios.post(`${HTTP_ADDRESS}/private/get_quotes`, {subaccount_id: subaccount_id_rfq, status: 'filled'}, {headers: authHeader})
  return resp.data.result;
}

async function completeRfq() {
    await sendRfq(createRfqObject())
    const rfq_response = await pollRfq();
    console.log(rfq_response);

    const buy_response = await sendQuote(rfq_response, 'buy');
    console.log(buy_response);

    const sell_response = await sendQuote(rfq_response, 'sell');
    console.log(sell_response);

    const quotes = await pollQuotes(rfq_response.rfq_id);
    console.log(quotes);

    const buyQuote = quotes.find((quote) => quote.direction === 'buy') as QuoteResultPublicSchema;
    console.log(buyQuote);

    const sellQuote = quotes.find((quote) => quote.direction === 'sell') as QuoteResultPublicSchema;
    console.log(sellQuote);

    const executeAsSeller = await sendExecute(buyQuote);
    console.log(executeAsSeller);

    // NOTE optionally execute as buyer instead, but only one side can execute
    // const executeAsBuyer = await sendExecute(sellQuote);
    // console.log(executeAsBuyer);

    console.log(await getSubaccount(subaccount_id_rfq));
    console.log(await getFilledQuotes());
}

completeRfq();

```