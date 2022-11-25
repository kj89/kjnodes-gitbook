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
peers="89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656,222385f3ce7f55f9c01c23f2ee340ed9548b18fa@35.222.169.98:26656,3da88430414ec9084c8983fe4d462cce655ff1f3@51.222.245.114:26656,4ed63a4748d04d1e0adfcdd240ab8ff43fbf41d3@89.149.218.202:26656,a35cc47b1025162b82b2220fb7dd20a438866742@157.90.93.245:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,6b3cd4f36112a1ef566974fb31e2998d2bc480b9@65.109.17.57:26656,0e71a3cbdddfe77ebff79378bf6ac07915e747dc@167.235.107.42:27002"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
