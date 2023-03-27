# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

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
* grpc: kujira.grpc.kjnodes.com:13090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (19)
```bash
peers="ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,9ef0bd43e617127e3978c585437619008ccca263@65.108.229.102:22656,5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,79ace78a1fb98876c7bcbf8ec54864b740aa76ff@65.108.128.201:11856,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
