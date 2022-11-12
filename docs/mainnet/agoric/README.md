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

**live-peers** (10)
```
peers="b2406ba97421a9030bed25560c99b25965b6c336@135.181.2.54:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656,2c03e71116d1a2f9ba39a63a97058fcdeabfe2be@159.148.31.233:26656,e07945e91c6f9936e3dee73afd49d904be320c99@128.0.51.3:26656,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,b8701af626159c0aac2d47b6009ce22988c32813@14.224.158.246:26656,3445f4b73fdc63a1bf78c638afb122f69cb0bd4a@157.90.208.234:26656,0861af66b3f637db967120d690758ee08222794c@75.119.148.118:36656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
