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

**live-peers** (18)
```bash
peers="5d0f0bc1c2d60f1d273165c5c8cefc3965c3d3c9@65.108.233.175:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,377510fb7c0ee3cacd1a46dbf13b45a4e1525fa6@51.91.153.78:32011,f2fe529a8d41ce4beffccb2e00342e74df9ebeca@78.31.71.246:26656,e92b3424ba53c10aefdf9b402f4c03888de96c2e@45.77.61.157:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,35af92154fdb2ac19f3f010c26cca9e5c175d054@65.108.238.61:27656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,0743497e30049ac8d59fee5b2ab3a49c3824b95c@198.244.200.196:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,bd2821b2dc8b928946026caf3e9bd1e7a0013a61@145.239.10.46:13656,a0927acbf1e931fc16e11e454b328c991e56d3fe@51.89.155.17:44656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
