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
peers="0c3348fdf301d4f3b88bcebe093ddca9e0cd0c02@135.181.128.114:12656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,7f593757c0cde8972ce929381d8ac8e446837811@178.18.255.244:26656,f3cee9895a0be20067b1aa2ca3fd7ede59ee0b71@83.149.102.56:33095,d8f1174a61bf1708f167163f8986db59c6695a29@171.244.137.23:26656,32e56362f47c425328bd29bfa913fe188de4c69e@51.38.53.101:26620,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,b9f18cfdcec405987335681eccb5ab3288225846@141.95.155.224:10056,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,8dd5dfefe8959f7186e6c80bdb87dbd919534677@18.223.174.1:45508,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
