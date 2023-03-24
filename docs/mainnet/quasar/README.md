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
peers="bcbc915effeb5e1f4e96670fd68d20a08ad4efa1@65.108.138.80:18256,2b01cb4d5c2108b20788aad68e11149899f170f4@99.80.59.242:26656,201eb8fc1e84beb4bdce8ae5614c7abb41e32edb@65.109.160.91:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:48656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.124:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,ff5c236c2d7d3a9688b00d27ea9838eb54700aac@51.89.7.235:26647,b5d43d295863db6675d07877878b2d7b47cb2ae5@157.90.36.48:26966,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,e62ce06e60a986ed04d2e080876a41e3b57a5304@93.190.141.218:26656,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,240c09f5d91d2c252cf29faa1a88aebd563d2561@57.128.144.247:26656,298e0e1faf8a5da43514cc2908d2908658e732a0@38.146.3.148:18256,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,619fc43aceebc5a9f70c6ea95ad2a94319294a54@141.95.103.138:26656,83f4a463b8130b9ccf3bc96f80ac213a9a856dfc@34.27.99.121:26656,f2e7f8af9e5f72bcde83a8bc0ca05aded6d51a5e@103.180.28.199:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
