# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.8.4 | **Wasm**: ON

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
peers="5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.238:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,e92b3424ba53c10aefdf9b402f4c03888de96c2e@45.77.61.157:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
