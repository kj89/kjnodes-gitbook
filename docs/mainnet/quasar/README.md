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
peers="6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,1993e3bee8826be9fd617720eebe83f826a8ebcf@51.89.7.235:26647,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,b5d43d295863db6675d07877878b2d7b47cb2ae5@157.90.36.48:26966,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,58a4943a150cc77ab77ded222c44b23548ee702a@146.59.81.23:26667,b76a4b43471c31cd5f251036d8e70e47dadba1e2@158.247.206.39:10000,bae51539de7b7b7ac784b4c7dc0bc6c005b4f593@65.109.115.226:18256,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
