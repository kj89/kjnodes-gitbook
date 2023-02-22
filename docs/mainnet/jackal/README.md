# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every 5 minutes)
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

**live-peers** (34)
```bash
peers="dbbd1e102b9d0cde827cd272205fa3a2886a6b2c@5.9.147.22:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,552795aa54d6a3a81c7474c6caf8c2a879f7159e@65.109.188.119:46656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,24d557203af1734d8a9e94d1819f0920ee66845c@185.252.235.83:27656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,4fa82212d657a171b1f4d3f21da33041f5cff9f9@65.21.88.172:31656,cda2f5ee8d1feff1a5136e17a17b4a3a374a6f49@65.109.106.172:32656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:15656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26906,80cc4b90a546a138a480642dd5ce0fcf65ba2d8c@65.108.41.172:29956,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,dd7ee88ff1a81be43fb5ed12c416cd23fd065f8e@65.109.69.154:32656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,159834da1073b793a9f6730841d827802051ed75@198.244.178.213:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,4a0fb6863526b3370b3f0dcba6bc2d548a363974@65.109.52.56:2506,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@135.181.5.219:17556,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,f42498ca4d9e62f95115f04ae18fa5ec1c1487f1@65.108.141.109:18656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,cebe2ad7290ce193069a938910905518a37f40c0@35.242.237.47:26656,2bb49680d595628991383323806db3fa53d15eb5@65.109.85.170:53656,ae69a9186ee7fc09d4c46e76ee0ebea537171937@94.130.137.122:33656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,c2ca1d57bb5178d442bd446cb04a2d0272ebe526@96.73.27.73:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
