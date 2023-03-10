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

**live-peers** (18)
```bash
peers="935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,9c8826ceeb1254d16856092a50df4fd720910362@50.116.49.237:26656,b1f66cdee3f626faf187f91699d82bfb9e111e42@146.59.81.18:30256,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,0c2e37714b7922b160bce8579eeb444e59802efa@65.108.198.118:11856,d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,cedf10f69de7d77b358964a1b802a15ad79a7c97@74.80.183.130:26655,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
