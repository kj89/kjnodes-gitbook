# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.6.4 | **Wasm**: ON

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
peers="177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,5ef740383b8a490c1bee7f9e61bf03c43427b182@83.149.102.56:32095,610b8e096b4d8f923b1f41f7bdf92d5b63e033dc@162.55.243.82:4060,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:13656,a429a1fa5cc1e8757b6bbc3975ecc13e0ab2bf2f@95.217.228.124:11856,beb3329e969ae64d97c276f0ed0a1773ebdf61dc@146.19.24.142:26656,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,94b124a422113f1871c3ea750097842004e4a095@18.222.185.33:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
