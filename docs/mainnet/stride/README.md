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
peers="d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,1b4f221c07a7fff994b5e749246c8305927518dd@178.170.47.62:26656,ef62c7e1bb793ef03481f71697be5ff28e191405@65.108.43.116:56136,d5035bd01baef508402b8649a33afc7b0fd190f1@141.95.72.74:24095,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,b07b6cc0b70f15e20c0125b202b7fbc5680b8836@136.243.78.251:36656,01899588499352857c214c50451c5fa59744ace2@88.99.161.228:26656,dc9241e56b67b2d9b39a79f4aa9dc432d78c1dbc@195.3.223.204:10156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
