> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a Starbase API Key

> Create Starbase API keys — add team members, pick Starbase-specific scopes, and generate the credentials required for gateway login and access.

Starbase API keys are created through the **Starbase** section of the Account Panel (not the API section). The creation flow is otherwise the same as standard Deribit API keys, but with a different set of available scopes and a required member setup step.

<Warning>
  The Starbase section is only visible after your account has been authorized by a Deribit admin. If you do not see it in the dropdown, contact [support@deribit.com](mailto:support@deribit.com).
</Warning>

<Warning>
  Before creating a Starbase API key, you must first add at least one member. Only main accounts can configure members. API key creation is scoped to a member.
</Warning>

<Note>
  Starbase API key management is a sensitive operation. If your account has Two-Factor Authentication (2FA) enabled, you will be prompted for a security key confirmation. See [Security Keys](/articles/security-keys) for details.
</Note>

## Front-end interface

<Steps>
  <Step title="Navigate to the Starbase Section">
    Head to the **Starbase** tab inside the top right Account Panel.

    The Starbase section is separate from the standard **API** section. Make sure you are in the correct tab.

    <img src="https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/starbase_tab.png?fit=max&auto=format&n=tO0Fri3Xhug1I2Vk&q=85&s=e3a4acdcc5ef7947f66e36ab782074fb" alt="Starbase Section" width="568" height="1154" data-path="starbase/starbase_tab.png" />
  </Step>

  <Step title="Add a Member">
    Before you can create an API key, you must add a member. Click **Add Member** and fill in:

    * **Member Name**: a label for this member (e.g. `New member`)
    * **Accounts**: select which accounts (main account and/or subaccounts) this member should have access to

          <img src="https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/add_member.png?fit=max&auto=format&n=tO0Fri3Xhug1I2Vk&q=85&s=04ba4d008f3ae0fb081fae8ad8c95b2d" alt="Starbase Members List" width="2482" height="730" data-path="starbase/add_member.png" />

    Click **Add Member** to open the dialog:

    <img src="https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/add_member_modal.png?fit=max&auto=format&n=tO0Fri3Xhug1I2Vk&q=85&s=1b4e0be16d9954c0f7739004428c9c18" alt="Add Member Dialog" width="976" height="918" data-path="starbase/add_member_modal.png" />

    Once saved, the member will appear in the Starbase member list.

    <Note>
      A Member is a Starbase-specific concept that groups one or more portfolios (accounts/subaccounts) into a single trading participant. See [Account Model](/starbase/account-model) for a full explanation.
    </Note>
  </Step>

  <Step title="Create a New API Key">
    With a member selected, press **Add new key** to open the key creation dialog.

    Provide an optional **Name** for the key, then select one or more scopes from the following:

    | Scope               | Description                                                                                                                |
    | ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
    | **FIX Drop Copy**   | Receive a consolidated drop copy of all activity on the portfolio via the [FIX Drop Copy API](/starbase/fix-drop-copy-api) |
    | **SBE Order Entry** | Submit, amend, and cancel orders via the [Simple Binary Encoding (SBE) Order Entry API](/starbase/binary-api-reference)    |
    | **REST**            | Access REST endpoints (portfolio management, cancel all, etc.)                                                             |

    <Note>
      Multicast market data and the retransmit API are unauthenticated — no API key or scope is required to subscribe to them.
    </Note>

    <img src="https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/starbase_api_key.png?fit=max&auto=format&n=tO0Fri3Xhug1I2Vk&q=85&s=dfbc42e906239bfff26854c18b765dca" alt="Create API Key Dialog" width="1838" height="792" data-path="starbase/starbase_api_key.png" />

    Click **Create API Key** to generate the key.
  </Step>

  <Step title="Save Your Credentials">
    Once created, you will receive a **Client ID** and **Client Secret**.

    <img src="https://mintcdn.com/deribit/tO0Fri3Xhug1I2Vk/starbase/starbase_credidentials.png?fit=max&auto=format&n=tO0Fri3Xhug1I2Vk&q=85&s=2f3a88aefd47c68224fe3ce331270680" alt="API Key Created" width="1812" height="450" data-path="starbase/starbase_credidentials.png" />

    <Warning>
      The Client Secret is only shown once when the key is created. Store it securely, as you cannot retrieve it later.
    </Warning>

    For a description of what these credentials are, see the [Client ID and Client Secret](/articles/creating-api-key#client-id) section of the Creating new API key guide.
  </Step>
</Steps>

## API key limits

Each subaccount can have up to **8 Starbase API keys**. Because each gateway connection requires its own API key, plan your key allocation based on the number of gateway connections you intend to maintain.

Starbase API keys use a separate counter from standard Deribit API keys. Starbase API keys do not count toward your standard API key quota, and standard API keys do not count toward your Starbase quota.

## Next steps

<CardGroup cols={2}>
  <Card title="Gateway Connectivity" icon="server" href="/starbase/gateway-connectivity">
    How API keys map to gateway connections and connection rules
  </Card>

  <Card title="Binary API Reference" icon="code" href="/starbase/binary-api-reference">
    SBE protocol structure, message headers, and data types
  </Card>

  <Card title="Placing a New Order" icon="arrow-up-right" href="/starbase/placing-new-order">
    Submit your first order via the SBE Order Entry API
  </Card>

  <Card title="FIX Drop Copy API" icon="copy" href="/starbase/fix-drop-copy-api">
    Consolidated drop copy of all portfolio activity
  </Card>

  <Card title="Session Messages" icon="plug" href="/starbase/session-messages">
    Logon, logout, and heartbeat session message flows
  </Card>

  <Card title="Cancel on Disconnect" icon="link-slash" href="/starbase/cancel-on-disconnect">
    Automatic order cancellation on connection loss
  </Card>
</CardGroup>


## Related topics

- [Creating new API key](/articles/creating-api-key.md)
- [Connectivity & Best Practices](/starbase/connectivity-best-practices.md)
- [Authentication](/articles/authentication.md)
- [Account Model](/starbase/account-model.md)
- [REST Order Gateway Authentication](/starbase/rest-authentication.md)
