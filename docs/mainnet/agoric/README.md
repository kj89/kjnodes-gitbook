# Agoric

[![Installation](https://i.ibb.co/MSCjwH2/button-installation.png)](./installation)
[![Upgrade](https://i.ibb.co/Jy6FZJv/button-upgrade.png)](./upgrade)
[![Snapshot](https://i.ibb.co/rFcf4cB/button-snapshot.png)](./snapshot)
[![State-sync](https://i.ibb.co/K0LzhCN/button-state-sync.png)](./state-sync)
[![Useful-commands](https://i.ibb.co/mNdXB4R/button-useful-commands.png)](./useful-commands)

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem. Agoric JavaScript smart contract platform enables 15M+ developers across the globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoC | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes\_proposal\_bot) to never miss upcoming proposals

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

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:27656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:27659
```

**addrbook**

```bash
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (25)

```bash
peers="f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@82.100.58.101:26657,c041ac25e8d0f34b453ebdbae00e72cad4bd7fd1@3.1.218.117:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,7a1b8143a8c9a338db3e4a3cc20198853d9e9ba6@45.79.96.110:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,956620729def7c20682fbc4f748a9ba7586f6015@93.115.25.106:44656,506f9bca6ce2f29a2556427f90693a8ee1b100ff@178.128.238.183:26060,37933cb8069e22554e454294d529eddb0fdae145@52.56.185.212:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,cccbc2151821e498e03a3a3df9115618571262a7@35.215.1.238:26656,98d989f486d42ec75203f918495c420ca9665514@34.122.28.103:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,cf6854b4615508d264ad4404061b083aa70ce9c8@34.72.229.79:26656,8346a2f94b41b8f0d43c49e37ca2ffc9855936b7@34.123.255.69:26656,4dfada1eaf19505734492171403a3c3c3648ba57@34.66.30.56:26656,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
