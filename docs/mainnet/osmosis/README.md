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
* grpc: osmosis.grpc.kjnodes.com:129090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:129656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:129659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,aa88cb583b8d932cadfcfd40de6594a64200da93@167.235.135.248:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,6ab610679f84de983dde1beb2f4cd3bd226aa31a@51.81.185.115:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,a427a6c73e65ad4aa5acdee633afabeb8f473603@65.109.116.204:10156,50491afd6cb3910f94ccbf7190ac32f693e76d5b@185.216.179.86:26656,14014a2125c203c7ed0a6527957fff1485f4dbf0@141.94.97.75:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
