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
peers="1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,00dc1964683a005274c39d3f347e83a5651dd923@65.21.127.159:26656,9661393350ef8224aaa620f543a7710c9af9c495@195.14.6.55:26656,71fb417c9ca941ddcd58c3d8995c18aa206c5281@35.215.33.76:26656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,964417b6767c62e4559988a290308cc553602e8e@142.132.132.148:31260,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,0766444edfd39ba589004830bc73cd65ec606bd6@34.94.183.70:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
