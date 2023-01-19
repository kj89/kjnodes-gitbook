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

**live-peers** (18)
```bash
peers="d0313585956c8e7969993c1577f4969739b19bb7@85.10.238.147:26656,d9abd1dd5bf7c57461f0476c61e28bac879430a2@141.94.109.71:10556,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,316864671ec9566a3d07b64040c45e3fc75ccf36@65.108.201.154:5020,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,39b55b1c49ad0994bbead006be40d9c84b0bf2d4@78.107.253.133:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
