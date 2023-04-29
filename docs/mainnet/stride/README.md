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

**live-peers** (29)
```bash
peers="2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,166da4de977381ea8853986be11dbb470d9dc2ba@149.202.72.186:26639,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,be546a9a1b8b664a32ad5f45fa1d4087b44e0f83@135.181.214.120:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,2f6a21a94be87df4c2a2d82683e6ea99b7b6b02b@50.21.173.78:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,8385b1a396afa02e777740277ed7b731e092bf49@212.90.120.249:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
