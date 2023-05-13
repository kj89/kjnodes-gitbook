# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.0 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quasar](https://explorer.kjnodes.com/quasar)

## Public endpoints

* api: [https://quasar.api.kjnodes.com](https://quasar.api.kjnodes.com)
* rpc: [https://quasar.rpc.kjnodes.com](https://quasar.rpc.kjnodes.com)
* grpc: quasar.grpc.kjnodes.com:14890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quasar.rpc.kjnodes.com:14856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quasar.rpc.kjnodes.com:14859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (10)
```bash
peers="a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.189:26656,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,2b01cb4d5c2108b20788aad68e11149899f170f4@99.80.59.242:26656,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,367d65ece0aafd9b46e15b9dd58fe319d7d29550@143.198.172.109:26656,fd0bd2366d5941580042cfc6444b9aea12363764@5.78.95.218:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,52c1443f58363c147393d7637116e8a0724329d4@51.89.7.235:26647,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
