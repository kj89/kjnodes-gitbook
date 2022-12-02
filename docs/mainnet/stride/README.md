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

**live-peers** (11)
```
peers="d3373b407aff1cf04a24cd55dad288f4886888a2@185.213.26.129:26656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,5b193f60f2b8378c42d7d30bd70d45de2b70730e@65.108.202.143:16656,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.67:26656,7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,e296d262e432daa021cf87a1cdd7eea249d59698@89.58.61.72:26656,5676fee42425893f90d0724994661d172230587a@188.165.252.51:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
