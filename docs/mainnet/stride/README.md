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
peers="d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,27e3200f2b3f83c403ad9dfa09bf83ae73b179b3@149.102.143.220:10173,af7229930a59c4d1860fd304a6b2d1c269a18fa4@138.201.8.248:51656,cc21cd5beebca219107c3cb31a01c21adb76670b@34.79.153.13:26656,5b20fde898024d705cba65ba9a9352f8a4a2d8d2@142.132.244.107:27012,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,5dbe792854b8f81df6c6fe5b7aa64d60b27f6100@137.184.235.212:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,df1d522512419a563615ed3708abf928f0fc5080@137.184.134.126:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
