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

**live-peers** (20)
```bash
peers="d48697ba840d046b453846fc55d9432d1c537b56@95.217.117.83:26656,502eadf625fff2474284062eef8e6c0c57bc9667@142.132.131.250:26656,bd0bc3737ca1cfebc3c2aef75ab2c3cc74768d8a@142.132.212.19:26656,2aedd7163a8ee725507e461b13fb90c091ee1c42@128.0.51.32:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,d03a9974f14ae380fdb7caf46ec71ce5278f0356@34.72.231.9:26656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,71bd0265037393f31ee9947a8e32fa494e51b637@135.181.218.98:26656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,90f39ace82550b0e3b0c63ac0435f1935baba725@65.109.35.50:20658,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,c84170667fcf54024b24f05b2f9dd6608570ac8c@157.90.35.145:28656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
