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
peers="1bf81f0f4e35769d075300bc46e3998d63bf2bb2@135.181.210.186:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,b5d43d295863db6675d07877878b2d7b47cb2ae5@157.90.36.48:26966,bbf8c1562c20726a436f1c1476ad49e560ca179b@51.89.190.33:26656,58a4943a150cc77ab77ded222c44b23548ee702a@146.59.81.23:26667,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,298e0e1faf8a5da43514cc2908d2908658e732a0@38.146.3.148:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.189:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
