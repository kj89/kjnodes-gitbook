# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: ON

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

**live-peers** (11)
```bash
peers="240c09f5d91d2c252cf29faa1a88aebd563d2561@57.128.144.247:26656,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,bccdc6cb3a0785bf3ee65d98c38bdd62bb843285@141.95.157.139:18256,66e0a7d2c2fc75a91627085d0ac5681a35dfd408@37.252.184.234:26656,1bf81f0f4e35769d075300bc46e3998d63bf2bb2@135.181.210.186:26656,b76a4b43471c31cd5f251036d8e70e47dadba1e2@158.247.206.39:10000,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
