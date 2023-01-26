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
peers="c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,328606ae735133063d4504037e14fd0af934596a@51.89.118.48:14656,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,f7b5bc8e8eb8a954f9c36ac7c06ff7b9b847c785@167.86.82.140:46656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,3e352224da2a8487d2c6277dc40d120cd574acb9@65.21.90.141:12133,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,a77da5b3ce86a5226bae6e7b87964dd4efe8fe46@65.21.170.3:31656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,ac6e9b3fc2d18f51aa8d6f98bae9e05acfac97e1@176.42.25.134:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
