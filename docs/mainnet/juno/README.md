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
peers="df3001e7402d763e9e762592df3d32dbbe72edd0@74.118.140.21:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.197:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,7832e05394c2251c6e6a5a1caf7b660f1fe403d7@195.3.223.108:36656,efe1a34f49a0342257fd0ba3ca5ea20e51ee77d5@95.217.219.151:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,1e95f780f110ca2335ecd09dca1927a9b5bb0090@154.12.241.136:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,155de67d7cd7f63c7aa070b9f99ab806736ba124@74.96.207.58:25656,ba89aa161ae33ddffa508d57368bd2666a97bbe2@164.68.115.226:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
