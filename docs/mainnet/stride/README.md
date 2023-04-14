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
peers="ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,6a1087004245692128a6ad11b812bb3640955b86@162.55.235.69:25656,474893e4c5c0970d70db5612e24a54ebd87abeac@95.217.192.173:6000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,6fca686eca83017f3bb3055c3b58a2f8d476de8f@204.93.241.110:27652,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,07b0db05f1f252b2925cb779a7c7146244b34901@65.108.98.235:43856,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,450d000d0d5c010cb2e7c45b72e6cda08a22fd04@35.224.198.112:26656,c3467e5becb108e62f6a6051eb5551e9f256d096@174.83.6.129:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,f8e2f80a8c58e6f53cc4940f5f1eac55c9067480@35.213.184.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
