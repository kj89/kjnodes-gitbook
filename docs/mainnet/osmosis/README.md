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
peers="e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.234:26656,253bc0e57f48cb4f70493e6109b756208e20e8fe@135.181.171.121:26656,0419c998d6aac0afdb05808ad9a935670248e209@65.108.204.56:26656,4e38d3caa1554d7f46a2654fa9997554c13f61f2@95.216.96.61:26656,e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,f9a920a61ee994b12b77178dd5f1fc1ed39b7cd2@142.132.255.49:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956,29ecd1a65ce2c244ca90a1d190b3b8e58eed1ada@51.81.106.237:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,ab4ea418db1c65c2517975988e2f35891637ff4a@185.111.159.235:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
