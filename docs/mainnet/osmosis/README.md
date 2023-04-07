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

**live-peers** (30)
```bash
peers="4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,c29b58aa25198ef724189f9a0b8d7ef4399d9587@65.109.52.178:26656,e327b773177d3a00c461f59552a1962dd83741b2@65.108.9.164:10156,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,14428e1dbdcdc7736b0704ea116f2ebd068193a0@65.109.16.239:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,627b3c536853894ed0d4231e538e2689718182e6@157.90.34.91:27656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,63e4dd6530bf4dc4c2202be256b262a27d661106@146.19.24.108:26656,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,2cb8dd6195c65458e3c18505bb70ce2ff624f85c@89.58.61.223:2000,91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,677ef9606ea18a13b5dbfad19493d99d7ea068f5@149.56.24.130:26656,437602070a5d9da452a1c9b52677bafa7fdf9f0b@20.224.234.60:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
