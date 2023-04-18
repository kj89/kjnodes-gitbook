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
peers="754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,722884e3add85791c34a0563253dc47901320878@65.108.238.61:36656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,c3467e5becb108e62f6a6051eb5551e9f256d096@174.83.6.129:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,f5732d5a406bdbbf08acad017c0993c0aa8ebe70@34.145.16.183:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.224.198.112:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,ed70fb7322fda1ee4646df34b47919ec6728586b@96.234.160.22:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
