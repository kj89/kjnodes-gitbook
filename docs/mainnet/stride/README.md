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
peers="6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,be546a9a1b8b664a32ad5f45fa1d4087b44e0f83@135.181.214.120:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,722884e3add85791c34a0563253dc47901320878@65.108.238.61:36656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,e8be5c472174a97a3d3076bd33be75f5fde92a5b@151.106.40.38:29656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,1e0e88fac793f68822d3ea8e952f2dc0f4c1ca57@142.132.135.125:20656,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,e9ad059b88d593682307587b5c04a16a43893c5e@65.21.205.225:4656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
