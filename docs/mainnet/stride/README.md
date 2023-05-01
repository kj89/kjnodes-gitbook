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
* grpc: stride.grpc.kjnodes.com:116090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:116656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:116659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (30)
```bash
peers="aa28a50f877a8d60c52f42d15d14ffa7ef8639c3@5.75.188.247:26639,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,3963b7cd5230ae2ba6800375421982d535a133e3@35.79.215.251:26656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,bf9168fbcc7250c7c5b9d8080cd4eeee6e399913@95.214.53.214:26886,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,a6d139e6cb349ae7fcb0104097f57e85e3bd33e0@13.212.155.28:26656,69fc32ac94aa1ccbac270fa58370459e647c251f@5.9.66.9:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,d041196a1a36091605448fc65181408ccc1d5da1@65.109.122.105:26656,a1f479dc2e3322c6547a39c6c7eef5a191def57f@34.132.213.169:26656,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,dfc62810eeaab86587b2975c79f3c12d4830652d@15.235.114.54:26656,8385b1a396afa02e777740277ed7b731e092bf49@212.90.120.249:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,6fca686eca83017f3bb3055c3b58a2f8d476de8f@204.93.241.110:27652,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
