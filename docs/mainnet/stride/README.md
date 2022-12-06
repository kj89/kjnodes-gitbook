# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v4.0.2 | **Wasm**: OFF

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
peers="8d7d0f32d53467c4d5e8871faf4ec58ea970fed2@157.90.179.182:26456,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,23180f90318d0003a4e8140a1e67407bf874d69d@78.107.234.44:25656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,ec3ab92c9635230e6262fa7d9293452d8130fc12@5.161.99.247:26656,2f6a21a94be87df4c2a2d82683e6ea99b7b6b02b@50.21.173.78:26656,698ecde23465c1d01d02cc364f36426d259ba1f0@192.99.247.170:26656,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
