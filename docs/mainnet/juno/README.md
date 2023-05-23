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
peers="b2bc63857693bf901ea76865cd08fa319fee26b5@148.113.8.63:12656,fdbbf603e09e1fffb54518ea8bf5ebc9a7b95152@93.189.30.70:26656,f3cee9895a0be20067b1aa2ca3fd7ede59ee0b71@83.149.102.56:33095,ca62ff6f732fcd391f1d9ef0630161cb595c7f4d@185.119.118.115:2000,7832e05394c2251c6e6a5a1caf7b660f1fe403d7@195.3.223.108:36656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,c5a2f8d48055b4b9f2f3e231900d2b0e48159d34@95.216.17.104:27655,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,169022205f5811e2a0b31b6d3cf11e8a6dfb8242@116.202.192.156:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,d8f1174a61bf1708f167163f8986db59c6695a29@171.244.137.23:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
