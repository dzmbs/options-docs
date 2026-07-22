> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Logout(5) — Production FIX API

> Logout(5) terminates a session on the Deribit production FIX API, describing the proper shutdown sequence and Cancel on Disconnect behavior on exit.

`Logout`(`5`) can be sent by either party in order to terminate a session. The
sending party should always wait for the echo of the logout request before they
close the socket. Closing connections in any other way is considered abnormal
behavior. Nonetheless, if `CancelOnDisconnect`(`9001`) was set at Logon, all
orders will be cancelled at Logout.

### Arguments

| Tag  | Name                     | Type    | Required | Comments                                                                                                                                                                                                      |
| ---- | ------------------------ | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 58   | `text`                   | String  | No       | Free format text string specifying the logout reason. This is ignored by the server                                                                                                                           |
| 9003 | `DontCancelOnDisconnect` | Boolean | No       | If `Y` then it disables `CancelOnDisconnect` for this connection even if `CancelOnDisconnect` was enabled in `Logon`(`A`) or account settings. Default - false(`N`), no changes for `CancelOnDisconnect` flag |


## Related topics

- [private/logout](/api-reference/authentication/private-logout.md)
- [FIX API Overview](/fix-api/production/overview.md)
- [Logon(A)](/fix-api/production/logon.md)
- [Creating a Starbase API Key](/starbase/creating-api-key.md)
- [Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
