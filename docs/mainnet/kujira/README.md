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
peers="94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,eb9742d81b436b95e324816794229a9efdaf8ea8@142.132.155.170:26656,ccdd8ee4d8fef171e8c2bfaaa2a535033d4af32b@65.108.135.82:29656,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,a429a1fa5cc1e8757b6bbc3975ecc13e0ab2bf2f@95.217.228.124:11856,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,e2f31b21039c20043ceb849f5f7e0274ba38d2e2@159.203.187.36:26020"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
