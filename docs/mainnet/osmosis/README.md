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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,ef30bc7dbac63eb868e66bad497368f2cd0924e1@141.98.217.102:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,e0f3b604f1df9bf6590c4cc09fee1e28f46b0b39@65.109.28.226:15656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,ab3be1a8b463ac07d457dcce7af6b95cc7bae46b@46.4.79.183:26736,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,6cbb7b7bddf723a28925fae2c19eb7be41ef687c@34.71.161.134:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,f024eadf265f72f4240e5e3ea20eac22f6695ccb@159.65.100.92:26656,e6b9d01d5adc8ab1106f142b18f5ea5da00ec306@144.76.82.52:26656,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
