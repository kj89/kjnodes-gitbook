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

**live-peers** (20)
```bash
peers="a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,c0b6d010bb442ff6511bc6fdde1f319b8a3a3bdc@65.108.127.50:17556,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,e61861653d42ebe5d7bf46d4c61f3753091985cd@83.53.221.249:36656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,ad8afbc89ac64db1ee99fdd904cbd48876d44b7d@195.3.222.240:26256,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,328606ae735133063d4504037e14fd0af934596a@51.89.118.48:14656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,39b55b1c49ad0994bbead006be40d9c84b0bf2d4@78.107.253.133:28656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
