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
peers="0a51eaa669fa7ad9ad6a8d19942f324725596f23@65.109.80.92:26656,c1a740841a6dc0b56730e975b1a4aa2d8c73b204@65.108.237.233:29656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,4018be5af4189573366762fa168826b4408418db@135.125.188.17:32095,94469c0d109e00e65d62a307f7ab3dc109c01055@65.108.238.104:11856,04bde8f0af8b79cca27bb9d3f5bde2eb25e6205d@169.155.169.213:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
