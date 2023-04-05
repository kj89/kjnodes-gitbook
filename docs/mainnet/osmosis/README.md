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
peers="91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,9bdeb59c97c139187236b2ce92c229c3b9156d93@5.78.80.161:26656,e327b773177d3a00c461f59552a1962dd83741b2@65.108.9.164:10156,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,57eb30061f595699185f3161925827bb5a391264@195.154.200.69:26656,b6ec9c7284b45eb912b01c192f7ffd8ef7508ec7@51.81.123.33:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,b54d611ce10b7a4e816fae4e0b87b44f25c7da74@50.242.73.9:26656,7b45d963eef82cefd973a2649b7db37c738d07d3@18.222.45.225:26656,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,ea5ce509e09790c70609c8dc87ad4b19a0f98855@168.119.108.203:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656,7f36123a395e902deaecf63bdaf5656bbb209623@15.204.52.75:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,8795f27e60048c3aba4d75abd7bcc2d244ef7ebd@34.126.171.234:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
