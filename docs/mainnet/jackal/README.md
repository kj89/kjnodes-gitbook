# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
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

**live-peers** (22)
```bash
peers="6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,d9abd1dd5bf7c57461f0476c61e28bac879430a2@141.94.109.71:10556,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,f6aaf53be76e005f83376ceca6d26d30ac93d42c@46.4.81.204:33656,2747cd770717937021e66d3da8b730c666d74ae6@65.109.93.152:36156,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,ad41936e5f89b119fdaae25fef0652949770f06e@185.107.57.74:26656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,4bfc9e0f762e952b76daee87e9ffd081d2974f75@31.156.233.3:26656,0b8bbc839c20b07ac5999bca7d905d53274c5f2d@24.158.14.214:36656,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@24.158.14.212:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
