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
peers="d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.213:26656,69fc32ac94aa1ccbac270fa58370459e647c251f@5.9.66.9:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,8385b1a396afa02e777740277ed7b731e092bf49@212.90.120.249:26656,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,59e886de6617994e8041124fecde40ab2ebae9e6@45.132.244.233:26656,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,be546a9a1b8b664a32ad5f45fa1d4087b44e0f83@135.181.214.120:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,2f6a21a94be87df4c2a2d82683e6ea99b7b6b02b@50.21.173.78:26656,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,2c1f55e905c7425f995947e2d600ca5ac863b8c1@15.235.53.91:13456,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,89757803f40da51678451735445ad40d5b15e059@169.155.168.67:26656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,51b83e27aee30e1900539cef37f18bddd4eab2d9@51.77.57.29:6000,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,fa34ce7ca08381d69278201e6386d3b7031e463f@162.55.163.71:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,bf0f5782650ddbf8121543b94705e5849f87120a@130.211.230.106:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
