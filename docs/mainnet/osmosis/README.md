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
peers="31d2c86f7957e2db91297e54c3b0456ea06c2250@173.67.177.115:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,a50c8dcd0e83032b5e29d5c5beef6e54ddafb508@35.83.253.164:26656,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,9203fbde463bd66bb451da3de390c7d3515c2bf2@65.108.46.248:26656,2f4c0337b2522034a614a5cb2c61a891fe753c03@5.9.81.187:29656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,4a837e3411b0281f00c07706cfea72d3ebc575f1@176.9.38.49:26656,ef30bc7dbac63eb868e66bad497368f2cd0924e1@141.98.217.102:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
