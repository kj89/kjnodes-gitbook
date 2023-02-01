# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt)

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

**live-peers** (21)
```bash
peers="83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,ff7ab7fdac43752163f141809b61c67eba837cb4@65.108.97.58:37656,9bcaee1ad957fa75f60a6dd9d8870e53220794a9@104.37.187.214:60756,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,039a1c4f438c1ecc2dd901e7316d16fdafadfdab@104.193.254.36:27656,e08efc0b0e15e4d8eacf0f4ed5e52f6e9bdc312d@144.76.97.251:36156,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
