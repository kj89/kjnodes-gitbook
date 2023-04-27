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
peers="2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,169022205f5811e2a0b31b6d3cf11e8a6dfb8242@116.202.192.156:26656,34aaa6b0eac3cb0b6f8d0ecb1795d7b50239b6bf@65.108.121.251:26656,7832e05394c2251c6e6a5a1caf7b660f1fe403d7@195.3.223.108:36656,285b8d9cabcc9423b419c603c9d5e4cf216082e0@74.118.140.100:26656,b2bc63857693bf901ea76865cd08fa319fee26b5@148.113.8.63:12656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,eee69cc98a6d5e336164697188ed2eb3631dce8c@85.237.193.95:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,97e4468ac589eac505a800411c635b14511a61bb@5.9.239.232:26656,aab8ab60cdf7b12e88661d65cd1ef7d78905951b@66.172.36.139:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
