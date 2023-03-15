# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v14.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)




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

**live-peers** (20)
```bash
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,4d659b7b244a68913bfbdc6c9e7aa1a64391238e@74.118.139.59:26656,9b1bfb99d9eb04af32510ed8e3eb83c59448662f@95.214.52.220:26656,8e72d0b37a9dc16ea58c0da705caa6530badd6ce@138.197.68.193:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.122:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,5e9051d2ae7d9be1656a5348ad0916f255b96c73@135.181.214.17:26656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,60a2c89e7253502e93517a026f44a2431cc81230@220.85.113.39:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
