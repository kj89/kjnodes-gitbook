# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:29090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:29656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:29659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,f986f99b9aebdc4dd1f01903a2288e6d34db20d8@65.108.206.90:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,ab3be1a8b463ac07d457dcce7af6b95cc7bae46b@46.4.79.183:26736,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,a220ccc0311498ac7414cbe0b29f62610844f618@34.79.77.122:26656,991e8c2d75ed411c3ee620d61db7d49346a3f88b@146.190.48.40:32143,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,8c5e9342661a728b810d82221152b2a2fce5018a@162.19.84.205:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,c5afa50cac6814f16facafb0c680871ebd62482d@184.105.162.166:26656,3e3f8f3a9ed941600550d090900aee639abb7906@93.159.134.158:56656,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
