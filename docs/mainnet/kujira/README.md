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
peers="5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,f2fe529a8d41ce4beffccb2e00342e74df9ebeca@78.31.71.246:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@136.243.248.190:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,8df276d9873c0ab16a911c5f779caa6f121c845e@89.163.145.138:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,08d426315d8b1b8996f5dd969777c143d27a5f06@142.132.199.211:26655,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,a7e7864f241db457f38d8e5b5b3c3de989dea2fe@66.94.126.62:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,b1f66cdee3f626faf187f91699d82bfb9e111e42@146.59.81.18:30256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
