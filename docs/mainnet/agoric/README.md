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
peers="aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,f1966845bebd30816f18635a20b86e6781211616@95.111.253.200:26656,2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,abc62ded9142361bd9832282242a53611785ffcd@51.81.109.109:26656,2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,23fd78b96fc7f17b47fc4a0d442b0ec53faebd88@157.90.91.20:12656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,c51a25f0ee9e8305e2c20ca116a4bc840c6fbbd5@65.108.234.23:14456,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
