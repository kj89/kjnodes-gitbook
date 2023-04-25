# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/juno.png" width="150" alt=""><figcaption></figcaption></figure>

Juno is a global, open source, permission-less  network for decentralized interoperable applications.

**Chain ID**: juno-1 | **Latest Version Tag**: v14.0.0 | **Wasm**: ON

[Website](https://www.junonetwork.io) | [Discord](https://discord.gg/qJxgUSGHbb) | [Twitter](https://twitter.com/JunoNetwork)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/juno](https://explorer.kjnodes.com/juno)

## Public endpoints

* api: [https://juno.api.kjnodes.com](https://juno.api.kjnodes.com)
* rpc: [https://juno.rpc.kjnodes.com](https://juno.rpc.kjnodes.com)
* grpc: juno.grpc.kjnodes.com:57090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@juno.rpc.kjnodes.com:57656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@juno.rpc.kjnodes.com:57659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/juno/addrbook.json > $HOME/.juno/config/addrbook.json
```

**live-peers** (14)
```bash
peers="a492330151835e4cbc8c7bca2d77007a4ff2178e@65.21.235.147:26656,ae1b388ee37b03d0eb292342341e969de695c427@65.108.235.34:2000,2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,9f8cd938d81d4232517ac1d29bd1510e3aac5ce4@146.59.52.95:33095,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,1e95f780f110ca2335ecd09dca1927a9b5bb0090@154.12.241.136:26656,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.232:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,d8f1174a61bf1708f167163f8986db59c6695a29@171.244.137.23:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,82588f011491c6100d922d133f52fc23460b9231@95.217.91.232:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
