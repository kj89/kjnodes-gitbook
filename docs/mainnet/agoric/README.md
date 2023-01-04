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

**live-peers** (26)
```
peers="feabf7eadf6e0b4d2d28c3fe59dc077258a74202@95.216.5.101:26656,96c998f1a59b108a24249da4132fb8f603ae7daf@95.217.118.121:26656,23fd78b96fc7f17b47fc4a0d442b0ec53faebd88@157.90.91.20:12656,c38608dc31dcb336600abdb85e6ff040f47aea00@159.203.187.36:26060,e780b9c3b6f761efb7ba3bca74d3011f9bdf4bfd@139.59.8.48:26060,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,1c9a5b1d34b9e6f184b2dcb18ed068cf0c282e50@51.79.98.163:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@3.8.160.134:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,8c30ee29afc4b77cf98222edcc3fe823cf1e8306@195.201.106.244:26656,c51a25f0ee9e8305e2c20ca116a4bc840c6fbbd5@65.108.234.23:14456,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
