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
peers="5ef740383b8a490c1bee7f9e61bf03c43427b182@83.149.102.56:32095,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346,fa57c7c253be46ad9f696ee2f2c1d72cbc6a1591@146.59.52.135:31095,413bd0410b649de5070b2fe8356cad356459dc37@65.108.235.165:26656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
