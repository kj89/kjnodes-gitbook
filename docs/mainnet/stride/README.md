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
peers="ede57d0b0373d95666626f259aa4f030d6660a57@65.109.49.163:36656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,33385960e3a20edbd1bfe0c466d5578dcdf087f3@209.145.56.74:26656,025c055b34da508bf6da83590e29f3a51b935b70@23.88.69.22:28656,32326506894e6afb1ba402adee0d38bb152efa9c@65.109.28.177:26666,b07b6cc0b70f15e20c0125b202b7fbc5680b8836@136.243.78.251:36656,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,27e3200f2b3f83c403ad9dfa09bf83ae73b179b3@149.102.143.220:10173"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
