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
peers="ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,ab842aeaf9550e5bdaa0ed9f940c67a37f1f31a2@65.109.92.241:21016,6a6a70719d44dfdaa74a074f017dc1f1ff23da62@146.59.0.123:6000,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,b07b6cc0b70f15e20c0125b202b7fbc5680b8836@136.243.78.251:36656,da56a252a1ed282f33f9171b18e41390528dbcbd@95.217.170.202:27013,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,7ec6917a0519decec00a9a29f599c4d90ebf3b86@65.21.136.170:51656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
