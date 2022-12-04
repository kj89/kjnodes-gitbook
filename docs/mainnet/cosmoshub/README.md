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
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,8dc4fd0007c74bdf4b7ee1e5a3ab68161cc8f845@142.132.208.213:26656,44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656,61bb33c7869e1d5014c996299a818d816ae961a6@52.77.137.184:26656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,aea820ece7c45c0a8b5dababc9ea813f7eb62638@93.186.201.125:26656,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,5d45bc48f6c0199c047e685fafb4309f53593f37@5.161.119.242:49656,07fc76b0a1dfcd25e3139a339728d50507bb5d96@67.209.54.35:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
