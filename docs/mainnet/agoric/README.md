# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every 5 minutes)
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

**live-peers** (31)
```bash
peers="90f39ace82550b0e3b0c63ac0435f1935baba725@65.109.35.50:20658,b2406ba97421a9030bed25560c99b25965b6c336@135.181.2.54:26656,629c3b0ea094deecb6a31025d01ef6a5ba0beee7@135.181.180.230:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,bd362992fa6f6c9d8ee40d19508b5b28daf3f6ed@18.142.177.75:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,4cfac01c912d33f74cb7b66e8b7005aaae47fc2a@146.190.59.8:26060,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,86d9c73c7687611a6a2619f0186e7ea59ff8af25@206.189.26.213:26060,9d2bf3feb8a0a95ccce16a94f926d1c5ddad5190@65.108.121.110:12656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,d7e0eedf5756b8c085104fb76c069ba3506f2183@80.64.208.64:26656,ee236040d06e78d70c3f34722407857615b1a755@34.69.117.194:26656,d48697ba840d046b453846fc55d9432d1c537b56@95.217.117.83:26656,0861af66b3f637db967120d690758ee08222794c@75.119.148.118:36656,71bd0265037393f31ee9947a8e32fa494e51b637@135.181.218.98:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
