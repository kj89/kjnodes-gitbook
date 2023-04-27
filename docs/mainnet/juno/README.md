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

**live-peers** (14)
```bash
peers="2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,ae1b388ee37b03d0eb292342341e969de695c427@65.108.235.34:2000,16b3cfebe67be36a72db0e170f4e4191aa938457@65.108.10.138:2000,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.161.208:26656,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.8:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.120:26656,e7c642bdd79fd79cd2677f4f8b1351236b5ec2f3@204.16.241.208:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,bc7fe9a419584ff96c507ede7af811e0c5eba8b7@35.176.225.244:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656,bba10290da32f3cb41e15c3a192413666ce05cee@5.9.208.8:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
