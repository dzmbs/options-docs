## API key Creation

Please refer to [my api page](/account/my-api) regarding API Key creation.

### Generating an API key

Create an API key on the website before signing any requests. After creating an API key, keep the following information safe:

- API key

- Secret key

- Passphrase

The system returns randomly-generated API keys and SecretKeys. You will need to provide the Passphrase to access the API. We store the salted hash of your Passphrase for authentication. We cannot recover the Passphrase if you have lost it. You will need to create a new set of API key.

### API key permissions

There are three permissions below that can be associated with an API key. One or more permission can be assigned to any key.

- `Read` : Can request and view account info such as bills and order history which need read permission

- `Trade` : Can place and cancel orders, funding transfer, make settings which need write permission

- `Withdraw` : Can make withdrawals

### API key security

To improve security, we strongly recommend clients linked the API key to IP addresses

- Each API key can bind up to 20 IP addresses, which support IPv4/IPv6 and network segment formats.

API keys that are not linked to an IP address and have `trade` or `withdraw` permissions will expire after 14 days of inactivity. (The API key of demo trading will not expire)

- Only when the user calls an API that requires API key authentication will it be considered as the API key is used.

- Calling an API that does not require API key authentication will not be considered used even if API key information is passed in.

- For websocket, only operation of logging in will be considered to have used the API key. Any operation though the connection after logging in (such as subscribing/placing an order) will not be considered to have used the API key. Please pay attention.

Users can get the usage records of the API key with `trade` or `withdraw` permissions but unlinked to any IP address though [Security Center](/account/security).
