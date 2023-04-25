# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoC | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/agoric](https://explorer.kjnodes.com/agoric)

## Public endpoints

* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)
* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* grpc: agoric.grpc.kjnodes.com:27090

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
peers="ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,e07945e91c6f9936e3dee73afd49d904be320c99@128.0.51.3:26656,7dbf60aa5851b7d7ba12673d7dcc71d6013fca8e@35.225.193.247:26656,37933cb8069e22554e454294d529eddb0fdae145@52.56.185.212:26656,506f9bca6ce2f29a2556427f90693a8ee1b100ff@178.128.238.183:26060,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,98d989f486d42ec75203f918495c420ca9665514@34.122.28.103:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,e5970b2440e4083c7d74b51c8991ac9fd0f54dc0@162.55.132.48:15634,81024f7597b22dd841613cac76a219d25a4533fe@13.215.217.74:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@82.100.58.101:26657,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,cccbc2151821e498e03a3a3df9115618571262a7@35.215.1.238:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,4dfada1eaf19505734492171403a3c3c3648ba57@34.66.30.56:26656,7a1b8143a8c9a338db3e4a3cc20198853d9e9ba6@45.79.96.110:26656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.134:26656,14c8fd41e030160bf28cb42ede8d6a0161563bfb@69.197.160.58:26656,b10682f3c25882b5ef94da284a4a195efad69d0d@95.216.94.106:26656,ee0ce8e2f964191564fd766daa8825ee2b02e697@18.179.198.198:26656,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,125911b3993930f69c873e3d8e80763d91cefab7@195.14.6.156:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
