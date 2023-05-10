# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.4-mainnet | **Wasm**: ON

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

**live-peers** (10)
```bash
peers="58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,4a87e847c8fc15812e4d8ce57c43581ab0e7a4dd@95.214.55.100:26256,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,c8b74590ce04f0f7c32b1c668290e00ec7ec275e@148.113.8.63:11856,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
