# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

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

**live-peers** (27)
```
peers="80e8d307c7b1e7027645a0054ba3e08addfa83b2@88.99.217.85:26656,853f52516e409ef3ec4921767abd02b151f5ecb7@146.59.81.23:26661,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@3.8.160.134:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,c38608dc31dcb336600abdb85e6ff040f47aea00@159.203.187.36:26060,90f39ace82550b0e3b0c63ac0435f1935baba725@65.109.35.50:20658,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,e780b9c3b6f761efb7ba3bca74d3011f9bdf4bfd@139.59.8.48:26060,c6475a8ccd715e297d21d17c5e391d5730393a78@18.214.40.80:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,af77fd96cb62c6011272ee67390e540504b47fd9@51.222.42.205:26656,586df7471fb74a7e182d6a96b6c8b1a58b0ed7a9@18.142.177.75:26656,fc425797b795205be22a38a391938690b9e28356@46.114.176.171:26656,b6396f86d6d73a99e1957ea202840d6f48eb03c9@44.192.103.233:26656,f23a7b7610843cb8d4a6f1f6a44d08926ea86e6d@195.14.6.2:26015"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
