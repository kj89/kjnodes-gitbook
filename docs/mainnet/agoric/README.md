# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoC | **Wasm**: OFF

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

**live-peers** (35)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,85393883ac84551737d1f14347e0ffb0db87498f@3.234.241.191:26656,e5970b2440e4083c7d74b51c8991ac9fd0f54dc0@162.55.132.48:15634,3f307f0ad680e24755f8b5c546d0c18ff2dbf90e@65.108.128.247:26656,9d2bf3feb8a0a95ccce16a94f926d1c5ddad5190@65.108.121.110:12656,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,f769805423416d3bec0d683b3796f98a984ed51d@65.108.15.174:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,aea83f0d95f3732c700c7fd22f4afdf68f53e538@143.198.100.136:26656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,8880e10d956bff921ef928794dcadcc22c7087b4@51.91.218.186:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.134:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@82.100.58.101:26657,23fd78b96fc7f17b47fc4a0d442b0ec53faebd88@157.90.91.20:12656,d77d30c7a86c9a6013883d075493eaee365c3d48@213.135.246.90:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,86d9c73c7687611a6a2619f0186e7ea59ff8af25@206.189.26.213:26060,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,90f39ace82550b0e3b0c63ac0435f1935baba725@65.109.35.50:20658,853f52516e409ef3ec4921767abd02b151f5ecb7@146.59.81.23:26661,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,3d7d9eac612775c9530e990c44092d7ff55dbb83@95.216.39.109:26656,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,9661393350ef8224aaa620f543a7710c9af9c495@195.14.6.55:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
