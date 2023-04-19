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

**live-peers** (28)
```bash
peers="28ca5fc2464e9494e8d5bd93955cde707e4e208e@34.29.90.236:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,8602d85bc570686ef255370177a92569e1ba4aa2@54.38.38.40:26639,471518432477e31ea348af246c0b54095d41352c@78.47.210.211:26656,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,ced7684f4d60399986cdbc1465ac00a420a14202@65.21.202.61:1807,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,7bbb4b5b161e38938414949ec3a82f4ac8ffb4ad@209.145.56.74:26656,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,7ab3bfcdbe618ed62317cbc40ef48aee783fb2b4@144.76.152.68:4656,c3467e5becb108e62f6a6051eb5551e9f256d096@98.97.16.41:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
