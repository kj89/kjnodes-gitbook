# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" alt=""><figcaption></figcaption></figure>

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
peers="ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,722884e3add85791c34a0563253dc47901320878@65.108.238.61:36656,18256dedf8f01bb65c5a0b9e1a8e80de5ea8f156@65.108.232.168:16656,a83cd29f4f9a4711346184966f9fb6c80bb658d2@65.108.103.184:21656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,be546a9a1b8b664a32ad5f45fa1d4087b44e0f83@135.181.214.120:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,d5035bd01baef508402b8649a33afc7b0fd190f1@141.95.72.74:24095,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,c948379b649bc6609557dd74f5a4e70716f100ea@51.210.240.201:10456,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,6fca686eca83017f3bb3055c3b58a2f8d476de8f@204.93.241.110:27652,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
