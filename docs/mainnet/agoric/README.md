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

**live-peers** (37)
```bash
peers="90f39ace82550b0e3b0c63ac0435f1935baba725@65.109.35.50:20658,a65d3172dca90f0d9f8251c3ed2747f350eb9a7e@95.216.246.187:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,c51a25f0ee9e8305e2c20ca116a4bc840c6fbbd5@65.108.234.23:14456,1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,ecdfb6d2223b562956eeb205cdd4b81e3e6e8581@213.135.246.90:26656,86d9c73c7687611a6a2619f0186e7ea59ff8af25@206.189.26.213:26060,4cfac01c912d33f74cb7b66e8b7005aaae47fc2a@146.190.59.8:26060,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,190ead3cfb1bd655241418f3ef9ba40bbf2deecd@157.90.130.44:26656,8698ec1488fbf96f817e15a07552139be9f8b35f@139.59.0.208:26656,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656,d7e0eedf5756b8c085104fb76c069ba3506f2183@80.64.208.64:26656,71bd0265037393f31ee9947a8e32fa494e51b637@135.181.218.98:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,ee236040d06e78d70c3f34722407857615b1a755@34.66.30.56:26656,00dc1964683a005274c39d3f347e83a5651dd923@65.21.127.159:26656,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,576e4e90b785fb16c129a0141b57342e51fd61b4@193.176.85.156:26656,8832d61e9b8856c0a80e240970a9200c69c101b7@88.99.161.228:21156,44476201c6e8610b194e75e4c7993ad6d54a1db8@51.91.70.90:29656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,bd362992fa6f6c9d8ee40d19508b5b28daf3f6ed@18.142.177.75:26656,baf3faf6d6e4c32c4ee2cde510efabe127d3ce74@35.77.171.242:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
