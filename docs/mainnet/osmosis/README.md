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
peers="6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,92551df875dc01b752d3560aee5ffe0007841a60@50.230.104.196:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,4d2605490fcd7369800cb0e1e27ef6d433c1cd96@65.109.20.37:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,c29b58aa25198ef724189f9a0b8d7ef4399d9587@65.109.52.178:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,3243426ab56b67f794fa60a79cc7f11bc7aa752d@35.210.252.64:26656,7c5459ea4bbc41aa4d86ffe8126f0651155227c8@85.195.102.127:26656,fae5ea7e5e08795fa404265d2b2d78b417a06d79@23.108.108.110:26657,d40d9763093fa618ce3adbdd0e6758a5b33e9ca4@173.215.85.171:20050,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,5d89cdee503f53f9ff21c8032928adcdbd6d4f70@20.196.206.0:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,b59016320a74525f92dbc3348521c64f2bf3f006@65.109.20.216:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,5fa811f382b46545faddbaff01effdd4b59c90b4@54.95.64.184:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
