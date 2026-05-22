- [](/docs/)
- Options Trading
- User Data Streams
- Start User Data Stream
**On this page


# Start User Data Stream (USER_STREAM)

## API Description​

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.

## HTTP Request​

POST `/eapi/v1/listenKey`

## Request Weight​

1**

## Request Parameters​

None

## Response Example​

```
{
 "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1",
 "expiration": 1762855900452
}

```
