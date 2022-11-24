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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656,eeb3b41fe019e4f75314c130aa83e2e0e8dcbd31@150.136.124.196:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,a35cc47b1025162b82b2220fb7dd20a438866742@157.90.93.245:26656,2240ec8c6271ab9a7e8ccf108f78a43c2521d3e6@34.125.189.191:26656,8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,bc0eeeabdc558cdb39f4a8148b5022ba537512b4@46.166.138.217:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
