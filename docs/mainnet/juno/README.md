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

**live-peers** (13)
```bash
peers="e726816f42831689eab9378d5d577f1d06d25716@23.88.22.8:26656,3087e068a1eec50768fc426e0e8687c2a37343a7@159.69.205.84:26656,7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,930600e82ae17023438e7caef7b6dd38a4adb2b0@65.108.201.154:3010,9f8cd938d81d4232517ac1d29bd1510e3aac5ce4@146.59.52.95:33095,eee69cc98a6d5e336164697188ed2eb3631dce8c@85.237.193.95:26656,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.232:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,0c3348fdf301d4f3b88bcebe093ddca9e0cd0c02@135.181.128.114:12656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
