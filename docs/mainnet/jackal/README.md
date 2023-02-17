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

**live-peers** (29)
```bash
peers="e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,8f68e41b8df40ea1f30ae2cae707bcc07f2da57f@51.79.27.21:14656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,d9abd1dd5bf7c57461f0476c61e28bac879430a2@141.94.109.71:10556,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,aca915dcd2087459a5d3e400b707ce1932f91401@65.108.229.102:56656,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,68b81df146d915f599775a18953bbefbd49d024a@193.70.33.64:17556,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,42909d7aedeb0a49dd9f4be1a2ba024bdd82fea2@65.144.145.234:26656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,ee2ef67b49cbc7b4af7ff0b7321870a5d9ae69a5@65.108.138.80:17556,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,a13b5c78c65b785f4189a7873015c47217f2c83c@65.108.13.185:27565,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,ac6e9b3fc2d18f51aa8d6f98bae9e05acfac97e1@217.131.117.217:26656,2b7f02456898efbbb9da462b9b3e80ba12ff2f7c@65.109.116.50:27656,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
