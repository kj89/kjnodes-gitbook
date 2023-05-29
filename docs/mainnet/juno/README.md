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

**live-peers** (12)
```bash
peers="b493c0311160cb6c00f483b2b10ff1e9968a73a5@65.108.122.246:26716,ca62ff6f732fcd391f1d9ef0630161cb595c7f4d@185.119.118.115:2000,d83892be2e6efc38e255943ce86ae8229d2aee90@178.128.220.188:26656,b2bc63857693bf901ea76865cd08fa319fee26b5@148.113.8.63:12656,32e56362f47c425328bd29bfa913fe188de4c69e@51.38.53.101:26620,7f593757c0cde8972ce929381d8ac8e446837811@178.18.255.244:26656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15756,e7c642bdd79fd79cd2677f4f8b1351236b5ec2f3@204.16.241.208:26656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
