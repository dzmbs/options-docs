> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Request(1) — Production FIX API

> TestRequest(1) solicits a Heartbeat response from the counterparty to verify the Deribit production FIX session is responsive during idle connection periods.

The Test `Request`(`1`) message forces a heartbeat from the opposing
application. The opposing application responds with a
[`Heartbeat`(`0`)](/fix-api/production/heartbeat) containing the `TestReqID`(`112`).

### Arguments

| Tag | Name        | Type   | Required | Comments                        |
| --- | ----------- | ------ | -------- | ------------------------------- |
| 112 | `TestReqId` | String | Yes      | Mirrors the original request ID |


## Related topics

- [FIX API Overview](/fix-api/production/overview.md)
- [Request For Positions(AN)](/fix-api/production/request-for-positions.md)
- [Welcome to Deribit API](/index.md)
- [Resend Request(2)](/fix-api/production/resend-request.md)
- [User Request(BE)](/fix-api/production/user-request.md)
