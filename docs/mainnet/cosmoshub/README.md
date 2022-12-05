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
peers="989f4e22208c3a77bd8b550ce68d8ad23e5bdda7@18.222.251.112:26656,07fc76b0a1dfcd25e3139a339728d50507bb5d96@67.209.54.35:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,e015ce661ca8670e01f38a7a05c19311658a25e8@35.186.181.152:26656,559d1ca1c9e8a0beb4356be336e3f5613f6997a6@162.55.245.121:26656,aea820ece7c45c0a8b5dababc9ea813f7eb62638@93.186.201.125:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,2122aa0409c6ccd7845e23eb6adb12f1d276665e@34.88.247.213:26656,eebc7a0257c91306b38fb42924b9292d6dd2951c@51.79.176.202:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
