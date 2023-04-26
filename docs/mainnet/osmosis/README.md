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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,7fc90a9c32c775ff685798c33fc06fe6d5009b26@202.61.229.102:26656,1990bfb9135023ca697bbb8a8d0defb6e4669478@211.219.19.74:26656,af678c610cf37bf5d443efdba7ac1354f104415c@137.184.9.18:32644,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,9379a49cadb2e71d896c2d4ebd5ca394e50bf983@18.116.211.23:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,8c5e9342661a728b810d82221152b2a2fce5018a@162.19.84.205:26656,f024eadf265f72f4240e5e3ea20eac22f6695ccb@159.65.100.92:26656,ef573bd8b519f9572798444f6c229ab0a3204bb8@5.9.94.24:26656,3d311ac374e6953e97ee07c74a76f399394c3025@173.215.85.171:20000,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,65f51ebf46256d829ae5903e9faf31dae35bdf46@65.109.64.245:26656,807eda3abecff79df294d127cf58d6d5e07393ee@67.209.54.21:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.234:26656,6ab610679f84de983dde1beb2f4cd3bd226aa31a@51.81.185.115:26656,b67b6f62e083eabe4efd2ef4f4238a56edaf85de@141.95.157.155:26656,6cbb199c891bf1ed925c64fd1ec0882afdc2e2dc@162.19.81.54:34656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,3243426ab56b67f794fa60a79cc7f11bc7aa752d@35.210.252.64:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,170e681516b039be361df87eb626ee81c08f07a4@157.245.115.42:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
