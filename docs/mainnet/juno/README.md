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
peers="b493c0311160cb6c00f483b2b10ff1e9968a73a5@65.108.122.246:26716,ca62ff6f732fcd391f1d9ef0630161cb595c7f4d@185.119.118.115:2000,7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,b2bc63857693bf901ea76865cd08fa319fee26b5@148.113.8.63:12656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,ae1b388ee37b03d0eb292342341e969de695c427@65.108.235.34:2000,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,155de67d7cd7f63c7aa070b9f99ab806736ba124@74.96.207.58:25656,285b8d9cabcc9423b419c603c9d5e4cf216082e0@74.118.140.100:26656,1c80957b5fde63a30771400342971ff67296d7c0@51.91.70.90:27656,c11bbb68486bdbff6e19f3eec029686b6d5eac32@65.108.121.190:2030,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
