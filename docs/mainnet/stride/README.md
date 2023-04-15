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

**live-peers** (29)
```bash
peers="2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,c3467e5becb108e62f6a6051eb5551e9f256d096@174.83.6.129:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,222b5f1f8f8b4933c1913818ab2b7379c282b4e2@65.108.75.107:11656,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,07b0db05f1f252b2925cb779a7c7146244b34901@65.108.98.235:43856,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,6a1087004245692128a6ad11b812bb3640955b86@162.55.235.69:25656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.224.198.112:26656,bf77a8579431d8525e88e5a9e8823db1144b1441@65.109.69.154:31656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.235:26656,7ab3bfcdbe618ed62317cbc40ef48aee783fb2b4@144.76.152.68:4656,df43d9a9490495aa528431077b526eabeec46b52@95.217.197.100:26653,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.243:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
