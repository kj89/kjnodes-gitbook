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
peers="6178f129efa76d235436e2156959d0acb4772c6a@65.108.128.168:36656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,d4e6a9d74abbf4676c8fd2d58d27fc24b59056b9@143.198.22.206:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:29656,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,f9bfc7f25f63bd7e392fbe5465126b311465cbce@65.108.78.186:26656,ec929701754be057fb38c824fc127e26add9c900@138.201.121.185:26666,747d01891a83d6f759d88f9be07159c268b584b0@141.95.65.98:26656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,d90150d606724bb19d533f861024174f3aa42351@213.239.213.115:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,569aac51b04607a18696c63035586816dec85511@157.90.213.235:26656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,fc590afe489a1b9ca8ff3f2fb396dbc20b1997a4@204.16.244.254:26656,bda8361db3939be2871b5dfb52131cf7d9d38004@18.159.135.176:26656,21ce481af9984b37ee7337a87c28da4e14eb72af@52.12.69.48:26656,27a98ff24502c088a28e1e1b82a0e063ce2ab838@3.15.176.200:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
