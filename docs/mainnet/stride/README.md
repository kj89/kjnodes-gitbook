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
peers="1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,aa28a50f877a8d60c52f42d15d14ffa7ef8639c3@5.75.188.247:26639,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.224.198.112:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,c3467e5becb108e62f6a6051eb5551e9f256d096@174.83.6.129:26656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,6e50791af47369e3afd1458fe73c6b6337ba460f@185.215.166.166:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,8385b1a396afa02e777740277ed7b731e092bf49@212.90.120.249:26656,018d66466cfd907d5cc166ba3d5df8958c96e80a@149.56.36.205:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
