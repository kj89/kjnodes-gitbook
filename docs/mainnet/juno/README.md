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
peers="ec562c5d3f8eff265be3557f455ae761d04469ae@95.217.202.49:34656,34aaa6b0eac3cb0b6f8d0ecb1795d7b50239b6bf@65.108.121.251:26656,2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.8:26656,155de67d7cd7f63c7aa070b9f99ab806736ba124@74.96.207.58:25656,0ed395467f8a74dfaa8c72d8e34234bfc3f36746@49.12.176.140:26656,f3cee9895a0be20067b1aa2ca3fd7ede59ee0b71@83.149.102.56:33095,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,d8f1174a61bf1708f167163f8986db59c6695a29@171.244.137.23:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
