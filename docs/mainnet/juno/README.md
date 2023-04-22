# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/juno.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (13)
```bash
peers="ae1b388ee37b03d0eb292342341e969de695c427@65.108.235.34:2000,34aaa6b0eac3cb0b6f8d0ecb1795d7b50239b6bf@65.108.121.251:26656,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,285b8d9cabcc9423b419c603c9d5e4cf216082e0@74.118.140.100:26656,471518432477e31ea348af246c0b54095d41352c@88.198.131.120:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656,04b935b4d45b2f0d809701f7ae4180a7267b82cf@15.235.51.191:10056,70fcee92283edc02340289b2a74e4ab1a0203848@116.202.236.59:39656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,ca62ff6f732fcd391f1d9ef0630161cb595c7f4d@185.119.118.115:2000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
