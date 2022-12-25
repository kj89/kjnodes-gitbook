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

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@jackal.rpc.kjnodes.com:37656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@jackal.rpc.kjnodes.com:37659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/jackal/addrbook.json > $HOME/.canine/config/addrbook.json
```

**live-peers** (10)
```
peers="173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@46.4.53.94:30565,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,7751d16cfa48da0a5bea6f40e9bcc386b4c76c50@51.89.7.184:26638,e258f57604c59fc02d07b9669ae64f00bb45a20c@162.205.240.139:37656,8d59eb5f7ad207e59c06620f6e9e7b6760b56211@65.108.75.107:18656,0985977a794b298e7ef990fe344d572c60c453b1@172.105.72.158:26656,a79da224ad9d4501dbf1d547986ebec55d56b951@135.181.128.114:17556,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,aca915dcd2087459a5d3e400b707ce1932f91401@65.108.229.102:56656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
