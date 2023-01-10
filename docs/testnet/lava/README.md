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

**live-peers** (21)
```bash
peers="2d3fd8c1021bc37dc78b04a944b74ee0e1359774@75.119.156.187:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,d64aa8f4d864daac54639cd1fdebbf4c464ba4f1@5.75.235.206:26656,d5e983cb8ad86a3d7d6dd0bc91e969cc8d416c7c@217.76.58.177:26656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@54.194.240.43:26656,39fe8916ab25530cba837f501beb0f2535a35642@84.46.246.109:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,1cfea692eeabae3c4382d62179278e88ebd8d447@164.92.223.212:26656,97a7c2941a5875ce518f4775b841ff3b888c82d4@65.108.129.104:21656,cab9892dd329b0308af3b8364356757f874d17fe@65.109.87.135:13656,897d44b1cb6633539cf51261f6629a9d5664eb9b@159.69.72.247:11656,2db2e00432fc950fa2afa03a84288a437fc1c305@2.58.82.212:26656,4d75d09b547792ab32a529f452580546e6ce9420@65.108.69.68:27262,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
