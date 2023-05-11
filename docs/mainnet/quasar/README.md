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
peers="c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,a286b35c9e9626cc7b780120ebe4afa883c059ce@144.76.40.53:18256,bbf8c1562c20726a436f1c1476ad49e560ca179b@51.89.190.33:26656,2b01cb4d5c2108b20788aad68e11149899f170f4@99.80.59.242:26656,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,97e4468ac589eac505a800411c635b14511a61bb@134.65.195.240:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856,0f7eca0da978e4304bb81fa1b9d9a1c87c57f45d@38.146.3.147:18256,982e80ee53fedcb54a19d5f0dba154a0c1aedc2a@3.34.113.161:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
