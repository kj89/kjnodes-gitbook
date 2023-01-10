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

**live-peers** (24)
```bash
peers="c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,5e0acd690771af91625095185f6081dd1bccdb8f@78.47.21.189:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,4cfac01c912d33f74cb7b66e8b7005aaae47fc2a@146.190.59.8:26060,05f967bf55fee6647e69bdfca69f064d7e4876c5@128.199.128.15:26060,b6396f86d6d73a99e1957ea202840d6f48eb03c9@44.192.103.233:26656,c6475a8ccd715e297d21d17c5e391d5730393a78@18.214.40.80:26656,44476201c6e8610b194e75e4c7993ad6d54a1db8@51.91.70.90:29656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,3704274281d20dc09e7161d80a1e16bcb2de0fbf@185.216.33.154:26656,1c9a5b1d34b9e6f184b2dcb18ed068cf0c282e50@51.79.98.163:26656,586df7471fb74a7e182d6a96b6c8b1a58b0ed7a9@18.142.177.75:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,f8ff12a774770fea36beadb303ccffc86863c6ec@65.109.69.59:14456,0e216cbbc65baedbb8732999f347255d5ac1debc@65.108.78.167:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
