# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v3.0.0 | **Wasm**: OFF

Website: [https://stride.zone](https://stride.zone)

## Restake

[Restake with kjnodes](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://stride.rpc.kjnodes.com](https://stride.rpc.kjnodes.com)
* api: [https://stride.api.kjnodes.com](https://stride.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:16656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (9)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,e296d262e432daa021cf87a1cdd7eea249d59698@89.58.61.72:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,27e3200f2b3f83c403ad9dfa09bf83ae73b179b3@149.102.143.220:10173,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
