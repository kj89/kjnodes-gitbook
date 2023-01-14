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

**live-peers** (10)
```bash
peers="d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.182:26656,c4737bc4c7705c4bd94ab23d0089bdb1136573ce@159.89.101.239:26020,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,d87e960e5512e89af70721484617fe72e43dcb29@165.22.199.234:26020,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,377510fb7c0ee3cacd1a46dbf13b45a4e1525fa6@51.91.153.78:32011,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,d02fc7c5db5e502bb78ceeb81067ddab5b0cf51a@89.39.104.128:13656,15679999b404a9ee027dc9f5e795d6c4fddb6cee@51.91.152.102:20000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
