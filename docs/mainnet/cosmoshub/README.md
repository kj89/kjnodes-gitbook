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
peers="34f0e424f747f62e04e8c34fde60013fb4dbc04b@65.108.0.165:14956,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,73c2a86cc0d4b51c81bd0e36cee69f1731bcda0d@23.88.69.157:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,222385f3ce7f55f9c01c23f2ee340ed9548b18fa@35.222.169.98:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@154.53.32.78:26656,1997e68bf205bedeed0c4723786bf03464987dc1@77.87.108.21:26656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,2e470eb2dfd65ffa34a9ae2d73646f82c6e594b7@65.108.10.36:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
