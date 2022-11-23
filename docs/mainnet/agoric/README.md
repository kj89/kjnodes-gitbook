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
peers="2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,abc62ded9142361bd9832282242a53611785ffcd@51.81.109.109:26656,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,766536f9ada683a9272c5305398ca7f82c9e7d43@35.215.60.158:26656,576e4e90b785fb16c129a0141b57342e51fd61b4@193.176.85.156:26656,0766444edfd39ba589004830bc73cd65ec606bd6@34.94.183.70:26656,bb257b3a0829910477a3845430b6b1f7eb2b4235@34.146.189.78:26656,2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
