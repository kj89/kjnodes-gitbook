# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

Website: [https://kujira.app](https://kujira.app)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (9)
```
peers="da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,5ef740383b8a490c1bee7f9e61bf03c43427b182@83.149.102.56:32095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,0743497e30049ac8d59fee5b2ab3a49c3824b95c@198.244.200.196:26656,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
