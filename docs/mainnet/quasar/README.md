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
peers="fd0bd2366d5941580042cfc6444b9aea12363764@5.78.95.218:26656,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,bbf8c1562c20726a436f1c1476ad49e560ca179b@51.89.190.33:26656,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,97e4468ac589eac505a800411c635b14511a61bb@134.65.195.240:26656,4399187c748f91d86932d3e530cd16c22c5f616a@199.231.163.42:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,b76a4b43471c31cd5f251036d8e70e47dadba1e2@158.247.206.39:10000,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
