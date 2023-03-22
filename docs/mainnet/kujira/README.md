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
peers="c62e0701155a690616fcd3a57fa2fda444840561@65.108.76.242:32095,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,c55d35ef908b74c2ddec2f47dbdb4032d7dfbcd4@23.88.69.22:27266,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,ff7a1787ea93a49ece2ee92f601a4c52951278c4@185.119.118.112:2000,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
