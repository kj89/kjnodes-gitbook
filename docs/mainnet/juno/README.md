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
peers="c44a49da8adf6ab86a26c9b7fa53da179597605b@85.10.243.90:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.197:26656,ca62ff6f732fcd391f1d9ef0630161cb595c7f4d@185.119.118.115:2000,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,ae1b388ee37b03d0eb292342341e969de695c427@65.108.235.34:2000,e1b058e5cfa2b836ddaa496b10911da62dcf182e@23.88.21.232:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,1e95f780f110ca2335ecd09dca1927a9b5bb0090@154.12.241.136:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,b2bc63857693bf901ea76865cd08fa319fee26b5@148.113.8.63:12656,285b8d9cabcc9423b419c603c9d5e4cf216082e0@74.118.140.100:26656,ae6075285a97b2edf699526085e298756f187f29@193.70.33.64:12656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
