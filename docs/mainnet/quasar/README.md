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
peers="201eb8fc1e84beb4bdce8ae5614c7abb41e32edb@65.109.160.91:18256,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.124:26656,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.189:26656,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
