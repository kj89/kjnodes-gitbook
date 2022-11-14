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
peers="da48fde15b0290a8eee6c6f0dc9bca658f73d361@65.108.200.49:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,53b3651680ec3482d736808cbb3035940107f8ab@185.146.148.119:26656,d9dbd30f7e9ae99dc05645f48f4637c2f4a14645@34.107.9.71:26656,61bb33c7869e1d5014c996299a818d816ae961a6@52.77.137.184:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@154.53.32.78:26656,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,60afd908298c1ff249bb8e60e469594c5422473d@136.243.91.221:26656,a6419bba2180d6f210bcfb67e193dbe00246e004@168.119.147.148:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaiad/config/config.toml
```
