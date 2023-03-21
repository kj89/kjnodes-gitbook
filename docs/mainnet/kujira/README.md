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

**live-peers** (19)
```bash
peers="da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,4af5ea231c2fe1ca8174fb627e65bc09564f313b@45.143.196.110:11856,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,263b9b4525e3e568e293677daa0d64d3087815f0@65.108.106.156:26676,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.14:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,0a51eaa669fa7ad9ad6a8d19942f324725596f23@65.109.80.92:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
