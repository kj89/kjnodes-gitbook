# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at every 5 minutes)
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

**live-peers** (30)
```bash
peers="ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,a877c11ecef83401dcc96c4499874ebc3f13367b@116.202.36.240:10756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,7751d16cfa48da0a5bea6f40e9bcc386b4c76c50@51.89.7.184:26638,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,b55e7c342620b73cbc9572604d1c2146892231d6@194.34.232.124:34656,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,ac6e9b3fc2d18f51aa8d6f98bae9e05acfac97e1@176.42.25.134:26656,f42498ca4d9e62f95115f04ae18fa5ec1c1487f1@65.108.141.109:18656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,2b7f02456898efbbb9da462b9b3e80ba12ff2f7c@65.109.116.50:27656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,3ebc427c4aea796e7eea5551e8bca74a7734fe52@65.144.145.234:26656,35986ec8d12abb75a2cd85b3102cee012dd90dd0@89.245.24.94:20356,f460d33619705cb145d88631115a0b5581515060@165.232.173.74:26656,6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,fa116b94190a93c092e4dadedec950bf3e00caca@86.32.74.154:26656,20e1000e88125698264454a884812746c2eb4807@65.108.227.217:17556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
