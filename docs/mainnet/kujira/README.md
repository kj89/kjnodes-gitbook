# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/kujira](https://explorer.kjnodes.com/kujira)

## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: [https://kujira.grpc.kjnodes.com](https://kujira.grpc.kjnodes.com)

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
peers="0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,cd11312654b4368dd2097afd468356d03a92cfe6@178.63.184.132:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,8df276d9873c0ab16a911c5f779caa6f121c845e@89.163.145.138:26656,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,5d0f0bc1c2d60f1d273165c5c8cefc3965c3d3c9@65.108.233.175:26656,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,9a725c47c49464facc147fe29fe1751f1ac6ec0e@65.21.238.147:56656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,8d59c2958dfb2f852b201cbaa60743c771ce338b@147.135.45.32:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
