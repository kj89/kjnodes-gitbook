# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

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

**live-peers** (30)
```bash
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,914865f0b02d76c48c5369457cf5aa4173d06ed8@54.169.236.90:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,ef30bc7dbac63eb868e66bad497368f2cd0924e1@141.98.217.102:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,aa88cb583b8d932cadfcfd40de6594a64200da93@167.235.135.248:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,e6b9d01d5adc8ab1106f142b18f5ea5da00ec306@144.76.82.52:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,f96947493f1edd08058afaeaef8f5830cc70b8f2@15.204.197.10:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,0dcd3bc339e3018b68e1dd176007dbd7421db9f2@34.241.178.111:26656,2ff9bc1740a721a9baeda01abee181997bb65568@142.132.140.20:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
