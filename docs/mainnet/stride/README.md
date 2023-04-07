# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v8.0.0 | **Wasm**: OFF

[Website](https://stride.zone) | [Discord](https://discord.gg/mzQZ8dAE7u) | [Twitter](https://twitter.com/stride_zone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/stride](https://explorer.kjnodes.com/stride)

## Public endpoints

* api: [https://stride.api.kjnodes.com](https://stride.api.kjnodes.com)
* rpc: [https://stride.rpc.kjnodes.com](https://stride.rpc.kjnodes.com)
* grpc: stride.grpc.kjnodes.com:16090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:16656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (30)
```bash
peers="cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,e41dd510feb9e14df82ce0f4eab258fad78645ea@158.247.218.149:10002,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,471518432477e31ea348af246c0b54095d41352c@78.47.210.211:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,fb24bc1de8c563e822897fba89bf150c602f3123@198.244.178.213:26656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,5383a21cf2d5e513aea2c3e430133f31aa2e5d00@138.201.32.103:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.187:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.27:26656,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,93d7b9da65d31e052027abf20fab35ff31d3d826@195.20.240.90:26656,65dc9cc6ad24c60de3ac5aaf2d25a0bf9cb1617f@164.90.152.11:31690,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
