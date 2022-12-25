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

**live-peers** (22)
```
peers="15f63de308337b66d8918ffaa74c6e956991bee9@138.201.120.161:28357,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,01c3a56aa6e69c59161a9e4ae1037388c8931367@116.202.114.4:26656,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@3.8.160.134:26656,e780b9c3b6f761efb7ba3bca74d3011f9bdf4bfd@139.59.8.48:26060,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,23fd78b96fc7f17b47fc4a0d442b0ec53faebd88@157.90.91.20:12656,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656,b2406ba97421a9030bed25560c99b25965b6c336@135.181.2.54:26656,0861af66b3f637db967120d690758ee08222794c@75.119.148.118:36656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,f34681c2aa8d198b754725b3f12cc48eb4066baf@114.132.59.209:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
