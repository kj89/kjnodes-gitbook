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
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaiad/config/addrbook.json
```

**live-peers** (10)
```
peers="89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,3c7cad4154967a294b3ba1cc752e40e8779640ad@84.201.128.115:26656,dd53fa5cfb6a604feb80860d47506d0dd84baa12@142.132.210.234:26656,8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656,f76c4c9529afcf1f1e8334e39e3aed5771e33bef@144.91.127.3:26676,1ce6b62ec8233f91d4383026dcd6e6f85da4de67@147.135.39.188:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,0848802b3a558aa18ba25ba3fbe6aea3486241a1@23.88.72.109:26696,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
