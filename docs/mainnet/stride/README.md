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
peers="b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.187:26656,2f6a21a94be87df4c2a2d82683e6ea99b7b6b02b@50.21.173.78:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,5dbe792854b8f81df6c6fe5b7aa64d60b27f6100@137.184.235.212:26656,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.187:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:16656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
