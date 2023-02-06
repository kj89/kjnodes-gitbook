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

**live-peers** (33)
```bash
peers="d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,f7b5bc8e8eb8a954f9c36ac7c06ff7b9b847c785@167.86.82.140:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,e2172f53b4c59ed157d97802dc6b5ae8b17d3bb1@109.236.81.221:46656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,b08a57014e190c241bd1ef5705bfc93625742030@65.21.77.173:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,c2ca1d57bb5178d442bd446cb04a2d0272ebe526@65.144.145.234:26656,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,039a1c4f438c1ecc2dd901e7316d16fdafadfdab@104.193.254.36:27656,fa116b94190a93c092e4dadedec950bf3e00caca@86.32.74.154:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,a13b5c78c65b785f4189a7873015c47217f2c83c@65.108.13.185:27565,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,9c149b35243970e1f8e0519f1f33f79f7d5bd91b@51.38.52.188:26638,39b55b1c49ad0994bbead006be40d9c84b0bf2d4@78.107.253.133:28656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,2bb49680d595628991383323806db3fa53d15eb5@65.109.85.170:53656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.134.170:26676,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,f460d33619705cb145d88631115a0b5581515060@165.232.173.74:26656,709d70730cbcbefd10071d316fd099160b84aced@203.135.152.216:26656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
