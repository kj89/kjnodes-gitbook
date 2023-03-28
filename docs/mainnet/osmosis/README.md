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

**live-peers** (22)
```bash
peers="82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,1c398af2208984d4e59bc41132e3eac0508abb0f@95.216.76.251:26656,2440091b1af9ae9e038dcfd4a46e17dc204d9f6d@18.159.135.176:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,6e9b0cf3ea78a9a540c75a4cfeb0c6a54b73fee4@65.108.127.166:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,a5edb41ef3ec40d09bc59a62f4337fc572971ab2@89.149.218.47:26656,b4241bd0c5c24ef09338f83d513c0c381a55c996@3.15.176.200:26656,94e69330d6f4cfe221cdd2ce49ee141e53e5f200@23.106.120.6:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
