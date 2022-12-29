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
peers="173c43436e2287f3660c344a5fd2386da4a61968@65.109.92.241:11126,7751d16cfa48da0a5bea6f40e9bcc386b4c76c50@51.89.7.184:26638,108652f503665772ad024d9d2129a9f4fa9ffe9b@176.9.98.24:30536,519f2b648a2a8794ac33b195f39b6d836e09f8f2@131.153.154.13:26656,a2afb42b65da7013eca54778ce01dfb877c2a82a@154.12.227.132:37656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:37656,0841db0ae5e5443905837e196d2e1ffd31f2e480@131.153.202.81:36656,c2842c76779913e05fa4256e3caab852e1782951@202.61.194.254:60756,6852add4eaa027707a6000c78ea9e7cde81b058f@18.118.26.4:26656,72f98b8ac9af924c77f52cdc26a78e7728d4e19d@24.158.14.212:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.canine/config/config.toml
```
