> ## Documentation Index
> Fetch the complete documentation index at: https://docs.derive.xyz/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Order [JavaScript]

Before making API calls, make sure to setup and fund you account in the "Getting Started" guide.

Order submission is a "self-custodial" request, a request that is guaranteed to not be alter-able by anyone except you, which means that it must past both:

1. orderbook authentication (steps 1-2)
2. on-chain signature verification (steps 3-4)

> 👍 If you are struggling to encode data correctly, you can use the public/order\_debug endpoint.  The route takes in all raw inputs and returns intermediary outputs shown in the below steps.

## 1. Authenticate

The first step is to login via WebSocket - see the [Authentication](https://docs.derive.xyz/reference/authentication) section for more:

```typescript
async function signAuthenticationHeader(): Promise<{[key: string]: string}> {
  const timestamp = Date.now().toString();
  const signature = await wallet.signMessage(timestamp);  
    return {
      wallet: wallet.address,
      timestamp: timestamp,
      signature: signature,
    };
}

const connectWs = async (): Promise<WebSocket> => {
    return new Promise((resolve, reject) => {
        const ws = new WebSocket(WS_ADDRESS);

        ws.on('open', () => {
            setTimeout(() => resolve(ws), 50);
        });

        ws.on('error', reject);

        ws.on('close', (code: number, reason: Buffer) => {
            if (code && reason.toString()) {
                console.log(`WebSocket closed with code: ${code}`, `Reason: ${reason}`);
            }
        });
    });
};

async function loginClient(wsc: WebSocket) {
    const login_request = JSON.stringify({
        method: 'public/login',
        params: await signAuthenticationHeader(),
        id: Math.floor(Math.random() * 10000)
    });
    wsc.send(login_request);
    await new Promise(resolve => setTimeout(resolve, 2000));
}

```

## 2. Define

See the WebSocket API reference for `private/order` on more param documentation.

The same order can also be sent through REST, see the REST API reference for `private/order` for more info.

```typescript
function defineOrder(): any {
    return {
        instrument_name: OPTION_NAME,
        subaccount_id: subaccount_id,
        direction: "buy",
        limit_price: 310,
        amount: 1,
        signature_expiry_sec: Math.floor(Date.now() / 1000 + 600), // must be >5min from now
        max_fee: "0.01",
        nonce: Number(`${Date.now()}${Math.round(Math.random() * 999)}`), // LYRA nonce format: ${CURRENT UTC MS +/- 1 day}${RANDOM 3 DIGIT NUMBER}
        signer: wallet.address,
        order_type: "limit",
        mmp: false,
        signature: "filled_in_below"
    };
}
```

## 3. Sign

When a fill occurs, this signature will be verified by the on-chain `Matching.sol` contract to ensure that you approved this trade.

```typescript

function encodeTradeData(order: any): string {
  let encoded_data = encoder.encode( // same as "encoded_data" in public/order_debug
  
    ['address', 'uint', 'int', 'int', 'uint', 'uint', 'bool'],
    [
      ASSET_ADDRESS, 
      OPTION_SUB_ID, 
      ethers.parseUnits(order.limit_price.toString(), 18), 
      ethers.parseUnits(order.amount.toString(), 18), 
      ethers.parseUnits(order.max_fee.toString(), 18), 
      order.subaccount_id, order.direction === 'buy'
    ]
  );
  return ethers.keccak256(Buffer.from(encoded_data.slice(2), 'hex')) // same as "encoded_data_hashed" in public/order_debug
}

async function signOrder(order: any) {
    const tradeModuleData = encodeTradeData(order)

    const action_hash = ethers.keccak256(
        encoder.encode(
          ['bytes32', 'uint256', 'uint256', 'address', 'bytes32', 'uint256', 'address', 'address'], 
          [
            ACTION_TYPEHASH, 
            order.subaccount_id, 
            order.nonce, 
            TRADE_MODULE_ADDRESS, 
            tradeModuleData, 
            order.signature_expiry_sec, 
            wallet.address, 
            order.signer
          ]
        )
    ); // same as "action_hash" in public/order_debug

    order.signature = wallet.signingKey.sign(
        ethers.keccak256(Buffer.concat([
          Buffer.from("1901", "hex"), 
          Buffer.from(DOMAIN_SEPARATOR.slice(2), "hex"), 
          Buffer.from(action_hash.slice(2), "hex")
        ]))  // same as "typed_data_hash" in public/order_debug
    ).serialized;
}
```

## 4. Send

You will most likely have more involved listeners, but for example purposes a built-in listener is added into the submitOrder function.

```typescript
async function submitOrder(order: any, ws: WebSocket) {
    return new Promise((resolve, reject) => {
        const id = Math.floor(Math.random() * 1000);
        ws.send(JSON.stringify({
            method: 'private/order',
            params: order,
            id: id
        }));

        ws.on('message', (message: string) => {
            const msg = JSON.parse(message);
            if (msg.id === id) {
                console.log('Got order response:', msg);
                resolve(msg);
            }
        });
    });
}
```

## Putting it all together

```typescript
import { ethers } from "ethers";
import { WebSocket } from 'ws';
import dotenv from 'dotenv';

dotenv.config();

const PRIVATE_KEY = process.env.OWNER_PRIVATE_KEY as string;
const PROVIDER_URL = 'https://testnet-rpc.derive.xyz/';
const WS_ADDRESS = 'wss://api-demo.lyra.finance/ws';
const ACTION_TYPEHASH = '0x4d7a9f27c403ff9c0f19bce61d76d82f9aa29f8d6d4b0c5474607d9770d1af17';
const DOMAIN_SEPARATOR = '0x9bcf4dc06df5d8bf23af818d5716491b995020f377d3b7b64c29ed14e3dd1105';
const ASSET_ADDRESS = '0xBcB494059969DAaB460E0B5d4f5c2366aab79aa1';
const TRADE_MODULE_ADDRESS = '0x87F2863866D85E3192a35A73b388BD625D83f2be';

const PROVIDER = new ethers.JsonRpcProvider(PROVIDER_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, PROVIDER);
const encoder = ethers.AbiCoder.defaultAbiCoder();
const subaccount_id = 9

const OPTION_NAME = 'ETH-20231027-1500-P'
const OPTION_SUB_ID = '644245094401698393600' // can retreive with public/get_instrument


async function signAuthenticationHeader(): Promise<{[key: string]: string}> {
  const timestamp = Date.now().toString();
  const signature = await wallet.signMessage(timestamp);  
    return {
      wallet: wallet.address,
      timestamp: timestamp,
      signature: signature,
    };
}

const connectWs = async (): Promise<WebSocket> => {
    return new Promise((resolve, reject) => {
        const ws = new WebSocket(WS_ADDRESS);

        ws.on('open', () => {
            setTimeout(() => resolve(ws), 50);
        });

        ws.on('error', reject);

        ws.on('close', (code: number, reason: Buffer) => {
            if (code && reason.toString()) {
                console.log(`WebSocket closed with code: ${code}`, `Reason: ${reason}`);
            }
        });
    });
};

async function loginClient(wsc: WebSocket) {
    const login_request = JSON.stringify({
        method: 'public/login',
        params: await signAuthenticationHeader(),
        id: Math.floor(Math.random() * 10000)
    });
    wsc.send(login_request);
    await new Promise(resolve => setTimeout(resolve, 2000));
}

function defineOrder(): any {
    return {
        instrument_name: OPTION_NAME,
        subaccount_id: subaccount_id,
        direction: "buy",
        limit_price: 310,
        amount: 1,
        signature_expiry_sec: Math.floor(Date.now() / 1000 + 600), // must be >5min from now
        max_fee: "0.01",
        nonce: Number(`${Date.now()}${Math.round(Math.random() * 999)}`), // LYRA nonce format: ${CURRENT UTC MS +/- 1 day}${RANDOM 3 DIGIT NUMBER}
        signer: wallet.address,
        order_type: "limit",
        mmp: false,
        signature: "filled_in_below"
    };
}

function encodeTradeData(order: any): string {
  let encoded_data = encoder.encode( // same as "encoded_data" in public/order_debug
    ['address', 'uint', 'int', 'int', 'uint', 'uint', 'bool'],
    [
      ASSET_ADDRESS, 
      OPTION_SUB_ID, 
      ethers.parseUnits(order.limit_price.toString(), 18), 
      ethers.parseUnits(order.amount.toString(), 18), 
      ethers.parseUnits(order.max_fee.toString(), 18), 
      order.subaccount_id, order.direction === 'buy']
    );
  return ethers.keccak256(Buffer.from(encoded_data.slice(2), 'hex')) // same as "encoded_data_hashed" in public/order_debug
}

async function signOrder(order: any) {
    const tradeModuleData = encodeTradeData(order)

    const action_hash = ethers.keccak256(
        encoder.encode(
          ['bytes32', 'uint256', 'uint256', 'address', 'bytes32', 'uint256', 'address', 'address'], 
          [
            ACTION_TYPEHASH, 
            order.subaccount_id, 
            order.nonce, 
            TRADE_MODULE_ADDRESS, 
            tradeModuleData, 
            order.signature_expiry_sec, 
            wallet.address, 
            order.signer
          ]
        )
    ); // same as "action_hash" in public/order_debug

    order.signature = wallet.signingKey.sign(
        ethers.keccak256(Buffer.concat([
          Buffer.from("1901", "hex"), 
          Buffer.from(DOMAIN_SEPARATOR.slice(2), "hex"), 
          Buffer.from(action_hash.slice(2), "hex")
        ]))  // same as "typed_data_hash" in public/order_debug
    ).serialized;
}

async function submitOrder(order: any, ws: WebSocket) {
    return new Promise((resolve, reject) => {
        const id = Math.floor(Math.random() * 1000);
        ws.send(JSON.stringify({
            method: 'private/order',
            params: order,
            id: id
        }));

        ws.on('message', (message: string) => {
            const msg = JSON.parse(message);
            if (msg.id === id) {
                console.log('Got order response:', msg);
                resolve(msg);
            }
        });
    });
}

async function completeOrder() {
    const ws = await connectWs();
    await loginClient(ws);
    const order = defineOrder();
    await signOrder(order);
    await submitOrder(order, ws);
}

completeOrder();

```

# Solidity Objects

### SignedAction Schema

| Param           | Type      | Description                                                                                                                                 |
| --------------- | --------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| `subaccount_id` | `uint`    | User subaccount id for the action (0 for a new subaccounts when depositing)                                                                 |
| `nonce`         | `uint`    | Unique nonce defined as \<UTC\_timestamp in ms>\<random\_number\_up\_to\_6\_digits> (e.g. 1695836058725001, where 001 is the random number) |
| `module`        | `address` | Deposit module address (see [Protocol Constants](https://docs.derive.xyz/reference/protocol-constants))                                                                   |
| `data`          | `bytes`   | Encoded module data ("TradeModuleData" for orders)                                                                                          |
| `expiry`        | `uint`    | Signature expiry timestamp in sec                                                                                                           |
| `owner`         | `address` | Wallet address of the account owner                                                                                                         |
| `signer`        | `address` | Either owner wallet or session key                                                                                                          |

### TradeModuleData Schema

| Param          | Type      | Description                                                    |
| -------------- | --------- | :------------------------------------------------------------- |
| `asset`        | `address` | Get with `public/get_instrument` (base\_asset\_address)        |
| `subId`        | `uint`    | Sub ID of the asset (Get from public/get\_instrument endpoint) |
| `amount`       | `int`     | Max amount willing to trade                                    |
| `max_fee`      | `uint`    | max fee                                                        |
| `recipient_id` | `uint`    | User subaccount id                                             |
| `isBid`        | `bool`    | Bid or Ask                                                     |