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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095,698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346,98a6a264d2f2f5093d317f09e71036e62aa73906@107.181.235.66:20656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,bed81e8d4243382da745f3e33c1a0d749bfe7ade@185.217.127.128:26656,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
