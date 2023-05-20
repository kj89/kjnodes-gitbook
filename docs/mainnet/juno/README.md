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
peers="b493c0311160cb6c00f483b2b10ff1e9968a73a5@65.108.122.246:26716,3aa00177a41ff8cedebf9f3f7f4358c1795ff3ea@185.207.250.206:50016,d8f1174a61bf1708f167163f8986db59c6695a29@171.244.137.23:26656,1e95f780f110ca2335ecd09dca1927a9b5bb0090@154.12.241.136:26656,71d6f44cd4ace21020437fba4139b5da8db60962@54.38.38.40:26620,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,0ed395467f8a74dfaa8c72d8e34234bfc3f36746@49.12.176.140:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,45f4da091b7f7536c3e0182083ff2326d0c3be6a@66.85.137.122:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
