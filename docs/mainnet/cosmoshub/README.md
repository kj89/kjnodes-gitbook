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
peers="8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656,505f4467926cdad29932c44dc5ea7a5da6982f48@176.9.101.44:26656,53b3651680ec3482d736808cbb3035940107f8ab@185.146.148.119:26656,07fc76b0a1dfcd25e3139a339728d50507bb5d96@67.209.54.35:26656,c7a1d95db766b57bbea36ad1db1fc3cb41857fc8@86.111.48.38:26656,ba3bacc714817218562f743178228f23678b2873@34.141.15.99:26656,aea820ece7c45c0a8b5dababc9ea813f7eb62638@93.186.201.125:26656,559d1ca1c9e8a0beb4356be336e3f5613f6997a6@162.55.245.121:26656,60afd908298c1ff249bb8e60e469594c5422473d@136.243.91.221:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
