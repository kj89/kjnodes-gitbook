# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (20)
```bash
peers="0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.82.78:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,f62a0842be95a33b191879c977eed2072e37926b@57.128.20.147:30256,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,5ae54af5483ff090e57a51f9f3568490373e2419@135.181.26.211:26656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,b690b0e6a904fc0172ef1eccc07bea9f48f4e454@141.94.73.39:53756,1a781f294b8c30ab0b4e54494359263e9b389ebb@141.94.219.133:11756,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,f2fe529a8d41ce4beffccb2e00342e74df9ebeca@78.31.71.246:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
