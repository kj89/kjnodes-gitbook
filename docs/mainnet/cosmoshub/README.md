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
peers="88b03d0ae562ec55414bef4b3e0073bb16933938@18.138.176.63:26656,84cc83cd09a974a234a3fdb5bb4fd46fd856f8ec@142.132.135.239:26656,89c643c1f8bee0eaa680a304eb067905df986643@95.217.122.233:26656,d9dbd30f7e9ae99dc05645f48f4637c2f4a14645@34.107.9.71:26656,44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,b4df042182f7c4e1ebcc537e721b9d7f0f8d9c76@51.15.82.190:26656,a35cc47b1025162b82b2220fb7dd20a438866742@157.90.93.245:26656,241b17dba97a2ed3c3747d12781fb86c9706e2d4@89.58.27.86:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gaia/config/config.toml
```
