# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

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
peers="166da4de977381ea8853986be11dbb470d9dc2ba@149.202.72.186:26639,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,0d8efc8205826a74867dd063c30aa24342dd652b@83.136.251.210:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,df3f533e6b9776c11f08da804edcb810cbdd2080@65.108.234.23:12256,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.67:26656,d5035bd01baef508402b8649a33afc7b0fd190f1@141.95.72.74:24095,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,c948379b649bc6609557dd74f5a4e70716f100ea@51.210.240.201:10456,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
