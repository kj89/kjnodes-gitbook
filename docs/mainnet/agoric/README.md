# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
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

**live-peers** (24)
```bash
peers="2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,fb3c53630803da3947a54ac76bae6bd6e989a058@34.72.229.79:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,b6396f86d6d73a99e1957ea202840d6f48eb03c9@44.192.103.233:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,d7e0eedf5756b8c085104fb76c069ba3506f2183@80.64.208.64:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,576e4e90b785fb16c129a0141b57342e51fd61b4@193.176.85.156:26656,05f967bf55fee6647e69bdfca69f064d7e4876c5@128.199.128.15:26060,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,8832d61e9b8856c0a80e240970a9200c69c101b7@88.99.161.228:21156,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
