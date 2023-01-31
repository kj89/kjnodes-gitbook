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

**live-peers** (21)
```bash
peers="2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,dd3cab79ffae0aed4f519503b66e9403c69eeb14@85.237.193.101:25565,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,ff94a29e02de8369faf37c76d3c97684bbd51bd6@185.16.38.165:17556,6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,68205c025ec65bf4d4183691d19d15b0a72221ec@65.108.42.185:26656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,8f68e41b8df40ea1f30ae2cae707bcc07f2da57f@51.79.27.21:14656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,7adbbe1a5f867a0befcf1fd94f395dd8257d718f@73.40.151.121:57656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
