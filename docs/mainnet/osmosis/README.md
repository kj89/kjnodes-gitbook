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

**live-peers** (11)
```bash
peers="e613079d9b1c1c688963215a975cc9b29722f4fb@65.108.238.103:12556,f3262b9f490720920b0002fadd500af1cef3e6a6@51.222.40.84:26656,406f64a8d601e34d7311fd61ec87b0c7028bd230@138.201.23.39:46656,e153cc49052d67280dfdd6d660f3d98622905850@209.133.193.74:26656,3197daa0ee5245b17a546be032ff0f6814e1d1db@148.251.191.239:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.169.186:26656,ac2fbcb5de633d136a942c28c3049e3edbc6e69a@85.239.233.61:2000,42f42a4b3527b927d5002d45abd37f66ecdd4861@51.178.74.75:16656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.10:26656,2048e1bc1f020fa210fb475e7a0ec0948919609f@185.217.125.64:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:12956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.osmosisd/config/config.toml
```
