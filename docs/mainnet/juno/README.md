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

**live-peers** (13)
```bash
peers="169022205f5811e2a0b31b6d3cf11e8a6dfb8242@116.202.192.156:26656,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,32e56362f47c425328bd29bfa913fe188de4c69e@51.38.53.101:26620,b493c0311160cb6c00f483b2b10ff1e9968a73a5@65.108.122.246:26716,0ed395467f8a74dfaa8c72d8e34234bfc3f36746@49.12.176.140:26656,2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,45f4da091b7f7536c3e0182083ff2326d0c3be6a@66.85.137.122:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656,f3cee9895a0be20067b1aa2ca3fd7ede59ee0b71@83.149.102.56:33095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
