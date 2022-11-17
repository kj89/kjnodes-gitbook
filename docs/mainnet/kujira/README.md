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

**live-peers** (11)
```
peers="0cb9d54761ca14006daad4442378f2a1335de6ad@65.21.121.118:26656,2840e88816e487a096cca323bc779ad98187e3e4@5.9.72.212:26656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,5ef740383b8a490c1bee7f9e61bf03c43427b182@83.149.102.56:32095,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,610b8e096b4d8f923b1f41f7bdf92d5b63e033dc@162.55.243.82:4060,3d150f6a71caca5607daff69c9049c04c37da64e@51.210.223.186:30095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:13656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
