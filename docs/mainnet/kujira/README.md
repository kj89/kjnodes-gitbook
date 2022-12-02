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

**live-peers** (10)
```
peers="d6d14f99ef25c8ffee6fa4afca40fece0c1ab9fe@107.181.229.154:20656,450e62f04093c283cc7dcf1257a9b2e4893ad545@148.251.85.115:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,935c1065ad23338a5e6a75f08fb650f9f46dbd3e@65.108.201.167:26656,253d2293272a29057a27797a5703f5171c267da1@192.99.15.159:26656,94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,a429a1fa5cc1e8757b6bbc3975ecc13e0ab2bf2f@95.217.228.124:11856"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
