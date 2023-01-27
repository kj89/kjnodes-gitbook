# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Chain explorer
[https://explorer.kjnodes.com/jackal](https://explorer.kjnodes.com/jackal)

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

**live-peers** (22)
```bash
peers="f42498ca4d9e62f95115f04ae18fa5ec1c1487f1@65.108.141.109:18656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,f7b5bc8e8eb8a954f9c36ac7c06ff7b9b847c785@167.86.82.140:46656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,c5b43622ecd7413dd41905f6f8f5b5befd299ced@65.109.65.210:32656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,ad8afbc89ac64db1ee99fdd904cbd48876d44b7d@195.3.222.240:26256,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,3ebc427c4aea796e7eea5551e8bca74a7734fe52@65.144.145.234:26656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,4bfc9e0f762e952b76daee87e9ffd081d2974f75@31.156.233.3:26656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:17556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
