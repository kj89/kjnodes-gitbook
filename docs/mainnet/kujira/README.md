# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.6 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: kujira.grpc.kjnodes.com:11390

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:11356
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:11359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (11)
```bash
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,56598f1d3153b4368a0d9ac083b379b09ae2b531@162.19.95.239:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11356,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,e244225f4ac1c401a913a8e48f8a715a8c61fe17@168.119.161.36:26635,08dae6e7a7b2da2697ed3dd982b57fab2c3cf64b@5.75.178.169:26635,07613f60a16bddef926715bb11fa7009521c1ef4@195.201.245.120:26656,b3c01f34ce7de9a0f74e1b45e8ebda4af293c5c7@31.17.205.204:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
