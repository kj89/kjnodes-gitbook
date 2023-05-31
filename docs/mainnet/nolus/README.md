# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: pirin-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/nolus/nolusvaloper126szq5tqtwrmd4guk4wxejxry4c55507d0vh3g)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/nolus/nolusvaloper126szq5tqtwrmd4guk4wxejxry4c55507d0vh3g) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/nolus](https://explorer.kjnodes.com/nolus)

## Public endpoints

* api: [https://nolus.api.kjnodes.com](https://nolus.api.kjnodes.com)
* rpc: [https://nolus.rpc.kjnodes.com](https://nolus.rpc.kjnodes.com)
* grpc: nolus.grpc.kjnodes.com:14390

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nolus.rpc.kjnodes.com:14356
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nolus.rpc.kjnodes.com:14359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (9)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14356,1703508b2ac11b81378b66fdbdfbc58f84eef2d4@51.89.7.235:26661,488c9ee36fc5ee54e662895dfed5e5df9a5ff2d5@136.243.39.118:26656,b22fcc033291f44aec43d8fc464dbd5bee5394b8@185.162.250.199:26656,21b6e67a9048037f2a6829912c97dd45b99b3900@65.108.105.134:3000,471518432477e31ea348af246c0b54095d41352c@169.155.46.141:26656,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.20:26656,a2b949be71ef0c28f09a41e08f7b868a178622b9@135.125.5.29:55666,7f56b6dc16831d5b417bc7a3106b5529a9aceda8@162.19.95.239:19756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
