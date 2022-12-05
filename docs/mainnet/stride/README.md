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

**live-peers** (10)
```
peers="0559809b9788925f85928f7b518e4315c090b4be@65.108.110.204:26656,f452fbafd9c5dd0ce7c0ecd6bf2ba413aedb88aa@65.108.229.244:36656,021974bdbb3108a706e97204434cc606a36e95b8@23.88.69.167:26767,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,2f6a21a94be87df4c2a2d82683e6ea99b7b6b02b@50.21.173.78:26656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,cc21cd5beebca219107c3cb31a01c21adb76670b@34.79.153.13:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
