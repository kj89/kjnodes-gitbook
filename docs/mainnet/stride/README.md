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

**live-peers** (28)
```bash
peers="1e0e88fac793f68822d3ea8e952f2dc0f4c1ca57@142.132.135.125:20656,022fd83f945fe03f9155fced534c90b5ce8db979@65.109.23.238:36656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,e41dd510feb9e14df82ce0f4eab258fad78645ea@158.247.218.149:10002,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,df851b1226bd4c35e1dcba58b90e99821dcfb8a7@174.83.6.129:26656,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,69fc32ac94aa1ccbac270fa58370459e647c251f@5.9.66.9:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,5383a21cf2d5e513aea2c3e430133f31aa2e5d00@138.201.32.103:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.46.64:26656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,18256dedf8f01bb65c5a0b9e1a8e80de5ea8f156@65.108.232.168:16656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,5022b336c75b79270967cbf91321b3ed5cf83abb@34.173.31.167:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
