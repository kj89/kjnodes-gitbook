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

**live-peers** (23)
```bash
peers="16f2ad1b7f154d6f8751c0ab7453e24f32ee8db3@95.217.45.52:26656,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,af77fd96cb62c6011272ee67390e540504b47fd9@51.222.42.205:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,05f967bf55fee6647e69bdfca69f064d7e4876c5@128.199.128.15:26060,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,c6475a8ccd715e297d21d17c5e391d5730393a78@18.214.40.80:26656,2f524fbc73a8b0daa29f2ba0b7642aae62bea86f@65.108.144.8:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,fb3c53630803da3947a54ac76bae6bd6e989a058@34.72.229.79:26656,8c30ee29afc4b77cf98222edcc3fe823cf1e8306@195.201.106.244:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,b6396f86d6d73a99e1957ea202840d6f48eb03c9@44.192.103.233:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,f23a7b7610843cb8d4a6f1f6a44d08926ea86e6d@195.14.6.2:26015"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
