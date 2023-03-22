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

**live-peers** (19)
```bash
peers="e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,32e9d4a7413dd5393c8be004bee68dea683be839@65.21.227.95:2004,b69e57cd6f796ac5d6efb1a834163365c37cbfa8@78.46.69.29:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,729219c108c059824ea9a17c09d11adc99226db4@66.172.36.139:36656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,980b15331dece2aa8020c1800b9c00ddb273c872@138.201.32.103:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
