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

**live-peers** (21)
```bash
peers="42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,b37a3c92c039de2582edd120b16afa3f462ecf3e@23.88.69.22:27166,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,dc230c6475bdbf3ab64058a37a8de2261b6396eb@74.96.207.58:26822,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,f95d9634ad68b8f0ac80ce308adb71d8c119ada5@141.98.219.104:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,83ba71ec35deb3885588084c754b860a70397573@3.15.176.200:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
