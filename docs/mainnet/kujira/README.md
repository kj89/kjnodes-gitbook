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
* grpc: https://kujira.grpc.kjnodes.com:443

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

**live-peers** (9)
```bash
peers="4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@134.65.193.158:26656,d87e960e5512e89af70721484617fe72e43dcb29@165.22.199.234:26020,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,ccffabe81f2de8a81e171f93fe1209392bf9993f@65.108.234.59:26656,0a51eaa669fa7ad9ad6a8d19942f324725596f23@65.109.80.92:26656,377510fb7c0ee3cacd1a46dbf13b45a4e1525fa6@51.91.153.78:32011"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
