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

**live-peers** (15)
```bash
peers="6b55539058ec85bcc38abb53604e0fa679336261@65.108.64.107:26656,f3cee9895a0be20067b1aa2ca3fd7ede59ee0b71@83.149.102.56:33095,155de67d7cd7f63c7aa070b9f99ab806736ba124@74.96.207.58:25656,b9f18cfdcec405987335681eccb5ab3288225846@141.95.155.224:10056,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,1e95f780f110ca2335ecd09dca1927a9b5bb0090@154.12.241.136:26656,285b8d9cabcc9423b419c603c9d5e4cf216082e0@74.118.140.100:26656,9f8cd938d81d4232517ac1d29bd1510e3aac5ce4@146.59.52.95:33095,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,e7c642bdd79fd79cd2677f4f8b1351236b5ec2f3@204.16.241.208:26656,16b3cfebe67be36a72db0e170f4e4191aa938457@65.108.10.138:2000,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
