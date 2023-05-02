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
* grpc: stride.grpc.kjnodes.com:11690

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,a988534ab1e4bc42aad26ea7ec7bdc7d5415a14c@107.6.2.27:32670,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,7ab3bfcdbe618ed62317cbc40ef48aee783fb2b4@144.76.152.68:4656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.213:26656,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,450d000d0d5c010cb2e7c45b72e6cda08a22fd04@35.193.66.50:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,dfc62810eeaab86587b2975c79f3c12d4830652d@15.235.114.54:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,d041196a1a36091605448fc65181408ccc1d5da1@65.109.122.105:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,a1f479dc2e3322c6547a39c6c7eef5a191def57f@34.132.213.169:26656,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,8385b1a396afa02e777740277ed7b731e092bf49@212.90.120.249:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
