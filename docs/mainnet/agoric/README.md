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
peers="c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,e07945e91c6f9936e3dee73afd49d904be320c99@128.0.51.3:26656,0766444edfd39ba589004830bc73cd65ec606bd6@34.94.183.70:26656,71fb417c9ca941ddcd58c3d8995c18aa206c5281@35.215.33.76:26656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,85c7363af4dc1823f8059b6c06c37a9df4b68790@65.109.39.50:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656,16f2ad1b7f154d6f8751c0ab7453e24f32ee8db3@95.217.45.52:26656,964417b6767c62e4559988a290308cc553602e8e@142.132.132.148:31260"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
