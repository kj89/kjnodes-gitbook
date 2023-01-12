# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/jackal.png" width="150" alt=""><figcaption></figcaption></figure>

The Jackal Protocol is a fast, scalable, and secure blockchain that empowers  individuals, developers, and enterprises to increase their data privacy and  cybersecurity posture without sacrificing ease of use. This protocol strives  to offer world-class applications to protect the planet's most important data–your data.

**Chain ID**: jackal-1 | **Latest Version Tag**: v1.1.2-hotfix | **Wasm**: ON

[Website](https://jackalprotocol.com) | [Discord](https://discord.com/invite/5GKym3p6rj) | [Twitter](https://twitter.com/Jackal_Protocol)

## Restake

[Restake with kjnodes](https://restake.app/jackal/jklvaloper1tr3wm3mdkz0tda6t7vavqnn7fe2g4un0f67xmt) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://jackal.rpc.kjnodes.com](https://jackal.rpc.kjnodes.com)
* api: [https://jackal.api.kjnodes.com](https://jackal.api.kjnodes.com)

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
peers="dd7e72f0a71476e51c0a601a40d6fc02a1ae1a95@65.108.6.45:60856,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,6fb595ce8c3a58ce4498537ddfe5333f36a24957@38.242.250.7:26646,0faa7f1099de2e02deebe09fcb52863056333265@144.202.72.17:26616,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,d942eeeae4fc5e34c3af009b17db52fec9ee83e7@96.234.160.22:26656,4118b172fc2a45e0335c59641fd7c2e5e5e2c53c@65.108.238.203:28656,2a55d2e6cc5fa2dda8a484ab7d00f77f076d237f@141.95.47.216:26656,173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,289c3e984194ac2ccaa74e201147010648e90970@195.3.223.108:26656,01aca4ff5fcbffb1b4d66ea3ecffb11e9680038c@70.71.164.192:37656,a4a4168d22313a9d34e5e6c208e053292096864d@66.85.149.162:43656,4398bd773ac885b7365de3604eb487be10c54563@185.16.38.210:26906,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,709d70730cbcbefd10071d316fd099160b84aced@203.135.152.216:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
