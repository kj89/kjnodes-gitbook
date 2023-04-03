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
peers="cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,fb24bc1de8c563e822897fba89bf150c602f3123@198.244.178.213:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,89757803f40da51678451735445ad40d5b15e059@169.155.168.67:26656,df851b1226bd4c35e1dcba58b90e99821dcfb8a7@174.83.6.129:26656,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,471518432477e31ea348af246c0b54095d41352c@78.47.210.211:26656,5383a21cf2d5e513aea2c3e430133f31aa2e5d00@138.201.32.103:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,d95477fd745d8a5e4b3d9052149d28a5dc447a88@35.206.158.54:26656,325d4b902381828b046a32fff3899078c775dda1@34.66.206.221:26656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
