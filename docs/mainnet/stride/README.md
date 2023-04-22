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
peers="a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,0d8efc8205826a74867dd063c30aa24342dd652b@83.136.251.210:26656,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,89757803f40da51678451735445ad40d5b15e059@169.155.168.67:26656,80b468e37cae35b2e5769e1f1b28d2e27d69f998@174.83.6.129:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,c948379b649bc6609557dd74f5a4e70716f100ea@51.210.240.201:10456,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,446d388856dde233a206d8649fdc24efbde2b57c@35.238.182.201:26656,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,2d64ce95c7e0c2b54ebd3c93b205418aeaa1ceb5@202.61.229.196:26656,c7a30393c5cab01f5b497c4c094424e4e6271bac@65.108.201.154:5010,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,a424cd8cc8d5fdb714d3d93daeb10509b28c7e27@85.214.29.87:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
