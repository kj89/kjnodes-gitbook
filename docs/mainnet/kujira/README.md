# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

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
peers="a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,377510fb7c0ee3cacd1a46dbf13b45a4e1525fa6@51.91.153.78:32011,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,263b9b4525e3e568e293677daa0d64d3087815f0@65.108.106.156:26676,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
