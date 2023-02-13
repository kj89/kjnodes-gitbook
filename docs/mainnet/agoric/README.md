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
peers="3d7d9eac612775c9530e990c44092d7ff55dbb83@95.216.39.109:26656,d48697ba840d046b453846fc55d9432d1c537b56@95.217.117.83:26656,956620729def7c20682fbc4f748a9ba7586f6015@93.115.25.106:44656,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,4cfac01c912d33f74cb7b66e8b7005aaae47fc2a@146.190.59.8:26060,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,d4dad3b42a98d85ab9c789328df81ce65481a492@178.128.42.132:26060,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,86d9c73c7687611a6a2619f0186e7ea59ff8af25@206.189.26.213:26060,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,502eadf625fff2474284062eef8e6c0c57bc9667@142.132.131.250:26656,8c30ee29afc4b77cf98222edcc3fe823cf1e8306@195.201.106.244:26656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,fb3c53630803da3947a54ac76bae6bd6e989a058@34.171.201.87:26656,71fb417c9ca941ddcd58c3d8995c18aa206c5281@35.215.33.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
