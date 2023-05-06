# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/osmosis.png" alt=""><figcaption></figcaption></figure>

Osmosis is a DEX protocol, which means it uses smart contracts  to determine the price of digital assets, to produce liquidity  via a peer-to-peer (P2P) methodology, and to exact trades between users

**Chain ID**: osmosis-1 | **Latest Version Tag**: v15.0.0 | **Wasm**: ON

[Website](https://osmosis.zone) | [Discord](https://discord.gg/osmosis) | [Twitter](https://twitter.com/osmosiszone)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/osmosis](https://explorer.kjnodes.com/osmosis)

## Public endpoints

* api: [https://osmosis.api.kjnodes.com](https://osmosis.api.kjnodes.com)
* rpc: [https://osmosis.rpc.kjnodes.com](https://osmosis.rpc.kjnodes.com)
* grpc: osmosis.grpc.kjnodes.com:12990

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@osmosis.rpc.kjnodes.com:12956
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@osmosis.rpc.kjnodes.com:12959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/osmosis/addrbook.json > $HOME/.osmosisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,914865f0b02d76c48c5369457cf5aa4173d06ed8@54.169.236.90:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,95dbddda671081fb433871fa612ff5291242d93d@45.67.221.200:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.234:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
