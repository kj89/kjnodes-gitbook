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
peers="01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,6f3129d01218b939511cccf7e0318bfe872d97c4@65.109.33.181:26656,2840e88816e487a096cca323bc779ad98187e3e4@5.9.72.212:26656,654b718cf71f0c6f187cf0a930cafbde551cd773@217.160.194.176:26656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,04bde8f0af8b79cca27bb9d3f5bde2eb25e6205d@169.155.169.213:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
