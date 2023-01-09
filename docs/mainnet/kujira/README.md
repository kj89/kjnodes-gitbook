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
peers="4c1f4d9358118cb8917567702c12ca4f31714b32@65.108.132.107:26656,0179a6055fc1e36053facef08766d06186f3cd33@65.21.200.224:11856,3a7733d4b670a672db326bd6e5f8ae37e14a3dbd@138.201.226.227:26656,2840e88816e487a096cca323bc779ad98187e3e4@5.9.72.212:26656,177872437b2a31ebb0fb740ba5bd32b0be99e280@5.79.74.229:31095,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:13656,66778cba932969c95117cf720c1ad820fdc68ff5@65.108.235.34:26656,d30fe390f09f6a1b9633d1ff7d2b786ccf7915ce@164.92.190.6:26656,01cf570d3b08fdb5fe2f307cb485de7a35a3af23@135.148.55.229:11856,129771a48f43b83c6144c7d282ad1da62434cc07@15.204.197.12:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.kujira/config/config.toml
```
