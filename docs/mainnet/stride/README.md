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

**live-peers** (29)
```bash
peers="f93ce5616f45d6c20d061302519a5c2420e3475d@135.125.5.31:54356,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,e41dd510feb9e14df82ce0f4eab258fad78645ea@158.247.218.149:10002,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,005a2f2a92d5bbf5f9376a8d2bd8b1f7ec0e4bf2@35.224.198.112:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,5383a21cf2d5e513aea2c3e430133f31aa2e5d00@138.201.32.103:26656,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,6fca686eca83017f3bb3055c3b58a2f8d476de8f@204.93.241.110:27652,c757aa720f0e0e9eff500dd6ada332119ee75c33@65.109.106.169:26656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,fb24bc1de8c563e822897fba89bf150c602f3123@198.244.178.213:26656,863663359048269f6fbfd09c94d0f7ed5b214aee@34.71.33.155:26656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,fc305427390397f8c4eebe5bc22919c1cc5d4532@65.109.43.75:27007,18256dedf8f01bb65c5a0b9e1a8e80de5ea8f156@65.108.232.168:16656,8602d85bc570686ef255370177a92569e1ba4aa2@54.38.38.40:26639,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
