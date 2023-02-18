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

**live-peers** (23)
```bash
peers="711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,1dfd1a8be38d892fa485e1b417bcf5f225b3f638@185.210.219.66:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,86d9c73c7687611a6a2619f0186e7ea59ff8af25@206.189.26.213:26060,4cfac01c912d33f74cb7b66e8b7005aaae47fc2a@146.190.59.8:26060,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,9d2bf3feb8a0a95ccce16a94f926d1c5ddad5190@65.108.121.110:12656,8c30ee29afc4b77cf98222edcc3fe823cf1e8306@195.201.106.244:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,f23a7b7610843cb8d4a6f1f6a44d08926ea86e6d@195.14.6.2:26015"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
