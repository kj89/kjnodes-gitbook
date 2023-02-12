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

**live-peers** (31)
```bash
peers="26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,ff7ab7fdac43752163f141809b61c67eba837cb4@65.108.97.58:37656,ad8afbc89ac64db1ee99fdd904cbd48876d44b7d@195.3.222.240:26256,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,84abbfb6912262fa129ff65e4b56107820a00d65@135.181.214.121:31656,24d557203af1734d8a9e94d1819f0920ee66845c@185.252.235.83:27656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,b08a57014e190c241bd1ef5705bfc93625742030@65.21.77.173:26656,35986ec8d12abb75a2cd85b3102cee012dd90dd0@89.245.24.78:20356,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,66ccc1f81b9922ea33fed598c77b491761d79cbb@65.108.77.250:36656,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,39b55b1c49ad0994bbead006be40d9c84b0bf2d4@78.107.253.133:28656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.134.170:26676,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26906,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:15656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@94.23.23.189:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
