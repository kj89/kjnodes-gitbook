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

**live-peers** (30)
```bash
peers="15f63de308337b66d8918ffaa74c6e956991bee9@138.201.120.161:28357,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,c041ac25e8d0f34b453ebdbae00e72cad4bd7fd1@3.1.218.117:26656,506f9bca6ce2f29a2556427f90693a8ee1b100ff@178.128.238.183:26060,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,cf6854b4615508d264ad4404061b083aa70ce9c8@34.72.229.79:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@82.100.58.101:26657,96c998f1a59b108a24249da4132fb8f603ae7daf@95.217.118.121:26656,98d989f486d42ec75203f918495c420ca9665514@34.122.28.103:26656,37933cb8069e22554e454294d529eddb0fdae145@52.56.185.212:26656,cccbc2151821e498e03a3a3df9115618571262a7@35.215.1.238:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,125911b3993930f69c873e3d8e80763d91cefab7@195.14.6.156:26656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,190ead3cfb1bd655241418f3ef9ba40bbf2deecd@157.90.130.44:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,f3e0f4913519788b0c72ad2b5c7254b978badf52@65.109.112.29:34656,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656,8346a2f94b41b8f0d43c49e37ca2ffc9855936b7@34.123.255.69:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,320dd22ee85e2b68f891b670331eb9fec9dc419e@80.64.208.63:26656,6ab5521047ae8e7bb0273a90029a6d445eb1a0a1@135.181.113.227:2206"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
