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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,ef30bc7dbac63eb868e66bad497368f2cd0924e1@141.98.217.102:26656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,d40d9763093fa618ce3adbdd0e6758a5b33e9ca4@173.215.85.171:20050,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.171.103:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,12910da249bcee4cdafbef938b10b51c94c0057e@5.9.142.165:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,6727a678e5d435ed8f372664a4210bb60ed53a31@13.213.56.178:26656,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,3226b67b2bb9da41b633392a785e87e8f6749939@162.55.245.149:12000,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.234:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
