# Services

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

**live-peers** (28)
```bash
peers="23fd78b96fc7f17b47fc4a0d442b0ec53faebd88@157.90.91.20:12656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@82.100.58.101:26657,37933cb8069e22554e454294d529eddb0fdae145@52.56.185.212:26656,506f9bca6ce2f29a2556427f90693a8ee1b100ff@178.128.238.183:26060,cccbc2151821e498e03a3a3df9115618571262a7@35.215.1.238:26656,85393883ac84551737d1f14347e0ffb0db87498f@3.234.241.191:26656,c041ac25e8d0f34b453ebdbae00e72cad4bd7fd1@3.1.218.117:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,576e4e90b785fb16c129a0141b57342e51fd61b4@193.176.85.156:26656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,b37f20e94ab5164cfcc25c3ba5816ba5a272a22c@46.4.116.21:26656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,4518031666b916836749b794cc249b0b47b7b312@95.217.196.54:2610,ee236040d06e78d70c3f34722407857615b1a755@34.69.117.194:26656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,90f39ace82550b0e3b0c63ac0435f1935baba725@65.109.35.50:20658"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
