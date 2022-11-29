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
peers="d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,021974bdbb3108a706e97204434cc606a36e95b8@23.88.69.167:26767,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,7ec6917a0519decec00a9a29f599c4d90ebf3b86@65.21.136.170:51656,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,2428de780659ec556e6b2e2856081bf29d0d9d38@167.235.98.202:26656,9acce7431b335820679fea49e09218687f5e3aa8@95.217.236.61:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
