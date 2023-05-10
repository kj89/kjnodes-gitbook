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
peers="b2bc63857693bf901ea76865cd08fa319fee26b5@148.113.8.63:12656,2d473ca3eb1cd728155ea12eb0b301eebccaec5e@162.19.89.8:10556,bc7fe9a419584ff96c507ede7af811e0c5eba8b7@35.176.225.244:26656,8dd5dfefe8959f7186e6c80bdb87dbd919534677@18.223.174.1:45508,b9f18cfdcec405987335681eccb5ab3288225846@141.95.155.224:10056,7d5548102518ef89a988960afcccba2504707a08@162.55.92.114:2030,6b55539058ec85bcc38abb53604e0fa679336261@65.108.64.107:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756,9f8cd938d81d4232517ac1d29bd1510e3aac5ce4@146.59.52.95:33095,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
