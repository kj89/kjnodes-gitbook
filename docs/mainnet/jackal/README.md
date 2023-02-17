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
peers="66ccc1f81b9922ea33fed598c77b491761d79cbb@65.108.77.250:36656,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,b3f167a06a8691d738de5fff2b3ba65053e0787d@65.21.183.76:26656,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:15656,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,2ec46ff04ebfafc19f505feaaf00943c15bb2757@185.16.38.149:26656,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,6e77de9c0b8364fb67fc1e86e2b7a8ac89f96d45@194.163.150.92:37656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,4fa82212d657a171b1f4d3f21da33041f5cff9f9@65.21.88.172:31656,fc905fe58d36875a833202ce53759d0ae6c11435@141.95.65.26:48656,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,2bb49680d595628991383323806db3fa53d15eb5@65.109.85.170:53656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,68eb09cb9c5a2b136e8c693a48bcb26d9108062f@157.90.2.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
