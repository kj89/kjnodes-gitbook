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
peers="0f95188872bf59edffb4874ed5593b012e377a0e@65.108.7.120:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.187:26656,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,1b4f221c07a7fff994b5e749246c8305927518dd@178.170.47.62:26656,0003bf00c79e8ebd1f31c0f83ad3d181f97f98e9@62.109.17.96:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
