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
peers="c51a25f0ee9e8305e2c20ca116a4bc840c6fbbd5@65.108.234.23:14456,2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,b8701af626159c0aac2d47b6009ce22988c32813@14.224.158.246:26656,abc62ded9142361bd9832282242a53611785ffcd@51.81.109.109:26656,190ead3cfb1bd655241418f3ef9ba40bbf2deecd@157.90.130.44:26656,1c9a5b1d34b9e6f184b2dcb18ed068cf0c282e50@51.79.98.163:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
