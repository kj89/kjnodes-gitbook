# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/agoric](https://explorer.kjnodes.com/agoric)

## Public endpoints

* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)
* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* grpc: [https://agoric.grpc.kjnodes.com](https://agoric.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:27656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:27659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (30)
```bash
peers="2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,e5970b2440e4083c7d74b51c8991ac9fd0f54dc0@162.55.132.48:15634,ef12448f0f8671a195ab38c590cac713ad703a8b@146.70.66.202:26656,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,e780b9c3b6f761efb7ba3bca74d3011f9bdf4bfd@139.59.8.48:26060,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,05f967bf55fee6647e69bdfca69f064d7e4876c5@128.199.128.15:26060,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,576e4e90b785fb16c129a0141b57342e51fd61b4@193.176.85.156:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,506f9bca6ce2f29a2556427f90693a8ee1b100ff@178.128.238.183:26060,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,3d7d9eac612775c9530e990c44092d7ff55dbb83@95.216.39.109:26656,586df7471fb74a7e182d6a96b6c8b1a58b0ed7a9@18.142.177.75:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,fb3c53630803da3947a54ac76bae6bd6e989a058@104.197.102.190:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
