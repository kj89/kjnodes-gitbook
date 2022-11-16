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

**live-peers** (9)
```
peers="9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,0f95188872bf59edffb4874ed5593b012e377a0e@65.108.7.120:26656,ae78d2819cb972184531f670fe76a9b2843b1133@138.201.141.76:60856,b72d5281c9388ae9f1274ec3b92c1db17857a4b7@194.195.246.27:26656,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,c4688bb34164eacacaa374bc7440b87986dd87ac@162.251.235.252:26656,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,921b74b0d483b13e786becb7fc196671d90e3fab@66.172.36.137:28656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
