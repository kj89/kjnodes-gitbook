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
peers="7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:15656,8cb23f8ba742452f2f81f019a648f0660fabfd46@65.109.106.155:26656,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,b511a0e15ac7afad376d9ea21d43bcc5f4ad06b5@65.109.122.105:61756,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.55.198:26906,a877c11ecef83401dcc96c4499874ebc3f13367b@116.202.36.240:10756,d709f7aa02cb0d49bd94dde1f4b339b7ab2c433c@172.105.104.182:26656,4a0fb6863526b3370b3f0dcba6bc2d548a363974@65.109.52.56:2506,4fa82212d657a171b1f4d3f21da33041f5cff9f9@65.21.88.172:31656,159834da1073b793a9f6730841d827802051ed75@198.244.178.213:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,24d557203af1734d8a9e94d1819f0920ee66845c@185.252.235.83:27656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,460cf6a14f3fa0f3882400fbdcb80033105cac79@178.154.241.46:26656,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,ac6e9b3fc2d18f51aa8d6f98bae9e05acfac97e1@217.131.117.217:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@135.181.5.219:17556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
