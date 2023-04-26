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
peers="abd37ab4036f8b1cac9ba901529391f30681476c@194.163.128.55:26656,1e95f780f110ca2335ecd09dca1927a9b5bb0090@154.12.241.136:26656,32e56362f47c425328bd29bfa913fe188de4c69e@51.38.53.101:26620,70fcee92283edc02340289b2a74e4ab1a0203848@116.202.236.59:39656,e7c642bdd79fd79cd2677f4f8b1351236b5ec2f3@204.16.241.208:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:27136,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656,86bc38c6148fac78e8fa4ffa567b6ca444c4e7e2@88.198.47.84:26656,b493c0311160cb6c00f483b2b10ff1e9968a73a5@65.108.122.246:26716,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,fff4bfc18221feae05a92f54faa32dd2492d1c70@168.119.50.205:36656,2832bdb0a1bdddb2b17d1229a799290222c085d0@135.125.189.131:33095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
