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
peers="84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656,27ad834c62dbefc5beb74be7575515927bd07c58@193.176.85.151:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,67685d93f2256caa7a2d53e3a104f9e437c3d247@95.216.114.244:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,701036e718d0746d1d7055fb0fd1245cf361e0b8@168.119.79.106:26656,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,60afd908298c1ff249bb8e60e469594c5422473d@136.243.91.221:26656,bba10290da32f3cb41e15c3a192413666ce05cee@23.88.18.129:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
