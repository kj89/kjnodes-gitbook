# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v2.0.3 | **Wasm**: OFF

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
peers="7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,def346f6f24fbfea94d53021a40dcacba2a2b5e3@38.242.137.34:16656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,23180f90318d0003a4e8140a1e67407bf874d69d@78.107.234.44:25656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,d88e3dd9d94dcb32d908a5d5fa19682dffcd52a5@146.59.47.210:26656,b549e0f88cbebe6cfd3f772937a70640b950fd98@66.172.36.133:28656,8385b1a396afa02e777740277ed7b731e092bf49@185.167.96.231:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
