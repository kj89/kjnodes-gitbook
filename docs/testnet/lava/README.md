# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.3 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Public endpoints

* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (17)
```bash
peers="42eb3b0a36574b1c31cdc2d69b3af49d0713cef7@65.109.52.156:6656,14d21ed30ba21b81ad48a7fd5b8651cdd70ecedb@209.97.130.85:16656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,2031e65ee8a13e57d922a14d28d67be0ada21a95@54.194.240.43:26656,3d4e0eecbbe713a42e785ac1e66ac8ad149b2c4d@164.92.120.104:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,46b4d74ffcbf709d5b5e0f9c653355d3d86804cb@45.87.2.247:26656,39fe8916ab25530cba837f501beb0f2535a35642@84.46.246.109:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,6b209fb04491938b4d60b2847340799fbaced19f@38.242.153.36:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,ed966605db2ea740c4b9d98244f50ae456b846de@162.55.245.219:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
