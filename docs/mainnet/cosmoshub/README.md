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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,2e6f37cfbc4549c23f4ec48e9de68203858b62fc@51.38.52.99:26656,f8ae898b130457bbbf05fd3d2e9ca4559bd528fd@37.120.245.157:26656,34f0e424f747f62e04e8c34fde60013fb4dbc04b@65.108.0.165:14956,e015ce661ca8670e01f38a7a05c19311658a25e8@35.186.181.152:26656,58b31074c33d34e96c35e071dc97fc1a82410df3@161.97.142.147:26656,eebc7a0257c91306b38fb42924b9292d6dd2951c@51.79.176.202:26656,915a5d104236764e33d5f7fd8d6c946e66766723@34.74.124.82:26656,52a6b8f416ba3ed2aafa72e35df28ee4c3ee547b@5.9.108.156:36656,8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
