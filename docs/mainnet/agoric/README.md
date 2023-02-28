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

**live-peers** (38)
```bash
peers="16f2ad1b7f154d6f8751c0ab7453e24f32ee8db3@95.217.45.52:26656,86d9c73c7687611a6a2619f0186e7ea59ff8af25@206.189.26.213:26060,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,320dd22ee85e2b68f891b670331eb9fec9dc419e@80.64.208.63:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,bd362992fa6f6c9d8ee40d19508b5b28daf3f6ed@18.142.177.75:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,4cfac01c912d33f74cb7b66e8b7005aaae47fc2a@146.190.59.8:26060,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,bb257b3a0829910477a3845430b6b1f7eb2b4235@34.146.189.78:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,6dfaacf27072052e335de6e83069c811311613c5@138.201.127.91:26656,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,85393883ac84551737d1f14347e0ffb0db87498f@3.234.241.191:26656,d48697ba840d046b453846fc55d9432d1c537b56@95.217.117.83:26656,e07945e91c6f9936e3dee73afd49d904be320c99@128.0.51.3:26656,ee236040d06e78d70c3f34722407857615b1a755@34.69.117.194:26656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,8832d61e9b8856c0a80e240970a9200c69c101b7@88.99.161.228:21156,4bc6c457c018b81a19efa49a9e403b64535decf1@137.184.141.111:26656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,190ead3cfb1bd655241418f3ef9ba40bbf2deecd@157.90.130.44:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,8c30ee29afc4b77cf98222edcc3fe823cf1e8306@195.201.106.244:26656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,0861af66b3f637db967120d690758ee08222794c@75.119.148.118:36656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
