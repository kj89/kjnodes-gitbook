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
peers="34aaa6b0eac3cb0b6f8d0ecb1795d7b50239b6bf@65.108.121.251:26656,7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,6b55539058ec85bcc38abb53604e0fa679336261@65.108.64.107:26656,f3cee9895a0be20067b1aa2ca3fd7ede59ee0b71@83.149.102.56:33095,169022205f5811e2a0b31b6d3cf11e8a6dfb8242@116.202.192.156:26656,bc7fe9a419584ff96c507ede7af811e0c5eba8b7@35.176.225.244:26656,8dd5dfefe8959f7186e6c80bdb87dbd919534677@18.223.174.1:45508,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656,fd29227cd0971725542a10173bbc629ecd074666@47.147.226.228:39656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
