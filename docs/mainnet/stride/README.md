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
peers="ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,0f95188872bf59edffb4874ed5593b012e377a0e@65.108.7.120:26656,dc9241e56b67b2d9b39a79f4aa9dc432d78c1dbc@195.3.223.204:10156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656,1387946c04bceb472113f657f55f670f71709230@65.108.4.188:12256,b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,1d1b344c4c17893903a881798f0edb2fa85df949@64.227.34.242:26656,d3373b407aff1cf04a24cd55dad288f4886888a2@185.213.26.129:26656,5b20fde898024d705cba65ba9a9352f8a4a2d8d2@142.132.244.107:27012"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
