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
peers="bffe92095850b08f905f6fde1d4282b4a619a690@5.161.97.148:26656,0f95188872bf59edffb4874ed5593b012e377a0e@65.108.7.120:26656,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,a83cd29f4f9a4711346184966f9fb6c80bb658d2@65.108.103.184:21656,05c410efdebfc0638c868dc0d6f9154168d57604@146.19.24.101:26646,b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,c4688bb34164eacacaa374bc7440b87986dd87ac@162.251.235.252:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
