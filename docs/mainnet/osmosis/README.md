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
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,8a0caf4581f135b1468408ec398d94573da02e8c@198.244.202.140:26656,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,fae5ea7e5e08795fa404265d2b2d78b417a06d79@23.108.108.110:26657,23d67702fc76a2f3b3f3b74876727934843cff94@195.14.6.2:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,c29b58aa25198ef724189f9a0b8d7ef4399d9587@65.109.52.178:26656,4d2605490fcd7369800cb0e1e27ef6d433c1cd96@65.109.20.37:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,3243426ab56b67f794fa60a79cc7f11bc7aa752d@35.210.252.64:26656,4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,bfcbd83f2ecfc2e839b246a001e355079e66f0fd@24.199.110.108:30799,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,4d1828a3df5a7c3d05030897eb7c82e6ac79c520@135.181.138.95:12000,e3ab699881792abe822e6de3a0da6eb84a143903@34.79.77.122:26656,d40d9763093fa618ce3adbdd0e6758a5b33e9ca4@173.215.85.171:20050,13d17adf418ceab5528096dcacf130830fee2b86@35.215.50.201:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,92551df875dc01b752d3560aee5ffe0007841a60@50.230.104.196:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,e327b773177d3a00c461f59552a1962dd83741b2@65.108.9.164:10156,7c5459ea4bbc41aa4d86ffe8126f0651155227c8@85.195.102.127:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
