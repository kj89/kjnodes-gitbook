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
peers="ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,04ea9eceee16db90872fee3fbef9ac50a87702c5@185.248.24.29:26656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,01899588499352857c214c50451c5fa59744ace2@88.99.161.228:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,a83cd29f4f9a4711346184966f9fb6c80bb658d2@65.108.103.184:21656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
