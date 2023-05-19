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
peers="0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,f1fe0a080d561d37a94bea6022cbc0972395a0f4@65.108.121.190:2000,1c02ae0be21e3b08d9beadf91c26aec4193d2659@135.181.22.238:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,a2024229e2eed1650ba3a3ea9db67fa318dc232e@142.132.199.3:26656,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,c7fb97358712f447ca0689e814fe8c965a71b314@65.21.133.114:26656,27e14df66c9e4cd6b176b0dca6adfa9b6750f911@5.161.72.103:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
