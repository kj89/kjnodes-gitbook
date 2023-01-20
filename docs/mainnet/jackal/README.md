# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)
* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* grpc: [https://jackal.grpc.kjnodes.com](https://jackal.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (19)
```bash
peers="fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,ad41936e5f89b119fdaae25fef0652949770f06e@185.107.57.74:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,f6aaf53be76e005f83376ceca6d26d30ac93d42c@46.4.81.204:33656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,2747cd770717937021e66d3da8b730c666d74ae6@65.109.93.152:36156,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
