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

**live-peers** (20)
```bash
peers="6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,e5a142be860ee9b2f5c71d813e39fceb12cbd218@78.46.78.83:26686,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,2747cd770717937021e66d3da8b730c666d74ae6@65.109.93.152:36156,83d66a37202785b09aee4e3ae1b50d2ddfbf860c@162.19.89.8:10856,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,399068f8371dce4ae5d7cd7da2c965e765e68f4b@65.108.238.102:17556,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,db9c7d34cd04e155b3eed730f68fc9315245cf5c@65.108.124.219:30656,01aca4ff5fcbffb1b4d66ea3ecffb11e9680038c@70.71.164.192:37656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,bc6ce122e5809b06dcf90742ee40091f3ee6bcee@142.132.248.253:42656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
