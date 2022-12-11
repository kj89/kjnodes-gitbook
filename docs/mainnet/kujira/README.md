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
peers="4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,1d85c9f16727584753db78b5b54eedf0ce8de3ed@51.159.16.49:5060,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,da2673cf09dc2c124947827f4cf5e7c17114d504@142.132.202.98:26656,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,0b749a2b1cf85f6a7d5ea6a08dded05a7f9362a4@128.199.128.15:26020,2840e88816e487a096cca323bc779ad98187e3e4@5.9.72.212:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
