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
peers="2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,155de67d7cd7f63c7aa070b9f99ab806736ba124@74.96.207.58:25656,a41df74bb4a1f83af77b47c32daf86176b3e6533@162.19.171.42:10056,3aa00177a41ff8cedebf9f3f7f4358c1795ff3ea@185.207.250.206:50016,c11bbb68486bdbff6e19f3eec029686b6d5eac32@65.108.121.190:2030,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.8:26656,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,9bc2e3a6ccee63366cf862afe33635fcc841acc9@154.53.41.185:10043,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
