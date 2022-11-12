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
peers="1387946c04bceb472113f657f55f670f71709230@65.108.4.188:12256,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,06c309d890fe6a1e7d2ac0a600ab077d1e793e18@51.195.89.43:10156,b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656,9acce7431b335820679fea49e09218687f5e3aa8@95.217.236.61:26656,025c055b34da508bf6da83590e29f3a51b935b70@23.88.69.22:28656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
