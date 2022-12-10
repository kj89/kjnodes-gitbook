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

**live-peers** (9)
```
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,241b17dba97a2ed3c3747d12781fb86c9706e2d4@89.58.27.86:26656,2938b48ed9dd80451f0be7d8e21840aa383ed929@34.239.177.249:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,07fc76b0a1dfcd25e3139a339728d50507bb5d96@67.209.54.35:26656,701036e718d0746d1d7055fb0fd1245cf361e0b8@168.119.79.106:26656,a94dff85ed430f0475f41fe306c82b7eb7f6e858@51.91.153.78:31649"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
