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
peers="ef30bc7dbac63eb868e66bad497368f2cd0924e1@141.98.217.102:26656,f1fe0a080d561d37a94bea6022cbc0972395a0f4@65.108.121.190:2000,82e224c9640048a6513c589e904c0d903bb99f32@74.118.140.23:26656,88fa3de90d06422b409ce6beb2367b94b2a1759e@51.79.17.73:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.169.71:26656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,a8a72dce31fdd36db889b1203d9af5fb7155e4d3@65.108.122.246:26686,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
