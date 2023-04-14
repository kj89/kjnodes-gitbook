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
peers="ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,c3467e5becb108e62f6a6051eb5551e9f256d096@174.83.6.129:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,a424cd8cc8d5fdb714d3d93daeb10509b28c7e27@85.214.29.87:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,07b0db05f1f252b2925cb779a7c7146244b34901@65.108.98.235:43856,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.27:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,c9027c0429bca7dc7a441d7764d404d50694c225@66.206.17.178:26665,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,450d000d0d5c010cb2e7c45b72e6cda08a22fd04@35.224.198.112:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
