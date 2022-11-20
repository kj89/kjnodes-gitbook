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

**live-peers** (11)
```
peers="6a1087004245692128a6ad11b812bb3640955b86@162.55.235.69:25656,b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,71082b73b93979f772b6e53bd700ca13cb69b847@162.251.235.253:26656,025c055b34da508bf6da83590e29f3a51b935b70@23.88.69.22:28656,04ea9eceee16db90872fee3fbef9ac50a87702c5@185.248.24.29:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,b07b6cc0b70f15e20c0125b202b7fbc5680b8836@136.243.78.251:36656,182d866c8be094dffad6719702ff2514b5dfeabb@54.37.129.164:54356,d13d51e660dbd89d6660ac9b61957c5e727efdae@135.181.130.145:6000,dfc62810eeaab86587b2975c79f3c12d4830652d@15.235.114.54:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
