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
peers="253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,3243426ab56b67f794fa60a79cc7f11bc7aa752d@35.210.252.64:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.171.103:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,ab3be1a8b463ac07d457dcce7af6b95cc7bae46b@46.4.79.183:26736,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,6727a678e5d435ed8f372664a4210bb60ed53a31@13.213.56.178:26656,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,627b3c536853894ed0d4231e538e2689718182e6@157.90.34.91:27656,e6b9d01d5adc8ab1106f142b18f5ea5da00ec306@144.76.82.52:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@178.211.139.77:26716,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,914865f0b02d76c48c5369457cf5aa4173d06ed8@54.169.236.90:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
