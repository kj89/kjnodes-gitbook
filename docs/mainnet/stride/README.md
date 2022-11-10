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
peers="d13d51e660dbd89d6660ac9b61957c5e727efdae@135.181.130.145:6000,1f206c22b2cc8fa06975aa9b6bcf3032eb3a5fae@213.133.102.206:21016,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,04ea9eceee16db90872fee3fbef9ac50a87702c5@185.248.24.29:26656,8cddcfa2ebcd25df7116f18bdbb0b22ae41392a6@65.108.193.133:16656,9acce7431b335820679fea49e09218687f5e3aa8@95.217.236.61:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,fbebe11a12def69c115c25b4bf871bc5976dfe50@65.109.59.118:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
