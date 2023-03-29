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
peers="82588f011491c6100d922d133f52fc23460b9231@95.217.91.238:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,58fc044463399f5c2d94a39e3474ea6196dab0bd@65.108.198.118:11856,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@95.217.65.54:26656,de08e6178779ff3b19a8b6d22a05664392cb2b35@185.216.179.205:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,6cceba286b498d4a1931f85e35ea0fa433373057@88.198.128.174:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
