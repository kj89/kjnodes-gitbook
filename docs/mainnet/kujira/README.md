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

**live-peers** (17)
```bash
peers="9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,0a03f5dfb5b995647808c4d100e7b98d0526302f@85.214.18.167:26656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
