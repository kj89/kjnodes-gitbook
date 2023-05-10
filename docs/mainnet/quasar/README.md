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

**live-peers** (11)
```bash
peers="89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,771659b9205187f9094f894c65d29effa79fdd2c@18.156.191.84:26656,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,6f9e244b6e225241c02b235f700c2b0788da982d@148.113.159.22:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,52c1443f58363c147393d7637116e8a0724329d4@51.89.7.235:26647,201eb8fc1e84beb4bdce8ae5614c7abb41e32edb@65.109.160.91:18256,4399187c748f91d86932d3e530cd16c22c5f616a@199.231.163.42:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
