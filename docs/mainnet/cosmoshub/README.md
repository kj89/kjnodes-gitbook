# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v7.1.0 | **Wasm**: OFF

Website: [https://hub.cosmos.network](https://hub.cosmos.network)


## Public endpoints

* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:34656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (10)
```
peers="73c2a86cc0d4b51c81bd0e36cee69f1731bcda0d@23.88.69.157:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,701036e718d0746d1d7055fb0fd1245cf361e0b8@168.119.79.106:26656,eafee411e6d5840d1c59aacb696893ab82b7fb38@35.194.41.158:26656,a94dff85ed430f0475f41fe306c82b7eb7f6e858@51.91.153.78:31649,37dfe1ec33e9f88f378a61a32462d57d2baa5e74@65.108.99.140:26656,aea820ece7c45c0a8b5dababc9ea813f7eb62638@93.186.201.125:26656,8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656,ed53d253068e44a1233798a08d82f7ac4897c5f3@54.251.217.58:26656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
