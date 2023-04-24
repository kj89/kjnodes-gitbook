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

**live-peers** (29)
```bash
peers="ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@172.111.52.51:32661,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,722884e3add85791c34a0563253dc47901320878@65.108.238.61:36656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,28ca5fc2464e9494e8d5bd93955cde707e4e208e@34.27.254.51:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,950da031d9536b9fbd0e9f0c70d65740d11d0111@192.118.76.199:26626,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,6fca686eca83017f3bb3055c3b58a2f8d476de8f@204.93.241.110:27652,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,e9ad059b88d593682307587b5c04a16a43893c5e@65.21.205.225:4656,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,c9027c0429bca7dc7a441d7764d404d50694c225@66.206.17.178:26665,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
