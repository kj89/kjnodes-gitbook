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

**live-peers** (27)
```bash
peers="c2ca1d57bb5178d442bd446cb04a2d0272ebe526@65.144.145.234:26656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,ad41936e5f89b119fdaae25fef0652949770f06e@185.107.57.74:26656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,637166728d6103ad4ec9fff97a321a024bff3e58@65.109.94.221:28656,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26906,57d82676ab660e8e4471664d7fee18e3e2e3dd19@89.58.38.59:26656,e5a142be860ee9b2f5c71d813e39fceb12cbd218@78.46.78.83:26686,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
