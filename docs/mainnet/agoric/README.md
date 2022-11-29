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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,b8701af626159c0aac2d47b6009ce22988c32813@14.224.158.246:26656,2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,86ae5b4d883a0b035a3ec0e17b1f98a545e6ad5b@44.225.233.214:26656,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,0766444edfd39ba589004830bc73cd65ec606bd6@34.94.183.70:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
