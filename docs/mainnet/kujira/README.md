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
peers="0cb9d54761ca14006daad4442378f2a1335de6ad@65.21.121.118:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,66c551ebcb68fe343c7e2720593dc47426813a68@93.189.30.101:26656,e751b31b5444ed4a7489a456be805c736756eeb8@195.3.223.19:26656,a9a4c977ec9f4bf907ce4dc74546de166bb40497@51.81.208.63:26656,b8d3a5e5d43d8e18c4ecfd56a8ca46dc3b91bc32@107.181.231.178:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,0743497e30049ac8d59fee5b2ab3a49c3824b95c@198.244.200.196:26656,698529d303400cc4dff026c6c47eb0dc6547b595@95.216.43.190:36346"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.kujira/config/config.toml
```
