# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: pirin-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


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

**live-peers** (10)
```bash
peers="d3f29b638d089a73651a290c3f2e27b8da663f92@65.109.122.105:60756,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.193.110:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.154:26656,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.20:26656,644a18b23212fb0df14a366bb3e9abd2ab2564c1@194.163.155.84:40656,7f56b6dc16831d5b417bc7a3106b5529a9aceda8@162.19.95.239:19756,e6be58138f6e654ea5a935dd9e1683266312de18@54.37.129.110:3000,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.172:26656,21b6e67a9048037f2a6829912c97dd45b99b3900@65.108.105.134:3000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
