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
peers="3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,c5358545d951ae666c695903036c1e93578951eb@135.181.176.113:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,6b1dd134b30aeaeb2f21f33bd2cd0370a2275501@138.68.6.165:26656,d0d4b88110767c503baa8a618cfd7e284482f8dc@37.120.245.11:26656,ea5ce509e09790c70609c8dc87ad4b19a0f98855@168.119.108.203:26656,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
