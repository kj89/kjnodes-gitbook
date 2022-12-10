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

**live-peers** (23)
```
peers="c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,1312bbbd4ed1e58b9e4eb1d7788187a4607915e9@165.22.199.234:26060,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,f1966845bebd30816f18635a20b86e6781211616@95.111.253.200:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,023be2465f7292cb3284a50787d6edc5a75c62a2@95.214.52.166:26656,320dd22ee85e2b68f891b670331eb9fec9dc419e@80.64.208.63:26656,c38608dc31dcb336600abdb85e6ff040f47aea00@159.203.187.36:26060,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,47c35c8137ad2098e0b2a79077fea93a530034d8@185.144.83.130:26656,9661393350ef8224aaa620f543a7710c9af9c495@195.14.6.55:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,766536f9ada683a9272c5305398ca7f82c9e7d43@35.215.60.158:26656,03c7d68a1433dde6db1acbbdf98712609843cc8f@161.97.187.189:36656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@3.8.160.134:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.agoric/config/config.toml
```
