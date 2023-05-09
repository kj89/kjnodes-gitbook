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

**live-peers** (15)
```bash
peers="b493c0311160cb6c00f483b2b10ff1e9968a73a5@65.108.122.246:26716,6b55539058ec85bcc38abb53604e0fa679336261@65.108.64.107:26656,285b8d9cabcc9423b419c603c9d5e4cf216082e0@74.118.140.100:26656,5292be1e0829141ce28e01de3234a2060d592802@198.244.176.186:36656,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.8:26656,c11bbb68486bdbff6e19f3eec029686b6d5eac32@65.108.121.190:2030,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,02158734569117ff9a94ca2e07e6b8144a1d343b@78.46.88.98:26656,2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
