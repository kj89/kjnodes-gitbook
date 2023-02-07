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

**live-peers** (25)
```bash
peers="44476201c6e8610b194e75e4c7993ad6d54a1db8@51.91.70.90:29656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,af77fd96cb62c6011272ee67390e540504b47fd9@51.222.42.205:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,3d7d9eac612775c9530e990c44092d7ff55dbb83@95.216.39.109:26656,cef26a8de3aa31f1f4e63898b38667b0816f35d3@14.224.155.176:26656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,fb3c53630803da3947a54ac76bae6bd6e989a058@34.72.229.79:26656,68c9c4e8388ed6936ff147ffe6b9913e79328957@35.215.62.66:26656,15f63de308337b66d8918ffaa74c6e956991bee9@138.201.120.161:28357,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,0e216cbbc65baedbb8732999f347255d5ac1debc@65.108.78.167:11656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,1ed533e5a4bd9749dc11f0cc22a6e3d92bdea4b4@34.171.201.87:26656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
