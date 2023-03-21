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

**live-peers** (23)
```bash
peers="e3cc05de734a9eb3da832cf0236f319a9a4063ba@95.216.101.39:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,71f2451869d7363ce5d91366143de63069641303@65.108.71.166:33656,31e7a8b8cc97e85472c609f9d220fdd9536d4f4d@94.130.220.54:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,f02eff1003b07604cc556bcb0e8b7116ef6ea692@52.12.69.48:26656,9b1596775c01622ebd826a93dcc7e5b32a4652e1@18.159.135.176:26656,2e8a680af0c192f1b57f438e0dd56150299adbd9@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
