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

**live-peers** (11)
```bash
peers="bcbc915effeb5e1f4e96670fd68d20a08ad4efa1@65.108.138.80:18256,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,ff8bfc8a197e279810ccb21acdd987dfd6d3eb54@81.0.248.60:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:48656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
