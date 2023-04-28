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
peers="f1fe0a080d561d37a94bea6022cbc0972395a0f4@65.108.121.190:2000,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,f024eadf265f72f4240e5e3ea20eac22f6695ccb@159.65.100.92:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,f986f99b9aebdc4dd1f01903a2288e6d34db20d8@65.108.206.90:26656,6d2558d2999d3edcc5bc0222561c9828e7b23fb9@51.161.115.51:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.171.103:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,c879d94349a7be8168166250c084c68698a1d18d@45.32.181.106:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,ab3be1a8b463ac07d457dcce7af6b95cc7bae46b@46.4.79.183:26736,2904827f3ffa642bf7122d65cef27e1ab40a7346@35.74.104.174:16656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
