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
peers="84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656,2e6f37cfbc4549c23f4ec48e9de68203858b62fc@51.38.52.99:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,c6f03336e99b15b104048a1af056063107389441@18.142.7.52:26656,aea820ece7c45c0a8b5dababc9ea813f7eb62638@93.186.201.125:26656,d9dbd30f7e9ae99dc05645f48f4637c2f4a14645@34.107.9.71:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,73c2a86cc0d4b51c81bd0e36cee69f1731bcda0d@23.88.69.157:26656,701036e718d0746d1d7055fb0fd1245cf361e0b8@168.119.79.106:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
