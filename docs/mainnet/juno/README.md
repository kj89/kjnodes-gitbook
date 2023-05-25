# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/juno.png" alt=""><figcaption></figcaption></figure>

Juno is a global, open source, permission-less  network for decentralized interoperable applications.

**Chain ID**: juno-1 | **Latest Version Tag**: v14.0.0 | **Wasm**: ON

[Website](https://www.junonetwork.io) | [Discord](https://discord.gg/qJxgUSGHbb) | [Twitter](https://twitter.com/JunoNetwork)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/juno](https://explorer.kjnodes.com/juno)

## Public endpoints

* api: [https://juno.api.kjnodes.com](https://juno.api.kjnodes.com)
* rpc: [https://juno.rpc.kjnodes.com](https://juno.rpc.kjnodes.com)
* grpc: juno.grpc.kjnodes.com:15790

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@juno.rpc.kjnodes.com:15756
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@juno.rpc.kjnodes.com:15759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/juno/addrbook.json > $HOME/.juno/config/addrbook.json
```

**live-peers** (14)
```bash
peers="7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,155de67d7cd7f63c7aa070b9f99ab806736ba124@74.96.207.58:25656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.232:26656,97f76286b6815e84c6bd457beb7c59d821c0b852@141.95.72.198:26656,e7094d5f8cd5c4bd69605f0b68e98681eb6eb881@37.59.21.96:12656,a3b9b97aba75a6c495f028240146fdcf2a40adf8@89.149.218.192:26656,7832e05394c2251c6e6a5a1caf7b660f1fe403d7@195.3.223.108:36656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,b493c0311160cb6c00f483b2b10ff1e9968a73a5@65.108.122.246:26716,7c0f7dc5942eab79def1a189175464952efa4d68@51.178.74.75:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
