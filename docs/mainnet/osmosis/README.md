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

**live-peers** (29)
```bash
peers="f1fe0a080d561d37a94bea6022cbc0972395a0f4@65.108.121.190:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,50d2c6d6ef06cec7167cb2588636ae3593f575a5@86.111.48.150:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,c879d94349a7be8168166250c084c68698a1d18d@45.32.181.106:26656,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,9f2df25f380a7e67a92c3dc5e7c33c08555b30dc@5.9.108.19:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,af4b2624a7e95c52a9feaa812287a95696e04fa3@213.168.227.59:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,89b6c99ecd215cbd7eeac7fe9636295600198621@176.9.158.219:41056,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,3243426ab56b67f794fa60a79cc7f11bc7aa752d@35.210.252.64:26656,914865f0b02d76c48c5369457cf5aa4173d06ed8@54.169.236.90:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
