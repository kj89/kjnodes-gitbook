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
peers="a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,a1f479dc2e3322c6547a39c6c7eef5a191def57f@34.132.213.169:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.213:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,99c09c4a6c29d0e53b2f24c8fb8be9272babb700@174.83.6.129:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
