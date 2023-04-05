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
peers="f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,c61bf85fd330bb702b1f13f58dd3cf83c5363bf2@149.56.26.22:26656,77bb5fb9b6964d6e861e91c1d55cf82b67d838b5@35.212.77.47:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,9bdeb59c97c139187236b2ce92c229c3b9156d93@5.78.80.161:26656,34340a9151d4a97a850d2cd64d8778279faf3f96@194.163.181.100:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,5bda7b3070d62b4ddbea815e8bea6c6e9548d17d@65.108.140.115:26656,42745690b41f6a7515c4a87d88efda2e82b55b76@78.46.94.183:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,4c927f93d430baf31e6d6418e62c56f442f092bc@46.4.28.42:26656,d0c050f33b7aa1032a3763da0e7eb8df0ac72a2c@162.55.92.114:12000,2186d344ff775c8181bf31de600eed0c72b9fe9e@65.109.28.213:26656,4d2605490fcd7369800cb0e1e27ef6d433c1cd96@65.109.20.37:26656,63b4a45bb2276fe141e69ce83750a2c53f1ceeda@198.244.202.196:26656,91ed0275dcc075ba506a150b446f32ca38d805e0@195.14.6.2:26656,a559df67d051d54627a3e25584ff18b8ca55a8b0@95.216.46.251:26656,c257db7b3a7f61688c6452d1e9dcfb3034e54fe8@143.198.98.144:26656,f4b811759e55f665180545ad5e1b42573f660861@135.181.181.251:26656,4cccbb26639559c39f44758d246c5ed928f7717f@176.9.19.66:26656,b54d611ce10b7a4e816fae4e0b87b44f25c7da74@50.242.73.9:26656,3e874613919a6f8b3fc26071fef563c88f031b3c@116.202.236.59:31656,74e8ba742d8312c250f3237c8c8f3f951c01f9df@95.216.4.104:26656,913e9db0332df1152e5afe032ab81bdb65e3f91c@110.11.23.44:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
