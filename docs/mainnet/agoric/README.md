# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)

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
peers="5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,d48697ba840d046b453846fc55d9432d1c537b56@95.217.117.83:26656,c6475a8ccd715e297d21d17c5e391d5730393a78@18.214.40.80:26656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,05f967bf55fee6647e69bdfca69f064d7e4876c5@128.199.128.15:26060,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,af77fd96cb62c6011272ee67390e540504b47fd9@51.222.42.205:26656,9661393350ef8224aaa620f543a7710c9af9c495@195.14.6.55:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,b6396f86d6d73a99e1957ea202840d6f48eb03c9@44.192.103.233:26656,586df7471fb74a7e182d6a96b6c8b1a58b0ed7a9@18.142.177.75:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,fb3c53630803da3947a54ac76bae6bd6e989a058@104.197.102.190:26656,8832d61e9b8856c0a80e240970a9200c69c101b7@88.99.161.228:21156,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
