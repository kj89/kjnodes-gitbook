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

**live-peers** (30)
```bash
peers="b7645e17efb21d31aa718cf7f1cf249650d81de4@85.10.203.235:26696,0c900d88aab9212e00607c756b152465a830723c@37.59.21.96:12256,5dbe792854b8f81df6c6fe5b7aa64d60b27f6100@137.184.235.212:26656,6fca686eca83017f3bb3055c3b58a2f8d476de8f@204.93.241.110:27652,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.213:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,950da031d9536b9fbd0e9f0c70d65740d11d0111@192.118.76.199:26626,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,722884e3add85791c34a0563253dc47901320878@65.108.238.61:36656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.193.66.50:26656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,446d388856dde233a206d8649fdc24efbde2b57c@35.238.182.201:26656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,8385b1a396afa02e777740277ed7b731e092bf49@212.90.120.249:26656,ed70fb7322fda1ee4646df34b47919ec6728586b@96.234.160.22:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
