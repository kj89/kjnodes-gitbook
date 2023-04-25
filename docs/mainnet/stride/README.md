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

**live-peers** (29)
```bash
peers="1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,b7645e17efb21d31aa718cf7f1cf249650d81de4@85.10.203.235:26696,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,aa28a50f877a8d60c52f42d15d14ffa7ef8639c3@5.75.188.247:26639,166da4de977381ea8853986be11dbb470d9dc2ba@149.202.72.186:26639,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,d95477fd745d8a5e4b3d9052149d28a5dc447a88@35.206.158.54:26656,8385b1a396afa02e777740277ed7b731e092bf49@212.90.120.249:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,28ca5fc2464e9494e8d5bd93955cde707e4e208e@34.29.90.236:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
