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
peers="d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,ec4f27b82691f44d38b4801889b3b92643bdc5c2@185.144.99.234:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,bffe92095850b08f905f6fde1d4282b4a619a690@5.161.97.148:26656,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,b07b6cc0b70f15e20c0125b202b7fbc5680b8836@136.243.78.251:36656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
