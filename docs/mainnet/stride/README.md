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
peers="8cddcfa2ebcd25df7116f18bdbb0b22ae41392a6@65.108.193.133:16656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,d3373b407aff1cf04a24cd55dad288f4886888a2@185.213.26.129:26656,def346f6f24fbfea94d53021a40dcacba2a2b5e3@38.242.137.34:16656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
