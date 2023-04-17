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

**live-peers** (31)
```bash
peers="ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,718ce477a62a14efe61571bd836fd3db9e43e6c1@38.105.232.61:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,c3467e5becb108e62f6a6051eb5551e9f256d096@174.83.6.129:26656,5e0250a806113d60be48fab434ed81bb3e41be13@51.254.197.170:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,c124ce0b508e8b9ed1c5b6957f362225659b5343@144.76.177.187:26656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.224.198.112:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,2767e0948e6a67c3eb989d84179ed9154e5ca0ad@65.108.234.106:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
