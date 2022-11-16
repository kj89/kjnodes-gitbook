# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

Website: [https://agoric.com](https://agoric.com)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:27656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:27659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (11)
```
peers="b2406ba97421a9030bed25560c99b25965b6c336@135.181.2.54:26656,1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,af77fd96cb62c6011272ee67390e540504b47fd9@51.222.42.205:26656,03c7d68a1433dde6db1acbbdf98712609843cc8f@161.97.187.189:36656,85c7363af4dc1823f8059b6c06c37a9df4b68790@65.109.39.50:26656,96c998f1a59b108a24249da4132fb8f603ae7daf@95.217.118.121:26656,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,023be2465f7292cb3284a50787d6edc5a75c62a2@95.214.52.166:26656,3445f4b73fdc63a1bf78c638afb122f69cb0bd4a@157.90.208.234:26656,0766444edfd39ba589004830bc73cd65ec606bd6@34.94.183.70:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
