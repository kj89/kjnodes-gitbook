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
peers="34aaa6b0eac3cb0b6f8d0ecb1795d7b50239b6bf@65.108.121.251:26656,a7bf18723f4757ce900f13cfb6a794de6a9d438a@198.244.229.100:26656,927b0c0775490e83781fa5fe3a90a3f70f069917@147.135.7.32:26656,155de67d7cd7f63c7aa070b9f99ab806736ba124@74.96.207.58:25656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.8:26656,f3cee9895a0be20067b1aa2ca3fd7ede59ee0b71@83.149.102.56:33095,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,7f593757c0cde8972ce929381d8ac8e446837811@178.18.255.244:26656,c11bbb68486bdbff6e19f3eec029686b6d5eac32@65.108.121.190:2030,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
