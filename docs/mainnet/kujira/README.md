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
peers="9ef0bd43e617127e3978c585437619008ccca263@65.108.229.102:22656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,89757803f40da51678451735445ad40d5b15e059@169.155.45.187:26656,9dc8a19299064e8d5a414a1fc25dd0d12d9871c8@138.201.16.240:30095,780ee91b43bcdced2daebee61996742f6b01b579@138.201.197.119:2000,ecafd5cadaf3526a588550a7bc343ce2670c988d@185.16.39.231:26656,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,f62a0842be95a33b191879c977eed2072e37926b@57.128.20.147:30256,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@95.217.70.62:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,d3427d444b6909529d73025fe32a73dfea7b90d1@148.251.85.115:26656,ffac364ae5a9a730b49f02ba95b11878f76b7043@135.125.189.131:31095,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,b8e8c1738a49cd6143cf83287a5087c2618ebca0@141.95.47.82:30256,2544287899424decd29c659445578a579a500ab2@85.10.200.231:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
