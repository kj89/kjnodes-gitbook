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
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.213:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,bf0f5782650ddbf8121543b94705e5849f87120a@34.170.13.86:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,80b468e37cae35b2e5769e1f1b28d2e27d69f998@174.83.6.129:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,0003bf00c79e8ebd1f31c0f83ad3d181f97f98e9@62.109.17.96:26656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,ffc51a67aa88ce3a978ba248952565d0f32a2655@46.38.232.54:26666"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
