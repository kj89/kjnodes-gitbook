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
peers="173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,11c23c5341d0ac69f9ebb3be9afa7fe0e134ece0@94.79.54.137:28656,f7b5bc8e8eb8a954f9c36ac7c06ff7b9b847c785@167.86.82.140:46656,5745d29dd5b49009f405e21913a474a23f1e40ec@131.153.57.226:43656,039a1c4f438c1ecc2dd901e7316d16fdafadfdab@104.193.254.36:27656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,3ebc427c4aea796e7eea5551e8bca74a7734fe52@65.144.145.234:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,7574e0ab179fc6cc47ac89284f4641790218540e@18.163.165.245:26626,26b6255375a592c3b0664bd474a6975f468c3785@88.99.164.158:11126,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,d942eeeae4fc5e34c3af009b17db52fec9ee83e7@96.234.160.22:26656,8314357f705b8ff9338d58f47fbea99294319cad@57.128.65.115:14656,55df88ae25223565af42ccd6b3b558b8e70bba31@213.239.216.252:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@95.214.52.139:26906,dbec14a10d43c25d77ee9987a985652fa4e6344a@131.153.59.6:26656,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,1f30e644ddd8edf310cbd9be4ac07b604eed581e@66.85.143.242:26676,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,01aca4ff5fcbffb1b4d66ea3ecffb11e9680038c@70.71.164.192:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.canine/config/config.toml
```
