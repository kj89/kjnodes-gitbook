# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

Kujira is a Layer 1 protocol built on Cosmos, which can be used for  hosting community-selected projects.

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Wasm**: ON

[Website](https://kujira.app) | [Discord](https://discord.gg/teamkujira) | [Twitter](https://twitter.com/TeamKujira)

## Restake

[Restake with kjnodes](https://restake.app/kujira/kujiravaloper1tnuqj73jfn3724lqz34c27tuv80nv336sadqym) (every day at 08:00, 20:00)
## Public endpoints

* api: [https://kujira.api.kjnodes.com](https://kujira.api.kjnodes.com)
* rpc: [https://kujira.rpc.kjnodes.com](https://kujira.rpc.kjnodes.com)
* grpc: [https://kujira.grpc.kjnodes.com](https://kujira.grpc.kjnodes.com)

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
peers="b12591db8b67f7a78b2834b5c122299fdb6c8deb@65.108.201.154:2060,4ae125f9c9b8e2f1ac83749c2209e26056b97851@65.108.238.103:11856,b802fbfb83d6400639f17f2883f30a46ee6b05ad@51.210.223.185:32095,b80cf7882c8cab4894d41ccd4f5a00406d8b5f7d@146.59.52.48:30095,bd1ec9985e9f3a1fbfbd7be5fa4c926a61cbd403@34.70.228.207:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,26d19e5b3f3a5ebafe827dabca4ef008d9c5e6fd@168.119.15.94:26656,d6f2eee997d108d4fde5683e31d678427376dfce@77.68.27.75:26656,4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
