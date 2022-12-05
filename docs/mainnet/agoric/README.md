# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

Website: [https://agoric.com](https://agoric.com)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)

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
```
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (30)
```
peers="1bc9d0bc21a36cbe549088b49539b73e7580506b@89.58.3.166:26656,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,1dfd1a8be38d892fa485e1b417bcf5f225b3f638@185.210.219.66:26656,9661393350ef8224aaa620f543a7710c9af9c495@195.14.6.55:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,99968808ecae7bc41b14df3bcb51b724ee5f782f@134.209.154.162:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,00dc1964683a005274c39d3f347e83a5651dd923@65.21.127.159:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,b8701af626159c0aac2d47b6009ce22988c32813@14.224.158.246:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,f4b809dcf7004b8a30eaa4e9bb0a65164368b75a@49.12.165.122:26656,5f4701b2038bd82b5b1b2c9a576f49b1020b0380@135.181.22.167:44656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,a03e731a748947824276f6fa8d7181411136117c@144.126.148.191:26656,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,6b0538dbee953a1c50c28312907fe497625a93d0@46.166.143.91:26656,16f2ad1b7f154d6f8751c0ab7453e24f32ee8db3@95.217.45.52:26656,af77fd96cb62c6011272ee67390e540504b47fd9@51.222.42.205:26656,8c30ee29afc4b77cf98222edcc3fe823cf1e8306@195.201.106.244:26656,c38608dc31dcb336600abdb85e6ff040f47aea00@159.203.187.36:26060,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
