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
peers="b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,025c055b34da508bf6da83590e29f3a51b935b70@23.88.69.22:28656,4606c18ffe5c5e0126b1c89289e9e1359014bed3@188.68.43.46:26656,1b4f221c07a7fff994b5e749246c8305927518dd@178.170.47.62:26656,921b74b0d483b13e786becb7fc196671d90e3fab@66.172.36.137:28656,89dbb2e146a2b3401fb959295babba090aa2f0e9@89.58.7.66:16656,777274fb08ed48a4e027664e2576a8460272e43c@15.235.115.153:26656,021974bdbb3108a706e97204434cc606a36e95b8@23.88.69.167:26767,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@15.156.2.222:26603,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
