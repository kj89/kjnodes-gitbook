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
peers="0e202ae079fb8b1849993ef6e6e6bd012b10374f@46.4.81.204:45656,b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.187:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,81139c36049f4a320c8b3c17427904a11471fb70@167.235.15.68:26656,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,0e67ce079f4e26ad5d22d7b1ba61e7df214d626c@65.108.101.50:60556"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
