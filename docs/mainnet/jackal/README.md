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

**live-peers** (17)
```bash
peers="173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,588e509e3a8c1dc4ba938779bf569cd9f6f0f4be@212.23.222.109:26256,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,aca915dcd2087459a5d3e400b707ce1932f91401@65.108.229.102:56656,46d4495643f2579573a61e181a88de3b8f0acc4f@2.139.23.24:36656,e2172f53b4c59ed157d97802dc6b5ae8b17d3bb1@109.236.81.221:46656,d39fecbc409541de13fa644d90066d4dabe08262@95.165.89.222:24475,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,d0313585956c8e7969993c1577f4969739b19bb7@46.4.88.116:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
