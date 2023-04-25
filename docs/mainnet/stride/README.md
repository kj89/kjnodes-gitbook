# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

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

**live-peers** (29)
```bash
peers="e9ad059b88d593682307587b5c04a16a43893c5e@65.21.205.225:4656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,be546a9a1b8b664a32ad5f45fa1d4087b44e0f83@135.181.214.120:26656,bffe92095850b08f905f6fde1d4282b4a619a690@5.161.97.148:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,d95477fd745d8a5e4b3d9052149d28a5dc447a88@35.206.158.54:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,450d000d0d5c010cb2e7c45b72e6cda08a22fd04@35.193.66.50:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,cb0b38aa612e8ac05f704d9b2feb7526607afb77@143.42.121.64:26656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
