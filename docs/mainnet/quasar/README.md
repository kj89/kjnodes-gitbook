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

**live-peers** (10)
```bash
peers="6f95ddfd08c07249c4efafb781eb30ca5739b223@65.109.93.44:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,ff8bfc8a197e279810ccb21acdd987dfd6d3eb54@81.0.248.60:18256,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,66e0a7d2c2fc75a91627085d0ac5681a35dfd408@37.252.184.234:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.189:26656,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,240c09f5d91d2c252cf29faa1a88aebd563d2561@57.128.144.247:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
