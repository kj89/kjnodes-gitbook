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

**live-peers** (25)
```bash
peers="71bd0265037393f31ee9947a8e32fa494e51b637@135.181.218.98:26656,b2406ba97421a9030bed25560c99b25965b6c336@135.181.2.54:26656,0861af66b3f637db967120d690758ee08222794c@75.119.148.118:36656,03c7d68a1433dde6db1acbbdf98712609843cc8f@161.97.187.189:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,aede0d57cd77051cf1270675fa770c22e8074501@64.32.40.117:26656,4eea1e0a22d8d2ade108fc5f8e07d6d6e711e909@65.108.10.138:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,c6475a8ccd715e297d21d17c5e391d5730393a78@18.214.40.80:26656,059f6ccc82a5bdd61e9089914368d0aade14fac0@159.89.101.239:26060,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.134:26656,e70955351f601ea5be9a9bf41032949a777f31b3@207.244.255.229:10003,8c30ee29afc4b77cf98222edcc3fe823cf1e8306@195.201.106.244:26656,1d4d7b77e79c2dad9e8586df4f30c7b550f5d49b@13.40.153.111:26656,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,71fb417c9ca941ddcd58c3d8995c18aa206c5281@35.215.33.76:26656,1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,44476201c6e8610b194e75e4c7993ad6d54a1db8@51.91.70.90:29656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@185.146.148.101:26657,fb3c53630803da3947a54ac76bae6bd6e989a058@104.197.102.190:26656,05f967bf55fee6647e69bdfca69f064d7e4876c5@128.199.128.15:26060"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
