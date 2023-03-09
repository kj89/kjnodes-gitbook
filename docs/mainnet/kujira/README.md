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
peers="4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,a9ed3a9256cbabe889b2989ad99a3e7e173c3ffe@108.165.178.242:26655,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,0a51eaa669fa7ad9ad6a8d19942f324725596f23@65.109.80.92:26656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,471518432477e31ea348af246c0b54095d41352c@88.198.131.126:26656,4db916788d45d5454cfe7a68ca02c56996ee6b96@194.163.151.124:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,38e36150df914ec2c9fbaf378ab0e73ada4a3987@95.216.6.111:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
