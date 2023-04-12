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
peers="c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,5022b336c75b79270967cbf91321b3ed5cf83abb@34.173.31.167:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,89757803f40da51678451735445ad40d5b15e059@169.155.168.67:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,b5300c6086d6ab6b7c98a0e5914f73b44a8dd55e@35.224.198.112:26656,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,3fef899adcdeded56f6c69fe55c5da1624303367@163.172.101.208:4656,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,daf9846eb75229e315080d62c99e43da32f2fd0f@174.83.6.129:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,18256dedf8f01bb65c5a0b9e1a8e80de5ea8f156@65.108.232.168:16656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,07b0db05f1f252b2925cb779a7c7146244b34901@65.108.98.235:43856,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
