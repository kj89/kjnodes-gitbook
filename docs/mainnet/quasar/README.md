# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.0 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quasar](https://explorer.kjnodes.com/quasar)

## Public endpoints

* api: [https://quasar.api.kjnodes.com](https://quasar.api.kjnodes.com)
* rpc: [https://quasar.rpc.kjnodes.com](https://quasar.rpc.kjnodes.com)
* grpc: quasar.grpc.kjnodes.com:48090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quasar.rpc.kjnodes.com:48656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quasar.rpc.kjnodes.com:48659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (20)
```bash
peers="201eb8fc1e84beb4bdce8ae5614c7abb41e32edb@65.109.160.91:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:48656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.124:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.189:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,ff5c236c2d7d3a9688b00d27ea9838eb54700aac@51.89.7.235:26647,619fc43aceebc5a9f70c6ea95ad2a94319294a54@141.95.103.138:26656,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,e62ce06e60a986ed04d2e080876a41e3b57a5304@93.190.141.218:26656,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,240c09f5d91d2c252cf29faa1a88aebd563d2561@57.128.144.247:26656,49b72b4c79d589955a5004797b45ee306da6a889@143.42.237.237:26656,298e0e1faf8a5da43514cc2908d2908658e732a0@38.146.3.148:18256,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,83f4a463b8130b9ccf3bc96f80ac213a9a856dfc@34.27.99.121:26656,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,b5d43d295863db6675d07877878b2d7b47cb2ae5@157.90.36.48:26966"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
