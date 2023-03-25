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
peers="4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,56fa1755d27cb5d8b061d5beeb0a969054ce056e@43.153.101.118:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,33cf290cc0cfec8c59e6af86f1a5579303d21087@138.68.14.64:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,4c727294c4d1b28e2c00399f3c00711a501a16c2@18.159.135.176:26656,3bc6699d0c9a6ce34aef3154f865b300b2f9aa1a@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
