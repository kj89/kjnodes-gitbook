# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every day at 08:00, 20:00)
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

**live-peers** (23)
```bash
peers="90f39ace82550b0e3b0c63ac0435f1935baba725@65.109.35.50:20658,2bda83f1501d30187e662c59d75ed4ffffcf8004@135.181.142.117:26656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,3704274281d20dc09e7161d80a1e16bcb2de0fbf@185.216.33.154:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,05f967bf55fee6647e69bdfca69f064d7e4876c5@128.199.128.15:26060,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,c51a25f0ee9e8305e2c20ca116a4bc840c6fbbd5@65.108.234.23:14456,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,fb3c53630803da3947a54ac76bae6bd6e989a058@34.72.229.79:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,01c3a56aa6e69c59161a9e4ae1037388c8931367@116.202.114.4:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,e759de7a872eff293ab1316a0745eb5fdd5614f3@88.217.142.187:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,cfc29147c8bfe80550c70f357a5385f62426507d@188.214.129.233:44656,b6396f86d6d73a99e1957ea202840d6f48eb03c9@44.192.103.233:26656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
