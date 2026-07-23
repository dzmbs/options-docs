> ## Documentation Index
> Fetch the complete documentation index at: https://docs.deribit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multicast Subscription Guide

> Step-by-step procedure to subscribe and unsubscribe from Starbase UDP multicast market data feeds, including channel discovery and IGMP setup.

<Info>
  **Multicast & networking support**: For detailed multicast or networking questions, contact [colo-support@coinbase.com](mailto:colo-support@coinbase.com).
</Info>

## Quick Start Guide

<Note>
  The IP address `224.0.12.234` used in the examples below is illustrative only. Replace it with the actual multicast group address for your feed. See the full list of available feeds on the [Multicast Channels](https://docs.deribit.com/starbase/multicast-channels) page.
</Note>

### For Colo Customers (Direct Connection)

Best for customers connected via active/backup bond interfaces.

1. **Identify your interface:** Usually `bond0`.
2. **Subscribe:** Run the join command on your server:
   ```
   smcroutectl join bond0 <mcast-address>
   ```
3. **Verify:** Check your local interface for incoming traffic.
4. **Unsubscribe:** Run the leave command:
   ```
   smcroutectl leave bond0 <mcast-address>
   ```

### For Cross-Connect Customers (BGP/PIM)

Best for customers using routing devices with BGP peering.

1. **Configure PIM RP:** Set the Rendezvous Point on your routing device:
   ```
   RP ADDRESS: 195.138.37.160
   ```
2. **Enable PIM:** Ensure `ip pim sparse-mode` is active on all interfaces facing the Starbase Gateway.
3. **Subscribe:** Send an IGMPv3 membership report from your server:
   ```
   smcroutectl join [interface] <mcast-address>
   ```
4. **Verify:** Check the PIM neighbor status and mroute table on your switch.

## Configuration Reference

### Verification Commands

To confirm the ASM tree is building correctly toward the RP:

| Command                               | Purpose                                                |
| ------------------------------------- | ------------------------------------------------------ |
| `show ip pim neighbor`                | Check neighbors (ensure status is "sparse")            |
| `show ip pim rp`                      | Check RP (should point to `195.138.37.160`)            |
| `show ip mroute`                      | Check routing (verify outgoing interface is correct)   |
| `show ip pim rp-hash <mcast-address>` | Confirm RP mapping (should return `195.138.37.160`)    |
| `show ip mroute <mcast-address>`      | Check shared tree (\*, G) entry pointing toward the RP |


## Related topics

- [Multicast Retransmit Gateway](/starbase/retransmit-gateway.md)
- [Market Data Collection](/articles/market-data-collection-best-practices.md)
- [Multicast Channels](/starbase/multicast-channels.md)
- [Quickstart Guide](/articles/deribit-quickstart.md)
- [Security List Request(x) — Production FIX API](/fix-api/production/security-list-request.md)
