# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

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
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,01d708d4124f30700c05c97947ae10231d8755f7@95.217.197.100:26655,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,b2c0dd94ee8d01f27ef0e3683d237e49927aaa1e@51.255.6.114:26656,6cf8b25d99bacca213c1d762e8d9ea21636fea41@178.211.139.222:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,d7c5f6099886bc3b770cdc4cdc16e69d17dc9442@185.249.227.231:28656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,35629bef4cc1a0be69ebd053ff4e16de82970add@5.79.79.80:30095"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
