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
peers="d11f867df7e498de0835e2d1b5bc34334c7337d1@65.109.31.114:2490,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.189:26656,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,52c1443f58363c147393d7637116e8a0724329d4@51.89.7.235:26647,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856,1369d544be2680e031b57f30a8d18cbe8b17a8ef@54.38.73.121:26656,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.193.11:26656,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,4a95d1523814b34c2469e62461d67b8ccef2ab02@34.27.99.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
