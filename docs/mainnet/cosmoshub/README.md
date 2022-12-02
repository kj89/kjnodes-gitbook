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
peers="aea820ece7c45c0a8b5dababc9ea813f7eb62638@93.186.201.125:26656,34f0e424f747f62e04e8c34fde60013fb4dbc04b@65.108.0.165:14956,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,52a6b8f416ba3ed2aafa72e35df28ee4c3ee547b@5.9.108.156:36656,989f4e22208c3a77bd8b550ce68d8ad23e5bdda7@18.222.251.112:26656,701036e718d0746d1d7055fb0fd1245cf361e0b8@168.119.79.106:26656,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
