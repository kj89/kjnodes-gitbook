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

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@kujira.rpc.kjnodes.com:13656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@kujira.rpc.kjnodes.com:13659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/kujira/addrbook.json > $HOME/.kujira/config/addrbook.json
```

**live-peers** (10)
```bash
peers="4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.213:26656,c4737bc4c7705c4bd94ab23d0089bdb1136573ce@159.89.101.239:26020,213dbb8301ce1c0f5662a9b723bd613f15e1dd4e@75.119.157.167:30656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,b29969a2384159db8f8052bc118066bd067157c4@85.215.105.19:15602,b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
