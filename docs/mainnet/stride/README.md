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

**live-peers** (9)
```
peers="1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,af7229930a59c4d1860fd304a6b2d1c269a18fa4@138.201.8.248:51656,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,d13d51e660dbd89d6660ac9b61957c5e727efdae@135.181.130.145:6000,89dbb2e146a2b3401fb959295babba090aa2f0e9@89.58.7.66:16656,f452fbafd9c5dd0ce7c0ecd6bf2ba413aedb88aa@65.108.229.244:36656,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,da56a252a1ed282f33f9171b18e41390528dbcbd@95.217.170.202:27013,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
